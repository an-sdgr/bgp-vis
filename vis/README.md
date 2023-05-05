# Visualization

Very WIP. Currently debug-only:

```shell-session
python3 main.py
```

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

Some imports in ./proto need to be fixed, i'm probably doing something wrong.

```python
# these
import gobgp_pb2 as gobgp__pb2

# change to these
from . import gobgp_pb2 as gobgp__pb2
```
