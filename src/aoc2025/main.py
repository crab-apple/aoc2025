import importlib
import textwrap
import time
from pathlib import Path


def solve_all():
    for day in _list_days():
        _solve_and_print(day, 1)
        _solve_and_print(day, 2)
        print("")


def _solve_and_print(day, half):
    with open("./inputs/" + day + "/input", "r") as file:
        problem_input = file.read()
    module = importlib.import_module(
        "aoc2025.solvers." + day + ".problem{}".format(half)
    )
    time_a = time.perf_counter()
    output = module.solve(problem_input)
    time_b = time.perf_counter()
    if output != -1:
        print(day + "-1:")
        print(
            "  {} ({:.3f} seconds)".format(str(output).ljust(20, " "), time_b - time_a)
        )


def create_boilerplate():
    Path("./src/aoc2025/solvers").mkdir(parents=True, exist_ok=True)
    open("./src/aoc2025/solvers/__init__.py", "a").close()
    for day in _list_days():
        Path("./src/aoc2025/solvers/" + day).mkdir(parents=True, exist_ok=True)
        open("./src/aoc2025/solvers/" + day + "/__init__.py", "a").close()
        solver_content = textwrap.dedent(
            """
        def solve(problem_input):
            return -1
            """
        ).lstrip()
        with open("./src/aoc2025/solvers/" + day + "/problem1.py", "w") as f:
            f.write(solver_content)
        with open("./src/aoc2025/solvers/" + day + "/problem2.py", "w") as f:
            f.write(solver_content)

        Path("./inputs/" + day).mkdir(parents=True, exist_ok=True)
        with open("./inputs/" + day + "/input", "w") as f:
            f.write("TODO\n")

        Path("./tests/" + day).mkdir(exist_ok=True)
        open("./tests/" + day + "/__init__.py", "a").close()
        test_content = textwrap.dedent(
            """
            from aoc2025.solvers.{day}.problem{problem} import solve
            import textwrap
            import unittest


            @unittest.skip("future problem")
            class TestProblem(unittest.TestCase):

                def test_example_input(self):
                    example_input = textwrap.dedent(
                        \"\"\"
                    EXAMPLE
                    INPUT
                    \"\"\"
                    ).strip()
                    self.assertEqual("TODO EXPECTED OUTPUT", solve(example_input))
                """
        ).lstrip()
        with open("./tests/" + day + "/test_problem1.py", "w") as f:
            f.write(test_content.replace("{day}", day).replace("{problem}", "1"))
        with open("./tests/" + day + "/test_problem2.py", "w") as f:
            f.write(test_content.replace("{day}", day).replace("{problem}", "2"))


def _list_days():
    return map(lambda i: "day{:02}".format(i + 1), range(12))
