# Integration model for ROS2 software platform for CoreACC application
import function_model as fm
import integration_model_ros2 as im

from pathlib import Path
import sys
import json

# Use the current file's directory to resolve the Function Json path
current_dir = Path(__file__).resolve().parent
function_json_path = str(current_dir.parent.joinpath("function_model"))
sys.path.append(function_json_path)

MetaInformation = fm.MetaInfoItem(
    Authority="ZF Friedrichshafen AG, DIRDS2",
    Author="Philipp Pelcz",
    Date="29.08.2025",
    Version="1.0.0",
)

FunctionInformation = fm.FunctionDetails(
    FunctionName="Core Acc Application",
    FunctionResponsible="Philipp Pelcz",
    Description="Core Acc application to integrate with Green Acc to form EcoControl",
)

SignalList = [
    fm.Signal(
        Name="BrkCylP",
        Description="Chasis Brake Cylinder Pressure",
        Role="Consumer",
        Datatype="DT_SInt64",
    ),
    fm.Signal(
        Name="SteerWhlAg",
        Description="Steering Wheel angle",
        Role="Consumer",
        Datatype="DT_SInt64",
    ),
    fm.Signal(
        Name="EnaGACC",
        Description="Is ADAS EcoControl Enabled",
        Role="Consumer",
        Datatype="DT_Bool",
    ),
    fm.Signal(
        Name="VehM",
        Description="Vehicle Mass",
        Role="Consumer",
        Datatype="DT_SInt64",
    ),
    fm.Signal(
        Name="SpdLimUnit",
        Description="ADAS Map DFS Map Data Speed UnitType",
        Role="Consumer",
        Datatype="DT_UInt8",
    ),
    fm.Signal(
        Name="HstVehALgtFild",
        Description="EgoVehicleLongitudinalAcceleration",
        Role="Consumer",
        Datatype="DT_SInt64",
    ),
    fm.Signal(
        Name="AsmAcc_AccIntSts",
        Description="eco control status",
        Role="Provider",
        Datatype="DT_UInt8",
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
        Scheduling="Non-Preemptive",
        Priority="higher than CoreAcc_Step function",
        Watchdog=None,
    ),
    fm.function(
        Name="CoreAcc_Step",
        Description="Core ACC Step function/Main Runnable",
        Runtype="Cyclic",
        Cycletime=50,
        PrevRunnable="CoreAcc_Init",
        Scheduling="Non-Preemptive",
        Priority="higher than Gacc  Component",
        funcContractList=funcContractListCoreAcc_Step,
        Watchdog=None,
    ),
    fm.function(
        Name="CoreAcc_Terminate",
        Description="Core ACC terminate function during shutdown",
        Runtype="Shutdown",
        Watchdog=None,
        Scheduling="Non-Preemptive",
        Priority="higher than CoreAcc_Step, and CoreACC_Init function",
    ),
]

DataMappingListInput = [
    im.DataMap(
        GlobalVariableName=[
            "core_inputs.bus_ACCIn.Bus_Veh.EgoVehALgt",
            "core_inputs.bus_ACCIn.Bus_Veh.SteerWhlAg",
            "core_inputs.bus_ACCIn.Bus_Veh.BrkCylP",
            "core_inputs.bus_ACCIn.Bus_Cust.EgoVehDshbSpdUnit",
            "core_inputs.bus_ACCIn.Bus_Cust.EgoVehMass",
        ],
        GlobalVariableDataType=["float", "float", "float", "uint8", "float"],
        ROSTopicFieldName=[
            "EgoVehALgt",
            "SteerWhlAg",
            "BrkCylP",
            "EgoVehDshbSpdUnit",
            "EgoVehMass",
        ],
        ROSTopicFieldDataType=["float", "float", "float", "uint8", "float"],
        ConversionAPI=None,
    )
]

DataMappingListOutputACC = [
    im.DataMap(
        GlobalVariableName=["AsmAcc_AccIntSts"],
        GlobalVariableDataType=["uint8"],
        ROSTopicFieldName=["ACCInt_Sts"],
        ROSTopicFieldDataType=["uint8"],
        ConversionAPI=None,
    )
]

DataMappingListOutputMeasurement = [
    im.DataMap(
        GlobalVariableName=["core_outputs.bus_Measurement_PRE.PRE_GaccEnbFlg"],
        GlobalVariableDataType=["boolean"],
        ROSTopicFieldName=["GaccEnbFlg"],
        ROSTopicFieldDataType=["boolean"],
        ConversionAPI=None,
    )
]

ROSTopicList = [
    im.ROSTopic(
        TopicName="bus_ACCIn",
        InterfaceName="bus_ACCIn",
        DataMappingList=DataMappingListInput,
    ),
    im.ROSTopic(
        TopicName="bus_ACCOut",
        InterfaceName="bus_ACC.bus_Asm",
        DataMappingList=DataMappingListOutputACC,
    ),
    im.ROSTopic(
        TopicName="bus_Measurement_PRE",
        InterfaceName="bus_Measurement_PRE",
        DataMappingList=DataMappingListOutputMeasurement,
    ),
]

CommunicationList = [
    im.Communication(RunnableName="CoreAcc_Runnable", ROSTopicList=ROSTopicList)
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

IntegrationModel = im.IntegrationModel(
    MetaInfo=MetaInformation,
    FunctionInfo=FunctionInformation,
    ComponentList=ComponentList,
    ModesList=None,
    Datatypes=DatatypesList,
    CommunicationList=CommunicationList,
)


f = open("integration_model_ros2_core_acc.json", "w+")
f.write(json.dumps(IntegrationModel.model_dump(), indent=3))
f.close()
