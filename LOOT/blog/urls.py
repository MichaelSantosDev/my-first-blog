from django.urls import path
from .views import post_list
from .views import post_detail
from .views import post_new
from .views import post_edit
from .views import post_draft_list
from .views import post_publish
from .views import post_delete
from .views import add_comment_to_post
from .views import comment_approve
from .views import comment_delete




urlpatterns = [
    path('', post_list, name="post_list"),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('post/(<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment_delete'),

]