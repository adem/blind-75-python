"""
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
`false` otherwise.

An anagram is a word of phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
"""

def solve(s: str, t: str):
    """ Solve the problem in linear time and linear memory using a hashmap.

    >>> solve("anagram", "nagaram")
    True
    >>> solve("rat", "car")
    False
    """
    if len(s) != len(t):
        return False
    seen = dict()
    for char_s, char_t in zip(s, t):
        if char_s == char_t:
            continue
        seen[char_s] = seen.get(char_s, 0) + 1
        seen[char_t] = seen.get(char_t, 0) - 1
    return all([v == 0 for v in seen.values()])

