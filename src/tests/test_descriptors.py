from unittest import TestCase, main
import s2_data
import re


dict_key_regex = re.compile('^[a-z][a-z0-9_]*$')


class DescriptorsTestCase(TestCase):

    def test_category_key_names(self):
        for key in s2_data.field_descriptors.keys():
            self.assertTrue(dict_key_regex.match(key))

    def test_descriptor_key_names(self):
        for category in s2_data.field_descriptors.values():
            for key in category.fields.keys():
                self.assertTrue(dict_key_regex.match(key), key)


if __name__ == '__main__':
    main()
