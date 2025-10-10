import os
import json
import shutil
from pathlib import Path
from source.system.run_logins import run_logins

os.environ['DRIVER_MOCK'] = 'true'

outdir = Path('results')
if outdir.exists():
    shutil.rmtree(outdir)

os.environ['OUTPUT_DIR'] = str(outdir)

print('Running mock run_logins(3)')
run_logins(3, max_workers=3)

json_path = outdir / 'results.json'
if not json_path.exists():
    raise SystemExit('results.json not generated')

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

if len(data) != 3:
    raise SystemExit('Unexpected number of results: ' + str(len(data)))

print('Mock test passed: results.json with', len(data), 'entries')
