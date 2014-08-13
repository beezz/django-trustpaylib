from django.conf.urls import patterns, include, url

from djtrustpaylib.views import TransactionView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TransactionView.as_view(template_name="home.html"), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
