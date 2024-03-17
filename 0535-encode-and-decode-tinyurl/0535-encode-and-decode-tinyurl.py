import random
class Codec:
    d={}
    u=random.randint(1,100)
            
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        Codec.d={}
        Codec.u=random.randint(1,100)
        while Codec.u in Codec.d.values():
            Codec.u=random.randint(1,100)
            if Codec.u not in Codec.d.values():
                break
        # Codec.d[longUrl[9:]]= Codec.u
        Codec.d[str(Codec.u)]= longUrl
        print(longUrl[:9]+'tinyurl.com/'+str(Codec.u))
        return (longUrl[:9]+'tinyurl.com/'+str(Codec.u))
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key=shortUrl[:21]
        # print(key)
        # print(Codec.d)
        # print(Codec.d[shortUrl[21:]])
        return (Codec.d[shortUrl[21:]])
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))