---
marp: true
size: 16:9
class:
  - invert
  - lead
color: white
backgroundImage: url(bg-image.png)
paginate: true
footer: "Copyright by Jibo He"
---

# PsychoPy Emotiv EEG

Jibo He, Ph.D.
Department of Psychology, Tsinghua University
hejibolaboratory@pku.org.cn

---
# Prepare Emotiv hardware and software:
We recommend that you use the EmotivLauncher and or EmotivPro software to establish that the headset is connected and the quality of the signals are good before running the experiment with Psychopy.

---
# EEG output file format:
- edf
- csv
- gzipped csv (need additional license)

We recommend viewing the eeg data in EmotivPro from which it can be exported as a csv or edf file. However, if you do want PschoPy to record the data into a gzipped csv file you need to set an environment variable CORTEX_DATA=1. Additionally you will need to apply for a RAW EEG API license. See: https://emotiv.gitbook.io/cortex-api/#prerequisites for more details.


---
# Emotiv-based PsychoPy online study
- Pavlovia not supported
- work good in Emotiv OMNI

If you are exporting the experiment to HTML the emotiv components will have no effect in Pavlovia. To import the experiment into Emotiv OMNI, export the experiment to HTML and follow the instructions in the OMNI platform.



---
# References:
https://www.psychopy.org/builder/components/emotiv_marking.html

## 当前备课资料
https://github.com/psychopy/psychopy/blob/release/docs/source/builder/components/emotiv_record.rst
