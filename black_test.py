import os
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent


def test_code_formatted_with_black():
    things_to_check = []

    def add_item(f):
        f = f.relative_to(PROJECT_DIR)
        f = os.fspath(f)
        things_to_check.append(f)

    for f in PROJECT_DIR.iterdir():
        if f.is_file() and f.suffix == ".py":
            add_item(f)
        if f.is_dir():
            for c in f.iterdir():
                if c.is_file() and c.suffix == ".py":
                    add_item(f)
                    break

    print(things_to_check)
    subprocess.check_call(["black", "--check", *things_to_check], cwd=PROJECT_DIR)
