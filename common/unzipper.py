import zipfile


class UnZipper:
    def unzip(self, zip_path, destination):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(destination)
            return True
        except Exception as e:
            print(f"Error occurred while unzipping {zip_path}: {e}")
            return False