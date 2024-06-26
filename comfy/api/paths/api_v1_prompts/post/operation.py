# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from comfy.api import api_client, exceptions
from comfy.api.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from comfy.api.components.schema import prompt
from comfy.api.paths.api_v1_prompts.post.request_body.content.multipart_formdata import schema

from .. import path
from .responses import (
    response_200,
    response_204,
    response_400,
    response_429,
    response_500,
    response_503,
    response_507,
)
from . import request_body


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
        '204': typing.Type[response_204.ResponseFor204],
        '400': typing.Type[response_400.ResponseFor400],
        '429': typing.Type[response_429.ResponseFor429],
        '500': typing.Type[response_500.ResponseFor500],
        '503': typing.Type[response_503.ResponseFor503],
        '507': typing.Type[response_507.ResponseFor507],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
    '204': response_204.ResponseFor204,
    '400': response_400.ResponseFor400,
    '429': response_429.ResponseFor429,
    '500': response_500.ResponseFor500,
    '503': response_503.ResponseFor503,
    '507': response_507.ResponseFor507,
}
_non_error_status_codes = frozenset({
    '200',
    '204',
})
_error_status_codes = frozenset({
    '400',
    '429',
    '500',
    '507',
    '503',
})

_all_accept_content_types = (
    "application/json",
)


class BaseApi(api_client.Api):
    @typing.overload
    def _api_v1_prompts_post(
        self,
        body: typing.Union[
            prompt.PromptDictInput,
            prompt.PromptDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: typing.Literal[False] = False,
        content_type: typing.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> typing.Union[
        response_200.ApiResponse,
        response_204.ApiResponse,
    ]: ...

    @typing.overload
    def _api_v1_prompts_post(
        self,
        body: typing.Union[
            prompt.PromptDictInput,
            prompt.PromptDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: typing.Literal[True],
        content_type: typing.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _api_v1_prompts_post(
        self,
        body: typing.Union[
            schema.SchemaDictInput,
            schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: typing.Literal[False] = False,
        content_type: typing.Literal["multipart/formdata"],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> typing.Union[
        response_200.ApiResponse,
        response_204.ApiResponse,
    ]: ...

    @typing.overload
    def _api_v1_prompts_post(
        self,
        body: typing.Union[
            schema.SchemaDictInput,
            schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: typing.Literal[True],
        content_type: typing.Literal["multipart/formdata"],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _api_v1_prompts_post(
        self,
        body: typing.Union[
            typing.Union[
                prompt.PromptDictInput,
                prompt.PromptDict,
            ],
            typing.Union[
                schema.SchemaDictInput,
                schema.SchemaDict,
            ],
            schemas.Unset,
        ] = schemas.unset,
        *,
        skip_deserialization: bool = False,
        content_type: typing.Literal[
            "application/json",
            "multipart/formdata",
        ] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        (API) Generate image
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        headers = self._get_headers(accept_content_types=accept_content_types)
        # TODO add cookie handling

        fields, serialized_body = self._get_fields_and_body(
            request_body=request_body.RequestBody,
            body=body,
            content_type=content_type,
            headers=headers
        )
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='post',
            host=host,
            headers=headers,
            fields=fields,
            body=serialized_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            skip_deser_response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
            self._verify_response_status(skip_deser_response)
            return skip_deser_response

        status = str(raw_response.status)
        if status in _non_error_status_codes:
            status_code = typing.cast(
                typing.Literal[
                    '200',
                    '204',
                ],
                status
            )
            return _status_code_to_response[status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
        elif status in _error_status_codes:
            error_status_code = typing.cast(
                typing.Literal[
                    '400',
                    '429',
                    '500',
                    '507',
                    '503',
                ],
                status
            )
            error_response = _status_code_to_response[error_status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
            raise exceptions.ApiException(
                status=error_response.response.status,
                reason=error_response.response.reason,
                api_response=error_response
            )

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class ApiV1PromptsPost(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    api_v1_prompts_post = BaseApi._api_v1_prompts_post


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    post = BaseApi._api_v1_prompts_post
