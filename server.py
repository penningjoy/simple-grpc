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
   '''
   This method prepares and starts the gRPC server.
   1. Creates the server object with 5 max thread workers
   2. A Summation service instance is assigned to the server. The server then
      knows which service to run when requests come in for summation
   3. Specifies a port
   4. Starts the server
   5. The start() method is non-blocking. A new thread will be created
      to handle requests. The wait_for_termination will keep the thread calling
      the start() method be blocked until the server is terminated
   '''
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))      #1
   summation_pb2_grpc.add_SummationServicer_to_server(Summation(), server) #2
   server.add_insecure_port('[::]:50051')  #3
   print("gRPC server starting")
   server.start()  #4
   server.wait_for_termination()  #5


if __name__ == "__main__":
    server()