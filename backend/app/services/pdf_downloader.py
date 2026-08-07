import os 
from pathlib import Path
import requests

class PDFDownloader:
    def __init__(self):
        self.base_folder=Path("data/reports")
        self.base_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def download(self, company: str, pdf_url: str):

        company_folder = self.base_folder / company.lower().replace(" ", "_")

        company_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        filename = pdf_url.split("/")[-1].split("?")[0]

        save_path = company_folder / filename

        response = requests.get(
            pdf_url,
            timeout=30,
            stream=True
        )

        response.raise_for_status()

        with open(save_path, "wb") as f:

            for chunk in response.iter_content(8192):

                f.write(chunk)

        return {
            "filename": filename,
            "local_path": str(save_path),
            "file_size": os.path.getsize(save_path)
        }
