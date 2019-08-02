import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
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

trivia_url_endpoint = [
        {"ID": 0, "question": "Imagine yourself in a dungeon. There are two doors: One you know for sure is the way out, and the other contains a furocious lion that hasn't eaten in three weeks! What path will you choose?",
            "count": 1,
            "correct_answer": "Door 1",
            "answers": [
                "Door 1",
                "Door 2",
                "Sit and Rot",
                "Make Tallies on the Wall"
            ],
	    "correct": False
        },
        {"ID":1, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
                ],
	    "correct": False
            },
        {"ID":2, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
            ],
	    "correct": False
        },
        {"ID":3, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
            ],
	    "correct": False
        },
        {"ID":4, "question": "You friend gives you this wierd looking phrase. Can you figur out what letters come next? :: Y F G Y T W L P C Y F O ...",
           "count": 1,
            "correct_answer": "W L C N",
            "answers": [
                "W Q D N",
                "J I D K",
                "W L C N",
                "I D C N"
            ], 
	    "correct": False
        },
    ]

class BrainDiagram(webapp2.RequestHandler):
  def get(self):
      user = users.get_current_user()
      email_address = user.nickname()
      cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
      first_name = CssiUser.query().filter(CssiUser.first_name == cssi_user.first_name).get()

      # If the user is registered...
      if cssi_user:
          braindiagram_html = the_jinja_env.get_template('HTML_groupproject.html')

          thisdict =	{
            "username": cssi_user,
            "first_name": cssi_user.first_name
          }
          self.response.write(braindiagram_html.render(thisdict))   



class CssiUser(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()

class LogIn(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      signout_link_html = '<a href="%s">sign out</a>' % (
              users.create_logout_url('/login'))
      signout_link = users.create_logout_url('/login')
      email_address = user.nickname()
      cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
      # If the user is registered...
      if cssi_user:
        # Greet them with their personal information
            login_html = the_jinja_env.get_template('thanksforusing.html')
            print(cssi_user)

            self.response.write(login_html.render(cssi_user = cssi_user, signout_link= signout_link))

      # If the user isn't registered...
      else:
        # Offer a registration form for a first-time visitor:
        self.response.write('''
            Goodbye, %s!  <br>
            <form method="post" action="/login">

            </form><br> %s <br>
            ''' % (email_address, signout_link_html))
    else:
      # If the user isn't logged in...
      login_url = users.create_login_url('/userinfo')
      login_html = the_jinja_env.get_template('login.html')
      # Prompt the user to sign in.
      self.response.write(login_html.render())

  def post(self):
    user = users.get_current_user()
    cssi_user = CssiUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        email=user.nickname())
    cssi_user.put()
    login_html = the_jinja_env.get_template('thankssignup.html')
    print(cssi_user)

    self.response.write(login_html.render(cssi_user = cssi_user))

class UserInfo(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        email_address = user.nickname()
        cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
        first_name = CssiUser.query().filter(CssiUser.first_name == cssi_user.first_name).get()

        # If the user is registered...
        if cssi_user:
            login_html = the_jinja_env.get_template('welcomeuser.html')
            print(cssi_user)

            thisdict =	{
              "username": cssi_user,
              "first_name": cssi_user.first_name
            }
            x = thisdict["username"]
            self.response.write(login_html.render(thisdict))
        # If the user isn't registered...



        else:
          # Offer a registration form for a first-time visitor:
          self.response.write(login_html.render(cssi_user = cssi_user))

          login_html = the_jinja_env.get_template('makeaccount.html')
          self.response.write(login_html.render(thisdict))


class BrainQuizPage(webapp2.RequestHandler):
    def get(self):
        current = self.request.get("current")
        next = 0
        if current != "":
            next = int(current)+ 1

        if next >= len(trivia_url_endpoint):
            self.response.write("<meta http-equiv=\"Refresh\" content=\"0; url=https://www.w3docs.com\" />")
            return

        quiz_template = the_jinja_env.get_template('quiz.html')



        # all_answers = trivia_url_endpoint[next]
        # for trivia_url_endpoint.next in trivia_url_endpoint:
        #     all_answers.append(trivia_url_endpoint.next["answers"])
        # add ...........................^[next]
        # for answer in trivia_url_endpoint[0]["incorrect_answers"]:

        qtn = self.get_current_qtn(next)
        self.response.write(quiz_template.render(qtn))

    def post(self):
        print(self.request.get("answer"))
        ans = self.request.get("answer")
	num = self.request.get("question")
        qtn = self.get_current_qtn(int(num))
        
        if(ans == qtn["correct"]):
	    print("ye")
	else:
	    print("no")
    
    def get_current_qtn(self, next):

        qtn = { "answers": trivia_url_endpoint[next]["answers"],
            "question": trivia_url_endpoint[next]["question"], "correct": trivia_url_endpoint[next]["correct_answer"], "ID": next
            }
	return qtn
	

app = webapp2.WSGIApplication([
    ('/brainquiz', BrainQuizPage),
    ('/login', LogIn),
    ('/braindiagram', BrainDiagram),
    ('/', MainPage),
    ('/userinfo', UserInfo),
    ], debug=True)
