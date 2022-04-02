#!/bin/bash

export FLASK_APP=app
/home/ubuntu/.local/bin/waitress-serve --port=3000 --call 'app:create_app'