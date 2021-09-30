# my_tools_provider.py

from processing_provider.example_processing_algorithm import \
    ExampleProcessingAlgorithm
from qgis.core import QgsProcessingProvider
from .tools.clip_layer import ClipLayer

from PyQt5.QtGui import QIcon
from os import path

class MyToolsProvider(QgsProcessingProvider):

    
    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(ClipLayer())

    def id(self, *args, **kwargs):
        """The ID of your plugin, used for identifying the provider.
        """
        return 'mytools'

    def name(self, *args, **kwargs):
        """The human friendly name of your plugin in Processing.
        """
        return self.tr('My Tools')

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
       return QIcon(path.dirname(__file__) + '/icon.png')

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers.
        """

        return self.name('Collection of my custom tools')
