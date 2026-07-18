from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import os
import shutil

class RemoteFilesRetriever:
    def __init__(self, system_operations, local_storage_path):
        self._system_operations = system_operations
        self.local_storage_path = local_storage_path

    def download_file(self, url: str, destination: Path) -> None:
        self._system_operations.log("Downloading file: " + url)
        destination = Path(destination)
        temporary_file = destination.with_suffix(destination.suffix + ".tmp")
        self._system_operations.log("Temporary file: " + str(temporary_file))

        request = Request(
            url,
            headers={"User-Agent": "PhotoFrame/1.0"},
        )

        try:
            self._system_operations.log("Make request to URL: " + url)
            with urlopen(request, timeout=30) as response:
                with temporary_file.open("wb") as output:
                    shutil.copyfileobj(response, output)

            self._system_operations.log("Replacing temporary file with destination file: " + str(destination))
            os.replace(temporary_file, destination)

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