def maxProfit(prices: list[int]):
    """
    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.
    """
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

if __name__ == "__main__":
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([12,11,10,9,8,7]) == 0
    print(" 🎉 All tests passed successfully!")