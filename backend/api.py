from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from demo_assist import analyze_message


HOST = "127.0.0.1"
PORT = 8000


class AgentAssistHandler(BaseHTTPRequestHandler):
    def _send_json(self, data: dict, status_code: int = 200) -> None:
        response = json.dumps(data, ensure_ascii=False).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send_json(
                {
                    "status": "ok",
                    "service": "agent-assist-oss",
                    "message": "Local API is running."
                }
            )
            return

        self._send_json(
            {
                "error": "Not found",
                "available_routes": ["/health", "/analyze"]
            },
            status_code=404,
        )

    def do_POST(self) -> None:
        if self.path != "/analyze":
            self._send_json(
                {
                    "error": "Not found",
                    "available_routes": ["/health", "/analyze"]
                },
                status_code=404,
            )
            return

        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length)

        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json(
                {"error": "Invalid JSON body."},
                status_code=400,
            )
            return

        message = payload.get("message", "")
        if not isinstance(message, str) or not message.strip():
            self._send_json(
                {"error": "Field 'message' must be a non-empty string."},
                status_code=400,
            )
            return

        result = analyze_message(message)
        self._send_json(result)

    def log_message(self, format: str, *args) -> None:
        return


def main() -> None:
    server = HTTPServer((HOST, PORT), AgentAssistHandler)
    print(f"agent-assist-oss API running at http://{HOST}:{PORT}")
    print("GET  /health")
    print("POST /analyze")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down API.")
        server.server_close()


if __name__ == "__main__":
    main()
