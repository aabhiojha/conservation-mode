# Conservation Mode Toggle for Lenovo Laptops

This Python script allows you to **enable** or **disable** Conservation Mode on Lenovo laptops running Linux.

Conservation Mode helps to prolong battery lifespan by limiting the maximum charge to around 80%, instead of 100%, which is useful for laptops plugged in for extended periods.

## Features
- Enable or disable Conservation Mode.
- Check current Conservation Mode status.
- Simple command-line interface.

## Prerequisites
- Python 3.x
- `argparse`
- Root privileges (sudo)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/conservation_mode.git
   cd conservation_mode
   ```

2. Make the script executable:
   ```bash
   chmod +x conservation_mode.py
   ```

## Usage
### Check Current Status
```bash
python3 conservation_mode.py get
```

### Enable Conservation Mode
```bash
sudo python3 conservation_mode.py -m enable
```

### Disable Conservation Mode
```bash
sudo python3 conservation_mode.py -m disable
```

### Help
```bash
python3 conservation_mode.py -h
```

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome! Feel free to open an issue if you encounter any problems.

## Author
[Abhishek Ojha](https://abhishekojha.com.np)

