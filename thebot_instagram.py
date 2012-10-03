from __future__ import absolute_import

import thebot
import random

from instagram.client import InstagramAPI


class Plugin(thebot.ThreadedPlugin):
    # each 15 minutes
    INTERVAL = 60 * 15
    INTERVAL = 10

    def do_job(self):
        api = InstagramAPI(client_id='1a748d8ab1ad48ab8e97b63c5d962355', client_secret='c9388c7acb064b779a7e5a3b4c5a7c12')
        photos = api.media_popular(count=20)
        photo = random.choice(photos)
        self._request.respond(photo.images['standard_resolution'].url)

    def on_stop(self):
        self._request.respond('instagram was turned off')

    def on_start(self):
        self._request.respond('instagram was turned on')

    @thebot.route('instagram on')
    def on(self, request):
        self._request = request
        self.start_worker(interval=self.INTERVAL)

    @thebot.route('instagram off')
    def off(self, request):
        self.stop_worker()

