# Django-Utils

Some utils I find useful in my projects.    
See the readme files or the code comments

###Bootstrap pagination

Add bootstrap pagination buttons to list views

### Model to Html

A View mixin to quickly add model fields with labels to a django template. Similar to a form "label":"value" output, but just text HTML without the input fields.


### Email Auth
Authentication backend with email & password

### Middleware

* AuthorizedViewsMiddleware: Make all site views login required by default, useful for web applications
* LogExceptionsMiddleware: logs unhandled exceptions
* UserCachedAttributeMiddleware: adds cached user attributes to request.user

### Template Tags

A few custom filters to format values in templates
