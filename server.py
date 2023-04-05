from concurrent import futures

import grpc
import summation_pb2
import summation_pb2_grpc

class Summation(summation_pb2_grpc.SummationServicer):
    def add(self, request, context):
        print("Got request : " + str(request))
        return summation_pb2.Output(sum=request.numberOne + request.numberTwo)
    

def server():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
   summation_pb2_grpc.add_SummationServicer_to_server(Summation(), server)
   server.add_insecure_port('[::]:50051')
   print("gRPC starting")
   server.start()
   server.wait_for_termination()


server()