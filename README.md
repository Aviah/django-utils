# Django-Utils

**Some utils that I find useful in my projects**    

See the readme files and the code comments for each util.

###Bootstrap pagination

Add bootstrap pagination buttons to ListViews

### Model to Html

A View mixin to quickly add model fields with labels to a django template. 

The output is similar to a form "label:value", but here it's just text HTML without the input fields.


### Email Auth
Authentication backend with email & password

### Middleware

* AuthorizedViewsMiddleware: Make all the site views login-required by default. Useful for web applications
* LogExceptionsMiddleware: logs unhandled exceptions
* UserCachedAttributeMiddleware: adds cached user attributes to request.user

### Template Tags
Custom filters to format template values
