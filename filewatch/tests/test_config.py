import os

from filewatch.config import settings, get_config

class TestConfig(object):
    def test_default_file_parsing(self):
        """Do we obtain expected defaults?"""
        assert settings.get('DEFAULT', 'interval') is not None

    def test_env_finder(self):
        """Can we find a config file from an env setting?"""
        dir_name = os.path.dirname(__file__)
        env_name = 'MY_TEST_CONFIG'
        conf_name = 'conf.ini'

        os.environ[env_name] = os.path.join(dir_name, conf_name)
        test_settings = get_config(config_name=conf_name, env_name=env_name)

        assert test_settings.get('DEFAULT', 'foo') == 'bar'
