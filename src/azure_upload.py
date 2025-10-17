
"""Uploader un fichier vers Azure Blob Storage (exemple).
ATTENTION: ne commentez jamais de secrets. Utilisez des variables d'environnement.
"""
import os
from pathlib import Path
from azure.storage.blob import BlobServiceClient

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "REPLACE_ME")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER", "demo-container")
LOCAL_FILE = os.getenv("LOCAL_FILE", str(Path(__file__).resolve().parents[1] / "data" / "laundryflow_orders.csv"))
BLOB_NAME = os.getenv("BLOB_NAME", "laundryflow_orders.csv")

def main():
    if "REPLACE_ME" in CONNECTION_STRING:
        raise SystemExit("Configurez AZURE_STORAGE_CONNECTION_STRING avant d'exécuter.")
    svc = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container = svc.get_container_client(CONTAINER_NAME)
    try:
        container.create_container()
    except Exception:
        pass
    with open(LOCAL_FILE, "rb") as f:
        container.upload_blob(name=BLOB_NAME, data=f, overwrite=True)
    print(f"✅ Upload réussi: {BLOB_NAME} → container {CONTAINER_NAME}")

if __name__ == "__main__":
    main()
