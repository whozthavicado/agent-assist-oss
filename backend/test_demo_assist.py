import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from demo_assist import analyze_message, detect_signals, normalize_text, suggest_reply


class DemoAssistTests(unittest.TestCase):
    def test_normalize_text_strips_and_lowercases(self):
        self.assertEqual(normalize_text("  Hello There  "), "hello there")

    def test_detects_price_objection_and_hesitation(self):
        message = "It's too expensive. I need to think about it."
        signals = detect_signals(message)

        self.assertIn("price_objection", signals)
        self.assertIn("hesitation", signals)

    def test_detects_support_frustration(self):
        message = "I've already explained this twice and nothing has changed."
        signals = detect_signals(message)

        self.assertIn("frustration", signals)
        self.assertIn("repeat_issue", signals)

    def test_suggest_reply_for_info_request(self):
        reply = suggest_reply(["info_request"])
        self.assertIn("send you the key information", reply.lower())

    def test_analyze_message_returns_expected_shape(self):
        result = analyze_message("I can't pay today. Maybe next week.")

        self.assertIn("input", result)
        self.assertIn("detected_signals", result)
        self.assertIn("suggested_reply", result)
        self.assertIn("summary", result)
        self.assertIn("crm_note", result)
        self.assertIn("payment_delay", result["detected_signals"])

    def test_no_strong_signal_case(self):
        result = analyze_message("Thanks, I just wanted to confirm the hours.")
        self.assertEqual(result["detected_signals"], [])
        self.assertIn("No strong predefined signals", result["summary"])


if __name__ == "__main__":
    unittest.main()
