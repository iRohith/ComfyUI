# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from comfy.api.shared_imports.header_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.multipart_form_data import schema as multipart_form_data_schema


class RequestBody(api_client.RequestBody):


    class MultipartFormDataMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = multipart_form_data_schema.Schema
    content = {
        'multipart/form-data': MultipartFormDataMediaType,
    }
