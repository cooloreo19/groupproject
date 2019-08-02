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
        {"ID": 0, "question": "Imagine yourself in a dungeon. There are two doors: Door1 you know for sure holds a deadly booby trap, and the other contains a furocious lion that hasn't eaten in three weeks! What path will you choose?",
            "count": 1,
            "correct_answer": "Door2",
            "answers": [
                "Door 1",
                "Door 2",
                "Sit and Rot",
                "Both"
            ]
        },
        {"ID":1, "question": "You friend gives you this wierd looking phrase. Can you figure out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
                ]
            },
        {"ID":2, "question": "What is the difference between a Student studying and a Farmer watching his cattle?",
           "count": 1,
            "correct_answer": "One stocks his mind, while the other watches his stock",
            "answers": [
                "One stocks bookshelves, while the other reads the books",
                "One stocks his mind, while the other watches his stock",
                "One goes to school all day, while the other goes to the farm all day",
                "IDK"
            ]
        },
        {"ID":3, "question": "Blue, Yellow, GRASS :: Red, White, ROSE :: Red, Yellow, ... What's Next?",
           "count": 1,
            "correct_answer": "Orange",
            "answers": [
                "Orange",
                "Pie",
                "Flower",
                "Ornange"
            ]
        },
        {"ID":4, "question": "It has keys but no locks, space but no room, you can enter but can't go inside...",
           "count": 1,
            "correct_answer": "It's a Keyboard",
            "answers": [
                "It's a Soul",
                "It's a Phone",
                "It's a Ship",
                "It's a Keyboard"
            ]
        },
        {"ID":5, "question": "1, 111, 131, 11311, 12321...What's Next?",
           "count": 1,
            "correct_answer": "14341",
            "answers": [
                "1123211",
                "14341",
                "1223221",
                "142241"
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



        qtn = { "answers": trivia_url_endpoint[next]["answers"],
            "question": trivia_url_endpoint[next]["question"],
            "correct": trivia_url_endpoint[next]["correct_answer"],
            "ID": next
            }

        # random.shuffle(qtn.question())



        self.response.write(quiz_template.render(qtn))

    def post(self):
        print(self.request.get("answers"))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/brainquiz', BrainQuizPage),
], debug=True)
