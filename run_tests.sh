#!/bin/bash
coverage run -m pytest test/ && coverage report && coverage html && pylint test/