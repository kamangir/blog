from bluer_options.env import load_config, load_env, get_env

load_env(__name__)
load_config(__name__)


BLUER_PLUGIN_SECRET = get_env("BLUER_PLUGIN_SECRET")

BLUER_PLUGIN_CONFIG = get_env("BLUER_PLUGIN_CONFIG")
