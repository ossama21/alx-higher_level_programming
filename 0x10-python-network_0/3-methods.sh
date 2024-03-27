#!/bin/bash
#Displays the allowed methods of a given url
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
