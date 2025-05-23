# noVNC

noVNC is a Python-based server that comes with included **(websockify and noVNC)** that utilizes noVNC and websockify to provide a web-based VNC client. This allows users to remotely access and control a desktop environment through their web browser.

## Features

* **Easy Setup** : Quickly integrate your VNC server and access it via a web browser.
* **Web-based Access** : No need for a standalone VNC client; everything runs in the browser.
* **Secure Connection** : Uses websockify to securely proxy WebSocket connections to the VNC server.

## Requirements

* Python 3.x
* VNC server (e.g., TigerVNC, TightVNC)

## Installation

Install via pip:

```
pip install novnc
```

Manual Installation:

To install Terminal Widgets locally, follow these steps:

1. Clone this repository to your local machine. `git clone https://github.com/imegeek/noVNC`
2. Navigate to the cloned directory. `cd noVNC`
3. Install the package using pip: `pip install .` or `pip3 install .`

This will install noVNC along with its dependencies from the local source files.

## Options

* `--listen HOST:PORT`: Sets the proxy/webserver IP address and port to listen. Default is `http://[::]:5800`.
* `--target HOST:PORT`: Sets the VNC IP address and port to target.
* `--cert FILE` : Path of certification file. If the file is pem and have the private key --key is not needed.
* `--key FILE` : Path of the key file. Neccessarry if the cert does not have the pricate key.
* `--ssl-only` : Make the website accessible only by `https://[::]:xxxx`.


## Usage

Start the server by running the module:

```
novnc --listen <HOST:PORT> --target <VNC_SERVER_IP>:<VNC_SERVER_PORT> --cert <.crt og pem file path> --key <.key file path> --ssl-only 
```

## Example

```
http://
	novnc --listen 0.0.0.0:8080 --target 127.0.0.1:5900


https:// with crt and key
	novnc --listen 0.0.0.0:8080 --target 127.0.0.1:5900 --cert path.pem --key path.key --ssh-only

https:// with pem
	novnc --listen 0.0.0.0:8080 --target 127.0.0.1:5900 --cert path.pem --ssh-only

Both http:// and https://
	https:// with pem
	novnc --listen 0.0.0.0:8080 --target 127.0.0.1:5900 --cert path.pem
	
```

Now server will listens on `0.0.0.0:8080` and targets the VNC server at `127.0.0.1:5900`.

## Configuration

To customize the program's behavior, you can use the --listen and --target with --cert, --key and --ssh-only options when running the executable.

## Troubleshooting

* **Connection Issues** : Ensure the VNC server is running and accessible. Verify the IP and port.
* **Certificate Issues**: Make sure your certifikate is valid otherwise the website will show connection_reset or firewall issues. Verify the certificate and private key.

## License

This program is licensed under the [MIT License](https://github.com/imegeek/noVNC/blob/master/LICENSE). See the LICENSE file for details.

## Acknowledgments

* [noVNC](https://github.com/novnc/noVNC) - Open source VNC client using HTML5 and WebSockets
* [websockify](https://github.com/novnc/websockify) - WebSockets support for any application
