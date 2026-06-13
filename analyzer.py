from scapy.all import *
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

protocol_counter = Counter()
ip_counter = Counter()

total_bytes = 0

def packet_callback(packet):

    global total_bytes

    total_bytes += len(packet)

    if packet.haslayer(IP):

        ip_counter[packet[IP].src] += 1

    if packet.haslayer(TCP):
        protocol_counter["TCP"] += 1

    elif packet.haslayer(UDP):
        protocol_counter["UDP"] += 1

    elif packet.haslayer(ICMP):
        protocol_counter["ICMP"] += 1

print("Monitoring for 60 seconds...")

sniff(prn=packet_callback, store=False, timeout=60)

print("\nProtocols")
print(protocol_counter)

print("\nTop Talkers")
print(ip_counter.most_common(10))

print(f"\nTotal MB: {total_bytes/(1024*1024):.2f}")

# Step 12: Export to CSV

df = pd.DataFrame(

    ip_counter.items(),

    columns=["IP Address", "Packet Count"]

)

df.to_csv("traffic_report.csv", index=False)

print("CSV report saved.")

plt.bar(
    protocol_counter.keys(),
    protocol_counter.values()
)

plt.title("Protocol Distribution")
plt.xlabel("Protocol")
plt.ylabel("Packets")

plt.savefig("protocol_chart.png")

plt.show()
