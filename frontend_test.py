import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent


def test_frontend():
    subprocess.check_call(["yarn", "vitest", "run"], cwd=PROJECT_DIR / "frontend")
