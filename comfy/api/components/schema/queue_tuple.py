# coding: utf-8

"""
    comfyui
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations

from comfy.api.components.schema import prompt, extra_data
from comfy.api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class QueueTupleTuple(
    typing.Tuple[
        typing.Union[int, float],
        str,
        prompt.PromptDict,
        extra_data.ExtraDataDict,
        "_4Tuple",
        typing_extensions.Unpack[typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]]
    ]
):

    def __new__(cls, arg: typing.Union[QueueTupleTupleInput, QueueTupleTuple], configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return QueueTuple.validate(arg, configuration=configuration)
QueueTupleTupleInput = typing.Union[
    typing.List[
        typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
    ],
    typing.Tuple[
        typing.Union[
            int,
            float
        ],
        str,
        typing.Union[
            prompt.PromptDictInput,
            prompt.PromptDict,
        ],
        typing.Union[
            extra_data.ExtraDataDictInput,
            extra_data.ExtraDataDict,
        ],
        typing.Union[
            "_4TupleInput",
            "_4Tuple"
        ],
        typing_extensions.Unpack[typing.Tuple[schemas.INPUT_TYPES_ALL, ...]]
    ]
]
_0: typing_extensions.TypeAlias = schemas.NumberSchema
_1: typing_extensions.TypeAlias = schemas.StrSchema
Items: typing_extensions.TypeAlias = schemas.StrSchema


class _4Tuple(
    typing.Tuple[
        str,
        ...
    ]
):

    def __new__(cls, arg: typing.Union[_4TupleInput, _4Tuple], configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return _4.validate(arg, configuration=configuration)
_4TupleInput = typing.Union[
    typing.List[
        str,
    ],
    typing.Tuple[
        str,
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class _4(
    schemas.Schema[schemas.immutabledict, _4Tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: _4Tuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            _4TupleInput,
            _4Tuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _4Tuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


@dataclasses.dataclass(frozen=True)
class QueueTuple(
    schemas.Schema[schemas.immutabledict, QueueTupleTuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    The first item is the queue priority
The second item is the hash id of the prompt object
The third item is a Prompt
The fourth item is optionally an ExtraData
The fifth item is optionally a list of "Good Outputs" node IDs.

    """
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    max_items: int = 5
    min_items: int = 3
    prefix_items: typing.Tuple[
        typing.Type[_0],
        typing.Type[_1],
        typing.Type[prompt.Prompt],
        typing.Type[extra_data.ExtraData],
        typing.Type[_4],
    ] = (
        _0,
        _1,
        prompt.Prompt,
        extra_data.ExtraData,
        _4,
    )
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: QueueTupleTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            QueueTupleTupleInput,
            QueueTupleTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueueTupleTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )