import struct
#Deal with the response packet
def PCKT_RES(NAM,IP_REP_FIN,IDENT):
    PCKT = struct.pack("!H", IDENT)+struct.pack("!H", 32768)+struct.pack("!H", 1)+struct.pack("!H", 1)+struct.pack("!H", 0)+struct.pack("!H", 0)         
    NAM_SPLT = NAM.split(".")
    for m in NAM_SPLT:
        PCKT += struct.pack("!B", len(m))
        for n in bytes(m):
            PCKT += struct.pack("!c", n)
    PCKT += struct.pack("!B", 0)+struct.pack("!H", 1)+struct.pack("!H", 1)+struct.pack("!H",49164)+struct.pack("!H", 1)+struct.pack("!H", 1)+struct.pack("!I", 0)+struct.pack("!H", 4)            
    split_final_replica_ip = IP_REP_FIN.split(".")
    for ip_piece in split_final_replica_ip:
        PCKT += struct.pack("!B", int(ip_piece))
    return PCKT