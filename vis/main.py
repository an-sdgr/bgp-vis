from proto import gobgp_pb2 as gobgp
from wrap import wrapper

gobgp_target = {"target_ipv4_address": "localhost", "target_rpc_port": 50051}

rpc = wrapper(**gobgp_target)

res = rpc.debug_peers()

print(res)

# graph = graphing.build_nx_from_peers(peers)

# graphing.draw_pyplot_graph(graph)
