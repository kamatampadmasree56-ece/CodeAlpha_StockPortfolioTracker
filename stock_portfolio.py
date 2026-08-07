# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 220,
    "TSLA": 310,
    "GOOGL": 190,
    "MSFT": 470,
    "AMZN": 235
}

portfolio = {}

print("=" * 45)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock = input("\nEnter Stock Symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Invalid Stock Symbol!")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("❌ Please enter a valid number.")

print("\n" + "=" * 45)
print("        PORTFOLIO SUMMARY")
print("=" * 45)

total = 0

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(f"{stock} x {quantity} = ${value}")

print("-" * 45)
print(f"Total Portfolio Value = ${total}")
print("-" * 45)

with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 30 + "\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock} x {quantity} = ${value}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Portfolio Value = ${total}\n")

print("\n✅ Portfolio saved successfully as portfolio.txt")