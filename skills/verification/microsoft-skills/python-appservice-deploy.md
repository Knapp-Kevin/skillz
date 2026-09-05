# Verification: Microsoft Skills `python-appservice-deploy`

- Source family: `microsoft-skills`
- Canonical path: `.github/plugins/azure-skills/skills/python-appservice-deploy`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `6e11dad529e50b7fbc37191de665788d0427ccad`
- `SKILL.md` blob: `ac25db692762945d0e3e9ed2016dcfa29fbfa610`
- Static disposition: **rejected unchanged**
- Score: **12/20**
- Behavioral validation: **not-run**
- Controlled tags: `cloud`, `deployment`, `operations`, `production-oriented`, `risk-aware`, `mutating`, `external-side-effect`, `low`

## Structured semantic review

### Useful material to preserve

The package has useful Azure App Service deployment prior art: explicit Flask/Django/FastAPI scope and non-trigger boundaries, framework detection, deterministic resource naming, shell-safe runtime syntax, separation of resource creation from code deployment, transient-error classification, idempotent `show || create` patterns, `.env` exclusion from ZIP packaging, server-side build configuration, FastAPI startup guidance, and an important distinction between deployment acceptance and asynchronous Oryx build/startup completion.

### Authority hard fail

Unchanged adoption fails the current authority standard. The workflow can create a resource group, a paid P0v3 App Service plan, a public web app, mutate application settings/startup configuration, package local code, and deploy it to Azure. `create-app.md` explicitly instructs the agent to print derived defaults, **not** ask for confirmation, and proceed with creation. A general request to deploy a Python application is not blanket authorization to infer subscription, region, resource names, paid SKU, resource creation, configuration mutation, or production-facing code deployment. Each consequential stage requires a real action-specific authorization checkpoint immediately before mutation.

### Secret and sensitive-data discipline

The package appropriately excludes `.env` from ZIP creation, reducing one obvious credential-leak path. Deployment still transmits application source to Azure and may expose or change an externally reachable service. The unchanged procedure does not impose a universal pre-deploy classification/minimization check for sensitive source/configuration content. Any adaptation must use approved external credential paths, avoid logging or soliciting secrets, verify that secret-bearing files are excluded, and obtain explicit authority for the target and code disclosure before upload/deployment.

### Trigger and non-trigger boundary

Use as reference for Python App Service deployment design, framework-specific startup behavior, Azure CLI command structure, retry/error classification, and asynchronous deployment semantics. Do not use unchanged as authorization to create Azure resources, incur App Service cost, change app configuration, upload source, or deploy code.

## Portability

Low unchanged portability because operational behavior is coupled to Azure App Service, Azure CLI/MCP tools, Oryx, Azure subscriptions, and App Service resource semantics. Framework-detection, shell-safety, deployment-state, retry-classification, and packaging safeguards generalize well.

## Validation note

This review inspected the exact registered-pin `SKILL.md` and canonical fourteen-file package tree statically, including the reference and helper-script surfaces. No Azure login, resource creation, paid plan allocation, app configuration, code packaging, upload, deployment, traffic probe, or credential-bearing operation was executed. No representative external behavioral/adversarial evidence exists, so behavioral validation remains `not-run`.