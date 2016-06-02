#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from crossprocess.serialization import Serializer
from crossprocess.objects import SimpleObject

if SimpleObject.__name__ not in os.environ:
    sys.exit(1)

print(Serializer.deserialize(
    os.environ[SimpleObject.__name__].encode()).get_name())
