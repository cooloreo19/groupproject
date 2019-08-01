import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
	#main_page = JINJA_ENVIRONMENT.get_template('templates/home.html')
	#self.response.write(main_page.render())
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Saluton, Mondo!')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
