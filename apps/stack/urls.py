from django.conf.urls import patterns, url, include

ajax_patterns = patterns('apps.stack.ajax',
    url(r'^project$', 'get_project', name='ajax-get-project'),
    url(r'^stack/name$', 'save_stack_name', name='ajax-save-stack-name'),
    url(r'^stack$', 'get_stack', name='ajax-get-stack'),
)

urlpatterns = patterns('apps.stack.views',
    url(r'^create$', 'create', name='create'),
    url(r'^edit$', 'edit', name='edit'),
    url(r'^explore$', 'explore', name='explore'),
    url(r'^my_stacks$', 'my_stacks', name='my-stacks'),
    url(r'^$', 'home', name='home'),
    (r'^ajax/', include(ajax_patterns)),
)

