import struct
import io
from dataclasses import dataclass
from field_descriptors import field_descriptors
import sys

with io.open(sys.argv[1], 'rb') as save_file:
    save = save_file.read()

    for category, elements in field_descriptors.items():
        print('##', category, end='\n\n')

        for element in elements:
            field_start = element.offset
            field_end = element.offset + element.type.size

            value = element.type.from_binary(save[field_start:field_end])

            print(f'{element.name:30} = {value}')

        print(end='\n\n')
