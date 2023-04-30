# GoogleScholar Badge Generator

[shields.io](https://shields.io) does not provide an API to help generate citation badges of articles/profiles 
on Google Scholar. Therefore, I create this repository to build us such a tool.
Need citation badges but cannot find a proper tool? Try GSBG! You can even make yourself a GoogleScholar version of shields.io with GitHub actions! Take a look at [Usage](-usage) below. 

Please star🌟 this repo to help others notice GSBG if you think it is useful. Thank you!

## ❖ Installation
You can install GSBG via pip: `pip install gsbg`, or from the latest source code: 
`pip install https://github.com/WenjieDu/Google_Scholar_Badge_Generator/archive/main.zip`.

## ❖ Usage
Apart from the below examples, you can also integrate GSBG with GitHub workflows to automatically generate badges 
for your articles/profiles, save them in your repo, and update them periodically.
Please take a look at [https://github.com/WenjieDu/WenjieDu](https://github.com/WenjieDu/WenjieDu) for an example.
The workflow [.github/workflows/gene_citation_badges.yml](https://github.com/WenjieDu/WenjieDu/blob/main/.github/workflows/gene_citation_badges.yml)
will regularly run the generating script [scripts/gene_google_scholar_badges.py](https://github.com/WenjieDu/WenjieDu/blob/main/scripts/gene_google_scholar_badges.py)
to maintain the badges under [figs/citation_badges](https://github.com/WenjieDu/WenjieDu/tree/main/figs/citation_badges).

You can fork my repo and modify the script and the workflow to fit your own needs.
If you meet any question, please [raise an issue](https://github.com/WenjieDu/Google_Scholar_Badge_Generator/issues).
I'll try my best to help.


```python
import gsbg

article_link = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ&citation_for_view=j9qvUg0AAAAJ:Y0pCki6q_DkC"
profile_link = "https://scholar.google.com/citations?user=j9qvUg0AAAAJ&hl=en"

article_citation_num = gsbg.fetch_article_citation_num(article_link)
profile_citation_num = gsbg.fetch_profile_citation_num(profile_link)
gsbg.gene_citation_badge_link(
    link='https://scholar.google.com/citations?user=j9qvUg0AAAAJ&hl=en', 
    link_type="profile",
)
gsbg.gene_citation_badge_svg(
    link='https://scholar.google.com/citations?user=j9qvUg0AAAAJ&hl=en', 
    link_type="profile",
    svg_name='gsbg.svg',
    path_to_save='generated_badges',
)
```


<details>
<summary>🏠 Visits</summary>
<a href="https://github.com/WenjieDu/GSBG">
    <img alt="GSBG visits" align="left" src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWenjieDu%2FGSBG&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false">
</a>
</details>
