def merge_ranges(ranges):
    ranges_stack = list(sorted(ranges, key=lambda r: r[0], reverse=True))
    result = []

    current = ranges_stack.pop()
    while True:
        if not ranges_stack:
            result.append(current)
            break
        next = ranges_stack[-1]
        if next[0] <= current[1]:
            current = (current[0], max(current[1], next[1]))
            ranges_stack.pop()
        else:
            result.append(current)
            current = ranges_stack.pop()

    return result
