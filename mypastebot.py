import requests
import json


class Create:
    @staticmethod
    def getToken():
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        r = requests.get('https://pastebin.com/', headers=head)
        token = str(r.text).split('<input type="hidden" name="csrf_token_post" value="')[1].split('">')[0]
        return token

    @staticmethod
    def makePaste(text, title, format, token):
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }

        form = {
            'csrf_token_post': token,
            'submit_hidden': 'submit_hidden',
            'paste_code': text,
            'paste_format': format,
            'paste_expire_date': 'N',
            'paste_private': '1',
            'paste_name': title
        }
        r = requests.post('https://pastebin.com/post.php', data=form, headers=head)

        paste = str(r.text).split('<a href="/raw/')[1].split('" class="buttonsm">raw</a><a')[0]
        return {'link': f'https://pastebin.com/{paste}', 'raw': f'https://pastebin.com/raw/{paste}'}


class Search:
    @staticmethod
    def find(term, limit, sortType=''):
        # term = what to look for
        # limit = amount of results
        # sortType = '' for relevance, 'date' for by date
        if 1 > int(limit) < 15:
            raise Exception('limit is too high/low. Max is 15 and Low is 1')
        else:
            head = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
            }

            r = requests.get(
                f'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num={limit}&hl=en&source=gcsc&gss=.com&cselibv=c96da2eab22f03d8&cx=013305635491195529773:0ufpuq-fpt0&q={term}&safe=off&cse_tok=AKaTTZj_hK0kxSDV-tRpF0Ag5Qdj:1569960966506&sort={sortType}&exp=csqr,cc,4229469&callback=google.search.cse.api46',
                headers=head)
            j = str(r.text).split('/*O_o*/')[1].split('google.search.cse.api46(')[1].split(');')[0].splitlines()
            j = "".join(j)
            m = json.loads(j)
            results = {'results': []}
            for result in m['results']:
                k = {'title': result['titleNoFormatting'], 'link': result['unescapedUrl']}
                results['results'].append(k)
            return results

    @staticmethod
    def new(linkType=None):
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }

        r = requests.get('https://pastebin.com/archive', headers=head)

        html = r.text
        j = str(html).split('<table class="maintable">')[1].split('</table>')[0].splitlines()
        l = {'results': []}
        for element in j:
            try:
                link = element.split('<a href="/')[1].split('">')[0]
                if linkType == 'raw':
                    link = f'https://pastebin.com/raw/{link}'
                elif linkType == 'link':
                    link = f'https://pastebin.com/{link}'
                title = element.split('<a href="/')[1].split('">')[1].split('</a>')[0]
                k = {'title': title, 'link': link}
                l['results'].append(k)
            except:
                pass
        return l

