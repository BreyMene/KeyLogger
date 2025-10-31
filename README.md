# KeyLogger

## Overview

This project demonstrates a basic client-server architecture for keyboard event monitoring, consisting of two main components:
1. A client component (`KeyLogger.py`) that captures keyboard events using the `pynput` library
2. A Flask-based server component (`server.py`) that receives and stores the captured data

This is an educational project for learning about:
- Event-driven programming with Python
- Client-server architectures
- HTTP API endpoints and data transmission
- Input device monitoring techniques

## Important Disclaimer

**This repository is strictly for educational and research purposes:**
- Use only for academic study and defensive security training
- Do not run on systems without explicit owner consent
- Never use for unauthorized monitoring or data collection
- Misuse may be illegal in your jurisdiction
- Authors are not responsible for improper use
- Consult legal counsel if unsure about intended use

## Requirements

The project dependencies are listed in `requirements.txt`. Install them into a virtual environment before working with the project. The dependencies in this repository are:

```
pynput    # For keyboard event monitoring
flask     # For the HTTP server component
requests  # For HTTP client communications
```

To install the requirements:

```powershell
# Create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Project Architecture

The project consists of two main Python scripts:

### Server Component (`server.py`)
- Flask-based HTTP server listening on port 5000
- Accepts POST requests at the `/upload` endpoint
- Creates a `logs` directory to store received data
- Saves data to separate files based on client IP addresses
- Simple error handling and response status codes

### Client Component (`KeyLogger.py`)
- Uses `pynput` to capture keyboard events
- Maintains a buffer of captured keystrokes
- Formats special keys (F1-F12, Shift, Ctrl, etc.)
- Sends data to server when Enter is pressed
- Includes timestamps with data
- Configurable server URL via `URL` constant

## Configuration

- Server: Edit `server.py` to change the port (default: 5000)
- Client: Update `URL` in `KeyLogger.py` to match your server's address

## License

See the `LICENSE` file in the repository root for the full license terms.

## Contact 
<a href="https://github.com/BreyMene/">
   <img src="https://contrib.rocks/image?repo=BreyMene/BreyMene" alt="Breyner" />
</a>