import json
from pathlib import Path

from demo_assist import analyze_message


def load_messages(file_path: Path):
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    current_dir = Path(__file__).parent
    input_file = current_dir / "test_messages.json"

    messages = load_messages(input_file)

    print("agent-assist-oss | Batch Demo")
    print(f"Loaded {len(messages)} test messages.\n")

    for item in messages:
        message_id = item.get("id", "unknown")
        message_text = item.get("message", "")

        result = analyze_message(message_text)

        print("=" * 60)
        print(f"ID: {message_id}")
        print(f"Input: {result['input']}")
        print("\nDetected signals:")
        if result["detected_signals"]:
            for signal in result["detected_signals"]:
                print(f"- {signal}")
        else:
            print("- none")

        print("\nSuggested reply:")
        print(result["suggested_reply"])

        print("\nSummary:")
        print(result["summary"])

        print("\nCRM note:")
        print(result["crm_note"])
        print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
