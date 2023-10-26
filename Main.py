
from Customer import Customer
from LinkedQueue import LinkedQueue
from TheatreSimulator import TheaterSimulator

def main():

    one_cashier = TheaterSimulator(750,0.55,1)
    two_cashier = TheaterSimulator(750, 0.55, 2)
    three_cashier = TheaterSimulator(750, 0.55, 3)

    print("Sim #1 w/ one cashier: ")
    one_cashier.run_simulation()
    print("\nSim #2 w/ two cashiers")
    two_cashier.run_simulation()
    print("\nSim #3 w/ three cashiers")
    three_cashier.run_simulation()




main()



