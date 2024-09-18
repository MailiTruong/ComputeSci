#!/usr/bin/env sh

######################################################################
# @author      : mailitg (mailitg@$HOSTNAME)
# @file        : run
# @created     : Wednesday Sep 18, 2024 17:33:11 CEST
#
# @description : 
####################################################################

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 plot.py
