[//]: # (title: Microsoft Sentinel - Migation de la solution)
[//]: # (description: Procédure sur la migration de la solution Microsoft Sentinel)
[//]: # (author: PhxDesign)
[//]: # (ms.author: jlgauthier)
[//]: # (ms.topic: SIEM)
[//]: # (ms.date: 03/19/2023)

# Microsoft Sentinel - Migration de la solution - ![](https://badgen.net/badge/Statut/draft/grey?icon=azure)

## Questions/réponses sur la migration

|Question |Réponse |
|--- |---|
|Est-ce possible de migrer la solution Microsoft Sentinel? |Oui, il est possible de migrer la solution. |
|Est-ce que la migration est supportée par Microsoft? |Non, pour le moment [Microsoft indique toujours](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/move-workspace#workspace-move-considerations) qu'il n'est pas possible de migrer la solution. |
|Est-ce que la migration s'effectue via un déplacement unique des ressources? | Non, la migration consiste en trois grandes étapes assez simples. |
|Est-ce que l'abonnement peut-être différent de l'instance source? |Oui, tant que l'abonnement permet de respecter les limites de migration identifiées plus bas. |
|Est-ce que la migration comporte la perte de données? |Non, les données présentes dans l'instance Log Analytics sont conservées. |
|Existe-t-il des limites pour la migration? |Oui, les limites sont les suivantes: |
| |  La solution doit rester dans le même tenant. |
| |  La région de destination, si déférente, doit conserver la même disponibilité de services que celle de la région source et des [opérations supplémentaires](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/move-workspace-region) sont requises et qui ne font pas partie de cette procédure. |
| |  Certains services complémentaires ne peuvent être migrés, ou conserveront la région d'origine (selon la possibilité du service). |

## Les trois grandes étapes

### Identification des ressources et des accès

Établir l'inventaire des ressources, des accès et de la configuration nécessaire au fonctionnement et l'utilisation de la solution.

### Migration de la solution

Définir les différentes étapes requises en vue de déplacer les composants identifiés.

### Validation et test

Assurer le comportement visé avant et après le processus de migration.

## Analyse et création des tâches de migration

### Identification des ressources et des accès

#### Documentation de la configuration Sentinel

Si ce n'est déjà fait, assurez-vous de documenter la configuration actuelle de la solution. Il est suggéré d'effectuer des captures d'écran qui serviront lors des opérations de validation. Vous devriez au minimum regrouper les sections:
 * Workbooks
 * Hunting
 * Notebooks
    * My notebooks
 * Content hub
 * Repositories
 * Watchlist
 * Automation
   * Automation rules
   * Active playbooks

> Les éléments suivants sont intégrés au Content hub et s'afficheront à titre informatif seulement lorsqu’activé: Data connectors et Analytics.

#### Identification des ressources de destination

À partir du portail Azure, exporter les éléments du groupe de ressources auquel appartient l'instance source Sentinel. Les données serviront à définir le statut de chacun des composants et suivre les étapes de migration.

#### Ajustement des accès selon le niveau (MG, Subs, RG)

Tout comme pour les ressources, il est important de s'assurer que les accès soient présents avant même de débuter la migration. Vous devez donc exporter la liste de ceux-ci, à partir du portail Azure ou via Powershel.

> Il est recommandé d'inclure au minimum les niveaux suivants; Groupe de gestion (Managment group), abonnement (Subscription) et groupe de ressources (Resources group).

### Migration de la solution

#### Suppression de la solution Sentinel source

À partir du groupe de ressources hébergeant l'instance source Microsoft Sentinel, identifier la solution SecurityCenterFree(_nom de l'instance log analytics_) puis supprimer cette dernière.

> ATTENTION, _nom de l'instance log analytics_ doit correspondre à celle liée avec la solution Sentinel que vous voulez migrer.

#### Migration des ressources
Il est suggéré de suivre ces étapes dans l'ordre afin d'optimiser le temps et limiter les erreurs. Pour chaque déplacement, effectuer une capture d'écran lorsque le processus de validation est complété.

> Le processus de validation représente l'étape 2 du déplacement de ressources.

1. Log Analytics Workspace
1. Storage Account
1. API Connection

#### Création de la nouvelle instance Sentinel

#### Configuration de la nouvelle solution Sentinel

### Validation et test

#### Vérification des composantes et éléments de la solution
