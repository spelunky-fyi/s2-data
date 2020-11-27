#!/usr/bin/env python3

import io
import sys
import zlib

from s2_data import field_descriptors


def field_range(descriptor):
    field_start = descriptor.offset
    field_end = descriptor.offset + descriptor.type.size
    return field_start, field_end


def read_field(save, descriptor):
    start, end = field_range(descriptor)
    value = descriptor.type.from_binary(save[start:end])
    return value


def to_text():
    with io.open(sys.argv[1], 'rb') as save_file:
        save = save_file.read()

        for category_key, category in field_descriptors.items():
            print('##', category.name, end='\n\n')

            for dkey, descriptor in category.fields.items():
                value = read_field(save, descriptor)

                print(f'{descriptor.name:30} =', value)

            print(end='\n\n')
