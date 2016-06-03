#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os
import sys
import shutil
import tempfile

from crossprocess.process import run_script
from crossprocess.objects import SimpleObject


class TestCrossprocess(object):

    def get_script(self, name, extension='.py'):
        """
        helper method to get a fixture script
        :param name: script name without extension
        :param extension: script extension
        """
        return os.path.join(
            os.path.dirname(__file__),
            'fixtures',
            name + extension
        )

    def read_from_stdout(self, result):
        """
        helper method to extract the stdout string
        :param result: the result tuple returned from run_script
        """
        return result[0].decode().strip()

    def copy_script(self, script):
        """
        helper method to create a temporary copy of a given script
        :param script: script to copy
        """
        tmpfile = tempfile.NamedTemporaryFile()
        name = tmpfile.name
        tmpfile.close()
        shutil.copyfile(script, name)

        return name

    def test_run_script(self):
        """
        run a simple script
        """
        assert self.get_script('simple') == self.read_from_stdout(
            run_script(self.get_script('simple')))

    def test_run_script_handle_fails(self):
        """
        ensure failing script is handled
        """
        with pytest.raises(Exception):
            run_script(self.get_script('failing'))

    def test_run_script_keeps_sys_path(self):
        """
        cross process sys path
        """
        expected = os.path.join(
            os.path.dirname(__file__),
            'mydir'
        )
        sys.path.append(expected)
        script = self.get_script('syspath')

        assert expected in self.read_from_stdout(run_script(script))

    def test_run_script_permits_transient_module(self):
        """
        project module is accessible from a subprocess
        """
        expected = 'transient_module'
        script = self.get_script(expected)

        assert expected == self.read_from_stdout(run_script(script))

    def test_run_copy_of_script(self):
        """
        project module is accessible from a subprocess even for copy
        """
        script = self.copy_script(self.get_script('transient_module'))
        expected = os.path.basename(script)
        assert expected == self.read_from_stdout(run_script(script))
        os.unlink(script)

    def test_run_script_persistence(self):
        """
        object internal persistence
        """
        script = self.get_script('persistent')
        obj = SimpleObject('persistent')
        assert obj.get_name() == self.read_from_stdout(
            run_script(script, obj))
