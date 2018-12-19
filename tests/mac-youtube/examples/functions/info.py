#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_youtube

info = mac_youtube.info("cvaIgq5j2Q8")
print("title: %s" % info["title"])
print("ext: %s" % info["ext"])
print("thumbnail: %s" % info["thumbnail"])
print(info.keys())
