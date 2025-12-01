from pathlib import Path
import textwrap


def solve_all():
    for day in _list_days():
        print(day)


def create_boilerplate():
    for day in _list_days():
        Path("./src/aoc2025/solvers/" + day).mkdir(parents=True, exist_ok=True)
        open("./src/aoc2025/solvers/" + day + "/__init__.py", "a").close()
        solver_content = textwrap.dedent(
            """
        def solve(input):
            print("TODO")
            """
        ).lstrip()
        with open("./src/aoc2025/solvers/" + day + "/problem1.py", "w") as f:
            f.write(solver_content)
        with open("./src/aoc2025/solvers/" + day + "/problem2.py", "w") as f:
            f.write(solver_content)


def _list_days():
    return map(lambda i: "day{:02}".format(i + 1), range(12))
