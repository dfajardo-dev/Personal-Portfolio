# Personal-Portfolio

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/dfajardo-dev/Personal-Portfolio/badge)](https://scorecard.dev/viewer/?uri=github.com/dfajardo-dev/Personal-Portfolio)

A small, static personal portfolio website showcasing software engineering interests and project summaries. This is an early version; some project details are placeholders that will be updated as links and demos become available.

## Features
- Responsive HTML/CSS layout
- Accessible navigation and skip link
- Projects, skills, and feedback sections
- Small JavaScript enhancement for the footer year
- No third-party runtime libraries

## Quick start
Clone this repository and open `index.html` in a modern browser. No build step or dependencies required.

```bash
git clone https://github.com/dfajardo-dev/Personal-Portfolio.git
cd Personal-Portfolio
python3 -m http.server 8000
```

Then open `http://localhost:8000`. The Python command is optional; opening `index.html` directly also works.

## Files and interface
- `index.html`: pages and external links. Entry point for the site.
- `assets/style.css`: layout and appearance.
- `assets/script.js`: updates the footer year based on the viewer's system clock.
- No user input is sent to a server and there is no backend or API.

## Limitations and security
This is an informational static site, not an authenticated application. It does not collect accounts, passwords, or payments. Its external GitHub links open GitHub pages, whose own policies apply. Avoid adding secrets, credentials, or private information to this public repository. See [SECURITY.md](SECURITY.md) for reporting security issues.

## Feedback and contributions
Use [GitHub Issues](https://github.com/dfajardo-dev/Personal-Portfolio/issues) for bugs and suggestions. See [CONTRIBUTING.md](CONTRIBUTING.md) for proposed changes and pull request steps.

## Plans
See [ROADMAP.md](ROADMAP.md) for planned work, and [CHANGELOG.md](CHANGELOG.md) for recorded releases.

## License
The source code is licensed under the [MIT License](LICENSE). Project names and descriptions are for portfolio presentation; please replace placeholder details with verified links before presenting them as completed projects.
