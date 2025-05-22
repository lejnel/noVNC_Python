import os
import sys
import zipfile
import tempfile
import argparse

__author__ = "Im Geek (Ankush Bhagat)" "Lejnel (Rasmus Brink)" 
__version__ = "1.0.3"

# Construct the path to the data folder
base_path = os.path.dirname(os.path.abspath(__file__))

def extract_zip(zip_file_path, extract_to_path):
    # Check if the file exists
    if not os.path.exists(zip_file_path):
        print(f"Error: The file {zip_file_path} does not exist.")
        return # zip file is not found

    # Check if the specified directory exists, if not, create it
    if not os.path.exists(extract_to_path):
        os.makedirs(extract_to_path)
    
    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all contents to the specified directory
        zip_ref.extractall(extract_to_path)

# Example usage
zip_file_path = os.path.join(base_path, "resources/novnc_server.zip")
server_path = os.path.join(tempfile.gettempdir(), 'novnc_server')

extract_zip(zip_file_path, server_path)

parser = argparse.ArgumentParser(
    description="A wrapper script to run noVNC server with websockify."
)
parser.add_argument(
    "--listen",
    metavar="HOST:PORT",
    default="0.0.0.0:5800",
    help="Set proxy/webserver ip address and port to listen. (Default: http://[::]:5800)"
)

parser.add_argument(
    "--target",
    metavar="HOST:PORT",
    required=True,
    help="Set VNC IP address and port to target."
)

# --- NEW ARGUMENTS FOR SSL/TLS ---
parser.add_argument(
    "--cert",
    metavar="FILE",
    help="Path to SSL certificate file (e.g., server.crt or combined server.pem).",
)

parser.add_argument(
    "--key",
    metavar="FILE",
    help="Path to SSL private key file (e.g., server.key). Only needed if --cert is not a combined .pem file.",
)

parser.add_argument(
    "--ssl-only",
    action="store_true",
    help="Instruct websockify to only allow SSL/TLS (WSS) connections. Reject plain HTTP (WS)."
)
# --- END NEW ARGUMENTS ---

parser.add_argument(
    "-v", "--version",
    action="version",
    version=f"{__version__}"
    )

args = parser.parse_args()

# Define the proxy mapping
listen_host, listen_port = args.listen.split(":")
target_host, target_port = args.target.split(":")

def main():
    # Construct the websockify command
    websockify_cmd = [
        "websockify",
        f"{listen_host}:{listen_port}",
        f"{target_host}:{target_port}",
        f"--web {server_path}"
    ]

    # Add SSL/TLS arguments if provided
    if args.cert:
        websockify_cmd.append(f"--cert {args.cert}")
        if args.key:
            websockify_cmd.append(f"--key {args.key}")
    
    if args.ssl_only:
        websockify_cmd.append("--ssl-only")

    # Join the command parts into a single string
    final_command = " ".join(websockify_cmd)
    
    print(f"Executing command: {final_command}") # For debugging

    try:
        # Start the websockify proxy server
        # Using subprocess.run is generally safer and more flexible than os.system()
        # For this simple case, os.system might still work, but subprocess is preferred.
        os.system(final_command)
        # Alternatively, for better error handling and more control:
        # import subprocess
        # subprocess.run(websockify_cmd, check=True)

    except (KeyboardInterrupt, Exception) as e:
        print(f"\nServer stopped or encountered an error: {e}")
        sys.exit(0)

if __name__ == "__main__":
    main()
