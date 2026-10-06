class ListToDictConverter:
    def convert(self, photos_list):
        photo_entries_by_name = {
            entry.photo_name: entry
            for entry in photos_list
            }
        return photo_entries_by_name