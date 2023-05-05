"""t"""
# Standard Imports
import yaml
from google.protobuf.json_format import MessageToDict

# RPC & GoBGP imports
import grpc
from proto import gobgp_pb2 as gobgp
from proto import gobgp_pb2_grpc
from proto import attribute_pb2
from proto import capability_pb2


class wrapper:
    """Class to add abstraction for RPC calls to a GoBGP Instance"""

    def __init__(
        self,
        target_ipv4_address: str = "",
        target_rpc_port: str = "",
        connect: bool = True,
    ):
        """Constructor initialises RPC session

        Args:
            target_ipv4_address: Management IPv4 Address of GoBGP instance
            target_rpc_port: Management Port of GoBGP Instance
            connect: When set false, will not build grpc channel or api stub objects
        """
        if connect:
            channel = grpc.insecure_channel(f"{target_ipv4_address}:{target_rpc_port}")
            self.stub = gobgp_pb2_grpc.GobgpApiStub(channel)

    def __get_bgp_peers(self) -> list:
        """RPC query for BGP Peers

        Sends gobgp.ListPeerRequest object over RPC session to get peer objects

        Returns:
            List of BGP Peer objects

        """
        request = gobgp.ListPeerRequest()
        response = self.stub.ListPeer(request)
        peers = [MessageToDict(peer) for peer in response]
        return peers

    def debug_peers(self) -> list:
        """Return peer list without further processing"""
        return self.__get_bgp_peers()
