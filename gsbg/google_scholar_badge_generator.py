"""
Storing the functions of GSBG.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

import logging
import os
import random
import warnings

import requests
from bs4 import BeautifulSoup, element

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s"
)


MIRROR_SITES = {
    "scholar.lanfanshu.cn": "True",  # 'True' means this mirror site is in Chinese
}

ARTICLE_CITATION_SELECTOR = "#gsc_oci_table > div > div.gsc_oci_value > div > a"
PROFILE_CITATION_SELECTOR = "#gsc_rsb_st > tbody > tr:nth-child(1) > td:nth-child(2)"

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
]


def get_header():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate",
    }


def apply_mirror_sites(link):
    site_to_use = random.choice(list(MIRROR_SITES.keys()))
    logging.info(f"Applying the mirror site '{site_to_use}'")
    os.environ["GS_MIRROR_SITE_IN_CHINESE"] = MIRROR_SITES[site_to_use]
    new_link = link.replace("scholar.google.com", site_to_use)
    logging.info(f"The updated URL is: {new_link}")
    return new_link


def fetch_selected_element_from_page(selector: str, page_url: str) -> element.Tag:
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
    if os.getenv("APPLY_MIRROR_SITES", "False") == "True":
        page_url = apply_mirror_sites(page_url)

    page = requests.get(page_url, headers=get_header()).text
    soup = BeautifulSoup(page, "html.parser")
    selected = soup.select_one(selector)
    if selected is None:
        logging.error(soup.prettify())
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
    if os.getenv("GS_MIRROR_SITE_IN_CHINESE", "False") == "True":
        article_citation_number = int(cited_by_num.text.split("被引用次数：")[-1])
    else:
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

        os.makedirs(path_to_save, exist_ok=True)
        if not svg_name.endswith(".svg"):
            svg_name = f"{svg_name}.svg"
        saving_path = os.path.join(path_to_save, svg_name)
        with open(saving_path, "wb") as file_handle:
            file_handle.write(requests.get(link).content)
    except Exception as e:
        logging.error("Generating failed.")
        raise e
    logging.info(f"Saved to {saving_path}. Please check out your badge there.")
