.PHONY: test ci

test:
	python3 cold_storage_manager/tests/run_tests.py

ci:
	bash .ci/run_ci.sh