#! /usr/bin/env bash

bluer_ai_source_caller_suffix_path /tests

bluer_ai_env_dot_load \
    caller,plugin=bluer_plugin,suffix=/../..

bluer_ai_env_dot_load \
    caller,filename=config.env,suffix=/..
