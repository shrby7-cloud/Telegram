import requests

GROQ_API_KEY = "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"

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.1-8b-instant",

    "messages": [
        {"role": "user", "content": "اكتب سؤالًا محرجًا بسيطًا"}
    ],
    "max_tokens": 50
}

r = requests.post(url, headers=headers, json=payload)
print("STATUS:", r.status_code)
print(r.text)
