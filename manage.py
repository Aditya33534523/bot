#!/usr/bin/env python
import os
import sys

# Fix for Python 3.13 compatibility with Django 3.2
try:
    import cgi_fix
except ImportError:
    pass

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_platform.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('Could not import Django') from exc
    execute_from_command_line(sys.argv)
