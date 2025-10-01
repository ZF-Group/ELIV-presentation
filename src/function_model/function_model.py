import json
from pydantic import BaseModel, Field, StringConstraints
from typing_extensions import Annotated
from typing import List, Optional


class Datatype(BaseModel):
    typeRef: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="Reference identifier for the datatype, e.g., DT_UInt16"
    )
    category: str = Field(
        ...,
        description="Classification of the datatype, typically primitive or userdefined",
    )
    cDef: str = Field(..., description="C language definition of the datatype")


class Signal(BaseModel):
    Name: str = Field(..., description="Name of the signal")
    Description: str = Field(..., description="Description of the signal's purpose")
    Role: str = Field(..., description="Role of the signal, e.g., Consumer or Provider")
    AsilLevel: Optional[str] = Field(
        None, description="Automotive Safety Integrity Level information of the signal"
    )
    Timeout: Optional[str] = Field(
        None, description="Timeout value of signal if applicable"
    )
    Access: Optional[str] = Field(None, description="Immediate or buffered access ")
    Datatype: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="Datatype reference used by the signal"
    )
    Factor: Optional[str] = Field(None, description="Scaling factor")
    Offset: Optional[str] = Field(None, description="Offset value")
    Min: Optional[float] = Field(None, description="Minimum valid value")
    Max: Optional[float] = Field(None, description="Maximum valid value")
    Default: Optional[float] = Field(None, description="Default value")
    InitValue: Optional[float] = Field(None, description="Initial value")
    Units: Optional[str] = Field(None, description="Measurement units")
    RangeErrorAction: Optional[str] = Field(
        None, description="Action to take on value range error"
    )


class DataQ(BaseModel):
    Name: str = Field(..., description="Name of the Queued Data Interface")
    Description: str = Field(
        ..., description="Description of the Queued Data Interface"
    )
    Role: str = Field(
        ..., description="Role of the Queued Data Interface(Consumer/Provider)"
    )
    AsilInfo: str = Field(..., description="ASIL information")
    QueueLength: int = Field(..., description="Length of the Queued Data Interface")
    Datatype: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="Datatype reference used by the signal"
    )
    Factor: float = Field(..., description="Scaling factor for the data")
    Offset: float = Field(..., description="Offset value for the data")
    InitValue: float = Field(..., description="Initial value of the data")
    Units: str = Field(..., description="Units of measurement")


class ArgTypeItem(BaseModel):
    Name: str = Field(..., description="Name of the argument or return value")
    Datatype: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="Data type of the argument"
    )
    Units: str = Field(..., description="Units of the argument")


class Method(BaseModel):
    Name: str = Field(..., description="Name of the method or service")
    Description: str = Field(..., description="Description of the method/service")
    Role: str = Field(..., description="Role of the method (Consumer/Provider)")
    InDataTypeList: List[ArgTypeItem] = Field(
        ..., description="List of input arguments"
    )
    OutDataTypeList: List[ArgTypeItem] = Field(
        ..., description="List of output return values"
    )


class Parameter(BaseModel):
    Name: str = Field(..., description="Name of the parameter port")
    Description: str = Field(..., description="Description of the parameter")
    Datatype: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="Datatype reference of the parameter"
    )
    Asillevel: str = Field(..., description="ASIL information ")
    Min: float = Field(..., description="Minimum allowed value")
    Max: float = Field(..., description="Maximum allowed value")
    Default: float = Field(..., description="Default value")
    InitValue: float = Field(..., description="Initial value")
    RangeErrorAction: str = Field(
        ..., description="Action on range error (Default/InitValue)"
    )
    Interfacetype: str = Field(
        ..., description="Type of interface (e.g., PersistenceMemory)"
    )
    Attribute: str = Field(..., description="Attribute type (e.g., Normal, Learning)")
    Units: str = Field(..., description="Units of measurement")


class Error(BaseModel):
    Name: str = Field(..., description="Name of the error or fault")
    Description: str = Field(..., description="Description of the error/fault")
    Datatype: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="Datatype reference of the Error"
    )
    Dependancy: List[str] = Field(
        ...,
        description="Dependency Error(Base SW/Superset Error) with which this Error is set automatically",
    )
    OccurenceCountLimit: int = Field(
        ...,
        description="Number of times the error has to occur to confirm the Error is active",
    )
    IgnitionCountLimit: int = Field(
        ...,
        description="Number of Ignition cycles count, the error to be reported to the Central Error/Fault Manager for the Error/Fault to be Confirmed. 0 if not valid",
    )
    MaturationTime: int = Field(
        ...,
        description="The duration in milli seconds for which the Error/Fault is reported to be confirmed. 0 if not valid",
    )
    Severity: str = Field(
        ...,
        description="Description of severity like Safety reaction: Complete funtion disable or degradation, or warning indicator Red/Amber Lamp",
    )


class SafetyReaction(BaseModel):
    Name: str = Field(..., description="Name of the safety reaction signal")
    Description: str = Field(..., description="Description of the safety reaction")
    Datatype: Annotated[str, StringConstraints(pattern=r"^DT_[A-Za-z0-9]+$")] = Field(
        ..., description="datatype of the safety reaction signal"
    )
    ErrorList: List[str] = Field(
        ..., description="List of Errors (any Error)  which enables the safety reaction"
    )


class WatchdogConfig(BaseModel):
    Min: float = Field(..., description="Number of minimum cycles or minimum time")
    Max: float = Field(..., description="Number of maximum cycles or maximum time")
    Ref: float = Field(
        ..., description="reference value for e.g. How much time/cycles to be observed"
    )
    ErrorName: str = Field(..., description="ErrorName with description")


class WatchdogItem(BaseModel):
    AliveSupervision: Optional[WatchdogConfig]
    DeadlineSupervision: Optional[WatchdogConfig]
    LogicalSupervision: Optional[str]


class Mode(BaseModel):
    Name: str = Field(..., description="Name of the mode")
    Description: str = Field(..., description="Description of the mode")
    RunnablesList: List[str] = Field(
        ...,
        description="List of runnables/Executables names to be executed in this mode ",
    )


class funcContract(BaseModel):
    Type: Optional[str] = Field(
        None, description="Type of contract, e.g., Global or C function calls"
    )
    SignalList: Optional[List[Signal]] = Field(
        ..., description="List of signal interfaces"
    )
    DataQList: Optional[List[DataQ]] = Field(
        ..., description="List of Queued Data interfaces"
    )
    MethodList: Optional[List[Method]] = Field(..., description="List of Methods")
    ParameterList: Optional[List[Parameter]] = Field(
        ..., description="List of Parameters"
    )
    ErrorList: Optional[List[Error]] = Field(..., description="List of Errors")
    SafetyReactionList: Optional[List[SafetyReaction]] = Field(
        ..., description="List of SafetyReactions"
    )


class function(BaseModel):
    Name: str = Field(..., description="Name of the function")
    Description: str = Field(..., description="Description of the function")
    Runtype: str = Field(
        ..., description="Runtime type, e.g., Init, Cyclic,event based or Shutdown"
    )
    Cycletime: Optional[int] = Field(None, description="Cycle time in milliseconds")
    StackSize: Optional[str] = Field(None, description="Stack size allocation")
    PrevRunnable: Optional[str] = Field(
        None, description="Previous runnable of the component"
    )
    ExecOffset: Optional[str] = Field(None, description="Execution offset")
    ParallelProcessing: Optional[bool] = Field(
        None, description="Indicates if parallel processing is enabled"
    )
    AsilLevel: Optional[str] = Field(None, description="ASIL level of the function")
    Watchdog: Optional[WatchdogItem] = Field(
        ...,
        description="Watchdog Configuration for the runnable/Executable. Min, Max and Ref for AliveSupervision in Cycles count, Deadline Supervision in ms time",
    )
    Scheduling: str = Field(
        ..., description="Scheduling type, e.g., Pre-emptive or Non-Preemptive"
    )
    DebounceDelay: Optional[str] = Field(
        None, description="Delay after which the function should run"
    )
    Priority: str = Field(..., description="Priority description")
    EventList: Optional[str] = Field(
        None,
        description="Associated events list with which the function is trigegred, only for future scope",
    )
    funcContractList: Optional[List[funcContract]] = Field(
        None, description="List of function contracts"
    )


class Component(BaseModel):
    Name: str = Field(..., description="Name of the component")
    functionList: List[function] = Field(
        ..., description="List of functions within the component"
    )


class FunctionDetails(BaseModel):
    FunctionName: str = Field(..., description="Name of the main function")
    FunctionResponsible: str = Field(..., description="Responsible person or team")
    Description: str = Field(..., description="General description of the function")


class MetaInfoItem(BaseModel):
    Authority: str = Field(
        "ZF Friedrichshafen AG, DIRDS2", description="Authoritative organization"
    )
    SchemaAuthor: str = Field(
        "Viswanatha Reddy, Batchu", description="Author of the schema"
    )
    Date: Annotated[str, StringConstraints(pattern=r"^\d{2}.\d{2}.\d{4}$")] = Field(
        "12.09.2025", description="Date in DD.MM.YYYY format"
    )
    SchemaVersion: Annotated[str, StringConstraints(pattern=r"^\d+\.\d+\.\d+$")] = (
        Field("1.0.0", description="Version of the schema")
    )
    SchemaDescription: str = Field(
        "Details of the standard function Interfaces - Working Revision",
        description="Description of the schema",
    )


class FDKFunctionModel(BaseModel):
    MetaInfo: MetaInfoItem = Field(..., description="Metadata information")
    FunctionInfo: FunctionDetails = Field(
        ..., description="Software Function Name and description"
    )
    ComponentList: List[Component] = Field(
        ..., description="List of components in a function"
    )
    ModesList: Optional[List[Mode]] = Field(
        ...,
        description="Different Modes of the Function and their active runnables/Executables",
    )
    Datatypes: List[Datatype] = Field(
        ..., description="List of Primitive and Userdefined datatypes"
    )


f = open("function_json_schema.json", "w+")
f.write(json.dumps(FDKFunctionModel.model_json_schema(), indent=2))
f.close()
