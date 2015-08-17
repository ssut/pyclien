# coding: utf-8
""":mod:`clien.classes` --- Classes for CLIEN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

class ClienProfile(object):
    """클리앙 유저 프로필"""

    def __init__(self, username='', nickname='', level=0, point=0, since=None, last_logged=None):
        self.username = username
        self.nickname = nickname
        self.level = level
        self.point = point
        self.since = since
        self.last_logged = last_logged

    def __repr__(self):
        return "<Profile %s(%s)>" % (self.username, self.nickname, )

class ClienArticle(object):
    pass


class ClienComment(object):
    pass


class ClienMessage(object):
    pass
