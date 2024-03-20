from collections import UserDict
from pathlib import Path
from os import environ

class SVTest(UserDict):
    def __init__(self, test_yaml_file, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        """
        Override __setitem__ to allow setting 'test_yaml_file' and 'test_container_name'.
        """
        if key in self._output_keys or key in ['test_yaml_file', 'test_name', 'test_container_name']:
            super().__setitem__(key, value)
        else:
            raise KeyError(f"Key '{key}' is not allowed.")

    def __getitem__(self, key):
        """
        Override __getitem__ to add lazy initialization for output keys.
        """
        if key not in self.data and key in self._output_keys:
            self.data[key] = None
        return super().__getitem__(key)