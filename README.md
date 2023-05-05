# gobgp in docker

This is an example repo showing how to use gobgp and docker to stand up BGP configurations.

The environment files `client.env` and `rr.env` are used to create separate configurations
for route-reflectors and route-reflector-client routers.

## Usage

```shell-session
docker compose up
```

After making configuration changes:

```shell-session
docker-compose up --build
```

If you have issues with duplicate IP addresses, try running this and waiting a few seconds.

```shell-session
docker-compose down --remove-orphans
```

## Interaction

You can connect to the containers using their name:

```shell-session
docker exec -it vis-rr-1 /bin/bash
```

From inside the container, `gobgp` is the binary used to interact with the router.

See the [gobgp docs](https://github.com/osrg/gobgp/blob/master/docs/sources/getting-started.md) for more info.
