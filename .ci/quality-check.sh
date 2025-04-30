echo "Running lint..."
pylint cold_storage_manager || exit 1

echo "Running tests..."
python3 -m unittest discover -s cold_storage_manager/tests -p 'test_*.py' || exit 1

echo "All checks passed!"