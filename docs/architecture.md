**PathGuard Architecture**



**Project Name**

*PathGuard*



**Problem Statement**

* Cloud infrastructure changes frequently introduce network failures or security exposure due to misconfigured routes, security policies, or connectivity assumptions.
* Manual review of infrastructure changes is often insufficient to detect the operational impact of network configuration modifications before deployment.
* PathGuard aims to analyze infrastructure changes before deployment and identify potential connectivity failures, routing conflicts, and unintended exposure risks.



*Objective*

Provide automated validation of cloud network changes prior to deployment by evaluating the impact of configuration modifications on connectivity paths and security boundaries.



*System Inputs*

\- infrastructure configuration changes

\- current cloud network state

\- network policy definitions

\- declared critical connectivity paths



*System Outputs*

\- connectivity impact analysis

\- network policy violation detection

\- predicted exposure changes

\- risk evaluation of proposed changes

\- structured validation report



*Core Components*

\- change ingestion module

\- cloud state collector

\- topology modeling engine

\- connectivity evaluation engine

\- policy validation engine

\- risk scoring module

\- reporting interface



*High Level Workflow*

1\. proposed infrastructure change is submitted

2\. system retrieves current cloud network state

3\. topology model is generated

4\. connectivity evaluation is executed

5\. policy validation is performed

6\. risk score is calculated

7\. validation report is produced



**Initial Scope**

Initial implementation focuses on AWS networking constructs including VPCs, subnets, route tables, security groups, and gateway resources.

