"""cetacea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.authtoken.views import obtain_auth_token

from . autenticated import DRFAuthenticatedGraphQLView

urlpatterns = [
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('', csrf_exempt(DRFAuthenticatedGraphQLView.as_view())),
    path('admin/', admin.site.urls),
    path('api/token', obtain_auth_token, name='api-token'), # Token <= login using username and password
    path('api/login/', include('rest_social_auth.urls_token')), # Token <= login using social auth
    path('api/social/', include('social_django.urls', namespace='social')),
]
