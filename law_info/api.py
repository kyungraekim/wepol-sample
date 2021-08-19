import json

import requests as requests
import xmltodict


class LawInfoRequest:
    URL_BASE = 'http://apis.data.go.kr/1170000/law'
    ADMIN_RULE = 'admrul'  # 행정규칙정보
    LAW_INFO = 'law'  # 법령정보
    ORDIN = 'ordin'  # 자치법규정보
    EXPC = 'expc'  # 법령해석례정보
    DETC = 'detc'  # 헌재결정례정보
    LICBYL = 'licbyl'  # 별표서식정보
    LSTRM = 'lstrm'  # 법령용어정보
    TRTY = 'trty'  # 조약정보

    def __init__(self, key, query, num_row, page_no):
        self._key = key
        self._query = query
        self._num_row = num_row
        self._page_no = page_no
        self._make_urls()

    def _make_urls(self):
        self.admin_rule = self._quote_urls(self.ADMIN_RULE)
        self.law = self._quote_urls(self.LAW_INFO)
        self.ordin = self._quote_urls(self.ORDIN)
        self.expc = self._quote_urls(self.EXPC)
        self.detc = self._quote_urls(self.DETC)
        self.licbyl = self._quote_urls(self.LICBYL)
        self.lstrm = self._quote_urls(self.LSTRM)
        self.trty = self._quote_urls(self.TRTY)

    def _quote_urls(self, target):
        quote = '&'.join([
            f'serviceKey={self._key}',
            f'target={target}',
            f'query={self._query}',
            f'numOfRows={self._num_row}',
            f'pageNo={self._page_no}'
        ])
        return f'{self.URL_BASE}/{target}SearchList.do?' + quote

    def get_admin_rule(self):
        return requests.get(self.admin_rule)

    def get_law_info(self):
        return requests.get(self.law)

    def get_ordin_info(self):
        return requests.get(self.ordin)

    def get_expc_info(self):
        return requests.get(self.expc)

    def get_detc_info(self):
        return requests.get(self.detc)

    def get_licbyl_info(self):
        return requests.get(self.licbyl)

    def get_lstrm_info(self):
        return requests.get(self.lstrm)

    def get_trty_info(self):
        return requests.get(self.trty)


def xmltext_to_dict(xml_text):
    return xmltodict.parse(xml_text)


def print_dict_from_xmltext(xml_text):
    print(json.dumps(xmltodict.parse(xml_text), indent=2, ensure_ascii=False))
