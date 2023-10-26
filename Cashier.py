from LinkedQueue import LinkedQueue

class Cashier():

    def __init__(self):
        self._total_customer_wait_time = 0
        self._customers_served = 0
        self._longest_wait = 0
        self._current_customer = None
        self._queue = LinkedQueue()

    def add_customer(self,c):
        self._queue.add(c)

    def serve_customer(self,current_time):
        """Spend 1 unit of time serving a current customer(if there is one)"""
        if self._current_customer is None:
            if self._queue.is_empty():
                # No customer to serve, so we can return
                return
            else:
                # Nobody is being served and there is a customer waiting in the queue. Start serving them
                self._current_customer = self._queue.pop()
                time_waited = current_time - self._current_customer.arrival_time
                if time_waited > self._longest_wait:
                    self._longest_wait = time_waited
                self._total_customer_wait_time += time_waited

        # Serve the current customer
        self._current_customer.serve()
        if self._current_customer.transaction_time == 0:
            # Current customer is finished
            self._current_customer = None
            self._customers_served +=1
    def print_statistics(self):
        print(f"Customer served: {self._customers_served}")
        print(f"Longest wait time: {self._longest_wait}")
        try:
            print(f"Average wait time: {self._total_customer_wait_time/self._customers_served:.2f}")
        except ZeroDivisionError:
            print("Average wait time: 0 (no customers served) ")
        print(f"Remaining customers in line: {len(self._queue)}")