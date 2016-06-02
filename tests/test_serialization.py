#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crossprocess.serialization import Serializer
from crossprocess.objects import SimpleObject


class TestSerialization(object):
    def new_object(self, name='SimpleObject'):
        """
        helper factory method to create a simple object instance
        """
        return SimpleObject(name)

    def test_serialize(self):
        """
        serialize result is a bytes string
        """
        result = Serializer.serialize(self.new_object())
        assert type(result) is bytes

    def test_deserialize(self):
        """
        deserialize recreate an object with the same internals
        """
        expected = 'my name'
        object = self.new_object(expected)
        result = Serializer.serialize(object)
        assert expected == Serializer.deserialize(result).get_name()
