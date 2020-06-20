a = 1000
n = 20
years = 5
def bank(a, n, years):
    a = a + (a * (n / 100)) * years
    return a
x = bank(a, n, years)
print(x)























