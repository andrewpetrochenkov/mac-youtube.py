#!/usr/bin/env python
"""download youtube video and print path"""
import click
import mac_youtube

MODULE_NAME = "mac_youtube.download"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s url ...' % MODULE_NAME


@click.command()
@click.argument('url', nargs=-1, required=True)
def _cli(url):
    for _url in url:
        path = mac_youtube.download(_url)
        print(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
