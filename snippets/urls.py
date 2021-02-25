from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('snippets/python/', views.language, name='language'),
    path('snippets/user/juancito/', views.user_snippets, name='user_snippets'),
    path('snippets/snippet/<int:pk>', views.SnippetDetail.as_view(), name='snippet'),
    path('snippets/add/', views.SnippetCreation.as_view(), name='snippet_add'),
    path('snippets/edit/<int:pk>', views.SnippetEdit.as_view(), name='snippet_edit'),
    path('snippets/delete/<int:pk>', views.SnippetDelete.as_view(), name='snippet_delete'),
]
