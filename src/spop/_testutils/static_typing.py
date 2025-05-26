from __future__ import annotations

from dataclasses import dataclass
import json


@dataclass
class Hit:
    file: str
    line: int
    column: int
    hint: str | None
    message: str
    code: str
    severity: str


def check(file: str) -> list[Hit]:
    """
    Run static type checker on the given file

    Returns
    -------
    A list of `Hit` objects
    """

    # lazy import to prevent accidentally importing this module from breaking everything
    # if dev dependencies not installed
    import mypy.api

    stdout, stderr, status_code = mypy.api.run(["-O", "json", "--", file])

    if status_code not in {0, 1}:
        raise RuntimeError(
            f"Mypy failed:\n{status_code=}\nstdout=\n{stdout}\nstderr=\n{stderr}\n"
        )

    hits = []
    for line in stdout.split("\n"):
        if line == "":
            continue
        entry = json.loads(line)
        if type(entry) is not dict:
            raise RuntimeError(
                f"Expected mypy stdout to produce a dictionary: {type(entry)=}"
            )
        hits.append(Hit(**entry))

    return hits
