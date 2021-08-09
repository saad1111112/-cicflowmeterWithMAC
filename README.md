# -cicflowmeterWithMAC
These two files need to be replaced in your tool files to generate the mac column in the CSV file output. 

# cicflowmeterWithMAC

% Saad Alabdulsalam


cicflowmeter tool generates NetFlow from the PCAP file; however, the CSV file output does not provide the MAC address of the source.

To get the mac address in the output, you need to replace two files in the tool. 


These files are: flow.py  the location of the file : 
cicflowmeter/flow.py
and packet_flow_key.py : the location of the file
cicflowmeter/features/context/packet_flow_key.py

Note: you can find cicflowmeter in the python folder.


If you do not have the tool, you need first install it on your device then replace the two files. 


To install the tool :

pip install cicflowmeter

To use it :
 

cicflowmeter -f example.pcap -c flows.csv


Thnaks


Saad Alabdulsalam
