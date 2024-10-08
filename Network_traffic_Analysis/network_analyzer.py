from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
from datetime import datetime

# Global list to store captured packets
captured_packets = []

# Packet analysis function
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        # Determine the protocol type
        if protocol == 6:  # TCP Protocol
            protocol = "TCP"
        elif protocol == 17:  # UDP Protocol
            protocol = "UDP"
        else:
            protocol = "Other"

        # Append packet details to captured packets list
        captured_packets.append({
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'protocol': protocol,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

# Function to capture network packets
def capture_packets(interface, packet_count=10):
    try:
        sniff(iface=interface, prn=packet_callback, store=0, count=packet_count)
    except Exception as e:
        print(f"An error occurred while capturing packets: {e}")

# Function to get captured packets as DataFrame
def get_captured_packets():
    return pd.DataFrame(captured_packets)

# Optionally, you can implement a function to clear the captured packets
def clear_captured_packets():
    global captured_packets
    captured_packets = []

# Example usage (uncomment to run outside of Streamlit context)
# if __name__ == "__main__":
#     interface = "your_network_interface"  # Specify your interface here
#     capture_packets(interface, packet_count=10)
#     df = get_captured_packets()
#     print(df)
