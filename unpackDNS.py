import struct
#Unpack DNS server
def UPCK_DNS (content, OST):
        L = []
        while True:
                LEN, = struct.unpack_from("!B", content, OST)
                if (LEN & 192) == 192:
                        PTR, = struct.unpack_from("!H", content, OST)
                        OST = OST + 2
                        return L + UPCK_DNS(content, PTR & 16383), OST
                OST += 1
                if LEN == 0:
                        return L, OST
                L.append(*struct.unpack_from("!%ds" % LEN, content, OST))
                OST = OST + LEN