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


class BrainDiagram(webapp2.RequestHandler):
  def get(self):
    braindiagram_html = the_jinja_env.get_template('HTML_groupproject.html')
    self.response.write(braindiagram_html.render())


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
        # If the user is registered...
        if cssi_user:
            login_html = the_jinja_env.get_template('welcomeuser.html')
            print(cssi_user)

            self.response.write(login_html.render(cssi_user = cssi_user))
        # If the user isn't registered...
        else:
          # Offer a registration form for a first-time visitor:
          login_html = the_jinja_env.get_template('makeaccount.html')
          self.response.write(login_html.render(cssi_user = cssi_user))




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
    ('/brainquiz', BrainQuizPage),
    ('/login', LogIn),
    ('/braindiagram', BrainDiagram),
    ('/userinfo', UserInfo),
], debug=True)
