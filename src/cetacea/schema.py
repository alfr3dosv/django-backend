import graphene

import users.schema
import projects.schema
import courses.schema

class Query(users.schema.Query,
            projects.schema.Query,
            courses.schema.Query,
            graphene.ObjectType):
    pass

# class Mutation(users.schema.Mutation, projects.schema.Mutation, graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     social_auth = graphql_social_auth.SocialAuthJWT.Field()
#     refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query)