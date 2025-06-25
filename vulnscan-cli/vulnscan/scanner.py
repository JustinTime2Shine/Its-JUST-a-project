
import subprocess
import json
from datetime import datetime

def run_scan(target_ip, port_range, enable_vuln_scan, output_file):
    """
    Run an Nmap scan using subprocess and save results to a file.

    Parameters:
    - target_ip: Target IP address or domain to scan
    - port_range: Ports to scan (e.g., "22,80,443" or "1-1000")
    - enable_vuln_scan: Boolean flag to include vulnerability scripts
    - output_file: File path to save the scan results
    """
    command = ["nmap", "-p", port_range, "-sV", "-oX", "-", target_ip]
    if enable_vuln_scan:
        command += ["--script", "vuln"]

    print(f"[+] Running Nmap command: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)

    # Simulate parsing result to JSON-like structure (basic)
    scan_data = {
        "target": target_ip,
        "ports": port_range.split(","),
        "vuln_scan": enable_vuln_scan,
        "timestamp": datetime.now().isoformat(),
        "raw_output": result.stdout[:1000]  # Truncate for brevity
    }

    with open(output_file, "w") as output:
        json.dump(scan_data, output, indent=4)
    print(f"[✓] Scan complete. Results saved to {output_file}")
