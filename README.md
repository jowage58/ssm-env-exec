# ssm-env-exec

Pass AWS SSM parameters as environment variables when executing a process

# Usage

    pip install -e .

You can now use the `ssmenv2exec` script from the command line to execute your process
and have it environment built from an AWS SSM Parameter store path.

    ssmenv2exec /app/mywebsite python app.py
