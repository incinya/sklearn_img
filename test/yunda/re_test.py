import re


def remove_html_tag(html):
    # return re.sub('<.*?>.*?>', '', html)
    return re.sub('<.*?>', '', html)


def get_filter(text):
    if not text:
        return ''
    if isinstance(text, list):
        text = ''.join(text)
    filter_list = [
        '\r', '\n', '\t', '\u3000', '\xa0', '\u2003', '\u2009',
        '<br>', '<br/>', '    ', '	', ' ', '&nbsp;', '>>', '↵', '展开全部', '</span>'
    ]
    for fl in filter_list:
        text = text.replace(fl, '')
    return text


def data_processing(html):
    html_list = html.split(";")
    result = list()
    for i in html_list:
        data = i.split(",")
        if len(data) == 2:
            _time = data[0]
            context = remove_html_tag(get_filter(data[1]))
            result.append({
                "_time": _time,
                "context": context
            })
        else:
            del data
            continue
    print(result)
    return result
