# VulnAPI

12 vulnerable endpoints and 9 different API types for security testing.

## Vulnerable Endpoints (FastAPI, port 5035)

| Endpoint | Vulnerability |
|----------|--------------|
| `/ping` | Command Injection |
| `/sqli` | SQL Injection |
| `/xss`, `/search`, `/search_1`..`/search_11` | XSS (Reflected, Stored, DOM) |
| `/rce` | Remote Code Execution |
| `/ssti` | Server-Side Template Injection |
| `/xxe` | XML External Entity |
| `/ptrav` | Path Traversal |
| `/open_redirect`, `/redir`, `/redirect` | Open Redirect |
| `/transfer`, `/transfer_form` | CSRF |
| `/page/{page}` | File Inclusion |
| `/upload_file` | File Upload |
| `/contact` | Insecure CAPTCHA |

## API Services

| Port | API Type |
|------|----------|
| 8082 | GraphQL |
| 443  | gRPC |
| 8080 | JSON:API |
| 8085 | JSON:API (v2) |
| 8086 | Web HTML |
| 8443 | JSON-RPC |
| 8880 | JSON-RPC (second) |
| 8000 | OData |
| 8888 | SOAP |
| 8081 | WebDAV |
| 1080 | WebSocket |
| 4567 | XML-RPC |
| 8089 | GraphQL (second) |

## How to deploy

```bash
docker build -t multi-api-apps .
```

```bash
docker run -d --restart=unless-stopped \
  -p 5035:5035 \
  -p 8082:8082 \
  -p 443:443 \
  -p 8080:8080 \
  -p 8085:8085 \
  -p 8086:8086 \
  -p 8443:8443 \
  -p 8880:8880 \
  -p 8000:8000 \
  -p 8888:8888 \
  -p 8081:8081 \
  -p 1080:1080 \
  -p 4567:4567 \
  -p 8089:8089 \
  multi-api-apps
```

## How to check specific APIs

1. **WebSocket** — `websocat ws://host:1080/ws`
2. **XML-RPC** — use client in `clients/`
3. **GraphQL** — `curl -X POST http://host:8082 -H "Content-Type: application/json" -d '{"query": "{ hello }"}'`
4. **gRPC** — use client in `clients/`
5. **JSON-RPC** — `curl -X POST http://host:8443/jsonrpc -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "hello", "params": {"name":"World"}, "id": 1}'`
6. **JSON:API** — `curl http://host:8080/v1/World`
7. **OData** — `curl -X GET "http://host:8000/odata/\$metadata"`
8. **SOAP** — `curl -X POST http://host:8888/soap`

## Sending test requests

```bash
python vuln_app/send_requests.py --host http://localhost:5035 --count 5
```
