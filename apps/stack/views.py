from django.shortcuts import render
from django.utils.simplejson import dumps
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from models import Project,Stack, Node, License, LINK_CHOICES 

def home(request, template='stack/home.html'):
    """default home request"""

    return render(request, template, {})

def explore(request, template='stack/explore.html'):
    return render(request, template, {'page': 'explore'})

def create(request, template='stack/create.html'):
    stack = Stack.objects.create(name='Your Stack')
    project = Project.objects.create(name='Your project', is_private=True, 
            is_stack_project=True)
    public_projects = Project.objects.filter(is_private=False)\
            .filter(is_stack_project=False)

    root = Node.add_root(project=project, stack=stack)
    root_dump = Node.dump_bulk(parent=root)
    nodes_dump = dumps(root_dump, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', public_projects)
    projects = dumps(temp_output, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', [project])
    project_json = dumps(temp_output, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', [stack])
    stack_json = dumps(temp_output, cls=DjangoJSONEncoder)

    return render(request, template, {
        'page': 'create', 
        'stack': stack_json,
        'project': project_json,
        'root': root,
        'nodes': root_dump,
        'nodes_dump': nodes_dump,
        'projects': projects,
        'projects_raw': public_projects,
        'link_types': LINK_CHOICES,
        'licenses': License.objects.all()
    })

def edit(request, stack_id, template='stack/edit.html'):
    stack = Stack.objects.get(pk=stack_id)
    root = Node.objects.get(stack=stack, depth=1)
    project = root.project

    public_projects = Project.objects.all()
    root_dump = Node.dump_bulk(parent=root)
    nodes_dump = dumps(root_dump, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', public_projects)
    projects = dumps(temp_output, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', [project])
    project_json = dumps(temp_output, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', [stack])
    stack_json = dumps(temp_output, cls=DjangoJSONEncoder)

    return render(request, template, {
        'page': 'edit', 
        'stack': stack_json,
        'stack_raw': stack,
        'project': project_json,
        'root': root,
        'nodes': root_dump,
        'nodes_dump': nodes_dump,
        'projects': projects,
        'projects_raw': public_projects,
        'link_types': LINK_CHOICES,
        'licenses': License.objects.all()
    })

def share(request, stack_id, template='stack/share.html'):
    stack = Stack.objects.get(pk=stack_id)
    root = Node.objects.get(stack=stack, depth=1)
    project = root.project

    public_projects = Project.objects.all()
    root_dump = Node.dump_bulk(parent=root)
    nodes_dump = dumps(root_dump, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', public_projects)
    projects = dumps(temp_output, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', [project])
    project_json = dumps(temp_output, cls=DjangoJSONEncoder)

    temp_output = serializers.serialize('python', [stack])
    stack_json = dumps(temp_output, cls=DjangoJSONEncoder)

    return render(request, template, {
        'page': 'share', 
        'stack': stack_json,
        'stack_raw': stack,
        'project': project_json,
        'root': root,
        'nodes': root_dump,
        'nodes_dump': nodes_dump,
        'projects': projects,
        'projects_raw': public_projects,
        'link_types': LINK_CHOICES,
        'licenses': License.objects.all()
    })

def my_stacks(request, template='stack/my_stacks.html'):
    return render(request, template, {'page': 'my_stacks'})

