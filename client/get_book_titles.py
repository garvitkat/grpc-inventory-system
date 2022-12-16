import client.inventory_client as client


# print details for isbn 001
client1 = client.TestInventory()
result = client1.run_with_isbn("001")
print(result)

print("--------------------------")

# print details for isbn 002
client2 = client.TestInventory()
result2 = client2.run_with_isbn("002")
print(result2)

