# Gobgp container

## Protobuf

To generate new protocol buffers:

```shell-script
pip3 install -r requirements.txt
git clone git@github.com:osrg/gobgp.git
cd gobgp/api
python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. *.proto
cd ../..
cp -R gobgp/api/ ./proto/
```

