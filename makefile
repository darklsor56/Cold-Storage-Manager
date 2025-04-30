#Makefile for Cold Storage Manager

.PHONY: test ci lint quality

test:
	@echo "Running unit tests..."
	python3 -m unittest discover -s cold_storage_manager/tests -p 'test_*.py'

ci:
	@echo "Running CI..."
	bash .ci/run_ci.sh

lint:
	@echo "Running pylint..."
	pylint cold_storage_manager

quality: lint test
	@echo "All quality checks passed!"