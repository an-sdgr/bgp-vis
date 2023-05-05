from proto import gobgp_pb2 as gobgp
from wrap import GoBGPQueryWrapper

gobgp_target = {"target_ipv4_address": "localhost", "target_rpc_port": 50051}

rpc = GoBGPQueryWrapper(**gobgp_target)

res = rpc.debug_peers()

print(res)

# graph = graphing.build_nx_from_lsdb(lsdb)

# graphing.draw_pyplot_graph(graph)
