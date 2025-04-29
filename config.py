# config.py
import os

# Пути для Windows
USER_PROFILE = os.environ['USERPROFILE']
BASE_DIRS = {
    'documents': os.path.join(USER_PROFILE, 'Documents'),
    'desktop': os.path.join(USER_PROFILE, 'Desktop'),
    'chrome_history': os.path.join(
        USER_PROFILE, 
        'AppData', 'Local', 'Google', 'Chrome', 
        'User Data', 'Default', 'History'
    )
}

IGNORE_FILES = ['passwords.txt', 'secrets']  # Что игнорировать