import unittest
from unittest.mock import patch
import requests
from FreddyApi import FreddyApi, Message, MessageRequestPayload

class TestFreddyApi(unittest.TestCase):

    def setUp(self):
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImFkbWluIiwibmJmIjoxNzEwODQ1Mzk2LCJleHAiOjE3MTE0NTAxOTYsImlhdCI6MTcxMDg0NTM5Nn0.msv82ta2LsSxXtELPlE6YPHeaOOYVgV4tXKSq6rW7nw"
        self.api = FreddyApi(self.token, version="v2.3")
        self.assistant_id = "asst_nsvUVKcFhDmHEiD0y6uvDu3o"
        self.messages = [
            Message(content="Hello!", role="user", type="text"),
            Message(content="Translate this to German", role="user", type="text")
        ]
        self.payload = MessageRequestPayload(
            assistantId=self.assistant_id,
            messages=self.messages,
            instructions="Translate this to German",
            stream=False
        )

    @patch('requests.post')  # Correct patching
    def test_send_message_success(self, mock_post):
        # Mocking the response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": "success"}

        response = self.api.send_message(self.payload)
        self.assertEqual(response, {"response": "success"})

    @patch('requests.post')  # Correct patching
    def test_send_message_rate_limit(self, mock_post):
        # Mocking the response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": "success"}

        # First call should work
        self.api.send_message(self.payload)

        # Rate limit should prevent second call
        with self.assertRaises(Exception) as context:
            self.api.send_message(self.payload)

        self.assertTrue("Rate limit reached" in str(context.exception))

    @patch('requests.post')  # Correct patching
    def test_send_message_error(self, mock_post):
        # Mocking an error response
        mock_response = mock_post.return_value
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad Request"}
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        with self.assertRaises(Exception) as context:
            self.api.send_message(self.payload)

        self.assertTrue("API request failed" in str(context.exception))


if __name__ == '__main__':
    unittest.main()