"""
Testing cases are here.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

from time import sleep
import os.path
import unittest

from gsbg import (
    fetch_article_citation_num,
    fetch_profile_citation_num,
    gene_citation_badge_link,
    gene_citation_badge_svg,
)


class TestCRLI(unittest.TestCase):
    os.environ["APPLY_MIRROR_SITES"] = "True"  # enable APPLY_MIRROR_SITES

    article_link = (
        "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ"
        "&citation_for_view=j9qvUg0AAAAJ:Y0pCki6q_DkC"
    )
    profile_link = "https://scholar.google.com/citations?user=j9qvUg0AAAAJ&hl=en"

    article_svg_name = "saits.svg"
    profile_svg_name = "wdu.svg"

    badge_saving_path = "generated_badges"

    def test_fetch_profile_citation_num(self):
        n_ = fetch_profile_citation_num(self.profile_link)
        assert isinstance(n_, int) and n_ > 0, "fetch_profile_citation_num failed"
        sleep(10)

    def test_fetch_article_citation_num(self):
        n_ = fetch_article_citation_num(self.article_link)
        assert isinstance(n_, int) and n_ > 0, "fetch_article_citation_num failed"
        sleep(10)

    def test_gene_citation_badge_link(self):
        l_ = gene_citation_badge_link(self.article_link, "article")
        assert (
            isinstance(l_, str) and "shields.io" in l_
        ), "gene_citation_badge_link failed with article_link"
        sleep(10)
        l_ = gene_citation_badge_link(self.profile_link, "profile")
        assert (
            isinstance(l_, str) and "shields.io" in l_
        ), "gene_citation_badge_link failed with profile_link"
        sleep(10)

    def test_gene_citation_badge_svg(self):
        gene_citation_badge_svg(
            self.article_link,
            "article",
            svg_name=self.article_svg_name,
            path_to_save=self.badge_saving_path,
        )
        assert os.path.exists(
            os.path.join(self.badge_saving_path, self.article_svg_name)
        ), "gene_citation_badge_svg failed with article_link"
        sleep(10)

        gene_citation_badge_svg(
            self.profile_link,
            "profile",
            svg_name=self.profile_svg_name,
            path_to_save=self.badge_saving_path,
        )
        assert os.path.exists(
            os.path.join(self.badge_saving_path, self.profile_svg_name)
        ), "gene_citation_badge_svg failed with profile_link"
        sleep(10)
