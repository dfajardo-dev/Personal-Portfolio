"""Basic checks for the static portfolio. Run: python3 -m unittest discover -s tests"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PortfolioTests(unittest.TestCase):
    def test_html_sections(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        for anchor in ('id="main"', 'id="about"', 'id="projects"', 'id="contact"'):
            self.assertIn(anchor, html)

    def test_no_remote_javascript(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertNotIn('<script src="http', html)
        self.assertIn('defer src="assets/script.js"', html)

if __name__ == '__main__':
    unittest.main()
