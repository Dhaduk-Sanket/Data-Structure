# Security Researcher - Backtracking

def gen(lock, used):
    if len(lock) == 3:
        print(lock)
        return

    for digit in ['1', '2', '3']:
        if digit not in used:
            gen(lock + digit, used + [digit])

gen("", [])


# File Size Calculator - Recursion

folder = {
    "file1": 60,
    "file2": 100,
    "subfolder": {
        "file3": 150,
        "file4": 200
    }
}

def total_size(data):
    size = 0

    for item in data.values():
        if isinstance(item, dict):
            size += total_size(item)
        else:
            size += item

    return size

print("Total Size:", total_size(folder), "MB")


# Climbing Stairs - Recursion

def climb(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return climb(n - 1) + climb(n - 2)

n = 5

print("Number of ways:", climb(n))