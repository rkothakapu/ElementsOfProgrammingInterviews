from typing import List


def buy_and_sell_stock(prices: List[float]) -> float:
    if not prices:
        return 0.0

    all_time_low = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > all_time_low:
            max_profit = max(max_profit, prices[i] - all_time_low)
        else:
            all_time_low = min(all_time_low, prices[i])

    return max_profit


if __name__ == "__main__":
    print(buy_and_sell_stock([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
