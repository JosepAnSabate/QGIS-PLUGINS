import math
from qgis.core import QgsFeatureRequest

def dc_summarizePoly(poly, lyrPoint, fldSpecies):
    ####################################################
    #
    # Function imputs parameters:
    #   poly = a single polygon QgsFeature
    #   lyrPoint = a QgsVectorLayer containing points. Each point
    #               represents a single observation of a species.
    #   fldSpecies = a string containing the name of the field
    #               in the points layer that contains the name of
    #               the species.
    #
    # The purpose of the function is to summarize the number of
    # observations of each species inside the polygon in the form of a
    # dictionary containing species as keys and the number of observations as values.

    dctPoly = {}

    # loop through all the points that intersect the polygons bounding box
    for obs in lyrPoint.getFeatures(QgsFeatureRequest(poly.geometry().boundingBox())):
        # check to see if the points is actually inside the polygon
        if poly.geometry().contains(obs.geometry()):
            # get the name of the species as a string variable
            sSpecies = obs.attribute(fldSpecies)
            # check to see if species already has an entry in the dictionary
            if sSpecies in dctPoly.keys():
                # if it does, increase the count 1
                dctPoly[sSpecies] += 1
            else:
                # if there is no entry for the species, create it and set its
                # initialvalue to 1
                dctPoly[sSpecies] = 1

    return dctPoly

def dc_mergeDictionaries(dctMain, sCategory, dctPoly):
    ########################################################
    #   This function take the as inputs the following parameters:
    #       dctMain = a dictionary with categories as the key and another
    #           dictionary containing summary information as the value.
    #       sCategory = a string containing the name of the category to be merged
    #       dctPoly = a string containing summary information for a polygon
    #               (created by the dc_processPoly function). The keys are the
    #               names of the species occurring in the polygon and the values
    #               are the number of observations of that species in the polygon
    #
    #   The purpose of the function is to merge the species counts from dctPoly
    #   into the appropiate summary information in dctMain.

    #   check to see if the category exists in the dctMain dictionary
    if sCategory in dctMain.keys():
        # if it does then loop through the summary data in dictpoly
        for species, obs in dctPoly.items():
            # check to see if there is already an entry for the species in this category
            if species in dctMain[sCategory].keys():
                # if there is then add the number of observations in the summary data
                dctMain[sCategory][species] += obs
            else:
                # if there isn't create a new entry for the species and set
                # the number of observations as the initial value
                dctMain[sCategory][species] = obs
    else:
        # if doesn't create a new entry for the category with the summary
        # dictionary as the initial value
        dctMain[sCategory] = dctPoly

    return dctMain

def dc_richness(dict):
    #######################################################################
    #
    #   This function take as inputs the following parameters:
    #       dict = a dictionary containing summary information for a polygon
    #           The keys are the names of the species occuring in the polygon
    #           and the values are the number of observations of the species
    #           in the polygon.
    #
    #   The purpose of the function is to calculate the species richness from the dict
    #   provideed above, wich is just the total number of species observed or the length
    #   of the dictionaries.

    return len(dict)

def dc_shannons(dict):
    ############################################################################
    #
    #   This function takes as inputs the following parameters:
    #       dict = a dictionary containing summary information for a polygon
    #           The keys are the names of the species occuring in the polygon
    #           and the values are the number of observations of the species
    #           in the polygon.
    #
    #   The purpose of the function is to calculate shannons diversity index from
    #   the dict provided above.

    # first calculate the total number of observations
    total = sum(dict.values())

    # set the initial value to 0
    shannons = 0;

    # loop through all the species counts in the dictionary
    for count in dict.values():
        # calculate proportion of total observations
        prop = count/total

        shannons += prop*math.log(prop)
    return abs(shannons);

def dc_simpsons(dict):
############################################################################
#
#   This function takes as inputs the following parameters:
#       dict = a dictionary containing summary information for a polygon
#           The keys are the names of the species occuring in the polygon
#           and the values are the number of observations of the species
#           in the polygon.
#
#   The purpose of th3e function is to calculate simpsons diversity index from
#   the dictionary provided above

    # first calculate the total number of observations
    total = sum(dict.values())

    # set the initial value to 0
    simpsons = 0;


    # loop through all the species counts in the dictionary
    for count in dict.values():
        # calculate proportion of total observations
        prop = count/total

        simpsons += prop * prop
    return simpsons;

def dc_evenness(dict):
    ############################################################################
    #
    #   This function takes as inputs the following parameters:
    #       dict = a dictionary containing summary information for a polygon
    #           The keys are the names of the species occuring in the polygon
    #           and the values are the number of observations of the species
    #           in the polygon.
    #
    #   The purpose of th3e function is to calculate the species evenness index from the dictionary provided above.
    #   Evenness will be 1 when all the species have the same number of observations and lower values as some species
    #   have greater number of observations than others

    # maximum value that Shannons index can be is the log of the total number of species (richness)
    max = math.log(dc_richness(dict))
    return dc_shannons(dict)/max

def dc_resultString(dict):
    result = ""
    for category, summary in dict.items():
        result += "{}: {} {:2.3f} {:2.3f} {:2.3f}\n".format(category, dc_richness(summary), dc_shannons(summary), dc_simpsons(summary), dc_evenness(summary))
    return result

def dc_resultHTML(dict, sLayer, sCategory, bDetail=True):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Diversity Calculator</title>
            <style>
                table, th, td {
                    border: 1px solid black;
                }
            </style>
        </head>
        <body>
            <h1>Diversity Calculator output</h1>
            <h2>""" + sLayer + ": " + sCategory + """</h2>
            <table>
                <tr>
                    <th> Name </th><th> Count </th><th> Richness </th><th> Evenness </th><th> Shannons H' </th><th> Simpsons D </th>
                <tr>
    """
    for category in sorted(dict.keys()):
        summary = dict[category]
        #html += "   <td>\n"
        html += "       <td>" + category + "</td>"
        html += "<td>" + str(sum(summary.values())) + "</td>"
        html += "<td>" + str(dc_richness(summary)) + "</td>"
        html += "<td>" + "{:3.3f}".format(dc_evenness(summary)) + "</td>"
        html += "<td>" + "{:3.3f}".format(dc_shannons(summary)) + "</td>"
        html += "<td>" + "{:3.3f}".format(dc_simpsons(summary)) + "</td> <tr>" # tr brak line

    html += """
            </table>
            """
    if bDetail:
        html += """
        <h2>Raw Data</h2>
        <table>
            <tr>
                <th> Name </th><th> Species </th><th> Observations </th>
            <tr>
        """
        for category in sorted(dict.keys()):
            for species, obs in dict[category].items():
                html += "       <tr>\n"
                html += "   <td>" + category + "</td>"
                html += "<td>" + species + "</td>"
                html += "<td>"+ str(obs) + "</td>\n"
                html += "       </tr>\n"
        html += """
        </table> """
        html += """
        </body>
    </html>
    """

    return html




