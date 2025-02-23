# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['containerapp'] = """
    type: group
    short-summary: Manage Azure Container Apps.
"""

helps['containerapp create'] = """
    type: command
    short-summary: Create a container app.
    examples:
    - name: Create a container app and retrieve its fully qualified domain name.
      text: |
          az containerapp create -n MyContainerapp -g MyResourceGroup \\
              --image myregistry.azurecr.io/my-app:v1.0 --environment MyContainerappEnv \\
              --ingress external --target-port 80 \\
              --registry-server myregistry.azurecr.io --registry-username myregistry --registry-password $REGISTRY_PASSWORD \\
              --query properties.configuration.ingress.fqdn
    - name: Create a container app with resource requirements and replica count limits.
      text: |
          az containerapp create -n MyContainerapp -g MyResourceGroup \\
              --image nginx --environment MyContainerappEnv \\
              --cpu 0.5 --memory 1.0Gi \\
              --min-replicas 4 --max-replicas 8
    - name: Create a container app with secrets and environment variables.
      text: |
          az containerapp create -n MyContainerapp -g MyResourceGroup \\
              --image my-app:v1.0 --environment MyContainerappEnv \\
              --secrets mysecret=secretvalue1 anothersecret="secret value 2" \\
              --env-vars GREETING="Hello, world" SECRETENV=secretref:anothersecret
    - name: Create a container app using a YAML configuration. Example YAML configuration - https://aka.ms/azure-container-apps-yaml
      text: |
          az containerapp create -n MyContainerapp -g MyResourceGroup \\
              --environment MyContainerappEnv \\
              --yaml "path/to/yaml/file.yml"
"""

helps['containerapp update'] = """
    type: command
    short-summary: Update a container app. In multiple revisions mode, create a new revision based on the latest revision.
    examples:
    - name: Update a container app's container image.
      text: |
          az containerapp update -n MyContainerapp -g MyResourceGroup \\
              --image myregistry.azurecr.io/my-app:v2.0
    - name: Update a container app's resource requirements and scale limits.
      text: |
          az containerapp update -n MyContainerapp -g MyResourceGroup \\
              --cpu 0.5 --memory 1.0Gi \\
              --min-replicas 4 --max-replicas 8
"""

helps['containerapp delete'] = """
    type: command
    short-summary: Delete a container app.
    examples:
    - name: Delete a container app.
      text: az containerapp delete -g MyResourceGroup -n MyContainerapp
"""

helps['containerapp show'] = """
    type: command
    short-summary: Show details of a container app.
    examples:
    - name: Show the details of a container app.
      text: |
          az containerapp show -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp list'] = """
    type: command
    short-summary: List container apps.
    examples:
    - name: List container apps in the current subscription.
      text: |
          az containerapp list
    - name: List container apps by resource group.
      text: |
          az containerapp list -g MyResourceGroup
"""

helps['containerapp exec'] = """
    type: command
    short-summary: Open an SSH-like interactive shell within a container app replica
    examples:
    - name: exec into a container app
      text: |
          az containerapp exec -n MyContainerapp -g MyResourceGroup
    - name: exec into a particular container app replica and revision
      text: |
          az containerapp exec -n MyContainerapp -g MyResourceGroup --replica MyReplica --revision MyRevision
    - name: open a bash shell in a containerapp
      text: |
          az containerapp exec -n MyContainerapp -g MyResourceGroup --command bash
"""

helps['containerapp browse'] = """
    type: command
    short-summary: Open a containerapp in the browser, if possible
    examples:
    - name: open a containerapp in the browser
      text: |
          az containerapp browse -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp up'] = """
    type: command
    short-summary: Create or update a container app as well as any associated resources (ACR, resource group, container apps environment, Github Actions, etc.)
    examples:
    - name: Create a container app from a dockerfile in a Github repo (setting up github actions)
      text: |
          az containerapp up -n MyContainerapp --repo https://github.com/myAccount/myRepo
    - name: Create a container app from a dockerfile in a local directory
      text: |
          az containerapp up -n MyContainerapp --source .
    - name: Create a container app from an image in a registry
      text: |
          az containerapp up -n MyContainerapp --image myregistry.azurecr.io/myImage:myTag
    - name: Create a container app from an image in a registry with ingress enabled and a specified environment
      text: |
          az containerapp up -n MyContainerapp --image myregistry.azurecr.io/myImage:myTag --ingress external --target-port 80 --environment MyEnv
"""

helps['containerapp logs'] = """
    type: group
    short-summary: Show container app logs
"""

helps['containerapp logs show'] = """
    type: command
    short-summary: Show past logs and/or print logs in real time (with the --follow parameter). Note that the logs are only taken from one revision, replica, and container.
    examples:
    - name: Fetch the past 20 lines of logs from an app and return
      text: |
          az containerapp logs show -n MyContainerapp -g MyResourceGroup
    - name: Fetch 30 lines of past logs logs from an app and print logs as they come in
      text: |
          az containerapp logs show -n MyContainerapp -g MyResourceGroup --follow --tail 30
    - name: Fetch logs for a particular revision, replica, and container
      text: |
          az containerapp logs show -n MyContainerapp -g MyResourceGroup --replica MyReplica --revision MyRevision --container MyContainer
"""

# Replica Commands
helps['containerapp replica'] = """
    type: group
    short-summary: Manage container app replicas
"""

helps['containerapp replica list'] = """
    type: command
    short-summary: List a container app revision's replica
    examples:
    - name: List a container app's replicas in the latest revision
      text: |
          az containerapp replica list -n MyContainerapp -g MyResourceGroup
    - name: List a container app's replicas in a particular revision
      text: |
          az containerapp replica list -n MyContainerapp -g MyResourceGroup --revision MyRevision
"""

helps['containerapp replica show'] = """
    type: command
    short-summary: Show a container app replica
    examples:
    - name: Show a replica from the latest revision
      text: |
          az containerapp replica show -n MyContainerapp -g MyResourceGroup --replica MyReplica
    - name: Show a replica from the a particular revision
      text: |
          az containerapp replica show -n MyContainerapp -g MyResourceGroup --replica MyReplica --revision MyRevision
"""

# Revision Commands
helps['containerapp revision'] = """
    type: group
    short-summary: Commands to manage revisions.
"""

helps['containerapp revision show'] = """
    type: command
    short-summary: Show details of a revision.
    examples:
    - name: Show details of a revision.
      text: |
          az containerapp revision show -n MyContainerapp -g MyResourceGroup \\
              --revision MyContainerappRevision
"""

helps['containerapp revision list'] = """
    type: command
    short-summary: List a container app's revisions.
    examples:
    - name: List a container app's revisions.
      text: |
          az containerapp revision list -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp revision restart'] = """
    type: command
    short-summary: Restart a revision.
    examples:
    - name: Restart a revision.
      text: |
          az containerapp revision restart -n MyContainerapp -g MyResourceGroup --revision MyContainerappRevision
"""

helps['containerapp revision activate'] = """
    type: command
    short-summary: Activate a revision.
    examples:
    - name: Activate a revision.
      text: |
          az containerapp revision activate -g MyResourceGroup --revision MyContainerappRevision
"""

helps['containerapp revision deactivate'] = """
    type: command
    short-summary: Deactivate a revision.
    examples:
    - name: Deactivate a revision.
      text: |
          az containerapp revision deactivate -g MyResourceGroup --revision MyContainerappRevision
"""

helps['containerapp revision set-mode'] = """
    type: command
    short-summary: Set the revision mode of a container app.
    examples:
    - name: Set a container app to single revision mode.
      text: |
          az containerapp revision set-mode -n MyContainerapp -g MyResourceGroup --mode Single
"""

helps['containerapp revision copy'] = """
    type: command
    short-summary: Create a revision based on a previous revision.
    examples:
    - name: Create a revision based on the latest revision.
      text: |
          az containerapp revision copy -n MyContainerapp -g MyResourceGroup \\
              --cpu 0.75 --memory 1.5Gi
    - name: Create a revision based on a previous revision.
      text: |
          az containerapp revision copy -g MyResourceGroup \\
              --from-revision PreviousRevisionName --cpu 0.75 --memory 1.5Gi

"""

helps['containerapp revision copy'] = """
    type: command
    short-summary: Create a revision based on a previous revision.
    examples:
    - name: Create a revision based on a previous revision.
      text: |
          az containerapp revision copy -n MyContainerapp -g MyResourceGroup --cpu 0.75 --memory 1.5Gi
"""

# Environment Commands
helps['containerapp env'] = """
    type: group
    short-summary: Commands to manage Container Apps environments.
"""

helps['containerapp env create'] = """
    type: command
    short-summary: Create a Container Apps environment.
    examples:
    - name: Create an environment with an auto-generated Log Analytics workspace.
      text: |
          az containerapp env create -n MyContainerappEnvironment -g MyResourceGroup \\
              --location eastus2
    - name: Create an environment with an existing Log Analytics workspace.
      text: |
          az containerapp env create -n MyContainerappEnvironment -g MyResourceGroup \\
              --logs-workspace-id myLogsWorkspaceID \\
              --logs-workspace-key myLogsWorkspaceKey \\
              --location eastus2
"""


helps['containerapp env delete'] = """
    type: command
    short-summary: Delete a Container Apps environment.
    examples:
    - name: Delete an environment.
      text: az containerapp env delete -n MyContainerappEnvironment -g MyResourceGroup
"""

helps['containerapp env show'] = """
    type: command
    short-summary: Show details of a Container Apps environment.
    examples:
    - name: Show the details of an environment.
      text: |
          az containerapp env show -n MyContainerappEnvironment -g MyResourceGroup
"""

helps['containerapp env list'] = """
    type: command
    short-summary: List Container Apps environments by subscription or resource group.
    examples:
    - name: List environments in the current subscription.
      text: |
          az containerapp env list
    - name: List environments by resource group.
      text: |
          az containerapp env list -g MyResourceGroup
"""

helps['containerapp env dapr-component'] = """
    type: group
    short-summary: Commands to manage Dapr components for the Container Apps environment.
"""

helps['containerapp env dapr-component list'] = """
    type: command
    short-summary: List Dapr components for an environment.
    examples:
    - name: List Dapr components for an environment.
      text: |
          az containerapp env dapr-component list -g MyResourceGroup --name MyEnvironment
"""

helps['containerapp env dapr-component show'] = """
    type: command
    short-summary: Show the details of a Dapr component.
    examples:
    - name: Show the details of a Dapr component.
      text: |
          az containerapp env dapr-component show -g MyResourceGroup --dapr-component-name MyDaprComponentName --name MyEnvironment
"""

helps['containerapp env dapr-component set'] = """
    type: command
    short-summary: Create or update a Dapr component.
    examples:
    - name: Create a Dapr component.
      text: |
          az containerapp env dapr-component set -g MyResourceGroup --name MyEnv --yaml MyYAMLPath --dapr-component-name MyDaprComponentName
"""

helps['containerapp env dapr-component remove'] = """
    type: command
    short-summary: Remove a Dapr component from an environment.
    examples:
    - name: Remove a Dapr component from a Container Apps environment.
      text: |
          az containerapp env dapr-component remove -g MyResourceGroup --dapr-component-name MyDaprComponentName --name MyEnvironment
"""

# Identity Commands
helps['containerapp identity'] = """
    type: group
    short-summary: Commands to manage managed identities.
"""

helps['containerapp identity assign'] = """
    type: command
    short-summary: Assign managed identity to a container app.
    long-summary: Managed identities can be user-assigned or system-assigned.
    examples:
    - name: Assign system identity.
      text: |
          az containerapp identity assign -n myContainerapp -g MyResourceGroup --system-assigned
    - name: Assign user identity.
      text: |
          az containerapp identity assign -n myContainerapp -g MyResourceGroup --user-assigned myUserIdentityName
    - name: Assign user identity (from a different resource group than the containerapp).
      text: |
          az containerapp identity assign -n myContainerapp -g MyResourceGroup --user-assigned myUserIdentityResourceId
    - name: Assign system and user identity.
      text: |
          az containerapp identity assign -n myContainerapp -g MyResourceGroup --system-assigned --user-assigned myUserIdentityResourceId
"""

helps['containerapp identity remove'] = """
    type: command
    short-summary: Remove a managed identity from a container app.
    examples:
    - name: Remove system identity.
      text: |
          az containerapp identity remove -n myContainerapp -g MyResourceGroup --system-assigned
    - name: Remove user identity.
      text: |
          az containerapp identity remove -n myContainerapp -g MyResourceGroup --user-assigned myUserIdentityName
    - name: Remove system and user identity (from a different resource group than the containerapp).
      text: |
          az containerapp identity remove -n myContainerapp -g MyResourceGroup --system-assigned --user-assigned myUserIdentityResourceId
    - name: Remove all user identities.
      text: |
          az containerapp identity remove -n myContainerapp -g MyResourceGroup --user-assigned
    - name: Remove system identity and all user identities.
      text: |
          az containerapp identity remove -n myContainerapp -g MyResourceGroup --system-assigned --user-assigned
"""

helps['containerapp identity show'] = """
    type: command
    short-summary: Show managed identities of a container app.
    examples:
    - name: Show managed identities.
      text: |
          az containerapp identity show -n myContainerapp -g MyResourceGroup
"""

# Ingress Commands
helps['containerapp ingress'] = """
    type: group
    short-summary: Commands to manage ingress and traffic-splitting.
"""

helps['containerapp ingress traffic'] = """
    type: subgroup
    short-summary: Commands to manage traffic-splitting.
"""

helps['containerapp ingress show'] = """
    type: command
    short-summary: Show details of a container app's ingress.
    examples:
    - name: Show the details of a container app's ingress.
      text: |
          az containerapp ingress show -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp ingress enable'] = """
    type: command
    short-summary: Enable ingress for a container app.
    examples:
    - name: Enable ingress for a container app.
      text: |
          az containerapp ingress enable -n MyContainerapp -g MyResourceGroup \\
              --type external --allow-insecure --target-port 80 --transport auto
"""

helps['containerapp ingress disable'] = """
    type: command
    short-summary: Disable ingress for a container app.
    examples:
    - name: Disable ingress for a container app.
      text: |
          az containerapp ingress disable -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp ingress traffic'] = """
    type: group
    short-summary: Commands to manage traffic-splitting.
"""

helps['containerapp ingress traffic set'] = """
    type: command
    short-summary: Configure traffic-splitting for a container app.
    examples:
    - name: Route 100%% of a container app's traffic to its latest revision.
      text: |
          az containerapp ingress traffic set -n MyContainerapp -g MyResourceGroup --traffic-weight latest=100
    - name: Split a container app's traffic between two revisions.
      text: |
          az containerapp ingress traffic set -n MyContainerapp -g MyResourceGroup --traffic-weight latest=80 MyRevisionName=20
"""

helps['containerapp ingress traffic show'] = """
    type: command
    short-summary: Show traffic-splitting configuration for a container app.
    examples:
    - name: Show a container app's ingress traffic configuration.
      text: |
          az containerapp ingress traffic show -n MyContainerapp -g MyResourceGroup
"""

# Registry Commands
helps['containerapp registry'] = """
    type: group
    short-summary: Commands to manage container registry information.
"""

helps['containerapp registry show'] = """
    type: command
    short-summary: Show details of a container registry.
    examples:
    - name: Show the details of a container registry.
      text: |
          az containerapp registry show -n MyContainerapp -g MyResourceGroup --server MyContainerappRegistry.azurecr.io
"""

helps['containerapp registry list'] = """
    type: command
    short-summary: List container registries configured in a container app.
    examples:
    - name: List container registries configured in a container app.
      text: |
          az containerapp registry list -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp registry set'] = """
    type: command
    short-summary: Add or update a container registry's details.
    examples:
    - name: Configure a container app to use a registry.
      text: |
          az containerapp registry set -n MyContainerapp -g MyResourceGroup \\
              --server MyExistingContainerappRegistry.azurecr.io --username MyRegistryUsername --password MyRegistryPassword
"""

helps['containerapp registry remove'] = """
    type: command
    short-summary: Remove a container registry's details.
    examples:
    - name: Remove a registry from a Containerapp.
      text: |
          az containerapp registry remove -n MyContainerapp -g MyResourceGroup --server MyContainerappRegistry.azurecr.io
"""

# Secret Commands
helps['containerapp secret'] = """
    type: group
    short-summary: Commands to manage secrets.
"""

helps['containerapp secret show'] = """
    type: command
    short-summary: Show details of a secret.
    examples:
    - name: Show the details of a secret.
      text: |
          az containerapp secret show -n MyContainerapp -g MyResourceGroup --secret-name MySecret
"""

helps['containerapp secret list'] = """
    type: command
    short-summary: List the secrets of a container app.
    examples:
    - name: List the secrets of a container app.
      text: |
          az containerapp secret list -n MyContainerapp -g MyResourceGroup
"""

helps['containerapp secret remove'] = """
    type: command
    short-summary: Remove secrets from a container app.
    examples:
    - name: Remove secrets from a container app.
      text: |
          az containerapp secret remove -n MyContainerapp -g MyResourceGroup --secret-names MySecret MySecret2
"""

helps['containerapp secret set'] = """
    type: command
    short-summary: Create/update secrets.
    examples:
    - name: Add secrets to a container app.
      text: |
          az containerapp secret set -n MyContainerapp -g MyResourceGroup --secrets MySecretName1=MySecretValue1 MySecretName2=MySecretValue2
    - name: Update a secret.
      text: |
          az containerapp secret set -n MyContainerapp -g MyResourceGroup --secrets MyExistingSecretName=MyNewSecretValue
"""

helps['containerapp github-action'] = """
    type: group
    short-summary: Commands to manage GitHub Actions.
"""

helps['containerapp github-action add'] = """
    type: command
    short-summary: Add a Github Actions workflow to a repository to deploy a container app.
    examples:
    - name: Add GitHub Actions, using Azure Container Registry and personal access token.
      text: az containerapp github-action add -g MyResourceGroup -n MyContainerapp --repo-url https://github.com/userid/repo --branch main
          --registry-url myregistryurl.azurecr.io
          --service-principal-client-id 00000000-0000-0000-0000-00000000
          --service-principal-tenant-id 00000000-0000-0000-0000-00000000
          --service-principal-client-secret ClientSecret
          --token MyAccessToken
    - name: Add GitHub Actions, using Azure Container Registry and log in to GitHub flow to retrieve personal access token.
      text: az containerapp github-action add -g MyResourceGroup -n MyContainerapp --repo-url https://github.com/userid/repo --branch main
          --registry-url myregistryurl.azurecr.io
          --service-principal-client-id 00000000-0000-0000-0000-00000000
          --service-principal-tenant-id 00000000-0000-0000-0000-00000000
          --service-principal-client-secret ClientSecret
          --login-with-github
    - name: Add GitHub Actions, using Docker Hub and log in to GitHub flow to retrieve personal access token.
      text: az containerapp github-action add -g MyResourceGroup -n MyContainerapp --repo-url https://github.com/userid/repo --branch main
          --registry-username MyUsername
          --registry-password MyPassword
          --service-principal-client-id 00000000-0000-0000-0000-00000000
          --service-principal-tenant-id 00000000-0000-0000-0000-00000000
          --service-principal-client-secret ClientSecret
          --login-with-github
"""

helps['containerapp github-action delete'] = """
    type: command
    short-summary: Remove a previously configured Container Apps GitHub Actions workflow from a repository.
    examples:
    - name: Remove GitHub Actions using a personal access token.
      text: az containerapp github-action delete -g MyResourceGroup -n MyContainerapp
          --token MyAccessToken
    - name: Remove GitHub Actions using log in to GitHub flow to retrieve personal access token.
      text: az containerapp github-action delete -g MyResourceGroup -n MyContainerapp
          --login-with-github
"""

helps['containerapp github-action show'] = """
    type: command
    short-summary: Show the GitHub Actions configuration on a container app.
    examples:
    - name: Show the GitHub Actions configuration on a Containerapp.
      text: az containerapp github-action show -g MyResourceGroup -n MyContainerapp
"""

# Dapr Commands
helps['containerapp dapr'] = """
    type: group
    short-summary: Commands to manage Dapr. To manage Dapr components, see `az containerapp env dapr-component`.
"""

helps['containerapp dapr enable'] = """
    type: command
    short-summary: Enable Dapr for a container app. Updates existing values.
    examples:
    - name: Enable Dapr for a container app.
      text: |
          az containerapp dapr enable -n MyContainerapp -g MyResourceGroup --dapr-app-id my-app-id --dapr-app-port 8080
"""

helps['containerapp dapr disable'] = """
    type: command
    short-summary: Disable Dapr for a container app. Removes existing values.
    examples:
    - name: Disable Dapr for a container app.
      text: |
          az containerapp dapr disable -n MyContainerapp -g MyResourceGroup
"""
