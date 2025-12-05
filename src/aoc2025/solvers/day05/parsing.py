def parse_ingredient_database(problem_input):
    lines = problem_input.splitlines()
    blank_line = lines.index("")
    ranges = map(
        lambda r: (int(r.split("-")[0]), int(r.split("-")[1])), lines[0:blank_line]
    )
    ingredients = map(lambda i: int(i), lines[blank_line + 1 :])
    return list(ranges), list(ingredients)
