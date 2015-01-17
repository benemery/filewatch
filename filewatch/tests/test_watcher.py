import os

from filewatch.watcher import Watcher

TEST_DIR = os.path.dirname(__file__)
TEST_DIR_A = os.path.join(TEST_DIR, 'TEST_DIR_A')

class TestWatcher(object):
    def test_file_discory(self):
        """Are we able to find the correct number of files?"""
        watcher = Watcher()
        watcher.run(TEST_DIR_A)

        assert len(watcher.files) == 5

