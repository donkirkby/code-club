def recursive_solve(part_string, finished_count):
    if not part_string:
        return ""
    finished_count += 1
    first_character = part_string[0]
    new_part_string = part_string[finished_count:]

    remaining = recursive_solve(new_part_string, finished_count)
    return first_character + remaining


def solve(s):
    # return recursive_solve(s, 0)
    return solve_iteratively(s)


def solve_iteratively(s):
    remaining_string = s
    finished_count = 0

    result_string = ""
    while remaining_string:
        finished_count += 1
        first_character = remaining_string[0]
        remaining_string = remaining_string[finished_count:]
        result_string += first_character

    return result_string


def main():
    print(solve("saalllaaaammmmm"))  # expects "salam"
    print(solve("z"))  # expects "z"
    print(solve("aaa"))  # expects "aa"


main()
