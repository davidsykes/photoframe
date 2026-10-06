from pathlib import Path
import unittest

from photo_set_builder.src.data.photo_entry import PhotoEntry
from photo_set_builder.src.logic.list_to_dict_converter import ListToDictConverter


class ListToDictConverterTests(unittest.TestCase):
    def test_the_list_is_converted_to_a_dictionary(self):
        result = self.out.convert(self.list_to_convert)

        self.assertEqual(result, self.expected_dictionary)

    def setUp(self):
        self.out = ListToDictConverter()
        self.list_to_convert = [
            PhotoEntry(source_path=Path('path/to/source1.jpg'),
                       relative_path=Path('relative/path1.jpg'),
                       output_name='output1'),
            PhotoEntry(source_path=Path('path/to/source2.jpg'),
                       relative_path=Path('relative/path2.jpg'),
                       output_name='output2'),
            PhotoEntry(source_path=Path('path/to/source3.jpg'),
                       relative_path=Path('relative/path3.jpg'),
                       output_name='output3')
        ]
        self.expected_dictionary = {
            'output1': self.list_to_convert[0],
            'output2': self.list_to_convert[1],
            'output3': self.list_to_convert[2]
        }
