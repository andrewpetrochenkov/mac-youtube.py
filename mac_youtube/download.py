#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import mac_youtube


PROG_NAME = 'python -m mac_youtube.download url ...'


@click.command()
@click.argument('url', nargs=-1, required=True)
def _cli(url):
    for _url in url:
        path = mac_youtube.download(_url)
        print(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
