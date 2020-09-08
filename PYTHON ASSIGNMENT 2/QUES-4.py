def near_thousand(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(near_thousand(100))
print(near_thousand(90))
print(near_thousand(80))
print(near_thousand(220))
