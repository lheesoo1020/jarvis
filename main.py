from modules import stt, llm

def main():
    print("Jarvis is ready. Press Enter to speak, Ctrl+C to quit.\n")
    stt.load_model()

    while True:
        input("[ Press Enter to speak ]")

        user_input = stt.transcribe(duration=5)
        if not user_input:
            print("(No speech detected)\n")
            continue

        print(f"You: {user_input}")
        reply = llm.ask(user_input)
        print(f"Jarvis: {reply}\n")

if __name__ == "__main__":
    main()
