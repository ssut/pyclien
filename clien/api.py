# coding: utf-8
""":mod:`clien.api` --- CLIEN API Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from clien.api import ClienAPI

class ClienAPI(object):
    """클리앙 API 클래스.
    클리앙 API 구현을 포함합니다."""

    def __init__(self, *args, **kwargs):
        raise NotImplemented(u'ClienAPI 클래스는 Session 클래스에 상속되어야 합니다.')
