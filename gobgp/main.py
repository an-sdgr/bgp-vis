# RPC tools
#from proto import GoBGPQueryWrapper
from proto import gobgp_pb2 as gobgp
# Graphing tools
import graphing
from wrap import GoBGPQueryWrapper

gobgp_target = {"target_ipv4_address": "localhost", "target_rpc_port": 50051}

rpc = GoBGPQueryWrapper(**gobgp_target)


#test = gobgp.ListPathRequest(
#            table_type=gobgp.LOCAL,
#            name="",
#            family=gobgp.Family(afi=gobgp.Family.AFI_LS, safi=gobgp.Family.SAFI_LS),
#            prefixes=None,
#            sort_type=True,
#        )

#request = gobgp.GetTableRequest()
#response = gobgp.GetTable(request)

test2 = rpc.debug_peers()

print(test2)

#lsdb = rpc.get_lsdb()
#graph = graphing.build_nx_from_lsdb(lsdb)

#graphing.draw_pyplot_graph(graph)