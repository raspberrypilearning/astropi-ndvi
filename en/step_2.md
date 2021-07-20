## What is NDVI

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
NDVI stands for Normalised Difference Vegetation Index, but what does that mean? In this section you will learn the basics of NDVI and set up your Python environment to be able to convert images.
</div>
</div>

--- task ---

On your Raspberry Pi, open a terminal by pressing and holding the **Ctrl** and **Alt** keys and then pressing the **t** key.

--- /task ---

This project requires some extra Python packages to perform some calculations on the images.

--- task ---

In the terminal type:

```bash
sudo pip3 install numpy openvc-python3
```

The packages should install after a few minutes.

--- /task ---

--- task ---

Open up **Thonny** from the **Programming** menu.

--- /task ---

To begin with you are simple going to load an image and display it on your screen.

--- task ---

Right click on this image, and save it to your home folder on the Raspberry Pi.

![an IR image of a park](images/park.png)

--- /task ---

--- task ---

Then in Thonny you can start by importing the two modules you will need to begin with.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 1
line_highlights: 1-2
---
import cv2
import numpy as np
--- /code ---

--- /task ---

The next stage is to load an image and display it on the screen.

--- task ---

- `cv2.imread` is used to load an image
- `cv2.namedWindow` is used to create a display window
- `cv2.imshow` is used to show an image in a window.
- `cv2.waitKey` stops the window from vanishing, until a key is pressed.

Here is the code you will need.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 1
line_highlights: 4-7
---
import cv2
import numpy as np

original = cv2.imread('original.png')
cv2.namedWindow('Display')
cv2.imshow('Display', original)
cv2.waitKey(0)
--- /code ---

--- /task ---

--- task ---

Now run your code. You should see the image appear on the screen. When you press a key it will disappear.

--- /task ---

--- collapse ---
---
title: "Debug: The image is too big for my monitor!"
---

You can resize images and display the resized image.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
import cv2
import numpy as np

original = cv2.imread('original.png')
cv2.namedWindow('Display')
resized = cv2.resize(original, (648, 488)) #resize the image
cv2.imshow('Display', resized) #display the resized image
cv2.waitKey(0)
--- /code ---

--- /collapse ---

--- save ---