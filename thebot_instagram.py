from __future__ import absolute_import

import thebot
import threading
import time
import random

from instagram.client import InstagramAPI


class Plugin(thebot.Plugin):
    # each 15 minutes
    INTERVAL = 60 * 15

    def worker(self):
        api = InstagramAPI(client_id='1a748d8ab1ad48ab8e97b63c5d962355', client_secret='c9388c7acb064b779a7e5a3b4c5a7c12')
        countdown = 0

        while not self._event.is_set():
            if countdown == 0:
                photos = api.media_popular(count=20)
                photo = random.choice(photos)
                self._request.respond(photo.images['standard_resolution'].url)
                countdown = self.INTERVAL
            else:
                countdown -= 1

            time.sleep(1)

        self._request.respond('instagram was turned off')


    @thebot.route('instagram on')
    def on(self, request):
        thread = getattr(self, '_thread', None)
        if thread is not None and thread.is_alive():
            return

        self._event = threading.Event()
        self._request = request
        self._thread = threading.Thread(target=self.worker)
        self._thread.daemon = True
        self._thread.start()

        request.respond('instagram was turned on')

    @thebot.route('instagram off')
    def off(self, request):
        event = getattr(self, '_event', None)
        if event is not None:
            event.set()

