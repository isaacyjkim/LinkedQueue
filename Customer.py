import random
class Customer():
    """Represents a single customer waiting in line to buy a ticket"""

    def __init__(self,arrival_time,transaction_time):
        # Arrival time tracks which clock tick this customer showed up at
        self._arrival_time = arrival_time

        # Transaction time is how many clock ticks it takes to server the customer
        self._transaction_time = transaction_time

    @classmethod
    def generate_customer(cls, probability_of_arrival, current_time):
        """Return a new customer object if the probability of arrival is greater than
        or equal to a random number between 0 and 1. Otherwise, return None to signify a customer
        did not arrive. """
        if random.random() < probability_of_arrival:
            return Customer(current_time,random.randint(1,3))
        else:
            return None

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def transaction_time(self):
        return self._transaction_time

    def serve(self):
        """Customer has been served by cashier for 1 clock tick """
        self._transaction_time -=1

