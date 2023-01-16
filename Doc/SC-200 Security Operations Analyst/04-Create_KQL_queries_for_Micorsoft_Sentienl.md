[//]: # (title: SC-200 Security Operations Analyst - Create queries for Microsoft Sentinel using Kusto Query Language)
[//]: # (description: Résumé de la formation Azure Fundamentals)
[//]: # (author: PhxDesign)
[//]: # (ms.author: jlgauthier)
[//]: # (ms.topic: Create queries for Microsoft Sentinel using Kusto Query Language)
[//]: # (ms.date: 01/14/2023)

# SC-200 Security Operations Analyst - Create queries for Microsoft Sentinel using Kusto Query Language

## Construct KQL statements for Microsoft Sentinel

Kusto Query Language (KQL) is the query language used to perform analysis on data to create Analytics, Workbooks, and perform Hunting in Microsoft Sentinel.

### Understand the Kusto Query Language statement structure

A KQL query is a read-only request to process data and return results. The query uses schema entities organized in a hierarchy similar to SQL's: databases, tables, and columns.

The query consists of a sequence of query statements. At least one statement is a tabular expression statement that produces data arranged in a table-like mesh of columns and rows.

For example, the statement starts with a table called SecurityEvent. The EventID column's value filters the data (rows) and then the results are summarized by creating a new column for the count() by Account. Next, in the Prepare phase, the results are then limited to 10 rows.

    [Query example](images/04-CKQMS-KQL_Query.png)

### Operators

- search: The search operator provides a multi-table/multi-column search experience. Although the search operator is easy to use, when compared to the where operator it's inefficient.

    ~~~kql
    search "err"
    search in (SecurityEvent,SecurityAlert,A*) "err"
    ~~~

- where: filters a table to the subset of rows that satisfy a predicate.

    ~~~kql
    SecurityEvent

    | where TimeGenerated > ago(1d)

    SecurityEvent
    | where TimeGenerated > ago(1h) and EventID == "4624"

    SecurityEvent
    | where TimeGenerated > ago(1h)
    | where EventID == 4624
    | where AccountType =~ "user"

    SecurityEvent | where EventID in (4624, 4625)
    ~~~

- let: bind names to expressions. For the rest of the scope, where the let statement appear, the name refers to its bound value.
  - Allow for the creation of variables to be used in later statements.

    ~~~kql
    let timeOffset = 7d;

    let discardEventId = 4688;

    SecurityEvent
    | where TimeGenerated > ago(timeOffset*2) and TimeGenerated < ago(timeOffset)
    | where EventID != discardEventId
    ~~~

  - Allow for the creation of dynamic tables or lists.

    ~~~kql
    let suspiciousAccounts = datatable(account: string) [
    @"\administrator",
    @"NT AUTHORITY\SYSTEM"

    ];
    SecurityEvent | where Account in (suspiciousAccounts)
    ~~~

- extend: create calculated columns and append the new columns to the result set.

    ~~~kql
    SecurityEvent
    | where ProcessName != "" and Process != ""
    | extend StartDir =  substring(ProcessName,0, string_size(ProcessName)-string_size(Process))
    ~~~

- order by: Sort the rows of the input table by one or more columns.

    ~~~kql
    SecurityEvent
    | where ProcessName != "" and Process != ""
    | extend StartDir =  substring(ProcessName,0, string_size(ProcessName)-string_size(Process))
    | order by StartDir desc, Process asc
    ~~~

- project: control what columns to include, add, remove, or rename in the result set of a statement.
    |Operator|Description|
    project|Select the columns to include, rename or drop, and insert new computed columns.
    project-away|Select what columns from the input to exclude from the output.
    project-keep|Select what columns from the input to keep in the output.
    project-rename|Select the columns to rename in the resulting output.
    project-reorder|Set the column order in the resulting output.
    |

    > The project operator will limit the size of the result set, which will increase performance.

    ~~~kql
    SecurityEvent
    | project Computer, Account

    SecurityEvent
    | where ProcessName != "" and Process != ""
    | extend StartDir =  substring(ProcessName,0, string_size(ProcessName)-string_size(Process))
    | order by StartDir desc, Process asc
    | project Process, StartDir
    ~~~

    ~~~kql
    SecurityEvent
    | where ProcessName != "" and Process != ""
    | extend StartDir =  substring(ProcessName,0, string_size(ProcessName)-string_size(Process))
    | order by StartDir desc, Process asc
    | project-away ProcessName
    ~~~

<details><summary><b>Knowledge check</b></summary>
1. What does the search operator do?
    <details><summary>Answer</summary>
    Searches across tables and isn't column-specific.
    </details>
2. What are project operators?
    <details><summary>Answer</summary>
    Project operators add, remove, or rename columns in a result set.
    </details>
</details>

## Analyze query results using KQL

## Build multi-table statements using KQL

## Work with data in Microsoft Sentinel using Kusto Query Language
