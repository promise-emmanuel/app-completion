from dotenv import load_dotenv, find_dotenv
import os
from openai import OpenAI
from flask import Flask, request, render_template


# Load environment variables
_ = load_dotenv(find_dotenv())
client = OpenAI()
model = os.environ['MODEL']
app=Flask(__name__)

@app.route("/", methods=["POST", 'GET'])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        prompt = f"""
            Summarize the following text by providing a concise overview in not more than 50 words.
            Here is the text: {query}
        """
        messages = [{"role":"user", "content":prompt}]        
        response = client.chat.completions.create(model=model, messages=messages)
        return render_template('index.html', query="Hello World!", response=response.choices[0].message.content)
    return render_template('index.html')

if __name__ =="__main__":
    port = int(os.environ.get('port', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)