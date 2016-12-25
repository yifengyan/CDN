import struct,questionDNS

#Manage the income packet
def MSG_DCODE_DNS(content):
    HDR_DNS = struct.Struct("!6H")
    D_H=HDR_DNS.unpack_from(content)
    OST = HDR_DNS.size
    CNT_q=D_H[2]
    IDENT=D_H[0]       
    sth = questionDNS.QUES_DNS_UPCK(content, OST, CNT_q)
    QUER=sth[0]
    OST=sth[1]
    NAM_D = QUER[0]['domain_name']
    NAM = ""
    for moreWord in NAM_D:
            if NAM_D.index(moreWord) == len(NAM_D) - 1:
                    NAM = NAM + moreWord
            else:
                    NAM = NAM + moreWord + "."
    return NAM,IDENT