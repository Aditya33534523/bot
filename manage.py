#!/usr/bin/env python
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import CGI fix BEFORE any Django imports
import cgi_fix

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_platform.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('Could not import Django') from exc
    execute_from_command_line(sys.argv)