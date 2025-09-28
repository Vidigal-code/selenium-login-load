import os
import time
import csv
import json
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from source.system.login_worker import perform_login, OUTPUT_DIR

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
    print(f"\nIniciando {n_logins} logins simultâneos...")
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
        print(f"[{r['index']}] ID: {r['id']} | Status: {r['status']} | Tempo: {r['time_seconds']}s")

    total_time = round(time.time() - start_total, 2)
    print(f"\nTempo total de execução: {total_time}s")

    if EXPORT_JSON:
        json_path = os.path.join(OUTPUT_DIR, "results.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"Resultados exportados para {json_path}")

    if EXPORT_CSV:
        csv_path = os.path.join(OUTPUT_DIR, "results.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"Resultados exportados para {csv_path}")

    summary_path = os.path.join(OUTPUT_DIR, "report_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(f"Total de logins: {n_logins}\nTempo total: {total_time}s\n")
        for r in results:
            f.write(f"[{r['index']}] ID: {r['id']} | {r['status']} - {r['time_seconds']}s\n")
    print(f"Resumo salvo em {summary_path}")