import logging
from typing import Mapping

import boto3

logger = logging.getLogger('ssmenv2exec.ssm')


def get_params_by_path(param_path: str, *, path_sep: str = '/') -> Mapping[str, str]:
    """Returns a mapping of parameters under the given path."""
    ssm_client = boto3.client('ssm')
    params = ssm_client.get_parameters_by_path(
        Path=param_path,
        WithDecryption=True,
    )
    if not params['Parameters']:
        logger.warning('No parameters found for path [%s]', param_path)
    return {
        param['Name'].rsplit(path_sep, maxsplit=1): param['Value']
        for param in params['Parameters']
    }
