import json
import logging
from logging import config
import pathlib

from assertpy import assert_that
from requests import Response

from lesson_23.core.api.petstore_api_service import PetstoreApiService
from lesson_23.core.test_data.json_parser import JSONParser
from lesson_23.core.test_data.pet_store_api_endpoints import PetStoreApiEndpoints
from lesson_23.core.test_data.pet_store_api_test_data import test_pet_item, test_pet_item_edit, \
    pet_not_found_error_message


def setup_logging():
    config_file = pathlib.Path("your_path_to_configuration_file")
    with open(config_file) as file:
        desired_configuration = json.load(file)

    logging.config.dictConfig(desired_configuration)


logger = logging.getLogger(__name__)

class TestPetStoreAPI:

    setup_logging()
    authorization_api_key: str = "special-key"

    def test_that_user_can_create_new_pet_object_sold_it_and_successfully_delete(self):
        desired_pet: json = JSONParser.serialize_json_from_dict(test_pet_item)
        desired_pet_id: int = int(test_pet_item.get("id"))

        current_pet_sold: json = JSONParser.serialize_json_from_dict(test_pet_item_edit)

        logger.info("Creation of new pet object...")
        pet_creation: Response = PetstoreApiService.post_item(PetStoreApiEndpoints.PET.value, desired_pet)

        assert_that(pet_creation.status_code, "Pet object was not created successfully.").is_equal_to(200)
        assert_that(pet_creation.json()).is_equal_to(test_pet_item)

        logger.info(f"Update created pet object with new status {test_pet_item_edit.get('status')}")
        pet_updating: Response = PetstoreApiService.put_item(PetStoreApiEndpoints.PET.value, current_pet_sold)

        assert_that(pet_updating.status_code).is_equal_to(200)
        assert_that(pet_updating.json()).is_equal_to(test_pet_item_edit)

        logger.info(f"Extracting of desired Pet Object that was created with id {test_pet_item_edit.get('id')}")
        get_desired_pet: Response = PetstoreApiService.get_item(f"{PetStoreApiEndpoints.PET.value}/{desired_pet_id}")
        assert_that(pet_updating.status_code).is_equal_to(200)

        logger.info(f"Validating that existed pet object has expected status {test_pet_item_edit.get('status')}")
        current_item_status: str = get_desired_pet.json().get("status")
        assert_that(current_item_status).is_equal_to(test_pet_item_edit.get("status"))

        params: dict[str, str] = {"api_key": self.authorization_api_key}

        logger.info(f"Deletion of pet object with id {test_pet_item_edit.get('id')}")
        current_item_deletion: Response = PetstoreApiService.delete_item_with_parameters(
            f"{PetStoreApiEndpoints.PET.value}/{desired_pet_id}", params)

        assert_that(current_item_deletion.status_code).is_equal_to(200)

        logger.info(f"Validating that after deletion there is NO pet object with id {test_pet_item_edit.get('id')}")
        get_desired_pet: Response = PetstoreApiService.get_item(f"{PetStoreApiEndpoints.PET.value}/{desired_pet_id}")

        assert_that(get_desired_pet.status_code).is_equal_to(404)
        assert_that(get_desired_pet.json().get("message")).is_equal_to(pet_not_found_error_message)


