import streamlit as st
import random
import time
import json
import pandas as pd

# Define suspicious conditions
def is_fraudulent(transaction):
    if transaction["amount"] > 800:
        return True, "High amount"
    if transaction["location"] in ["FL", "IL"]:
        return True, "Suspicious location"
    return False, ""

# Generate a mock transaction
def generate_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.randint(1, 100),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "location": random.choice(["NY", "LA", "TX", "FL", "IL"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }

# Streamlit UI
st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("🕵️‍♀️ Real-Time Fraud Detection (Simulated)")

num_txns = st.slider("Number of transactions to simulate", min_value=5, max_value=50, value=10)

if st.button("🚀 Run Fraud Detection"):
    records = []

    for _ in range(num_txns):
        txn = generate_transaction()
        fraud, reason = is_fraudulent(txn)
        txn["fraudulent"] = fraud
        txn["reason"] = reason if fraud else "Safe"
        records.append(txn)
        time.sleep(0.1)  # Simulate real-time effect

    df = pd.DataFrame(records)

    st.subheader("📊 All Transactions")
    st.dataframe(df)

    st.subheader("⚠️ Flagged Transactions")
    st.dataframe(df[df["fraudulent"] == True])

    st.success("Detection complete!")
