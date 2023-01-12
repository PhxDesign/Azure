---
title: Azure Fundamentals - Les principaux composants architecturaux
description: Résumé de la formation Azure Fundamentals
author: PhxDesign
ms.author: jlgauthier
ms.topic: overview
ms.date: 01/05/2023
ms.custom: template-overview
---

# Azure Fundamentals - Les principaux composants architecturaux

Condensé sur la formation Azure Fundamentals permettant d'obtenir la certification AZ-900.

## Qu'est-ce que Azure

Azure est un ensemble de services cloud en constante évolution qui vous aide à faire face aux défis actuels et futurs de l’entreprise. Il vous offre la possibilité de créer, gérer et déployer des applications sur un réseau de dimension mondiale avec vos outils et frameworks préférés.

****Avantages****

- Préparer le futur: l’innovation continue chez Microsoft soutient vos projets de développement d’aujourd’hui et vos visions de produits de demain.
- Développez selon vos conditions: avec l’open source et la prise en charge de l’ensemble des langages et des frameworks, vous pouvez développer et déployer comme vous le souhaitez.
- Travaillez en mode hybride et en continu: localement, dans le cloud et en périphérie, intégrez et gérez vos environnements avec des outils et des services conçus pour une solution de cloud hybride.
- La confiance du cloud:  bénéficiez d’une sécurité de bout en bout, avec l’appui d’une équipe d’experts et d’une conformité proactive approuvée par les entreprises.

### Les comptes Azure

Pour utiliser les services Azure, un compte doit être créé afin d'y ajouter un abonnement et ainsi déployer des ressources. Une entreprise peut utiliser un seul compte Azure pour l’ensemble de son activité, mais des abonnements distincts pour les services de développement, de marketing et de vente.

***Les comptes***

- Compte Azure gratuit
  - L’accès gratuit aux principaux produits Azure pendant 12 mois.
  - Un crédit à utiliser dans les 30 premiers jours.
  - L’accès à plus de 25 produits toujours gratuits.

- Compte étudiant Azure gratuit
  - Accès gratuit à certains services Azure pendant 12 mois.
  - Un crédit de 100$ à utiliser pendant les 12 premiers mois.
  - Accès gratuit à certains outils de développement de logiciels.

- Bac à sable Microsoft Learn

    La technologie de bac à sable créee un abonnement temporaire et l’ajoute à votre compte Azure, ce qui permet de créer des ressources Azure dans le cadre d’un module Learn et de les nettoyer automatiquement une fois que vous avez terminé le module.

## Décrire l'infrastructure physique

### Infrastructure physique

À la base de l’infrastructure physique d’Azure se trouvent les centres de données, dont les ressources sont organisées dans des racks, avec une alimentation, un système de refroidissement et une infrastructure réseau dédiés. Cependant, ces centres de données individuels ne sont pas directement accessibles, ils sont regroupés dans des régions ou des zones de disponibilité conçues pour  bénéficier d’une résilience et d’une fiabilité vitales pour les charges de travail.

#### Régions

Une région est une zone géographique constituée d’au moins un centre de données, mais qui peut en contenir plusieurs proches les uns des autres et reliés par un réseau à faible latence.

> - Certains services ou fonctionnalités de machines virtuelles ne sont disponibles que dans certaines régions, comme des tailles de machines virtuelles ou des types de stockage spécifiques.
> - Certains services Azure mondiaux ne vous obligent pas à sélectionner une région particulière, comme c’est le cas d’Azure Active Directory, d’Azure Traffic Manager et d’Azure DNS.

#### Zones de disponibilité

Les zones de disponibilité sont des centres de données physiquement séparés au sein d’une région. Chaque zone de disponibilité est composée d’un ou de plusieurs centres de données équipés d’une alimentation, d’un refroidissement et d’un réseau indépendants et constitue une limite d'isolation.

Les zones de disponibilité sont utilisées principalement pour les machines virtuelles, les disques managés, les équilibreurs de charge et les bases de données SQL puis classés en trois catégories:

- Services zonaux: vous épinglez la ressource à une zone spécifique.
- Services redondants interzones: la plateforme effectue automatiquement une réplication entre des zones.
- Services non régionnaux: les services sont toujours disponibles à partir de zones géographiques et sont résilients aux pannes à l’échelle de la zone ainsi qu’aux pannes à l’échelle de la région.

> Les régions qui ont des zones de disponibilité ont au moins trois zones disctinctes.

****Avantages****

- Vous pouvez utiliser des zones de disponibilité pour exécuter des applications stratégiques et bâtir la haute disponibilité dans votre architecture d’application par la colocalisation de vos ressources de calcul, de stockage, de réseau et de données dans une zone de disponibilité, et par la réplication dans d’autres zones de disponibilité.

#### Paires de régions

La plupart des régions Azure sont associées à une autre région au sein d’une même zone géographique (par exemple États-Unis, Europe ou Asie) distante d’au moins 480 kilomètres. Cette approche permet la réplication de ressources à l’échelle d’une zone géographique, ce qui contribue à réduire les risques d’interruptions liées à des événements tels que des catastrophes naturelles, des troubles civils, des coupures de courant ou des pannes de réseau physique affectant une région entière.

****Avantages****

- En cas de panne importante d’Azure, une région de chaque paire est prioritaire pour garantir qu’au moins l’une d’entre elles est restaurée aussi rapidement que possible pour les applications hébergées dans cette paire de régions.
- Les mises à jour Azure planifiées sont déployées sur les régions jumelées, à raison d’une région à la fois, pour limiter les interruptions de service et les risques de panne de l’application.
- Les données continuent de résider dans la même zone géographique que la région avec laquelle elle est jumelée (sauf Brésil Sud) afin de répondre aux exigences relatives à la fiscalité et à l’application de la loi.

> Certaines régions sont appairées dans une seule direction, appelé appairage unidirectionnel ou la région primaire n’assure pas de sauvegarde pour sa région secondaire.

#### Régions souveraines

Les régions souveraines sont des instances d’Azure isolées de l’instance principale d’Azure.

- US DoD Centre, US Gov Virginie, US Gov Iowa, etc.: ces centres de données sont gérés par un personnel autorisé aux États-Unis et incluent des certifications de conformité supplémentaires.
- Chine Est, Chine Nord, etc.: ces régions sont disponibles via un partenariat unique conclu entre Microsoft et 21Vianet, qui stipule que Microsoft ne gère pas directement les centres de données.

## Décrire l'infrastructure de gestion

L’infrastructure de gestion comprend des ressources et des groupes de ressources, des abonnements et des comptes Azure.

### Ressources et groupes de ressources

#### Ressource
Une ressource est le bloc de construction de base que vous créez, provisionnez, déployez, etc. dans Azure, tel les machines virtuelles, les réseaux virtuels, les bases de données, les services cognitifs, etc.

#### Groupe de ressources

Un groupe de ressources est simplement un regroupements d'une ou plusieurs ressources. Un groupe de ressource ne peut être imbriqué dans un autre groupe et chaque ressource appartient à un seul groupe de ressource.

Les groupes de ressources offrent un moyen pratique de regrouper des ressources. Quand vous appliquez une action à un groupe de ressources, cette action s’applique à toutes les ressources actuelles et futures contenues dans le groupe de ressources.

> Il n’existe pas de règles strictes concernant la façon d’utiliser les groupes de ressources. Lorsque vous provisionnez des ressources, il est judicieux de réfléchir à la structure de groupe de ressources qui répond le mieux à vos besoins.

### Abonnements

Les abonnements sont une unité de gestion, de facturation et de mise à l’échelle permettant d’organiser logiquement vos groupes de ressources tout en facilitant la facturation.

Un compte peut comporter plusieurs abonnements, mais il n'est pas nécessaire d’en posséder plusieurs. Avec de multiples abonnements il est possible de configurer différents modèles de facturation et appliquer différentes stratégies de gestion d’accès en vue de définir des limites autour de produits, de services et de ressources Azure.

****Types de limites d'abonnement****

- Limites de facturation: détermine la façon dont l’utilisation d’Azure est facturée à un compte Azure.
- Limites de contrôle d'accès: Azure applique des stratégies de gestion des accès au niveau de l’abonnement, ce qui vous permet de créer des abonnements distincts pour les différentes structures organisationnelles.

#### Créer des abonnements Azure supplémentaires

Vous pouvez créer des abonnements supplémentaires à des fins de gestion des ressources ou de la facturation.

****Exemples****

- Environnements: pour des raisons de sécurité ou pour isoler les données à des fins de conformité, des abonnements distincts peuvent être configurés pour des environnements de développement et de tests.
- Structures organisationelles: ous pouvez créer des abonnements qui reflètent vos différentes structures organisationnelles. Cette conception vous permet de gérer et contrôler l’accès aux ressources provisionnées par les utilisateurs au sein de chaque abonnement.
- Facturation: vous pouvez créer des abonnements supplémentaires pour vos besoins de facturation. Par exemple, créez un abonnement dédié à vos charges de travail de production et un autre abonnement réservé à vos charges de travail de développement et de test.

### Groupe d'administration

Les groupes d’administration Azure fournissent un niveau d’étendue au-delà des abonnements et améliorent la gestion des accès, des stratégies et de la conformité de ceux-ci. Vous organisez les abonnements en conteneurs appelés groupes d’administration, et vous appliquez des conditions de gouvernance à ce niveau. Les groupes d’administration vous permettent une gestion de niveau entreprise à grande échelle, quel que soit le type de vos abonnements.

****Avantages****

- Tous les abonnements contenus dans un groupe d’administration héritent automatiquement des conditions appliquées au groupe d’administration.
- Les groupes d’administration peuvent être imbriqués.

### Groupe d'administration, abonnements et hiéarchie de groupes de ressources

Comment utiliser les groupes d'administration?

* Créer une hiéarchie qui applique une stratégie

    Vous pouvez limiter la localisation des ressources à une ou certaines régions spécifiques afin de répondre à des règles de conformité.

* Fournir aux utilisateurs un accès à plusieurs abonnements

    Vous pouvez créer une affectation de contrôle d’accès en fonction du rôle (RBAC) dans le groupe d’administration, ainsi tous les sous-groupes d’administration, abonnements, groupes de ressources et ressources relevant de ce groupe d’administration hériteraient également de ces autorisations.

> Important
>
> - 10 000 groupes d’administration peuvent être pris en charge dans un seul annuaire.
> - Une arborescence de groupes d’administration peut prendre en charge jusqu’à six niveaux de profondeur. Cette limite n’inclut pas le niveau Racine ni le niveau de l’abonnement.
> - Chaque groupe d’administration et chaque abonnement ne peut avoir qu’un seul parent.

## Décrire les services de calcul et réseau

### Décrire les machines virtuelles

Les machines virtuelles fournissent une infrastructure IaaS (infrastructure as a service) sous la forme d’un serveur virtualisé, et peuvent être utilisées de nombreuses façons. Cependant, s’agissant d’une offre IaaS, vous devez quand même configurer, mettre à jour et maintenir les logiciels qui s’exécutent sur la machine virtuelle.

****Avantages****

- Avoir un contrôle total sur le système d’exploitation.
- Exécuter des logiciels personnalisés.
- Utiliser des configurations d’hébergement personnalisées.

Vous pouvez créer et provisionner une machine virtuelle en quelques minutes quand vous sélectionnez une image de machine virtuelle préconfigurée, étant un modèle pouvant déjà inclure un système d’exploitation et d’autres logiciels, tels que des outils de développement ou des environnements d’hébergement web.

#### Mise à l'échelle des machines virtuelles

Vous pouvez exécuter des machines virtuelles uniques à des fins de test, de développement ou de tâches mineures, ou regrouper des machines virtuelles afin de fournir une haute disponibilité, une scalabilité et une redondance.

****Groupes identiques de machines virtuelles****

  Les groupes identiques vous permettent de gérer, configurer et mettre à jour de manière centralisée un grand nombre de machines virtuelles en quelques minutes. Ils déploient automatiquement un équilibreur de charge pour faire en sorte que vos ressources soient utilisées de manière efficace.

****Groupes de haute disponibilité de machines virtuelles****

  Les groupes à haute disponibilité sont conçus pour faire en sorte que les machines virtuelles échelonnent les mises à jour et qu’elles disposent d’une alimentation et d’une connectivité réseau différenciées. Ils regroupent de deux manières:

  - ****Domaine de mise à jour:**** machines virtuelles de groupes de domaine de mise à jour qui peuvent être redémarrées en même temps.
  - ****Domaine d'erreur:**** le domaine d’erreur regroupe vos machines virtuelles selon une source d’alimentation et un commutateur réseau communs.

#### Cas d'utilisation de machines virtuelles

- ****Pendant le test et le développement:****
le personnel chargé des tests et du développement peut facilement créer différentes configurations de système d’exploitation et d’application pour ensuite les supprimer quand il n’en a plus besoin.

- ****Lors de l'exécution d'application dans le cloud:****
Arrêter des machines virtuelles lorsque vous n’en avez pas besoin ou les démarrer rapidement pour répondre à une augmentation soudaine de la demande en lien à une application cloud peut apporter des avantages économiques substantiels puisque vous payez uniquement pour les ressources que vous utilisez.

- ****Lors de l'extension de votre centre de données au cloud:****
 Une organisation peut développer les capacités de son propre réseau local en créant un réseau virtuel dans Azure et en ajoutant des machines virtuelles à ce réseau virtuel.

- ****Pendant une reprise d'activité après sinistre:****
En cas de panne du centre de données principal, vous pouvez créer des machines virtuelles s’exécutant sur Azure pour exécuter vos applications critiques, puis les arrêter quand le centre de données principal redevient opérationnel.

#### Migrer vers le cloud avec des machines virtuelles

- ****Lift-and-shift:****
lorsque vous passez d’un serveur physique au cloud, vous pouvez créer une image du serveur et l’héberger dans une machine virtuelle avec peu ou pas de changements.

#### Ressources de machine virtuelle

- ****La taille**** (objet, nombre de coeurs de processeur et quantité de ram)
- ****Les disque de stockage**** (disques durs, SSD, etc.)
- ****Le réseau**** (réseau virtuel, adresse IP publique et configuration de port)

### Décrire Azure Virtual Desktop

#### Améliorer la sécurité

Azure Virtual Desktop est un service de virtualisation des postes de travail et des applications qui s'exécute dans le cloud. Il  fournit une gestion centralisée de la sécurité pour les bureaux des utilisateurs par le biais d’Azure AD (Azure Active Directory) et utilisant comme exemple l’authentification multifacteur pour sécuriser les connexions et l’accès aux données en affectant de manière précise des contrôles d’accès en fonction du rôle (RBAC) aux utilisateurs.

Le bureau et les applications proprement dits s’exécutant dans le cloud, les données se trouvent aussi séparées du matériel local.

#### Déploiement de Windows 10 ou Windows 11 multisession

Azure Virtual Desktop vous permet d’utiliser Windows 10 ou Windows 11 Entreprise multisession, le seul système d’exploitation basé sur le client Windows qui permet à plusieurs utilisateurs d’accéder simultanément à une même machine virtuelle.

### Décrire les conteneurs

Les conteneurs constituent un excellent choix si vous souhaitez exécuter plusieurs instances d’une application sur une même machine hôte.

#### Qu'est-ce que les conteneurs

Les conteneurs constituent un environnement de virtualisation. Vous pouvez exécuter plusieurs conteneurs sur un seul hôte physique ou virtuel. Ils sont sont légers et conçus pour être créés, mis à l’échelle (scale-out) et arrêtés de façon dynamique, ils s’avèrent être une méthode plus légère et plus agile.

- Permet de répondre aux modifications à la demande.
- Possibilité de redémarrer rapidement en cas d'incident ou d'interruption matérielle.
- Moteurs Dockers pris en charge par Azure.

#### Azure Container Instances

Azure Container Instances est une offre PaaS (Platform as a Service) et vous permet de charger vos conteneurs, le service exécute alors les conteneurs à votre place.

#### Utiliser des conteneurs dans vos solutions

****Avantages****

- Souvent utilisés pour créer des solutions avec architecture de microservices.
- Divisez vos solutions en structures plus petites et indépendantes.
- Permet de séparer des parties de votre application en sections logiques qui peuvent être gérées, mises à l’échelle ou mises à jour séparément.

### Décrire Azure Functions

Azure Functions est une option de calcul serverless pilotée par les événements qui ne demande pas de maintenance au niveau des machines virtuelles ou des conteneurs. Un événement déclenche la fonction, ce qui limite la nécessité de garder des ressources provisionnées quand il n’y a pas d’événements.

****Avantages****

- Idéal quand votre seule préoccupation est le code qui exécute votre service et non la plateforme ou l’infrastructure sous-jacentes.
- Se met à l’échelle automatiquement en fonction de la demande.
- Exécute votre code quand il est déclenché et libère automatiquement les ressources lorsque la fonction est terminée.
- Peuvent être sans état (par défaut) pour se comporter comme si elles étaient redémarrées chaque fois ou avec état (Durable Function) lorsqu'un contexte est transmis via la fonction pour effectuer le suivi de l’activité précédente.
- Une plateforme de calcul générale permettant d’exécuter n’importe quel type de code.

### Décrire les options d'hébergement d'applications

#### Azure App Service

App Service vous permet de créer et d’héberger des applications web, des tâches en arrière-plan, des back-ends mobiles et des API RESTful dans le langage de programmation de votre choix, sans devoir gérer l’infrastructure.

****Avantages****

- Offre une mise à l’échelle automatique et une haute disponibilité.
- Prise en charge Windows et Linux.
- Permet des déploiements automatisés à partir de GitHub, Azure DevOps ou n’importe quel dépôt Git (CI/CD).
- Prend en charge plusieurs langages, dont .NET, .NET Core, Java, Ruby, Node.js, PHP ou Python.
- Le déploiement et la gestion sont intégrés à la plateforme.
- Les points de terminaison peuvent être sécurisés.
- Les sites peuvent être mis à l’échelle rapidement afin de gérer des charges de trafic élevées.
- L’équilibrage de charge intégré et Traffic Manager offrent une haute disponibilité.

****Types de services d'application****

- ****Applications web:**** prise en charge complète de l’hébergement d’applications web avec ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP ou Python que ce soit sous Windows ou Linux.
- ****Applications API:**** vous pouvez générer des API web REST en utilisant le langage et l’infrastructure de votre choix, incluant la prise en charge complète de Swagger, vous pouvez empaqueter et publier votre API sur la Place de marché Azure.
- ****Webjobs:**** pour exécuter un programme (.exe, Java, PHP, Python ou Node.js) ou un script (.cmd, .bat, PowerShell ou Bash) dans le même contexte qu’une application web, une application API ou une application mobile.
- ****Applications mobiles:**** la fonctionnalité Mobile Apps d’App Service pour créer rapidement un back-end pour les applications iOS et Android tel que:
    - Stocker les données d’application mobile dans une base de données SQL basée sur le cloud.
  - Authentifier les clients par rapport à des fournisseurs de réseaux sociaux courants comme MSA, Google, Twitter et Facebook.
  - Envoyer des notifications Push.
  - Exécuter une logique de back-end personnalisée en C# ou Node.js.

> Du côté de l’application mobile, vous disposez de la prise en charge des SDK pour les applications natives iOS et Android, Xamarin et React.

### Décrire Azure Virtual Network

Les réseaux virtuels et les sous-réseaux virtuels Azure permettent à des ressources Azure de communiquer entre elles, avec des utilisateurs sur Internet et des ordinateurs clients locaux.

****Fonctionnalités****

- ****L’isolement et la segmentation:****

- ****Les communications Internet:****
possibilité d'activer les connexions entrantes depuis Internet en attribuant une adresse IP publique à une ressource Azure ou en plaçant la ressource derrière un équilibreur de charge public.
- ****Communiquer entre des ressources Azure:****
Il existe deux méthodes permettant aux ressources Azure de communiquer entre elles en toute sécurité
  - Les réseaux virtuels
  - Les points de terminaison de service
- ****Communiquer avec des ressources locales:**** lier des ressources ensemble dans votre environnement local et au sein de votre abonnement Azure via trois mécanisme
  - Les connexions de réseau privé virtuel point à site (ordinateur extérieur à votre réseau d’entreprise).
  - Les réseaux privés virtuels de site à site (un appareil VPN local ou votre passerelle à la passerelle VPN Azure sur un réseau virtuel).
  - Azure ExpressRoute (connectivité privée dédiée vers Azure qui ne passe pas par Internet).

- ****Router le trafic:**** par défaut, Azure achemine le trafic entre les sous-réseaux sur tous les réseaux virtuels connectés, les réseaux locaux et Internet. Il est aussi possible de contrôler le routage et remplacer les paramètres
  - Les tables de routage
  - Le protocole BGP

- ****Filtrer le trafic:****
possiblité de filter le traffic entre des sous-réseaux à l'aide des approches
  - Les groupes de sécurité réseau (peuvent contenir plusieurs règles de sécurité d’entrée et de sortie).
  - Les appliances virtuelles réseau (machines virtuelles spécialisées remplissant une fonction réseau particulière, comme exécuter un pare-feu ou effectuer une optimisation WAN).

- ****Connecter des réseaux virtuels:****
le peering permet à deux réseaux virtuels de se connecter directement entre eux. Le trafic réseau échangé entre réseaux appairés est privé et transite par le réseau principal Microsoft, sans jamais entrer sur l’Internet public.

    > Les routes définies par l’utilisateur (UDR) vous permettent de contrôler les tables de routage entre les sous-réseaux d’un réseau virtuel ou entre les réseaux virtuels.

Prend en charge les points de terminaison publics et privés pour permettre la communication entre des ressources externes ou internes et d’autres ressources internes.

- ****Les points de terminaison publics:**** ont une adresse IP publique et sont accessibles partout dans le monde.
- ****Les points de terminaison privés:**** existent au sein d’un réseau virtuel et ont une adresse IP privée comprise dans l’espace d’adressage de ce réseau virtuel.

### Décrire les réseaux privés virtuels

Les VPN sont généralement déployés pour connecter plusieurs réseaux privés approuvés via un réseau non approuvé (en général l’Internet public). Les VPN peuvent permettre à des réseaux de partager de manière sûre et sécurisée des informations sensibles.

#### Passerelles VPN

Les instances Passerelle VPN Azure sont déployées dans un sous-réseau dédié du réseau virtuel et assurent la connectivité suivante :

- Connecter des centres de données locaux à des réseaux virtuels par le biais d’une connexion site à site.
- Connecter des appareils individuels à des réseaux virtuels par le biais d’une connexion point à site.
- Connecter des réseaux virtuels à d’autres réseaux virtuels par le biais d’une connexion réseau à réseau.

> Vous pouvez déployer une seule passerelle VPN dans chaque réseau virtuel. En revanche, vous pouvez utiliser une même passerelle pour vous connecter à plusieurs emplacements.

Il existe deux type de passerelles VPN, soit:

- Les passerelles VPN basées sur une stratégie spécifient de manière statique l’adresse IP des paquets qui doivent être chiffrés via chaque tunnel.
- Dans les passerelles basées sur une route, les tunnels IPSec sont modélisés sous forme d’interface réseau ou d’interface de tunnel virtuel. Le routage IP détermine quelle interface de tunnel utiliser pour envoyer chaque paquet. Elles sont recommandées pour:
  - Connexion entre réseaux virtuels
  - Connexions point à site
  - Connexions multisites
  - Coexistence avec une passerelle Azure ExpressRoute

#### Scénarios de haute disponibilité

****Actif/passif****

Par défaut, les passerelles VPN sont déployées comme deux instances dans une configuration de type actif/passif. Quand une maintenance planifiée ou une interruption non planifiée affecte l’instance active, l’instance de secours prend automatiquement en charge les connexions sans intervention de l’utilisateur.

****Actif/actif****

Avec la prise en charge du protocole de routage BGP, vous pouvez également déployer des passerelles VPN dans une configuration de type actif/actif.

****Basculement ExpressRoute****

Il existe une autre possibilité de haute disponibilité, qui consiste à configurer une passerelle VPN comme un chemin de basculement sécurisé pour les connexions ExpressRoute. Dans les scénarios de haute disponibilité, lorsqu’il existe un risque associé à une défaillance d’un circuit ExpressRoute, vous pouvez également provisionner une passerelle VPN qui utilise Internet comme autre mode de connectivité.

****Passerelles redondantes interzones****

Dans les régions qui prennent en charge les zones de disponibilité, les passerelles VPN et ExpressRoute peuvent être déployées dans une configuration redondante interzone. Ces passerelles ont besoin de différentes références SKU et utilisent des adresses IP publiques Standard au lieu d’adresses IP publiques De base.

### Décrire Azure ExpressRoute
permet d’étendre vos réseaux locaux dans le cloud Microsoft via une connexion privée, avec l’aide d’un fournisseur de connectivité. Chaque emplacement a son propre circuit ExpressRoute. La connectivité peut provenir d’un réseau universel (IP VPN), d’un réseau Ethernet point à point ou d’une interconnexion virtuelle via un fournisseur de connectivité dans un centre de colocalisation.

****Avantages****

- Connectivité aux services de cloud de Microsoft dans toutes les régions de la zone géopolitique.
  - Microsoft Office 365
  - Microsoft Dynamics 365
  - Les services de calcul Azure comme les machines virtuelles Azure
  - Les services cloud Azure comme Azure Cosmos DB et Stockage Azure
- Connectivité globale aux services Microsoft dans toutes les régions grâce à ExpressRoute Global Reach: pour échanger des données entre vos sites locaux en connectant vos circuits ExpressRoute.
- Routage dynamique entre votre réseau et Microsoft via le protocole BGP (Border Gateway Protocol): ce protocole active le routage dynamique entre votre réseau local et les services qui s’exécutent dans le cloud Microsoft.
- Redondance intégrée dans chaque emplacement de peering pour une plus grande fiabilité: chaque fournisseur de connectivité utilise des appareils redondants pour garantir la haute disponibilité des connexions établies avec Microsoft.

#### Modèles de connectivité ExpressRoute

- ****Colocation CloudExchange:****
si votre installation est colocalisée dans un échange cloud, vous pouvez demander une connexion croisée virtuelle au cloud Microsoft.
- ****Connexions Ethernet point à point:****
une connexion ethernet point à point fait référence à l’utilisation d’une connexion point à point pour connecter votre installation au cloud Microsoft.
- ****Connexion universelle:****
avec une connectivité Any-To-Any, vous pouvez intégrer votre réseau étendu (WAN) à Azure en établissant des connexions avec vos bureaux et centres de données.
- ****Directement à partir de sites ExpressRoute:****
offre une double connectivité de 100 Gbits/s ou 10 Gbits/s qui prend en charge la connectivité Active/Active à grande échelle.

#### Considération relatives à la sécurité

ExpressRoute est une connexion privée entre votre infrastructure locale et votre infrastructure Azure. Même si vous disposez d’une connexion ExpressRoute, les requêtes DNS, la vérification de la liste de révocation des certificats et les demandes de réseau de diffusion de contenu sont quand même envoyées via l’Internet public.

### Décrire Azure DNS

Azure DNS est un service d’hébergement pour les domaines DNS qui offre une résolution de noms à l’aide de l’infrastructure Microsoft Azure.

****Avantages****

- ****Fiabilité et performances:****
les domaines DNS sont hébergés sur le réseau global de serveurs de noms DNS d’Azure, offrant résilience et haute disponibilité. Azure DNS utilise la mise en réseau Anycast.
- ****Sécurité:****
basé sur Azure Resource Manager, vous donnant l’accès à des fonctionnalités telles que :
  - Contrôle d’accès en fonction de rôles (Azure RBAC)
  - Journaux d’activité
  - Verrouillage de ressource
- ****Simplicité d’utilisation:****
Azure DNS est intégré au portail Azure et utilise les mêmes informations d’identification, de facturation et de contrat d’assistance que vos autres services Azure. Gestion disponible via:
  - Azure PowerShell
  - Azure CLI
  - Intégrer au service par le biais de l’API REST
  - Kits de développement logiciel (SDK)
- ****Des réseaux virtuels personnalisables:****
Cette fonctionnalité vous permet d’utiliser vos propres noms de domaine personnalisés dans vos réseaux virtuels privés et de ne pas être limité aux noms fournis par Azure.
- ****Enregistrements d’alias:****
Vous pouvez utiliser un jeu d’enregistrements d’alias pour référencer une ressource Azure, comme une adresse IP publique Azure, un profil Azure Traffic Manager ou point de terminaison Azure Content Delivery Network.

> Vous ne pouvez pas utiliser Azure DNS pour acheter un nom de domaine.
