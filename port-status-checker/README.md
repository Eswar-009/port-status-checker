# Port Status Checker

A Python TCP socket utility that checks the status of ports on an authorized target host.

## Features

- TCP socket programming
- Target hostname/IP input
- Custom port range
- Connection timeout
- Open port detection
- Closed port detection
- Filtered/timeout detection
- Basic TCP service identification
- Command-line interface

## Requirements

- Python 3.x
- No external libraries

## Usage

```bash
python port_checker.py <target> <start_port> <end_port>
```

Example:

```bash
python port_checker.py 127.0.0.1 1 100
```

Custom timeout:

```bash
python port_checker.py 127.0.0.1 1 100 --timeout 2
```

## Port States

OPEN
: TCP connection was successfully established.

CLOSED
: TCP connection was refused.

FILTERED
: Connection timed out or a socket error prevented determining the state.

## Security / Authorization

Use this utility only against systems and networks you own or have explicit permission to test.

## Objective

Program network socket connections to audit the status of authorized host ports.
