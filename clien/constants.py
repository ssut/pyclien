# coding: utf-8
""":mod:`clien.constants` --- Constants for CLIEN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import re

#: 클리앙 모바일 기본 URL
CLIENM_URL = 'http://m.clien.net/cs3'

class CLIENM_URI(object):
    """클리앙 URI들"""

    SIGNIN = 'https://www.clien.net/cs2/bbs/login_check.php'
    PROFILE = 'http://www.clien.net/cs2/bbs/profile.php?mb_id={username}'
    CMLIST = CLIENM_URL + '/cmMain/index'


class REGEXP(object):
    """정규식"""

    ALERT_CONTENT = re.compile(r'alert\(\'([^\"\']+)', re.MULTILINE)
    SCRIPT_ISLOGIN = re.compile(r'var isLogin = \"([^\"]+)', re.MULTILINE)
