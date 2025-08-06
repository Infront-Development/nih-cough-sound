from rest_framework import authentication, status

from api.models import APIToken


class AWSIntegationAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        authorization = request.META.get("HTTP_AUTHORIZATION")
        if authorization is None:
            raise authentication.exceptions.AuthenticationFailed(
                detail="No Bearer Token provided", code=status.HTTP_401_UNAUTHORIZED
            )
        if "Bearer" in authorization:
            token = authorization.replace("Bearer", "")
            token = token.strip()

            # validated = validate(token)

            api_token: APIToken = APIToken.validate_token(token)
            if api_token is not None:
                return None, {"token": api_token.token, "owner": api_token.owner}

            else:
                raise authentication.exceptions.NotAuthenticated(
                    detail="Invalid Token", code=status.HTTP_401_UNAUTHORIZED
                )
        else:
            raise authentication.exceptions.NotAuthenticated(
                detail="No Bearer Token provided", code=status.HTTP_401_UNAUTHORIZED
            )
