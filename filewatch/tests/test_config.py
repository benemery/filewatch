from filewatch.config import settings

class TestConfig(object):
    def test_default_file_parsing(self):
        """Do we obtain expected defaults?"""
        assert settings.get('DEFAULT', 'interval') is not None
