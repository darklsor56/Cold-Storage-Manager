#!/bin/bash
# Install pre-push hook into the local git config

HOOK_PATH=".git/hooks/pre-push"
cp .ci/pre-push.sh "$HOOK_PATH"
chmod +x "$HOOK_PATH"

echo "Pre-push git hook installed!"
