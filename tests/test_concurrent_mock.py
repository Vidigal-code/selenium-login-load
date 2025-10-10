import os
import json
import time
import shutil
from source.system.run_logins import run_logins, OUTPUT_DIR

# Ensure mock driver mode
os.environ['DRIVER_MOCK'] = 'true'

def test_run_logins_mock_tmpdir(tmp_path):
    # Ensure OUTPUT_DIR is a temp directory
    outdir = tmp_path / "results"
    os.environ['OUTPUT_DIR'] = str(outdir)
    # Run with 3 logins
    run_logins(3, max_workers=3)
    # Verify results.json exists and contents
    json_path = outdir / "results.json"
    assert json_path.exists(), "results.json not generated"
    data = json.loads(json_path.read_text(encoding='utf-8'))
    assert len(data) == 3
    for entry in data:
        assert 'status' in entry
        assert 'time_seconds' in entry
        assert 'token' in entry
