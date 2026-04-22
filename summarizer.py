import requests

def summarize_text(text):
    url = "http://localhost:11434/api/generate"

    prompt = f"You are a summarization tool. Summarize text in a short and clear way.\n\nText:\n{text}"

    data = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()['response']
    else:
        return response.text  

text = input("Enter your text:\n")
summary = summarize_text(text)

print("\n--- Summary ---")
print(summary)
