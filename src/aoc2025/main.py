from pathlib import Path
import textwrap
import importlib


def solve_all():
    for day in _list_days():
        with open("./inputs/" + day + "/input", "r") as file:
            problem_input = file.read()
        print(day + "-1:")
        module = importlib.import_module("aoc2025.solvers." + day + ".problem1")
        print("  " + str(module.solve(problem_input)))
        print(day + "-2:")
        module = importlib.import_module("aoc2025.solvers." + day + ".problem2")
        print("  " + str(module.solve(problem_input)))
        print("")


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
