# Provenance: Microsoft Skills `python-appservice-deploy`

- Source family: `microsoft-skills`
- Source repository: `https://github.com/microsoft/skills`
- Source class: official Microsoft
- License: MIT
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Canonical package path: `.github/plugins/azure-skills/skills/python-appservice-deploy`
- Canonical `SKILL.md`: `.github/plugins/azure-skills/skills/python-appservice-deploy/SKILL.md`
- Package tree: `6e11dad529e50b7fbc37191de665788d0427ccad`
- `SKILL.md` blob: `ac25db692762945d0e3e9ed2016dcfa29fbfa610`
- Freshness evidence: `24a3a7bd6caa8e87b3a91e93c95959e3cfdb906d` synchronized this package on 2026-06-15T13:03:05Z
- Behavioral validation: `not-run`

## Package identity and boundary

`python-appservice-deploy` is an independently front-mattered first-class skill in the registered Microsoft Skills pin. The exact package contains fourteen files: the root `SKILL.md`, eight reference documents, and four shell/PowerShell helpers plus their containing directories. The upstream scripts remain source evidence only; they are not repository-owned `skillz` runtime.

## Purpose and dependencies

The skill deploys Python Flask, Django, FastAPI, or generic Python applications to Azure App Service Linux. It resolves Azure context, detects framework shape, creates missing resource groups/App Service plans/web apps, configures build and startup settings, packages local code, deploys ZIP content, and reports the resulting endpoint. Operational use depends on Azure CLI/MCP access, authenticated Azure identity, subscription/resource-group authority, local application files, shell/PowerShell tooling, and App Service availability/quota.

## Authority and portability

Authority profile: **mutating + external-side-effect**. The normal workflow can create Azure resource groups, a paid P0v3 App Service plan, web apps, app settings and startup configuration, package local source, and deploy code. Its own `create-app.md` explicitly says not to ask for confirmation after printing derived defaults and to proceed with creation, so it lacks the mandatory action-specific authorization boundary required for consequential cloud, cost, configuration, and deployment mutations.

Portability: **low** unchanged because execution is tightly coupled to Azure App Service, Azure CLI/MCP semantics, Oryx behavior, and Azure resource lifecycle. Its framework detection, explicit create-before-deploy decomposition, shell-safety guidance, transient-error classification, and post-deploy asynchronous-build caveats remain useful adaptation/reference evidence.

## Secret and sensitive-data context

The ZIP packaging guidance explicitly excludes `.env`, which is a useful safeguard, but deployment still transmits application source and may affect production traffic or externally reachable services. Any adaptation must use approved credential paths, keep secret material out of conversational/log output, confirm the intended subscription/resource group/app/region/SKU, and require explicit authorization immediately before resource creation, configuration mutation, and code deployment.