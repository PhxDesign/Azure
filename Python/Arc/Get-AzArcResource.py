from azure.identity import DefaultAzureCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest

# Initialisez les informations d'identification pour l'authentification Azure
credential = DefaultAzureCredential()

# Initialisez le client ResourceGraphClient
client = ResourceGraphClient(credential)

# Définissez la requête Resource Graph pour récupérer les ressources Arc Servers
query = QueryRequest(
    query="where type == 'Microsoft.HybridCompute/machines' | where kind == 'AzureArcMachines' | project name"
)

# Exécutez la requête et récupérez les résultats
result = client.resources(query)

# Parcourez les résultats et imprimez les noms des serveurs Arc
for item in result.data:
    print(item["name"])
