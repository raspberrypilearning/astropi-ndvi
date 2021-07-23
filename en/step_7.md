## Create your own NDVI images

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
For this step you will need to have a Raspberry Pi HQ Camera and some filters, or the Raspberry Pi Noir Camera module. You can then take your own NDVI images, or even enter Mission Space Lab and take NDVI images from the International Space Station.
![dying plant shown with all the various stages of capture](images/dying_plant.png)
</div>
</div>

--- collapse ---
---
title: Converting your Raspberry Pi HQ Camera with a RED + Near IR filter
---

- You will need to purchase a [Red and 850nm NIR filter](https://midopt.com/filters/db660850/).
- Follow [this guide](https://www.raspberrypi.org/documentation/hardware/camera/hqcam_filter_removal.md) to remove the IR filter from your Raspberry Pi HQ Camera. **This will void the warranty**. 
- Follow this video guide to install your filter in your camera.
 <video width="320" height="240" controls>
  <source src="images/fit_filter.mp4" type="video/mp4">
  Your browser does not support mp4 files.
</video> 

--- /collapse ---

--- collapse ---
---
title: Converting your Raspberry Pi HQ Camera with an R26 Red filter
---

- You will need to purchase a sheet of [Rosculux 26: Light Red filters](https://www.pnta.com/expendables/gels/roscolux/roscolux-26-light-red/).
- Follow [this guide](https://www.raspberrypi.org/documentation/hardware/camera/hqcam_filter_removal.md) to remove the IR filter from your Raspberry Pi HQ Camera. **This will void the warranty**. 
- The red filter can be tapped to the front of your HQ camera lens or held in place with a [3D printed part](images/stlfilehere.stl), as shown below.
![HQ camera with a red filter over the lens, held in place by a 3D printed plastic ring](images/3D_print_filter.png)

--- /collapse ---

--- collapse ---
---
title: Using the Raspberry Pi Noir Camera module
---

You can use the Raspberry Pi Noir camera module for NDVI images, however, you will need to change one of your lines of code. This is becuase the Pi Noir camera uses a blue, instead of a red filter.

The line is highlighted and commented in the script below.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 
line_highlights: 26
---
import cv2
import numpy as np
from fastiecm import fastiecm

park = cv2.imread('park.png')


def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)
    
    out_min = 0.0
    out_max = 255.0
    
    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    
    return out


def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (r.astype(float) - b) / bottom # THIS IS THE CHANGED LINE
    return ndvi

contrasted = contrast_stretch(park)
ndvi = calc_ndvi(contrasted)
ndvi_contrasted = contrast_stretch(ndvi)
color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

cv2.imwrite('contrasted.png', contrasted)
cv2.imwrite('ndvi.png', ndvi)
cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
cv2.imwrite('color_mapped.png', color_mapped_image)
--- /code ---

--- /collapse ---

If you need to know how to connect a camera module to the Raspberry Pi, and learn the basics of using the PiCamera module, you can have a look at our [Getting started with the camera module guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera).

--- task ---

With your Raspberry Pi turned off, connect your camera and then restart your Raspberry Pi.

--- /task ---

The first step is to set up the camera to take a photograph. Resolutions of different cameras vary. If you're using the Pi Noir camera then you want to use a resolution of `1920x1080`. If you are using the HQ camera, then you can use a resolution of `2582x1952`.

--- task ---

Add these lines to your code, to setup and use the Raspberry Pi camera. Comment out the line that loads the `park.png` image.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 
line_highlights: 4,5,7,8,9,10
---
import cv2
import numpy as np
from fastiecm import fastiecm
import picamera
import picamera.array

cam = picamera.PiCamera()
cam.rotation = 180
# cam.resolution = (1920, 1080) # Uncomment if using a Pi Noir camera
cam.resolution = (2592, 1952) # Comment this line if using a Pi Noir camera

# park = cv2.imread('park.png') #Comment out this line, as no longer used
--- /code ---

--- /task ---

Rather than just capture an image with the camera and save it to the SD card, the image is going to be captured as an array of pixel data, so that it can be used by `numpy` and `OpenCV`.

--- task ---

Capture a stream and save it as an array. These lines can be called after you `contrast_stretch` and `calc_ndvi` functions.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 35
line_highlights: 36-38
---

stream = picamera.array.PiRGBArray(cam)
cam.capture(stream, format='bgr', use_video_port=True)
image = stream.array

--- /code ---

--- /task ---

Instead of the contrast_stretch function being run on the `park` object, it will now be run on the `image` object.

--- task ---

Edit the line highlighted and commented below, so that the `image` object is passed into the `contrast_stretch` function.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 37
line_highlights: 40
---
cam.capture(stream, format='bgr', use_video_port=True)
image = stream.array

contrasted = contrast_stretch(image) #load image and not park
ndvi = calc_ndvi(contrasted)
--- /code ---

--- /task ---

--- task ---

Add a line near the end of your code, to write out the original image to a file.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 46 
line_highlights: 46
---
cv2.imwrite('original.png', image)
cv2.imwrite('contrasted.png', contrasted)
cv2.imwrite('ndvi.png', ndvi)
cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
cv2.imwrite('color_mapped.png', color_mapped_image)
--- /code ---

--- /task ---

This image shows all the captures of a dying basil plant. You can see that at the base of the plant, the leaves are either dying or dead, where as near the top, there are still some healthy leaves.
![dying plant shown with all the various stages of capture](images/dying_plant.png)

--- save ---