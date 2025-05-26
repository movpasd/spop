import re

from spop import _testutils


def test_static_typing():
    """
    Tests the static type-checking of the expression module is working

    This test exists because defining the type signatures of the expression objects
    requires a lot of detailed, repetitive overload specifications.
    """

    STATIC_TYPING_TEST_FILE = "./testdata/static_typing/expr.py"

    with open(STATIC_TYPING_TEST_FILE, "r") as f:
        test_file_contents = f.readlines()
    checks: list[tuple[int, str]] = []
    for i, line in enumerate(test_file_contents, 1):
        if (m := re.match(r"\s*# test: (.*)\n", line)) is None:
            continue
        test_argument = m.group(1)
        # Each test comment applies to the following line
        next_line_num = i + 1
        checks.append((next_line_num, test_argument))

    hits_in_file = _testutils.static_typing.check(STATIC_TYPING_TEST_FILE)
    hit_lines = set(hit.line for hit in hits_in_file)

    check_results: list[bool] = []
    for line_num, test_argument in checks:
        if test_argument == "ok":
            check_result = line_num not in hit_lines
        elif test_argument == "fail":
            check_result = line_num in hit_lines
        else:
            assert False, f"bad test argument: {line_num=}, {test_argument=}"
        check_results.append(check_result)

    if not all(check_results):
        print("Failed checks report:")
        for (line_num, test_argument), result in zip(checks, check_results):
            if result:
                continue
            bad_line = test_file_contents[line_num - 1]
            print(f"line {line_num}\t# test: ".expandtabs(12) + test_argument)
            print("\t".expandtabs(12) + bad_line.strip())
        assert False, "checks failed"
