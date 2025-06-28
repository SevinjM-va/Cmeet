# summarizer.py
import requests

def summarize_messages(messages: list[str], api_key: str) -> str:
    if not messages:
        return "Сегодня не пришло никаких сообщений."

    text = "\n".join(f"- {msg}" for msg in messages)

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek",
        "messages": [
            {
                "role": "user",
                "content": f"Пожалуйста, сделай краткое summary следующих сообщений:\n{text}"
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["message"]["content"]
