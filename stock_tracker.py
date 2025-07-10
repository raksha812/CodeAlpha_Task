# stock_tracker.py

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 300          
}

# Step 2: Get user input
portfolio = {}
print("📈 Stock Tracker - Enter stock holdings (type 'done' to finish)\n")
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()
    if stock == "DONE": 
        break
    if stock not in stock_prices:
        print("❌ Stock not in price list. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Invalid number. Try again.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Step 3: Calculate total investment
total_value = 0
lines = []
print("\n📊 Your Investment Summary:\n")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    line = f"{stock}: {quantity} shares × ${price} = ${value}"
    lines.append(line)
    print(line)

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 4: Save to file
filename = "investment_summary.txt"
with open(filename, "w") as file:
    file.write("Your Investment Summary:\n\n")
    for line in lines:
        file.write(line + "\n")
    file.write(f"\nTotal Investment Value: ${total_value}\n")     

print(f"\n✅ Summary saved to '{filename}'")    
