"""
hubspot contacts api
"""
import urllib.parse
import warnings
from typing import Dict, List, Union

from hubspot3.base import BaseClient
from hubspot3.crm_associations import CRMAssociationsClient
from hubspot3.utils import get_log, prettify

CONTACTS_API_VERSION = "1"

class ConnectionsClient(BaseClient):
    """
    Lets you extend to non-existing clients, this example extends pipelines
    """

    def __init__(self, *args, **kwargs):
        """initialize a connections client"""
        super(ConnectionsClient, self).__init__(*args, **kwargs)
        self.log = get_log("hubspot3.connections")
   
    def create(
        self,
        payload: dict,
        **options,
    ):
        """
        create a hubspot association
        :param from_object: ID of object to relate
        :param to_object: ID of object to relate to
        :param definition: Definition ID for the objects you're looking for associations of
        """

        return self._call(
            f"objects/p3298701_connection",
            method="POST",
            data=payload,
            **options,
        )

    def delete(
        self,
        connection_vid: int,
        **options,
    ):
        """
        create a hubspot association
        :param from_object: ID of object to relate
        :param to_object: ID of object to relate to
        :param definition: Definition ID for the objects you're looking for associations of
        """

        return self._call(
            f"objects/p3298701_connection/{connection_vid}",
            method="DELETE",
            **options,
        )

    def update(
        self,
        connection_vid: int,
        payload: dict,
        **options,
    ):
        """
        create a hubspot association
        :param from_object: ID of object to relate
        :param to_object: ID of object to relate to
        :param definition: Definition ID for the objects you're looking for associations of
        """

        return self._call(
            f"objects/p3298701_connection/{connection_vid}",
            method="PATCH",
            data=payload,
            **options,
        )

    def add_association(
        self,
        connection_vid: int,
        vid: int,
        object_type: str,
        **options,
    ):
        """
        create a hubspot association
        :param from_object: ID of object to relate
        :param to_object: ID of object to relate to
        :param definition: Definition ID for the objects you're looking for associations of
        """

        return self._call(
            f"objects/p3298701_connection/{connection_vid}/associations/{object_type}/{vid}/connection_to_{object_type}",
            method="PUT",
            **options,
        )

    def remove_association(
        self,
        connection_vid: int,
        vid: int,
        object_type: str,
        **options,
    ):
        """
        create a hubspot association
        :param from_object: ID of object to relate
        :param to_object: ID of object to relate to
        :param definition: Definition ID for the objects you're looking for associations of
        """

        return self._call(
            f"objects/p3298701_connection/{connection_vid}/associations/{object_type}/{vid}/connection_to_{object_type}",
            method="DELETE",
            **options,
        )
