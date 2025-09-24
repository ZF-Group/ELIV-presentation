from enum import Enum
import json
from typing import List, Optional, Union
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field

class MetaInformation(BaseModel):
    Authority: str = Field("ZF Friedrichshafen AG, DIRDP1", description="Department Responsible")
    SchemaAuthor: str = Field("Viswanatha Reddy, Batchu", description="Author of the file")
    SchemaReleaseDate: Annotated[str, StringConstraints(pattern=r'^\d{4}-\d{2}-\d{2}$')] = Field("28.05.2024", description="date of the last update in the format YYYY-MM-DD")
    SchemaVersion: Annotated[str, StringConstraints(pattern=r'^\d+\.\d+\.\d+$')] = Field("0.0.3", description="version information of the file")
    SchemaDescription: str = Field("Details of the standard function Interfaces - Working Revision", description="Author of the file")

class FunctionInformation(BaseModel):
    FunctionName: str = Field(..., description="Name of the function")
    FunctionResponsible: str = Field(..., description="Responsible function developer")
    Description: str = Field(..., description="description of the function")

class NumericalDatatypes(str, Enum):
    float = 'float'
    double = 'double'
    int8 = 'int8'
    int16 = 'int16'
    int32 = 'int32'
    int64 = 'int64'
    uint8 = 'uint8'
    uint16 = 'uint16'
    uint32 = 'uint32'
    uint64 = 'uint64'

class Numerical(BaseModel):
    Datatype: NumericalDatatypes
    MinValue: Optional[float] = Field(..., description="Minumum value of the numerical signal after scaling and offset")
    MaxValue: Optional[float] = Field(..., description="Maximum value of the numerical signal after scaling and offset")
    Offset: float = Field(..., description="Offset of the numerical signal after scaling")
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

class StructDatatype(BaseModel):
    Datatype: str = "struct"
    FieldsList: List[Union[Numerical, StringDatatype, BooleanDatatype]]

class Event(BaseModel):
    EventType: Annotated[str, StringConstraints(pattern=r'^(DataEvent|ErrorEvent|ModeSwitch|CyclicEvent)$')] = Field(..., description="Type of the event")
    EventValue: str = Field(..., description="SignalName/Error/Mode/CycleTime")

class SchedulingInfo(BaseModel):
    Runtype: Annotated[str, StringConstraints(pattern=r'^(Cyclic|EventBased)$')] = Field(..., description="Runtype of the function/runnable, can be Cyclic or EventBased")
    CycleTime: float = Field(..., description="Cycle time of the function runnable in ms. Set cycletime to 0 (or -1) if function/runnable is only eventbased.") 
    PrevFunction: Optional[str] = Field(..., description="Init/Cyclic/OtherRunnableName after this Runnable the above function or Runnable has to run")
    ExecOffset: Optional[float] = Field(..., description="Runnable First Execution Offset/Initial delay in ms")
    Scheduling: Optional[str] = Field(..., description="Preemptive/Non-Preemptive/RR/FIFO/EDF etc.")
    DebounceDelay: Optional[float] = Field(..., description="Successive execution delay of the runnable in ms")
    Priority: Optional[str] = Field(..., description="high priority than the runnable/function mentioned here")
    EventList: List[Event]

class Error(BaseModel):
    Name: str = Field(..., description="Name of the error/fault")
    Description: str = Field(..., description="Description of the error/fault")
    Dependancy: str = Field(..., description="Dependency Error(Base SW/Superset Error) with which above Error is set automatically")
    OccurenceCountLimit: int = Field(..., description="Number of times the error has to occur to confirm the Error is active")
    IgnitionCountLimit: int = Field(..., description="Number of Ignition cycles count, the error to be reported to the Central Error/Fault Manager for the Error/Fault to be Confirmed. 0 if not valid")
    MaturationTime: float = Field(..., description="The duration in milli seconds for which the Error/Fault is reported to be confirmed. 0 if not valid")
    Severity: str = Field(..., description="Description of severity like Safety reaction: Complete funtion disable or degradation, or warning indicator Red/Amber Lamp")

class SafetyReaction(BaseModel):
    Name: str = Field(..., description="Name of the safety reaction signal")
    Description: str = Field(..., description="Description of the safety reaction")
    Datatype: str = Field(..., description="datatype of the safety reaction signal")
    ErrorList: List[str] = Field(..., description="List of Errors (any Error)  which enables the safety reaction")

class AsilLevel(str, Enum):
    qm = 'qm'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

class WatchdogConfig(BaseModel): 
    Min: float
    Max: float
    ErrorName: str
    Description: str

class Watchdog(BaseModel):
    AsilLevel: AsilLevel
    AliveSupervision: Optional[WatchdogConfig] 
    DeadlineSupervision: Optional[WatchdogConfig]
    LogicalSupervision: Optional[str]

class InterfaceDatatype(BaseModel):
    Name: str = Field(..., description="Name of the signal")
    Role: Annotated[str, StringConstraints(pattern=r'^(Consumer|Provider)$')] = Field(..., description="Role of the signal, can be either Consumer or Provider")
    Type: str = Field(..., description="Function Contract type, for e. g. Global Variable Interfaces/ C function call Interfaces")
    Datatype: Union[Numerical, StringDatatype, BooleanDatatype, StructDatatype] = Field(..., description="datatype of the signal")
    Description: str = Field(..., description="Description of the signal")
    RangeErrorAction: Optional[Annotated[str, StringConstraints(pattern=r'^(Default|Init)$')]] = Field(..., description="In case of Value Range error of the signal which value to be considered")
    TimeoutValue: Optional[float] = Field(..., description="Signal timeout value in ms")
    TimeoutError: Optional[str] = Field(..., description="Name of the signal timeout error")
    AsilInfo: AsilLevel = Field(..., description="Asil Level of the signal")
    ArraySize: Optional[int] = Field(..., description="If the signal is given as an arry the array size shall be specified with this field")

class Message(BaseModel):
    Name: str = Field(..., description="Name of the message")
    Role: Annotated[str, StringConstraints(pattern=r'^(Consumer|Provider)$')] = Field(..., description="Role of the signal, can be either Consumer or Provider")
    Description: str = Field(..., description="Description of the signal")
    AsilInfo: AsilLevel = Field(..., description="Asil Level of the signal")
    QueueLength: int = Field(..., description="queue length of the messages Data/Array")
    Datatype: Union[Numerical, StringDatatype, BooleanDatatype, StructDatatype] = Field(..., description="datatype of the signal")
    ArraySize: Optional[int] = Field(..., description="If the message datatype is given as an arry the array size shall be specified with this field")


class MethodDatatype(BaseModel):
    Name: str = Field(..., description="Name of the variable")
    Datatype: Union[Numerical, StringDatatype, BooleanDatatype, StructDatatype]
    ArraySize: Optional[int] = Field(..., description="If the method datatype is given as an arry the array size shall be specified with this field")


class Method(BaseModel):
    Name: str = Field(..., description="Name of the method")
    Description: str = Field(..., description="Description of the method")
    Role: Annotated[str, StringConstraints(pattern=r'^(Consumer|Provider)$')] = Field(..., description="Role of the method, can be either Consumer or Provider")
    InDataTypeList: List[MethodDatatype] = Field(..., description="Input parameters of the method")
    OutDataTypeList: List[MethodDatatype] = Field(..., description="Output parameters of the method")

class Parameter(BaseModel):
    Name: str = Field(..., description="Name of the parameter")
    Description: str = Field(..., description="Description of the parameter")
    AsilInfo: AsilLevel = Field(..., description="Asil Level of the parameter")
    Datatype: Union[Numerical, StringDatatype, BooleanDatatype, StructDatatype] = Field(..., description="datatype of the parameter")
    RangeErrorAction: Optional[Annotated[str, StringConstraints(pattern=r'^(Default|Init)$')]] = Field(..., description="In case of Value Range error of the parameter which value to be considered")
    InterfaceType: Annotated[str, StringConstraints(pattern=r'^(PersistanceMemory|Calibration|Measurement)$')] = Field(..., description="?")
    Attribute: Annotated[str, StringConstraints(pattern=r'^(NA|Normal|LearningParameter)$')] = Field(..., description="?")

class AllocationInfo(BaseModel):
    StackSize: Optional[int] = Field(..., description="Stacksize allocation of the Runnable in bytes")
    ParallelProcessing: Optional[bool] = Field(..., description="True/False; Details of the runnables which can run in parallel")

class Function(BaseModel):
    Name: str = Field(..., description="Name of the function/runnable")
    Description: str = Field(..., description="description of the function/runnable")
    InterfaceData: List[InterfaceDatatype]
    SchedulingInfo: SchedulingInfo
    MessageList: Optional[List[Message]]
    MethodList: Optional[List[Method]]
    ParameterList: Optional[List[Parameter]]
    ErrorList: Optional[List[Error]]
    SafetyReactionList: Optional[List[SafetyReaction]]
    Watchdog: Optional[Watchdog]
    AllocationInfo: Optional[AllocationInfo]

class Component(BaseModel):
    Name: str = Field(..., description="Name of the component")
    FunctionList: List[Function]

class Mode(BaseModel):
    Name: str = Field(..., description="Name of the mode")
    Description: str = Field(..., description="Description of the mode")
    RunnablesList: List[str] = Field(..., description="List of runnable names")

class LETInterval(BaseModel):
    Length: float = Field(..., description="LET execution time in ms")
    JitterAllowed: float = Field(..., description="LET execution time Jitter allowed in ms, default is 0.0") 

class LETPeriod(BaseModel):
    Length: float = Field(..., description="LET cycle time in ms")
    JitterAllowed: float = Field(..., description="LET cycle time Jitter allowed in ms, default is 0.0")

class LETOffset(BaseModel):
    Length: float = Field(..., description="LET Offset time in ms")
    JitterAllowed: float = Field(..., description="LET Offset time Jitter allowed in ms, default is 0.0") 

class LETInfo(BaseModel):
    Name: str = Field(..., description="Name of the LET")
    FunctionList: List[str] = Field(..., description="List of runnables/Exectuable names in LET")
    Interval: LETInterval
    Period: LETPeriod
    Offset: LETOffset

class FunctionModel(BaseModel):
    MetaInformation: MetaInformation
    FunctionInformation: FunctionInformation
    ComponentList: List[Component]
    ModesList: Optional[List[Mode]]
    LETList: Optional[List[LETInfo]]


f = open("function_json_schema.json", "w+")
f.write(json.dumps(FunctionModel.model_json_schema(), indent=2))
f.close()