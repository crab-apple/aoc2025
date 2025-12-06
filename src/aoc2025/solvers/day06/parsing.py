def find_whitespace(line):
    result = set()
    for i in range(0, len(line)):
        if line[i] == " ":
            result.add(i)
    return result
