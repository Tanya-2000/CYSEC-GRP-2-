def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


# Check
print(blackjack(5, 6, 7))

# Check
print(blackjack(9, 9, 9))

# Check
print(blackjack(9, 9, 11))