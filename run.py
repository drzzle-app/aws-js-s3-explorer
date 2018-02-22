import sys
import time
import subprocess
import traceback
import shlex


def cmd(command):
    proc = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        out = proc.stdout.readline()
        if out == '' and proc.poll() is not None:
            break
        if out:
            print(out.strip())
        rtn = proc.poll()
        return rtn


print('Starting reverse proxy for s3 and webserver')
cmd('mitmdump -R http://localstack:4572 -p 4572')
cmd('python -m http.server 8001')

try:
    while True:
        time.sleep(1)
except Exception as e:
    print(traceback.format_exc())

sys.exit(1)
