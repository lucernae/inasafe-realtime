# coding=utf-8
import logging
import os

from PyQt4.QtCore import QObject
from qgis.core import QgsRasterLayer
from realtime.utilities import get_grid_source, realtime_logger_name

from realtime.earthquake.localizations import ShakeHazardString
from realtime.earthquake.settings import EQ_GRID_SOURCE_TYPE
from safe.gui.tools.shake_grid.shake_grid import ShakeGrid, USE_ASCII

LOGGER = logging.getLogger(realtime_logger_name())


class ShakeHazard(QObject):
    """Class placeholder for Shakemap hazard object."""

    def __init__(
            self, grid_file=None, force_flag=False, algorithm=USE_ASCII,
            output_dir=None, output_basename=None):
        """Create Shake Hazard event placeholder object.

        :param grid_file: filepath of grid.xml
        :type grid_file: str

        :param force_flag: set True to force overwrite
        :type force_flag: bool

        :param algorithm: MMI generation algorithm (based on InaSAFE core)
        :type algorithm: str

        :param output_dir: optional output location
        :type output_dir: str

        :param output_basename: optional output basename
        :type output_basename: str
        """
        super(ShakeHazard, self).__init__()
        self.localization = ShakeHazardString()
        self.grid_file = grid_file
        if not output_dir:
            output_dir = os.path.dirname(grid_file)
        if not output_basename:
            output_basename = 'hazard'

        self._shake_grid = ShakeGrid(
            '', get_grid_source(), self.grid_file,
            output_dir=output_dir,
            output_basename=output_basename)
        self.hazard_path = self.shake_grid.mmi_to_raster(
            force_flag=force_flag, algorithm=algorithm)
        self.source_type = EQ_GRID_SOURCE_TYPE

    @property
    def shake_grid(self):
        """
        :return: ShakeGrid object
        :rtype: ShakeGrid
        """
        return self._shake_grid

    @property
    def source(self):
        """
        :return: Source of grid
        :rtype: str
        """
        return self.shake_grid.source

    @property
    def event_id(self):
        """
        :return: Event ID of shake
        :rtype: str
        """
        return self.shake_grid.event_id

    @property
    def latitude(self):
        """
        :return: Latitude of shake location
        :rtype: float
        """
        return self.shake_grid.latitude

    @property
    def longitude(self):
        """
        :return: Longitude of shake location
        :rtype: float
        """
        return self.shake_grid.longitude

    @property
    def location(self):
        """
        :return: Human friendly name of location
        :rtype: float
        """
        return self.shake_grid.location

    @property
    def timestamp(self):
        """
        :return: timestamp of event with timezone
        :rtype: datetime.datetime
        """
        return self.shake_grid.time

    @property
    def magnitude(self):
        """
        :return: Magnitude of shake
        :rtype: float
        """
        return self.shake_grid.magnitude

    @property
    def depth(self):
        """
        :return: Depth of shake
        :rtype: float
        """
        return self.shake_grid.depth

    @property
    def time_zone(self):
        """
        :return: Timezone string of shake timestamp
        :rtype: float
        """
        return self.shake_grid.time_zone

    @property
    def hazard_exists(self):
        """Make sure hazard layer generated
        :return: True if hazard exists
        :rtype: bool
        """
        # Perform other checks to make sure hazard file is complete
        return os.path.exists(self.hazard_path)

    @property
    def hazard_layer(self):
        """
        :return: QGIS Layer of Hazard file
        :rtype: QgsRasterLayer
        """
        return QgsRasterLayer(self.hazard_path)

    def is_valid(self):
        """Validate InaSAFE Layer generation."""
        if self.hazard_exists and self.hazard_layer.isValid():
            return True
        return False
