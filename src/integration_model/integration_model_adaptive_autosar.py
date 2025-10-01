from enum import Enum
import json
from typing import List, Optional, Union
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field


class MetaInformation(BaseModel):
    Authority: str = Field(..., description="Department Responsible")
    Author: str = Field(..., description="Author of the file")
    Date: Annotated[str, StringConstraints(pattern=r"^\d{4}-\d{2}-\d{2}$")] = Field(
        ..., description="date of the last update"
    )
    Version: Annotated[str, StringConstraints(pattern=r"^\d+\.\d+\.\d+$")] = Field(
        ..., description="version information of the file"
    )


class FunctionInformation(BaseModel):
    FunctionName: str = Field(..., description="Name of the function")
    Responsible: str = Field(..., description="Responsible function developer")
    Description: str = Field(..., description="description of the function")


class NumericalDatatypes(str, Enum):
    float = "float"
    double = "double"
    int32 = "int32"
    int64 = "int64"
    uint32 = "uint32"
    uint64 = "uint64"
    float32 = "float32"
    bool = "bool"
    int8_t = "int8_t"
    uint8_t = "uint8_t"
    int16_t = "int16_t"
    uint16_t = "uint16_t"


class Numerical(BaseModel):
    Datatype: NumericalDatatypes
    MinValue: float = Field(
        ...,
        description="Minumum value of the numerical signal after scaling and offset",
    )
    MaxValue: float = Field(
        ...,
        description="Maximum value of the numerical signal after scaling and offset",
    )
    Offset: float = Field(
        ..., description="Offset of the numerical signal after scaling"
    )
    Scaling: float = Field(..., description="Scaling factor of the numerical signal")
    Unit: Optional[str] = Field(..., description="Unit of the signal")
    Default: float = Field(..., description="Default value of the signal")
    InitValue: float = Field(..., description="Init value of the signal")


class StringDatatype(BaseModel):
    DataType: str = "string"
    Default: str = Field(..., description="Default value of the signal")
    InitValue: str = Field(..., description="Init value of the signal")


class BooleanDatatype(BaseModel):
    Datatype: str = "boolean"
    Default: bool = Field(..., description="Default value of the signal")
    InitValue: bool = Field(..., description="Init value of the signal")


class StructFields(BaseModel):
    Name: str = Field(..., description="Name of the structure's field")
    Type: Union[NumericalDatatypes, "StructFields", str]


class StructDatatype(BaseModel):
    Name: str = Field(..., description="Name of the structure")
    Class: str = "structure"
    Field: List[StructFields]
    TypeRef: str


class TypeReference(BaseModel):
    Name: str = Field(..., description="Name of the type reference")
    Class: str = "type_reference"
    cDef: NumericalDatatypes


class ArrayDimensionDatatype(BaseModel):
    Name: str = Field(..., description="Name of the array dimension")
    Class: str = "array_dimension"
    Dimension: int


class ArrayDatatype(BaseModel):
    Name: str = Field(..., description="Name of the array")
    Class: str = "array"
    Type: NumericalDatatypes
    Dimension: Union[int, str]
    TypeRef: str


class EnumList(BaseModel):
    Symbol: str
    Value: int


class EnumerationDatatype(BaseModel):
    Name: str = Field(..., description="Name of the enumeration")
    Class: str = "enumeration"
    EnumField: List[EnumList]


class MethodDatatype(BaseModel):
    Name: str = Field(..., description="Name of the variable")
    Datatype: Union[Numerical, StringDatatype, BooleanDatatype, StructDatatype]


class Method(BaseModel):
    Name: str = Field(..., description="Name of the method")


class Mode(BaseModel):
    Name: str = Field(..., description="Name of the mode")


class Parameter(BaseModel):
    Name: str = Field(..., description="Name of the parameter")
    Description: str = Field(..., description="Description of the parameter")
    Datatype: Union[Numerical, StringDatatype, BooleanDatatype, StructDatatype] = Field(
        ..., description="datatype of the parameter"
    )
    RangeErrorAction: Optional[
        Annotated[str, StringConstraints(pattern=r"^(Default|Init)$")]
    ] = Field(
        ...,
        description="In case of Value Range error of the parameter which value to be considered",
    )
    InterfaceType: Annotated[
        str, StringConstraints(pattern=r"^(PersistanceMemory|Calibration|Measurement)$")
    ] = Field(
        ...,
        description="Description of the type of parameter (persistent, calibration or measurement)",
    )
    Attribute: Annotated[
        str, StringConstraints(pattern=r"^(NA|Normal|LearningParameter)$")
    ] = Field(
        ..., description="Description on the parameter attribute (constant or learning)"
    )


class Function(BaseModel):
    Name: str = Field(..., description="Name of the function/runnable")
    Modes: List[str]
    RunType: Annotated[str, StringConstraints(pattern=r"^(Init|Cyclic|Terminate)$")] = (
        Field(..., description="Type of execution of the function")
    )
    CycleTime: Optional[float] = Field(
        ..., description="Run time of the function in milliseconds", nullable=True
    )
    Scheduling: Optional[
        Annotated[
            str, StringConstraints(pattern=r"^(Preemptive|Non-preemptive|RR|FIFO)$")
        ]
    ] = Field(..., description="Type of scheduling", nullable=True)


class Event(BaseModel):
    Name: str = Field(..., description="Name of the event")
    DataType: Union[NumericalDatatypes, str] = Field(
        ..., description="datatype of the event"
    )
    DataMappingList: Optional[List[str]] = Field(
        ..., description="Name of the variable being mapped"
    )


class Fields(BaseModel):
    Name: str = Field(..., description="Name of the field")


class Provider(BaseModel):
    Name: str = Field(..., description="Name of the provider for the service")
    ServiceDeploymentType: str = Field(
        ..., description="Type of the deployment for the service"
    )
    ServiceInstanceID: Optional[float] = Field(
        ..., description="Instance ID of the service", nullable=True
    )
    ContractName: str = Field(..., description="Name of the MW framework")


class Services(BaseModel):
    Events: List[Event]
    Methods: List[Method]
    Fields: List[Fields]


class ServiceInterface(BaseModel):
    Name: str = Field(..., description="Name of the service interface")
    Role: Annotated[str, StringConstraints(pattern=r"^(Consumer|Provider)$")] = Field(
        ...,
        description="Role of the service interface, can be either Consumer or Provider",
    )
    ServiceList: List[Services] = Field(..., description="List of services")
    Provider: Optional[List[Provider]]


class Component(BaseModel):
    Name: str = Field(..., description="Name of the component")
    ExecutableName: str = Field(..., description="Name of the executable")
    HeaderFiles: Optional[List[str]]
    FunctionGroupModes: List[str]
    FunctionList: List[Function]
    ParameterList: Optional[List[Parameter]]
    ServiceInterfaceList: List[ServiceInterface]


class FunctionModel(BaseModel):
    MetaInformation: MetaInformation
    FunctionInformation: FunctionInformation
    ComponentList: List[Component]
    DataTypes: Optional[
        List[Union[TypeReference, StructDatatype, ArrayDatatype, EnumerationDatatype]]
    ] = Field(..., description="datatype of the interfaces")


f = open("integration_schema_adaptive_autosar.json", "w+")
f.write(json.dumps(FunctionModel.model_json_schema(), indent=2))
f.close()
