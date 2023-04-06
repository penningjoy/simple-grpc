from concurrent import futures

import grpc
import summation_pb2
import summation_pb2_grpc

class Summation(summation_pb2_grpc.SummationServicer):
    '''
    Summation Class implements the SummationServicer interface. It provides the
    implementation of the method "add" which will actually do the job of summation.
    '''
    def add(self, request, context):
        '''
        This method takes two numbers from the request body, adds them and sends 
        back the sum as response.
        
        args: request : request body that is modeled after the Input model in the
                        protocol buffer - summation.proto
              context : context object that provides RPC specific information such
                        as timeout limits.
        returns: Output type response. Output is defined in the protocol buffer
                 - summation.proto
        '''
        print("Got request : " + str(request))
        return summation_pb2.Output(sum=request.numberOne + request.numberTwo)
    

def server():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
   summation_pb2_grpc.add_SummationServicer_to_server(Summation(), server)
   server.add_insecure_port('[::]:50051')
   print("gRPC starting")
   server.start()
   server.wait_for_termination()  # will keep the current thread blocked until the server is terminated


if __name__ == "__main__":
    server()