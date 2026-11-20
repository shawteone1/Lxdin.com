# Approved LXDiN logo integration

Review branch: `review/lxdin-approved-logo-integration-2026-11-20`.
Base: approved enterprise-polish commit `7ba6ac709a03a7a28257ff4fc41c4acebb038131`.

## Artwork and changes

The founder attached the approved 1280×640 metallic silver/cyan LXD lock artwork. The exact JPEG is preserved at `brand/approved-lxdin/master.jpg`, SHA256 `d6b1b9646edcb396787cc895e718d174169e1533258aff83135480eea1b174cb`. No previous concept, tracing, regeneration, recoloring or alternate artwork is used.

The full symbol, LXDiN wordmark and tagline are retained in a crop (208,20,1072,578) with its original navy/glow background. Optimized lossless WebP assets are exported at 432/864 pixels wide. Header/footer use the identical proportional image. Header width is 128px on desktop/iPad and 112px on phones, with 4px vertical padding. The proportional image makes the header approximately 91px tall on desktop (previously about 156px). Footer widths remain 216px desktop and 176px phone. Navigation typography is unchanged. Only scoped logo sizing, necessary header padding and dropdown positioning below the taller header are added. All original CSS remains intact before the appended branding rules. No transparent-background processing is attempted, preserving the metallic/glow appearance exactly.

Icons derive from the complete LXD/lock monogram crop (304,24,960,392), centered proportionally on a square canvas padded with navy sampled from the approved image. No letters are redrawn or clipped. PNG sizes 16/32/48/64/180/192/512 and ICO 16/32/48/64 are supplied. The smaller favicon versions should be reviewed at native size; fine keyhole/metallic detail naturally reduces at 16px.

`public/index.html` changes are limited to the two brand links' contents and favicon/touch-icon declarations. Copy, sections, links, IDs, navigation controller and primary demo CTA are unchanged. `public/demo/index.html` is byte-identical to the approved baseline. The parent-company footer and ecosystem links remain. The demo's existing fictional Soccer Center treatment and behavior are untouched.

`SOURCE.json` records the candidate's current hashes, retains the previous approved hashes as `pre_logo_sha256`, and preserves the original rollback reference. The existing verifier is unchanged. New logo checks verify image integrity, icon dimensions, normalized non-brand HTML and original CSS preservation.

## Actual verification

- `python3 scripts/verify.py`: PASS code/source/route/asset/JavaScript/disclosure checks.
- `python3 scripts/verify_logo.py`: PASS provenance, asset hashes/dimensions and preservation checks.
- Temporary local HTTP checks: 19/19 public files returned 200 with exact bytes. Stylesheet served as text/css; WebP assets served as image/webp. Master source outside public is not served.
- Exported header and 180px icon inspected as image files; crop retains the approved complete lock/letters, wordmark and tagline. This is asset inspection, not a browser screenshot.
- Browser initialization attempted and failed before navigation: `the gaas-browser node_repl sandbox cannot be disabled`. No bypass attempted.
- Desktop/iPad/mobile rendering, navigation touch behavior, console QA and real browser screenshots remain INCOMPLETE. No live Codespaces URL is claimed.

## Exact Codespaces setup

From the repository root, after saving any unrelated work:

```sh
git fetch origin review/lxdin-approved-logo-integration-2026-11-20
git switch review/lxdin-approved-logo-integration-2026-11-20
git pull --ff-only origin review/lxdin-approved-logo-integration-2026-11-20
python3 scripts/verify.py
python3 scripts/verify_logo.py
python3 -m http.server 3000 --bind 0.0.0.0 --directory public
```

If port 3000 already has a server, stop that process with Ctrl+C first. In Codespaces Ports, forward port 3000 with upstream protocol HTTP, preserve Private visibility, and open its generated HTTPS browser URL. Sign in as an authorized Codespace owner/collaborator for private forwarding. Do not guess a preview URL or make the port public merely to bypass access controls. Python serves public/ only; no npm install, build, backend or domain configuration is required.

Review desktop, iPad landscape (1024×768), iPad portrait (768×1024) and phone (390×844): full logo visible/proportional, appropriate spacing, navigation opens below header, no overflow, footer readable, demo opens/resets/returns, fictional disclosures visible. Review the favicon at 16/32px. Use a hard refresh if the previous logo/favicon is cached.

No production deployment, main/release merge, DNS, GoDaddy or other-product changes are included. Founder visual acceptance remains pending.
