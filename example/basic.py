import os
import sys

try:
    from clien import Session
except:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from clien import Session

clien = Session()
print(clien)
