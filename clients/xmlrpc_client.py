import xmlrpc.client
import ssl

client = xmlrpc.client.ServerProxy("http://vuln.host.com:8009/xmlrpc", context=ssl._create_unverified_context())
print(client.hello("World"))
