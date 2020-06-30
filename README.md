<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-youtube.svg?maxAge=3600)](https://pypi.org/project/mac-youtube/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-youtube.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-youtube.py/actions)

### Installation
```bash
$ [sudo] pip install mac-youtube
```

#### Features
+   `play()`, `pause()`, `playing()`, `urls()` works only in MacOS `Google Chrome.app`

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
    <a href="https://readme42.com/">readme42.com</a>
</p>