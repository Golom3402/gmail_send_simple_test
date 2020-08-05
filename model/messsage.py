# -*- coding: utf-8 -*-


class Message:

    def __init__(self, address=None, subject=None, body_message=None):
        self.address = address
        self.subject = subject
        self.body_message = body_message

    def __repr__(self):
        return "%s:%s:%s" % (self.address, self.subject, self.body_message)
