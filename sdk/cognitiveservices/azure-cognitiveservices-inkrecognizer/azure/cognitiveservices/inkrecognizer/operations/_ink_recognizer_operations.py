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

from msrest.pipeline import ClientRawResponse

from .. import models


class InkRecognizerOperations(object):
    """InkRecognizerOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def recognize(
            self, body, x_ms_client_request_id=None, custom_headers=None, raw=False, **operation_config):
        """Ink Recognition operation is used to perform ink layout and recognition
        of written words and shapes. It allows passing the ink strokes to the
        service to get the recognition results in the response.

        :param body: The collection of stroke objects to send for analysis
        :type body:
         ~azure.cognitiveservices.inkrecognizer.models.AnalysisRequest
        :param x_ms_client_request_id: The request id used to uniquely
         identify each request during troubleshooting. This is an optional
         parameter useful for correlating logs and other artifacts.
        :type x_ms_client_request_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalysisResponse or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.inkrecognizer.models.AnalysisResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorModelException<azure.cognitiveservices.inkrecognizer.models.ErrorModelException>`
        """
        # Construct URL
        url = self.recognize.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", x_ms_client_request_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'AnalysisRequest')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorModelException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AnalysisResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    recognize.metadata = {'url': '/recognize'}