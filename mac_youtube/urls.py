#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_youtube


def _cli():
    urls = mac_youtube.urls()
    if urls:
        print("\n".join(urls))


if __name__ == "__main__":
    _cli()
