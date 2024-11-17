import unittest
import asyncio
from Aitronos import FreddyError
from Aitronos.AppHive import Authentication, LoginResponse
from config import Config

class TestAuthentication(unittest.TestCase):
    """Test suite for the Authentication functionality."""

    def setUp(self):
        """Set up test environment with configuration values."""
        self.valid_email = Config.test_email()
        self.valid_password = Config.test_password()
        self.invalid_email = "invalid_user@example.com"
        self.invalid_password = "wrong_password"

    def test_login_success(self):
        """Test synchronous login with valid credentials."""
        response = Authentication.login(username_email=self.valid_email, password=self.valid_password)
        self.assertIsInstance(response, LoginResponse, "Expected LoginResponse object.")
        self.assertIsNotNone(response.token, "Token should not be None.")
        print("Login Successful! Token:", response.token)

    def test_login_failure_invalid_credentials(self):
        """Test synchronous login with invalid credentials."""
        response = Authentication.login(username_email=self.invalid_email, password=self.invalid_password)
        self.assertIsInstance(response, FreddyError, "Expected FreddyError object.")
        self.assertEqual(
            response.error_type,
            FreddyError.Type.INVALID_CREDENTIALS,
            "Expected INVALID_CREDENTIALS error."
        )
        print("Login failed as expected:", response.description)

    def test_login_async_success(self):
        """Test asynchronous login with valid credentials."""
        async def run_async_test():
            response = await Authentication.login_async(username_email=self.valid_email, password=self.valid_password)
            self.assertIsInstance(response, LoginResponse, "Expected LoginResponse object.")
            self.assertIsNotNone(response.token, "Token should not be None.")
            print("Async Login Successful! Token:", response.token)

        asyncio.run(run_async_test())

    def test_login_async_failure_invalid_credentials(self):
        """Test asynchronous login with invalid credentials."""
        async def run_async_test():
            response = await Authentication.login_async(username_email=self.invalid_email, password=self.invalid_password)
            self.assertIsInstance(response, FreddyError, "Expected FreddyError object.")
            self.assertEqual(
                response.error_type,
                FreddyError.Type.INVALID_CREDENTIALS,
                "Expected INVALID_CREDENTIALS error."
            )
            print("Async Login failed as expected:", response.description)

        asyncio.run(run_async_test())

if __name__ == "__main__":
    unittest.main()