#!/usr/bin/env python
"""print `true` if youtube video playing, else `false`"""
import mac_youtube


def _cli():
    playing = mac_youtube.playing()
    if playing:
        print("true")


if __name__ == "__main__":
    _cli()
