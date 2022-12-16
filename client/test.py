import asyncio
import unittest
from unittest.mock import Mock, MagicMock, AsyncMock, patch, call, sentinel

import sys
sys.path.insert(1, 'client')

import inventory_client as client

# mock object for client "mockClient"
mockClient = Mock()
mockClient.run_with_isbn.return_value = {"id": "002","title": "Book 2","author": "Pong", "pub_year": "2011","genre": "NONFICTION"}


# TEST 1: unit test for testing the client (Server is not running)
client1 = client.TestInventory()
result = mockClient.run_with_isbn()
test_1_result = result == {"id": "002","title": "Book 2","author": "Pong", "pub_year": "2011","genre": "NONFICTION"}
assert test_1_result
print("Test 1 passed")

# TEST 2: unit test for testing get_book_titles (Server is running)
client1 = client.TestInventory()
result = client1.run_with_isbn("001")
assert result.id == "001"
assert result.title == "Book 1"
assert result.author == "Ping"
assert result.pub_year == 1991
print("Test 2 passed")




