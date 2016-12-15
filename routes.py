import webapp2

from handlers.misc_handlers import HomeHandler, SearchHandler, GurHandler, ScalingHandler



# See http://webapp-improved.appspot.com/guide/routing.html#simple-routes
routes = [webapp2.Route(r'/', handler=HomeHandler, name='home'),
          webapp2.Route(r'/gur', handler=GurHandler, name='gur'),
          webapp2.Route(r'/scaling', handler=ScalingHandler, name='scaling'),
          webapp2.Route(r'/search', handler=SearchHandler, name='search'),
    ]
