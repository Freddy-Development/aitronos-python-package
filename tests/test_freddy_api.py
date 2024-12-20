import unittest
from Aitronos import FreddyApi, MessageRequestPayload, StreamEvent, Message, Aitronos
import logging
from config import Config
from tqdm import tqdm  # For progress visualization
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class FreddyApiTests(unittest.TestCase):
    """Test suite for the FreddyApi and related functionalities."""

    def setUp(self):
        """Set up the test environment."""
        # Load a real API token from your config
        token = Config.load_token()
        self.api = Aitronos(api_key=token).AssistantMessaging

    def test_send_message_success(self):
        """Test sending a valid message with the API."""
        # Create the payload with real data
        payload = MessageRequestPayload(
            organization_id=1,  # Real organization ID
            assistant_id=1,  # Real assistant ID
            messages=[Message(content="Hello", role="user")]
        )

        # Perform a real API call
        try:
            response = self.api.create_run(payload)  # Assuming this function sends the message
            self.assertIsNotNone(response, "The response should not be None")
            print("API Response:", response)
        except Exception as e:
            self.fail(f"API call failed: {e}")

    def test_send_message_failure(self):
        """Test sending a message with invalid data to simulate failure."""
        # Create an invalid payload (e.g., invalid assistant ID)
        payload = MessageRequestPayload(
            organization_id=1,  # Real organization ID
            assistant_id=9999,  # Invalid or non-existent assistant ID
            messages=[Message(content="Hello", role="user")]
        )

        # Perform a real API call and expect failure
        try:
            self.api.create_run(payload)
            self.fail("Expected an exception, but the API call succeeded unexpectedly.")
        except Exception as e:
            # Assert the exception message contains specific text indicating failure
            self.assertIn("Network or connection error", str(e))
            print("Caught expected exception:", e)

    def test_check_run_status_completed(self):
        """Test checking the status of a run until it completes."""
        organization_id = 1  # Real organization ID
        run_key = "run_zYJ14m8sGAqt7JBZ3NzVUaiu"  # Replace with a valid run_key
        thread_key = "thread_3T6BSDLITANwaGIkWaychThJ"  # Replace with a valid thread_key

        # Poll for the status of the run
        try:
            for _ in tqdm(range(100), desc="Checking run status", unit="attempt"):
                status = self.api.check_run_status(
                    organization_id=organization_id,
                    run_key=run_key,
                    thread_key=thread_key
                )

                if status == "completed":
                    self.assertEqual(status, "completed", "Run status should be completed")
                    print("Run Status:", status)
                    break
                time.sleep(2)  # Simulate waiting period between status checks
            else:
                self.fail("Run did not complete after multiple attempts.")

        except Exception as e:
            self.fail(f"API call failed: {e}")

    def test_get_run_response(self):
        """Test getting the response of a completed run."""
        organization_id = 2  # Real organization ID
        thread_key = "thread_WQWyoPExdIpJF8P9NqldtBZL"  # Replace with a valid thread_key

        # Perform a real API call to get the final run response
        try:
            response = self.api.get_run_response(organization_id=organization_id, thread_key=thread_key)
            self.assertIsNotNone(response, "The response should not be None")
            self.assertIn("response", response, "The response should contain the 'response' key")
            print("Run Response:", response["response"])
        except Exception as e:
            self.fail(f"API call failed: {e}")

        def test_execute_run_live(self):
            """Test executing a full live run."""
            messages = [
                Message(content="Tell me a joke.", role="user"),
            ]
            payload = MessageRequestPayload(
                organization_id=1,  # Real organization ID
                assistant_id=1,  # Real assistant ID
                instructions="Provide a joke",
                additional_instructions="Use humor",
                messages=messages
            )

            # Perform the full live run, checking the status and getting the response
            try:
                response = self.api.execute_run(payload)

                # Ensure that the response is not None
                self.assertIsNotNone(response, "The response should not be None")

                # Assert that the response is a list and has at least one element
                self.assertIsInstance(response, list, "The response should be a list")
                self.assertGreater(len(response), 0, "The response list should not be empty")

                # Extract the first dictionary from the list
                first_event = response[0]

                # Ensure that 'response' is a key in the first event
                self.assertIn("response", first_event, "The response should contain the 'response' key")

                # Print the actual response content
                print("Run Response:", first_event["response"])

            except Exception as e:
                self.fail(f"An error occurred during the test: {e}")


if __name__ == "__main__":
    unittest.main()