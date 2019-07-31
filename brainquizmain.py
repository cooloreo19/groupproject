import webapp2
import jinja2
import os
# from google.appengine.api import urlfetch
import json
import random



the_jinja_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)


class BrainQuizPage(webapp2.RequestHandler):
    def get(self):
        trivia_url_endpoint = {"category": "Frontal Lobe",
            "question": "MAIN CONTROL",
            "count": 1,
            "correct_answer": "Jupiter",
            "incorrect_answers": [
            "Uranus",
            "Neptune",
            "Mars"
            ]};


        quiz_template = the_jinja_env.get_template('quiz.html')



        all_answers = [trivia_url_endpoint["correct_answer"]]
        for answer in trivia_url_endpoint["incorrect_answers"]:
            all_answers.append(answer)
        random.shuffle(all_answers)

        qtn = { "answers": all_answers,
            "question": trivia_url_endpoint["question"], "correct": trivia_url_endpoint["correct_answer"]
            }





        self.response.write(quiz_template.render(trivia_url_endpoint))

app = webapp2.WSGIApplication([
    ('/brainquiz', BrainQuizPage)
], debug=True)
