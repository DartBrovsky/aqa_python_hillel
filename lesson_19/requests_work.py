import json
from typing import Mapping

import requests
from assertpy import assert_that
from requests import Response

from lesson_19.test_data import get_expected_response_data, first_comment_query_dict, post_new_comment_body, \
    fifth_post_expected_data, expected_fifth_post_expected_data


class TestApiWithResponse:
    __base_url: str = "http://jsonplaceholder.typicode.com"

    __get_url: str = f"{__base_url}/posts/1/comments"
    __post_url: str = f"{__base_url}/posts"

    __base_header: Mapping[str, str] = {
        'Content-Type': 'application/json'
    }

    def test_get_request(self):
        response: Response = requests.get(self.__get_url, headers=self.__base_header)

        response_status_code: int = response.status_code
        response_data: json = response.json()

        (assert_that(response_status_code, f"Request GET was unsuccessful with status {response_status_code}")
         .is_equal_to(200))

        (assert_that(response_data, f"Data from response is not equal to expected.")
         .is_equal_to(get_expected_response_data))

    def test_get_request_with_parameters(self):
        response: Response = requests.get(self.__get_url, params=first_comment_query_dict, headers=self.__base_header)

        response_status_code: int = response.status_code
        response_data: json = response.json()

        (assert_that(response_status_code, f"Request GET was unsuccessful with status {response_status_code}")
         .is_equal_to(200))

        expected_data: list[dict[str, object]] = list(filter(
            lambda item: item if item["id"] == first_comment_query_dict["id"] else None,
            get_expected_response_data))

        (assert_that(response_data, f"Data from response is not equal to expected.")
         .is_equal_to(expected_data))

    def test_post_request(self):
        response: Response = requests.post(self.__post_url, post_new_comment_body, headers=self.__base_header)

        response_status_code: int = response.status_code
        response_data: json = response.json()

        (assert_that(response_status_code, f"Request GET was unsuccessful with status {response_status_code}")
         .is_equal_to(201))

        (assert_that(response_data, f"Data from response is not equal to expected.")
         .is_equal_to(post_new_comment_body))

    def test_put_request(self):
        id_of_desired_item: int = int(fifth_post_expected_data["id"])

        response: Response = requests.put(f"{self.__post_url}/{id_of_desired_item}", fifth_post_expected_data,
                                          headers=self.__base_header)

        response_status_code: int = response.status_code
        response_data: json = response.json()

        (assert_that(response_status_code, f"Request GET was unsuccessful with status {response_status_code}")
         .is_equal_to(200))

        (assert_that(response_data, f"Data from response is not equal to expected.")
         .is_equal_to(expected_fifth_post_expected_data))

    def test_delete_request(self):
        id_of_desired_item: int = int(post_new_comment_body["id"])
        response: Response = requests.delete(f"{self.__post_url}/{id_of_desired_item}", params=post_new_comment_body,
                                             headers=self.__base_header)

        response_status_code: int = response.status_code

        (assert_that(response_status_code, f"Request GET was unsuccessful with status {response_status_code}")
         .is_equal_to(200))
