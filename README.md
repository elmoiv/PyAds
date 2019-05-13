# PyAds
Simple ad blocker using the hosts file.


# Features
- You can block as many ad providers as you want.
- Your cat can use this code.

# How to Use
```
import pyads

adblock = pyads.Adblock(hostDic, hostSrc)

adblock.parseHosts(adblock.getHosts())
```
- _hostDic_ : Location of the system hosts file.
- _hostSrc_ : List, tuple or set containing urls with hosts raw data _see [test.py](test.py)_.

- if you want to revert the hosts file back:
```
adblock.cleanHosts()
```


*MUST RUN THIS SCRIPT WITH ADMIN PRIVILEGES*
