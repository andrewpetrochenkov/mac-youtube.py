[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-youtube.svg?longCache=True)](https://pypi.org/pypi/mac-youtube/)
[![](https://img.shields.io/pypi/v/mac-youtube.svg?maxAge=3600)](https://pypi.org/pypi/mac-youtube/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-youtube.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-youtube.py/)

### Install
```bash
$ [sudo] pip install mac-youtube
```

### Features
`Google Chrome.app` only

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

### Todo
+   `mac_youtube.playing()`
+   `mac_youtube.mute()`, `mac_youtube.muted()`, `mac_youtube.unmute()`