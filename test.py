import pyads

hostDic = r'C:\Windows\System32\drivers\etc\hosts'
hostSrc =   [
            'https://adaway.org/hosts.txt',
            'https://hosts-file.net/ad_servers.txt'
            ]

adblock = pyads.Adblock(hostDic, hostSrc)
adblock.parseHosts(adblock.getHosts())