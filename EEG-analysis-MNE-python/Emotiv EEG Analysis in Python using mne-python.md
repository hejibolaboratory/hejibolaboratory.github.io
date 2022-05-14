---
marp: true
---

# Emotiv EEG Analysis in Python using mne-python

---

# convert Emotiv edf file to csv file. 

- https://stackoverflow.com/questions/52293033/how-to-convert-edf-file-into-csv-file-in-python

- python

import numpy as np
import mne
edf = mne.io.read_raw_edf('your_edf_file.edf')
header = ','.join(edf.ch_names)
np.savetxt('your_csv_file.csv', edf.get_data().T, delimiter=',', header=header)

---
# Emotiv EEG CSV file variable description

- https://emotiv.gitbook.io/emotivpro-v3/managing-your-eeg-data-recordings/exporting-an-eeg-data-recording/csv-files

