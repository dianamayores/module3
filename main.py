import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'team4_guestbook'
DEFAULT_GUESTBOOK_NAME1 = 'team4mem2_guestbook'
DEFAULT_GUESTBOOK_NAME2 = 'team4mem1_guestbook'
DEFAULT_GUESTBOOK_NAME3 = 'team4thesis_guestbook'
DEFAULT_GUESTBOOK_NAME4 = 'team4adviser_guestbook'
DEFAULT_GUESTBOOK_NAME5 = 'team4student_guestbook'

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME1):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME2):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME3):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME4):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)        

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME5):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)        

class Greeting(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Thesis(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    thesis_title = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)
    status = ndb.StringProperty(indexed=False)
    school_year = ndb.StringProperty(indexed=False)

class Adviser(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    first_name = ndb.StringProperty(indexed=False)
    last_name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    phone_number = ndb.StringProperty(indexed=False)
    department = ndb.StringProperty(indexed=False)

class Student(ndb.Model):
    first_name = ndb.StringProperty(indexed=False)
    last_name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    student_number = ndb.StringProperty(indexed=False)
    department = ndb.StringProperty(indexed=False)
    remarks = ndb.StringProperty(indexed=False)


class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values1 = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('homepage.html')
        self.response.write(template.render(template_values1))

class Guestbook(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params)) 

class Guestbook2(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME1)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/module-1/2?' + urllib.urlencode(query_params)) 

class Guestbook3(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME3)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/thesis/list?' + urllib.urlencode(query_params))   

class Guestbook4(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME4)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/adviser/list?' + urllib.urlencode(query_params))

class Guestbook5(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME4)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/student/list?' + urllib.urlencode(query_params))                 

class Guestbook1(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME2)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/module-1/1?' + urllib.urlencode(query_params)) 

class MemberOnePage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME2)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('member_onepage.html')
        self.response.write(template.render(template_values))

class MemberTwoPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME1)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }
        template = JINJA_ENVIRONMENT.get_template('member_twopage.html')
        self.response.write(template.render(template_values))

class ThesisSuccessHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('successthesis.html')
        self.response.write(template.render())

class AdviserSuccessHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('successadviser.html')
        self.response.write(template.render())             

class StudentSuccessHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('successstudent.html')
        self.response.write(template.render())

class StudentHomepageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('studenthome.html')
        self.response.write(template.render())        

class ThesisHomepageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('thesishome.html')
        self.response.write(template.render()) 

class AdviserHomepageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('adviserhome.html')
        self.response.write(template.render())         

class ThesisNewHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('thesisnew.html')
        self.response.write(template.render())

    def post(self):
        thesis = Thesis()
        thesis.thesis_title = self.request.get('thesis_title')
        thesis.description = self.request.get('description')
        thesis.school_year = self.request.get('school_year')
        thesis.status = self.request.get('status')
        thesis.put();
        self.redirect('/thesis/success')

class AdviserNewHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('advisernew.html')
        self.response.write(template.render())

    def post(self):
        adviser = Adviser()
        adviser.title = self.request.get('title')
        adviser.first_name = self.request.get('first_name')
        adviser.last_name = self.request.get('last_name')
        adviser.email = self.request.get('email')
        adviser.phone_number = self.request.get('phone_number')
        adviser.department = self.request.get('department')
        adviser.put();
        self.redirect('/adviser/success')

class StudentNewHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('studentnew.html')
        self.response.write(template.render())

    def post(self):
        student = Student()
        student.first_name = self.request.get('first_name')
        student.last_name = self.request.get('last_name')
        student.email = self.request.get('email')
        student.student_number = self.request.get('student_number')
        student.department = self.request.get('department')
        student.remarks = self.request.get('remarks')
        student.put();
        self.redirect('/student/success')

class ThesisListHandler(webapp2.RequestHandler):
    def get(self):
        thesis = Thesis.query().fetch();
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME3)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values ={
            'thesis_all': thesis,
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }
        
        template = JINJA_ENVIRONMENT.get_template('thesislist.html')
        self.response.write(template.render(template_values))


class AdviserListHandler(webapp2.RequestHandler):
    def get(self):
        adviser = Adviser.query().fetch();
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME4)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values ={
            'adviser_all': adviser,
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('adviserlist.html')
        self.response.write(template.render(template_values))

class StudentListHandler(webapp2.RequestHandler):
    def get(self):
        student = Student.query().fetch();
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME5)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values ={
            'student_all': student,
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('studentlist.html')
        self.response.write(template.render(template_values))

class ThesisViewHandler(webapp2.RequestHandler):
    def get(self, thesis_id):
        thesis_all=Thesis.query().fetch()
        template_values={
            'id': int(thesis_id),
            'thesis_all': thesis_all,
        }
        template = JINJA_ENVIRONMENT.get_template('viewthesis.html')
        self.response.write(template.render(template_values))

class AdviserViewHandler(webapp2.RequestHandler):
    def get(self, adviser_id):
        adviser_all=Adviser.query().fetch()
        template_values={
            'id': int(adviser_id),
            'adviser_all': adviser_all,
            
        }
        template = JINJA_ENVIRONMENT.get_template('viewadviser.html')
        self.response.write(template.render(template_values))

class StudentViewHandler(webapp2.RequestHandler):
    def get(self, student_id):
        student_all=Student.query().fetch()
        template_values={
            'id': int(student_id),
            'student_all': student_all,
        }
        template = JINJA_ENVIRONMENT.get_template('viewstudent.html')
        self.response.write(template.render(template_values))

class AdviserEditHandler(webapp2.RequestHandler):
    def get(self,adviser_id):
       
        adviserquery = Adviser.query().fetch()
        adviser_id = int(adviser_id)
 
        values = {
            'adviserquery': adviserquery,
            'id': adviser_id
        }
 
        template = JINJA_ENVIRONMENT.get_template('adviseredit.html')
        self.response.write(template.render(values))
 
 
    def post(self, adviser_id):
        adviser_id = int(adviser_id)
        adviser = Adviser.get_by_id(adviser_id)
        adviser.title = self.request.get('title')
        adviser.first_name = self.request.get('first_name')
        adviser.last_name = self.request.get('last_name')
        adviser.email = self.request.get('email')
        adviser.phone_number = self.request.get('phone_number')
        adviser.department = self.request.get('department')
        adviser.put()
        self.redirect('/adviser/success')

class StudentEditHandler(webapp2.RequestHandler):
    def get(self,student_id):
       
        studentquery = Student.query().fetch()
        student_id = int(student_id)
 
        values = {
            'studentquery': studentquery,
            'id': student_id
        }
 
        template = JINJA_ENVIRONMENT.get_template('studentedit.html')
        self.response.write(template.render(values))
 
 
    def post(self, student_id):
        student_id = int(student_id)
        student = Student.get_by_id(student_id)
        student.first_name = self.request.get('first_name')
        student.last_name = self.request.get('last_name')
        student.email = self.request.get('email')
        student.student_number = self.request.get('student_number')
        student.department = self.request.get('department')
        student.remarks = self.request.get('remarks')
        student.put()
        self.redirect('/student/success')

class ThesisEditHandler(webapp2.RequestHandler):
    def get(self,thesis_id):
       
        thesisquery = Thesis.query().fetch()
        thesis_id = int(thesis_id)
 
        values = {
            'thesisquery': thesisquery,
            'id': thesis_id
        }
 
        template = JINJA_ENVIRONMENT.get_template('thesisedit.html')
        self.response.write(template.render(values))
 
 
    def post(self, thesis_id):
        thesis_id = int(thesis_id)
        thesis = Thesis.get_by_id(thesis_id)
        thesis.thesis_title = self.request.get('thesis_title')
        thesis.description = self.request.get('description')
        thesis.school_year = self.request.get('school_year')
        thesis.status = self.request.get('status')
        thesis.put()
        self.redirect('/thesis/success')

application = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/sign', Guestbook),
        ('/sign1', Guestbook1),
        ('/sign2', Guestbook2),
        ('/sign3', Guestbook3),
        ('/sign4', Guestbook4),
        ('/sign5', Guestbook5),
        ('/module-1/1', MemberOnePage),
        ('/module-1/2', MemberTwoPage),

        ('/thesis/success', ThesisSuccessHandler),
        ('/thesis/new', ThesisNewHandler),
        ('/thesis/list', ThesisListHandler),
        ('/thesis/view/(\d+)', ThesisViewHandler),
        ('/thesis/homepage', ThesisHomepageHandler),
        ('/thesis/edit/(\d+)', ThesisEditHandler),

        ('/adviser/new', AdviserNewHandler),
        ('/adviser/list', AdviserListHandler),
        ('/adviser/view/(\d+)', AdviserViewHandler),
        ('/adviser/success', AdviserSuccessHandler),
        ('/adviser/homepage', AdviserHomepageHandler),
        ('/adviser/edit/(\d+)', AdviserEditHandler),

        ('/student/new', StudentNewHandler),
        ('/student/list', StudentListHandler),
        ('/student/view/(\d+)', StudentViewHandler),
        ('/student/success', StudentSuccessHandler),
        ('/student/homepage', StudentHomepageHandler),
        ('/student/edit/(\d+)', StudentEditHandler),
], debug=True)

#
