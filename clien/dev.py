# coding: utf-8
""":mod:`clien.dev` --- Developer Tools for Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from __future__ import print_function

def report(*args):
    print(u"""아래 텍스트를 복사하여 이슈 트래커에 보고해주시면 이 오류에 대한 해결 방안을 찾을 수 있게 됩니다.
:주의: 중요한 정보가 내용에 포함되어 있다면 반드시 제거해주세요. 한 번 등록한 이슈는 삭제할 수 없습니다. (수정만 가능)
https://github.com/ssut/pyclien/issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{}""".format("\n".join(args)))
