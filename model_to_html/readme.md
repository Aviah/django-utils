# ModelToHtml

A View mixin to quickly add model fields with labels to a django template (similar to a form "label":"value" output, but just text HTML without the input fields)

Useful for:

1. Details views
2. Form views where the form edits only a few fields, yet you want to just show other fields
3. Delete views, to show the details of the object to be deleted.


## How To


In the view file:

        from django.views import generic
        from model_to_html import ModelToHtmlMixin
        from myapp.models import Product
        ...
        
        class MyDetailView(ModelToHtmlMixin,generic.DetailView):
        
                template_name = "my_proudct_template.html"
                model = Product
                model_to_html_fields = ['product_name','category','price','notes']
                
                
Then in the `my_proudct_template.html` content:

        {{ model_html.as_p }}
        
        
That's it. The product page will show something like:

        Product Name: The django framework
        Category: Tech
        Price: 10
        Notes: A great book
        
The model_to_html uses the field's verbose_name as a label. If no verbose_name is provided, django uses the field's name.
Verbose names are defined in the model.

## Style

To style the rows, use:

        {{ model_html.styled }}
        
The styled row uses 4 of the Mixin attributes that you can change:
*  styled_row_element: the default is "h4"
*  styled_divider: the default is ":"
*  styled_row_template: a template row that uses {row_start}{label}{divider}{value}{row_end}
*  date_format: a python strftime, the default is  "%Y-%m-%d %H:%M", which formats the datetime fields.
  
 To create a styled html:
 
        class MyDetailView(ModelToHtmlMixin,generic.DetailView):

                template_name = "my_proudct_template.html"
                model = Product
                model_to_html_fields = ['product_name','category','price','notes']
                styled_row_element = "h3"
                styled_divider = "-"
                styled_row_template = "{row_start} <span class="label-info"> {label} </span> {divider} {value} {row_end}"
                
And the html will be something like:

        <h3> <span class="label-info"> Product Name </span> - The django framework </h3>
 
### Using the same style in many templates
If you use the same style throughout the project, then edit the style attributes in the ModelToHtmlMixin class inplace, then just use `{{ model_html.styled }}` in the templates.

## Install
Place the model_to_html.py file in any project directory, such as utils or the main directory, where you can import the mixin to the views:

        from model_to_html import ModelToHtmlMixin
        

 




                
                
