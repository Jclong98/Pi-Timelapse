# Pi Timelapse

Usage: run `python main.py` with any of the following arguments.

| arg             | description         | default |
| --------------- | ------------------- | ------- |
| -o --output     | Output directory    | ./      |
| -dY --d-years   | duration in years   | 0       |
| -dH --d-hours   | duration in hours   | 0       |
| -dM --d-minutes | duration in minutes | 0       |
| -dS --d-seconds | duration in seconds | 0       |
| -dD --d-days    | duration in day     | 0       |
| -iH --i-hours   | interval in hours   | 0       |
| -iM --i-minutes | interval in minutes | 0       |
| -iS --i-seconds | interval in seconds | 0       |
| -iD --i-days    | interval in day     | 0       |

If you don't use any of the duration arguments, the duration will default to `100 years`.

If you don't use any of the interval arguments, the interval will default to `15 minutes`.

---

Use the following command to create a video of the output images

```
ffmpeg -framerate 8 -i ./path/to/files/%d.jpg ./path/to/files/output.mp4
```

