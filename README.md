# CASAS GUI
Thesis project.

![Image description](https://scontent-fco1-1.xx.fbcdn.net/v/t1.15752-9/s2048x2048/71591951_471759277014124_601849601070202880_n.png?_nc_cat=107&_nc_oc=AQn7jTuFk0qjfySoiHn7m504tbtUUvaV_RoXHnl91lYHvgGkCEx-QrkUSFhoE-ioTyA&_nc_ht=scontent-fco1-1.xx&oh=f4617578777aa8315883ecb881fbdcbd&oe=5DEFCE7B)

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

