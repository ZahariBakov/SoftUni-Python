from django.urls import path

from cbv_demos.web.views import list_articles, ArticlesListView, RedirectToArticlesView

urlpatterns = (
    path('', list_articles, name='list articles'),
    path('cbv/', ArticlesListView.as_view(), name='list articles cbv'),
    path('cbv/<int:pk>/', ArticlesListView.as_view(), name='list articles cbv'),
    path('redirect-to-articles/', RedirectToArticlesView.as_view(), name='redirect to articles'),
)
