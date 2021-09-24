## Increasing the contrast

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Contrast is the difference between the brightness or colour in an image. The image below has been split so that the left half has a low contrast and the right side has a high contrast. You need to **increase** the contrast of your image for NDVI.
<a title="Toniht at English Wikipedia, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Photo_editing_contrast_correction.jpg"><img width="512" alt="Photo editing contrast correction" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Photo_editing_contrast_correction.jpg/512px-Photo_editing_contrast_correction.jpg"></a>
</div>
</div>

--- task ---

Create a new function called `contrast_stretch`. It will have a single parameter that will be the `cv2` image object that has been loaded. The function should come after the image has been loaded.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 1 
line_highlights: 19
---
import cv2
import numpy as np

original = cv2.imread('/home/pi/park.png')


def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def contrast_stretch(im):
--- /code ---

--- /task ---

The image object called `park` is just a big list of numbers. The next step is to find the largest and smallest of those numbers, using `numpy`.

--- task ---

Add these two lines to your function to find the top brightness of pixels in the image in the top 5% and bottom 5% of your image.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 19 
line_highlights: 20-21
---
def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

--- /code ---

--- /task ---

Now you need to set the maximum brightness and minimum brightness on the new image you are going to create. The brightest a pixel's colour can be is 255, and the lowest is 0.

--- task ---

Add these lines to your function.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 19 
line_highlights: 23-24
---
def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0
--- /code ---

--- /task ---

Now some calculations need to be performed to change all the pixels in the image, so that the image has the full range of contrasts from 0 to 255.

--- task ---

Add these lines to stretch out the pixel values and return the contrasted image.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 19 
line_highlights: 26-30
---
def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    
    return out
--- /code ---

--- /task ---

Now that you have a function to stretch the contrast of the image, you can convert your image and display it on the screen.

--- task ---

Call your `contrast_stretch` function, and alter then display it using your `display` function.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 33 
line_highlights: 34, 35
---
display(original, 'Original')
contrasted = contrast_stretch(original)
display(contrasted, 'Contrasted original')
--- /code ---
--- /task ---

There should be a noticable difference in the contrast of the two images now.

![Low and high contrast images of the park image.](images/low-high-contrast.png)

--- task ---

You can save your high contrast image by adding a single line to the end of your code, so that you can compare the two images in your file browser. It will be called `contrasted.png`.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 33 
line_highlights: 36
---
display(original, 'Original')
contrasted = contrast_stretch(park)
display(contrasted, 'Contrasted original')
cv2.imwrite('contrasted.png', contrasted)
--- /code ---

--- /task ---

--- save ---
