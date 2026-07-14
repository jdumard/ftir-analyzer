# FTIR Spectra Automatic Baseline Corrector & Visualizer

A Python-based automation tool designed to streamline the processing, baseline correction, and visualization of Fourier-transform infrared spectroscopy (FTIR) data. This project eliminates manual data entry and formatting bottlenecks for laboratory researchers, enabling bulk processing through an intuitive graphical user interface (GUI).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Specific Application & Scope
> **Note on Customization**: This version of the analyzer has been custom-tailored for a specific laboratory setup.
* **Target Equipment**: Configured specifically to parse and process raw data output from a dedicated FTIR spectrometer model (Shimadzu IR-Tracer 100), matching its default file export structure and column headers.
* **Target Spectral Band**: Optimized specifically for the carbonyl band (C=O stretching region). The automated baseline alignment and peak-picking algorithms are calibrated to detect, evaluate, and annotate precise peak intensity variations and shifts in this specific chemical region.

## 🧪 Scientific & Technical Background
FTIR datasets often suffer from baseline shifts due to instrumental drift or sample preparation. This script automates:
1. **Bulk Importing**: Recursively loads multiple raw `.txt` spectrometer outputs.
2. **Metadata Extraction**: Cleanly extracts sample names dynamically from file paths, removing noisy directory prefixes and extensions.
3. **Baseline Correction**: Puts the dataset through a baseline-zeroing threshold reference (at customizable regions).
4. **Data Aggregation**: Merges analyzed curves and peaks into a single structured Pandas DataFrame.
5. **Dynamic Plotting**: Automatically finds wavenumber peaks and overlays all spectra in a single, publication-ready Matplotlib chart with precise annotations.

## 🛠️ Built With
* **Python 3**
* **Pandas** - Data manipulation and cleaning
* **Matplotlib** - Data visualization and plotting
* **Tkinter** - Native OS directory selection GUI
* **PyInstaller** - Code compilation into a standalone executable

## 📂 Repository Structure
* `ftir_analyzer.py`: The main Python script containing the ETL pipeline and visualization logic.
* `.gitignore`: Configured to keep the repository clean of compiled binaries (`/dist`, `/build`) and cache.
* `LICENSE`: MIT License terms allowing open-source distribution and modifications.
* `INSTRUCTIONS.md`: Instructions to download and use the latest version of the FTIR Analyzer.
