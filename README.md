# Remote control Bugatti Atlantic Project

## Goal

* 3D print Bugatti Type 57 SC Atlantic Body
* Use an ESP32-CAM board as the controller
* Use a PCA9685 16-channel servo controller to control servos and leds
* Create a webserver on which we see the live videofeed and on which we can control the car

## < 2021

I started this project a good year ago. I managed to create a decent 3D model of the car's body (this was another project I stared a few years ago) with separate doors, bonnet, boot, etc.
However I had problems programming the webserver in arduino (C++) so eventually gave up.

## > 2021

Just learned that you can run microPython on ESP boards, so I gave it a try and it works quite well!
I used this [project](https://github.com/lemariva/uPyCam) from [Lemariva](https://github.com/lemariva) as a reference and built something custom.

## Functionality of project

* Choice between AP and standard wifi mode
* Webserver showing live video-feed
* Custom options for video feed on webpage
* Interactable buttons on webpage for car control
* PCA9685 intgration: can control servos and leds
* ...

## To-Do List

* Install all servos in car
* Configure each servo correclty in software
* ...?
