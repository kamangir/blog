import os

from bluer_options.help.functions import get_help
from bluer_objects import file, README

from bluer_plugin import NAME, VERSION, ICON, REPO_NAME
from bluer_plugin.help.functions import help_functions

items = README.Items(
    [
        {
            "name": f"feature {index}",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",
            "description": f"description of feature {index} ...",
            "url": "./bluer_plugin/docs/feature_{}".format(
                index if index == 1 else f"{index}.md"
            ),
        }
        for index in range(1, 4)
    ]
)


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
            help_function=lambda tokens: get_help(
                tokens,
                help_functions,
                mono=True,
            ),
        )
        for readme in [
            {"path": "..", "items": items},
            {"path": "./docs"},
            # aliases
            {"path": "./docs/aliases"},
            {"path": "./docs/aliases/plugin.md"},
            # features
            {"path": "./docs/feature_1"},
            {"path": "./docs/feature_1/this.md"},
            {"path": "./docs/feature_1/that.md"},
            {"path": "./docs/feature_2.md"},
            {"path": "./docs/feature_3.md"},
        ]
    )
