EC2 Servers:

ec2-54-167-4-20.compute-1.amazonaws.com	Origin server (running Web server on port 8080)

ec2-54-210-1-206.compute-1.amazonaws.com		N. Virginia

ec2-54-67-25-76.us-west-1.compute.amazonaws.com		N. California

ec2-35-161-203-105.us-west-2.compute.amazonaws.com	Oregon

ec2-52-213-13-179.eu-west-1.compute.amazonaws.com	Ireland

ec2-52-196-161-198.ap-northeast-1.compute.amazonaws.com	Tokyo

ec2-54-255-148-115.ap-southeast-1.compute.amazonaws.com	Singapore

ec2-13-54-30-86.ap-southeast-2.compute.amazonaws.com	Sydney

ec2-52-67-177-90.sa-east-1.compute.amazonaws.com	Sao Paolo

ec2-35-156-54-135.eu-central-1.compute.amazonaws.com    Frankfurta


------------------------------------------------------------------------------------

I.	High level approach
a.	DNSSever:
The DNS Server calculates the distance between client and all the replica servers and gives back the IP address of the nearest replica server with the help of active measurements.
1.	Dnsserver.py: It is the main entrance for the dnsserver, run the DNS server.
2.	constructDNS.py: It is used to manage the income packet
3.	questionDNS.py: It is used to define the DNS question format
4.	responsePacket.py: It is used to deal with response packet
5.	unpackDNS.py: It is used to unpack the DNS server
b.	HTTPSever
The main function of this is to deliver the requested content to the client.
1.	Httpserver.py: It is the HTTP server which deal with all income request. It will search the information from the cache, if it is not in the cache, it will ask for the origin server and save the information in the cache.
c.	Mapping
1.	Mapping.py: We will compare all replicated servers with client based on their locations. We will use ipinfodb service get their locations through their IP address, then select the nearest replicate server and return its IP address to the client. 

II.	Running the program:
1.	Run the deployCDN script – The source code is deployed to the DNS server and HTTP Servers to all replica servers.
2.	Run the runCDn script – It will run DNS server and all HTTP servers on all replicated servers.
3.	The dig command should be run on the client in order to get the IP address. Then we can use wget command to request information from the nearest replicated server which the DNS server replied.
4.	Run the stopCDN script – To kill all the processes on the DNS and HTTP servers this is used.

III.	performance enhancing techniques
1.	Use “scp -q” to copy the file into the server which avoid showing too much upload information.
2.	Use scamper command to watch the latency
CHALLENGES FACED:
1: The understanding of the basic requirements took us a long time especially the DNS part which involves packing and unpacking
2: Choosing active or passive measurement was a tough task for us. The passive measurement were fast but active would give better results for servers that were located far hence we chose for active
3: We faced lot of difficulties to execute the program as whole and to track the flow.
4. Let all servers use the same public key make us confused initially, but we know about the private key and public key now.
5. How to find out the best replicated server is the main challenge for us, we test manually and find the algorithm we used before cannot reply the best replicated server. Then we take a long time to improve our algorithm and now it is much more better than before.

