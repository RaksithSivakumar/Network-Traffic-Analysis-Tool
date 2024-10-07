# Network Traffic Analysis Tool

## Description

The **Network Traffic Analysis Tool** is a Python-based application designed to capture and analyze network traffic in real-time. This tool utilizes the powerful Scapy library to sniff packets and provides a user-friendly interface using Streamlit. The captured packets can be analyzed to detect potential threats and monitor network activity.

## Features

- Capture network packets from selected interfaces.
- Analyze packet details such as source IP, destination IP, and protocol type (TCP, UDP, etc.).
- Visualize captured packet statistics through bar charts.
- Real-time monitoring of network traffic.

## Prerequisites

- Python 3.6 or higher
- Required Python packages:
  - Streamlit
  - Scapy
  - Pandas

You can install the required packages using pip:

pip install streamlit scapy pandas

## Installation

Clone the repository:

git clone https://github.com/yourusername/Network_Traffic_Analysis.git

cd Network_Traffic_Analysis

Install the required dependencies as mentioned in the prerequisites section.

## Usage

Run the application:

streamlit run app.py
Open your web browser and navigate to http://localhost:8501.

Select the desired network interface from the dropdown menu.

Specify the number of packets you wish to capture.

Click the "Start Capture" button to begin capturing packets.

Once the capture is complete, the tool will display the captured packet details and summary statistics.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to create a pull request or open an issue.

## Acknowledgments

Streamlit - for building the web application interface.
Scapy - for packet manipulation and capturing.
Pandas - for data manipulation and analysis.
