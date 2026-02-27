# TakeAIBite

Personal blog and portfolio site -- data science methodology, AI-assisted development, and lessons from building real projects.

**Author:** Alberto Diaz Durana
**URL:** https://takeaibite.de/
**Built with:** [Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod)

## Local Development

### Prerequisites

- Hugo v0.157.0 extended ([installation guide](https://gohugo.io/installation/))
- Git

### Setup

```bash
git clone --recurse-submodules https://github.com/albertodiazdurana/dsm-blog-poster.git
cd dsm-blog-poster
hugo server -D
```

The `-D` flag includes draft posts. Visit `http://localhost:1313/` to preview.

### Creating a New Post

```bash
hugo new blog/YYYY-MM-DD-slug/index.md
```

This uses the `archetypes/blog.md` template. Edit the generated file, set `draft: false` when ready to publish.

### Publishing Workflow

1. Create or edit a post in `content/blog/YYYY-MM-DD-slug/index.md`
2. Preview locally with `hugo server -D`
3. Set `draft: false` in the post's front matter
4. Commit and push to `main`
5. GitHub Actions builds and deploys automatically

### Blog Post Front Matter

```yaml
---
title: "Post Title"
date: YYYY-MM-DD
draft: false
description: "One-sentence summary for SEO and previews."
tags: ["Tag1", "Tag2"]
categories: ["Technical"]
author: "Alberto Diaz Durana"
showToc: true
ShowReadingTime: true
slug: "url-friendly-slug"
---
```

### Project Structure

```
dsm-blog-poster/
  archetypes/          # Content templates
    blog.md            # Blog post template
    default.md         # Default template
  content/
    blog/              # Blog posts (leaf bundles)
      YYYY-MM-DD-slug/
        index.md       # Post content
        *.png          # Post images (co-located)
    archives.md        # Archives page
    search.md          # Search page
  docs/                # DSM project documentation
  static/
    CNAME              # Custom domain for GitHub Pages
  themes/
    PaperMod/          # Theme (git submodule)
  hugo.toml            # Site configuration
```

## Deployment

The site deploys automatically via GitHub Actions on push to `main`. The workflow:

1. Installs Hugo v0.157.0 extended
2. Builds the site with `--gc --minify`
3. Deploys to GitHub Pages

## Custom Domain Setup (takeaibite.de)

DNS configuration is managed separately in GoDaddy. See `docs/plans/handover-from-dsm-central.md` for details.

## License

Blog content is copyright Alberto Diaz Durana. The site source code follows the MIT license.
