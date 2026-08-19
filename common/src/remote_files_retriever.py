from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import os
import shutil
from zipfile import ZipFile

class RemoteFilesRetriever:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def download_file_or_return_false(self, url: str, destination: str) -> str:
        temporary_file = destination.with_suffix(destination.suffix + ".tmp")

        request = Request(
            url,
            headers={"User-Agent": "PhotoFrame/1.0"},
        )

        try:
            with urlopen(request, timeout=30) as response:
                with temporary_file.open("wb") as output:
                    shutil.copyfileobj(response, output)

            os.replace(temporary_file, destination)
            return True

        except HTTPError as ex:
            temporary_file.unlink(missing_ok=True)
            self._system_operations.error(
                f"Could not download '{url}': HTTP error {ex.code} {ex.reason}"
            )

        except URLError as ex:
            temporary_file.unlink(missing_ok=True)
            self._system_operations.error(
                f"Could not download '{url}': {ex.reason}"
            )

        except OSError as ex:
            temporary_file.unlink(missing_ok=True)
            self._system_operations.error(
                f"Could not save downloaded file as '{destination}': {ex}"
            )
        return False

    def download_file_or_raise_exception(self, url: str, destination: str) -> str:
        temporary_file = destination.with_suffix(destination.suffix + ".tmp")

        request = Request(
            url,
            headers={"User-Agent": "PhotoFrame/1.0"},
        )

        try:
            with urlopen(request, timeout=30) as response:
                with temporary_file.open("wb") as output:
                    shutil.copyfileobj(response, output)

            os.replace(temporary_file, destination)
            return True

        except HTTPError as ex:
            temporary_file.unlink(missing_ok=True)
            raise RuntimeError(
                f"Could not download '{url}': HTTP error {ex.code} {ex.reason}"
            ) from ex

        except URLError as ex:
            temporary_file.unlink(missing_ok=True)
            raise RuntimeError(
                f"Could not download '{url}': {ex.reason}"
            ) from ex

        except OSError as ex:
            temporary_file.unlink(missing_ok=True)
            raise RuntimeError(
                f"Could not save downloaded file as '{destination}': {ex}"
            ) from ex

    def extract_release(zip_path: Path, target_folder: Path) -> None:
        with ZipFile(zip_path, "r") as archive:
            archive.extractall(target_folder)
