## What is NDVI?

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
NDVI stands for Normalised Difference Vegetation Index, but what does that mean? In this section you will learn the basics of NDVI and set up your Python environment to be able to convert images.
</div>
</div>

Plants are typically green in colour, but have you ever wondered why?

<a title="Rkitko, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Diversity_of_plants_image_version_5.png"><img width="256" alt="Diversity of plants image version 5" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Diversity_of_plants_image_version_5.png/256px-Diversity_of_plants_image_version_5.png"></a>

The reason most leaves are green is that they contain a chemical called chlorophyll. This chemical helps them to use light from the sun to turn carbon dioxide and water into useful chemicals called carbohydrates, in a process called photosynthesis.

<a title="At09kg, Wattcle, Nefronus
At09kg: original
Wattcle: vector graphics
Nefronus: redoing the vector graphics, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Photosynthesis_en.svg"><img width="256" alt="Photosynthesis en" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Photosynthesis_en.svg/256px-Photosynthesis_en.svg.png"></a>

Chlorophyll can't use all of the suns light though. Light from the sun comes in many different forms. When you look at a rainbow, you can see several different colours of light. There are forms of light that humans can't see. Ultraviolet (UV) light is invisible to humans. It's a type of light that can cause you to get a sunburn. Infrared (IR) light is also invisible to humans, but it's the reason you can feel heat when you place your hands in front of a fire. There are also other forms of light that you might have heard of, such as microwaves, radio waves, x-rays and gamma radiation.

<a title="Philip Ronan, Gringer, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:EM_spectrumrevised.png"><img width="512" alt="EM spectrumrevised" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/EM_spectrumrevised.png/512px-EM_spectrumrevised.png"></a>

Chlorophyll can only use some of the light from the sun to perform photosynthesis. Plants don't like infrared radiation very much as it makes them heat up, in the same way you wouldn't want to hold your hands in front of a fire for too long. So plants have evolved to reflect as much infrared light as they can.

<a title="Chlorophyll_ab_spectra2.PNG: Daniele Pugliesi
derivative work: M0tty, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Chlorophyll_ab_spectra-en.svg"><img width="512" alt="Chlorophyll ab spectra-en" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Chlorophyll_ab_spectra-en.svg/512px-Chlorophyll_ab_spectra-en.svg.png"></a>

Modern cameras can detect many of the different types of light. Because a picture from a digital camera, that also showed infrared light, would look a little odd to the human eye, they have special filters added to them, so that infrared light can't reach the sensor. You can see an image below of a park, taken with the infrared filter removed.

![park photo taken without an IR filter](images/park.png)

This is really useful for measuring the health of plants. If a plant is healthy, it will reflect a lot of infrared light. If a plant is dying, it will absorb a lot of infrared light. The blue-green colour in the photos means more infrared light is being reflected.

Look at this image of leaves reflecting light. You can see that infrared light is reflected more from healthy leaves than stressed or dead leaves.

![ASK DESIGN FOR THIS IMAGE TO BE REPLICATED](https://midopt.com/wp-content/uploads/2017/09/Leaves-Reflectance-cmyk-768x383.jpg)

Using a camera without an infrared filter allows us to detect the amount of infrared light that is reflected by plants, and so measure how healthy the plant is.