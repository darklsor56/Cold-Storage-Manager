#!/bin/bash
# Git pre-push hook to run project tests before pushing

echo "Running test suite before push..."
cd "$(dirname "$0")/../cold_storage_manager/tests"
python3 run-tests.py

if [ $? -ne 0 ]; then
    echo "❌ Pre-push failed: Tests did not pass."
    exit 1
else
    echo "✅ All tests passed. Proceeding with push."
fi
