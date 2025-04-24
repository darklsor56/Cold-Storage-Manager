import subprocess
import yaml

with open("../../.test.yaml") as f:
    config = yaml.safe_load(f)

print("🚀 Starting tests...\n")

for test in config.get("tests", []):
    name = test.get("name")
    cmd = test.get("command")
    print(f"🔧 {name}")
    print(f"   $ {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode == 0:
        print("✅ Passed\n")
    else:
        print("❌ Failed\n")
