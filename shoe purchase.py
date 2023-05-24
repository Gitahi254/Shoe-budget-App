from shoes import shoes

low = shoes('Michel Njoroge', 800)
medium = shoes('Air chonjo', 1200)
high = shoes('Off black', 1500)

try:
    shoe_budget = float(input('What is your shoe budget?'))
except ValueError:
    exit('Please enter a number.')

for shoes in(high,medium,low):
    shoes.buy(shoe_budget)