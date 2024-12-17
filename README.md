# EGP Doc Generator

## Introduction
The EGP Doc Generator is a tool that automatically analyses the source code of a RESTful API, extracts information about endpoints, parameters, and responses, and generates detailed documentation in the OpenAPI format. The generated documentation can be displayed using Swagger UI.

## Context
This project was developed during a GitHub Copilot Hackathon, where participants collaborated to create innovative tools and solutions using GitHub Copilot.

## Project Structure
```mermaid
graph TD;
    A[API_Python] --> B[appegp];
    B --> C[api];
    C --> D[v1];
    D --> E[endpoints];
    E --> F[example.py];
    B --> G[core];
    G --> H[config.py];
    B --> I[main.py];
    B --> J[models];
    J --> K[example.py];
    B --> L[schemas];
    L --> M[example.py];
    B --> N[tests];
    N --> O[test_example.py];
    A --> P[requirements.txt];
    A --> Q[README.md];
    A --> R[Dockerfile];
    S[Ficheiros_EGP] --> T[1_DUMP_MGPEC_TESTE.EGP];
    S --> U[README.md];

## Requesting a Feature or Reporting a Bug

If you would like to request a feature or report a bug, please open an issue on our [GitHub repository](https://github.com/gaspar-m-brogueira-alpt/doc_egp_generator/issues).