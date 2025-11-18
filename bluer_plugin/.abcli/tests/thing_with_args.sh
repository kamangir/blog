#! /usr/bin/env bash

function test_bluer_plugin_thing_with_args() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    local arg
    for arg in this that; do
        bluer_ai_log "testing arg=$arg ..."

        bluer_ai_eval ,$options \
            echo "🌀 $arg"
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done
}
