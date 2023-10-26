from Cashier import Cashier
from Customer import Customer

class TheaterSimulator:

    def __init__(self, length, odds_of_new_customer,num_cashiers):
        self._odds_of_new_customer = odds_of_new_customer
        self._simulation_length = length
        self._cashiers = []
        for cashiers in range(num_cashiers):
            self._cashiers.append(Cashier())


    def shortest_queue(self):
        """Iterates through list of cashiers in order to find the shortest queue.
        Return the index of the queue with the shortest length.  """
        index_shortest = 0
        for c in range(len(self._cashiers)):
            if self._cashiers[c]._queue._size < self._cashiers[index_shortest]._queue._size:
                index_shortest = c
        return index_shortest

    def run_simulation(self):
        """Run the simulation for self._simulation_length clock ticks"""
        for cur_time in range(self._simulation_length):
            # Attempt to generate a new customer each clock tick
            new_customer = Customer.generate_customer(self._odds_of_new_customer,cur_time)

            # Add new customer to the Cashier w/ the least amount of customers in line.
            if new_customer is not None:
                self._cashiers[self.shortest_queue()].add_customer(new_customer)

            # Iterate through all cashiers in the list and serve each customer.
            for i in range(len(self._cashiers)):
                self._cashiers[i].serve_customer(cur_time)

        # Print the results for each cashier
        for i in range(len(self._cashiers)):
            print(f"\nCashier #{i+1}\n")
            self._cashiers[i].print_statistics()


