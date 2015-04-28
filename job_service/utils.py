__author__ = 'cgiridhar'

import uuid

class Utils:
    def __init__(self):
        pass

    def generate_api_key(self):
        return uuid.uuid4()

    def show_fields(self, bundle, *args):
        for f in bundle.data.keys():
            if not f in args:
                del bundle.data[f]

    def remove_fields(self, bundle, *args):
        for f in bundle.data.keys():
            if f in args:
                del bundle.data[f]

