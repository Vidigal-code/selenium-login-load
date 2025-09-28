import os
import time
import csv
import json
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from source.system.login_worker import perform_login, OUTPUT_DIR
from source.messages.message_system import MESSAGE_SYSTEM_RUN_LOGINS

load_dotenv()

MAX_CONCURRENT = int(os.getenv("MAX_CONCURRENT", 5))
EXPORT_JSON = os.getenv("EXPORT_JSON", "true") == "true"
EXPORT_CSV = os.getenv("EXPORT_CSV", "true") == "true"
SEQUENCE = os.getenv("SEQUENCE", "RANDOM").upper()

def generate_sequence(n):
    if SEQUENCE == "RANDOM":
        return [str(uuid.uuid4()) for _ in range(n)]
    elif SEQUENCE == "INCREASING":
        return [str(i+1) for i in range(n)]
    elif SEQUENCE == "DECREASING":
        return [str(n-i) for i in range(n)]
    else:
        return [str(uuid.uuid4()) for _ in range(n)]

def run_logins(n_logins):
    print(MESSAGE_SYSTEM_RUN_LOGINS["start_logins_text"].format(n_logins=n_logins))
    start_total = time.time()
    results = []

    sequence_ids = generate_sequence(n_logins)

    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as executor:
        futures = {executor.submit(perform_login, i, sequence_ids[i]): i for i in range(n_logins)}
        for future in as_completed(futures):
            res = future.result()
            results.append(res)

    if SEQUENCE == "INCREASING":
        results.sort(key=lambda r: int(r["id"]))
    elif SEQUENCE == "DECREASING":
        results.sort(key=lambda r: -int(r["id"]))

    for r in results:
        print(MESSAGE_SYSTEM_RUN_LOGINS["login_status_text"].format(
            index=r['index'], login_id=r['id'], status=r['status'], time_seconds=r['time_seconds']
        ))

    total_time = round(time.time() - start_total, 2)
    print(MESSAGE_SYSTEM_RUN_LOGINS["total_time_text"].format(total_time=total_time))

    if EXPORT_JSON:
        json_path = os.path.join(OUTPUT_DIR, "results.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(MESSAGE_SYSTEM_RUN_LOGINS["results_exported_json_text"].format(json_path=json_path))

    if EXPORT_CSV:
        csv_path = os.path.join(OUTPUT_DIR, "results.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(MESSAGE_SYSTEM_RUN_LOGINS["results_exported_csv_text"].format(csv_path=csv_path))

    summary_path = os.path.join(OUTPUT_DIR, "report_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(MESSAGE_SYSTEM_RUN_LOGINS["summary_header_text"].format(n_logins=n_logins, total_time=total_time))
        for r in results:
            f.write(MESSAGE_SYSTEM_RUN_LOGINS["summary_entry_text"].format(
                index=r['index'], login_id=r['id'], status=r['status'], time_seconds=r['time_seconds']
            ))
    print(MESSAGE_SYSTEM_RUN_LOGINS["summary_saved_text"].format(summary_path=summary_path))

def run_logins_with_queue(n_logins, queue):
    start_total = time.time()
    results = []
    sequence_ids = generate_sequence(n_logins)

    queue.put(MESSAGE_SYSTEM_RUN_LOGINS["start_logins_text"].format(n_logins=n_logins))

    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as executor:
        futures = {executor.submit(perform_login, i, sequence_ids[i]): i for i in range(n_logins)}
        for future in as_completed(futures):
            res = future.result()
            results.append(res)
            queue.put(MESSAGE_SYSTEM_RUN_LOGINS["login_status_text"].format(
                index=res['index'], login_id=res['id'], status=res['status'], time_seconds=res['time_seconds']
            ))

    if SEQUENCE == "INCREASING":
        results.sort(key=lambda r: int(r["id"]))
    elif SEQUENCE == "DECREASING":
        results.sort(key=lambda r: -int(r["id"]))

    total_time = round(time.time() - start_total, 2)
    queue.put(MESSAGE_SYSTEM_RUN_LOGINS["total_time_text"].format(total_time=total_time))

    if EXPORT_JSON:
        json_path = os.path.join(OUTPUT_DIR, "results.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        queue.put(MESSAGE_SYSTEM_RUN_LOGINS["results_exported_json_text"].format(json_path=json_path))

    if EXPORT_CSV:
        csv_path = os.path.join(OUTPUT_DIR, "results.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        queue.put(MESSAGE_SYSTEM_RUN_LOGINS["results_exported_csv_text"].format(csv_path=csv_path))

    summary_path = os.path.join(OUTPUT_DIR, "report_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(MESSAGE_SYSTEM_RUN_LOGINS["summary_header_text"].format(n_logins=n_logins, total_time=total_time))
        for r in results:
            f.write(MESSAGE_SYSTEM_RUN_LOGINS["summary_entry_text"].format(
                index=r['index'], login_id=r['id'], status=r['status'], time_seconds=r['time_seconds']
            ))
    queue.put(MESSAGE_SYSTEM_RUN_LOGINS["summary_saved_text"].format(summary_path=summary_path))