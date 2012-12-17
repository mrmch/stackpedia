from django.conf.urls import patterns, url, include

ajax_patterns = patterns('apps.stack.ajax',
    url(r'^node/save$', 'save_node', name='ajax-save-node'),
    url(r'^node$', 'get_node', name='ajax-get-node'),
    url(r'^project/save$', 'save_project', name='ajax-save-project'),
    url(r'^project$', 'get_project', name='ajax-get-project'),
    url(r'^stack/create$', 'create_stack', name='ajax-create-stack'),
    url(r'^stack/name$', 'save_stack_name', name='ajax-save-stack-name'),
    url(r'^stack/(?P<stack_id>\d+)/nodes$', 'get_stack_nodes', name='ajax-get-stack-nodes'),
    url(r'^stack$', 'get_stack', name='ajax-get-stack'),
)

urlpatterns = patterns('apps.stack.views',
    url(r'^create$', 'create', name='create'),
    url(r'^edit/(?P<stack_id>\d+)$', 'edit', name='edit-stack'),
    url(r'^explore$', 'explore', name='explore'),
    url(r'^my_stacks$', 'my_stacks', name='my-stacks'),
    url(r'^(?P<stack_id>\d+)$', 'share', name='share-stack'),
    url(r'^$', 'home', name='home'),
    (r'^ajax/', include(ajax_patterns)),
)

