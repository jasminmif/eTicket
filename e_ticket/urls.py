from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from ticket import views as TCK

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'e_ticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TCK.main_view),
    url(r'^/ticket/scan_ticket/$', TCK.scan_ticket),
    url(r'^/ticket/add_ticket/$', TCK.add_ticket_uuid),
    url(r'^/ticket/generate_ticket_images/$', TCK.generate_ticket_images),
)
