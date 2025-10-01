# ELIV-2025 - Efficient Integration of Cross Platform Functions onto Service-Oriented Architectures
## Abstract
The automotive industry is currently undergoing a major transformation with respect to the Electric/Electronic (E/E) and software architecture, driven by a significant increase in the complexity of the technological stack within a vehicle. This complexity acts as a driving force for Software-Defined Vehicles (SDVs) leading to the evolution of the automotive E/E architectures from decentralized configuration comprising multiple Electronic Control Units (ECUs) towards a more integrated configuration comprising a smaller number of ECUs, domain controllers, gateways, and High-Performance Computers (HPCs). This transition along with several other reasons have resulted in heterogeneous software platforms such as AUTOSAR Classic, AUTOSAR Adaptive, and prototypical frameworks like ROS 2™. It is therefore essential to develop applications that are both hardware- and platform/middleware-agnostic to attain development and integration efficiency. This work presents an application development and integration concept to facilitate developing applications as Software as a Product (SaaP), while simultaneously ensuring efficient integration onto multiple software architecture platforms. The concept involves designing applications in a hardware- and software platform-agnostic manner and standardizing application interfaces. It also includes describing the relevant aspects of the application and corresponding middleware in a machine-readable format to aid the integration of developed applications. Additionally, tools are developed to facilitate semi-automation of the development and integration processes. An example application has been developed and integrated onto AUTOSAR Adaptive and ROS 2, demonstrating the applicability of the approach. Finally, metrics are presented to show the efficiency of the overall concept.

## Mission
The aim of the project is to design the applications in such a way that they are agnostic to the underlying hardware and software platforms. The relevant aspects of the application and the underlying software platforms are described in a machine-readable format, i.e., JavaScript Object Notation (JSON) that is in turn consumed by tools to enable efficient integration of applications. The project also aims to standardize the data interface of the application based on Vehicle Signal Specification (VSS).

## Code of Conduct
See our CoC: https://github.com/ZF-Group/ELIV-presentation/blob/main/CODE_OF_CONDUCT.md

## Supported features
Pydantic models are created to generate JSON schemas for:
- Function model: Describing the application related information agnostic to the underlying hardware and software platform.
- Integration model: Describing the application related information along with the additional information necessary when the application should be integrated to a specific software platform, e.g., AUTOSAR Adaptive.

## Project language
- Language: Python

## Workflow
An example workflow for the AUTOSAR Adaptive platform with the Pydantic models and corresponding JSONs is shown in the Figure below. For detailed information, refer to the complete publication: TODO: Add the link to the publication.

<p align="center"><img width="741" height="343" alt="image" src="https://github.com/user-attachments/assets/f102dbfe-aacb-4f94-b1d3-734c8e7c4f5d" />

Note: The generation of the function model and the integration model is currently done manually. The automatic generation of the integration JSON based on the function JSON and the software platform information is of future development scope.

# Getting Started
## Dependencies
- The function and integration model is based on Python (tested in v3.10) and the following libraries:
    - pydantic>=2.0
    - typing-extensions>=4.0

## Structure of this repository
- [src/function_model](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/function_model): Contains the function pydantic model. Also, an example function model and JSON for an exemplary ADAS application is included in the folder.
- [src/integration_model](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/integration_model): Contains the integration pydantic model for both AUTOSAR Adaptive and ROS 2 platform.  Also, an example integration model and JSON for the ADAS application is included in the folder.
- [src/example_adas_application.vspec](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/example_adas?_application.vspec): It is the Vehicle Signal Specification of the exemplary ADAS application.

# Build and Test
- Run the script [function_model.py](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/function_model) to generate the function JSON schema: `python function_model.py`. The output of the script is the `function_json_schema.json` file.
- Run the script [function_model_core_acc.py](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/function_model) to generate the function JSON for the exemplary ADAS application: `python function_model_core_acc.py`. The output of the script is the `function_model_core_acc.json` file.
- Run the script [integration_model_adaptive_autosar.py](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/integration_model) to generate the integration JSON schema: `python integration_model_adaptive_autosar.py`. The output of the script is the `integrarion_schema_adaptive_autosar.json` file.
- Run the script [integration_model_AA_core_acc.py](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/integration_model) to generate the integration JSON for the exemplary ADAS application: `python integration_model_AA_core_acc.py`. The output of the script is the `integration_model_AA_core_acc.json` file.

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. See contribution.md.
