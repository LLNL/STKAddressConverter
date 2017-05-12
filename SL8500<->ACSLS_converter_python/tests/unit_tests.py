#!/usr/bin/env python
#
# Huy Le
# 01/11/2017
#
# Unit testing that tests the address translation of acs2internal.
#

from unittest import TestCase, main
from os import path as os_path
from sys import path as sys_path

# Find the directory where unit_test.py is.
TESTS_DIR = os_path.dirname(os_path.realpath(__file__))
sys_path.insert(0, TESTS_DIR + "/../")

from acs2internal import acs2internal

class UnitTests(TestCase):
    """Unit tests for acs2internal.py.
    """

    def test_run_command(self):
        """Utility function that runs arbitrary commands.
        """
        assert acs2internal.run_command("ls", 1, "ls")

    def test_acsls_to_internal(self):
        """Equivalent to `python acs2internal.py -d 1,10,1,4`
           ACSLS address to internal address.
        """
        self.assertEqual("3,3,-1,1,1",
                         acs2internal.acsls_addr_to_internal_addr( \
                         acs_address="1,10,1,4"))

    def test_internal_to_acsls(self):
        """Equivalent to `python acs2internal.py -i 3,3,-1,1,1`
           Internal address to acsls address.
        """
        self.assertEqual("1,10,1,4",
                         acs2internal.internal_addr_to_acsls_addr( \
                         internal_address="3,3,-1,1,1"))

if __name__ == "__main__":
    main()
