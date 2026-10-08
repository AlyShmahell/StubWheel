#!/usr/bin/env python3
import os
import sys
import tempfile
import questionary
from textwrap import dedent
from types import SimpleNamespace

def stubwheel(args):
    stub = dedent(
        f"""
        from setuptools import setup, find_packages
        setup(
            name='{args.name}',
            version='{args.version}',
            url='{args.url}',
            author='{args.author}',
            author_email='{args.email}',
            description='{args.desc}',
            long_description='{args.name} {args.desc}',
            long_description_content_type='text/markdown'
        )
        """
    )
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "setup.py"), 'w') as f:
            f.write(stub)
        os.system(f'cd "{tmp}" && python setup.py sdist bdist_wheel && twine check dist/* && twine upload dist/*')

def ask_text(message, default="", validate=None):
    answer = questionary.text(message, default=default, validate=validate).ask()
    if answer is None:
        raise SystemExit(1)
    return answer

def main():
    args = SimpleNamespace(
        name=ask_text(
            "Package name:",
            validate=lambda text: True if text.strip() else "package name is required",
        ).strip(),
        version=ask_text("Package version:", default="0.0.0"),
        url=ask_text("Package URL:"),
        author=ask_text("Author name:"),
        email=ask_text("Author email:"),
        desc=ask_text("Package description:"),
    )
    stubwheel(args)

if __name__ == "__main__":
    sys.exit(main())