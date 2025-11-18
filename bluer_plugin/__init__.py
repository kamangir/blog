NAME = "bluer_plugin"

ICON = "🌀"

DESCRIPTION = f"{ICON} A git template for a bluer-ai plugin."

VERSION = "4.54.1"

REPO_NAME = "bluer-plugin"

MARQUEE = "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true"

ALIAS = "@plugin"


def fullname() -> str:
    return f"{NAME}-{VERSION}"
