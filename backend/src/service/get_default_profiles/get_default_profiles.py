from functools import lru_cache
import json
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Dict
from src.dtos.predict_request_dto import Locale

log: Logger = getLogger(__name__)


class DefaultProfilesGetter:
    """
    A class responsible for retrieving and caching default profiles based on the specified locale.
    """

    PROFILES_DIR = Path("src/data/default_profiles")

    @lru_cache(maxsize=5)
    def get(self, accept_language: Locale) -> List[Dict[str, str]]:
        """
        Retrieves a list of default profiles for the given locale.

        Args:
            accept_language (Locale): The locale specifying which profiles to retrieve.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing profile_id and title.
        """
        try:
            if type(accept_language) is not Locale:
                raise TypeError(
                    f"Invalid type for accept_language: '{type(accept_language)}'. Must be 'Locale'."
                )

            profiles_dir = self.PROFILES_DIR / accept_language.value

            if not profiles_dir.is_dir():
                raise FileNotFoundError(
                    f"Directory for locale '{accept_language.value}' not found."
                )

            profiles = [
                self._load_profile(file_path)
                for file_path in profiles_dir.iterdir()
                if self._is_default_profile_file(file_path)
            ]

            return profiles
        except Exception as e:
            log.error("Failed to get default profiles: %s", e)
            raise e

    @staticmethod
    def _load_profile(file_path: Path) -> Dict[str, str]:
        """
        Loads a single profile from a JSON file.

        Args:
            file_path (Path): The path to the JSON file.

        Returns:
            Dict[str, str]: A dictionary containing profile_id and title.
        """
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return {
                "profile_id": data["profile_id"],
                "title": data["title"],
            }

    @staticmethod
    def _is_default_profile_file(file_path: Path) -> bool:
        """
        Checks if a file is a default profile file.

        Args:
            file_path (Path): The path to the file.

        Returns:
            bool: True if the file is a default profile file, False otherwise.
        """
        return (
            file_path.is_file()
            and file_path.name.startswith("profile")
            and file_path.suffix == ".json"
        )
