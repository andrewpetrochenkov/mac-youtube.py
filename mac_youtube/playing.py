#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_youtube


def _cli():
    playing = mac_youtube.playing()
    if playing:
        print("true")


if __name__ == "__main__":
    _cli()
