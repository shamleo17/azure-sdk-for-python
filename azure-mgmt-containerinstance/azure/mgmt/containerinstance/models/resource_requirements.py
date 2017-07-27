# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceRequirements(Model):
    """The resource requirements.

    :param requests: The resource requests of this container.
    :type requests: :class:`ResourceRequests
     <azure.mgmt.containerinstance.models.ResourceRequests>`
    :param limits: The resource limits of this container.
    :type limits: :class:`ResourceLimits
     <azure.mgmt.containerinstance.models.ResourceLimits>`
    """

    _validation = {
        'requests': {'required': True},
    }

    _attribute_map = {
        'requests': {'key': 'requests', 'type': 'ResourceRequests'},
        'limits': {'key': 'limits', 'type': 'ResourceLimits'},
    }

    def __init__(self, requests, limits=None):
        self.requests = requests
        self.limits = limits
