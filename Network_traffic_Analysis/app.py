import streamlit as st
from scapy.all import conf, get_if_list
from network_analyzer import capture_packets, get_captured_packets
import threading

# Function to start capturing packets
def start_capture(interface, packet_count):
    capture_packets(interface, packet_count)
    st.success("Packet capture completed!")

# Streamlit app layout
st.title("Network Traffic Analysis Tool")

# List available network interfaces
interfaces = get_if_list()

# Display available network interfaces in Streamlit
st.write("Available Network Interfaces:", interfaces)

# Select the interface for capturing packets
interface = st.selectbox("Select the network interface:", interfaces)

# Select the number of packets to capture
packet_count = st.number_input("Number of packets to capture:", min_value=1, max_value=1000, value=10)

# Button to start capturing packets
if st.button("Start Capture"):
    st.write(f"Capturing {packet_count} packets on interface {interface}...")
    
    # Start the capture in a separate thread
    capture_thread = threading.Thread(target=start_capture, args=(interface, packet_count))
    capture_thread.start()

# If packets are captured, display analysis
packets_df = get_captured_packets()
if not packets_df.empty:
    st.write("Captured Packets:")
    st.dataframe(packets_df)

    st.write("Summary of Captured Traffic:")
    protocol_count = packets_df['protocol'].value_counts()
    st.bar_chart(protocol_count)
