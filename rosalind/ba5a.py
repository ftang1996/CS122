from math import inf


def min_coins(money, coins):
    m_coins = [0]
    for m in range(1, money + 1):
        min = inf
        for x in range(len(coins)):
            if m >= coins[x]:
                if m_coins[m - coins[x]] + 1 < min:
                    min = m_coins[m - coins[x]] + 1
        m_coins.append(min)
    return m_coins[money]


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        money = int(input.readline().strip())
        coins = [int(coin) for coin in input.readline().strip().split(',')]
    print(min_coins(money, coins))