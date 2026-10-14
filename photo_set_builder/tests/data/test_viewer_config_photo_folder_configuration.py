import unittest

from photo_set_builder.src.data.viewer_config_photo_folder_configuration import ViewerConfigPhotoFolderConfiguration



class ViewerConfigPhotoFolderConfigurationTests(unittest.TestCase):
    def test_a_config_can_be_initialised_from_an_array(self):
        out = ViewerConfigPhotoFolderConfiguration(
                    ['Name', 'db', 'filter', 'date']
                )       
        self.assertEqual(out.name, 'Name')
        self.assertEqual(out.version, 0)
        self.assertEqual(out.date, 'date')
        
    def test_insufficient_entries_throw_an_exception(self):
        with self.assertRaises(Exception):
            out = ViewerConfigPhotoFolderConfiguration(
                ['Name','dropbox', 'filter']
                )

    def test_names_can_have_spaces(self):
        out = ViewerConfigPhotoFolderConfiguration(
                    ['Name 1', 'db', 'filter', 'date']
                )       
        self.assertEqual(out.name, 'Name 1')
        self.assertEqual(out.version, 0)

    def test_versioned_configuration_can_be_retrieved(self):
        out = ViewerConfigPhotoFolderConfiguration(
                    ['Basename-123', 'db', 'filter', 'date']
                )       
        self.assertEqual(out.name, 'Basename')
        self.assertEqual(out.version, 123)

    def test_update_version(self):
        out = ViewerConfigPhotoFolderConfiguration(
                    ['Basename-123', 'db', 'filter', 'date']
                )       
        out.update_version()

        self.assertEqual(out.name, 'Basename')
        self.assertEqual(out.version, 124)

    def test_the_date_can_be_retrieved(self):
        out = ViewerConfigPhotoFolderConfiguration(
                    ['Basename-123', 'dropbox', 'filter', 'date']
                )       

        self.assertEqual(out.date, 'date')

    def test_the_date_can_be_updated(self):
        out = ViewerConfigPhotoFolderConfiguration(
                    ['Basename-123', 'dropbox', 'filter', 'date']
                )       
        out.update_date('new date')

        self.assertEqual(out.date, 'new date')