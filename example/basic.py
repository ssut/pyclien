# coding: utf-8
from __future__ import print_function
import os
import sys

try:
    from clien import Session
except:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from clien import Session

def main():
    clien = Session()
    success = False
    if not os.path.exists('session.tmp'):
        success, reason = clien.login(username='', password='')
        if success:
            clien.save_session('session.tmp')
        else:
            print(reason)
    else:
        success, reason = clien.login(sessionpath='session.tmp')
    print(u'로그인 결과:', success)


if __name__ == '__main__':
    main()
