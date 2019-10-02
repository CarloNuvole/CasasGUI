# CASAS GUI
Thesis project.

![CASAS GUI](https://scontent-mxp1-1.xx.fbcdn.net/v/t1.15752-9/s2048x2048/71823942_703495783484635_5314052066270773248_n.png?_nc_cat=111&_nc_oc=AQl5imN3jdPcL5CfHVrerbY6qo98NoT71e_mAWeoNY_1TDtpfKqu0HAhOH-PrqiH99c&_nc_ht=scontent-mxp1-1.xx&oh=ec468d123c2f704da50aabfc1e8f0c05&oe=5DF3A9B8)

# **Before starting**
This project uses Python3 with the following libreries, be sure to have them before running:

- _tkinter_ (pip install tkinter)
- _pandas_ (pip install pandas)
- _numpy_ (pip install numpy)
- _os_
- _re_

# **System requirements**
**REQUIRES AT LEAST 1280x1024 SCREEN RESOLUTION, 1920x1080 or better is recomended**
_If you are using different screen resolution you may lose some information and/or buttons._

This project was written and tested using **Python 3**, be sure to have it installed before execution. Python 2 may be incompatible with some libreries.

The project was **written and tested using Mac OS.** _(Mac OS 10.14 Mojave)
If you are running **Windows** or **Ubuntu** (or other), you may encounter some graphical problems due to _tkinter_, such as un-aligned buttons or strange fonts.
These problems **do not affect functionality**, but only GUI.


# **Setup**
1) Download CASAS dataset from http://casas.wsu.edu/datasets/, choosing _21 Kyoto 400 Cognitive assessment activity data_

2) Extract files in any folder you want.
 
3) In the same folder of the project, create a new folder called _dataset_ and insert all files in _data_ folder of CASAS dataset you downloaded previously.

4) Run **cleanDatabase.py** to set the dataset in order to be used in this project. _python cleanDatabase.py_

5) Move _diagnosis.txt_ from CASAS dataset folder to the main folder of the project.

6) Run **cleanDiagnosis.py** to run this project. _python cleanDiagnosis.py_

7) Run **Tirocinio.py.** _python Tirocinio.py_

# **How to use**
By default, you will start tracking from the first patient avaiable, without any filter based on diagnosis and with in-window text notification about each activity detected.

Using GUI, you can:
- Filter patients by diagnosis
- Be noticed by pop-up window or disable any notification about activity detection
- Pause the tracking and restart (you can restart only pausing tracking)
- Move a slidebar to a desidered position of the dataset
- Increase or decrease velocity (up to 1000x and down to 0.25x) _Velocity toolbar option_
- Choose if you want a real-time (based on time difference between records) or automatic (code-based) tracking _Velocity time toolbar option_

Lines represent a movement from sensor A to sensor B (with an arrow indicating the direction)
Circles represent a loop (from sensor A to sensor A)
