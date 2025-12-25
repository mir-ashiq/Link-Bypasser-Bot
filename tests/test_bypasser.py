import unittest
from unittest.mock import patch, MagicMock
import bypasser
import base64

class TestBypasser(unittest.TestCase):

    def test_shortner_fpage_api(self):
        # Prepare a valid URL
        target_url = "https://google.com"
        encoded_url = base64.b64encode(target_url.encode("utf-8")).decode("utf-8")
        test_link = f"https://example.com/full?api=someapikey&url={encoded_url}"

        result = bypasser.shortner_fpage_api(test_link)
        self.assertEqual(result, target_url)

        # Test invalid link
        self.assertIsNone(bypasser.shortner_fpage_api("https://invalid.com"))

    def test_shortner_quick_api(self):
        target_url = "https://google.com"
        test_link = f"https://example.com/st?api=someapikey&url={target_url}"

        result = bypasser.shortner_quick_api(test_link)
        self.assertEqual(result, target_url)

        # Test invalid link
        self.assertIsNone(bypasser.shortner_quick_api("https://invalid.com"))

    def test_ispresent(self):
        # Test helper function
        whitelist = ["example.com", "google.com"]
        self.assertTrue(bypasser.ispresent(whitelist, "https://example.com/foo"))
        self.assertTrue(bypasser.ispresent(whitelist, "https://google.com/bar"))
        self.assertFalse(bypasser.ispresent(whitelist, "https://yahoo.com"))

    @patch('bypasser.requests.get')
    def test_bitly_tinyurl(self, mock_get):
        # Setup mock
        expected_url = "https://destination.com"
        mock_response = MagicMock()
        mock_response.url = expected_url
        mock_get.return_value = mock_response

        # Call function
        result = bypasser.bitly_tinyurl("https://bit.ly/sometoken")

        # Assertions
        self.assertEqual(result, expected_url)
        mock_get.assert_called_with("https://bit.ly/sometoken")

    @patch('bypasser.requests.get')
    def test_thinfi(self, mock_get):
        # Setup mock for success case
        expected_url = "https://destination.com"
        html_content = f'<html><body><p><a href="{expected_url}">Click here</a></p></body></html>'

        mock_response = MagicMock()
        mock_response.content = html_content.encode('utf-8')
        mock_get.return_value = mock_response

        # Call function
        result = bypasser.thinfi("https://thinfi.com/sometoken")

        # Assertions
        self.assertEqual(result, expected_url)
        mock_get.assert_called_with("https://thinfi.com/sometoken")

    @patch('bypasser.requests.get')
    def test_thinfi_failure(self, mock_get):
        # Setup mock for failure case (exception)
        mock_get.side_effect = Exception("Network error")

        # Call function
        result = bypasser.thinfi("https://thinfi.com/sometoken")

        # Assertions
        self.assertEqual(result, "Something went wrong :(")

if __name__ == '__main__':
    unittest.main()
