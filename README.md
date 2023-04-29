# GoogleScholar Badge Generator

[shields.io](https://shields.io) does not provide an API to help generate citation badges of articles/profiles 
on Google Scholar. Therefore, I create this repository to build us such a tool.
Need citation badges but cannot find a proper tool? Try GSBG!

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