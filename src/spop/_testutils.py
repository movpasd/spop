"""
Utilities used internally for running tests
"""

from typing import Any

import json


def parse_mypy_output(stdout: str) -> list[dict[str, Any]]:
    """
    Parses the mypy output to extract the list of mypy hits

    `stdout` should be the standard output (not standard error) of mypy with `--output
    json` is enabled.
    """
    hits = []
    for line in stdout.split("\n"):
        if line == "":
            continue
        entry = json.loads(line)
        if type(entry) is not dict:
            raise RuntimeError(
                f"Expected mypy stdout to produce a dictionary: {type(entry)=}"
            )
        hits.append(entry)
    return hits
