import requests

r = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={
        "Authorization": "Bearer PUT_YOUR_GROQ_API_KEY_HERE",
        "Content-Type": "application/json"
    },
    json={
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": "اختبر"}]
    }
)

print(r.json())
