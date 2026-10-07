class PhotosSynchroniser:
    def __init__(self,
                 list_to_dict_converter,
                 photos_compressor,
                 compressed_photos_remover):
           self._list_to_dict_converter = list_to_dict_converter
           self._photos_compressor = photos_compressor
           self._compressed_photos_remover = compressed_photos_remover

    def synchronise_photos(self,
                           photos_list,
                           compressed_photos_list,
                           compressed_photos_folder):
          photos_dictionary = self._list_to_dict_converter.convert(
                photos_list)
          compressed_photos_dictionary = self._list_to_dict_converter.convert(
                compressed_photos_list)
          self._photos_compressor.compress_photos(
                photos_list,
                compressed_photos_dictionary,
                compressed_photos_folder
          )
          self._compressed_photos_remover.remove_compressed_photos(
                compressed_photos_list,
                photos_dictionary,
                compressed_photos_folder
          )
        