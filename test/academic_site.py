"""Check the built academic pages and the search index that visitors receive."""
from pathlib import Path
import re
import sys

site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('_site')
pages = ['index.html', 'research/index.html', 'publications/index.html', 'moments/index.html']
for page in pages:
    html = (site / page).read_text()
    assert not re.search(r'\bCGPA\b|\bGPA\b|Albert Einstein|a post with', html, re.I), page
    assert '/assets/css/academic.css' in html, page
    for nav_id in ['nav-profile', 'nav-research', 'nav-publications', 'nav-moments']:
        assert nav_id in html, (page, nav_id)
    search = re.search(r'ninja\.data\s*=\s*\[(.*?)\];', html, re.S)
    assert search, (page, 'search index missing')
    assert not re.search(r'"(?:Posts|Books|News|Projects|Teachings)"', search.group(1)), page

home = (site / 'index.html').read_text()
for text in ['MS in Microbiology', 'Doctor of Veterinary Medicine', '2019–2025', 'April 2025', 'afsansarwer.bd@gmail.com']:
    assert text in home, ('education or contact missing', text)
for asset in ['academic.css']:
    assert (site / 'assets/css' / asset).is_file(), asset
for asset in ['prof_pic.jpg', 'sust-award.webp', 'horse-sampling.webp', 'gau-poster.webp']:
    assert (site / 'assets/img' / asset).is_file(), asset
for demo in ['blog', 'projects', 'people', 'books', 'teaching']:
    assert not (site / demo).exists(), ('template route still published', demo)
print('Academic pages, education, contact, images, and search index passed.')
