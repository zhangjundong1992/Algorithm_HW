#!F:\Python\Algorithm\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==19.0.work3','console_scripts','pip3'
__requires__ = 'pip==19.0.work3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==19.0.work3', 'console_scripts', 'pip3')()
    )
