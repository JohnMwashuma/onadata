# -*- coding: utf-8 -*-
"""
Messaging /messaging viewsets.
"""
from __future__ import unicode_literals

from rest_framework import mixins, viewsets
from actstream.models import Action

from onadata.apps.messaging.serializers import MessageSerializer
from onadata.apps.messaging.constants import MESSAGE


# pylint: disable=too-many-ancestors
class MessagingViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """
    ViewSet for the Messaging app - implements /messaging API endpoint
    """

    serializer_class = MessageSerializer
    queryset = Action.objects.filter(verb=MESSAGE)
