# Some useful simple tamplate tags.

See comments how to use the tags in django templates.

To add the tags to the project:

1. Add this templatetags dir to any application that is listed in INSTALLED_APPS
2. In every template that uses at least one of the tags add at the beginning of the template a load for the template tags file, like:

                {% load value_format_tags %}
                
                
*Note: if you already have templatetags directory in another app, you can also just drop the file in this directory*