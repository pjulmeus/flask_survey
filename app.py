from flask import Flask, request, render_template, redirect
from surveys import satisfaction_survey , Survey, Question

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses = []
# list1 = []
questions_list = []
responses_list = []
# size = len(satisfaction_survey.questions)

@app.route('/')
def homepage():
    header = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("home.html", survey_title=header, survey_instructions = instructions)

# size = len(satisfaction_survey.questions)
# for n in range(size):
#     list1.append(n)
    
for q in satisfaction_survey.questions:
        questions_list.append(q.question)

for r in satisfaction_survey.questions:
    responses_list.append(r.choices)

# quest_dict = dict(zip(list1, questions_list))
# responses_dict = dict(zip(list1, responses_list))       

@app.route('/questions/<int:id>')
def questions(id): 
    q_item = questions_list[id]
    r_item = responses_list[id]
    if questions_list[id] == questions_list[-1]:
         return render_template("answer.html", responses = responses)
    # size = len(satisfaction_survey.questions)
    else:
        answers = request.args.get("responses")
        responses.append(answers)
        return render_template("questions.html", survey_questions = q_item, survey_respones = r_item, id = id)

# @app.route('/questions', methods = ["POST"])
# def questions_post():
#     answers = request.form['responses']
#     responses.append(answers)
#     return render_template("question.html", rep = responses)
# @app.route('/questions/<int:sizes>')
# def reroute(sizes):
#      sizes = size
#      return redirect("/answer")

# @app.route('/answer', methods = ["POST"])
# def answers():
#     return render_template("answer.html", responses = responses)
    