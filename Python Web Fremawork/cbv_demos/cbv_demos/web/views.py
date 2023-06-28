from django.shortcuts import render
from django.views import generic as views

from cbv_demos.web.models import Article

# View in Django
# 1. The `view` must be `callable`
# 2. Returns `HttpResponse` object

'''
    if request.method == 'POST':
        ...
    else:
        ...

    ...
    form = ArticlesForm()

    ...build `context`
    ...
    '''


def list_articles(request):
    context = {
        'articles': Article.objects.all(),
    }

    return render(request, 'articles/list.html', context)


# views.CreateView
# views.ListView
# views.UpdateView
# views.DeleteView
# views.DetailView

# class AdminOnlyView:
#     def is_admin(self):
#         pass


class BaseView:
    def get(self, request):
        pass

    def post(self, request):
        pass

    @classmethod
    def as_view(cls):
        self = cls()

        def view(request):
            if request.method == 'GET':
                return self.get(request)
            else:
                return self.post(request)

        return view


# class ArticlesListView(views.View):
#     def get(self, request):
#         # def get_context_data(....):...
#         context = {
#             'articles': Article.objects.all(),
#         }
#         # def render_to_response(...):...
#         return render(request, 'articles/list.html', context)


class ArticlesListView(views.TemplateView):
    template_name = 'articles/list.html'

    # static data
    # extra_context = {
    #     'articles': Article.objects.all(),
    # }

    # dynamic data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


print(ArticlesListView.as_view())
