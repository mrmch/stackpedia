from django.http import HttpResponse
from django.utils.simplejson import dumps
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from models import Project, License, Stack, Node
        

def ajax_success(request, msg=None, data=None, model=False):
    resp = {
        'success': True,
        'message': msg,
        'data': data
    }

    if model:
        data = serializers.serialize("json", data)
        return HttpResponse(data)

    return HttpResponse(dumps(resp, cls=DjangoJSONEncoder))

def ajax_failure(request, msg=None, data=None, model=False):
    resp = {
        'success': False,
        'message': msg,
        'data': data
    }

    if model:
        data = serializers.serialize("json", data)
        return HttpResponse(data)
    return HttpResponse(dumps(resp, cls=DjangoJSONEncoder))
    
def get_project(request):
    try:
        project_id = request.GET.get('id')
        project = Project.objects.get(pk=project_id)
    except Exception as e:
        return ajax_failure(request, msg=str(e))

    return ajax_success(request, data=project, model=True)

def get_stack(request, stack_id):
    try:
        stack_id = request.GET.get('id')
        stack = Stack.objects.get(pk=stack_id)
    except Exception as e:
        return ajax_failure(request, msg=str(e))

    return ajax_success(request, data=stack, model=True)

def add_dep(request):
    try:
        parent = Node.objects.get(pk=request.GET.get('parent_id'))
        stack = Stack.objects.get(pk=request.GET.get('stack_id'))
        project = Project.objects.get(pk=request.GET.get('project_id'))
        dep = parent.add_child(stack=stack, project=project)
    except Exception as e:
        return ajax_failure(request, msg=str(e))

    return ajax_success(request, data=dep, model=True)

def save_stack_name(request):
    try:
        stack = Stack.objects.get(pk=request.GET.get('stack_id'))
        name = request.GET.get('name')
        stack.name = name
        stack.save()
    except Exception as e:
        return ajax_failure(request, msg=str(e))

    return ajax_success(request)

def save_project(request):
    try:
        project = Project.objects.get(pk=request.GET.get('project_id'))
    except:
        project = Project.objects.create()

    try:
        project.name = request.GET.get('name')
        project.github = request.GET.get('github')
        project.logo = request.GET.get('logo')
        project.save()
    except Exception as e:
        return ajax_failure(request, msg=str(e))

    return ajax_success(request, data=[project], model=True)

def save_node(request):
    try:
        project = Project.objects.get(pk=request.GET.get('project_id'))
        stack = Stack.objects.get(pk=request.GET.get('stack_id'))
        node = Node.objects.get(pk=request.GET.get('node_id'))
    except:
        try:
           root = Node.objects.get(pk=request.GET.get('root_id'))
           node = root.add_child(project=project, stack=stack)
        except Exception as e:
            return ajax_failure(request, msg=str(e))

    try:
        node.project = project
        node.stack = stack
        node.link_type = request.GET.get('link_type')
        node.save()
    except Exception as e:
        return ajax_failure(request, msg=str(e))

    return ajax_success(request, data=[node], model=True)

