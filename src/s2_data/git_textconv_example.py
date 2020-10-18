import struct
import io
from dataclasses import dataclass
from field_descriptors import field_descriptors
import sys

with io.open(sys.argv[1], 'rb') as save_file:
    save = save_file.read()

    for category_key, category in field_descriptors.items():
        print('##', category.name, end='\n\n')

        for dkey, descriptor in category.fields.items():
            field_start = descriptor.offset
            field_end = descriptor.offset + descriptor.type.size

            value = descriptor.type.from_binary(save[field_start:field_end])

            print(f'{descriptor.name:30} =', value)

        print(end='\n\n')
