#!/bin/bash

# Add profile pages only
git add static/profiles/e/*
if [ $1 == "add" ]
then
    git commit -m "Register user profile ${2}."
elif [ $1 == "update" ] 
then
    git commit -m "Update user profile ${2}."
fi
git push origin master
