#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import google_chrome
import mac_icon
import public
import requests
import runcmd
import subprocess
import tempfile
import youtube_dl


@public.add
def pause():
    """pause youtube videos"""
    code = """
repeat with w in every window
    repeat with t in every tab of w
        if "youtube" is in (get URL of t) then
            tell t
                set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('audio,video'),function(elem){return elem.duration > 0 && !elem.paused})"
                if is_playing is true then
                    execute javascript "document.getElementsByClassName('ytp-play-button ytp-button')[0].click();"
                end if
            end tell
        end if
    end repeat
end repeat
"""
    return google_chrome.tell(code)


@public.add
def play():
    """continue play youtube video"""
    code = """
repeat with w in every window
    repeat with t in every tab of w
        if "youtube" is in (get URL of t) then
            tell t
                set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('audio,video'),function(elem){return elem.duration > 0 && !elem.paused})"
                if is_playing is false then
                    execute javascript "document.getElementsByClassName('ytp-play-button ytp-button')[0].click();"
                end if
            end tell
        end if
    end repeat
end repeat
"""
    return google_chrome.tell(code)

@public.add
def playing():
    """return True if youtube video is playing"""
    code = """
repeat with w in every window
    repeat with t in every tab of w
        if "youtube" is in (get URL of t) then
            tell t
                set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('audio,video'),function(elem){return elem.duration > 0 && !elem.paused})"
                if is_playing is true then
                    log (get URL of t)
                end if
            end tell
        end if
    end repeat
end repeat
    """
    return google_chrome.tell(code).out.splitlines()

@public.add
def urls():
    """return list of opened youtube videos"""
    return list(filter(lambda url: "www.youtube.com/" in url, google_chrome.urls()))


@public.add
def id(url):
    """return video id"""
    return url.split("/")[-1] if "=" not in url else url.split("=")[1]

@public.add
def info(id):
    """return info dictionary"""
    url = 'https://www.youtube.com/watch?v=%s' % id
    with youtube_dl.YoutubeDL({'quiet': True}) as ydl:
          return ydl.extract_info(url, download=False)

@public.add
def download_thumbnail(video):
    """download thumbnail and return path"""
    url = "https://www.youtube.com/watch?v=%s" % id(video)
    info = mac_youtube.info(id(video))
    path = tempfile.mkstemp()[1]
    with open(thumbnail_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return path

@public.add
def download(video,dst):
    """download youtube video and set Finder Icon"""
    url = "https://www.youtube.com/watch?v=%s" % id(video)
    if os.path.dirname(dst) and not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    args = ["youtube-dl", "-o", "'%s'" % dst, "--no-cache-dir", url]
    process = subprocess.Popen(args).communicate()
    process.communicate()
    out, err = process.communicate()
    code = process.returncode
    if code!=0:
        raise OSError(err.decode("utf-8"))
