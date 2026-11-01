# Contributing

Thanks for your interest in improving this portfolio.

1. Search existing GitHub Issues before reporting a bug or suggesting a feature.
2. Open an issue describing the problem and expected behavior when appropriate.
3. Fork the repository or create a working branch (do not push directly to protected `main`).
4. Make a focused change, check that the site still renders in a modern browser, and verify navigation and layout on narrow screens.
5. Open a pull request describing what changed, why, and how you tested it.
6. The repository maintainer reviews proposed changes and decides whether to merge them.

Prefer readable HTML, accessible labels, small vanilla JavaScript changes, and no unnecessary dependencies. Do not submit credentials, personal data, or copyrighted materials you cannot license.
## Testing requirements

All major new functionality must include appropriate automated tests. Bug fixes should include regression tests when practical.

Before submitting a pull request, contributors should run:

`python3 -m unittest discover -s tests -v`

All tests must pass before changes are merged. Contributors should also verify that the portfolio website displays and functions correctly in a modern browser.
