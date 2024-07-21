# TASK1: INTRODUCTION
```
Learning Objectives

    Understand components and functions of a red team engagement.
    Learn how to properly plan an engagement based of needs and resources available and TTPs. 
    Understand how to write engagement documentation in accordance to client objectives.
```
# TASK2: Definig Scope and Objectives
```
Example 1 - Global Enterprises:

Objectives:

    Identify system misconfigurations and network weaknesses.
        Focus on exterior systems.
    Determine the effectiveness of endpoint detection and response systems.
    Evaluate overall security posture and response.
        SIEM and detection measures.
        Remediation.
        Segmentation of DMZ and internal servers.
    Use of white cards is permitted depending on downtime and length.
    Evaluate the impact of data exposure and exfiltration.

Scope:

    System downtime is not permitted under any circumstances.
        Any form of DDoS or DoS is prohibited.
        Use of any harmful malware is prohibited; this includes ransomware and other variations.
    Exfiltration of PII is prohibited. Use arbitrary exfiltration data.
    Attacks against systems within 10.0.4.0/22 are permitted.
    Attacks against systems within 10.0.12.0/22 are prohibited.
    Bean Enterprises will closely monitor interactions with the DMZ and critical/production systems.
        Any interaction with "*.bethechange.xyz" is prohibited.
        All interaction with "*.globalenterprises.thm" is permitted.


What CIDR range is permitted to be attacked?
10.0.4.0/22

Is the use of white cards permitted? (Y/N)
y

Are you permitted to access "*.bethechange.xyz?" (Y/N)
n
```
# TASK3: Rules of Engagement
```
https://redteam.guide/docs/templates/roe_template/

Once downloaded, read the sample document and answer the questions below.
N/A

How many explicit restriction are specified?
3

What is the first access type mentioned in the document?
phishing

Is the red team permitted to attack 192.168.1.0/24? (Y/N)
N
```
# TASK4: Campaing Planning
```
https://redteam.guide/docs/checklists/red-team-checklist/

Read the above and move on to engagement documentation. 
N/A
```
# TASK5: Engagement Documentation
```
Engagement documentation is an extension of campaign planning where ideas and thoughts of campaign planning are officially documented. In this context, the term "document" can be deceiving as some plans do not require proper documentation and can be as simple as an email; this will be covered later in this task.

In this task, we will cover a technical overview of the contents of each campaign plan prior to looking at the plans and documents themselves in upcoming tasks.

Engagement Plan:
Component	Purpose
CONOPS (Concept of Operations)
	Non-technically written overview of how the red team meets client objectives and target the client.
Resource plan
	Includes timelines and information required for the red team to be successful—any resource requirements: personnel, hardware, cloud requirements.

Operations Plan:
Component	Purpose
Personnel 
	Information on employee requirements.
Stopping conditions
	How and why should the red team stop during the engagement.
RoE (optional)
	-
Technical requirements
	What knowledge will the red team need to be successful.

Mission Plan:
Component	Purpose
Command playbooks (optional)
	Exact commands and tools to run, including when, why, and how. Commonly seen in larger teams with many operators at varying skill levels.
Execution times
	Times to begin stages of engagement. Can optionally include exact times to execute tools and commands.
Responsibilities/roles
	Who does what, when.

Remediation Plan (optional):
Component	Purpose
Report
	Summary of engagement details and report of findings.
Remediation/consultation 
	How will the client remediate findings? It can be included in the report or discussed in a meeting between the client and the red team.
```
# TASK6: Concept of Operations
```
Based on customer security posture and maturity, the TTP of the threat group: FIN6, will be employed throughout the engagement.


How long will the engagement last?
1 month

How long is the red cell expected to maintain persistence?
1 week

What is the primary tool used within the engagement?
Cobalt Strike
```
# TASK7: Resource Plan
```

Navigate to the "View Site"  button and read the provided resource plan. Once complete, answer the questions below.

When will the engagement end? (MM/DD/YYYY)
11/14/2021

What is the budget the red team has for AWS cloud cost?
$1000

Are there any miscellaneous requirements for the engagement? (Y/N)
n
```
# TASK8: Operation Plan
```
What phishing method will be employed during the initial access phase?
spearphishing

What site will be utilized for communication between the client and red cell?
vectr.io

If there is a system outage, the red cell will continue with the engagement. (T/F)
F
```
# TASK9: Mission Plan
```
 Navigate to the "View Site"  button and read the provided mission plan. Once complete, answer the questions below.

When will the phishing campaign end? (mm/dd/yyyy)
10/23/2021

Are you permitted to attack 10.10.6.78? (Y/N)
N

When a stopping condition is encountered, you should continue working and determine the solution yourself without a team lead. (T/F)
F
```
# TASK10: Conclusion
```


We have covered how you can quantify campaign plans into documents and prepare for a successful red team engagement in this room. The consistent theme throughout this room has been that each red team will have its internal documents and way of doing things. This is a crucial concept to understand when moving into the real world. This room only acts as a guide to get you used to concepts and ideas and provides a framework to use, not as a definitive step-by-step manual. When planning an engagement, remember that your number 1 goal is to meet the client's objectives.

Planning and documenting are often overlooked and are crucial to a successful engagement.

```