import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from demo_assist import (
    analyze_message,
    detect_signals,
    load_signal_rules,
    normalize_text,
    suggest_reply,
)


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

    def test_load_signal_rules_from_external_file(self):
        custom_rules = {
            "budget_question": ["need a lower price", "can you lower the price"],
            "language_switch": ["háblame en español"]
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            rules_path = Path(temp_dir) / "custom_rules.json"
            rules_path.write_text(json.dumps(custom_rules), encoding="utf-8")

            loaded_rules = load_signal_rules(rules_path)

        self.assertIn("budget_question", loaded_rules)
        self.assertIn("language_switch", loaded_rules)
        self.assertIn("need a lower price", loaded_rules["budget_question"])

    def test_detect_signals_with_custom_rules(self):
        custom_rules = {
            "budget_question": ["need a lower price"],
        }

        signals = detect_signals(
            "I need a lower price before I move forward.",
            signal_rules=custom_rules,
        )

        self.assertEqual(signals, ["budget_question"])


if __name__ == "__main__":
    unittest.main()
