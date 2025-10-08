# ELIV-2025 – Efficient Integration of Cross-Platform Functions onto Service-Oriented Architectures

![Python](https://img.shields.io/badge/language-Python-blue)

## Abstract

The automotive industry is rapidly evolving its Electric/Electronic (E/E) and software architectures in response to growing vehicle complexity. This transformation has led to the coexistence of multiple platforms, including:

- **AUTOSAR Classic**
- **AUTOSAR Adaptive**
- **ROS 2™** (Robot Operating System)

To address integration and development challenges across these heterogeneous environments, this project presents a concept for building applications as **Software as a Product (SaaP)**. The approach focuses on:

- Designing applications in a platform-agnostic manner
- Standardizing application interfaces
- Describing application and middleware aspects in **machine-readable formats** (JSON)
- Providing tools for **semi-automated development and integration**

A demonstration application has been successfully integrated onto AUTOSAR Adaptive and ROS 2, validating the approach and providing efficiency metrics.

---

## Mission

Our objectives are to:

- Develop applications agnostic to hardware and software platforms
- Use **JSON** to describe application and platform aspects
- Enable tool-based integration leveraging these descriptions
- Standardize data interfaces using **Vehicle Signal Specification (VSS)**

---

## Code of Conduct

Please review our [Code of Conduct](https://github.com/ZF-Group/ELIV-presentation/blob/main/CODE_OF_CONDUCT.md).

---

## Features

- **Function Model:** Pydantic models generate JSON schemas to describe application information independently of the underlying platform.
- **Integration Model:** Pydantic models describe integration details required for specific platforms (e.g., AUTOSAR Adaptive, ROS 2).

---

## Project Language

- **Language:** Python (tested with v3.10+)

---

## Workflow

Below is a sample workflow for the AUTOSAR Adaptive platform using Pydantic models and JSON:

<p align="center">
  <img width="741" height="343" alt="Workflow Diagram" src="https://github.com/user-attachments/assets/f102dbfe-aacb-4f94-b1d3-734c8e7c4f5d" />
</p>

> **Note:** Function and integration models are currently generated manually. Future releases aim to automate JSON generation based on function and platform data.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

```bash
pip install pydantic>=2.0 typing-extensions>=4.0
```

### Repository Structure

- [`src/function_model`](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/function_model): Function Pydantic model, example function model, and JSON for an exemplary ADAS application.
- [`src/integration_model`](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/integration_model): Integration Pydantic models for AUTOSAR Adaptive and ROS 2 platforms, with example integration models and JSON.
- [`src/example_adas_application.vspec`](https://github.com/ZF-Group/ELIV-presentation/tree/main/src/example_adas_application.vspec): Vehicle Signal Specification (VSS) for the exemplary ADAS application.

---

## Build and Test

### Function Model

- Generate function model schema:
  ```bash
  python function_model.py  # Outputs: function_json_schema.json
  ```
- Generate function model for core ACC:
  ```bash
  python function_model_core_acc.py  # Outputs: function_model_core_acc.json
  ```

### Integration Model – AUTOSAR Adaptive

- Generate integration schema:
  ```bash
  python integration_model_adaptive_autosar.py  # Outputs: integration_schema_adaptive_autosar.json
  ```
- Generate integration model for core ACC:
  ```bash
  python integration_model_AA_core_acc.py  # Outputs: integration_model_AA_core_acc.json
  ```

### Integration Model – ROS 2

- Generate integration schema for ROS 2:
  ```bash
  python integration_model_ros2.py  # Outputs: integration_schema_ros2.json
  ```
- Generate integration model for core ACC:
  ```bash
  python integration_model_ros2_core_acc.py  # Outputs: integration_model_ros2_core_acc.json
  ```

---

## Contributing

We welcome contributions to improve code quality, add features, and expand platform support. Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

**TODO:** Further instructions for contributing will be added soon.

---

## Publication

For full project details, refer to the upcoming publication.

*TODO: Add the link to the publication when available.*

---

## Contact & Support

For questions or support, please open an issue or contact the maintainers via GitHub.
