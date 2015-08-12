# coding: utf-8
""":mod:`clien.api` --- CLIEN API Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import os
import pickle
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from clien.constants import CLIENM_URL, CLIENM_URI
from clien.constants import REGEXP
from clien.dev import report
from clien.classes import ClienProfile
from clien.utils import intfromstr

class ClienAPI(object):
    """클리앙 API 클래스.
    클리앙 API 구현을 포함합니다."""

    def __init__(self, *args, **kwargs):
        raise NotImplemented(u'ClienAPI 클래스는 Session 클래스에 상속되어야 합니다.')

    def login(self, username=None, password=None, sessionpath=None):
        """클리앙에 로그인합니다.
        아이디 + 비밀번호 조합으로 넘기거나 세션 파일을 미리 저장해둔 경우 세션 파일 경로를 넘기면 됩니다.

        :param str username: 클리앙 아이디
        :param str password: 클리앙 비밀번호
        :param str sessionpath: (저장한 세션이 존재하는 경우) 세션 파일 경로"""
        session = None
        result = False
        reason = ''

        if sessionpath:
            if not os.path.exists(sessionpath):
                raise IOError(u'존재하지 않는 세션 파일입니다: '.format(sessionpath))
            with open(sessionpath, 'r') as f:
                cookies = pickle.load(f)
            if not cookies:
                raise IOError(u'유효하지 않은 세션 파일입니다: '.format(sessionpath))
            self.session = requests.Session()
            self.session.cookies = cookies
            result = self.check_logged()

        if username and password:
            session = requests.Session()
            payload = {
                'url': CLIENM_URL,
                'mb_id': username,
                'mb_password': password,
            }
            r = session.post(CLIENM_URI.SIGNIN, data=payload)
            r.encoding = 'utf-8'
            if 'history.go(-1);' in r.text:
                result = False
                reason = REGEXP.ALERT_CONTENT.search(r.text).groups()[0]
            else:
                result = True
            result = self.check_logged(r.text)
            self.session = session

        # 로그인 아이디 가져오기
        if sessionpath and result:
            r = self.session.get(CLIENM_URL)
            r.encoding = 'utf-8'
            try:
                content = BeautifulSoup(r.text, 'lxml')
                script = content.select('header + div + script')[0].string
            except:
                result = False
                reason = u'로그인 계정을 가져오지 못했습니다.'
            else:
                username = REGEXP.SCRIPT_ISLOGIN.search(script).groups()[0]
                self.username = username
        else:
            self.username = username
        self.update_profile()

        return (result, reason, )

    def check_logged(self, content=None):
        """로그인 여부를 확인합니다.

        :param str content: 미리 요청한 리퀘스트가 존재하는 경우 이 파라미터로 전달
        """
        result = False

        if not content:
            r = self.session.get(CLIENM_URL)
            r.encoding = 'utf-8'
            content = r.text

        # 로그인 직후 시도했을 때
        if '?nowlogin=1' in content:
            result = True
        else:
            content = BeautifulSoup(content, 'lxml')
            try:
                btntext = content.select('header h1 + button')[0].text
            except IndexError:
                report(content)
                raise ValueError(u'로그인 상태를 확인할 웹 객체를 찾지 못했습니다.')
            if btntext == u'로그인':
                result = False
            elif btntext == u'로그아웃':
                result = True

        return result

    def update_profile(self):
        """로그인된 계정의 정보를 업데이트합니다."""
        assert self.username
        self.profile = self.get_userinfo(self.username)
        return self.profile

    def get_userinfo(self, username):
        """특정 사용자의 정보를 가져옵니다.

        :param str username: 사용자 아이디
        """
        assert self.session

        result = False
        reason = ''

        url = CLIENM_URI.PROFILE.format(username=username)
        r = self.session.get(url)
        r.encoding = 'utf-8'
        alerts = REGEXP.ALERT_CONTENT.search(r.text)
        if alerts:
            reason = alerts.groups()[0]
        else:
            content = BeautifulSoup(r.text, 'lxml')
            nick = content.select('body > table')[0].select('span.member')[0].string
            rows = content.select('body > table')[1].select('table')[2].select('tr td')
            since, last_logged = rows[7].string.split(' : ')[-1], rows[10].string.split(' : ')[-1]
            since = datetime.strptime(since, r'%Y-%m-%d')
            last_logged = datetime.strptime(last_logged, r'%Y-%m-%d %H:%M:%S')
            info = {
                'username': username,
                'nickname': nick,
                'level': intfromstr(rows[1].string),
                'point': intfromstr(rows[4].string),
                'since': since,
                'last_logged': last_logged,
            }
            result = ClienProfile(**info)

        return (result, reason, )
