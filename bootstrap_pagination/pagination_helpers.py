from django.conf import settings
from django.core.paginator import Paginator

class PaginationContextMixin(object):
    
    def update_pagination_context(self,context):
        if len(self.object_list) > settings.MAX_PAGINATION_ITEMS_PER_PAGE:
            context['paginate'] = True
            p = Paginator(self.object_list,settings.MAX_PAGINATION_ITEMS_PER_PAGE)
            page = p.page(int(self.request.GET.get('page',1)))
            context['page'] = page
            context['pages'] = p.page_range
            context['object_list'] = page.object_list
        
        return