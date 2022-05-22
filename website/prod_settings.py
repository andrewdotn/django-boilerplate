from .common_settings import *

DEBUG = False

DEBUG_TOOLBAR = False

# You’ll want to configure this.
ALLOWED_HOSTS = ["localhost"]

STATIC_ROOT = BASE_DIR / "public" / "static"

FRONTEND_DIST_DIR = BASE_DIR / "frontend" / "static" / "dist"

STATICFILES_DIRS += [FRONTEND_DIST_DIR.parent]

#

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db" / "prod.sqlite3",
    }
}
