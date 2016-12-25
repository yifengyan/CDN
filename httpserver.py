import httplib2, BaseHTTPServer, sys

global originServerName, localCache, postions
class HTTPServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    #Save the content in the cache if it is not in the replicated server
    def saveInCache(self,info):
        if len(localCache) == 10:
                position = postions[0]
                localCache.pop(position)
                postions.remove(0)
        localCache[self.path] = info
    
    #Search the content in the Cache
    def searchInCache(self):
            self.do_HEAD()
            info = localCache[self.path]
            self.wfile.write(info)
            
    #If the content is not in the replicated server, get the content from the origin server
    def searchFromOrigin(self):
            self.do_HEAD()
            r=httplib2.Http()
            originPath="http://"+originServerName+":8080"+self.path
            sth = r.request(originPath)
            info=sth[1]
            self.wfile.write(info)
            self.saveInCache(info)
    
    #Deal with the Header part of the packet
    def do_HEAD(self):
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
    
    #Deal with the Get Method of the packet
    def do_GET(self):
        if self.path not in localCache:
            postions.append(self.path)
        if self.path in localCache:
            self.searchInCache()
        else:
            self.searchFromOrigin()

portno = int(sys.argv[2])
originServerName = sys.argv[4]
localCache = {}
postions = []
localHost = BaseHTTPServer.HTTPServer(('', portno), HTTPServerHandler)
try:
    localHost.serve_forever()
except KeyboardInterrupt:
    localHost.server_close()
    print "Please do not type anything during the running!"
