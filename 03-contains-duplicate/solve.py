def solve(nums: list[int]):
    """
    Given an integer array `nums`, return `true` if any value appears at least
    twice in the array, and return `false` if every element is distinct.

    >>> solve([1, 2, 3, 1])
    True
    >>> solve([1, 2, 3, 4])
    False
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
