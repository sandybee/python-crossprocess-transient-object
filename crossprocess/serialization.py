#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import base64


class Serializer(object):
    @classmethod
    def serialize(cls, object):
        """
        save a given object into a byte string
        :param object: the object to serialize
        """
        return base64.b64encode(pickle.dumps(object, 2))

    @classmethod
    def deserialize(cls, bstring):
        """
        load a given object from a byte string
        :param bstring: the string to deserialize
        """
        return pickle.loads(base64.b64decode(bstring))
