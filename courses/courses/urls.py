from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

app_name = "courses"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
]
