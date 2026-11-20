# Header sizing correction

Starting commit: `8e74991677ca1df4d1f8a09c4ef894727feedf4a`. Same logo review branch. Approved artwork bytes, original page CSS prefix, messaging, navigation destinations, hero and fictional demo remain unchanged.

## Diagnosis and evidence

The previous CSS selector matches the header image, has higher specificity than the generic brand image rule, and is active at both landscape widths (>900px). With the exact checked-in stylesheet, sandboxed Chromium measured **128×82.65625px** at 1024×768 and 1180×820. There is no evidence that a conflicting selector in this commit overrides 128px. Claiming that would be incorrect.

The code defect is an unsafe sizing fallback: the header HTML still declared **width=864 height=558**, and the brand flex item had no fixed width/basis and retained its intrinsic automatic minimum width. `sizes` only controls image candidate selection; it does not set rendered width. The earlier fix depended entirely on the latest external logo CSS. Supplying the existing stylesheet without the appended brand rules reproduces an **864×558px** image and parent. Navigation is compressed/wrapped and extends to x=1202, beyond the header's right edge (997 at 1024px; 1153 at 1180px). This is recorded in before-computed.json and the reproduced-failure screenshot.

The founder's exact Codespaces URL redirects unauthenticated page AND CSS requests to the GitHub private-port sign-in page. Those final responses are text/html, not the underlying stylesheet. This prevents confirming the precise CSS bytes/cache state received by the owner's signed-in iPad. The local reproduction establishes the intrinsic fallback failure, but stale CSS in that private Safari session remains an explanation to confirm, not a claimed observation. No authentication or sandbox bypass was attempted.

## Correction

- Header HTML now declares proportional **144×93** display dimensions, while the image files remain unchanged. Even older CSS cannot expose an 864px HTML fallback.
- A header-only CSS variable fixes the brand parent's width, max-width and flex-basis to **144px**, with `min-width:0`. The actual image is bounded to that container with `width/max-width:100%`, `min-width:0`, proportional auto height and shrink allowed.
- Mobile parent width is **112px**; image height remains proportional. Footer branding is unchanged.
- Landscape navigation uses nowrap and a zero automatic minimum width within its existing flex layout.
- The stylesheet reference carries its content hash as a query version to avoid silently reusing a pre-brand stylesheet. The existing local-path verifier now parses URL paths correctly when a query string is present; file-existence assertions remain enforced. The logo verifier checks that the stylesheet hash version matches the actual file.

## Real browser regression results

Run `python3 scripts/test_header_browser.py` from the repository root. It starts and stops a temporary local public-only server, launches normal Chromium with **chromium_sandbox=True**, waits for fonts/images, reads computed styles and bounding boxes, and checks actual header scroll width, logo/parent bounds, proportional height, single-line landscape nav and touch-menu controls. It also tests both iPad landscape sizes with the branding CSS deliberately omitted. Output JSON/screenshots go to `/tmp/lxdin-header-browser` or `LXDIN_QA_ARTIFACTS`. Set `LXDIN_CHROMIUM` to select a normal installed Chromium executable. A standard Python Playwright/browser installation is a QA-only dependency.

| Viewport | Actual image | Parent width | Header height | Header overflow / nav |
| --- | --- | --- | --- | --- |
| 1024×768 | 144×93 | 144 | 102 | None; one row |
| 1180×820 | 144×93 | 144 | 102 | None; one row |
| 1440×1000 | 144×93 | 144 | 102 | None; one row |
| 768×1024 | 144×93 | 144 | 102 | None; menu opens/closes |
| 390×844 | 112×72.328125 | 112 | 81.328125 | None; menu opens/closes |

Both stale-brand-CSS cases also measure 144×93 with parent width 144 and no header overflow; header height is 94 without brand padding. **7/7 cases passed**, zero page JavaScript errors or HTTP error responses. Screenshots are real browser screenshots at device pixel ratio 2; dimensions in this table are CSS pixels.

Existing `scripts/verify.py` and `scripts/verify_logo.py` PASS. The former's generic browser-incomplete line still applies to complete demo/native-device qualification, not these newly executed header tests. Demo bytes are unchanged; no demo logic was modified.

## Limits

These are sandboxed Chromium tablet/phone viewport tests, not native iPad Safari. The authenticated Codespaces preview's actual CSS/cache state remains unverified. The 1024px full page has pre-existing horizontal overflow in both the starting commit and candidate, outside the correctly bounded header. It was recorded rather than hidden by an overflow-clipping workaround or a hero redesign. No claim is made that the whole page is overflow-free. All other tested viewport widths had no page-level overflow.

To update the founder preview: pull this same review branch with `git pull --ff-only`, restart `python3 -m http.server 3000 --bind 0.0.0.0 --directory public` from the repository root, and reload the private forwarded URL while signed in. Confirm its document contains width=144 height=93 and a styles.css?v=... link. No production merge, publication, DNS or hosting change is included.
