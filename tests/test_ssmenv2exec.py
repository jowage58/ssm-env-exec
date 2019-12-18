import unittest

import ssmenv2exec


class TestParameterParsing(unittest.TestCase):

    def test_parse_empty(self):
        params = ssmenv2exec.parse_ssm_params([], path_sep='/')
        self.assertDictEqual(params, {})

    def test_parse_none(self):
        self.assertRaises(TypeError, ssmenv2exec.parse_ssm_params, None, path_sep='/')

    def test_parse_params(self):
        params = [
            {'Name': '/app/myapp/DB_PASS',
             'Type': 'String',
             'Value': 'tiger',
             },
            {'Name': '/app/myapp/DB_URL',
             'Type': 'String',
             'Value': 'localhost/orcl',
             },
            {'Name': '/app/myapp/DB_USER',
             'Type': 'String',
             'Value': 'scott',
             },
            {'Name': '/app/myapp/SECRET_KEY',
             'Type': 'SecureString',
             'Value': 'super_secret',
             }
        ]
        expected = {
            'DB_PASS': 'tiger',
            'DB_URL': 'localhost/orcl',
            'DB_USER': 'scott',
            'SECRET_KEY': 'super_secret'
        }
        actual = ssmenv2exec.parse_ssm_params(params, path_sep='/')
        self.assertDictEqual(actual, expected)
