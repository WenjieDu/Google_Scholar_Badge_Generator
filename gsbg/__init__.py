"""
The GoogleScholar Badge Generator package.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3


from gsbg.google_scholar_badge_generator import (
    fetch_article_citation_num,
    fetch_profile_citation_num,
    gene_citation_badge_link,
    gene_citation_badge_svg,
)

__version__ = "0.1.2"

__all__ = [
    "fetch_article_citation_num",
    "fetch_profile_citation_num",
    "gene_citation_badge_link",
    "gene_citation_badge_svg",
    "__version__",
]
