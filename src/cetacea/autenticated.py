from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated


class DRFAuthenticatedGraphQLView(GraphQLView):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((TokenAuthentication,))(view)
        view = api_view(['POST'])(view)
        return view