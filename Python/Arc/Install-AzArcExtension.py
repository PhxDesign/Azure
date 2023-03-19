pip install azure-mgmt-resource azure-mgmt-hybridcompute azure-identity

import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.hybridcompute import HybridComputeManagementClient
from azure.mgmt.hybridcompute.models import MachineExtensionUpdate

# Renseignez les informations d'identification Azure
credential = DefaultAzureCredential()

# Renseignez le nom et l'emplacement de votre groupe de ressources
resource_group_name = "nom_groupe_de_ressources"
location = "emplacement"

# Renseignez le nom et l'emplacement de votre serveur Azure Arc
machine_name = "nom_machine"
subscription_id = "votre_id_d'abonnement"
resource_id = "/subscriptions/" + subscription_id + "/resourceGroups/" + resource_group_name + "/providers/Microsoft.HybridCompute/machines/" + machine_name

# Renseignez le nom de l'extension et la version à mettre à jour
extension_name = "MDE.Windows"
version = "version_extension"

# Instanciez les clients ResourceManagementClient et HybridComputeManagementClient
resource_client = ResourceManagementClient(credential, subscription_id)
hybrid_client = HybridComputeManagementClient(credential, subscription_id)

# Obtenez l'extension de la machine
extension = hybrid_client.machine_extensions.get(resource_id, extension_name)

# Mettez à jour l'extension
extension_update = MachineExtensionUpdate(auto_upgrade_minor_version=True, force_update_tag=version)
hybrid_client.machine_extensions.update(resource_id, extension_name, extension_update)

print("L'extension MDE.Windows a été mise à jour sur la machine Azure Arc " + machine_name)
