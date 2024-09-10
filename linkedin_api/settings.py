"""
Settings module for LinkedIn API.

This module sets up various directory paths and environment settings used
by the LinkedIn API scripts, including paths for user data and cookies.
"""

import os
from pathlib import Path

HOME_DIR = str(Path.home())
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LINKEDIN_API_USER_DIR = os.path.join(HOME_DIR, ".linkedin_api/")
COOKIE_PATH = os.path.join(LINKEDIN_API_USER_DIR, "cookies/")
