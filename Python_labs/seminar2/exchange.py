def sum_coins(k, length_coins, matrix):
    sum_prob = 0
    for i in range(1, length_coins):
        sum_prob += matrix[i][k]
    return sum_prob


def exchange_money(n):
    if n == 0:
        return 1
    length_coins = 5
    end = 50
    matrix = [[0 for x in range(end + 1)] for y in range(length_coins + 1)]
    matrix[1][1] = 1
    for i in range(1, end + 1):
        if i % 2 == 0:
            matrix[2][i] = 1
        if 4 < i < 15:
            matrix[3][i] = 1
        if i == 6 or i == 8:
            matrix[3][i] = 0
        if i > 14:
            matrix[3][i] = matrix[3][i - 10] + 1
        if i > 9:
            matrix[4][i] = matrix[4][i - 10] + matrix[3][i - 5]
        matrix[5][i] = matrix[5][i - 1] + sum_coins(i, length_coins, matrix)
    return matrix[length_coins][n]


