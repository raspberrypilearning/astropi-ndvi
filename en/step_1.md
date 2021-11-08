## Introduction

[[[camera-bullseye]]]

In this project, you will learn how to use images, taken with a camera fitted with special filters, to measure the health of plants. If you have access to a [Raspberry Pi High Quality Camera](https://www.raspberrypi.org/products/raspberry-pi-high-quality-camera/), you will also learn how to modify it so the camera can be used to take these photos. If you have access to a [Pi NoIR camera module](https://www.raspberrypi.org/products/pi-noir-camera-v2/), this can be used too.

![Three images showing the three stages of processing photos to get a measure of plant health.](images/montage.png)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Filters**</span> can be used on cameras to prevent some wavelengths of light from reaching the sensor. For instance, most digital cameras have an infrared filter to stop infrared light from reaching the sensor.
</p>

You will:
+ Learn what is meant by Normalised Difference Vegetation Index (NDVI)
+ Convert an image taken with a modified camera so that it can be used to measure NDVI
+ Modify a Raspberry Pi camera module, so it can be used to take NDVI images

You will need:
+ A Raspberry Pi computer
+ Optionally a modified Raspberry Pi HQ camera or a Raspberry Pi NoIR camera module
