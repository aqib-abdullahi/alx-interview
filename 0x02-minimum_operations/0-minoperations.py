#!/usr/bin/python3
"""minimum operations
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters in a file.
    """
    if n <= 1:
        return n

    operations = 0
    clipboard = 0
    current_content = 1

    while current_content < n:
        if n % current_content == 0:
            clipboard = current_content
        current_content += clipboard
        operations += 1

    if current_content == n:
        return operations
    else:
        return 0
