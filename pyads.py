#       pyads.py, simple adblocker using hosts file.
#
#       Copyright 2019 Khaled El-Morshedy <elmoiv>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License 3 as published by
#       the Free Software Foundation.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os, requests, stat, re

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
                print(f'Loaded: {url}')
            except:
                # Feel free to raise error or do whatever
                print(f'Error at: {url}')
        return set(i for i in hosts if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*", i))
    
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
