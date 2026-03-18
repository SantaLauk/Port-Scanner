# Python Port Scanner

This project is a simple multi-threaded port scanner written in Python.  
It was built as part of my effort to learn the fundamentals of **network security, service enumeration, and concurrent programming** while preparing for further study in cybersecurity.

The scanner performs basic reconnaissance by identifying open ports on a target host and attempting to retrieve service banners when available. While intentionally lightweight, it demonstrates several core techniques used in real security tools.

---

## Project Goals

The primary objective of this project was to deepen my understanding of:

- TCP networking and socket communication
- Concurrent programming using threads
- Queue-based task distribution
- Service enumeration and banner grabbing
- Command-line interface design in Python

Building this tool helped translate theoretical networking concepts into practical code and provided hands-on experience with techniques used in early stages of security assessments.

---

## Features

- Multi-threaded port scanning
- Queue-based work distribution for efficient task handling
- Service identification for common ports
- Banner grabbing for basic service fingerprinting
- HTTP server detection through response headers
- Configurable scanning ranges
- Progress tracking during scans
- Command-line interface using `argparse`

---

## Technologies Used

This project relies entirely on Python's standard library:

- `socket` — TCP network communication  
- `threading` — concurrent scanning  
- `queue` — thread-safe task management  
- `argparse` — command-line interface  

No external dependencies are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SantaLauk/Port-Scanner.git
cd Port-Scanner
```

Ensure Python 3 is installed:

```bash
python --version
```

---

## Usage

### Quick Scan (ports 20–100)

```bash
python scanner.py scanme.nmap.org --quick
```

### Full Scan (ports 1–1024)

```bash
python scanner.py scanme.nmap.org --full
```

### Custom Port Range

```bash
python scanner.py scanme.nmap.org --start 50 --end 200
```

---

## Example Output

```
Scanning target: 45.33.32.156
Scanning ports 20-100

Port 22   OPEN  SSH   SSH-2.0-OpenSSH_6.6.1p1 Ubuntu
Port 80   OPEN  HTTP  Server: Apache/2.4.7 (Ubuntu)

Scanned 10/81 ports...
Scanned 20/81 ports...
Scanned 30/81 ports...
```

---

## How It Works

1. The target domain is resolved to an IP address.
2. The selected port range is added to a queue.
3. Multiple worker threads retrieve ports from the queue simultaneously.
4. Each thread attempts a TCP connection using Python sockets.
5. If the connection succeeds, the scanner attempts to retrieve service information using banner grabbing.

This approach reflects the initial reconnaissance phase used by professional network scanning tools such as :contentReference[oaicite:0]{index=0}.

---

## Limitations

This scanner is intentionally simple and does not attempt advanced detection techniques such as:

- OS fingerprinting
- stealth scanning methods
- encrypted service probing (e.g., HTTPS TLS negotiation)

These features are handled by specialized tools and frameworks in professional environments.

---

## Future Improvements

Planned enhancements include:

- Colored terminal output
- Structured output (JSON or CSV)
- Configurable thread count
- Top 1000 port scan mode
- Improved service fingerprinting

---

## Educational Context

This project was developed as part of my transition into cybersecurity. It represents one of my attempts at implementing core networking concepts in Python and building tools commonly used in security research and penetration testing.

---

## Disclaimer

This tool is intended for educational purposes only.

Only scan systems you own or have explicit permission to test. Unauthorized network scanning may violate laws or network policies.

---

## Author

SantaLauk
