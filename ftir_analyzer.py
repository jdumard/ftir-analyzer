# ===========================================================
# FTIR SPECTRA ANALYZER
# Version: 1.0
# ===========================================================
# Developer: Juliana Dumard
# ===========================================================
# Equipment: IR-Tracer 100 (Shimadzu)
# File Format: .txt
# Outputs: Spectra and absorbance in the carbonyl band
# ===========================================================


# ===========================================================
# Import Libraries
# ===========================================================
import os
import glob
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


# ===========================================================
# Analysis Parameter Definition
# ===========================================================
# For naphthenic acid detection, the region of interest
# is the carbonyl band, near 1710 cm-1

# Region of interest band
band_min, band_max = 1700, 1720

# Zero reference region for offset calculation
ref_min, ref_max = 1800, 1850


# ===========================================================
# FUNCTION: Select source folder containing files
# ===========================================================
# Only files with .txt extension can be imported

def select_folder():
    # Creates a hidden Tkinter root window to prevent an empty app from opening in the background
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Forces the window to appear in front of all other applications
    
    # Opens the visual dialog box for the user to select the folder
    selected_folder = filedialog.askdirectory(title='Select the folder containing the FTIR result files (.txt)')
    return selected_folder


# ============================================================
# User Folder Selection
# ============================================================
data_folder = select_folder()


# ============================================================
# FILE ANALYSIS
# ============================================================
# Create an empty list to store the results
results = []

# Check if a folder was selected
if not data_folder:
    print('No folder selected. Execution canceled.')
else:
    print(f'Selected folder: {data_folder}') # Shows the path of the selected folder
    
    # --- If the folder is successfully selected, the files are analyzed ---

    # Create a search path combining the correct operating system slashes with the selected folder path
    search_path = os.path.join(data_folder, '*.txt')
    # Retrieve and save the files from the folder
    files = glob.glob(search_path)
    
    # Check if there are .txt files in the folder
    if len(files) == 0:
        print('Warning: No .txt files were found in this folder.')
    else:
        print(f'Success! Found {len(files)} files. Processing...\n')
        
        # --- If the folder contains .txt files, proceed with the analysis ---

        # Set up the figure for the plot to be generated
        plt.figure(figsize=(12, 7))
        
        # Loop for automated file processing
        for file in files:
            file_path = Path(file)
            sample_name = file_path.stem  # The sample name will be the filename without the .txt extension
            
            try:
                # Load each result file as a CSV-formatted file
                df = pd.read_csv(file, 
                                 sep='\t', 
                                 skiprows=4, # Number of header rows
                                 names=['wavenumber', 'abs'], # Column headers
                                 decimal='.', 
                                 header=None)
                
                # Create a column in the DataFrame to identify the sample
                df['sample'] = sample_name

                # --- EXPERIMENTAL DATA PROCESSING -------------------
                # Baseline correction --> Performed separately for each sample
                # 1. Calculate the average in the reference region (Baseline)
                mask_ref = df['wavenumber'].between(ref_min, ref_max)
                offset_value = df.loc[mask_ref, 'abs'].mean() # The offset will be the mean of the selected zero-region absorbances
        
                 # 2. Spectrum correction
                df['corrected_abs'] = df['abs'] - offset_value # Correct the entire spectrum based on the offset value
        
                # 3. Identification of the absorbance maximum (Wavenumber and intensity)
                mask_band = df['wavenumber'].between(band_min, band_max)
                df_band = df.loc[mask_band]
        
                # Find the index of the maximum value within the selected region of df_band
                idx_band = df_band['corrected_abs'].idxmax()

                # Get the wavenumber and absorbance of the strongest peak
                wavenumber_band = df_band.loc[idx_band, 'wavenumber']
                absorbance_band = df_band.loc[idx_band, 'corrected_abs']

                # --- END OF DATA PROCESSING ------------------------

                # Store results in the results list
                results.append({
                    'Sample': sample_name, 
                    'Wavenumber (cm⁻¹)': wavenumber_band, 
                    'Absorbance (u.a.)': absorbance_band
                })
        
                # --- GENERATE PLOT ---------------------------------
                
                # Create the legend using the name extracted from the filename
                legend_text = f"{sample_name} (Abs = {absorbance_band:.3f})"
                
                # Plot the curve for this specific file
                plt.plot(df['wavenumber'], df['corrected_abs'], label=legend_text)

            # If file processing fails, print the error   
            except Exception as e:
                print(f"Failed to process file {file_path.name}: {e}")
        

        # --- Plot formatting and display --------------------------
        plt.title('FTIR Spectra - Corrected baseline', fontsize=14)
        plt.xlabel('Wavenumber (cm⁻¹)', fontsize=12)
        plt.ylabel('Absorbance (u.a.)', fontsize=12)
        
        # Invert X-axis and set axis limits
        plt.xlim(max(df['wavenumber']), min(df['wavenumber']))

        # Annotate the wavenumber of maximum absorbance
        df_res = pd.DataFrame(results) # Convert the results into a DataFrame to extract the necessary information
        wavenumber_target = df_res['Wavenumber (cm⁻¹)'].max()
        plt.axvline(x=wavenumber_target, color='gray', linestyle='--', alpha=0.7, zorder=1)
        # Add text with the wavenumber value at the top of the plot
        plt.text(wavenumber_target, plt.gca().get_ylim()[1] * 0.97, f" Max: {wavenumber_target:.5} cm⁻¹", 
                 color='black', fontsize=9, weight='bold', va='center')

        # Create legend
        plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
        plt.grid(True, linestyle=':', alpha=0.5)

        plt.tight_layout()


        # --- SAVE RESULTS -----------------------------------------

        # Destination path for the results
        destination_path = Path(data_folder) # Convert selected directory to a Path object
        plot_path = destination_path / 'ftir_plot.png'
        csv_path = destination_path / 'ftir_results.csv'

        # --- Save results to .csv file ----------------------------
        df_res.to_csv(csv_path, index=False)  
        print('\nResults file saved.') 

        # --- Save plot --------------------------------------------
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        print('\nPlot saved.')

        # --- Display plot -----------------------------------------
        print('\nProcess completed! Generating plot...')
        plt.show()