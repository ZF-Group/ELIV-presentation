# Integration model for Adaptive AUTOSAR software platform for CoreACC application
from pathlib import Path
import sys
import json

sys.path.append(str(Path.cwd().parent.joinpath("IntegrationModel")))
import integration_model_adaptive_autosar as im

MetaInformation = im.MetaInformation(
    Authority="ZF Friedrichshafen AG, DIRDP1",
    Author="Parthasarathy Nadarajan",
    Date="2025-08-29",
    Version="1.0.0",
)

FunctionInformation = im.FunctionInformation(
    FunctionName="Core Acc Application",
    Responsible="Parthasarathy Nadarajan",
    Description="Core Acc application to integrate with Green Acc to form EcoControl",
)

FunctionListCoreAccAlgorithm = [
    im.Function(
        Name="CoreAcc_Init",
        RunType="Init",
        Modes=["Startup"],
        CycleTime=None,
        Scheduling="Preemptive",
    ),
    im.Function(
        Name="CoreAcc_Step",
        RunType="Cyclic",
        Modes=["Run"],
        CycleTime=50.0,
        Scheduling="Non-preemptive",
    ),
    im.Function(
        Name="CoreAcc_Terminate",
        RunType="Terminate",
        Modes=["Terminate"],
        CycleTime=None,
        Scheduling="Non-preemptive",
    ),
]

EventListMapToCoreAcc = [
    im.Event(
        Name="ADAS_Map_DFS_MDIGeneralMapDataSpdUnitTyp",
        DataType="uint8_t",
        DataMappingList=None,
    ),
]

ServiceListMapToCoreAcc = [
    im.Services(Events=EventListMapToCoreAcc, Fields=[], Methods=[])
]

ProviderListMapToCoreAcc = [
    im.Provider(
        ContractName="AdaptiveAUTOSAR",
        Name="SOME/IP",
        ServiceDeploymentType="SOME/IP",
        ServiceInstanceID=None,
    )
]

EventListChassisToCoreAcc = [
    im.Event(Name="Chassis_Brake_CylP", DataType="double", DataMappingList=None),
    im.Event(Name="Chassis_Steering_WhlAg", DataType="double", DataMappingList=None),
    im.Event(
        Name="Chassis_IMU_LongitudinalAccleration",
        DataType="double",
        DataMappingList=None,
    ),
]

ServiceListChassisToCoreAcc = [
    im.Services(Events=EventListChassisToCoreAcc, Fields=[], Methods=[])
]

ProviderListChassisToCoreAcc = [
    im.Provider(
        ContractName="AdaptiveAUTOSAR",
        Name="SOME/IP",
        ServiceDeploymentType="SOME/IP",
        ServiceInstanceID=None,
    )
]

EventListCoreAccOutput = [
    im.Event(Name="ADAS_EcoControl_Status", DataType="uint8_t", DataMappingList=None),
]

ServiceListCoreAccOutput = [
    im.Services(Events=EventListCoreAccOutput, Fields=[], Methods=[])
]

EventListCoreAccToEcoControl = [
    im.Event(Name="ADAS_EcoControl_IsEnabled", DataType="bool", DataMappingList=None),
    im.Event(Name="Vehicle_Mass", DataType="double", DataMappingList=None),
]

ServiceListCoreAccToEcoControl = [
    im.Services(Events=EventListCoreAccToEcoControl, Fields=[], Methods=[])
]


ServiceInterfaceListCoreAccAlgorithm = [
    im.ServiceInterface(
        Name="MapToCoreAcc",
        Role="Consumer",
        ServiceList=ServiceListMapToCoreAcc,
        Provider=ProviderListMapToCoreAcc,
    ),
    im.ServiceInterface(
        Name="ChassisToCoreAcc",
        Role="Consumer",
        ServiceList=ServiceListChassisToCoreAcc,
        Provider=ProviderListChassisToCoreAcc,
    ),
    im.ServiceInterface(
        Name="CoreAccOutput",
        Role="Provider",
        ServiceList=ServiceListCoreAccOutput,
        Provider=None,
    ),
    im.ServiceInterface(
        Name="CoreAccToEcoControl",
        Role="Provider",
        ServiceList=ServiceListCoreAccToEcoControl,
        Provider=None,
    ),
]

ServiceInterfaceListGatewayInputAlgorithm = [
    im.ServiceInterface(
        Name="ChassisToCoreAcc",
        Role="Provider",
        ServiceList=ServiceListChassisToCoreAcc,
        Provider=None,
    ),
    im.ServiceInterface(
        Name="MapToCoreAcc",
        Role="Provider",
        ServiceList=ServiceListMapToCoreAcc,
        Provider=None,
    ),
]

ProviderListCoreAccToEcoControl = [
    im.Provider(
        ContractName="AdaptiveAUTOSAR",
        Name="SOME/IP",
        ServiceDeploymentType="SOME/IP",
        ServiceInstanceID=None,
    )
]

ServiceInterfaceListGreenAccAlgorithm = [
    im.ServiceInterface(
        Name="CoreAccToEcoControl",
        Role="Consumer",
        ServiceList=ServiceListCoreAccToEcoControl,
        Provider=ProviderListCoreAccToEcoControl,
    )
]

ComponentList = [
    im.Component(
        Name="CoreAcc",
        ExecutableName="CoreAccExecutable",
        HeaderFiles=None,
        FunctionGroupModes=["Startup", "Run", "Terminate"],
        FunctionList=FunctionListCoreAccAlgorithm,
        ParameterList=None,
        ServiceInterfaceList=ServiceInterfaceListCoreAccAlgorithm,
    ),
]

FunctionModel = im.FunctionModel(
    MetaInformation=MetaInformation,
    FunctionInformation=FunctionInformation,
    ComponentList=ComponentList,
    DataTypes=None,
)

f = open("integration_model_AA_core_acc.json", "w+")
f.write(json.dumps(FunctionModel.model_dump(), indent=3))
f.close()
