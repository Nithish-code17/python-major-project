import os
import json
import pandas as pd

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "tasks.csv")
JSON_FILE = os.path.join(DATA_DIR, "tasks.json")


def ensure_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["id", "title", "status", "priority"])
        df.to_csv(CSV_FILE, index=False)

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump([], f)


def load_tasks_csv():
    ensure_data_files()
    return pd.read_csv(CSV_FILE)


def save_tasks_csv(df):
    df.to_csv(CSV_FILE, index=False)


def save_tasks_json(df):
    tasks_list = df.to_dict(orient="records")
    with open(JSON_FILE, "w") as f:
        json.dump(tasks_list, f, indent=2)
