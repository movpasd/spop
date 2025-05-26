import json
from typing import Any

import mypy


def run_mypy(file: str) -> tuple[list[dict[str, Any]], int, str]:
    """
    Run mypy on the given file

    Returns
    -------
    (hits, status_code, stderr) -- where `hits` is a dictionary consisting of each mypy
    hit (each mypy error found) as printed to stdout
    """
    stdout, stderr, status_code = mypy.api.run(["-O", "json", "--", file])

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

    return hits, status_code, stderr
