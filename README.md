# LabJack module

Implementation of a MADSci Node Module for integrating LabJack DAQ Based Devices.

See `definitions/labjack.node.yaml` for an example node definition file, and `definitions/labjack.node.info.yaml` for a description of the capabilities of the node.

## Installation and Usage

### Python

```bash
# Create a virtual environment named .venv
python -m venv .venv
# Activate the virtual environment on Linux or macOS
source .venv/bin/activate
# Alternatively, activate the virtual environment on Windows
# .venv\Scripts\activate
# Install the module and dependencies in the venv
pip install .
# Start the node
```

You can use `0.0.0.0` as the hostname to connect from any device on the local network, or `127.0.0.1` to limit it only to local connections.
