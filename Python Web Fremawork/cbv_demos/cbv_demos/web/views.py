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

    return render(request, 'article/list.html', context)


# views.CreateView
# views.ListView
# views.UpdateView
# views.DeleteView
# views.DetailView

# class AdminOnlyView:
#     def is_admin(self):
#         pass


class ArticlesListView(views.View):
    # def __pos__(self):
    #     pass

    def get(self):
        context = {
            'articles': Article.objects.all(),
        }

        return render(self.request, 'article/list.html', context)
