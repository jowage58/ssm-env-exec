import logging
import os
import sys

import ssmenv2exec.ssm

logger = logging.getLogger('ssmenv2exec.main')


def main() -> None:
    if len(sys.argv) < 3:
        print('Usage:')
        print('\tssmenv2env /app/cas/ java -jar some.jar\n')
        sys.exit(1)
    params = ssmenv2exec.ssm.get_params_by_path(sys.argv[1])
    env = os.environ
    for k, v in params.items():
        if not env.get(k):
            env[k] = v
        else:
            logger.warning('Env var [%s] already exists, skipping', k)
    args = sys.argv[2:]
    os.execvpe(args[0], args, env)


if __name__ == '__main__':
    main()
