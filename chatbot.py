import subprocess
import sys


def detect_intent(user_input):
    image_keywords = [
        "generate an image",
        "create an image",
        "draw",
        "make an image",
        "show me",
        "picture of",
        "image of"
    ]

    text = user_input.lower()

    for word in image_keywords:
        if word in text:
            return "image"

    return "chat"


def chat_with_ollama(message):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=message.encode("utf-8"),
        capture_output=True
    )

    return result.stdout.decode("utf-8", errors="ignore").strip()


def generate_image(prompt):
    """
    Calls the Stable Diffusion image generator
    """
    subprocess.run(
        [sys.executable, "generate_image.py"],
        input=prompt,
        text=True
    )


def main():
    print("🤖 AI Chatbot started")
    print("Type naturally (chat or image requests)")
    print("Type /exit to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "/exit":
            print("Goodbye 👋")
            break

        # 🔹 INTENT ROUTING
        intent = detect_intent(user_input)

        if intent == "image":
            print("🎨 Generating image...")
            generate_image(user_input)
        else:
            response = chat_with_ollama(user_input)
            print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
