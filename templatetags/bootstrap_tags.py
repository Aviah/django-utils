from django import template
from django.contrib.messages import constants
Dmsg = {
    constants.DEBUG:"bg-info",
    constants.INFO:"bg-primary",
    constants.SUCCESS:"bg-success",
    constants.WARNING:"bg-warning",
    constants.ERROR:"bg-danger"
}
register = template.Library()

@register.filter
def msg_class(value):
    """simple conversion of a django message.level to a bootstrap alert class.    
    The template can look like:
    
   {% if messages %}
        <ul class="messages">
            {% for message in messages %}
                  <li{% if message.tags %} class="{{msg.level|msg_class"{% endif %}>{{ message }}</li>
            {% endfor %}
       </ul>
   {% endif %}
   """
    
    return Dmsg.get(value,"")