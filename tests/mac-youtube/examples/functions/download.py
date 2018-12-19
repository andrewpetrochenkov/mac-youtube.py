#!/usr/bin/env python
import mac_youtube

url = "https://www.youtube.com/watch?v=7M-jsjLB20Y"
dst="/tmp/youtube"
path = mac_youtube.download(url,dst)
print(path)
