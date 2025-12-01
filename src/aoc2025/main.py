from pathlib import Path


def solve_all():
    for day in _list_days():
        print(day)


def create_boilerplate():
    for day in _list_days():
        Path("./src/aoc2025/solvers/" + day).mkdir(parents=True, exist_ok=True)
        open("./src/aoc2025/solvers/" + day + "/__init__.py", "a").close()
        open("./src/aoc2025/solvers/" + day + "/problem1.py", "a").close()
        open("./src/aoc2025/solvers/" + day + "/problem2.py", "a").close()


def _list_days():
    return map(lambda i: "day{:02}".format(i + 1), range(12))
