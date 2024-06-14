#!/bin/bash

# Create a temporary file
tmpfile=$(mktemp /tmp/shell_pip_cat.XXXXXX)

# Dump all passed arguments to the temporary file
echo "Arguments:" > "$tmpfile"
for arg in "$@"; do
  echo "$arg" >> "$tmpfile"
done

# Read and write standard input to the temporary file
echo "Standard Input:" >> "$tmpfile"
while IFS= read -r line; do
  echo "$line" >> "$tmpfile"
done

# Open xterm and display the contents of the temporary file using cat in the background
xterm -e cat "$tmpfile" &

# Optional: Clean up the temporary file after some delay (e.g., 10 seconds)
 sleep 30
# rm "$tmpfile"
