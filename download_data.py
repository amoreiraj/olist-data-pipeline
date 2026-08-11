"""Download the Olist Brazilian e-commerce dataset from Kaggle.

Prerequisites:
    1. Install dependencies from requirements.txt.
    2. Configure Kaggle authentication locally.

The dataset is downloaded into data/ and is intentionally excluded from Git.
"""

from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATASET = "olistbr/brazilian-ecommerce"


def download_dataset() -> None:
    """Download and extract the Olist dataset into the local data directory."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Starting Olist dataset download...")
    print(f"Destination: {DATA_DIR}")

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        DATASET,
        path=str(DATA_DIR),
        unzip=True,
    )

    csv_files = sorted(DATA_DIR.glob("*.csv"))
    print(f"Download complete. Found {len(csv_files)} CSV files:")

    for file_path in csv_files:
        print(f"  - {file_path.name}")


if __name__ == "__main__":
    download_dataset()
