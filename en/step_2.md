## What is NDVI?

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
NDVI stands for Normalised Difference Vegetation Index, but what does that mean? In this section you will learn the basics of NDVI and set up your Python environment to be able to convert images.
</div>
</div>

Plants are typically green in colour, but have you ever wondered why?

The reason most leaves are green is that they contain a chemical called chlorophyll. This chemical helps them to use light from the sun to turn carbon dioxide and water into useful chemicals like glucose, in a process called photosynthesis. Glucose is used by plants as a way of storing energy, and for making other useful chemicals like starch.

Chlorophyll can't use all of the suns light though. Light from the sun comes in many different forms. When you look at a rainbow, you can see several different colours of light. There are forms of light that you can't see though. Ultraviolet light is invisible to humans. It's a type of light that can cause you to get a sunburn. Infrared light is also invisible to humans, but it's the reason you can feel heat when you place your hands in front of a fire. There are also other forms of light that you might have heard of, such as microwaves, radio waves, x-rays and gamma radiation.

Chlorophyll can only use some of the light from the sun to perform photosynthesis. Plants don't like infrared radiation very much, in the same way you wouldn't want to hold your hands in front of a fire for too long. So plants have evolved to reflect as much infrared light as they can.

Modern cameras can detect many of the different types of light. Because a picture from a digital camera, that also showed infrared light, would look a little odd to the human eye, they have special filters added to them, so that infrared light can't reach the sensor. You can see an image below of a park, taken with the infrared filter removed.

![park photo taken without an IR filter](images/original.png)

This is really useful though, for measuring the health of plants. If a plant is healthy, it will reflect a lot of infrared light. If a plant is dying, it will absorb a lot of infrared light. The blue-green colour in the photos means more infrared light is being reflected.

Look at this image of two plants, side by side. You can see which one is healthy, by how blue-green it looks in the image.

![](images/get photo of one of many dying plants in house)

To measure exactly how healthy the plant is, some calculations need to be perfomed on the image, and this is what you will learn in this project.