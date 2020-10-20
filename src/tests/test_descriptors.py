from unittest import TestCase, main
import s2_data
import re
from itertools import chain


dict_key_regex = re.compile('^[a-z][a-z0-9_]*$')


class DescriptorsTestCase(TestCase):

    def test_category_key_names(self):
        for key in s2_data.field_descriptors.keys():
            self.assertTrue(dict_key_regex.match(key))

    def test_descriptor_key_names(self):
        for category in s2_data.field_descriptors.values():
            for key in category.fields.keys():
                self.assertTrue(dict_key_regex.match(key), key)

    def test_descriptors_dont_overlap(self):
        """Fields should never share bytes."""
        categories = s2_data.field_descriptors.values()
        descriptors = list(chain(*[c.fields.values() for c in categories]))
        # Order by offset so we only have to check whether a field overlaps
        # with the following field.
        by_offset = sorted(descriptors, key=lambda d: d.offset)

        current = by_offset[0]
        for next_ in by_offset[1:]:
            with self.subTest(current=current, next_=next_):
                current_end = current.offset + current.type.size
                self.assertLessEqual(current_end, next_.offset)

                current = next_


if __name__ == '__main__':
    main()
