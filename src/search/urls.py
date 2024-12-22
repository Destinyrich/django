from django.urls import re_path  # Use re_path for regular expressions
from .views import SearchProductView

app_name = 'search'
urlpatterns = [
    re_path(r'^$', SearchProductView.as_view(), name='query'),  # Replace `url` with `re_path`
]
