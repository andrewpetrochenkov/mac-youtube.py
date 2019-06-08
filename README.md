<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-youtube.svg?longCache=True)](https://pypi.org/project/mac-youtube/)
[![](https://img.shields.io/pypi/v/mac-youtube.svg?maxAge=3600)](https://pypi.org/project/mac-youtube/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-youtube.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-youtube.py/)

#### Installation
```bash
$ [sudo] pip install mac-youtube
```

#### Features
+   `play()`, `pause()`, `playing()`, `urls()` works only in MacOS `Google Chrome.app`

#### Functions
function|`__doc__`
-|-
`mac_youtube.id(url)` |return video id
`mac_youtube.info(video)` |return info dictionary

#### Executable modules
usage|`__doc__`
-|-
`python -m mac_youtube.download url ...` |download youtube video and print path
`python -m mac_youtube.pause` |pause youtube videos
`python -m mac_youtube.play` |continue play youtube video
`python -m mac_youtube.playing` |print playing urls
`python -m mac_youtube.urls` |print youtube urls

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

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>