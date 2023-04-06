import grpc

import summation_pb2
import summation_pb2_grpc

def run():
    '''
    - Stub: It's the client object that helps in executing remote calls the server.
    - The Input and Output of the remote procedure call are defined in the protocol 
      buffer file, summation.proto, in the protos folder.

    Client Execution Flow - Steps:
    1. Takes two numbers from user
    2. Create a stub/client object using the communication channel
    3. Calls the target procedure, sum, using the stub object and passes the two numbers
       and receives response
    4. Prints the sum returned with the response
    '''
    
    #1  Take two inputs from user
    numOne = int(input("Enter the first number: "))
    numTwo = int(input("Enter the second number: "))

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = summation_pb2_grpc.SummationStub(channel)        #2
        response = stub.add(summation_pb2.Input(numberOne=numOne, numberTwo=numTwo))  #3
    
    print(f"Sum of {numOne} and {numTwo} is {str(response.sum)}") #4


if __name__ == "__main__":
    run()