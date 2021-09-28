import cv2
import numpy as np
from fastiecm import fastiecm
from picamera import PiCamera
import picamera.array

cam = PiCamera()
cam.rotation = 180
cam.resolution = (2592, 1952)
stream = picamera.array.PiRGBArray(cam)
cam.capture(stream, format='bgr', use_video_port=True)
original = stream.array

#original = cv2.imread('/home/pi/park.png')


def contrast_stretch(image):
    in_min = np.percentile(image, 5)
    in_max = np.percentile(image, 95)
    
    out_min= 0.0
    out_max = 255.0
    
    out = image - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    
    return out


def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)

    
def calc_ndvi(image):
    b,g,r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) -r) / bottom
    return ndvi


display(original, 'Original')
contrasted = contrast_stretch(original)
display(contrasted, 'Original Contrasted')
ndvi = calc_ndvi(contrasted)
display(ndvi, 'NDVI')
ndvi_contrasted = contrast_stretch(ndvi)
display(ndvi_contrasted, 'NDVI Contrasted')
color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
display(color_mapped_image, 'Color mapped')

cv2.imwrite('contrasted.png', contrasted)
cv2.imwrite('ndvi.png', ndvi)
cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
cv2.imwrite('color_mapped_image.png', color_mapped_image)