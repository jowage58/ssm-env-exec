import unittest

import ssmenv2exec


class TestParameterParsing(unittest.TestCase):

    def test_parse_empty(self):
        params = ssmenv2exec.parse_ssm_params([], path_sep='/')
        self.assertDictEqual(params, {})

    def test_parse_none(self):
        self.assertRaises(TypeError, ssmenv2exec.parse_ssm_params, None, path_sep='/')
