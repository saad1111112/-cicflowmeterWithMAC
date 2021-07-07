# cicflowmeterWithMAC

% Saad Alabdulsalam

These two files need to be replaced in your tool files to generate the mac column in the CSV file output. 

These files are : flow.py  the location of the file : 
cicflowmeter/flow.py
and packet_flow_key.py : the location of the file
cicflowmeter/features/context/packet_flow_key.py

Note : you can find cicflowmeter in python folder.


So first you need to install the tool ( cicflowmeter) 

pip install cicflowmeter

to use the tool : 

cicflowmeter -f example.pcap -c flows.csv


Thnaks
Saad Alabdulsalam
