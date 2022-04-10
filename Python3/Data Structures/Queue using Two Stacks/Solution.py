# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:

    def __init__(self):
        self._q = []
        self._list_of_queries = []

    def enqueue(self, value):  # Enqueue element x into the end of the queue.
        self._q.append(value)
    
    def dequeue(self):   # Dequeue the element at the front of the queue.
        self._q.pop(0)
    
    def print_front(self):   # Print the element at the front of the queue.
        print(self._q[0])
    
    def get_queries(self):
        queries = int(input())
        for _ in range(queries):
            self._list_of_queries.append(input())
            
    def run_queries(self):
        for query in self._list_of_queries:
            if query[0] == '1':
                self.enqueue(query.split()[1])
            elif query[0] == '2':
                self.dequeue()
            elif query[0] == '3':
                self.print_front()
        
if __name__ == '__main__':
    q = Queue()
    q.get_queries()
    q.run_queries()
