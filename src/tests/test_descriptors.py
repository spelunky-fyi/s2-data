import s2_data
import re
import os
from unittest import TestCase, main
from itertools import chain


dict_key_regex = re.compile('^[a-z][a-z0-9_]*$')
save_game_path = os.path.join(
    os.path.dirname(__file__),
    '../../data/saves/mostly-full-savegame.sav')

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

    def test_writing_current_value_is_noop(self):
        """Converting a field's bytes to a value and back into bytes should
        always succeed and the final bytes should be the same as the original
        bytes."""
        with open(save_game_path, 'rb') as save_file:
            save = save_file.read()

            for category in s2_data.field_descriptors.values():
                for field_descriptor in category.fields.values():
                    with self.subTest(category=category.name, field=field_descriptor.name):
                        field_start = field_descriptor.offset
                        field_end = field_start + field_descriptor.type.size
                        field_bytes = save[field_start:field_end]
                        value = field_descriptor.type.from_binary(field_bytes)
                        bytes_ = field_descriptor.type.to_binary(value)
                        self.assertEqual(field_bytes, bytes_)


if __name__ == '__main__':
    main()
