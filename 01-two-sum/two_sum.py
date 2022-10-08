def solve(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers `nums` and an integer `target`, return indices
    of the two numbers such that they add up to `target`.

    >>> solve([2, 7, 11, 15], 9)
    [0, 1]
    """
    lookup = dict()
    for i, n in enumerate(nums):
        j = lookup.get(target - n)
        if j is not None:
            return [j, i]
        lookup[n] = i
