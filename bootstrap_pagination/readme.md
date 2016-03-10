# Bootstrap Pagination


## Overview

A simple util that can add bootstrap pagination buttons to any list view.
The pagination will work with a GET "page" argument:

	http:/www.example.com/products/?page=1
	
The pagination includes 3 files:

* pagination_tags.py: a template tag
* pagination.html: the html snippet to show the pagination buttons
* pagination_helpers.py: a view mixin that calculate the pages
	
	
## Install


To use the pagination in your project you will need the bootstrap, see https://getbootstrap.com/components/#pagination


1. Add the **pagination_tags.py** file to one of the application that are listed in INSTALLED_APPS. The file should be in the application `templatetags` directory:

		myapp/
			migrations
				0001_initial.py
				...
			templatetags
				pagination_tags.py
			admin.py
			models.py
			tests.py
			urls.py
			views.py
		
2. Add the **pagination.html** tag to your project main templates directory, where the templates are available to all views, something like:

		mysite/
			myapp1/
			myapp2/
			templates/
				base.html
				pagination.html
			settings.py
			...
					
3. Add the **pagination_helpers.py** to the project utils, or the project main directory, so you can import the pagination mixin, something like:

		from pagination_helpers import PaginationContextMixin
		
4. Add a MAX_PAGINATION_ITEMS_PER_PAGE key to your main settings.py:

		MAX_PAGINATION_ITEMS_PER_PAGE = 10
	
	Is a maximum 10 items per page.


## Use Pagination


### Templates

In any template that requires pagination, add the following code where the pagination buttons should show:

 	{% if paginate %}   
        {% include "templates/pagination.html" %}        
    {% endif %}
    
*Note: if you use pagination a lot, add this to your base template*
    
### Views

In a the list view:

	from django.views import generic
	from pagination_helpers import PaginationContextMixin
		
	class MyListView(generic.ListView,PaginationContextMixin):
		...
				
		def get_context_data(self,*args,**kwargs):
			context = super(MyListView,self).get_context_data(*args,**kwargs)
			self.update_pagination_context(context)
			return context
		
	
That's it. The list view page will show pagination buttons when the object_list has objects for more than one page.
	



	
	
		