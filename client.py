import grpc

import summation_pb2
import summation_pb2_grpc

def run():
    numOne = int(input("Enter the first number: "))
    numTwo = int(input("Enter the second number: "))

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = summation_pb2_grpc.SummationStub(channel)
        response = stub.add(summation_pb2.Input(numberOne=numOne, numberTwo=numTwo))
    
    print(f"Sum of {numOne} and {numTwo} is {str(response.sum)}")


run()