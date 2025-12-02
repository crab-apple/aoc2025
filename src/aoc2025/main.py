from pathlib import Path
import textwrap
import importlib


def solve_all():
    for day in _list_days():
        with open("./inputs/" + day + "/input", "r") as file:
            problem_input = file.read()
        print(day + "-1:")
        module = importlib.import_module("aoc2025.solvers." + day + ".problem1")
        print("  " + module.solve(problem_input))
        print(day + "-2:")
        module = importlib.import_module("aoc2025.solvers." + day + ".problem2")
        print("  " + module.solve(problem_input))
        print("")


def create_boilerplate():
    for day in _list_days():
        Path("./src/aoc2025/solvers/" + day).mkdir(parents=True, exist_ok=True)
        open("./src/aoc2025/solvers/" + day + "/__init__.py", "a").close()
        solver_content = textwrap.dedent(
            """
        def solve(problem_input):
            return problem_input
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
            import unittest


            class TestProblem(unittest.TestCase):
                def test_example_input(self):
                    self.assertEqual(2, 2)
                """
        ).lstrip()
        with open("./tests/" + day + "/test_problem1.py", "w") as f:
            f.write(test_content)
        with open("./tests/" + day + "/test_problem2.py", "w") as f:
            f.write(test_content)


def _list_days():
    return map(lambda i: "day{:02}".format(i + 1), range(12))
