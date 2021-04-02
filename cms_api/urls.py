from . import views
from django.urls import re_path

urlpatterns = [

    # User Registration And Login
    re_path(r'^register/', views.UserRegistration.as_view(), name='user-registration'),  # POST
    re_path(r'^login/', views.UserLogin.as_view(), name='login'),  # POST

    # Content CRUD Opration
    re_path(r'^create-content/', views.CreateContent.as_view(), name='create-content'),  # POST
    re_path(r'^retrieve-content/(?P<pk>\d+)/', views.RetrieveContent.as_view(), name='retrieve-content'),  # GET
    re_path(r'^update-content/(?P<pk>\d+)/', views.UpdateContent.as_view(), name='update-content'),  # POST
    re_path(r'^delete-content/(?P<pk>\d+)/', views.DeleteContent.as_view(), name='delete-content'),  # GET
    re_path(r'^all-content/', views.GetAllContentAPI.as_view(), name='GetAllContentAPI'),  # GET

    # Searching Content # pass keyword in ?search={{search_keyword}}
    re_path(r'^search-content/', views.SearchContent.as_view()),  # GET

    re_path(r'^test/', views.Test.as_view()),  # GET
]
