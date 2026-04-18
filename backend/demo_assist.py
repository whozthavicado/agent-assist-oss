from __future__ import annotations

import json
from typing import Dict, List


SIGNAL_RULES: Dict[str, List[str]] = {
    "price_objection": [
        "too expensive",
        "too much",
        "expensive",
        "very expensive",
        "costs too much",
        "price is too high",
        "muy caro",
        "caro",
    ],
    "hesitation": [
        "i need to think about it",
        "i'll think about it",
        "let me think",
        "maybe later",
        "not sure yet",
        "lo voy a pensar",
        "déjame pensarlo",
        "dejame pensarlo",
    ],
    "info_request": [
        "send me the information",
        "send me info",
        "send me details",
        "can you send me details",
        "mandame informacion",
        "mándame información",
        "enviame informacion",
        "envíame información",
    ],
    "not_interested": [
        "not interested",
        "i'm not interested",
        "no thanks",
        "no thank you",
        "not right now",
        "no me interesa",
    ],
    "frustration": [
        "this is frustrating",
        "i'm frustrated",
        "nothing has changed",
        "i already explained this",
        "explained this twice",
        "this makes no sense",
        "estoy frustrado",
        "ya expliqué esto",
        "ya explique esto",
    ],
    "repeat_issue": [
        "again",
        "still happening",
        "nothing has changed",
        "already explained this twice",
        "same problem",
        "same issue",
        "otra vez",
        "sigue pasando",
        "mismo problema",
    ],
    "payment_delay": [
        "i can't pay today",
        "maybe next week",
        "i can pay later",
        "not today",
        "next week",
        "no puedo pagar hoy",
        "tal vez la próxima semana",
        "la proxima semana",
    ],
    "uncertain_commitment": [
        "maybe",
        "probably",
        "i guess",
        "not sure",
        "perhaps",
        "tal vez",
        "quizá",
        "quizas",
        "no estoy seguro",
    ],
}


def normalize_text(text: str) -> str:
    return text.strip().lower()


def detect_signals(message: str) -> List[str]:
    normalized = normalize_text(message)
    detected: List[str] = []

    for signal, keywords in SIGNAL_RULES.items():
        if any(keyword in normalized for keyword in keywords):
            detected.append(signal)

    return detected


def suggest_reply(signals: List[str]) -> str:
    if "price_objection" in signals and "hesitation" in signals:
        return (
            "I understand. Many customers compare options first. "
            "Would it help if I explain the value more clearly or show a version that fits your budget better?"
        )

    if "info_request" in signals:
        return (
            "Of course. I can send you the key information right away. "
            "Before I do, would you like a quick summary of the most important points?"
        )

    if "frustration" in signals or "repeat_issue" in signals:
        return (
            "I understand your frustration. Let me take ownership of this, summarize the issue clearly, "
            "and help move this forward faster."
        )

    if "payment_delay" in signals:
        return (
            "Understood. What day would be most realistic for you so I can note it correctly and follow up properly?"
        )

    if "not_interested" in signals:
        return (
            "Understood. Before we close this, would it be helpful if I leave you with the most relevant information "
            "in case the timing changes later?"
        )

    if "hesitation" in signals:
        return "That makes sense. What would help you feel more confident about the next step?"

    return "Thanks for sharing that. Let me summarize your situation and guide the next best step clearly."


def build_summary(message: str, signals: List[str]) -> str:
    if not signals:
        return (
            f"Customer message received: '{message}'. "
            "No strong predefined signals were detected."
        )

    readable_signals = ", ".join(signals)
    return (
        f"Customer message received: '{message}'. "
        f"Detected signals: {readable_signals}."
    )


def build_crm_note(message: str, signals: List[str]) -> str:
    if not signals:
        return (
            f"Customer said: '{message}'. No major predefined signal detected. "
            "Recommended next step: review context manually."
        )

    readable_signals = ", ".join(signals)
    return (
        f"Customer said: '{message}'. Detected signals: {readable_signals}. "
        "Recommended next step: follow up based on the detected intent and conversation context."
    )


def analyze_message(message: str) -> Dict[str, object]:
    signals = detect_signals(message)

    return {
        "input": message,
        "detected_signals": signals,
        "suggested_reply": suggest_reply(signals),
        "summary": build_summary(message, signals),
        "crm_note": build_crm_note(message, signals),
    }


def main() -> None:
    print("agent-assist-oss | Rule-Based Demo")
    print("Type a customer message and press Enter.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Customer message: ").strip()

        if user_input.lower() == "exit":
            print("Exiting demo.")
            break

        result = analyze_message(user_input)

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

        print("\nJSON output:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
