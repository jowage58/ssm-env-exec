import logging
import os
import sys
from typing import Mapping

import boto3

logger = logging.getLogger('ssmenv2exec.main')


def get_params_by_path(param_path: str, *, path_sep: str = '/') -> Mapping[str, str]:
    """Returns a mapping of parameters under the given path."""
    ssm_client = boto3.client('ssm')
    params = ssm_client.get_parameters_by_path(
        Path=param_path,
        WithDecryption=True,
    )
    if not params['Parameters']:
        logger.warning('No parameters found for path [%s]', param_path)
        return {}
    return {
        param['Name'].rsplit(path_sep, maxsplit=1): param['Value']
        for param in params['Parameters']
    }


def main() -> None:
    if len(sys.argv) < 3:
        print('Usage:')
        print('\tssmenv2env /app/cas/ java -jar some.jar\n')
        sys.exit(1)
    params = get_params_by_path(sys.argv[1])
    env = os.environ
    for k, v in params.items():
        if k not in env:
            env[k] = v
        else:
            logger.warning('Env var [%s] already exists, skipping', k)
    args = sys.argv[2:]
    os.execvpe(args[0], args, env)


if __name__ == '__main__':
    main()
