#! /usr/bin/env bash

function bluer_plugin() {
    local task=$1

    if [ "$task" == "task" ]; then
        local options=$2
        local do_dryrun=$(bluer_ai_option "$options" dryrun 0)
        local what=$(bluer_ai_option "$options" what all)

        local object_name_1=$(bluer_ai_clarify_object $3 .)

        bluer_ai_eval dryrun=$do_dryrun \
            python3 -m bluer_plugin \
            task \
            --what "$what" \
            --object_name "$object_name_1" \
            "${@:4}"

        return
    fi

    bluer_ai_generic_task \
        plugin=bluer_plugin,task=$task \
        "${@:2}"
}

bluer_ai_log $(bluer_plugin version --show_icon 1)
