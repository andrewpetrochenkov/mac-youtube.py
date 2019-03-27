#!/usr/bin/env python
"""print playing urls"""
import mac_youtube


def _cli():
    urls = mac_youtube.playing()
    if urls:
        print("\n".join(urls))


if __name__ == "__main__":
    _cli()
