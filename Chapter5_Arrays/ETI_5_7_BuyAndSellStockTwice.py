from typing import List
from Chapter5_Arrays.ETI_5_6_BuyAndSellAStock import buy_and_sell_stock_once


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """
    Compute the maximum profit by buying and selling a stock twice.
    The second buy must be made after the first sell.
    :param prices: opn prices for a list of days.
    :return: maximum profit by buying and selling a stock twice
    """
    max_total_profit = float('-inf')
    for i in range(1, len(prices)):
        max_total_profit = max(max_total_profit,
                               (buy_and_sell_stock_once(prices[:i+1]) + buy_and_sell_stock_once(prices[i+1:])))

    return max_total_profit


if __name__ == '__main__':
    prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print(buy_and_sell_stock_twice(prices))
    print([i for i in enumerate(prices)])
