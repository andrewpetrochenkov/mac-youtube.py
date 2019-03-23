#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import google_chrome
import public
import runcmd
import subprocess
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
    """return a list of opened youtube videos"""
    return list(filter(lambda url: "www.youtube.com/" in url, google_chrome.urls()))


@public.add
def id(url):
    """return video id"""
    return url.split("/")[-1] if "=" not in url else url.split("=")[1]

@public.add
def info(video):
    """return info dictionary"""
    url = 'https://www.youtube.com/watch?v=%s' % id(video)
    with youtube_dl.YoutubeDL({'quiet': True}) as ydl:
          return ydl.extract_info(url, download=False)

