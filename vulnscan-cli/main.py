
import argparse
from vulnscan.scanner import run_scan

def parse_arguments():
    """
    Parse command-line arguments for VulnScan CLI.
    """
    parser = argparse.ArgumentParser(description="VulnScan CLI - Simple Nmap wrapper in Python")
    parser.add_argument("--target", required=True, help="Target IP or domain to scan")
    parser.add_argument("--ports", default="1-1000", help="Ports to scan (default: 1-1000)")
    parser.add_argument("--vuln", action="store_true", help="Enable vulnerability detection")
    parser.add_argument("--output", default="scan_output.json", help="Output file to save results")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    run_scan(args.target, args.ports, args.vuln, args.output)
