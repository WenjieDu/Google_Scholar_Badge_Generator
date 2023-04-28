"""
Storing the functions of GSBG.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

import os

import bs4
import requests
from bs4 import BeautifulSoup
import warnings

ARTICLE_CITATION_SELECTOR = (
    "#gsc_oci_table > div:nth-child(6) > div.gsc_oci_value > div:nth-child(1) > a"
)
PROFILE_CITATION_SELECTOR = "#gsc_rsb_st > tbody > tr:nth-child(1) > td:nth-child(2)"


def fetch_selected_element_from_page(selector: str, page_url: str) -> bs4.element.Tag:
    """Fetch the selected element from the given page.

    Parameters
    ----------
    selector : str,
        A valid CSS selector.

    page_url : str,
        A valid URL, should contain the element selected by the given selector.

    Returns
    -------
    selected : bs4.element.Tag,
        The element selected by the given selector on the given page.

    """
    page = requests.get(page_url).text
    soup = BeautifulSoup(page, "html.parser")
    selected = soup.select_one(selector)
    if selected is None:
        print(soup.prettify())
        raise RuntimeError(
            f"Cannot find the element selected by {selector} on {page_url}. "
            f"This may caused by an invalid selector, an invalid page_url. "
            f"The reason also may be your IP address got blocked by the server. "
            f"The fetch html page got printed above, please check it to find more details."
        )
    return selected


def fetch_profile_citation_num(profile_link: str) -> int:
    """Parse the given GoogleScholar profile link and return its total citation number.

    Parameters
    ----------
    profile_link : str,
        A profile link on GoogleScholar. It must be a link to a valid profile.

    Returns
    -------
    profile_citation_number : int,
        The total citation number of the given profile.

    """
    citations_all = fetch_selected_element_from_page(
        selector=PROFILE_CITATION_SELECTOR,
        page_url=profile_link,
    )
    profile_citation_number = int(citations_all.text)
    return profile_citation_number


def fetch_article_citation_num(article_link: str) -> int:
    """Parse the given GoogleScholar article link and return its total citation number.

    Parameters
    ----------
    article_link : str,
        An article link on GoogleScholar. It must be a link to a valid article.

    Returns
    -------
    article_citation_number : int,
        The total citation number of the given article.

    """

    cited_by_num = fetch_selected_element_from_page(
        selector=ARTICLE_CITATION_SELECTOR,
        page_url=article_link,
    )
    article_citation_number = int(cited_by_num.text.split("Cited by ")[-1])
    return article_citation_number


def gene_citation_badge_link(link: str, link_type: str) -> str:
    """Generate a badge link for the given link.

    Parameters
    ----------
    link : str,
        A valid GoogleScholar link. It could be either a profile link or an article link.

    link_type: str,
        The type of the given link. It must be either "profile" or "article".

    Returns
    -------
    link : str,
        A link of the badge displaying the current total citation number of the given profile or article.

    """
    if link_type == "profile":
        citation_num = fetch_profile_citation_num(link)
    elif link_type == "article":
        citation_num = fetch_article_citation_num(link)
    else:
        raise ValueError(
            "Invalid type. link_type must be either 'profile' or 'article'."
        )

    link = f"https://img.shields.io/badge/Citations-{citation_num}-blue.svg?logo=google-scholar"
    warnings.warn(
        "Please note that the generated link of the badge only contains "
        "the citation number at this time point, and the citation number won't be updated."
    )
    return link


def gene_citation_badge_svg(
    link: str, link_type: str, svg_name: str, path_to_save: str
) -> None:
    """Generate a badge for the given link with the given name to the given path.

    Parameters
    ----------
    link : str,
        A valid GoogleScholar link. It could be either a profile link or an article link.

    link_type: str,
        The type of the given link. It must be either "profile" or "article".

    svg_name : str,
        The name of the generated badge.

    path_to_save : str,
        The path to save the generated badge. If it doesn't exist, it will be created.

    """
    try:
        if link_type == "profile":
            citation_num = fetch_profile_citation_num(link)
        elif link_type == "article":
            citation_num = fetch_article_citation_num(link)
        else:
            raise ValueError(
                "Invalid type. link_type must be either 'profile' or 'article'."
            )

        link = f"https://img.shields.io/badge/Citations-{citation_num}-blue.svg?logo=google-scholar"

        os.makedirs(path_to_save)
        if svg_name.endswith(".svg"):
            svg_name = f"{svg_name}.svg"
        saving_path = os.path.join(path_to_save, svg_name)
        with open(saving_path, "wb") as file_handle:
            file_handle.write(requests.get(link).content)
    except Exception as e:
        print("Generating failed.")
        raise e
    print(f"Saved to {saving_path}. Please check out your badge there.")
