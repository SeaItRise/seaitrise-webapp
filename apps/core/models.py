# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.contrib.gis.db import models


class File(models.Model):
    fileid = models.AutoField(primary_key=True)
    filename = models.TextField()
    coordinates = models.PointField()
    localtimestamp = models.DateTimeField()
    utc_timestamp = models.DateTimeField()
    file_url = models.TextField()
