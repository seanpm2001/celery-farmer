from __future__ import absolute_import


def get_tags(task):
    return {
        "name": task.name,
        "worker": task.hostname,
    }
