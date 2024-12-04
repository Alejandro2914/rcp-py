from xmlrpc.server import SimpleXMLRPCServer

def hello_world():
    return "¡Hola Mundo desde RPC!"

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(hello_world, "hello_world")
print("Servidor RPC corriendo en http://localhost:8000")
server.serve_forever()
