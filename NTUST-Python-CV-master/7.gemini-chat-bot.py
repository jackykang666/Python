from google import genai


def chat_gemini(user_prompt):
    """透過 Gemini 進行溝通"""
    client = genai.Client(api_key="AIzaSyB7OEB5hxLZX34G_6ini3G23tZ44mLyQl0")
    system_prompt = ""
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[system_prompt + user_prompt],
    )
    return res.text


while True:
    user_input = input("請輸入內容與 Gemini 對話:")
    response = chat_gemini(user_input)
    print(f"Gemini: {response}")
