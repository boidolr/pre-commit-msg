#!/usr/bin/env python3
import argparse
import pathlib
import sys
from collections.abc import Sequence


def _ensure_message_format(commit_msg_filepath: str, capitalize: bool) -> None:
    # ensure there are always two empty lines between short description and description
    with pathlib.Path(commit_msg_filepath).open("r+") as fh:
        lines = fh.read().splitlines()
        if len(lines) > 0 and capitalize:
            lines[0] = lines[0].capitalize()

        if len(lines) > 1 and lines[1] != "":
            lines.insert(1, "")

        if len(lines) > 2 and lines[2] != "":
            lines.insert(2, "")

        while len(lines) >= 4 and lines[3] == "":
            lines.pop(3)

        fh.seek(0, 0)
        fh.write("\n".join(lines))
        fh.truncate()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Commit message file path")
    parser.add_argument("-c", "--capitalize", action="store_true", help="Capitalize subject line")
    args = parser.parse_args(argv)

    _ensure_message_format(args.filename, args.capitalize)

    return 0


if __name__ == "__main__":
    sys.exit(main())
