#!/usr/bin/env bash
#
# Description: Generate test outputs for man pages.
# Usage: ./generate-test-outputs.sh [options]
#

set -Eeuo pipefail
shopt -s inherit_errexit

if [[ $# -ne 1 ]]; then
	echo "Usage: $(basename "$0") outputDirectory" >&2
	exit 1
fi

# Validate input
if [[ -z "${1:-}" ]]; then
	echo "Error: Output directory cannot be empty" >&2
	exit 1
fi

# Check required commands
command -v man >/dev/null 2>&1 || {
	echo "Error: 'man' command not found" >&2
	exit 1
}

readonly OUTPUT_DIRECTORY="$1"
mkdir -p -- "$OUTPUT_DIRECTORY"

readonly ALL_MAN_PAGES_1=(
	is-true
	is-false
	prefix
	suffix
	siakhooi-textutils
)

for i in "${ALL_MAN_PAGES_1[@]}"; do
	MANWIDTH=120 man --pager=cat -- "$i" >"$OUTPUT_DIRECTORY/man_${i}.out"
done
