"""
WSGI config for vercel_app project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

# 19-10-2025 - Start - Settings for wsgi.py by Web Tab
# import sys

# from dotenv import load_dotenv
# project_folder = os.path.expanduser('~/mysite')  # adjust as appropriate
# load_dotenv(os.path.join(project_folder, '.env'))

# Add your project directory to the sys.path
# project_home = '/home/persteen/mysite'
# if project_home not in sys.path:
#    sys.path.insert(0, project_home)
# 19-10-2025 - End - Settings for wsgi.py by Web Tab

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = get_wsgi_application()
