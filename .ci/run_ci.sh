#!/bin/bash

# Path to your project
cd "$(dirname "$0")/.." || { echo "Fail to cd"; exit 1; }

# Pull latest changes
git pull origin main

# Run tests
echo "Running tests..."
python3 cold_storage_manager/tests/run_tests.py

# Save log
echo "Finished at $(date)" >> .ci/ci.log
