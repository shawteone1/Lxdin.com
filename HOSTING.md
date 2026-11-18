# Hosting handoff

## Repository status

Intended private GitHub repository: shawteone1/LXDiN. Creation/access is blocked, so no verified repository or branch URL is available yet. See GITHUB-SETUP.md. The exact prepared commit is obtained with `git rev-parse HEAD` in this checkout or from the supplied bundle.

## Requirements and configuration

| Setting | Value |
| --- | --- |
| Website type | Static HTML/CSS/JavaScript |
| Root directory | Repository root |
| Framework preset | None |
| Build/install command | None; `exit 0` if required |
| Publish/output directory | `public` |
| Runtime/start command | None |
| Environment variables/secrets | None |
| Candidate branch | `release/lxdin-commercial-2026-11-18` |
| Future approved production branch | `main` (not created or modified here) |

Serve public/index.html and public/demo/index.html with normal directory-index handling. No SPA rewrite, Node runtime or backend is needed. Never publish the repository root, docs or .git directory.

## Recommended preview path — later approval required

A GitHub-connected static host such as Cloudflare Pages supports this buildless package and branch previews. Connect only the dedicated private repository and grant minimum necessary repository access. Configure `main` explicitly as the production branch, the release branch as a preview branch, and `public` as output. Do not accept the release branch as production merely because it is GitHub's initial default branch. If the setup wizard requires an existing main or immediately publishes production, stop for release approval rather than creating/updating main as a workaround.

Require authenticated preview access (Cloudflare Access or the selected host's equivalent); Cloudflare branch-preview URLs are public by default. Review the complete fictional demo and desktop/mobile/iPad layouts before approving production. No host has been provisioned and no preview has been deployed by this work.

Reference: https://developers.cloudflare.com/pages/framework-guides/deploy-anything/
Preview access and branch behavior: https://developers.cloudflare.com/pages/configuration/preview-deployments/

## Existing Sites host evaluation

The existing standalone LockedIn Sites project can serve these same static files. Its manifest retains project appgprj_6afe12b6dfd881918e335f5c23dfce9c and static output dist. It is currently independent of lxdin.com and has no attached custom domains. Its native source remote is the Sites-managed repository, not GitHub. Direct GitHub-triggered deployment to this existing Site has not been established. It could be reused through the native Sites source/version/deployment process, but should not be described as a working GitHub-connected pipeline without a supported connection. No new Sites application or replacement hosting identity is included in this GitHub export. The original project configuration remains untouched.

## Domain setup after preview and release approval

lxdin.com is registered at GoDaddy and currently parked; registration alone is not hosting. No domain attachment is part of this preparation.

1. Choose/approve the static host and production release. Preserve existing DNS records and a known-good deployed artifact before changes.
2. Register BOTH lxdin.com and www.lxdin.com in that host's custom-domain controls first. Obtain the exact assigned targets and validation records; never guess them from the current parking IPs.
3. For Cloudflare Pages, an apex custom domain requires a Cloudflare zone and Cloudflare nameservers. Registration can stay at GoDaddy, but DNS authority would move. Import and verify all existing MX/TXT/mail and other records before any separately approved nameserver change. If retaining GoDaddy DNS authority is required, choose a host supporting an external-DNS apex rather than assuming Pages apex can use a simple CNAME there. A Pages www subdomain can use the host-provided CNAME at GoDaddy, after association in Pages.
4. Apply only separately approved provider-supplied DNS/validation changes. Do not affect unrelated domains or mail records.
5. Wait for validated TLS certificates covering BOTH apex and www before configuring an HTTPS redirect to the chosen canonical hostname. Verify HTTP-to-HTTPS and www/apex redirects without loops, then the landing page, /demo/ route and all assets on both names. Investigate any remaining 503 instead of treating DNS propagation as a guaranteed explanation.

Domain requirements: https://developers.cloudflare.com/pages/configuration/custom-domains/

## Rollback

The original published LockedIn source remains e669d849963b333c91128a04df1aa6461d39ac1e, tagged rollback/lockedin-published-v1 in the original project. Its saved version is appgprj_6afe12b6dfd881918e335f5c23dfce9c~appgver_032dbb6e90448191b0e3afa32edb49d7. This does not represent an existing lxdin.com production deployment.

Before any future new-host release, save that host's previous deployment ID and artifact plus DNS configuration. Roll back using the host's previous immutable deployment or redeploy its recorded source SHA; use a reviewed revert commit for GitHub main, never a force-push. Restore DNS only from the recorded configuration if separately approved and necessary. Keep the original Sites version intact throughout.

## Remaining qualification

Code-level verification passes; visual, accessibility and full demo interaction QA remain incomplete because the supported browser environment is unavailable. No runtime or screenshot pass is claimed. Neither a private GitHub repository nor a remote SHA has been verified yet; repository creation permission is the immediate blocker.
