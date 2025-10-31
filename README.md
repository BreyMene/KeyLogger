# KeyLogger

**Important**: This repository contains code intended for research and educational purposes only. Do not use these tools to monitor, record, or intrude on other people's devices or accounts without explicit, informed, and written consent. Misuse of keylogging or monitoring software may be illegal in your jurisdiction and can cause harm. By using the code in this repository you accept full responsibility for ensuring your use is legal and ethical.

## Overview

This project provides an educational example of capturing keyboard events on a local machine for learning, testing, and defensive research (for example, detecting or understanding how key capture works so you can build protections). The repository is NOT intended to be used for spying, credential theft, or any malicious activity.

Do not run the code on systems you do not own or administer, and always obtain explicit consent from any users or owners before executing monitoring software.


## Disclaimer (Educational Use Only)

- This repository is provided for academic, research, and defensive security training only.
- Do not use this code to invade privacy, commit fraud, or violate laws.
- The author(s) and contributors are not responsible for any misuse.
- If you are unsure whether your intended use is allowed, consult legal counsel and obtain written consent.

## Requirements

The project dependencies are listed in `requirements.txt`. Install them into a virtual environment before working with the project. The dependencies in this repository are:

```
pynput
```

To install the requirements:

```powershell
# Create and activate a virtual environment (Windows PowerShell)
python -m venv .venv; .\.venv\Scripts\activate
pip install -r requirements.txt
```

Note: Installing packages is safe and allowed; however, do not execute any key-capture or monitoring scripts on machines without permission.

## Development / Inspecting the Code

If you're here to learn, read the source files to understand how keyboard event handling and recording are implemented. Use static analysis, code reading, and controlled experiments on disposable virtual machines to test behavior — never on production systems or other people's hardware without consent.


## License

See the `LICENSE` file in the repository root for the full license terms.

## Contact 
<a href="https://github.com/BreyMene/">
   <img src="https://contrib.rocks/image?repo=BreyMene/BreyMene" alt="Breyner" />
</a>