import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        first_student = Student("Harry", "Potter", 59)
        self.response.write(first_student)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

class Student(object):
    def __init__(self, first_name, last_name, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.credits = credits

    def __str__(self):
        return "%s %s has %s credits." % (self.first_name, self.last_name, self.credits)
