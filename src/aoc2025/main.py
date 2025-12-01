from pathlib import Path
import textwrap
import importlib


def solve_all():
    for day in _list_days():
        print(day + "-1:")
        module = importlib.import_module("aoc2025.solvers." + day + ".problem1")
        print("  " + module.solve("foo"))
        print(day + "-2:")
        module = importlib.import_module("aoc2025.solvers." + day + ".problem2")
        print("  " + module.solve("foo"))
        print("")


def create_boilerplate():
    for day in _list_days():
        Path("./src/aoc2025/solvers/" + day).mkdir(parents=True, exist_ok=True)
        open("./src/aoc2025/solvers/" + day + "/__init__.py", "a").close()
        solver_content = textwrap.dedent(
            """
        def solve(problem_input):
            return "TODO"
            """
        ).lstrip()
        with open("./src/aoc2025/solvers/" + day + "/problem1.py", "w") as f:
            f.write(solver_content)
        with open("./src/aoc2025/solvers/" + day + "/problem2.py", "w") as f:
            f.write(solver_content)


def _list_days():
    return map(lambda i: "day{:02}".format(i + 1), range(12))
