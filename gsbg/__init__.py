"""
The GoogleScholar Badge Generator package.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3


from gsbg.google_scholar_badge_generator import (
    get_random_header,
    fetch_selected_element_from_page,
    fetch_article_citation_num,
    fetch_profile_citation_num,
    gene_citation_badge_link,
    gene_citation_badge_svg,
)

__version__ = "0.1.3"

__all__ = [
    "get_random_header",
    "fetch_selected_element_from_page",
    "fetch_article_citation_num",
    "fetch_profile_citation_num",
    "gene_citation_badge_link",
    "gene_citation_badge_svg",
    "__version__",
]
