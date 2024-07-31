from flask import Flask, request, render_template
from chatbot_model.model import QAModel

app = Flask(__name__)
chat_history = []
model = QAModel("Fsoft-AIC/videberta-base")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        context = request.form.get("context", "")
        question = request.form.get("question", "")
        answer = model.get_answer(question, context)
        print(context)
        if question:
            chat_history.append({"role": "user", "text": question})
        if answer:
            chat_history.append({"role": "bot", "text": answer})
        return render_template("index.html", chat_history=chat_history, context=context, question=question)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)