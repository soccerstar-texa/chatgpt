
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

api_key = "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"
openai.api_key = api_key


@app.route('/')
def home():
    return render_template('projectt.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    chat_response = response['choices'][0]['message']['content']
    return render_template('projectt.html', user_input=user_input, chat_response=chat_response)


if __name__ == '__main__':
    app.run(debug=True)
