import gc
import uos
import machine
import json
import time
import camera
from microWebSrv import MicroWebSrv

carOption = ""

class webcam():

    def __init__(self):
        self.quality = 10
        self.vflip = 0
        self.hflip = 0
        self.framesize = camera.FRAME_CIF
        self.routeHandlers = [
            ("/", "GET", self._httpHandlerIndex),
            ("/stream/<d>", "GET", self._httpStream),
            ("/upy/<quality>/<vflip>/<hflip>/<framesize>", "GET", self._httpHandlerSetData),
            ("/upy", "GET", self._httpHandlerGetData),
            ("/car/<option>", "GET", self._httpCar)         #############CAR GET REQUESST HANDLER#############
        ]

    def run(self, app_config):
        self.led = machine.Pin(app_config['led'], machine.Pin.OUT)

        # Camera resilience - if we fail to init try to deinit and init again
        if app_config['camera'] == 'ESP32-CAM':
            camera.init(0, format=camera.JPEG, framesize=self.framesize)      #ESP32-CAM

        mws = MicroWebSrv(routeHandlers=self.routeHandlers, webPath="www/")
        mws.Start(threaded=True)
        gc.collect()

######################################CAR GET REQUESST HANDLER############################################
##########################################################################################################

    def _httpCar(self, httpClient, httpResponse, routeArgs):
        global carOption
        carOption = routeArgs['option']
        #print(carOption)

        headers = { 'Last-Modified' : 'Fri, 1 Jan 2018 23:42:00 GMT', \
                    'Cache-Control' : 'no-cache, no-store, must-revalidate' }
        httpResponse.WriteResponse(code=200, headers=headers,
                                    contentType="text/html",
                                    contentCharset="UTF-8",
                                    content=None)

##########################################################################################################
##########################################################################################################


    def _httpStream(self, httpClient, httpResponse, routeArgs):
        image = camera.capture()

        headers = { 'Last-Modified' : 'Fri, 1 Jan 2018 23:42:00 GMT', \
                    'Cache-Control' : 'no-cache, no-store, must-revalidate' }

        httpResponse.WriteResponse(code=200, headers=headers,
                                    contentType="image/jpeg",
                                    contentCharset="UTF-8",
                                    content=image)

    def _httpHandlerIndex(self, httpClient, httpResponse):
        f = open("www/index.html", "r")
        content =  f.read()
        f.close()

        headers = { 'Last-Modified' : 'Fri, 1 Jan 2018 23:42:00 GMT', \
                            'Cache-Control' : 'no-cache, no-store, must-revalidate' }

        httpResponse.WriteResponseOk(headers=None,
                                    contentType="text/html",
                                    contentCharset="UTF-8",
                                    content=content)

    def _httpHandlerSetData(self, httpClient, httpResponse, routeArgs):
        self.quality = int(routeArgs['quality'])
        self.vflip = bool(routeArgs['vflip'])
        self.hflip = bool(routeArgs['hflip'])
        self.framesize = int(routeArgs['framesize'])

        camera.quality(self.quality)
        camera.flip(self.vflip)
        camera.mirror(self.hflip)
        camera.framesize(self.framesize)

        data = {
            'quality': self.quality,
            'vflip': self.vflip,
            'hflip': self.hflip,
            'framesize': self.framesize
        }
        self._newdata = True
        httpResponse.WriteResponseOk(headers=None,
                                        contentType="text/html",
                                        contentCharset="UTF-8",
                                        content=json.dumps(data))

    def _httpHandlerGetData(self, httpClient, httpResponse):
        data = {
            'quality': self.quality,
            'vflip': self.vflip,
            'hflip': self.hflip,
            'framesize': self.framesize
        }

        httpResponse.WriteResponseOk(headers=None,
                                    contentType="application/json",
                                    contentCharset="UTF-8",
                                    content=json.dumps(data))