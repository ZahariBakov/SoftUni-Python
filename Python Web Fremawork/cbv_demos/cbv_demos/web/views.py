from django.shortcuts import render
from django.urls import reverse_lazy
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
#     def get(self, request, *args, **kwargs):
#         # def get_context_data(....):...
#         context = {
#             'articles': Article.objects.all(),
#         }
#         # def render_to_response(...):...
#         return render(request, 'articles/list.html', context)


# class ArticlesListView(views.TemplateView):
#     template_name = 'articles/list.html'
#
#     # static data
#     # extra_context = {
#     #     'articles': Article.objects.all(),
#     # }
#
#     # dynamic data
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context


class ArticlesListView(views.ListView):
    template_name = 'articles/list.html'
    model = Article
    # In this view by default:
    # content['object_list'] = Article.object.all()
    # 'object_list' is default name
    context_object_name = 'articles' # Use default - `object_list` is good enough.
    paginate_by = 15


class RedirectToArticlesView(views.RedirectView):
    url = reverse_lazy('list articles cbv')


print(ArticlesListView.as_view())
