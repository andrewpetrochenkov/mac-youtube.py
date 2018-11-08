#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import google_chrome
import mac_icon
import public
import requests
import runcmd

"""
https://rg3.github.io/youtube-dl/
~/Library/Caches/youtube/id/name.ext
"""

CACHES = os.path.expanduser("~/Library/Caches")
OUTPUT_TEMPLATE = "%(title)s.%(ext)s"


@public.add
def pause():
    runcmd.run(["youtube", "pause"])._raise()


@public.add
def play():
    runcmd.run(["youtube", "play"])._raise()


@public.add
def playing():
    return runcmd.run(["youtube", "playing"])._raise().out.splitlines()


@public.add
def urls():
    return list(filter(lambda url: "www.youtube.com/" in url, google_chrome.urls()))


@public.add
def id(url):
    return url.split("/")[-1] if "=" not in url else url.split("=")[1]


def _download_path(folder):
    if os.path.exists(folder):
        for l in os.listdir(folder):
            return os.path.join(folder, l)


@public.add
def download(url):
    folder = os.path.join(CACHES, "youtube", id(url))
    if _download_path(folder):
        return _download_path(folder)
    output = os.path.join(folder, OUTPUT_TEMPLATE)
    url = "https://www.youtube.com/watch?v=%s" % id(url)
    args = ["youtube-dl", "-o", "'%s'" % output, "--no-cache-dir", url]
    code = os.system("%s 1>&2" % " ".join(args))
    thumbnail_url = "https://img.youtube.com/vi/%s/hqdefault.jpg" % id(url)
    thumbnail_path = "/tmp/thumbnail.jpg"

    r = requests.get(thumbnail_url)
    with open(thumbnail_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    path = _download_path(folder)
    mac_icon.update(path, thumbnail_path)
    return path
