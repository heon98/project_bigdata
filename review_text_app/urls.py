from django.urls import path

from review_text_app.views import hello_world

app_name = "review_text_app"

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world')
]