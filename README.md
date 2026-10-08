# JEM Labs website

Static, product-first company website. No runtime dependencies, build step, JavaScript, accounts, analytics, or data storage.

## Preview

Run `python3 -m http.server 8000` in this repository, then open http://localhost:8000. Serve from the repository root because shared asset URLs are root-relative.

## Deploy to Vercel

Import this repository, choose **Other** as the framework, leave the build command empty, and use `.` as the output directory. `vercel.json` supplies security headers. Configure jemlabs.org in Vercel when ready. No deployment is performed by this PR.

## Files

- `index.html`: products, about, future tools, contact
- `privacy.html`, `terms.html`, `support.html`: standalone information pages
- `assets/styles.css`: shared responsive design
- `assets/jem-mark.svg`: original logo and favicon
- `robots.txt`, `sitemap.xml`: discovery
- `vercel.json`: hosting configuration
- `scripts/check.py`: local links/assets and required-content validation

## Brand

Warm charcoal #211C1B, ivory #F7F0E6, muted peach #E8AD91, burnt orange #B64A2A, wine #641E35, sand #EEE2D2, muted text #BDB0A6, and border #493C37. Arial/Helvetica sans-serif typography with compact headings and comfortable body text. The mark assembles three modules and an open diagonal fourth module, suggesting a system being built and tested. Product monograms are editorial identifiers, not claimed official product logos.

## Remaining content

- TaskDizzle: replace the non-interactive “App Store link coming soon” status and adjacent TODO with a real link once the URL is available. Its main CTA already links to taskdizzle.online.
- Confirm Privacy and Terms reflect the final hosting setup and company practices before launch.
