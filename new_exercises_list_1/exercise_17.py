from datetime import datetime
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def edit_profile_view(request):
    if not request.user or not request.user.is_authenticated:
        return HttpResponseForbidden

    user = request.user
    #xxxxx
    # user.updated_at = datetime.now()
    user.updated_at = timezone.now() #insted datetim.now()
    user.save()



"""Use django timezone util"""
