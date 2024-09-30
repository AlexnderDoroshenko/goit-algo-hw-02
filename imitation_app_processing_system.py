import queue
import random
import time

# Queue initialization
REQUEST_QUEUE = queue.Queue()


def generate_request(queue, request_id):
    """
    Generates a new request and adds it to the queue.

    Args:
        queue (queue.Queue): The queue where requests are stored.
        request_id (int): The unique identifier for the request.

    Returns:
        None
    """
    print(f"New request created with ID: {request_id}")
    queue.put(request_id)


def process_request(queue):
    """
    Processes a request from the queue if it's not empty.

    Args:
        queue (queue.Queue): The queue storing the requests.

    Returns:
        int or None: The ID of the processed request if the queue is not empty,
                     or None if the queue is empty.
    """
    if not queue.empty():
        request_id = queue.get()
        print(f"Processing request with ID: {request_id}")
        return request_id
    else:
        print("The queue is empty, no more requests to process.")
        return None


def main():
    """
    Main function to simulate the generation and processing of requests.

    Continuously creates and processes requests in a loop, with a sleep time
    to simulate the delay between operations. It handles keyboard interruption 
    to safely stop the execution.

    Returns:
        None
    """
    request_id = 1  # Initial request ID
    try:
        while True:
            # Simulate the creation of new requests
            if random.random() > 0.3:  # Randomly decide whether to create a new request
                generate_request(REQUEST_QUEUE, request_id)
                request_id += 1

            # Simulate request processing
            process_request(REQUEST_QUEUE)
            time.sleep(1)  # Delay to simulate service center operation

    except KeyboardInterrupt:
        print("\nSystem shutting down.")


if __name__ == '__main__':
    main()
