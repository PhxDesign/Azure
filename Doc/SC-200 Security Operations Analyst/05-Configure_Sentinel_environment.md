[//]: # (title: SC-200 Security Operations Analyst - Configure your Microsoft Sentinel environment)
[//]: # (description: Résumé de la formation Azure Fundamentals)
[//]: # (author: PhxDesign)
[//]: # (ms.author: jlgauthier)
[//]: # (ms.topic: Configure your Microsoft Sentinel environment)
[//]: # (ms.date: 01/14/2023)

# SC-200 Security Operations Analyst - Configure your Microsoft Sentinel environment

Microsoft Learn training digest to take the SC-200 Security Operations Analyst exam.

## Introduction to Microsoft Sentinel

### What is Microsoft Sentinel

#### What's a SIEM

It's is a tool that an organization uses to collect, analyze, and perform security operations on its computer systems.

****Enables you to****

- Collect and query logs.
- Do some form of correlation or anomaly detection.
- Create alerts and incidents based on your findings.

****Potential functionalities****

- Log management
- Alerting
- Visualization
- Incident management
- Querying data

#### What is Microsoft Sentinel?

It's a cloud-native SIEM that a SOT can use for:

- Get security insights across the enterprise by collecting data from virtually any source.
- Detect and investigate threats quickly by using built-in machine learning and Microsoft threat intelligence.
- Automate threat responses by using playbooks and by integrating Azure Logic Apps.

IT helps you enable end-to-end security operations including collection, detection, investigation, and response:

|Collect|Detect|Investigate|Respond|
|-|-|-|-|
|Visibility|Analytics, Hunting|Incidents|Automation|
|

### How Microsoft Sentinel works

#### Data connectors

Microsoft Sentinel ingests information from data connectors linked to services like

- syslog
- Common Event Format (CEF)
- Trusted Automated eXchange of Indicator Information (TAXII) (for threat intelligence)
- Azure
- AWS services

#### Log retention

Your data is stored by using Log Analytics and include the ability to use the Kusto Query Language (KQL), that's a rich query language that gives you the power to dive into and gain insights from our data.

#### Workbooks

Think of workbooks as dashboards which each component is built by using an underlying KQL query of your data.

#### Analytics alerts

You can enable built-in analytics alerts within your Sentinel workspace, you can edit to your own needs or also create custom, scheduled alerts from scratch.

#### Threat hunting

There are some built-in hunting queries that SOC analysts can use and they can also create their. It also integrates with Azure Notebooks and provides example notebooks for advanced hunters.

#### Incidents and Investigations

An incident is created when an alert that you've enabled is triggered. you can do standard incident management tasks like changing status or assigning incidents to individuals for investigation and you can visually investigate incidents by mapping entities across log data along a timeline.

#### Automation Playbooks

You can automate some of your security operations and make your SOC more productive. Sentinel integrates with Azure Logic Apps, enabling you to create automated workflows, or playbooks, in response to events. These capabilities are often referred to as a security orchestration, automation, and response (SOAR).

****Possibilities****

- Ingest data from your cloud and on-premise environments.
- Perform analytics on that data.
- Manage and investigate any incidents that occur.
- Perhaps even respond automatically by using playbooks.

### When to use Microsoft Sentinel

If you want to:

- Collect event data from various sources.
- Perform security operations on that data to identify suspicious activity.

Operations could include:

- Visualization of log data.
- Anomaly detection.
- Threat hunting.
- Security incident investigation.
- Automated response to alerts and incidents.

Other capabilities...

- Cloud-native SIEM. There are no servers to provision, so scaling is effortless.
- Integration with the Azure Logic Apps service and its hundreds of connectors.
- Benefits of Microsoft research and machine learning.
- Key log sources provided for free.
- Support for hybrid cloud and on-premise environments.
- SIEM and a data lake all in one.

Clear requirements from the organization:

- Support for data from multiple cloud environments.
- Features and functionality required for a security operations center (SOC), without too much administrative overhead.

> If you're collecting infrastructure or application logs for performance monitoring, also consider using Azure Monitor and Log Analytics for that purpose.

### Knowledge check

- What does Microsoft Sentinel provide?
  - An end-to-end solution for security operations
- Which language is used to query data within Microsoft Sentinel?
  - KQL
- Which Azure service stores the log data that is ingested into Microsoft Sentinel?
  - Log Analytics
- Within Microsoft Sentinel, which Azure product is used to run automated playbooks in response to alerts?
  - Azure Logic Apps

## Create and manage Microsoft Sentinel workspaces

### Plan for the Microsoft Sentinel workspace

#### Implementation options

****Single-Tenant with a single Microsoft Sentinel Workspace****

Receives logs from resources in other regions within the same tenant.

|Pros|Cons|
|------|------|
|Central Pane of Glass|May not meet Data Governance Requirements|
|Consolidates all security logs and information|Can incur bandwidth cost for cross region|
|Easier to query all information|
|Azure Log Analytics RBAC to control data access|
|Microsoft Sentinel RBAC for service RBAC|
|

****Single-Tenant with regional Microsoft Sentinel Workspaces****

Will have multiple Sentinel workspaces requiring the creation and configuration of multiple Microsoft Sentinel and Log Analytics workspaces.

|Pros|Cons|
|----|----|
|No cross-region bandwidth costs|No central pane of glass. You aren't looking in one place to see all the data.|
|May be required to meet Data Governance requirements|Analytics, Workbooks, etc. must be deployed multiple times.|
|Granular data access control|
|Granular retention settings|
|Split billing|
|

> To query data across workspaces, use the workspace() function before the table name, ex:

~~~kql
    Tablename
    | union workspace("WorkspaceName").TableName
~~~

****Multi-Tenant****

You implement Microsoft Sentinel workspace in multiple tenant using Azure Lighthouse.

> Use the same workspace for both Microsoft Sentinel and Microsoft Defender for Cloud, so that all logs collected by Microsoft Defender for Cloud can also be ingested and used by Microsoft Sentinel.

### Create a Microsoft Sentinel workspace

****Requiers****

- To enable: contributor permission to the subscription in which the Microsoft Sentinel workspace resides.
- To use: need either contributor or reader permission on the resource group that the workspace belongs.

#### Create and configure a Log Analytics workspace

****Add Microsoft Sentinel to a workspace****

Need a Log Analytics Workspace and you can create one when adding Microsoft Sentiel. The LAW requires

- A subscription
- A resource group
- A name (shared between Log Analytics and Sentinel)
- A region

> The Region is the location where ingested data is stored. The data location impacts data governance requirements and can't be moved from region to region.

Once the LAW selected, just add the Microsoft Sentinel Solution and the active screen will show you a panel with:

- General
- Threat management
- Content management
- Configuration

> The most common scenario is sharing the Log Analytics workspace used by Microsoft Defender for Cloud. Sharing the workspace enables one central workspace to query security data.

### Manage workspaces across tenants using Azure Lighthouse

Azure Lighthouse allows greater flexibility to manage resources for multiple customers without having to sign in to different accounts in different tenants. Azure Lighthouse allows greater flexibility to manage resources for multiple customers without having to sign in to different accounts in different tenants.

### Understand Microsoft Sentinel permission and roles

Use Azure RBAC to create and assign roles within your security operations team to grant appropriate access to Microsoft Sentinel. Roles can be assigned in the Microsoft Sentinel workspace directly, or in a subscription or resource group that the workspace belongs to.

#### Microsoft Sentinel-specific roles

For best results, these roles should be assigned to the resource group that contains the Microsoft Sentinel workspace.

- ****Microsoft Sentinel Reader:**** can view data, incidents, workbooks, and other Microsoft Sentinel resources.
- ****Microsoft Sentinel Responder:**** can, in addition to the above, manage incidents (assign, dismiss, etc.).
- ****Microsoft Sentinel Contributor:**** can, in addition to the above, create and edit workbooks, analytics rules, and other Microsoft Sentinel resources.
- ****Microsoft Sentinel Automation Contributor:**** allows Microsoft Sentinel to add playbooks to automation rules
    > MSAC role isn't meant for user accounts.

#### Additional roles and permission

- ****Working with playbooks to automate responses to threats:**** You can use the Logic App Contributor role to assign explicit permission for using playbooks.
- ****Giving Microsoft Sentinel permission to run playbooks:**** this account must be granted explicit permission to the resource group where the playbook resides. To grant these permissions to this service account, your account must have Owner permission on the resource groups containing the playbooks.
- ****Connecting data sources to Microsoft Sentinel:**** you must assign the user write permission on the Microsoft Sentinel workspace.
- ****Guest users assigning incidents:**** in addition to the Microsoft Sentinel Responder role, the user will also need to be assigned the role of Directory Reader.
- ****Creating and deleting workbooks:**** the user requires either the Microsoft Sentinel Contributor role or a lesser Microsoft Sentinel role plus the Azure Monitor role of Workbook Contributor.

#### Azure roles and Azure Monitor Log Analytics roles

These roles include access to your Microsoft Sentinel workspace and other resources:

- Owner
- Contributor
- Reader

Log Analytics roles grant access across all your Log Analytics workspaces:

- Log Analytics Contributor
- Log Analytics Reader

#### Custom roles and advanced Azure RBAC

You can create your own custom roles. Just like built-in roles, you can assign custom roles to users, groups, and service principals.

### Manage Microsoft Sentinel settings

Environment Settings are managed in two areas, in Microsoft Sentinel (Pricing, Settings) and in the Log Analytics workspace where Microsoft Sentinel resides and where most of the settings  are managed.

#### Configure log retention

Data retention at the workspace level can be configured from 30 to 730 days (two years) for all workspaces unless they're using the legacy Free pricing tier.

> You can adjust the retention days for a table through the workspace settings in the Microsoft Sentinel Settings area.

#### Configure logs

Data in each table in a Log Analytics workspace is retained for a specified period of time after which it's either removed or archived with a reduced retention fee.

****Log types****

- Analytics Logs: By default, all tables in a workspace are of type Analytics Logs, which are available to all features of a Log Analytics workspace
- Basic Logs: only retained for 8 days, you can configure certain tables as Basic Logs to reduce the cost of storing high-volume verbose logs you use for debugging, troubleshooting and auditing.
- Archive Logs: when you no longer use the logs, but still need to keep the data for compliance or occasional investigation, archive the logs to save costs.

#### KQL language limits

Queries against Basic Logs include operators:

- where
- extend
- project
- project-away
- project-keep
- project-rename
- project-reorder
- parse
- parse-where

But not:

- join
- union
- aggregates (summarize)

#### Table support Basic Logs

You can configure particular tables to use Basic Logs. You can't configure a table for Basic Logs if Azure Monitor relies on that table for specific features.

- All tables created with the Data Collection Rule (DCR)-based custom logs API.
- ContainerLogV2, which Container Insights uses and which include verbose text-based log records.
- AppTraces, which contain freeform log records for application traces in Application Insights.

### Knowledge check

- Where is your log data stored?
  - Log Analytics workspace
- Which Microsoft Sentinel security role can create workbooks?
  - Microsoft Sentinel Contributor
- Why is it important to set the region when creating the Log Analytics workspace?
  - Specifies where the log data will be stored.

## Query logs in Microsoft Sentinel

### Query logs in the logs page

KQL is the language used to query the log data in the Log Analytics workspace. The query window allows you to run queries, save queries, run saved queries, create a new alert rule, and export.

### Understand Microsoft Sentinel tables

The primary tables to manage alerts and incidents are SecurityAlert and SecurityIncident.

|Table|Description|
|------|------|
|SecurityAlert|Contains Alerts Generated from Sentinel Analytical Rules. Also, it could include Alerts created directly from a Sentinel Data Connector|
|SecurityIncident|Alerts can generate Incidents. Incidents are related to Alert(s).|
|ThreatIntelligenceIndicator|Contains user-created or data connector ingested Indicators such as File Hashes, IP Addresses, Domains|
|Watchlist|A Microsoft Sentinel watchlist contains imported data.|
|

### Understand common tables

|Table| Description|
|------|------|
AzureActivity| Entries from the Azure Activity log that provide insight into any subscription-level or management group-level events that have occurred in Azure.
AzureDiagnostics| Stores resource logs for Azure services that use Azure Diagnostics mode. Resource logs describe the internal operation of Azure resources.
AuditLogs| Audit log for Azure Active Directory. Includes system activity information about user and group management, managed applications, and directory activities.
CommonSecurityLog| Syslog messages using the Common Event Format (CEF).
McasShadowItReporting| Microsoft Cloud App Security logs
OfficeActivity| Audit logs for Office 365 tenants collected by Microsoft Sentinel. Including Exchange, SharePoint and Teams logs.
SecurityEvent| Security events collected from windows machines by Azure Security Center or Microsoft Sentinel
SigninLogs| Azure Activity Directory Sign-in logs
Syslog| Syslog events on Linux computers using the Log Analytics agent.
Event| Sysmon Events collected from a Windows host.
WindowsFirewall| Windows Firewall Events
|

### Understand Microsoft 365 Defender tables

|Table name| Description|
|------|------|
AlertEvidence| Files, IP addresses, URLs, users, or devices associated with alerts
CloudAppEvents| Events involving accounts and objects in Office 365 and other cloud apps and services
DeviceEvents| Multiple event types, including events triggered by security controls such as Windows Defender Antivirus and exploit protection
DeviceFileCertificateInfo| Certificate information of signed files obtained from certificate verification events on endpoints
DeviceFileEvents| File creation, modification, and other file system events
DeviceImageLoadEvents| DLL loading events
DeviceInfo| Machine information, including OS information
DeviceLogonEvents| Sign-ins and other authentication events on devices
DeviceNetworkEvents| Network connection and related events
DeviceNetworkInfo| Network properties of devices, including physical adapters, IP and MAC addresses, as well as connected networks and domains
DeviceProcessEvents| Process creation and related events
DeviceRegistryEvents| Creation and modification of registry entries
EmailEvents| Microsoft 365 email events, including email delivery and blocking events
EmailPostDeliveryEvents| Security events that occur post-delivery, after Microsoft 365 has delivered the emails to the recipient mailbox
EmailUrlInfo| Information about URLs on emails
EmailAttachmentInfo| Information about files attached to Office 365 emails
IdentityDirectoryEvents| Events involving an on-premise domain controller running Active Directory (AD). This table covers a range of identity-related events and system events on the domain controller.
IdentityLogonEvents| Authentication events on Active Directory and Microsoft online services
IdentityQueryEvents| Queries for Active Directory objects, such as users, groups, devices, and domains
|

<details><summary><b>Knowledge check</b></summary>
1. Which table stores Defender for Endpoint logon events?
    <details><summary>Answer</summary>
    DeviceLogonEvents
    </details>
2. What table contains logs from Windows hosts collected directly to Microsoft Sentinel?
    <details><summary>Answer</summary>
    SecurityEvent
    </details>
3. Which table stores Alerts from Microsoft Defender for Endpoint?
    <details><summary>Answer</summary>
    SecurityAlert
    </details>
</details>

## Use watchlists in Microsoft Sentinel

Microsoft Sentinel watchlists enable collecting data from external data sources for correlation with the events in your Microsoft Sentinel environment. Watchlists are stored in your Microsoft Sentinel workspace as name-value pairs and are cached for optimal query performance and low latency.

### Plan for watchlists

****Common scenarios for using watchlists****

- Investigating threats and responding to incidents quickly with the rapid import of IP addresses, file hashes, and other data from CSV files.
- Importing business data as a watchlist.
- Reducing alert fatigue, like creating allowlists to suppress alerts from a group of users, such as users from authorized IP addresses that perform tasks that would normally trigger the alert
- Enriching event data with name-value combinations derived from external data sources.

### Create a watchlist

To use the watchlist data in KQL, use the KQL function _GetWatchlist('watchlist name').

> File uploads are currently limited to files of up to 3.8 MB in size.

### Manage watchlists

We recommend you edit an existing watchlist instead of deleting and recreating a watchlist, has Log analytics has a five-minute SLA for data ingestion.

- Edit a watchlist to edit or add an item to the watchlist.
- Bulk update of a watchlist appends items to the existing watchlist. Then, it de-duplicates the items in the watchlist where all the value in each column match.

    > If you've deleted an item from your watchlist file and upload it, bulk update won't delete the item in the existing watchlist. Delete the watchlist item individually. Or, when you have many deletions, delete and recreate the watchlist.

<details><summary><b>Knowledge check</b></summary>
1. Which of the following operations is a typical scenario for using a Microsoft Sentinel watchlist??
    <details><summary>Answer</summary>
    Responding to incidents quickly with the rapid import of IP addresses.
    </details>
2. How do you access a new watchlist named MyList in KQL??
    <details><summary>Answer</summary>
    _GetWatchlist('MyList')
    </details>
</details>

## Utilize threat intelligence in Microsoft Sentinel

### Define threat intelligence

The most utilized CTI in SIEM solutions like Microsoft Sentinel is threat indicator data, sometimes called Indicators of Compromise (IoCs). Threat indicators, considered as tactical, associate URLs, file hashes, IP addresses, and other data with known threat activity like phishing, botnets, or malware.

****You can integrate threat intelligence (TI)****

- Use Data connectors to various TI platforms to import threat intelligence into Microsoft Sentinel.
- View and manage the imported threat intelligence in Logs and the new Threat Intelligence area of Microsoft Sentinel.
- Use the built-in Analytics rule templates to generate security alerts and incidents using your imported threat intelligence.
- Visualize critical information about your threat intelligence in Microsoft Sentinel with the Threat Intelligence workbook.
- Perform threat hunting with your imported threat intelligence.

[Sentinel Data connectors](images/05-CSE-Sentinel_data_connectors.png)

### Manage your threat indicators

With the Threat Intelligence area you can also view, sort, filter, and search your imported threat indicators without even writing a Logs query. These tasks include indicator tagging and creating new indicators related to security investigations.

Tagging threat indicators is an easy way to group them to make them easier to find. You can tag threat indicators individually or multi-select indicators and tag them all at once. Since tagging is free-form, a recommended practice is to create standard naming conventions for threat indicator tags.

### View your threat indicators with KQL

The indicators reside in the ThreatIntelligenceIndicator table.

To view your threat indicators with KQL. Select Logs from the General section of the Microsoft Sentinel menu. Then run a query on the ThreatIntelligenceIndicator table.

~~~kql
ThreatIntelligenceIndicator
~~~

<details><summary><b>Knowledge check</b></summary>
1. In Threat Intelligence, indicators are considered as which of the following?
    <details><summary>Answer</summary>
    Tactical
    </details>
2. Which of these items is an example of a Threat indicator?
    <details><summary>Answer</summary>
    Domain Name
    </details>
3. What table do you query in KQL to view your indicators?
    <details><summary>Answer</summary>
    ThreatIntelligenceIndicator
    </details>
</details>
