import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
history = []

def ask(user_input: str) -> str:
    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system="You are Jarvis, a personal AI assistant. Be concise.",
        messages=history,
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply

def reset():
    history.clear()