# Value Filter
This is a python program that will apply a Value filter to your main screen.

That means it will only show the value of colors in the window. (Value from HSV color space). It can be easily rewritten to do any color filtering though. Here's all possible color conversions [cv2.cvtcolor](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html).

Or you could also convert the colors on your own.

The program is running in the background, so if you press the shortcut at any point, it will open the Filter window.
If you are in Task Manager, the shorcut doesn't work for some reason.

If you have the Filter window open and press pause shorcut, it will freeze and the content won't be updated until you unpause it again (with the same shorcut).

# config.json
`"resolution_downscale"`: how many times will the filter window be smaller than original resolution.
Must be a number, any number (1+)

`"shorcut"`: keys required to start and close the filter window

`"pause"`: keys required to freeze and unfreeze the filter window

# Install
Check out [InstallationGuide.md](InstallationGuide.md).

# Compatibility
The program requires an NVIDIA GPU with CUDA cores. How to check: Find your GPU at the bottom of `Task Manager -> Performance`.

Type into google: does [my gpu] have CUDA cores

# Remove GPU acceleration
If you don't want to utilize this amazing feature, or simply can't (no CUDA cores) - remove `@jit` from `ImageFilter.py`, simple as that.
