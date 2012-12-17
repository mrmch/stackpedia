from django.db import models
from django.contrib.auth.models import User
from django.utils.simplejson import dumps
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from treebeard.mp_tree import MP_Node

LINK_CHOICES = (
    ('dy', 'Dynamic Linking'),
    ('st', 'Static Linking'),
    ('ot', 'Other')
)

class License(models.Model):
    class Meta:
        ordering = ['odc_id',]

    odc_id = models.CharField(max_length=300)
    domain_content = models.CharField(max_length=300)
    domain_data = models.CharField(max_length=300)
    domain_software = models.CharField(max_length=300)
    is_okd_compliant = models.BooleanField(default=False)
    is_osi_compliant = models.BooleanField(default=False)
    status = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

class Contributor(models.Model):
    login = models.CharField(max_length=255)
    github_id = models.CharField(max_length=255)
    avatar_url = models.URLField(max_length=500)

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    github = models.URLField(max_length=255, null=True, blank=True)
    logo = models.URLField(max_length=255, null=True, blank=True)
    license = models.ManyToManyField(License)
    is_private = models.BooleanField(default=False)
    is_stack_project = models.BooleanField(default=False)
    contributors = models.ManyToManyField(Contributor, related_name='projects')

    def __unicode__(self):
        return self.name

    def get_contributors(self):
        if self.github != "":
            url = 'http://api.github.com/repos/%s/collaborators' % (
                self.github
            )

class Stack(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)
    #owner = models.ForeignKey(User, related_name='stacks')

    def __unicode__(self):
        return self.name

    def head(self):
        return Node.objects.get(stack=self, is_head=True)

    def get_node_json(self):
        root = self.head()
        root_dump = Node.dump_bulk(parent=root)
        nodes_dump = dumps(root_dump, cls=DjangoJSONEncoder)

        return nodes_dump

class Node(MP_Node):
    created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name="nodes")
    stack = models.ForeignKey(Stack, related_name="nodes")
    link_type = models.CharField(max_length=2, choices=LINK_CHOICES, default='ro')
    is_head = models.BooleanField(default=False)
    version = models.CharField(max_length=255, null=True, blank=True)

    #node_order_by = ['created']

    def __unicode__(self):
        return '%s @%s' % (self.project.name, self.stack.name)

