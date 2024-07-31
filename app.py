from flask import Flask, request, render_template
from chatbot_model.model import QAModel

app = Flask(__name__)
model = QAModel("Fsoft-AIC/videberta-base")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]
        context = request.form["context"]
        answer = model.get_answer(question, context)
        return render_template("index.html", question=question, context=context, answer=answer)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5000)