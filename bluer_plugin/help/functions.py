from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help_leaf(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun,upload"
    args = [
        "[--<keyword-1> <value-1>]",
        "[--<keyword-2> <value-2>]",
    ]

    return show_usage(
        [
            "@plugin",
            "leaf",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "bluer-plugin leaf <object-name>.",
        mono=mono,
    )


def help_task(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "<thing-1+thing-2>|all",
        ]
    )

    return show_usage(
        [
            "@plugin",
            "task",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "task -things-> <object-name>.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "leaf": help_leaf,
        "node": help_node,
        "task": help_task,
    }
)
