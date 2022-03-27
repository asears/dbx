import logging

from path import Path

from dbx.utils.common import InfoFile, read_json
from dbx.constants import INFO_FILE_PATH
from .utils import DbxTest


class UtilsTest(DbxTest):
    def test_default_initialize(self):
        with self.project_dir:
            InfoFile.initialize()
            init_content = read_json(INFO_FILE_PATH)
            self.assertEqual(init_content.get("environments"), {})

    def test_non_empty_behaviour(self):
        with self.project_dir:
            logging.info(self.project_dir)
            InfoFile.initialize()
            self.assertTrue(Path(".dbx").exists())
            InfoFile.update({"environments": {"new-env": "payload"}})
            InfoFile.initialize()
