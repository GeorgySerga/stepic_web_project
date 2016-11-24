from django.conf.urls import url
from qa.views import test, question_details, question_list

urlpatterns = [
    url(r'^$', question_list),
    url(r'^login/.*$', test, name='login'),
    url(r'^signup/.*', test, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', question_details, name='question_details'),
    url(r'^ask/.*', test, name='ask'),
    url(r'^popular/$', question_list, name='popular'),
    url(r'^new/$', test, name='new'),
]
