#!F:\py1814aixianfeng\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hex==2.0.0','console_scripts','hex'
__requires__ = 'hex==2.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hex==2.0.0', 'console_scripts', 'hex')()
    )
