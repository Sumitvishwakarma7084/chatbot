# app.py
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": user_input}]
            )
            response_text = response.choices[0].message.content
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
