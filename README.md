# LXDiN

Standalone commercial landing page and existing fictional interactive onboarding demonstration. A technology venture from LA02UK.

## Static hosting

Deploy **public/**. Framework: none. Build/install/start commands: none. For a host requiring a build command, use `exit 0`. No Node.js runtime, database, API keys, verification provider or payment integration is required. The demo keeps its state in memory and performs no live provider requests. Its images are embedded data URLs.

## Verification

Run `python3 scripts/verify.py`. Node, when available on a developer machine, is used only for JavaScript syntax validation. All product files are checked against the approved source hashes in SOURCE.json. These checks do not replace browser QA.

## Provenance and boundaries

Exact product files were extracted from source commit `7b812ba50986c36db999a8e52fa48c62b61ad836`, branch `release/lxdin-commercial-2026-11-18`, in the existing standalone LockedIn Sites project. See SOURCE.json. No redesign or demo change was made. Original rollback commit `e669d849963b333c91128a04df1aa6461d39ac1e` and tag `rollback/lockedin-published-v1` remain in that source repository.

This export excludes the original Git history, .openai hosting identity, unrelated source/apps, obsolete calculator, QA captures, test data and credentials. Original source checkout and remote remain unchanged. Fictional sample names and sample health/payment descriptions remain intentionally, as required by the demo; they are not real personal records. Pattern scans and source inspection found no live credentials; this is not a formal security audit.

## Branch policy

Current candidate: release/lxdin-commercial-2026-11-18. Reserve main for a future approved production release. Do not create or update main or connect automatic production deployment without approval. In an initially empty repository, GitHub may select the first pushed release branch as its default; default branch is not production approval. Explicitly select main as the future production branch in hosting controls.

## Current readiness

GitHub creation was denied by the available integration (`Resource not accessible by integration (createRepository)`). No remote repository or push has been verified. See GITHUB-SETUP.md for the exact completion commands.

Visual and browser interaction qualification is incomplete. The managed browser previously failed initialization with `the gaas-browser node_repl sandbox cannot be disabled`; no supported browser-control tool is available for this packaging turn. No server or browser workaround was attempted. No screenshots or runtime acceptance are claimed.

See HOSTING.md for preview and future domain handoff. This package does not deploy or attach a domain.
