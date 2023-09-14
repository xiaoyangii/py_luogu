import unittest
from frontend import get_url

class TestGetUrl(unittest.TestCase):

    # def test_with_keyword(self):
    #     keyword_entry = "编程"
    #     selected_difficulty = "0"
    #     selected_type = "B%7CP"
    #     url, params, doc_name = get_url(keyword_entry, selected_difficulty, selected_type)
    #     expected_url = "https://www.luogu.com.cn/problem/list?type=B%7CP&difficulty=0&keyword=编程&page=1"
    #     expected_params = {"difficulty": "0", "type": "B%7CP", "page": 1, "_contentOnly": 1}
    #     expected_doc_name = "暂无评定-编程"
    #     self.assertEqual(url, expected_url)
    #     self.assertEqual(params, expected_params)
    #     self.assertEqual(doc_name, expected_doc_name)

    def test_without_keyword(self):
        keyword_entry = ""
        selected_difficulty = "1"
        selected_type = "B%7CP"
        url, params, doc_name = get_url(keyword_entry, selected_difficulty, selected_type)
        expected_url = "https://www.luogu.com.cn/problem/list?type=B%7CP&difficulty=1&keyword=&page=1"
        expected_params = {"difficulty": "1", "type": "B%7CP", "page": 1, "_contentOnly": 1}
        expected_doc_name = "入门-无关键词"
        self.assertEqual(url, expected_url)
        self.assertEqual(params, expected_params)
        self.assertEqual(doc_name, expected_doc_name)

if __name__ == '__main__':
    unittest.main()