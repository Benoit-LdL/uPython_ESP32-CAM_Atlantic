#start = utime.time()   necessary? 
#ntptime.settime()      necessary? maybe sync with gps clock?


# These parameters: format=camera.JPEG, xclk_freq=camera.XCLK_10MHz are standard for both cameras.
# You can try using a faster xclk (20MHz), this also worked with the esp32-cam and m5camera 
# but the image was pixelated and somehow green.

#wri = Writer(oled, arial35, verbose=False)
    #Writer.set_textpos(20,64)# In case a previous test has altered this
    #wri.printstring(numSat)
    
    '''
    !!! GPS To-Do
    -> try in thread to read all incoming nmea sentences and not 1 per oled loop cycle
    -> Necessary data in 2 sentences:
        * GGA: Time, Lon, Lat, # sats, altitude
        * RMC: Time,(Lon,Lat), Speed, course(degrees/boussole)
    -> If ok, parse GGA,RMC automatically instead of using BIG GPS library
    '''

#oled.text(gps.latitude_string() + "/" + gps.longitude_string() ,0,44)


#image = camera.capture()
    #f = open('sd/image-'+str(mainCounter)+'.jpg','a')
    #f.write(image)
    #utime.sleep(0.1)
    #f.close()
    #mainCounter += 1