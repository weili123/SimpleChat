# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MessageStream(models.Model):
    message_stream_id = models.AutoField(primary_key=True)
    message_timestamp = models.DateTimeField()
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    message = models.CharField(max_length=500)


class User(models.Model):
    user_name = models.CharField(max_length=20)

    @property
    def user_id(self):
        return self.id