import urllib,math

class mapping:  
    pass   
    
    #The algorithm get the distance between two locations
    def getCompare(self,first, second):  
        if not first or not second:   
            return 0;  
        first.longitude = self.eastToWest(first.longitude, -180, 180);  
        first.latitude = self.leftToWest(first.latitude, -74, 74);  
        second.longitude = self.eastToWest(second.longitude, -180, 180);  
        second.latitude = self.leftToWest(second.latitude, -74, 74);  
        return self.townDown(self.originInt(first.longitude), self.originInt(second.longitude), self.originInt(first.latitude), self.originInt(second.latitude))    
    
    def leftToWest(self,first, second, third):  
        first = max(first,second)  
        first = min(first,third)  
        return first  
      
    def eastToWest(self,first, second, third):  
          
        while first > third:  
            first -= third - second  
        while first < second:  
            first += third - second  
        return first  
                    
    def originInt(self,first):  
        return math.pi * first / 180  
      
    def townDown(self,first, second, third, forth):   
        return 6371000 * math.acos(math.sin(third) * math.sin(forth) + math.cos(third) * math.cos(forth) * math.cos(second - first))  

    def returnIP(self,IP_CLNT):
        IP_REP = ['54.210.1.206', '54.67.25.76', '35.161.203.105','52.213.13.179', '52.196.161.198', '54.255.148.115','13.54.30.86', '52.67.177.90', '35-156-54-135']
        POS_REP =['39.043720245361', '-77.487487792969', '37.774929046631', '-122.41941833496', ' 47.585639953613', '-122.297996521', '53.343990325928', '-6.2671899795532', '35.689506530762', '139.69169616699', '1.2896699905396', '103.85006713867', '-33.867851257324', '151.20732116699', '-23.547500610352', '-46.636108398438', '51.606979370117', '13.312430381775']
        DET_REP = urllib.urlopen('http://api.ipinfodb.com/v3/ip-city/?key=6fbe2ea7db25753b423c2952ff787ed99bdccbf8042e244c7f5a7395f5be4120&ip='+IP_CLNT).read()
        SPLT_DET_REP = DET_REP.split(';')
        print SPLT_DET_REP
        localLocation=mapping()
        #Get the client location and every servers locations
        localLocation.latitude=float(SPLT_DET_REP[-3])
        localLocation.longitude=float(SPLT_DET_REP[-2])
        serverLocation=mapping()
        serverLocation.latitude=float(POS_REP[0])
        serverLocation.longitude=float(POS_REP[1])
        Dis=self.getCompare(localLocation, serverLocation)
        minDistanse = Dis
        minnumber=0;
        m=1
        #Compare each distance return the nearest server to the client
        while (m < 9):
            serverLocation.latitude=float(POS_REP[2*m])
            serverLocation.longitude=float(POS_REP[2*m+1])
            Dis=self.getCompare(localLocation, serverLocation)
            print Dis
            if Dis<minDistanse:
                minnumber=m
                minDistanse=Dis
            m += 1 
        print minnumber  
        return IP_REP[minnumber]      