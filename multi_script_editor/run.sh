#!/bin/bash
CURRENT=`dirname $(readlink -f $0)`
python "$CURRENT/scriptEditor.py"
