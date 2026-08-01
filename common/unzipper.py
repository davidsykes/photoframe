import zipfile


class UnZipper:
    def unzip(self, zip_path, destination):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination)
        return True