### [2026-03-07] Domain architecture decision: take-ai-bite.com

**Status:** Processed (2026-03-07, S3)
**Resolution:** Accepted with adjustment

Actual architecture (differs from proposal due to GoDaddy DNS limitations):
- `takeaibite.de` = landing page (GoDaddy Website Builder, finished)
- `take-ai-bite.com` = Hugo blog at root domain (Cloudflare DNS, GitHub Pages)
- Landing page links to blog (no subdomain needed -- separate domains)

No config changes required. Hugo already deployed at take-ai-bite.com.

### [2026-03-09] Update GitHub link to public repo

**Status:** Processed (2026-03-09, S4)
**Resolution:** Already resolved -- hugo.toml social link already points to `https://github.com/albertodiazdurana/take-ai-bite` (updated in S3)