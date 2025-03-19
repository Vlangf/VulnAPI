from flask import Flask, request
from zeep import Settings, Client
from zeep.transports import Transport

app = Flask(__name__)

# Create a simple SOAP service
class HelloWorldService:
    def say_hello(self, name, times):
        return f"Hello, {name}!" * times

# Create a WSDL-like structure
WSDL = '''<?xml version="1.0"?>
<definitions name="HelloWorldService"
             targetNamespace="http://example.com/soap"
             xmlns="http://schemas.xmlsoap.org/wsdl/"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:tns="http://example.com/soap"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <message name="say_helloRequest">
        <part name="name" type="xsd:string"/>
        <part name="times" type="xsd:int"/>
    </message>
    <message name="say_helloResponse">
        <part name="result" type="xsd:string"/>
    </message>
    <portType name="HelloWorldPortType">
        <operation name="say_hello">
            <input message="tns:say_helloRequest"/>
            <output message="tns:say_helloResponse"/>
        </operation>
    </portType>
    <binding name="HelloWorldBinding" type="tns:HelloWorldPortType">
        <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="say_hello">
            <soap:operation soapAction="http://example.com/soap/say_hello"/>
            <input>
                <soap:body use="encoded" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
            </input>
            <output>
                <soap:body use="encoded" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
            </output>
        </operation>
    </binding>
    <service name="HelloWorldService">
        <port name="HelloWorldPort" binding="tns:HelloWorldBinding">
            <soap:address location="http://localhost:8888/soap"/>
        </port>
    </service>
</definitions>'''

# Create a custom transport that handles the SOAP requests
class FlaskTransport(Transport):
    def __init__(self, app):
        self.app = app

    def post(self, address, message, headers):
        with self.app.test_client() as client:
            response = client.post('/soap', data=message, headers=headers)
            return response.data

# Create the service
service = HelloWorldService()
transport = FlaskTransport(app)
settings = Settings(strict=False)
server = Client(WSDL, transport=transport, settings=settings)

@app.route("/soap", methods=["POST"])
def soap():
    return server.service.say_hello(request.data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
