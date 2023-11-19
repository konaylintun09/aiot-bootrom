# SPDX-License-Identifier: MIT

import pkg_resources
import platform
import subprocess
import sys

def main():
    bin_name = 'bin/bootrom-tool'
    if platform.system() == "Windows":
        bin_name += ".exe"

    binary = pkg_resources.resource_filename('aiot_bootrom', bin_name)
    sys.argv[0] = binary

    try:
        subprocess.run(sys.argv, check=True)
    except KeyboardInterrupt:
        pass
