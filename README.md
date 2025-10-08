# **ELIV-2025** – Efficient Integration of Cross-Platform Functions onto Service-Oriented Architectures

## **Abstract**
The automotive industry is undergoing a major transformation in Electric/Electronic (E/E) and software architecture, driven by increasing complexity in vehicle technology. This shift is accelerating the rise of **Software-Defined Vehicles (SDVs)** and evolving E/E architectures from **decentralized configurations** with multiple ECUs to **integrated configurations** featuring domain controllers, gateways, and **High-Performance Computers (HPCs)**.

This evolution has led to the coexistence of heterogeneous platforms such as **AUTOSAR Classic**, **AUTOSAR Adaptive**, and prototypical frameworks like **ROS 2™**. To ensure development and integration efficiency, applications must be **hardware- and middleware-agnostic**.

This project introduces a concept for developing applications as **Software as a Product (SaaP)**, enabling efficient integration across multiple platforms. Key elements include:
- Designing applications in a platform-agnostic manner
- Standardizing application interfaces
- Describing application and middleware aspects in **machine-readable formats**
- Developing tools for **semi-automated development and integration**

An example application has been successfully integrated onto AUTOSAR Adaptive and ROS 2, demonstrating the concept’s applicability. Efficiency metrics are also presented.

## **Mission**
The project aims to:
- Design applications that are **agnostic to hardware and software platforms**
- Describe application and platform aspects using **JavaScript Object Notation (JSON)**
- Enable tool-based integration using these descriptions
- Standardize data interfaces based on **Vehicle Signal Specification (VSS)**

## Code of Conduct
See our CoC: https://github.com/ZF-Group/ELIV-presentation/blob/main/CODE_OF_CONDUCT.md

## Supported features
Pydantic models are created to generate JSON schemas for:
- Function model: Describing the application related information agnostic to the underlying hardware and software platform.
- Integration model: Describing the application related information along with the additional information necessary when the application should be integrated to a specific software platform, e.g., AUTOSAR Adaptive.

## Project language
- Language: Python

## Workflow
An example workflow for the AUTOSAR Adaptive platform using Pydantic models and JSON is shown below.

📘 *For detailed information, refer to the complete publication.*
📌 *TODO: Add the link to the publication.*

<p align="center">
  <img width="741" height="343" alt="Workflow Diagram" src="https://github.com/user-attachments/assets/f102dbfe-aacb-4f94-b1d3-734c8e7c4f5d" />
</p>

> **Note**: Function and integration models are currently generated manually. Future development will focus on automating integration JSON generation based on function JSON and platform data.

---

# Getting Started
To begin using this project, ensure you have Python 3.10 or higher installed. Install the required dependencies using pip.

## Dependencies
- The function and integration model is based on Python (tested in v3.10) and the following libraries:
    - pydantic>=2.0
    - typing-extensions>=4.0

## Structure of this repository
- [src/function_model](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/function_model): Contains the function pydantic model. Also, an example function model and JSON for an exemplary ADAS application is included in the folder.
- [src/integration_model](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/integration_model): Contains the integration pydantic model for both AUTOSAR Adaptive and ROS 2 platform.  Also, an example integration model and JSON for the ADAS application is included in the folder.
- [src/example_adas_application.vspec](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/example_adas?_application.vspec): It is the Vehicle Signal Specification of the exemplary ADAS application.

---

# Build and Test
## **Function Model**
- `python function_model.py` → Generates `function_json_schema.json`
- `python function_model_core_acc.py` → Generates `function_model_core_acc.json`

## **Integration Model – AUTOSAR Adaptive**
- `python integration_model_adaptive_autosar.py` → Generates `integration_schema_adaptive_autosar.json`
- `python integration_model_AA_core_acc.py` → Generates `integration_model_AA_core_acc.json`

## **Integration Model – ROS 2**
- `python integration_model_ros2.py` → Generates `integration_schema_ros2.json`
- `python integration_model_ros2_core_acc.py` → Generates `integration_model_ros2_core_acc.json`


# Contribute
TODO: Explain how other users and developers can contribute to make your code better. See contribution.md.
