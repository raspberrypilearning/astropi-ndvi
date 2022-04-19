## Load and display images with Python

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
To turn an image from one that has had no IR filter, to an NDVI image, you're going to use a graphics module called OpenCV.
</div>
</div>

--- task ---

On your Raspberry Pi, open a terminal by pressing and holding the <kbd>Ctrl</kbd> and <kbd>Alt</kbd> keys, and then pressing the <kbd>t</kbd> key.

--- /task ---

This project requires some extra Python packages to perform some calculations on the images.

--- task ---

In the terminal type:

```bash
sudo pip3 install -U numpy
sudo pip3 install opencv-python
sudo apt install libatlas-base-dev
```

The packages should install after a few minutes.

--- /task ---

--- task ---

Open up **Thonny** from the **Programming** menu.

--- /task ---

To begin with, you are simply going to load an image and display it on your screen.

--- task ---

Right click on this image, and save it to your home folder on your Raspberry Pi.

![An infrared image of a park.](images/park.png)

--- /task ---

--- task ---

Then in Thonny, start by importing the two modules you will need to begin with.

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

- `cv2.imread` is used to load an image
- `np.array(original, dtype=float)/float(255)` is used to convert the image to an array with the correct type
- `cv2.namedWindow` is used to create a display window
- `cv2.imshow` is used to show an image in a window
- `cv2.waitKey` stops the window from vanishing, until a key is pressed
- `cv2.destroyAllWindows()` closes the window when the key has been pressed

--- task ---
Here is the code you will need. Don't forget to use your own `username` for you home directory.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 1
line_highlights: 4-9
---
import cv2
import numpy as np

image = cv2.imread('/home/username/park.png') # load image
image = np.array(image, dtype=float)/float(255) #convert to an array
cv2.namedWindow('Original') # create window
cv2.imshow('Original', image) # display image
cv2.waitKey(0) # wait for key press
cv2.destroyAllWindows()
--- /code ---

--- /task ---

--- task ---

Now run your code. You should see the image appear on the screen. When you press a key, it will disappear.

--- /task ---

The image may be too big for your screen, but that can be fixed by scaling the image.

--- task ---

First you need to get the width and height of the image you are using, and then scale the values down. In the example below, the image height and width are divided by `2`, but you could use a different value to scale them more or less.
Add the highlighted code below.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 4
line_highlights: 6-8
---
image = cv2.imread('/home/username/park.png') # load image
image = np.array(original, dtype=float)/float(255) #convert to an array
shape = image.shape
height = int(shape[0]/2)
width = int(shape[1]/2)
cv2.namedWindow('Original') # create window
--- /code ---

--- /task ---

--- task ---

Now resize the image before displaying it, by adding the highlighted code.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 6
line_highlights: 10
---
shape = image.shape
height = in(shape[0] / 2)
width = int(shape[1] / 2)
image = cv2.resize(image, (width, height))
cv2.namedWindow('Original') # create window
--- /code ---

--- /task ---

--- task ---

As you will want to display other images as well, you can turn the code you have written into a function, and call it. The function will take an **image object** and also a **string** that describes the image.

Here is the complete code, so far.

--- code ---
---
language: python
filename: ndvi.py
line_numbers: true
line_number_start: 1
line_highlights: 7-19
---
import cv2
import numpy as np

original = cv2.imread('/home/username/park.png')


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


display(original, 'Original')
--- /code ---

--- /task ---

--- save ---
