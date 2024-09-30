import unittest
import queue

# Import functions from the main code file
from imitation_app_processing_system import generate_request, process_request


class TestQueueSystem(unittest.TestCase):

    def setUp(self):
        """Initialization of the queue before each test."""
        self.test_queue = queue.Queue()

    def test_generate_request(self):
        """Test adding requests to the queue."""
        print("Testing request addition to the queue")
        request_id = 1
        generate_request(self.test_queue, request_id)
        # Check if queue size is 1
        self.assertEqual(self.test_queue.qsize(), 1)
        # Queue should not be empty
        self.assertFalse(self.test_queue.empty())
        # Check if request ID is as expected
        self.assertEqual(self.test_queue.get(), request_id)
        print("test_generate_request - passed")

    def test_process_request(self):
        """Test processing requests from the queue."""
        print("Testing request processing from the queue")
        request_id = 1
        generate_request(self.test_queue, request_id)

        processed_id = process_request(self.test_queue)
        # Processed ID should match the added request ID
        self.assertEqual(processed_id, request_id)
        # Queue should be empty after processing
        self.assertTrue(self.test_queue.empty())
        print("test_process_request - passed")

    def test_process_empty_queue(self):
        """Test processing an empty queue."""
        print("Testing processing an empty queue")
        result = process_request(self.test_queue)
        # Should return None for empty queue
        self.assertIsNone(result)
        print("test_process_empty_queue - passed")

    def test_multiple_requests(self):
        """Test handling multiple requests in the queue."""
        print("Testing handling multiple requests")
        ids = [1, 2, 3, 4]  # Request IDs to be added
        for request_id in ids:
            generate_request(self.test_queue, request_id)

        # Queue size should match the number of requests
        self.assertEqual(self.test_queue.qsize(), len(ids))

        for expected_id in ids:
            processed_id = process_request(self.test_queue)
            # Each processed ID should match the corresponding request
            self.assertEqual(processed_id, expected_id)
        print("test_multiple_requests - passed")

    def tearDown(self):
        """Clear the queue after each test."""
        # Check if there are any remaining items in the queue
        if not self.test_queue.empty():
            print(f"Residual requests in the queue: {
                  self.test_queue.qsize()}. Clearing...")
            while not self.test_queue.empty():
                removed_request = self.test_queue.get()
                print(f"Removed request: {removed_request}")

        print("Queue cleared and ready for the next test.")


# Run tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
