from django.db import models
from django.contrib.auth.models import User

from treebeard.mp_tree import MP_Node

LINK_CHOICES = (
    ('dy', 'Dynamic Linking'),
    ('st', 'Static Linking'),
    ('ot', 'Other'),
    ('na', 'None'),
    ('ro', 'Root')
)

class Licenses(models.Model):
    name = models.CharField(max_length=255)

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    github = models.URLField(max_length=255, null=True, blank=True)
    license = models.ManyToManyField(Licenses)
    is_private = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Stack(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    #owner = models.ForeignKey(User, related_name='stacks')

    def __unicode__(self):
        return self.name

    def head(self):
        pass

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

