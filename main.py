import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple HTML page generator")
    # usage: python3 main.py --payload <mypayload>
    parser.add_argument("--payload", default="", help="The payload to be injected in the image tag", required=False)
    parser.add_argument("--ports", default="22,80,443,8000,8080,8081,8082", help="The ports to be used", required=False)
    parser.add_argument("--host", default="127.0.0.1", help="The host to be used", required=False)
    args = parser.parse_args()
    payload = args.payload
    ports = args.ports
    host = args.host
    # Split the ports by comma
    ports = ports.split(",")
    print("<html>")
    print("<head>")
    print("<title>My Webpage</title>")
    print("</head>")
    print("<body>")
    print("<h1>Welcome to my webpage!</h1>")
    for i in ports:
        print(f'<img src="http://{host}:{i}/{payload}"></img>')
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
