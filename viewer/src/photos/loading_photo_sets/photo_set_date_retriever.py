from datetime import date


class PhotoSetDateRetriever:
    def get_photo_set_date(self, set_name, config):
        photo_folders = config.photo_folders
        for folder in photo_folders:
            if folder[0] == set_name:
                if len(folder) > 3:
                    return folder[3]
        return date.min