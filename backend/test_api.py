import json
import sys
import threading
import unittest
from pathlib import Path
from urllib import error, request

sys.path.append(str(Path(__file__).resolve().parent))

from api import AgentAssistHandler
from http.server import HTTPServer


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), AgentAssistHandler)
        host, port = cls.server.server_address
        cls.base_url = f"http://{host}:{port}"
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def get_json(self, path: str):
        response = request.urlopen(f"{self.base_url}{path}")
        body = response.read().decode("utf-8")
        return response.status, json.loads(body)

    def post_json(self, path: str, payload=None, raw_body: bytes | None = None):
        if raw_body is None:
            raw_body = json.dumps(payload).encode("utf-8")

        req = request.Request(
            f"{self.base_url}{path}",
            data=raw_body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            response = request.urlopen(req)
            body = response.read().decode("utf-8")
            return response.status, json.loads(body)
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8")
            return exc.code, json.loads(body)

    def test_health_endpoint(self):
        status, data = self.get_json("/health")

        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["service"], "agent-assist-oss")

    def test_analyze_valid_message(self):
        status, data = self.post_json(
            "/analyze",
            payload={"message": "It's too expensive. I need to think about it."},
        )

        self.assertEqual(status, 200)
        self.assertIn("price_objection", data["detected_signals"])
        self.assertIn("hesitation", data["detected_signals"])
        self.assertIn("suggested_reply", data)
        self.assertIn("summary", data)
        self.assertIn("crm_note", data)

    def test_analyze_rejects_invalid_json(self):
        status, data = self.post_json("/analyze", raw_body=b"{")

        self.assertEqual(status, 400)
        self.assertEqual(data["error"], "Invalid JSON body.")

    def test_analyze_rejects_empty_message(self):
        status, data = self.post_json("/analyze", payload={"message": "   "})

        self.assertEqual(status, 400)
        self.assertIn("must be a non-empty string", data["error"])

    def test_analyze_rejects_missing_message(self):
        status, data = self.post_json("/analyze", payload={})

        self.assertEqual(status, 400)
        self.assertIn("must be a non-empty string", data["error"])


if __name__ == "__main__":
    unittest.main()
