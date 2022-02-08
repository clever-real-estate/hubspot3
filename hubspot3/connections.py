"""
hubspot connections api
"""
from hubspot3.base import BaseClient
from hubspot3.utils import get_log


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
        create a hubspot connection
        :param payload: Dict A connection dict
        """

        return self._call(
            "objects/p3298701_connection",
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
        delete a hubspot connection
        :param connection_vid: Integer ID of connection in hubspot
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
        update a hubspot connection
        :param connection_vid: Integer ID of connection in hubspot
        :param payload: Dict A connection dict
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
        create a hubspot connection association
        :param connection_vid: Integer ID of connection in hubspot
        :param vid: Integer ID of associated object in hubspot
        :param object_type: String Type of object to be associated
        """

        return self._call(
            (
                f"objects/p3298701_connection/{connection_vid}/associations/"
                f"{object_type}/{vid}/connection_to_{object_type}"
            ),
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
        remove a hubspot connection association
        :param connection_vid: Integer ID of connection in hubspot
        :param vid: Integer ID of associated object in hubspot
        :param object_type: String Type of object to be associated
        """

        return self._call(
            (
                f"objects/p3298701_connection/{connection_vid}/associations/"
                f"{object_type}/{vid}/connection_to_{object_type}"
            ),
            method="DELETE",
            **options,
        )
