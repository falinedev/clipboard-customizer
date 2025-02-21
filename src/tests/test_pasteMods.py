from pasteMods_v1 import clean_links, clean_lines, clean_markdown

def test_clean_links():
    assert clean_links('![Logo](https://website.com)') == 'https://website.com'
    assert clean_links('[Link Name](https://www.website2.com)') == 'https://www.website2.com'

def test_clean_lines():
    assert clean_lines('Here is some text\n   And more text') == 'Here is some text\nAnd more text'

def test_clean_markdown():
    assert clean_markdown('## Headers # H1 ## H2 ### H3 #### H4 ##### H5 ###### H6') == 'Headers  H1  H2  H3  H4  H5  H6'