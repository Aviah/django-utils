import logging
import sys
from django.conf import settings
from django.http import Http404,HttpResponseRedirect
from django.core.cache import cache
from django.core.urlresolvers import reverse

class AuthorizedViewsMiddleware(object):

    """Handle all views as login required, unless the view is explictly listed as a public view.
    When the website is  a web application, most of the views require login.
    It's easier to default all views to login, without adding login_required or LoginRequiredMixin to each view
    To use this middleware, add a PUBLIC_VIEWS_MODULES to your settings
    with the full path to the public view. Something like:
    PUBLIC_VIEWS_MODULES = ['mysite.home.HomePageView','mysite.info.AboutUsView']"""
    
    def process_view(self,request,view_func,*arg,**kwargs):
        
        if request.path_info.split('/')[1] == settings.ADMIN_URL:
            return None
        
        if view_func.__module__  in settings.PUBLIC_VIEWS_MODULES:
            return None
        
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home_page'))


class LogExceptionsMiddleware(object):
    """Logs any unhandled exceptions, ignores Http404"""

    def process_exception(self,request, exception):
        
        if isinstance(exception, Http404):
            
            return

        logging.getLogger('main').critical(exception,exc_info=sys.exc_info())
        
        return
    
class UserAttributeMiddleware(object):
    """Adds cached user attributes to the request.user object, with a cached dictionary
    then in the code use: request.user.foo
    useful for attributes that are used a lot, but don't change a lot
    """
    
    def process_view(self,request,view_func,*args,**kwargs):
 
        if request.user.is_authenticated():
            
            # check if cache is valid
            D = cache.get("user_%s"%request.user.id) 
            if D!=None and D.has_key['foo']: #and cache is valid
                foo = D['foo']
            else:
                foo = 'baz' # get the foo value from db or otherwise here
                cahe.set("user_%s"%request.user.id,{'foo','baz'})
              
            request.user.foo = foo           
            return None
                

    
    