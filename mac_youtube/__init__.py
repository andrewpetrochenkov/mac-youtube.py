#!/usr/bin/env python
# -*- coding: utf-8 -*-
import google_chrome
from public import public
import runcmd


@public
def pause():
    runcmd.run(["youtube", "pause"])._raise()


@public
def play():
    runcmd.run(["youtube", "play"])._raise()


@public
def playing():
    return runcmd.run(["youtube", "playing"])._raise().out.splitlines()


@public
def urls():
    return list(filter(lambda url: "www.youtube.com/" in url, google_chrome.urls()))
