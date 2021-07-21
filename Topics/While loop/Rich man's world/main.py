deposit = float(input())
interest_per_year = 7.1 / 100
years = 0
while 50000 <= deposit <= 700000:
    years += 1
    deposit += (deposit * interest_per_year)
print(years)
