# coding: utf-8
""":mod:`clien.session` --- CLIEN Session Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import os
import pickle

import requests

from clien.api import ClienAPI
from clien.constants import CLIENM_URL

class Session(ClienAPI):
    """클리앙 세션 객체.
    :class:`requests.Session`를 이용해 세션을 유지하며 모든 API를 포함합니다."""

    def __init__(self, username=None, password=None, sessionpath=None):
        self.session = requests.Session()
        if not sessionpath and username and password:
            success, reason = self.login(username=username, password=password)
            print(reason)

    def save_session(self, path):
        """세션 정보를 저장합니다.

        :param str path: 저장할 경로
        :return: 저장 성공여부"""
        with open(path, 'w') as f:
            print(self.session.cookies)
            pickle.dump(self.session.cookies, f)
        result = os.path.exists(path)
        return result
