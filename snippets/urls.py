from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('snippets/<slug>', views.LanguageListView.as_view(), name='language'),
    path('snippets/user/juancito/', views.user_snippets, name='user_snippets'),
    path('snippets/snippet/<int:pk>', views.SnippetDetail.as_view(), name='snippet'),
    path('snippets/add/', views.SnippetCreation.as_view(), name='snippet_add'),
    path('snippets/edit/<int:pk>', views.SnippetEdit.as_view(), name='snippet_edit'),
    path('snippets/delete/<int:pk>', views.SnippetDelete.as_view(), name='snippet_delete'),
]
