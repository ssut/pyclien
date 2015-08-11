# coding: utf-8
""":mod:`clien.utils` ---
~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import re

RE_INT = re.compile(r'([0-9,]+)', re.MULTILINE)

def intfromstr(text):
    """문자열에서 숫자를 찾아 int형으로 변환환 후 반환

    :param str text: 대상 문자열"""
    result = None
    matches = RE_INT.search(text)
    if matches:
        result = matches.group().replace(',', '')
        try:
            result = int(result)
        except ValueError:
            result = None

    return result
