# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ActiveBaseSecurityAdminRule
from ._models_py3 import ActiveBaseSecurityUserRule
from ._models_py3 import ActiveConfigurationParameter
from ._models_py3 import ActiveConnectivityConfiguration
from ._models_py3 import ActiveConnectivityConfigurationsListResult
from ._models_py3 import ActiveDefaultSecurityAdminRule
from ._models_py3 import ActiveDefaultSecurityUserRule
from ._models_py3 import ActiveSecurityAdminRule
from ._models_py3 import ActiveSecurityAdminRulesListResult
from ._models_py3 import ActiveSecurityUserRule
from ._models_py3 import ActiveSecurityUserRulesListResult
from ._models_py3 import AddressPrefixItem
from ._models_py3 import AdminRule
from ._models_py3 import AdminRuleCollection
from ._models_py3 import AdminRuleCollectionListResult
from ._models_py3 import AdminRuleListResult
from ._models_py3 import AzureAsyncOperationResult
from ._models_py3 import BaseAdminRule
from ._models_py3 import BaseUserRule
from ._models_py3 import CloudErrorBody
from ._models_py3 import Components1Jq1T4ISchemasManagedserviceidentityPropertiesUserassignedidentitiesAdditionalproperties
from ._models_py3 import ConfigurationGroup
from ._models_py3 import ConnectivityConfiguration
from ._models_py3 import ConnectivityConfigurationListResult
from ._models_py3 import ConnectivityGroupItem
from ._models_py3 import CrossTenantScopes
from ._models_py3 import DefaultAdminRule
from ._models_py3 import DefaultUserRule
from ._models_py3 import EffectiveBaseSecurityAdminRule
from ._models_py3 import EffectiveConnectivityConfiguration
from ._models_py3 import EffectiveDefaultSecurityAdminRule
from ._models_py3 import EffectiveSecurityAdminRule
from ._models_py3 import EffectiveVirtualNetwork
from ._models_py3 import EffectiveVirtualNetworksListResult
from ._models_py3 import EffectiveVirtualNetworksParameter
from ._models_py3 import Error
from ._models_py3 import ErrorDetails
from ._models_py3 import ExtendedLocation
from ._models_py3 import Hub
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import NetworkGroup
from ._models_py3 import NetworkGroupListResult
from ._models_py3 import NetworkManager
from ._models_py3 import NetworkManagerCommit
from ._models_py3 import NetworkManagerConnection
from ._models_py3 import NetworkManagerConnectionListResult
from ._models_py3 import NetworkManagerDeploymentStatus
from ._models_py3 import NetworkManagerDeploymentStatusListResult
from ._models_py3 import NetworkManagerDeploymentStatusParameter
from ._models_py3 import NetworkManagerEffectiveConnectivityConfigurationListResult
from ._models_py3 import NetworkManagerEffectiveSecurityAdminRulesListResult
from ._models_py3 import NetworkManagerListResult
from ._models_py3 import NetworkManagerPropertiesNetworkManagerScopes
from ._models_py3 import NetworkManagerSecurityGroupItem
from ._models_py3 import PatchObject
from ._models_py3 import ProxyResource
from ._models_py3 import QueryRequestOptions
from ._models_py3 import Resource
from ._models_py3 import ScopeConnection
from ._models_py3 import ScopeConnectionListResult
from ._models_py3 import SecurityAdminConfiguration
from ._models_py3 import SecurityAdminConfigurationListResult
from ._models_py3 import SecurityUserConfiguration
from ._models_py3 import SecurityUserConfigurationListResult
from ._models_py3 import StaticMember
from ._models_py3 import StaticMemberListResult
from ._models_py3 import SubResource
from ._models_py3 import SystemData
from ._models_py3 import TagsObject
from ._models_py3 import UserRule
from ._models_py3 import UserRuleCollection
from ._models_py3 import UserRuleCollectionListResult
from ._models_py3 import UserRuleListResult


from ._network_management_client_enums import (
    Access,
    AddressPrefixType,
    AdminRuleKind,
    AuthenticationMethod,
    ConfigurationType,
    ConnectivityTopology,
    CreatedByType,
    DeleteExistingNSGs,
    DeleteExistingPeering,
    DeploymentStatus,
    EffectiveAdminRuleKind,
    EffectiveUserRuleKind,
    ExtendedLocationTypes,
    GroupConnectivity,
    IPAllocationMethod,
    IPVersion,
    IsGlobal,
    MembershipType,
    NetworkIntentPolicyBasedService,
    NetworkOperationStatus,
    ProvisioningState,
    ResourceIdentityType,
    ScopeConnectionState,
    SecurityConfigurationRuleAccess,
    SecurityConfigurationRuleDirection,
    SecurityConfigurationRuleProtocol,
    UseHubGateway,
    UserRuleKind,
)

__all__ = [
    'ActiveBaseSecurityAdminRule',
    'ActiveBaseSecurityUserRule',
    'ActiveConfigurationParameter',
    'ActiveConnectivityConfiguration',
    'ActiveConnectivityConfigurationsListResult',
    'ActiveDefaultSecurityAdminRule',
    'ActiveDefaultSecurityUserRule',
    'ActiveSecurityAdminRule',
    'ActiveSecurityAdminRulesListResult',
    'ActiveSecurityUserRule',
    'ActiveSecurityUserRulesListResult',
    'AddressPrefixItem',
    'AdminRule',
    'AdminRuleCollection',
    'AdminRuleCollectionListResult',
    'AdminRuleListResult',
    'AzureAsyncOperationResult',
    'BaseAdminRule',
    'BaseUserRule',
    'CloudErrorBody',
    'Components1Jq1T4ISchemasManagedserviceidentityPropertiesUserassignedidentitiesAdditionalproperties',
    'ConfigurationGroup',
    'ConnectivityConfiguration',
    'ConnectivityConfigurationListResult',
    'ConnectivityGroupItem',
    'CrossTenantScopes',
    'DefaultAdminRule',
    'DefaultUserRule',
    'EffectiveBaseSecurityAdminRule',
    'EffectiveConnectivityConfiguration',
    'EffectiveDefaultSecurityAdminRule',
    'EffectiveSecurityAdminRule',
    'EffectiveVirtualNetwork',
    'EffectiveVirtualNetworksListResult',
    'EffectiveVirtualNetworksParameter',
    'Error',
    'ErrorDetails',
    'ExtendedLocation',
    'Hub',
    'ManagedServiceIdentity',
    'NetworkGroup',
    'NetworkGroupListResult',
    'NetworkManager',
    'NetworkManagerCommit',
    'NetworkManagerConnection',
    'NetworkManagerConnectionListResult',
    'NetworkManagerDeploymentStatus',
    'NetworkManagerDeploymentStatusListResult',
    'NetworkManagerDeploymentStatusParameter',
    'NetworkManagerEffectiveConnectivityConfigurationListResult',
    'NetworkManagerEffectiveSecurityAdminRulesListResult',
    'NetworkManagerListResult',
    'NetworkManagerPropertiesNetworkManagerScopes',
    'NetworkManagerSecurityGroupItem',
    'PatchObject',
    'ProxyResource',
    'QueryRequestOptions',
    'Resource',
    'ScopeConnection',
    'ScopeConnectionListResult',
    'SecurityAdminConfiguration',
    'SecurityAdminConfigurationListResult',
    'SecurityUserConfiguration',
    'SecurityUserConfigurationListResult',
    'StaticMember',
    'StaticMemberListResult',
    'SubResource',
    'SystemData',
    'TagsObject',
    'UserRule',
    'UserRuleCollection',
    'UserRuleCollectionListResult',
    'UserRuleListResult',
    'Access',
    'AddressPrefixType',
    'AdminRuleKind',
    'AuthenticationMethod',
    'ConfigurationType',
    'ConnectivityTopology',
    'CreatedByType',
    'DeleteExistingNSGs',
    'DeleteExistingPeering',
    'DeploymentStatus',
    'EffectiveAdminRuleKind',
    'EffectiveUserRuleKind',
    'ExtendedLocationTypes',
    'GroupConnectivity',
    'IPAllocationMethod',
    'IPVersion',
    'IsGlobal',
    'MembershipType',
    'NetworkIntentPolicyBasedService',
    'NetworkOperationStatus',
    'ProvisioningState',
    'ResourceIdentityType',
    'ScopeConnectionState',
    'SecurityConfigurationRuleAccess',
    'SecurityConfigurationRuleDirection',
    'SecurityConfigurationRuleProtocol',
    'UseHubGateway',
    'UserRuleKind',
]
