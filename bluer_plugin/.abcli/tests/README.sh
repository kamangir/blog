#! /usr/bin/env bash

function test_bluer_plugin_README() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_plugin build_README
}
