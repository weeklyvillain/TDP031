#!/bin/bash
set -- "arg 1" "arg 2" "arg    3"

for word in "$@"; do echo $word; done

echo

for word in "$*"; do echo $word; done

echo 
# "$@" Makes linebreaks between the args, "$*" does not make linebrakes
# If we do it like this the spaces are also preserved:
for word in "$@"; do echo "$word"; done
