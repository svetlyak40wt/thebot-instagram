from __future__ import absolute_import

import thebot
import random

from instagram.client import InstagramAPI


class Plugin(thebot.ThreadedPlugin):
    # each 15 minutes
    DEFAULT_INTERVAL = 60 * 15

    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        self.interval = self.storage.get('interval', self.DEFAULT_INTERVAL)
        self.restarting = False

        if self.storage.get('on'):
            self._request = self.storage['request']
            self.start_worker(interval=self.interval)

    def do_job(self):
        api = InstagramAPI(client_id='1a748d8ab1ad48ab8e97b63c5d962355', client_secret='c9388c7acb064b779a7e5a3b4c5a7c12')
        photos = api.media_popular(count=20)
        photo = random.choice(photos)
        self._request.respond(photo.images['standard_resolution'].url)

    def on_start(self):
        self.storage['on'] = True
        self.storage['request'] = self._request

        if self.restarting:
            self._request.respond('instagram was restarted')
            self.restarting = False
        else:
            self._request.respond('instagram was turned on')

    def on_stop(self):
        self.storage['on'] = False
        del self.storage['request']

        if not self.restarting:
            self._request.respond('instagram was turned off')

    @thebot.route('instagram on')
    def on(self, request):
        """Turn image fetching on."""
        self._request = request
        self.start_worker(interval=self.interval)

    @thebot.route('instagram off')
    def off(self, request):
        """Turn image fetching off."""
        self.stop_worker()

    @thebot.route('instagram set interval (?P<interval>[0-9.]+)')
    def set_interval(self, request, interval):
        """Sets interval between pictures (in minutes)."""
        self.interval = float(interval) * 60
        self.storage['interval'] = self.interval

        if self.is_working():
            self.restarting = True
            self.stop_worker()
            self.start_worker(interval=self.interval)

    @thebot.route('instagram status')
    def status(self, request):
        """Shows instagram settings."""
        request.respond('images fetching is {}, iterval {} min'.format(
            'on' if self.storage.get('on') else 'off',
            self.interval / 60.0
        ))

