# Lenovo Conservation Mode Toggle

A simple Python script to enable, disable, or check the status of Conservation Mode on Lenovo laptops running Linux.

## Usage

### Prerequisites
- Python 3.x
- Root privileges (sudo)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/conservation_mode.git
   cd conservation_mode
   ```
2. Make the script executable:
   ```bash
   chmod +x conservation_mode.py
   ```
3. Install the script globally using the provided install script:
   ```bash
   chmod +x addToPath.sh
   sudo ./addToPath.sh
   ```

### Install Script Details
To simplify installation, use `addToPath.sh`, which performs the following steps:
```bash
#!/bin/bash

SCRIPT_NAME="conservation_mode.py"
DEST_PATH="/usr/local/bin/conservation_mode"

# Check if the script exists in the current directory
if [ ! -f "$SCRIPT_NAME" ]; then
    echo "Error: $SCRIPT_NAME not found in the current directory."
    exit 1
fi

# Copy the script to /usr/local/bin
sudo cp "$SCRIPT_NAME" "$DEST_PATH"

# Make it executable
sudo chmod +x "$DEST_PATH"

echo "Installation complete! You can now run 'conservation_mode' from anywhere."
```

### Command Line Arguments

```bash
usage: conservation_mode [-h] [-m {enable,disable}] [{get}]
```

This tool toggles conservation mode on Lenovo laptops.

#### Positional Arguments:
- `get` : Use this to check the current status of Conservation Mode.

#### Optional Arguments:
- `-h, --help` : Show help message and exit.
- `-m {enable,disable}, --mode {enable,disable}` : Set Conservation Mode to either `enable` or `disable`.

### Examples

Check current Conservation Mode status:
```bash
sudo conservation_mode get
```

Enable Conservation Mode:
```bash
sudo conservation_mode -m enable
```

Disable Conservation Mode:
```bash
sudo conservation_mode -m disable
```

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
Abhishek Ojha

## Links
- [Portfolio](https://abhishekojha.com.np)
- [GitHub](https://github.com/username)

