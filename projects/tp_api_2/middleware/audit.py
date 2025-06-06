from django.utils.deprecation import MiddlewareMixin
from ..models.log import ResourceLog
from .token import check_token

class ResourceAccessMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Ignore Django admin, static files, etc.
        if request.path.startswith("/admin") or request.path.startswith("/static"):
            return None

        user, error = check_token(request)
        if error is None and user:
            ResourceLog.objects.create(
                user=user,
                resource=request.path
            )
        return None
