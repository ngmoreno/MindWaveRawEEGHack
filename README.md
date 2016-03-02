# What is raweeg?

This program will output the raw data from the Mindwave Mobile.
See line 39 in sniff.py to access integer datapoint, "rawdata".

# Dependencies and Notes:
  - python 2.7.11
  - scapy 2.3.2
  - matplotlib 1.5.1
  
Dev platform: Mac OS X 10.11.3

To install using pip, execute the following in Terminal:
  - sudo pip install matplotlib scapy

# HOW TO USE

1. run ThinkGear Connector (keep it running)
2. run Brainwave Visualizer (keep it running)
3. make sure Mindwave Mobile is connected
4. run Terminal
5. navigate to raweeg/ directory 
6. execute in Terminal: 
  - sudo python sniff.py
  - < press enter if prompted >

