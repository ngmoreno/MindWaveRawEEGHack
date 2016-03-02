from scapy.all import *
import datetime
import graph


class RAWEEG_packet_sniffer:
	
	def __init__(self):
		# here for measuring sampling rate
		self.new_clock = 0
		self.old_clock = 0
		self.Hz = 0
		self.grph = graph.rt_2D_graph()
		self.rawData = 0
	
	
	def pkt_callback(self,pkt):

		# convert packet into ascii string
		p = str(pkt)

		# store index of "rawEeg" key
		raweeg = p.find("rawEeg")

		# store index of ending char
		e = p.find("}")
		
		# checks if p is target packet
		if raweeg > -1 and e > -1:

			# "{'rawEeg': 123 }" = p[raweeg-2:e+1]
			dstr = p[raweeg-2:e+1]

			if len(dstr) > 6:
				# evaluates the dictionary string
				d = eval(dstr)

				if d.get('rawEeg') != None:
					self.rawData = int(d['rawEeg'])
					self.grph.update(self.rawData)
					

					#self.Hz += 1
					#if self.Hz == 10:
					#	self.grph.update(self.rawData)
					#	self.rawData = []
					
					#self.new_clock = int(datetime.datetime.strftime(datetime.datetime.now(), '%S'))
					#if self.new_clock-self.old_clock > 0:
					#	self.old_clock = self.new_clock
					#	self.Hz = 0

raweeg_ps = RAWEEG_packet_sniffer()

sniff(iface="lo0", prn=raweeg_ps.pkt_callback, filter="ip", store=0)


