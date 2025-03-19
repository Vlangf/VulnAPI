9 different types of APIs and vuln_endpoints, for testing

**How to deploy:**

```
docker build -t multi-api-apps .
```

`docker run -d --restart=unless-stopped -p 8082:8082 -p 443:443 -p 8080:8080 -p 8085:8085 -p 8443:8443 -p 8880:8880 -p 8000:8000 -p 8888:8888 -p 8081:8081 -p 1080:1080 -p 4567:4567 -p 8089:8089 multi-api-apps`


| Port | API type |
|------| ------- |
| 8082 | graphql   |
| 443  | grpc   | -
| 8080 | jsonapi    |
| 8085 | web_html    |
| 8443 | jsonrpc    | 
| 8880 | jsonrpc_second    | 
| 8000 | odata    | 
| 8888 | soap    |
| 8081 | webdav    |
| 1080 | websocket    | -
| 4567 | xmlrps    | -
| 8089 | graphql_second   |



**How to check specific APIs:**

1. websocket - CLI command `websocat ws://host:8008/ws`
2. xmlrps - use client in dir clients
3. graphql - `curl -X POST http://host -H "Content-Type: application/json" -d '{"query": "{ hello }"}'`
4. grpc - use client in dir clients
5. jsonrpc - `curl -X POST http://host:8004/jsonrpc -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "hello", "params": {"name":"World"}, "id": 1}'`
6. jsonapi - `curl http://host:8003/v1/World`
7. odata - `curl -X GET "http://host:8000/odata/\$metadata"`
8. soap - `curl -X POST http://host:8006/soap`
