#!/bin/bash

# Check if credentials are provided as arguments
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <username> <password> [api_key]"
    echo "Example: $0 test@example.com mypassword sk_test_key"
    exit 1
fi

# Set environment variables
export AITRONOS_TEST_USERNAME="$1"
export AITRONOS_TEST_PASSWORD="$2"

# Set API key if provided
if [ "$#" -eq 3 ]; then
    export AITRONOS_TEST_API_KEY="$3"
fi

# Run the tests
python -m unittest tests/test_authentication.py 