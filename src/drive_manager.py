import os.path
from typing import Optional
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

class DriveManager:
    """Manages Google Drive actions, specifically uploading zip files."""

    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/drive.file"]

    def __init__(self, credentials_path: str = "credentials.json", token_path: str = "token.json") -> None:
        """
        Initializes the DriveManager.
        
        Args:
            credentials_path: Path to the Google Cloud credentials JSON file.
            token_path: Path where the access token will be stored after first login.
        """
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.creds = self._authenticate()
        self.service = build("drive", "v3", credentials=self.creds)

    def _authenticate(self) -> Credentials:
        """Handles the OAuth2 authentication flow."""
        creds = None
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except RefreshError:
                    print("Token refresh failed. Re-authenticating...")
                    creds = None
            
            if not creds or not creds.valid:
                if not os.path.exists(self.credentials_path):
                    raise FileNotFoundError(
                        f"'{self.credentials_path}' not found. Please download it from "
                        "Google Cloud Console and place it in the project root."
                    )
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open(self.token_path, "w") as token:
                token.write(creds.to_json())
        
        return creds

    def upload_zip(self, file_path: str, folder_id: Optional[str] = None) -> Optional[str]:
        """
        Uploads a zip file to a specific Google Drive folder.
        
        Args:
            file_path: Local path to the zip file.
            folder_id: The ID of the target Google Drive folder.
            
        Returns:
            The ID of the uploaded file if successful, None otherwise.
            
        Example:
            drive.upload_zip("my_data.zip", folder_id="1abc123...xyz")
        """
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return None

        file_metadata = {"name": os.path.basename(file_path)}
        if folder_id:
            file_metadata["parents"] = [folder_id]

        try:
            media = MediaFileUpload(file_path, mimetype="application/zip", resumable=True)
            file = (
                self.service.files()
                .create(body=file_metadata, media_body=media, fields="id")
                .execute()
            )
            file_id = file.get("id")
            print(f"File uploaded successfully. File ID: {file_id}")
            return file_id

        except HttpError as error:
            print(f"An error occurred during upload: {error}")
            return None
