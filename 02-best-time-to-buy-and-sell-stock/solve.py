def solve(prices: list[int]):
    """
    You are given an array `prices` where prices[i] is the price of a given
    stock on the `i`th day.

    You  want to maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you
    cannot achieve any profit, return `0`.

    >>> solve([7, 1, 5, 3, 6, 4])
    5
    """
    max_profit = 0
    left = 0
    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            left = right
            continue
        profit = prices[right] - prices[left]
        if profit > max_profit:
            max_profit = profit
    return max_profit
