import pandas as pd
from tools.data_handler import load_tasks_csv, save_tasks_csv, save_tasks_json


def add_task(title, priority):
    df = load_tasks_csv()

    new_id = 1 if df.empty else int(df["id"].max()) + 1
    new_task = {"id": new_id, "title": title, "status": "Pending", "priority": priority}

    df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)

    save_tasks_csv(df)
    save_tasks_json(df)
    print("✅ Task Added Successfully!")


def view_tasks():
    df = load_tasks_csv()

    if df.empty:
        print("⚠️ No tasks found.")
        return

    print("\n📌 TASK LIST")
    print(df)


def mark_done(task_id):
    df = load_tasks_csv()

    if df.empty:
        print("⚠️ No tasks found.")
        return

    if task_id not in df["id"].values:
        print("❌ Task ID not found.")
        return

    df.loc[df["id"] == task_id, "status"] = "Done"

    save_tasks_csv(df)
    save_tasks_json(df)
    print("✅ Task marked as DONE!")


def filter_tasks_by_status(status):
    df = load_tasks_csv()

    filtered = df[df["status"].str.lower() == status.lower()]

    if filtered.empty:
        print("⚠️ No matching tasks found.")
    else:
        print(filtered)


def sort_tasks_by_priority():
    df = load_tasks_csv()

    if df.empty:
        print("⚠️ No tasks found.")
        return

    print(df.sort_values(by="priority"))
