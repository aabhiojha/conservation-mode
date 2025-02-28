#!/bin/bash

SCRIPT_NAME="conservation_mode.py"
DEST_PATH="/usr/local/bin/conservation_mode"

# Check if the script exists in the current directory
if [ ! -f "$SCRIPT_NAME" ]; then
    echo "Error: $SCRIPT_NAME not found in the current directory."
    exit 1
fi

# Move the script to /usr/local/bin
sudo cp "$SCRIPT_NAME" "$DEST_PATH"

# Make it executable
sudo chmod +x "$DEST_PATH"

echo "Installation complete! You can now run 'conservation_mode' from anywhere."