#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

from .serialization import Serializer


def run_script(script, object=None):
    """
    run a given script
    """
    os.environ['PYTHONPATH'] = os.pathsep.join(sys.path)
    if object:
        os.environ[object.__class__.__name__] = Serializer.serialize(
            object).decode()

    proc = subprocess.Popen(
        [sys.executable, script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    result = proc.communicate()

    exit_status = proc.wait()
    if exit_status != 0:
        raise Exception("script failed (exit status: %d)" % exit_status)

    return result
