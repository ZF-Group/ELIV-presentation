# Function model for Example/Dummy application
from pathlib import Path
import sys
import json

sys.path.append(str(Path.cwd().parent.joinpath("FunctionModel")))
import function_model as fm


MetaInfo = fm.MetaInfoItem(
    Authority="ZF Friedrichshafen AG, DIRDS2",
    SchemaAuthor="Viswanatha Reddy, Batchu",
    Date="12.09.2025",
    Version="1.0.0",
    SchemaDescription="Details of the standard function Interfaces - Working Revision",
)

FunctionInfo = fm.FunctionDetails(
    FunctionName="CoreAcc",
    FunctionResponsible="ParthaSarathy Natarajan",
    Description="Core Adaptive Cruise Control application",
)

SignalList = [
    fm.Signal(
        Name="BrkCylP",
        Description="Chassis Brake Cylinder Pressure",
        Role="Consumer",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_SInt64",
        Factor=None,
        Offset=None,
        Min=-30,
        Max=276.9,
        Default=None,
        InitValue=0,
        Units=None,
        RangeErrorAction=None,
    ),
    fm.Signal(
        Name="SteerWhlAg",
        Description="Steering Wheel angle",
        Role="Consumer",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_SInt64",
        Factor=None,
        Offset=None,
        Min=-16,
        Max=16.766,
        Default=None,
        InitValue=-16,
        Units="rad",
        RangeErrorAction=None,
    ),
    fm.Signal(
        Name="EnaGACC",
        Description="Is ADAS EcoControl Enabled",
        Role="Consumer",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_Bool",
        Factor=None,
        Offset=None,
        Min=0,
        Max=1,
        Default=0,
        InitValue=0,
        Units=None,
        RangeErrorAction=None,
    ),
    fm.Signal(
        Name="VehM",
        Description="Vehicle Mass",
        Role="Consumer",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_SInt64",
        Factor=None,
        Offset=None,
        Min=None,
        Max=None,
        Default=None,
        InitValue=2495,
        Units=None,
        RangeErrorAction=None,
    ),
    fm.Signal(
        Name="SpdLimUnit",
        Description="ADAS Map DFS Map Data Speed UnitType",
        Role="Consumer",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_UInt8",
        Factor=None,
        Offset=None,
        Min=0,
        Max=3,
        Default=None,
        InitValue=0,
        Units="enum",
        RangeErrorAction=None,
    ),
    fm.Signal(
        Name="HstVehALgtFild",
        Description="EgoVehicleLongitudinalAcceleration",
        Role="Consumer",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_SInt64",
        Factor=None,
        Offset=None,
        Min=-20,
        Max=20.94,
        Default=None,
        InitValue=-20,
        Units="m/s^2",
        RangeErrorAction=None,
    ),
    fm.Signal(
        Name="AsmAcc_AccIntSts",
        Description="eco control status",
        Role="Provider",
        AsilLevel="qm",
        Timeout=None,
        Access=None,
        Datatype="DT_UInt8",
        Factor=None,
        Offset=None,
        Min=0,
        Max=15,
        Default=0,
        InitValue=None,
        Units=None,
        RangeErrorAction=None,
    ),
]

funcContractListCoreAcc_Step = [
    fm.funcContract(
        Type="Global Variable Interfaces",
        SignalList=SignalList,
        DataQList=None,
        MethodList=None,
        ParameterList=None,
        ErrorList=None,
        SafetyReactionList=None,
    )
]

functionListCoreAcc = [
    fm.function(
        Name="CoreAcc_Init",
        Description="Core ACC initialisation function",
        Runtype="Init",
        Cycletime=None,
        StackSize=None,
        PrevRunnable=None,
        ExecOffset=None,
        ParallelProcessing="False",
        AsilLevel=None,
        Watchdog=None,
        Scheduling="Non-Preemptive",
        DebounceDelay=None,
        Priority="higher than CoreAcc_Step function",
        EventList=None,
        funcContractList=None,
    ),
    fm.function(
        Name="CoreAcc_Step",
        Description="Core ACC Step function/Main Runnable",
        Runtype="Cyclic",
        Cycletime=50,
        StackSize=None,
        PrevRunnable="CoreAcc_Init",
        ExecOffset=None,
        ParallelProcessing=None,
        AsilLevel=None,
        Watchdog=None,
        Scheduling="Non-Preemptive",
        DebounceDelay=None,
        Priority="higher than Gacc  Component",
        EventList=None,
        funcContractList=funcContractListCoreAcc_Step,
    ),
    fm.function(
        Name="CoreAcc_Terminate",
        Description="Core ACC terminate function during shutdown",
        Runtype="Shutdown",
        Cycletime=None,
        StackSize=None,
        PrevRunnable=None,
        ExecOffset=None,
        ParallelProcessing=None,
        AsilLevel=None,
        Watchdog=None,
        Scheduling="Non-Preemptive",
        DebounceDelay=None,
        Priority="higher than CoreAcc_Step, and CoreACC_Init function",
        EventList=None,
        FuncContractList=None,
    ),
]

ComponentList = [
    fm.Component(
        Name="CoreAcc",
        functionList=functionListCoreAcc,
    )
]

DatatypesList = [
    fm.Datatype(
        typeRef="DT_UInt16",
        category="primitive",
        cDef="unsigned short int",
    ),
    fm.Datatype(
        typeRef="DT_UInt8",
        category="primitive",
        cDef="unsigned char",
    ),
    fm.Datatype(
        typeRef="DT_SInt64",
        category="primitive",
        cDef="double",
    ),
    fm.Datatype(
        typeRef="DT_UInt64",
        category="primitive",
        cDef="Unsigned double",
    ),
    fm.Datatype(typeRef="DT_Bool", category="primitive", cDef="unsigned char"),
]

FDKFunctionModel = fm.FDKFunctionModel(
    MetaInfo=MetaInfo,
    FunctionInfo=FunctionInfo,
    ComponentList=ComponentList,
    ModesList=None,
    Datatypes=DatatypesList,
)

f = open("function_model_core_acc.json", "w+")
f.write(json.dumps(FDKFunctionModel.model_dump(), indent=3))
f.close()
