# Network Traffic Analyzer

## Overview

The Network Traffic Analyzer is a Python-based cybersecurity project that captures and analyzes live network traffic using Scapy. The tool monitors packet activity, identifies network protocols, tracks active hosts, measures bandwidth usage, exports traffic statistics, and generates visual reports.

This project was developed on Kali Linux as part of a hands-on cybersecurity learning path focused on network analysis and packet inspection.

---

## Features

- Live packet capture using Scapy
- Protocol detection (TCP, UDP, ICMP)
- Top-talker identification
- Bandwidth utilization measurement
- CSV report generation
- Protocol distribution visualization
- Traffic statistics collection
- Linux command-line execution

---

## Technologies Used

- Python 3
- Scapy
- Pandas
- Matplotlib
- Kali Linux

---

## Project Structure

```text
network-traffic-analyzer/
│
├── analyzer.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── screenshots/
│   ├── analyzer-running.png
│   ├── protocol-chart.png
│   └── csv-report.png
│
├── output/
│   ├── protocol_chart.png
│   └── sample_traffic_report.csv
│
└── docs/
    └── architecture-diagram.png
```

---

## How It Works

1. Scapy captures live packets from the network interface.
2. Packets are inspected and categorized by protocol.
3. Source IP addresses are tracked to identify the most active hosts.
4. Packet sizes are measured to calculate bandwidth usage.
5. Results are exported to a CSV file.
6. Matplotlib generates protocol distribution charts.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/network-traffic-analyzer.git

cd network-traffic-analyzer
```

Create a virtual environment:

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the analyzer with administrator privileges:

```bash
sudo python analyzer.py
```

The analyzer will:

- Capture network traffic
- Analyze protocols
- Track active hosts
- Measure traffic volume
- Generate reports
- Create visualizations

---

## Example Output

```text
Monitoring for 60 seconds...

Protocols
Counter({'TCP': 248, 'UDP': 41, 'ICMP': 8})

Top Talkers
192.168.1.100 512
8.8.8.8 133

Total MB: 3.41
```

---

## Skills Demonstrated

- Network Traffic Analysis
- Packet Inspection
- Network Protocols
- Python Programming
- Linux Administration
- Data Analysis
- Data Visualization
- Cybersecurity Fundamentals

---

## Future Improvements

- DNS Query Monitoring
- Port Analysis
- Real-Time Dashboard
- PCAP Export Support
- Threat Detection Alerts
- Packet Filtering
- GUI Interface

---

## Acknowledgements

This project was inspired by the Network Traffic Analyzer project idea from:

https://github.com/CarterPerez-dev/Cybersecurity-Projects

The implementation, testing, documentation, and enhancements in this repository were completed independently as a learning project.

---

## Author

[Your Name]

Cybersecurity Student | Python | Network Security | Linux
