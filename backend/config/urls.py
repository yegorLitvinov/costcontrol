from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('apps.accounts.urls', namespace='accounts')),
    url(r'^api/costcontrol/', include('apps.costcontrol.urls', namespace='costcontrol')),
    url(r'^api/todo/', include('apps.todo.urls', namespace='todo')),
]
