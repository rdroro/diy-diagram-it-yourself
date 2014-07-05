#!/bin/bash
export PYTHONPATH=../bin:{PYTHONPATH}
python -m unittest discover -s unit-test -p 'Test*'