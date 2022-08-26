from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogsListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blog-detail'),
    path('blog/create', views.BlogCreate.as_view(), name='blog-create'),
    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogDelete.as_view(), name='blog-delete'),
    path('myblogs/', views.myblogs_list, name='myblog_list'),
    path('blog/<int:pk>/comment', views.CommentCreate.as_view(), name='comment-create'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('blogger/<int:pk>', views.BloggerDetail.as_view(), name='profile'),
    path('blogger/edit', views.ProfileUpdate.as_view(), name='profile-edit'),
]
