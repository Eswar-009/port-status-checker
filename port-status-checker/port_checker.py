import socket
import argparse
from datetime import datetime


def check_port(target, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            return "OPEN"
        return "CLOSED"

    except socket.timeout:
        return "FILTERED"
    except socket.error:
        return "FILTERED"
    finally:
        sock.close()


def scan_ports(target, start_port, end_port, timeout):
    print("\n" + "=" * 65)
    print("                 PORT STATUS CHECKER")
    print("=" * 65)
    print(f"Target Host : {target}")
    print(f"Port Range  : {start_port}-{end_port}")
    print(f"Timeout     : {timeout} seconds")
    print(f"Started     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "-" * 65)
    print(f"{'PORT':<10}{'STATUS':<15}{'SERVICE':<20}")
    print("-" * 65)

    for port in range(start_port, end_port + 1):
        status = check_port(target, port, timeout)

        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        print(f"{port:<10}{status:<15}{service:<20}")

    print("-" * 65)
    print("Scan completed.")
    print("=" * 65)


def main():
    parser = argparse.ArgumentParser(
        description="TCP Port Status Checker"
    )

    parser.add_argument("target", help="Authorized target hostname or IP address")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Connection timeout in seconds"
    )

    args = parser.parse_args()

    if not 1 <= args.start_port <= 65535:
        parser.error("Start port must be between 1 and 65535.")
    if not 1 <= args.end_port <= 65535:
        parser.error("End port must be between 1 and 65535.")
    if args.start_port > args.end_port:
        parser.error("Start port cannot be greater than end port.")
    if args.timeout <= 0:
        parser.error("Timeout must be greater than 0.")

    try:
        target_ip = socket.gethostbyname(args.target)
        print(f"\nResolved Target IP: {target_ip}")
    except socket.gaierror:
        print("Error: Unable to resolve target host.")
        return

    scan_ports(target_ip, args.start_port, args.end_port, args.timeout)


if __name__ == "__main__":
    main()
