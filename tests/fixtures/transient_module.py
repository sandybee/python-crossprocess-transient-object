#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from crossprocess.objects import SimpleObject

so = SimpleObject(os.path.basename(__file__).replace('.py', ''))

print(so.get_name())
