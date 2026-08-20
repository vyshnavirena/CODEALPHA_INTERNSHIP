# Basic Network Sniffer

## 1. Project Objective

The Basic Network Sniffer is a Python-based network monitoring tool that captures and analyzes network packets. It displays important packet information such as source IP, destination IP, protocol, ports, packet size, and timestamp.

## 2. Technologies Used

* Python
* Scapy
* VS Code
* Windows

## 3. Features

* Capture network packets
* Capture all IP packets
* Filter TCP packets
* Filter UDP packets
* Filter ICMP packets
* Display source and destination IP addresses
* Display port information
* Display packet size
* Display packet timestamp
* Identify selected suspicious ports
* Generate a capture report

## 4. How the System Works

1. The user starts the Python program.
2. The program displays four capture options.
3. The user selects a protocol.
4. Scapy captures matching network packets.
5. The program extracts packet information.
6. The information is displayed in the terminal.
7. The captured information is saved in `capture_report.txt`.
8. A capture summary is displayed after the capture is completed.

## 5. Packet Information Captured

For each packet, the program can display:

* Timestamp
* Source IP
* Destination IP
* Protocol
* Source and destination ports
* Packet size
* Alert status

## 6. Testing Results

### TCP Test

TCP packet capture was successfully tested.

Example result:

* TCP Packets: 1
* Destination Port: 443
* Alert: Normal

### UDP Test

UDP packet capture was successfully tested.

Example result:

* UDP Packets: 6
* TCP Packets: 0
* ICMP Packets: 0

### All-Packet Test

The program successfully captured network traffic when the "Capture All Packets" option was selected.

### ICMP Test

The ICMP option is included in the program, but ICMP packets were not successfully captured during testing.

## 7. Output Report

The program stores captured packet information in:

`capture_report.txt`

The report contains packet details and a capture summary.

## 8. Future Enhancements

* Real-time packet graphs
* Advanced intrusion detection
* IP reputation checking
* More detailed protocol analysis
* Export reports to CSV
* Graphical user interface
* Improved network-interface selection
* Advanced alert and threat detection

## 9. Conclusion

The project demonstrates the basic principles of network packet capture and analysis using Python and Scapy. It provides a simple way to monitor network traffic and understand important packet information.

