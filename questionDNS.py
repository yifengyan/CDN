import struct,unpackDNS
#Define the DNS question format
def QUES_DNS_UPCK(content, OST, COUNT_QUES):
    QUERY = []
    FORMT_QUER_DNS = struct.Struct("!2H")
    for i in range(COUNT_QUES):
        sth1 = unpackDNS.UPCK_DNS(content, OST)
        NAM_QUE=sth1[0]
        OST=sth1[1]
        sth2 = FORMT_QUER_DNS.unpack_from(content, OST)
        TYP_Q=sth2[0]
        CLS_Q=sth2[1]
        OST = OST + FORMT_QUER_DNS.size
        QUEST = {"domain_name": NAM_QUE,
                    "query_type": TYP_Q,
                    "query_class": CLS_Q}
        QUERY.append(QUEST)
    return QUERY, OST