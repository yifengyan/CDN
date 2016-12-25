all:
	chmod +x dnsserver
	chmod +x httpserver
	chmod +x deployCDN
	chmod +x runCDN
	chmod +x stopCDN
	chmod +x constructDNS.py
	chmod +x dnsserver.py
	chmod +x httpserver.py
	chmod +x mapping.py
	chmod +x questionDNS.py
	chmod +x responsePacket.py
	chmod +x unpackDNS.py
	dos2unix deployCDN
	dos2unix runCDN
	dos2unix stopCDN