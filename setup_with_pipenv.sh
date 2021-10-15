#!/bin/bash


PIPENV=$(dpkg -s pipenv)

if [ "$PIPENV" ];

    then

        echo 'Pipenv found. Starting to setting up environment with pipenv.'
            pipenv install
            pipenv shell
            exit 0

fi
