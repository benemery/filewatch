import os
import hashlib

class Watcher(object):
    def __init__(self):
        # A map of filepath keys to their last modified date
        self.files = {}

        self._first_run = True

    def run(self, start_directory=None):
        """Run a check over filesytem.

        :note: If no start directory is supplied then we will begin walking
        from the current working directory.
        """
        if not start_directory:
            start_directory = os.getcwd()

        for dirpath, dirnames, filenames in os.walk(start_directory):
            for filename in filenames:
                broadcast_required = False
                full_path = os.path.join(dirpath, filename)
                key = self._get_key(full_path)

                file_modified = os.path.getmtime(full_path)

                try:
                    last_changed = self.files[key]

                    broadcast_required = last_changed < file_modified
                except KeyError:
                    # We have not seen this file before, add it our dict and
                    # broadcast
                    self.files[key] = file_modified

                    broadcast_required = not self._first_run

                if broadcast_required:
                    # Tell our observer about this file
                    pass

        # Keep track of state
        self._first_run = False

    def _get_key(self, full_path):
        """Build a checksum used to identify this filepath"""
        full_path_checksum = hashlib.sha1(full_path).digest()
        return full_path
