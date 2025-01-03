from queue import Queue


class Order:
    def __init__(self, order_id):
        self.order_id = order_id

    def __str__(self):
        return str(self.order_id)


queue = Queue()
order_id: int = 0


def generate_request():
    global order_id
    order = Order(order_id)
    order_id += 1
    queue.put(order)


def process_request():
    if queue.empty():
        print("Queue is empty")
    else:
        order = queue.get()
        print(" processed ok: " + str(order))


user_exit = False
while not user_exit:
    if input("Press 0 to exit, Enter key to continue ") == '0':
        user_exit = True
    else:
        generate_request()
        process_request()
