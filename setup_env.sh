#!/bin/bash


PIPENV=$(dpkg -s pipenv)
PIP=$(dpkg -s pip)


if [ "$PIPENV" ];

    then

        echo 'Pipenv found. Starting to setting up environment with pipenv.'
            pipenv install
            pipenv shell
            exit 0

elif [ "$PIP" ];

    then
        echo 'Why are you using pip?'
fi
