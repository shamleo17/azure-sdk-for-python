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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.alert_rules_operations import AlertRulesOperations
from .operations.actions_operations import ActionsOperations
from .operations.alert_rule_templates_operations import AlertRuleTemplatesOperations
from .operations.cases_operations import CasesOperations
from .operations.comments_operations import CommentsOperations
from .operations.case_comments_operations import CaseCommentsOperations
from .operations.bookmarks_operations import BookmarksOperations
from .operations.data_connectors_operations import DataConnectorsOperations
from .operations.entities_operations import EntitiesOperations
from .operations.office_consents_operations import OfficeConsentsOperations
from .operations.product_settings_operations import ProductSettingsOperations
from .operations.cases_aggregations_operations import CasesAggregationsOperations
from .operations.entity_queries_operations import EntityQueriesOperations
from . import models


class SecurityInsightsConfiguration(AzureConfiguration):
    """Configuration for SecurityInsights
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SecurityInsightsConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-securityinsight/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class SecurityInsights(SDKClient):
    """API spec for Microsoft.SecurityInsights (Azure Security Insights) resource provider

    :ivar config: Configuration for client.
    :vartype config: SecurityInsightsConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.securityinsight.operations.Operations
    :ivar alert_rules: AlertRules operations
    :vartype alert_rules: azure.mgmt.securityinsight.operations.AlertRulesOperations
    :ivar actions: Actions operations
    :vartype actions: azure.mgmt.securityinsight.operations.ActionsOperations
    :ivar alert_rule_templates: AlertRuleTemplates operations
    :vartype alert_rule_templates: azure.mgmt.securityinsight.operations.AlertRuleTemplatesOperations
    :ivar cases: Cases operations
    :vartype cases: azure.mgmt.securityinsight.operations.CasesOperations
    :ivar comments: Comments operations
    :vartype comments: azure.mgmt.securityinsight.operations.CommentsOperations
    :ivar case_comments: CaseComments operations
    :vartype case_comments: azure.mgmt.securityinsight.operations.CaseCommentsOperations
    :ivar bookmarks: Bookmarks operations
    :vartype bookmarks: azure.mgmt.securityinsight.operations.BookmarksOperations
    :ivar data_connectors: DataConnectors operations
    :vartype data_connectors: azure.mgmt.securityinsight.operations.DataConnectorsOperations
    :ivar entities: Entities operations
    :vartype entities: azure.mgmt.securityinsight.operations.EntitiesOperations
    :ivar office_consents: OfficeConsents operations
    :vartype office_consents: azure.mgmt.securityinsight.operations.OfficeConsentsOperations
    :ivar product_settings: ProductSettings operations
    :vartype product_settings: azure.mgmt.securityinsight.operations.ProductSettingsOperations
    :ivar cases_aggregations: CasesAggregations operations
    :vartype cases_aggregations: azure.mgmt.securityinsight.operations.CasesAggregationsOperations
    :ivar entity_queries: EntityQueries operations
    :vartype entity_queries: azure.mgmt.securityinsight.operations.EntityQueriesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SecurityInsightsConfiguration(credentials, subscription_id, base_url)
        super(SecurityInsights, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-01-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rules = AlertRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.actions = ActionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rule_templates = AlertRuleTemplatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cases = CasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.comments = CommentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.case_comments = CaseCommentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bookmarks = BookmarksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_connectors = DataConnectorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entities = EntitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.office_consents = OfficeConsentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.product_settings = ProductSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cases_aggregations = CasesAggregationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entity_queries = EntityQueriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
