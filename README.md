[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-youtube.svg?longCache=True)](https://pypi.org/project/mac-youtube/)
[![](https://img.shields.io/pypi/v/mac-youtube.svg?maxAge=3600)](https://pypi.org/project/mac-youtube/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-youtube.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-youtube.py/)

#### Install
```bash
$ [sudo] pip install mac-youtube
```

#### Features
+   `play()`, `pause()`, `playing()`, `urls()` works only in MacOS `Google Chrome.app`

#### Functions
function|`__doc__`
-|-
`mac_youtube.download(video, dst)`|download youtube video and set Finder Icon
`mac_youtube.download_thumbnail(video)`|download thumbnail and return path
`mac_youtube.id(url)`|return video id
`mac_youtube.info(id)`|return info dictionary
`mac_youtube.pause()`|pause youtube videos
`mac_youtube.play()`|continue play youtube video
`mac_youtube.playing()`|return True if youtube video is playing
`mac_youtube.urls()`|return list of opened youtube videos

#### CLI
usage|`__doc__`
-|-
`python -m mac_youtube.download url ...`|download youtube video and print path
`python -m mac_youtube.pause`|pause youtube videos
`python -m mac_youtube.play`|continue play youtube video
`python -m mac_youtube.playing`|print `true` if youtube video playing, else `false`
`python -m mac_youtube.urls`|print youtube urls

#### Examples
```python
>>> import mac_youtube
>>> mac_youtube.urls()
['https://www.youtube.com/watch?v=cvaIgq5j2Q8','https://www.youtube.com/watch?v=YrhYhI3L32c']
>>> mac_youtube.play()
>>> mac_youtube.playing()
['https://www.youtube.com/watch?v=cvaIgq5j2Q8']
>>> mac_youtube.pause()
```

info
```python
>>> info = mac_youtube.info("cvaIgq5j2Q8")
>>> "%s.%s" % (info["title"], info["ext"])
'Nightcore - Angel With A Shotgun.webm'
```

download
```python
>>> mac_youtube.download('https://www.youtube.com/watch?v=cvaIgq5j2Q8', "title.webm")
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>