import sqlite3
import unittest
import uuid
from os.path import dirname, join

from qgis.core import QgsCoordinateReferenceSystem
from qgis.utils import iface
from .utilities import get_qgis_app
from aequilibrae_menu import AequilibraEMenu


class OpenMainDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        _ = get_qgis_app()

    def test_if_dialog_opens(self):
        """Test we can click OK."""

        self.dialog = AequilibraEMenu(iface)


if __name__ == "__main__":
    suite = unittest.makeSuite(OpenMainDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)