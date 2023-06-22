"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from dj_rest_auth.registration.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls')),
    path('dj_rest_auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', RegisterView.as_view(), name=('rest_register')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
