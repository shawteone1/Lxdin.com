# LXDiN — LXD security identity / founder review v1

Two original flat-vector identity treatments. Both are ready for founder selection; neither is approved for integration. Exact spelling: **LXDiN**. Tagline: **IDENTITY. CONSENT. CONTROL.**

Baseline: corrected enterprise-polish commit `7ba6ac709a03a7a28257ff4fc41c4acebb038131`.
Review branch: `review/lxdin-lxd-security-logo-2026-11-20`.

## Open first

- `comparison-board.png` / `.svg` / `.pdf`: the two concepts side by side, light, dark and monochrome.
- `favicon-comparison.png`: native 16, 32, 48 and 64 px render tests, plus nearest-neighbor enlarged 16 px pixels.
- `application-comparison.png`: proposed header placement and presentation cover, explicitly mockups rather than a modified website.
- Each concept also contains an individual website-header, document and presentation mockup in SVG/PNG; document and presentation covers include PDF exports.

## A — Solid LXD

Custom geometric L and D flank a cyan/electric-blue X. The shackle sits on the two upper arms of the X; the crossing X itself is the lock body. A small true knockout keyhole keeps the security cue restrained. This is an original drawn monogram, not an assembled stock lock/shield/dial.

The light version uses navy L/D and blue X. The dark version uses silver L/D and cyan X. Monochrome and reverse versions preserve the same geometry without color doing the explanatory work.

## B — Negative-space LXD

The letters are cut through one compact, angular lock housing; the shackle remains centered above the X. No extra keyhole or decorative hardware is added. The D counter is a vector island, not a white rectangle. The entire symbol, including the letter knockouts, remains truly transparent outside its filled paths.

Its 16 px favicon has a separately editable pixel-hinted micro master: whole-pixel letter counters and a simplified shackle for optical clarity. The 32/48/64 px exports use the normal master. This intentional micro derivative is labeled explicitly and is not a new master identity.

## Evaluation and recommendation

These are design judgments from inspection of the rendered exports, not user-research results or a trademark assessment.

| Criterion | A — Solid | B — Negative space |
| --- | --- | --- |
| Letter readability | Strongest separation of L, X and D | Clear at normal sizes; reduced internal counters at micro sizes |
| Security recognition | X and shackle become one distinctive security gesture | Stronger familiar lock silhouette; more utilitarian housing |
| Versatility | Strong for wordmark, document and presentation use; one-color remains clear | Strong for compact badges and square applications; knockout counters need care in reproduction |
| Enterprise credibility | Restrained, precise and open; least dependent on a container | Disciplined and robust; more stamp-like in tone |
| Smallest tests | At 16 px the wide monogram is primarily a mark, not comfortably read lettering | Pixel-hinted 16 px version improves structure; 32 px+ is still preferable for clear LXD recognition |

**Recommend A as the primary identity** because it keeps the three letters most distinct and integrates the lock directly into the X with less surrounding furniture. B is a genuine alternative if compact badge recognition is the founder's priority. This recommendation does not authorize A, B, or a hybrid system to be integrated. Founder selection is required.

## Files per concept

- `master-symbol.svg`, `master-horizontal.svg`: primary editable outlined vectors, no external fonts or raster content.
- `symbol-light|dark|mono|reverse.svg` and matching transparent PNGs.
- `lockup-light|dark|mono|reverse.svg` and matching transparent PNGs.
- Symbol PNG exports are 4× the SVG canvas; lockups are 1740×504. These PNGs have alpha channels and no matte/checkerboard.
- `favicon-tests/`: exact 16/32/48/64 px PNGs for light, dark and mono palettes, scalable favicon SVGs and a multi-resolution `.ico`. B includes its optical 16 px SVGs.
- `website-header-mockup.svg/.png`: proposed placement only; compact header treatment omits the small tagline, which appears in the hero instead.
- `presentation-mockup.svg/.png/.pdf` and `document-mockup.svg/.png/.pdf`.

Light/dark are **palette** variants with transparent backgrounds. Place dark-palette assets on navy/graphite, light-palette assets on white/light backgrounds. White one-color files are named `reverse`; navy one-color files are named `mono`.

## Color and use

- Deep navy `#102A43`
- Electric blue `#087FC1` on light backgrounds
- Cyan `#38C7F0` on dark backgrounds
- Silver `#DCE5EF`
- White `#FFFFFF`

No gold, gradients, glow, combination dial, shield or stock padlock is used in the master marks. Keep clear space at least the main letter-stroke width around each mark. Do not add outlines, bevels, glows, drop shadows, provider names, certification badges or implied verification guarantees.

Recommended minimums: symbol 32 px for clear lettering; full lockup with tagline 360 px wide. At smaller header sizes use the symbol + wordmark without the tagline, as shown in the proposed header mockups. Native 16 px tests are supplied honestly; they do not imply that all letter/keyhole detail remains independently legible at that size. Print minimums should be confirmed with the actual reproduction process before manufacturing.

## Meaning and positioning

The integrated lock refers to controlled consent, authorized access and purpose-specific handoffs. It does not assert that LXDiN itself performs every identity or document verification. Mockup copy explicitly places established specialist providers within the workflow. LA02UK remains the parent organization.

## Editing and reproducibility

The symbol geometry is original path construction. Wordmark and tagline are editable vector outlines derived from the existing Manrope/DM Sans files; SIL Open Font Licenses are included under `licenses/`. No recipient needs fonts installed to render the SVG masters.

`build.py` is the editable geometric source and regenerates the vectors, PNGs, optical tests and mockups. It runs from the existing repository with development-only Python packages fontTools, CairoSVG and Pillow, using the already-present local font files. These are artwork-generation tools, not website/runtime dependencies. `tool-versions.json` records the renderer versions used.

## Preservation and delivery checks

- All assets are in `brand-review/`, outside the website's `public/` output.
- Landing page, navigation, About/Mission/Contact, portfolio links, demo, partner references, workflows and simulation disclosures are byte-identical to the corrected baseline.
- SVGs parsed; primary vector masters contain no embedded raster images or external font/network dependency.
- All logo PNGs have transparent alpha backgrounds; no checkerboard is baked in. Keyhole/letter knockouts were checked for zero alpha.
- Native favicon dimensions and ICO image sizes checked. These are actual rendered asset tests, not a claim of browser/site integration.
- Comparison board, favicon sheet, header/presentation sheet and document cover were visually inspected for spacing, letter recognition, clipping and contrast.

No integration, merge, deployment, publication or DNS change is included. Soccer Center, Arena Pathway and PlayRcmd are untouched.
