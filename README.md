# bgp-vis

This is a project exploring BGP visualization and discovery.

The environment files `client.env` and `rr.env` are used to create separate configurations
for route-reflectors and route-reflector-client routers.

A peer group is configured to avoid having to configure every peer relationship with `N` routers.

## Usage

```shell-session
docker compose up
```

Connect to the route-reflector, and validate peering:

```shell-session
docker exec -it vis-rr-1 /bin/bash

bash-5.1# gobgp neighbor
Peer         AS  Up/Down State       |#Received  Accepted
10.10.0.2 64600 00:00:00 Establ      |        0         0
```

After making configuration changes:

```shell-session
docker-compose up --build
```

## Scaling

The `replicas:` parameter for the client in `docker-compose.yaml` can be used to scale the network up and down.

## gobgp

See the [gobgp docs](https://github.com/osrg/gobgp/blob/master/docs/sources/getting-started.md) for more info.

[add route to rib](https://github.com/osrg/gobgp/blob/master/docs/sources/cli-command-syntax.md#--syntax)

Example, add a route on a client:

```shell-session
docker exec -it vis-client-1 /bin/bash
5d90b0e0f7ab:/gobgp# gobgp global rib add 10.23.0.0/24 -a ipv4
5d90b0e0f7ab:/gobgp# exit
```

Validate it appears in the rr:

```shell-session
docker exec -it vis-rr-1 /bin/bash    
48f54966e6e1:/gobgp# gobgp neighbor
Peer         AS  Up/Down State       |#Received  Accepted
10.10.0.2 64600 00:00:35 Establ      |        1         1
....

48f54966e6e1:/gobgp# gobgp global rib
   Network              Next Hop             AS_PATH              Age        Attrs
*> 10.20.0.0/24         10.10.0.2                                 00:02:43   [{Origin: ?} {LocalPref: 100}
```

You can check another client of the route-reflector to validate routes are actually reflecting:

```shell-session
docker exec -it vis-client-2 /bin/bash
gobgp global rib
   Network              Next Hop             AS_PATH              Age        Attrs
*> 10.20.0.0/24         10.10.0.4                                 00:00:21   [{Origin: ?} {LocalPref: 100} {Originator: 10.10.0.4} {ClusterList: [10.10.0.1]}]
```
