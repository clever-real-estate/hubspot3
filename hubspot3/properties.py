"""
hubspot properties api
"""
import urllib.parse
from hubspot3.base import BaseClient
from hubspot3.utils import prettify, get_log
from typing import Union


PROPERTIES_API_VERSION = "1"


class PropertiesClient(BaseClient):
    """
    The hubspot3 Properties client uses the _make_request method to call the API
    for data.  It returns a python object translated from the json returned
    """

    class Recency:
        """recency type enum"""

        CREATED = "created"
        MODIFIED = "modified"

    def __init__(self, *args, **kwargs):
        super(PropertiesClient, self).__init__(*args, **kwargs)
        self.log = get_log("hubspot3.properties")

    def _get_path(self, subpath):
        return "properties/v{}/{}".format(
            self.options.get("version") or PROPERTIES_API_VERSION, subpath
        )

    def get_all_contact_properties(self, **options):
        return self._call("contacts/properties", method="GET", **options)

    def get_all_deal_properties(self, **options):
        return self._call("deals/properties", method="GET", **options)
