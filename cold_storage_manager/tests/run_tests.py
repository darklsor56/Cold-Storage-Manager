"""Organize and Run the Tests from the YAML."""

import sys
import os
import subprocess
import yaml

# Check for a --dry-run flag
dry_run = "--dry-run" in sys.argv

# Get the absolute path to the YAML file
script_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.abspath(os.path.join(script_dir, "../../.test.yaml"))

try:
    with open(yaml_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print(f"❌ Error: .test.yaml not found at {yaml_path}")
    sys.exit(1)

# Start the Tests
print("Starting tests...\n")

# Loop through the tests from the YAML and see if they pass or fail.
for test in config.get("tests", []):
    name = test.get("name")
    cmd = test.get("command")

    print(f"🧪 {name}")
    print(f"▶ {cmd}")

    if dry_run:
        print("🔍 (Dry run — command not executed)\n")
        continue

    result = subprocess.run(cmd, shell=True, check=False)

    if result.returncode == 0:
        print("✅ Passed\n")
    else:
        print("❌ Failed\n")
        sys.exit(1)
