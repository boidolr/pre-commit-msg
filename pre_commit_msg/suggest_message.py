#!/usr/bin/env python3
import argparse
import pathlib
import sys
import urllib.request
from collections.abc import Sequence


def _retrieve_message(timeout_seconds: int = 1) -> str:
    url = "https://whatthecommit.com/index.txt"
    with urllib.request.urlopen(url, timeout=timeout_seconds) as f:  # noqa: S310
        return f.read().decode("utf-8").strip()


def _prepend_message(
    commit_msg_filepath: str,
) -> bool:
    try:
        suggestion = _retrieve_message()
    except Exception as exc:
        print("Failed to retrieve message suggestion", str(exc))
        return False

    with pathlib.Path(commit_msg_filepath).open("r+") as fh:
        commit_msg = fh.read()
        fh.seek(0, 0)
        fh.write(f"# {suggestion}\n")
        fh.write(commit_msg)
        fh.truncate()

    return True


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Commit message file path")
    args = parser.parse_args(argv)

    updated = _prepend_message(args.filename)
    return 0 if updated else 1


if __name__ == "__main__":
    sys.exit(main())
