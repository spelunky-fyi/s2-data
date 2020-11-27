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


def write_field(save, descriptor, value):
    start, end = field_range(descriptor)
    save[start:end] = descriptor.type.to_binary(value)


def to_text():
    with io.open(sys.argv[1], 'rb') as save_file:
        save = save_file.read()

        for category_key, category in field_descriptors.items():
            print('##', category.name, end='\n\n')

            for dkey, descriptor in category.fields.items():
                value = read_field(save, descriptor)

                print(f'{descriptor.name:30} =', value)

            print(end='\n\n')


def fixup_crc():
    crc_descriptor = field_descriptors['crc'].fields['crc']
    with io.open(sys.argv[1], 'rb') as save_file:
        save = bytearray(save_file.read())
        current_crc = read_field(save, crc_descriptor)

    # Spelunky 2 needs a 32bit bitnot operation applied to the crc32.
    # ~ Doesn't work in Python because it can result in negative numbers,
    # but xor has the desired effect.
    correct_crc = 0xffffffff ^ zlib.crc32(save[2:-4])

    if current_crc == correct_crc:
        print('CRC already correct!')
        return

    write_field(save, crc_descriptor, correct_crc)
    with io.open(sys.argv[1], 'wb') as save_file:
        save_file.write(save)
        print(f"CRC was {current_crc}. Corrected to {correct_crc}.")
