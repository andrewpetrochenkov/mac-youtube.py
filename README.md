[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-youtube.svg?longCache=True)](https://pypi.org/pypi/mac-youtube/)
[![](https://img.shields.io/pypi/v/mac-youtube.svg?maxAge=3600)](https://pypi.org/pypi/mac-youtube/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-youtube.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-youtube.py/)

### Install
```bash
$ [sudo] pip install mac-youtube
```

### Features
+   `play()`, `pause()`, `playing()`, `urls()` works only in MacOS `Google Chrome.app`

### Examples
```python
>>> import mac_youtube
>>> mac_youtube.urls()
['https://www.youtube.com/watch?v=cvaIgq5j2Q8','https://www.youtube.com/watch?v=YrhYhI3L32c']
>>> mac_youtube.play()
>>> mac_youtube.playing()
['https://www.youtube.com/watch?v=cvaIgq5j2Q8']
>>> mac_youtube.pause()
```

download
```python
>>> mac_youtube.download('https://www.youtube.com/watch?v=cvaIgq5j2Q8')
'~/Library/Caches/youtube/IzpVGLv6JoU/Nightcore - Angel With A Shotgun.mp4'
```