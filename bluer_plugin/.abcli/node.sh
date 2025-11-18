#! /usr/bin/env bash

function bluer_plugin_node() {
    local task=$1

    local function_name=bluer_plugin_node_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    bluer_ai_log "@plugin: node: 🌀"

    # or

    bluer_ai_log_error "@plugin: node: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /node
