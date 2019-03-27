def buy_or_pass(stock_price, all_time_high):
    return 'Buy' if stock_price <= all_time_high *.8 else 'Pass'

print(buy_or_pass(800, 1000))