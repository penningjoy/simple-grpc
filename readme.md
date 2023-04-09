## A simple gRPC example

The project is a simple example to demonstrate how gRPC works using python ( both server
and client ). In gRPC, an application, client, can directly call a method in another
application, server, running remotely in a different machine. The operation is almost
as fast as a local method/function call.

For further reading, refer to [https://grpc.io/docs/what-is-grpc/](https://grpc.io/docs/what-is-grpc/)

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
