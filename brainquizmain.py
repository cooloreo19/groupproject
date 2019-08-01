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
        current = self.request.get("current")
        next = 0
        if current != "":
            next = int(current)+ 1



        trivia_url_endpoint = [
        {"ID": 0, "question": "Imagine yourself in a dungeon. There are two doors: One you know for sure is the way out, and the other contains a furocious lion that hasn't eaten in three weeks! What path will you choose?",
            "count": 1,
            "correct_answer": "Door 1",
            "answers": [
                "Door 1",
                "Door 2",
                "Sit and Rot",
                "Make Tallies on the Wall"
            ]
        },
        {"ID":1, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
                ]
            },
        {"ID":2, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
            ]
        },
        {"ID":3, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
            ]
        },
        {"ID":4, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
            ]
        },
    ]
        if next >= len(trivia_url_endpoint):
            self.response.write("<meta http-equiv=\"Refresh\" content=\"0; url=https://www.w3docs.com\" />")
            return






        quiz_template = the_jinja_env.get_template('quiz.html')



        # all_answers = trivia_url_endpoint[next]
        # for trivia_url_endpoint.next in trivia_url_endpoint:
        #     all_answers.append(trivia_url_endpoint.next["answers"])
        # add ...........................^[next]
        # for answer in trivia_url_endpoint[0]["incorrect_answers"]:

        # random.shuffle(all_answers)

        qtn = { "answers": trivia_url_endpoint[next]["answers"],
            "question": trivia_url_endpoint[next]["question"], "correct": trivia_url_endpoint[next]["correct_answer"], "ID": next
            }





        self.response.write(quiz_template.render(qtn))

    def post(self):
        print(self.request.get("answers"))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/brainquiz', BrainQuizPage),
], debug=True)
