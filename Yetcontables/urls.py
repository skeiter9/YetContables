from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  	url(r'^$', 'principal.views.inicio'),
    url(r'^login/', 'principal.views.inicio'),
    url(r'^home/', 'principal.views.home'),
    url(r'^logout/', 'principal.views.cerrar'),
    url(r'^usuarios/', 'principal.views.usuarios'),
    url(r'^upload-user/', 'principal.views.user_profile'),
    url(r'^plan-contable/', 'principal.views.plan'),
    url(r'^periodos/', 'principal.views.periodo'),
    url(r'^transacciones/', 'principal.views.transacciones'),
    url(r'^libro-diario/', 'principal.views.libroDiario'),
    url(r'^libro-mayor/', 'principal.views.libroMayor'),
    url(r'^cierre-y-apertura/', 'principal.views.cierreYApertura'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
