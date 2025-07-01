from summarizer import summarize_messages

api_key = "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"

messages = [
    "Привет, как дела?",
    "Мне нужна помощь с заказом.",
    "Какой статус моего заказа?"
]

summary = summarize_messages(messages,api_key)
print("Deepseek cavabiiiii: ")
print(summary)