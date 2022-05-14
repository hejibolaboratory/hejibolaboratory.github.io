---
marp: true
theme: default
paginate: true
---
<!-- page_number: true -->
# Emotiv EEG Analysis in Python using mne-python
## 《大数据与多模态》
Dr. Jibo He
Tsinghua University
![](./sleep-deprived%20brain-0-cover.jpeg)

---
# 课程目的

- 讲述EEG的原理
- Emotiv 的操作
- 使用Python获取Emotiv EEG数据 
- Emotiv 的数据分析

---

# convert Emotiv edf file to csv file. 

- https://stackoverflow.com/questions/52293033/how-to-convert-edf-file-into-csv-file-in-python

```python

import numpy as np
import mne
edf = mne.io.read_raw_edf('your_edf_file.edf')
header = ','.join(edf.ch_names)
np.savetxt('your_csv_file.csv', edf.get_data().T, delimiter=',', header=header)
```

---
# Emotiv EEG CSV file variable description

- https://emotiv.gitbook.io/emotivpro-v3/managing-your-eeg-data-recordings/exporting-an-eeg-data-recording/csv-files

