#! /usr/bin/env bash

function test_bluer_plugin_thing() {
    local options=$1

    local test_options=$2

    bluer_ai_eval ,$options \
        "echo 📜 bluer-plugin: test: thing: $test_options: ${@:3}."
}
