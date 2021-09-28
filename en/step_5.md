## Calculating NDVI

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now that you have a high contrast image, it's time to do the NDVI calculations. This will take all the blue pixels and make them brighter, and make all the red pixels darker, leaving an image that will be black and white. The brightest pixels in the image indicate healthy plants, and the darkest pixels indicate unhealthy plants or an absence of plants.
![Four images side by side: the original park, the contrasted park, the NDVI, and the contrasted NDVI.](images/ndvi-contrasts.png)
</div>
</div>

--- task ---

Create a new function and call it `calc_ndvi`. It will take a `cv2` image as a parameter.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 19
line_highlights: 32
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


def calc_ndvi(image):
--- /code ---

--- /task ---

To adjust the pixels in the image and only work with red and blue, the image needs splitting into its three seperate channels. `r` for red, `g` for green, and `b` for blue.

--- task ---

Add this line to your function.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 32
line_highlights: 33
---
def calc_ndvi(image):
    b, g, r = cv2.split(image)
--- /code ---

--- /task ---

Now the red and blue channels need to be added together and stored as `bottom`. The blue channel can then have the red channel subtracted (remember that red would mean unhealthy plants or no plants), and then divided by the `bottom` calculation. Because we're doing a division, we also need to make sure that none of our divisors are `0`, or there will be an error.

--- task ---

Add these lines to your function to perform the calculation.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 32
line_highlights: 34-37
---
def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi


--- /code ---

--- /task ---

Now that you have a function to calculate NDVI, you can pass in the contrasted image, display it, and save it.

--- task ---

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 40
line_highlights: 44-46
---
display(original, 'Original')
contrasted = contrast_stretch(park)
display(contrasted, 'Contrasted original')
cv2.imwrite('contrasted.png', contrasted)
ndvi = calc_ndvi(contrasted)
display(ndvi, 'NDVI')
cv2.imwrite('ndvi.png', ndvi)
--- /code ---

--- /task ---

--- task ---

If you have a look at your NDVI image, it will probably be pretty dark, although you might catch patches of brighter pixels. To once again enhance the image, it can be run through the `contrast_stretch` function.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 40
line_highlights: 46-48
---
display(original, 'Original')
contrasted = contrast_stretch(original)
display(contrasted, 'Contrasted original')
cv2.imwrite('contrasted.png', contrasted)
ndvi = calc_ndvi(contrasted)
display(ndvi, 'NDVI')
ndvi_contrasted = contrast_stretch(ndvi)
display(ndvi_contrasted, 'NDVI Contrasted')
cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)
--- /code ---

Now you can see healthy plant life by the brightness of the pixels in the `ndvi_contrasted.png` image.

--- /task ---

--- save ---
