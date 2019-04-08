import os, requests, stat

class Adblock:
    
    def __init__(self, hostDic='', hostSrc=[]):
        self.hd = hostDic
        self.hs = hostSrc
    
    def getHosts(self):
        hosts = []
        for url in self.hs:
            try:
                raw_url = requests.get(url, timeout=10).content.decode()
                raw_url = raw_url.replace('\r', '').replace('\t', ' ')
                hosts += raw_url.split('\n')
            except:
                # Feel free to raise error or do whatever
                print(f'Error at {url}')
        return set(i for i in hosts if i and i[0].isdigit())
    
    def parseHosts(self, newHosts):
        os.chmod(self.hd, stat.S_IWRITE)
        data = open(self.hd).read().split('\n')
        if '#PyAds' in data:
            data = data[:data.index('#PyAds') + 1]
        else:
            data.append('#PyAds')
        with open(self.hd, 'w') as hs:
            hs.write('\n'.join(data))
            for line in newHosts:
                try:
                    hs.write(f'\n{line}')
                except:
                    # Feel free to raise error or do whatever
                    pass
        os.chmod(self.hd, stat.S_IREAD)
    
    def cleanHosts(self):
        data = open(self.hd).read().split('\n')
        if '#PyAds' in data:
            data = data[:data.index('#PyAds') + 1]
            os.chmod(self.hd, stat.S_IWRITE)
            with open(self.hd, 'w') as hs:
                hs.write('\n'.join(data))
            os.chmod(self.hd, stat.S_IREAD)