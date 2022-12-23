This is a solution for the Coding Problem [309. Best Time to Buy and Sell Stock with Cooldown from LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description):

Imagine you have a stock that you can buy and sell. You want to make as much money as possible by buying and selling the stock. However, there are some rules:

- You can only buy and sell the stock once per day.
- If you sell the stock, you have to wait one day before you can buy it again.

For example, suppose the stock is worth the following amount on different days:

- Day 1: $1
- Day 2: $2
- Day 3: $3
- Day 4: $0
- Day 5: $2

What is the most money you can make by buying and selling the stock according to the rules?

One possible solution is to:

- Buy the stock on day 1
- Sell the stock on day 2
- Wait one day (day 3)
- Buy the stock on day 4
- Sell the stock on day 5

This would give us a profit of $3.

To solve this problem, we can use a computer program that follows these steps:

1.  Define three states: `buy`, `sell`, and `cooldown`.
2.  Set the initial values for the states:
    - `buy[0]`: the maximum profit if the last action was a buy, and it's the first day. We set this to -$1, because we're buying the stock for $1.
    - `sell[0]`: the maximum profit if the last action was a sell, and it's the first day. We set this to $0, because we haven't made any profit yet.
    - `cooldown[0]`: the maximum profit if the last action was a cooldown, and it's the first day. We set this to $0, because we haven't made any profit yet.
3.  For each day from 1 to the last day:
    - Calculate the maximum profit if the last action was a buy:
      - If the last action was a buy, we can either keep holding the stock or sell it. The maximum profit is the maximum of these two options.
      - If the last action was a cooldown, we can buy the stock. The maximum profit is the maximum of this option and the previous maximum.
    - Calculate the maximum profit if the last action was a sell:
      - If the last action was a sell, we have to wait one day before we can buy the stock again. The maximum profit is the previous maximum.
      - If the last action was a buy, we can sell the stock and make a profit. The maximum profit is the maximum of this option and the previous maximum.
    - Calculate the maximum profit if the last action was a cooldown:
      - If the last action was a cooldown, we can either keep waiting or sell the stock. The maximum profit is the maximum of these two options.
      - If the last action was a sell, we have to wait one day before we can buy the stock again. The maximum profit is the previous maximum.
4.  Return the maximum of `sell[last day]` and `cooldown[last day]`, because these are the maximum profits if the last action was a sell or a cooldown, respectively.

That's it! The program follows these steps to find the maximum profit by buying and selling the stock according to the rules.

Let me explain the code line by line:

```python
def maxProfit(prices):
    if not prices:
        return 0
```

This code checks if the list of prices is empty. If it is, it returns 0 because we can't make any profit if there are no prices.

```python
    n = len(prices)
    buy = [0] * n
    sell = [0] * n
    cooldown = [0] * n
```

These lines define the length of the list of prices (`n`), and three lists with `n` elements each, called `buy`, `sell`, and `cooldown`. These lists will store the maximum profit for each state (`buy`, `sell`, or `cooldown`) at each day.

```python
    buy[0] = -prices[0]
    sell[0] = 0
    cooldown[0] = 0
```

These lines set the initial values for the first day. The initial value for `buy` is -$1 (the price of the stock on the first day), the initial value for `sell` is $0 (we haven't made any profit yet), and the initial value for `cooldown` is also $0 (we haven't made any profit yet).

```python
    for i in range(1, n):
        buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])
        sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        cooldown[i] = max(cooldown[i-1], sell[i-1])
```

These lines calculate the maximum profit for each state at each day. For each day `i` from 1 to `n-1` (the last day):

- The maximum profit for `buy` is the maximum of:
  - The maximum profit for `buy` on the previous day (`buy[i-1]`).
  - The maximum profit for `cooldown` on the previous day minus the price of the stock on day `i` (`cooldown[i-1] - prices[i]`).
- The maximum profit for `sell` is the maximum of:
  - The maximum profit for `sell` on the previous day (`sell[i-1]`).
  - The maximum profit for `buy` on the previous day plus the price of the stock on day `i` (`buy[i-1] + prices[i]`).
- The maximum profit for `cooldown` is the maximum of:
  - The maximum profit for `cooldown` on the previous day (`cooldown[i-1]`).
  - The maximum profit for `sell` on the previous day (`sell[i-1]`).

```python
    return max(sell[-1], cooldown[-1])
```

This line returns the maximum of the maximum profit for `sell` on the last day (`sell[-1]`) and the maximum profit for `cooldown` on the last day (`cooldown[-1]`). This is the maximum profit if the last action was a sell or a cooldown, respectively.

This code has a **time complexity of O(n)** and a **space complexity of O(n)**, where n is the number of days.

I hope this helps! Let me know if you have any questions.
