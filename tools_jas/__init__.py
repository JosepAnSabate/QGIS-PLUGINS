# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ToolsJAS
                                 A QGIS plugin
 Plugin to acces my tools
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-09-29
        copyright            : (C) 2021 by Josep Andreu Sabate
        email                : josep.andreu@e-campus.uab.cat
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ToolsJAS class from file ToolsJAS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tools_jas import ToolsJAS
    return ToolsJAS(iface)


from .clip_layer import ClipLayer
