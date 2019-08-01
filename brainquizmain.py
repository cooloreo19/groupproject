import webapp2
import jinja2
import os
import json
import random



the_jinja_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('HTML_groupproject.html')
        self.response.write(home_template.render())

class BrainQuizPage(webapp2.RequestHandler):
    def get(self):

        trivia_url_endpoint = [
        {"ID": 0, "question": "FRONTAL LOBE: dlfjldkfglgkjdflgkjfdlgkjld?",
            "count": 1,
            "correct_answer": "Jupiter",
            "answers": [
                "Jupiter",
                "Uranus",
                "Neptune",
                "Mars"
            ]
        },
        {"ID":1, "question": "TEMPORAL LOBE: ",
            "count": 1,
            "correct_answer": "Jiter",
            "answers": [
                "Jiter",
                "Urus",
                "Nune",
                "Mrs"
                ]
            },
        ]


        quiz_template = the_jinja_env.get_template('quiz.html')



        all_answers = trivia_url_endpoint[0]["answers"]
        # for answer in trivia_url_endpoint[0]["incorrect_answers"]:
        #     all_answers.append(answer)
        random.shuffle(all_answers)

        qtn = { "answers": all_answers,
            "question": trivia_url_endpoint[0]["question"], "correct": trivia_url_endpoint[0]["correct_answer"]
            }





        self.response.write(quiz_template.render(qtn))

    def post(self):
        print(self.request.get("answers"))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/brainquiz', BrainQuizPage),
], debug=True)
