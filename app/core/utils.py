import os
import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.owner.id, "portrait", ext)
    return os.path.join('portraits', filename)


def image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    random_string = generate_random_string()
    filename = "%s-%s.%s" % (instance.name, random_string, ext)
    return os.path.join('charity', filename)


def schedule_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.name, instance.id, ext)
    return os.path.join('schedules', filename)
