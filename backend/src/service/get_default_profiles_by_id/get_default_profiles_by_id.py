from functools import lru_cache
import json
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict
from src.dtos.predict_request_dto import Locale, PredictRequestDTO
from src.service.get_default_profiles.get_default_profiles import DefaultProfilesGetter
from src.service.process_predict_request.process_predict_request import (
    PredictRequestProcessor,
)

log: Logger = getLogger(__name__)


class DefaultProfilesByIdGetter:

    def __init__(
        self,
        profiles_getter: DefaultProfilesGetter,
        predict_request_processor: PredictRequestProcessor,
    ):
        self._profiles_getter = profiles_getter
        self._predict_request_processor = predict_request_processor

    @lru_cache(maxsize=10)
    def get(self, profile_id: int, accept_language: Locale) -> dict:
        try:
            if type(accept_language) is not Locale:
                raise TypeError(
                    f"Invalid type for accept_language: '{type(accept_language)}'. Must be 'Locale'."
                )

            if type(profile_id) is not int:
                raise TypeError(
                    f"Invalid type for profile_id: '{type(profile_id)}'. Must be 'int'."
                )

            profiles_dir = self._profiles_getter.PROFILES_DIR / accept_language.value

            if not profiles_dir.is_dir():
                raise FileNotFoundError(
                    f"Directory for locale '{accept_language.value}' not found."
                )

            profile_file = f"profile_{profile_id}.json"

            if not (profiles_dir / profile_file).is_file():
                raise FileNotFoundError(
                    f"Profile with id '{profile_id}' not found for locale '{accept_language.value}'."
                )

            profile_data = self._load_profile(profiles_dir / profile_file)

            profile_predict = self._predict_request_processor.process(
                PredictRequestDTO.model_validate(profile_data["predict_input"])
            )

            profile_output = {
                "profile_info": {
                    "profile_id": profile_data["profile_id"],
                    "title": profile_data["title"],
                },
                "predict_input": profile_data["predict_input"],
                "predict_output": profile_predict,
            }

            return profile_output

        except Exception as e:
            log.error("Failed to get default profiles by id: %s", e)
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
            return json.load(file)

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
