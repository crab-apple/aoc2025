def parse_input(problem_input):
    result = []
    for part in problem_input.split(","):
        rge = int(part.split("-")[0]), int(part.split("-")[1])
        result.append(rge)

    return result
