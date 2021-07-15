import picamera
import picamera.array
import cv2
import numpy as np

from fastiecm import fastiecm

cam = picamera.PiCamera()
cam.rotation = 180
#cam.resolution = (1920, 1080)
cam.resolution = (2592, 1952)

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
    ndvi = (b.astype(float) - r) /bottom
    ndvi = contrast_stretch(ndvi)
    return ndvi

stream = picamera.array.PiRGBArray(cam)
cam.capture(stream, format='bgr', use_video_port=True)

image = stream.array
cv2.imwrite('original.png', image)

ndvi_image = calc_ndvi(contrast_stretch(image))
cv2.imwrite('ndvi.png', ndvi_image)

ndvi_image = ndvi_image.astype(np.uint8)

color_mapped_image = cv2.applyColorMap(ndvi_image, fastiecm)
cv2.imwrite('color_mapped.png', color_mapped_image)

cam.close()
