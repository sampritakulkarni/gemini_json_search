from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6LzrVeWrTuuR5jBLL_juJQJE7jM-nmbo0dCZm40y89UYg"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)