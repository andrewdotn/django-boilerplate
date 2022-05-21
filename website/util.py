import json
from pathlib import Path

from django.conf import settings
from django.core.management.utils import get_random_secret_key


def load_or_generate_secret_key():
    """Load or generate a secret key, stored in BASE_DIR / .secrets.json

    Instead of checking in an insecure key, use a local file to store it,
    automatically generating it if needed.
    """
    secrets_file: Path = settings.BASE_DIR / ".secrets.json"
    if not secrets_file.exists():
        secrets = {}
    else:
        secrets = json.loads(secrets_file.read_text())

    # XXX There’s a potential race condition here if multiple django processes
    # all start up at once for the first time.
    secret_key = secrets.get("SECRET_KEY", None)
    if secret_key is None:
        secret_key = get_random_secret_key()

        secrets["SECRET_KEY"] = secret_key
        secrets_file.write_text(json.dumps(secrets, indent=True) + "\n")

    return secret_key
