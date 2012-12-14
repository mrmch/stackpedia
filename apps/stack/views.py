from django.shortcuts import render
from django.utils.simplejson import dumps
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from models import Project,Stack, Node

def home(request, template='stack/home.html'):
    """default home request"""

    return render(request, template, {})

def explore(request, template='stack/explore.html'):
    return render(request, template, {'page': 'explore'})

def create(request, template='stack/create.html'):
    stack = Stack.objects.create(name='Your Stack')
    project = Project.objects.create(name='Your project', is_private=True)

    root = Node.add_root(project=project, stack=stack)
    root_dump = Node.dump_bulk(parent=root)

    #temp_output = serializers.serialize('python', root_dump)
    #output = dumps(temp_output, cls=DjangoJSONEncoder)
    output = dumps(root_dump, cls=DjangoJSONEncoder)

    return render(request, template, {
        'page': 'create', 
        'stack': stack,
        'project': project,
        'root': root,
        'nodes': root_dump,
        'nodes_dump': output
    })

def edit(request, template='stack/edit.html'):
    return render(request, template, {'page': 'edit'})

def my_stacks(request, template='stack/my_stacks.html'):
    return render(request, template, {'page': 'my_stacks'})

