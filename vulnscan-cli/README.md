
# VulnScan CLI

## 🔍 Overview
VulnScan CLI is a simple Python tool that wraps around Nmap to perform scans for:
- Open ports
- Service version detection
- Basic vulnerability detection (optional)

## ✅ Features
- Accept target IP/domain from the command line
- Scan a range or list of ports
- Save results in JSON format
- Optional vulnerability scan using Nmap's `vuln` script

## 💻 Usage
```bash
python main.py --target 192.168.1.1 --ports 22,80 --vuln --output result.json
```

## 📦 Requirements
- Python 3.8+
- Nmap installed and available in system PATH

## 🛠 Setup
```bash
pip install -r requirements.txt
```

## 📁 Output
Results are saved to `scan_output.json` in JSON format with basic info.
