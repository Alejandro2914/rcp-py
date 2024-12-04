import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
print(proxy.hello_world())
