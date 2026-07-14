# How to Run the FTIR Analyzer (User Guide)

You do **not** need to install Python, Jupyter Notebook, or any programming libraries to use this tool. It has been compiled into a standalone Windows application. Follow the simple steps below to run your analysis.

---

## 📥 Step-by-Step Installation

1. **Download the Program:**
   * Go to the **Releases** section on the right side of this GitHub page.
   * Under **Assets**, click on `FTIR_analyzer.zip` to download it.

2. **Extract the Files:**
   * Locate the downloaded `.zip` file in your Downloads folder.
   * Right-click the `.zip` file and select **"Extract All..."** (or use WinRAR/7-Zip) to extract the folder.
   * *Note: The program will not work if you try to run it from inside the zipped folder.*

3. **Open the App:**
   * Open the extracted folder, find the application file named **`ftir_analyzer.exe`**, and double-click it to run.
   * *(Optional)*: You can right-click `ftir_analyzer.exe` and select **"Send to > Desktop (create shortcut)"** for easier access in the future.

---

## 📊 How to Use It

1. **Select Your Data Folder:**
   * Once opened, a window popup will ask you to select the folder where your raw `.txt` FTIR files are stored.
   * Select the folder and click **OK**.

2. **Automatic Processing:**
   * The program will scan your folder, find all `.txt` files, and automatically correct the baseline, identify maximum wavenumbers, and plot all spectra on a single chart.

3. **Output Results:**
   * **The Graph:** A high-resolution chart (`ftir_plot.png`) will be automatically saved **inside the very same folder** you selected.
   * **The Data Sheet:** An aggregated spreadsheet (`ftir_results.csv`) will also be saved in that folder, ready to be opened in Excel.

---

## ⚠️ Troubleshooting
* **"Windows protected your PC" popup:** Because this is a custom-made laboratory tool without a paid Microsoft digital signature, Windows Defender might show a blue warning. Simply click on **"More info"** and then click the **"Run anyway"** button.
* **No files found:** Double-check if your raw files are saved as `.txt` (lowercase) and that they are placed directly inside the selected folder.