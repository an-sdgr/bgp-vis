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

If you have issues with duplicate IP addresses, try running this and waiting a few seconds.

```shell-session
docker-compose down --remove-orphans
```

## gobgp

See the [gobgp docs](https://github.com/osrg/gobgp/blob/master/docs/sources/getting-started.md) for more info.

[add route to rib](https://github.com/osrg/gobgp/blob/master/docs/sources/cli-command-syntax.md#--syntax)

Example, add a route on a client:

```shell-session
docker exec -it vis-client-1 /bin/bash
5d90b0e0f7ab:/gobgp# gobgp global rib add 10.33.0.0/16 -a ipv4
5d90b0e0f7ab:/gobgp# exit
```

Validate it appears in the rr:

```shell-session
docker exec -it vis-rr-1 /bin/bash    
48f54966e6e1:/gobgp# gobgp neighbor
Peer         AS  Up/Down State       |#Received  Accepted
10.10.0.2 64600 00:00:35 Establ      |        1         1
48f54966e6e1:/gobgp# gobgp global rib
   Network              Next Hop             AS_PATH              Age        Attrs
*> 10.33.0.0/16         10.10.0.2                                 00:02:43   [{Origin: ?} {LocalPref: 100}
```
