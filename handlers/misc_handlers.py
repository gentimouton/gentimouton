from handlers.base import BaseHandler

     
class HomeHandler(BaseHandler):
    def get(self):
        context = {}
        self.render_response('home.html', **context)
class GurHandler(BaseHandler):
    def get(self):
        context = {}
        self.render_response('gur.html', **context)
class ScalingHandler(BaseHandler):
    def get(self):
        context = {}
        self.render_response('scaling.html', **context)

class SearchHandler(BaseHandler):
    def get(self):
        query = self.request.get('q')
        context = {'query': query}
        self.render_response('search.html', **context)
        
        