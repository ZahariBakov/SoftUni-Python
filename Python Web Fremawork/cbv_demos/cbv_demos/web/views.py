from django.forms import modelform_factory
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
    context_object_name = 'articles'  # Use default - `object_list` is good enough.
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    # Article.objects.filter(name__icontains=search)


class ArticleDetailView(views.DetailView):
    model = Article
    template_name = 'articles/detail.html'


# def ArticleForm(forms.ModelForm):
#     pass

# Forms:
# 1. Auto created (default)
# 2. `form_class` - return class
# 3. `get_form_class` - return class
# 4. `get_form` - return instance


class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


class ArticlesCreateView(DisabledFormFieldsMixin, views.CreateView):
    model = Article
    template_name = 'articles/create.html'
    fields = '__all__'
    success_url = reverse_lazy('list articles cbv')

    disabled_fields = ('title',)  # Not built-in

    # form_class = ArticleForm

    # def get_form_class(self):
    #     pass


class ArticleUpdateView(views.UpdateView):
    pass


class ArticleDeleteView(DisabledFormFieldsMixin, views.DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    form_class = modelform_factory(
        Article,
        fields=('title', 'content')
    )
    disabled_fields = ('title', 'content')


class RedirectToArticlesView(views.RedirectView):
    url = reverse_lazy('list articles cbv')


print(ArticlesListView.as_view())
