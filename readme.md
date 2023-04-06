## A simple gRPC example

The project is a simple example to demonstrate how gRPC works using python ( both server
and client). In gRPC, an application, say client, can directly call a method in another
application, say server, running remotely in a different machine. The operation is almost
as fact as a local method/function call.

To install gRPC tools, run
```bash
python -m pip install grpcio-tools
```

Run the command to generate the gRPC code:

```bash
python -m grpc_tools.protoc -I ./protos/ --python_out=./ --grpc_python_out=. ./protos/summation.proto

```

### Execution Instruction
1. Run the Server

```bash
python server.py
```

2. Run the client 

```bash
python client.py
```