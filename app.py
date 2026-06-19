import json
from google import genai
from google.genai import types

# Gemini API Key
# API_KEY = "AQ.Ab8RN6LzrVeWrTuuR5jBLL_juJQJE7jM-nmbo0dCZm40y89UYg"

def query_json_with_gemini():
    try:
        # Initialize Gemini Client
        client = genai.Client(api_key=API_KEY)

        # Load JSON Data
        with open("data.json", "r", encoding="utf-8") as file:
            json_data = json.load(file)

        print("=" * 50)
        print("🚀 Gemini JSON Search Assistant")
        print("Type 'exit' to quit")
        print("=" * 50)

        while True:
            user_question = input("\n🔍 Ask a question: ").strip()

            if user_question.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break

            if not user_question:
                continue

            system_instruction = """
            You are a JSON Search Assistant.

            Rules:
            1. Answer ONLY from the provided JSON data.
            2. Do not make up information.
            3. If the answer is not available, reply:
               'Data not found in JSON.'
            4. Keep answers short and accurate.
            """

            prompt = f"""
            JSON Data:
            {json.dumps(json_data, indent=2)}

            User Question:
            {user_question}
            """

            print("\n🤖 Thinking...")

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.2
                )
            )

            print("\n💡 Answer:")
            print(response.text)
            print("-" * 50)

    except FileNotFoundError:
        print("❌ data.json file not found.")
    except json.JSONDecodeError:
        print("❌ Invalid JSON format in data.json.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    query_json_with_gemini()