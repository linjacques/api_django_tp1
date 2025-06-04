import os
import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter

data_dir = r"C:\Users\jacqu\Documents\Efrei\M1_2024_2025\data_integration1.5\TP_DataLake_DataWarehouse\datalake\transaction_log\2025-04-28"

def load_all_transactions():
    transactions = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    transactions.extend(json.load(f))
                except json.JSONDecodeError:
                    continue
    return transactions

def compute_money_last_5min():
    now = datetime.utcnow()
    time_limit = now - timedelta(minutes=5)
    total = 0.0

    for tx in load_all_transactions():
        ts = tx.get("timestamp")
        if ts:
            try:
                dt = datetime.fromisoformat(ts)
                if dt > time_limit:
                    total += float(tx.get("amount", 0))
            except ValueError:
                continue
    return total

def compute_total_per_user_and_type():
    result = defaultdict(lambda: defaultdict(float))  # user -> type -> total

    for tx in load_all_transactions():
        user = tx.get("user_id")
        tx_type = tx.get("payment_method")
        amount = float(tx.get("amount", 0))
        if user and tx_type:
            result[user][tx_type] += amount

    return result

def get_top_products(x):
    counter = Counter()

    for tx in load_all_transactions():
        product = tx.get("product_category")
        if product:
            counter[product] += 1

    return counter.most_common(x)
