import ConfigParser
import os

def get_config(config_name, env_name=None):
    if not env_name:
        env_name = '%s_CONF' % config_name.split('.')[0]

    config = ConfigParser.RawConfigParser()

    path_to_config = os.path.join(os.path.dirname(__file__), config_name)

    home_path = os.path.expanduser('~/.%s' % config_name)
    paths = [path_to_config, home_path, ]

    if env_name in os.environ:
        paths.append(os.environ[env_name])

    config.read(paths)

    return config

settings = get_config(config_name='filewatch.ini')