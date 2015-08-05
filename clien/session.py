# coding: utf-8
""":mod:`clien.session` --- CLIEN Session Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import requests

from clien.api import ClienAPI
from clien.constants import CLIENM_URL

class Session(ClienAPI):
    """클리앙 세션 객체.
    :class:`requests.Session`를 이용해 세션을 유지하며 모든 API를 포함합니다."""

    def __init__(self, username=None, password=None, sessionpath=None):
        if not sessionpath and username and password:
            pass

