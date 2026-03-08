\# PathGuard Threat Model



\## Purpose

This document identifies security and operational risks associated with PathGuard and defines initial protection goals.



\## Assets

\- cloud network topology data

\- infrastructure change data

\- policy definitions

\- validation reports

\- credentials used for cloud state collection



\## Trust Boundaries

\- local execution environment

\- cloud provider APIs

\- infrastructure change input source

\- report output destination



\## Primary Risks

\- unauthorized access to cloud credentials

\- exposure of sensitive network topology data

\- incorrect risk evaluation leading to unsafe change approval

\- tampered input plans or policy files

\- excessive cloud API permissions

\- insecure storage of reports containing network details



\## Security Goals

\- minimize privileges for cloud access

\- protect sensitive topology and policy data

\- preserve integrity of change inputs

\- ensure validation results are reproducible

\- prevent unauthorized modification of reports



\## Initial Controls

\- read-only cloud access where possible

\- scoped IAM permissions

\- local secret isolation

\- input validation for change files

\- structured logging

\- controlled report storage

\- explicit versioning of policy rules



\## Assumptions

\- initial development is performed in a personal environment

\- AWS is the first supported cloud provider

\- PathGuard does not directly apply infrastructure changes

\- users are responsible for protecting their local workstation



\## Out of Scope

\- multi-user authentication system

\- centralized secrets management

\- distributed execution

\- production-grade report retention controls

