import os
import random
import string

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.owner.id, "portrait", ext)
    return os.path.join('portraits', filename)


def image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.id, "schedule", ext)
    return os.path.join('charity', filename)

def schedule_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.name, instance.id, ext)
    return os.path.join('schedules', filename)