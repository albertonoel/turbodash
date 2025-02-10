# TurboDash

TurboDash is a Python program that synchronizes desktop shortcuts across multiple Windows devices, ensuring a consistent user interface.

## Features

- Synchronizes `.lnk` shortcut files across specified devices.
- Configurable source and target devices.
- Simple and efficient file copying mechanism.

## Prerequisites

- Python 3.x
- Windows operating system
- Shared network path accessible by all devices for synchronization

## Installation

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/turbodash.git
    cd turbodash
    ```

2. Adjust the configuration file `turbodash_config.json` to define your devices and paths.

## Configuration

Create a `turbodash_config.json` file in the root directory with the following structure:

```json
{
    "devices": {
        "DeviceName1": {
            "name": "Device 1",
            "path": "\\\\Device1\\Shared\\Desktop"
        },
        "DeviceName2": {
            "name": "Device 2",
            "path": "\\\\Device2\\Shared\\Desktop"
        }
    }
}
```

- Replace `DeviceName1` and `DeviceName2` with the actual hostnames of your devices.
- Ensure paths are correct and accessible from the network.

## Usage

Run the script using Python:

```bash
python turbodash.py
```

The program will synchronize the `.lnk` files from the configured source device to the target devices.

## Troubleshooting

- Ensure network paths are correctly configured and accessible.
- Verify that the correct device hostname is used in the configuration.
- Check for necessary permissions to read/write in shared directories.

## License

This project is licensed under the MIT License.
```

This code provides a basic setup for synchronizing desktop shortcuts across Windows devices. Make sure to adjust the configuration file and paths according to your actual network setup.