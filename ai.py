from openai import OpenAI
import os

# הגדר את מפתח ה-API כמשתנה סביבה
os.environ["XAI_API_KEY"] = "xai-WtTfjdk66kwGueEEOR38DbYNBEZNZpBr83p821ig3HyGBA8E2ngHlWRhrY28Dp3fXo66RmUkn4U5D7B5"

# יצירת לקוח API
client = OpenAI(
    api_key="xai-WtTfjdk66kwGueEEOR38DbYNBEZNZpBr83p821ig3HyGBA8E2ngHlWRhrY28Dp3fXo66RmUkn4U5D7B5",
    base_url="https://api.x.ai/v1"
)

# יצירת רשימת הודעות עם הודעת המערכת הראשונית
messages = [
    {
        "role": "system",
        "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
    }
]

# לולאה אינסופית לשיחה
while True:
    # קבלת קלט מהמשתמש
    user_input = input("אתה: ")
    
    # אם המשתמש מקליד 'quit', יציאה מהלולאה
    if user_input.lower() == "quit":
        break
    
    # הוספת ההודעה של המשתמש לרשימת ההודעות
    messages.append({"role": "user", "content": user_input})
    
    # שליחת בקשת צ'אט
    response = client.chat.completions.create(
        model="grok-beta",
        messages=messages,
        temperature=0.7
    )
    
    # קבלת התשובה מהמודל
    assistant_response = response.choices[0].message.content
    print(f"Grok: {assistant_response}")
    
    # הוספת התשובה של המודל לרשימת ההודעות
    messages.append({"role": "assistant", "content": assistant_response})