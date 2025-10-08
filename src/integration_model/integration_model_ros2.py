import function_model as fm
import sys
import json
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field


current_dir = Path(__file__).resolve().parent
function_json_path = str(current_dir.parent.joinpath("function_model"))
sys.path.append(function_json_path)
print(function_json_path)


# Necessary to generate the necessary conversion API's for converting data from the ROS-Topic to the function interface
class ConversionAPI(BaseModel):
    Name: str
    ReturnDataType: str


class DataMap(BaseModel):
    # Can be a non VSS standardized interface
    GlobalVariableName: List[str]
    # Implement a datatype validation between (GlobalVariableDataType vs ROSTopicFieldDataType) before the integration JSON is written
    # In case of a mismatch a conversion API need to be defined
    GlobalVariableDataType: List[str]
    # Apply here the VSS Signal names
    ROSTopicFieldName: List[str]
    ROSTopicFieldDataType: List[str]
    ConversionAPI: Optional[List[ConversionAPI]]


# Each interface definition in the function model shall have a data mapping defined, to describe how the data can be retrieved from the ROS2 topics
class ROSTopic(BaseModel):
    TopicName: str = Field(..., description="Name of the ROS2 topic")
    InterfaceName: str = Field(
        ..., description="Name of the interface from the runnable"
    )
    # Obsolete as already defined in the InterfaceDataType of the function
    # Role: Annotated[str, StringConstraints(pattern=r'^(Consumer|Provider)$')] = Field(..., description="Role of the topic, can be either Consumer or Provider")
    DataMappingList: List[DataMap] = Field(
        ..., description="Mapping of global variables to ROS2 topic fields"
    )


class Communication(BaseModel):
    RunnableName: str = Field(
        ..., description="Name of the runnable to map the communication to"
    )
    ROSTopicList: List[ROSTopic] = Field(
        ..., description="Relevant ROS Topics for the function"
    )


class IntegrationModel(fm.FDKFunctionModel):
    CommunicationList: List[Communication]


f = open("integration_schema_ros2.json", "w+")
f.write(json.dumps(IntegrationModel.model_json_schema(), indent=2))
f.close()
