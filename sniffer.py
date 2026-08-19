
from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

print("=== Basic Network Sniffer ===")
print("1. Capture All Packets")
print("2. Capture TCP Packets")
print("3. Capture UDP Packets")
print("4. Capture ICMP Packets")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    selected_protocol = "ALL"
elif choice == "2":
    selected_protocol = "TCP"
elif choice == "3":
    selected_protocol = "UDP"
elif choice == "4":
    selected_protocol = "ICMP"
else:
    print("Invalid choice.")
    exit()

print(f"\nCapturing {selected_protocol} packets...")
print("Capturing 10 packets...\n")

# Start a fresh report for every capture
with open("capture_report.txt", "w") as report:
    report.write("=== Network Sniffer Capture Report ===\n\n")

tcp_count = 0
udp_count = 0
icmp_count = 0
other_count = 0
total_count = 0

# Ports flagged for review
suspicious_ports = [21, 23, 445, 3389]


def packet_callback(packet):
    global tcp_count, udp_count, icmp_count
    global other_count, total_count

    if IP not in packet:
        return

    if selected_protocol == "TCP" and TCP not in packet:
        return

    if selected_protocol == "UDP" and UDP not in packet:
        return

    if selected_protocol == "ICMP" and ICMP not in packet:
        return

    total_count += 1

    timestamp = datetime.now().strftime("%H:%M:%S")
    source = packet[IP].src
    destination = packet[IP].dst
    size = len(packet)

    alert = "Normal"

    if TCP in packet:
        protocol = "TCP"
        ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
        tcp_count += 1

        if packet[TCP].dport in suspicious_ports:
            alert = "Suspicious TCP Port"

    elif UDP in packet:
        protocol = "UDP"
        ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
        udp_count += 1

        if packet[UDP].dport in suspicious_ports:
            alert = "Suspicious UDP Port"

    elif ICMP in packet:
        protocol = "ICMP"
        ports = "N/A"
        icmp_count += 1

    else:
        protocol = "Other"
        ports = "N/A"
        other_count += 1

    print(f"Time           : {timestamp}")
    print(f"Source IP      : {source}")
    print(f"Destination IP : {destination}")
    print(f"Protocol       : {protocol}")
    print(f"Ports          : {ports}")
    print(f"Packet Size    : {size} bytes")
    print(f"Alert          : {alert}")
    print("-" * 40)

    with open("capture_report.txt", "a") as report:
        report.write(f"Time           : {timestamp}\n")
        report.write(f"Source IP      : {source}\n")
        report.write(f"Destination IP : {destination}\n")
        report.write(f"Protocol       : {protocol}\n")
        report.write(f"Ports          : {ports}\n")
        report.write(f"Packet Size    : {size} bytes\n")
        report.write(f"Alert          : {alert}\n")
        report.write("-" * 40 + "\n")


sniff(count=10, prn=packet_callback, store=False)

print("\nPacket capture completed.")
print("\n=== Capture Summary ===")
print(f"Total Packets : {total_count}")
print(f"TCP Packets   : {tcp_count}")
print(f"UDP Packets   : {udp_count}")
print(f"ICMP Packets  : {icmp_count}")
print(f"Other Packets : {other_count}")

with open("capture_report.txt", "a") as report:
    report.write("\n=== Capture Summary ===\n")
    report.write(f"Total Packets : {total_count}\n")
    report.write(f"TCP Packets   : {tcp_count}\n")
    report.write(f"UDP Packets   : {udp_count}\n")
    report.write(f"ICMP Packets  : {icmp_count}\n")
    report.write(f"Other Packets : {other_count}\n")

