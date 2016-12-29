from django.conf.urls import include, url
from dashing.utils import router

from dashing.setting import DASHBOARD_NAME
from .views import MultipleDashboards

urlpatterns = [
    url(r'^'+DASHBOARD_NAME+'/', include(router.urls)),
    url(r'^multiple_dashboards/$', MultipleDashboards.as_view()),
]
