#!/usr/bin/python3
"""minimum operations
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters in a file.
    """
    if not isinstance(n, int):
        return 0
    operations = 0
    clipboard = 0
    cur_content = 1

    while cur_content < n:
        # if n % current_content == 0:
        #     clipboard = current_content
        # current_content += clipboard
        # operations += 1
        if clipboard == 0:
            clipboard = cur_content
            cur_content += clipboard
            operations += 2
        elif n - cur_content > 0 and (n - cur_content) % cur_content == 0:
            clipboard = cur_content
            cur_content += clipboard
            operations += 2
        elif clipboard > 0:
            cur_content += clipboard
            operations += 1

    return operations
