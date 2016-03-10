import datetime
from django.utils.safestring import mark_safe

class ModelToHtml(object):
    """ html output for fields by verbose name, in the order provided"""
    
    simple_row_template =  "{row_start} {label} {divider} {value} {row_end} \n"
    obj = None
    
    def __init__(self,model,fields,styled_row_element,styled_row_template,date_format,styled_divider):
        
        self.model = model
        self.Lfields = fields
        self.styled_row_element = styled_row_element
        self.styled_row_template = styled_row_template
        self.date_format = date_format
        self.style_divider = styled_divider
        s = set(model._meta.get_all_field_names())
        assert set(fields).issubset(s)
             
    def _row(self,row_template,field_name,value,row_start,row_end,divider):
        
        label = self.model._meta.get_field(field_name).verbose_name
        return row_template.format(row_start=row_start,label=label,row_end=row_end,divider=divider,value=value)
        
    def _output_html(self,tag,row_template,divider="  "):
        
        html_output = ""
        for field_name in self.Lfields:
            value = getattr(self.obj,field_name)
            if isinstance(value,datetime.datetime):
                value = value.strftime(self.date_format)
            else:
                value = str(value)
            
            html_output = html_output + self._row(row_template,field_name,value,"<%s>"%tag,"</%s>"%tag,divider)
            
        return mark_safe(html_output)
    
    def as_p(self):
        
        return self._output_html("p",self.simple_row_template)
    
    def styled(self):
        
        return self._output_html(self.styled_row_element,self.styled_row_template,self.style_divider)
    
    
class ModelToHtmlMixin(object):
    
    model_to_html_fields = None
    model_to_html = None
    styled_row_element = "h4"
    date_format = "%Y-%m-%d %H:%M" # edit to any python strftime like "%b. %d, %Y"
    styled_divider = ":"
    
    # edit the span class for the label and the value
    styled_row_template = '{row_start}<span class="">{label}</span>{divider} <span class="">{value}</span> {row_end} \n'    
    
    def __init__(self,*args,**kwargs):
        
        model = self.model_to_html if self.model_to_html != None else self.model
        self.model_html = ModelToHtml(
            model=model, 
            fields=self.model_to_html_fields,
            styled_row_element=self.styled_row_element,
            date_format=self.date_format,
            styled_divider=self.styled_divider
        )
    
    def get_context_data(self,*args,**kwargs):
        
        context = super(ModelToHtmlMixin,self).get_context_data(*args,**kwargs)
        self.model_html.obj = self.object
        context ['model_html'] = self.model_html
        return context
        
            
            
            
        
        
            
        
        
        
        
        
        