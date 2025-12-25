import unittest
import ddl

class TestDDLUtils(unittest.TestCase):
    def test_get_readable_time(self):
        self.assertEqual(ddl.get_readable_time(0), "0s")
        self.assertEqual(ddl.get_readable_time(59), "59s")
        self.assertEqual(ddl.get_readable_time(60), "1m0s")
        self.assertEqual(ddl.get_readable_time(61), "1m1s")
        self.assertEqual(ddl.get_readable_time(3600), "1h0m0s")
        self.assertEqual(ddl.get_readable_time(3661), "1h1m1s")
        self.assertEqual(ddl.get_readable_time(86400), "1d0h0m0s")
        self.assertEqual(ddl.get_readable_time(90061), "1d1h1m1s")

    def test_is_share_link(self):
        # Matching links
        self.assertTrue(ddl.is_share_link("https://new1.gdtot.cfd/file/123"))
        self.assertTrue(ddl.is_share_link("https://filepress.store/file/123"))
        self.assertTrue(ddl.is_share_link("https://appdrive.in/file/123"))
        self.assertTrue(ddl.is_share_link("https://gdflix.top/file/123"))
        self.assertTrue(ddl.is_share_link("https://driveseed.net/file/123"))

        # Non-matching links
        self.assertFalse(ddl.is_share_link("https://google.com"))
        self.assertFalse(ddl.is_share_link("http://example.com"))

if __name__ == '__main__':
    unittest.main()
