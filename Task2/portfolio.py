import csv
import os
import yfinance as yf

FILE = "portfolio_summary.csv"

while True:
    ticker = input("Stock code (or 'exit' to quit): ").strip().upper()
    if ticker == "EXIT":
        break

    price = float(input("Price per share: "))
    quantity = int(input("Number of shares: "))
    total_cost = price * quantity

    try:
        current_price = float(yf.Ticker(ticker).fast_info["last_price"])
    except Exception:
        print(f"Could not get a price for {ticker}, skipping.")
        continue

    current_value = current_price * quantity
    profit_loss = (current_value - total_cost) / total_cost * 100
    print(f"{ticker}: {profit_loss:+.2f}%")

    new_file = not os.path.exists(FILE) or os.path.getsize(FILE) == 0
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["ticker", "buy_price", "quantity", "total_cost",
                             "current_value", "profit_loss_pct"])
        writer.writerow([ticker, price, quantity, total_cost,
                         round(current_value, 2), round(profit_loss, 2)])

print("Saved to:", os.path.abspath(FILE))
