import debug_toolbar
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "We Love Python "
admin.site.index_title = "tarek administrstion "

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("__debug__/", include(debug_toolbar.urls)),
]
