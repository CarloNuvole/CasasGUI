from tkinter import *
from tkinter.messagebox import *
import pandas as pd
import numpy as np
import os

from Timestamp import Timestamp
from activityList import *


class App(object):
    def __init__(self, title, dim, lastFilter, lastNotification, lastContinue):
        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root, height=900, width=1350)
        self.canvas.grid(row=0, column=0, sticky=N)
        self.slideBar = Scale(self.root, from_=0, to=dim, orient=HORIZONTAL, length=700, width=60, troughcolor='#DCDCDC') #660
        self.slideBar.grid(row=0, column=0, sticky=S, padx=335, pady=20) #325
        self.velocity = 1
        self.playState = True

        # Images
        self.imgON = PhotoImage(file="img/rettangolo_ON.png")
        self.imgOFF = PhotoImage(file="img/rettangolo_OFF.png")
        self.imgONv = PhotoImage(file="img/rettangolo_ON_vert.png")
        self.imgOFFv = PhotoImage(file="img/rettangolo_OFF_vert.png")
        self.imgNextDisabled = PhotoImage(file="img/next_button_disabled.png")
        self.imgPreviousDisabled = PhotoImage(file="img/previous_button_disabled.png")
        self.imgPause = PhotoImage(file="img/pause_button.png")
        self.imgResume = PhotoImage(file="img/play_button.png")
        self.imgStop = PhotoImage(file="img/stop_button.png")
        self.imgNext = PhotoImage(file="img/next_button.png")
        self.imgPrevious = PhotoImage(file="img/previous_button.png")
        self.imgRestart = PhotoImage(file="img/restart_button.png")
        self.backgnd = PhotoImage(file="img/home.png")
        self.imgPatient = PhotoImage(file="img/patient.png")
        self.imgPatientAlert = PhotoImage(file="img/patient_alert.png")

        # Buttons
        self.buttonPause = Button(self.root, image=self.imgPause, borderwidth=0, relief=FLAT,
                                  command=lambda: setPause(self))
        self.buttonPause.grid(row=0, column=0, sticky=SW, padx=90, pady=20)
        self.buttonNext = Button(self.root, image=self.imgNext, borderwidth=0, relief=FLAT,
                                 command=lambda: setNextPatient(self))
        self.buttonNext.grid(row=0, column=0, sticky=SW, padx=250, pady=20)
        self.buttonPrevious = Button(self.root, image=self.imgPrevious, borderwidth=0, relief=FLAT,
                                     command=lambda: setPreviousPatient(self))
        self.buttonPrevious.grid(row=0, column=0, sticky=SW, padx=10, pady=20)
        self.buttonStop = Button(self.root, image=self.imgStop, borderwidth=0, relief=FLAT,
                                 command=lambda: setStop(self))
        self.buttonStop.grid(row=0, column=0, sticky=SW, padx=170, pady=20)

        # BooleanVars
        self.pause = BooleanVar()
        self.pause.set(False)
        self.stop = BooleanVar()
        self.stop.set(False)
        self.restart = BooleanVar()
        self.restart.set(False)
        self.next = BooleanVar()
        self.next.set(False)
        self.previous = BooleanVar()
        self.previous.set(False)

        # OptionMenus
        self.choicesDiagnosis = ["All (default)",
                                 "Dementia",
                                 "MCI",
                                 "Middle age (45-59)",
                                 "Young old (60-74)",
                                 "Old old (75+)",
                                 "Other medical",
                                 "Watch/at risk",
                                 "Younger adult",
                                 "Younger adult (English second language)",
                                 "Diagnosis not available"]
        self.filterActive = StringVar(self.root)
        self.filterActive.set(lastFilter)
        self.filter = OptionMenu(self.root, self.filterActive, *self.choicesDiagnosis)
        self.filter.config(width=12, anchor=W, padx=15)
        self.filter.grid(row=0, column=0, stick=NE, pady=90, padx=80)

        self.choicesNotification = ["In-window text",
                                    "Pop-up window",
                                    "No notification"]
        self.notificationActive = StringVar(self.root)
        self.notificationActive.set(lastNotification)
        self.notification = OptionMenu(self.root, self.notificationActive, *self.choicesNotification)
        self.notification.config(width=12, anchor=W, padx=15)
        self.notification.grid(row=0, column=0, stick=NE, pady=120, padx=80)

        self.choicesContinue = ["Continue with next patient",
                                "Close the application"]
        self.continueActive = StringVar(self.root)
        self.continueActive.set(lastContinue)
        self.continue_ = OptionMenu(self.root, self.continueActive, *self.choicesContinue)
        self.continue_.config(width=15, anchor=W, padx=15)
        self.continue_.grid(row=0, column=0, stick=NE, pady=30, padx=80)

        self.choicesChronology = ["2 movements",
                                  "5 movements",
                                  "10 movements",
                                  "11 movements",
                                  "12 movements",
                                  "13 movements",
                                  "14 movements",
                                  "15 movements",
                                  "16 movements",
                                  "17 movements",
                                  "18 movements",
                                  "19 movements",
                                  "20 movements",
                                  "25 movements",
                                  "30 movements",
                                  "40 movements",
                                  "50 movements"]
        self.chronologyActive = StringVar(self.root)
        self.chronologyActive.set(lastChronology)
        self.chronology = OptionMenu(self.root, self.chronologyActive, *self.choicesChronology)
        self.chronology.config(width=11, anchor=W, padx=15)
        self.chronology.grid(row=0, column=0, stick=NE, pady=60, padx=80)

        # Labels

        self.continueLabel = Label(self.root, text="When finished:")
        self.continueLabel.grid(row=0, column=0, sticky=NE, padx=271, pady=30)

        self.movementsLabel = Label(self.root, text="Patient route length:")
        self.movementsLabel.grid(row=0, column=0, sticky=NE, padx=238, pady=60)

        self.patientInfoText = Label(self.root, text="Filter by diagnosis:")
        self.patientInfoText.grid(row=0, column=0, sticky=NE, padx=246, pady=90)

        self.notificationLabel = Label(self.root, text="Activity notification:")
        self.notificationLabel.grid(row=0, column=0, sticky=NE, padx=241, pady=120)

        self.preferencesLabel = Label (self.root, text="Visualization preferences",  font=("Purisa", 18, 'bold'),
                                  anchor=W)
        self.preferencesLabel.grid(row=0, column=0, sticky=NE, padx=138)

        # Variables
        self.traces = []
        self.chronoPos = []
        self.tracesHistory = []
        self.sensorPair = []
        self.chronoIndex = 0
        self.currentIndex = 0
        self.currentPatient = 0
        self.lastRead = ""

        # Menubar
        menuBar = Menu(self.root)
        self.root.config(menu=menuBar)
        chooseSpeed = Menu(menuBar, tearoff=0)
        chooseSpeedFlow = Menu(menuBar, tearoff=1)

        chooseSpeed.add_command(label="0.25x", command=lambda: setSpeed(4, self))
        chooseSpeed.add_command(label="0.5x", command=lambda: setSpeed(2, self))
        chooseSpeed.add_command(label="1x", command=lambda: setSpeed(1, self))
        chooseSpeed.add_command(label="2x", command=lambda: setSpeed(0.5, self))
        chooseSpeed.add_command(label="4x", command=lambda: setSpeed(0.25, self))
        chooseSpeed.add_command(label="10x", command=lambda: setSpeed(0.10, self))
        chooseSpeed.add_command(label="50x", command=lambda: setSpeed(0.02, self))
        chooseSpeed.add_command(label="250x", command=lambda: setSpeed(0.004, self))
        chooseSpeed.add_command(label="1000x", command=lambda: setSpeed(0.001, self))
        menuBar.add_cascade(label="Speed", menu=chooseSpeed)

        chooseSpeedFlow.add_command(label="Real", command=lambda: setSpeedFlow(True, window))
        chooseSpeedFlow.add_command(label="Automatic", command=lambda: setSpeedFlow(False, window))
        menuBar.add_cascade(label="Speed flow", menu=chooseSpeedFlow)

        self.canvas.create_line(0, 790, 1985, 790, fill='grey', width=2)
        self.canvas.create_image(0, 0, image=self.backgnd, anchor="nw")
        self.patientImg = self.canvas.create_image(1100,850, image=self.imgPatient)

    def writeInfo(self, text):
        txt = self.canvas.create_text(1000, 750, text=text, anchor=W)
        return txt

    def writeTime(self, text):
        txt = self.canvas.create_text(1000, 770, text="Timestamp: " + text, anchor=W)
        return txt

    def writeMoreInfo(self, text):
        txt = self.canvas.create_text(1000, 450, text=text, anchor=W, width=300)
        return txt

    def drawLine(self, i, colour, thickness):
        l = self.canvas.create_line(self.chronoPos[i - 1][0], self.chronoPos[i - 1][1], self.chronoPos[i][0],
                                    self.chronoPos[i][1], fill=colour, width=thickness * 2, arrow='last')
        return l

    def drawLoop(self, i, colour, reps, thickness):
        x = self.chronoPos[i - 1][0]
        y = self.chronoPos[i - 1][1]
        r = 15 + reps + (i % reps)

        l = self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=colour, width=thickness)
        return l

    def drawRoute(self):
        lines = []
        c = 0
        if self.chronoIndex >= 2:

            for i in range(1, len(self.chronoPos)):
                lines.append(self.chronoPos[i])

                for j in range(0, len(self.sensorPair)):
                    c = self.sensorPair.count((self.chronoPos[i], self.chronoPos[i]))

                if (self.chronoPos[i - 1] != self.chronoPos[i]) and (
                        self.chronoPos[i] is not None and self.chronoPos[i - 1] is not None):
                    if i == (len(self.chronoPos) - 1):  # Last movement
                        colour = 'red'
                        thickness = 2
                    elif i == (len(self.chronoPos) - 2):  # 10-2
                        colour = 'black'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 3):  # 10-3
                        colour = '#708090'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 4):  # 10-4
                        colour = '#696969'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 5):  # 10-5
                        colour = '#A9A9A9'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 6):  # 10-6
                        colour = '#C0C0C0'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 7):  # 10-7
                        colour = '#C0C0C0'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 8):  # 10-8
                        colour = '#D3D3D3'
                        thickness = 1
                    else:  # Previous movements
                        colour = '#DCDCDC'
                        thickness = 1

                    lines.append(self.drawLine(i, colour, thickness))

                elif (self.chronoPos[i - 1] == self.chronoPos[i]) and (self.chronoPos[i] is not None) and (
                        self.chronoPos[i - 1] is not None):

                    if i == (len(self.chronoPos) - 1):  # Last movement
                        colour = 'red'
                        thickness = 3
                    elif i == (len(self.chronoPos) - 2):  # 10-2
                        colour = 'black'
                        thickness = 2
                    elif i == (len(self.chronoPos) - 3):  # 10-3
                        colour = '#708090'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 4):  # 10-4
                        colour = '#696969'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 5):  # 10-5
                        colour = '#A9A9A9'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 6):  # 10-6
                        colour = '#C0C0C0'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 7):  # 10-7
                        colour = '#C0C0C0'
                        thickness = 1
                    elif i == (len(self.chronoPos) - 8):  # 10-8
                        colour = '#D3D3D3'
                        thickness = 1
                    else:  # Previous movements
                        colour = '#DCDCDC'
                        thickness = 1
                    lines.append(self.drawLoop(i, colour, c, thickness))

        return lines

    def setSensorState(self, coordinate, status):
        img = None

        if coordinate is not None:
            posX = coordinate[0]
            posY = coordinate[1]

            if isVertical(coordinate) == False:

                if status == "ON" or status == "OPEN" or status == "PRESENT":
                    img = self.canvas.create_image(posX, posY, image=self.imgON)

                if status == "OFF" or status == "CLOSE" or status == "ABSENT":
                    img = self.canvas.create_image(posX, posY, image=self.imgOFF)
            else:
                if status == "ON" or status == "OPEN" or status == "PRESENT":
                    img = self.canvas.create_image(posX, posY, image=self.imgONv)

                if status == "OFF" or status == "CLOSE" or status == "ABSENT":
                    img = self.canvas.create_image(posX, posY, image=self.imgOFFv)
        return img

    def setPatientImg(self, status):
        self.deleteElement(self.patientImg)
        if status:
            self.patientImg = self.canvas.create_image(1100,850, image=self.imgPatientAlert)
        else:
            self.patientImg = self.canvas.create_image(1100, 850, image=self.imgPatient)

    def deleteElement(self, elem):
        self.canvas.delete(elem)


def deleteElements(cnv, elem1, elem2, elem3, elem4, elem5):
    cnv.deleteElement(elem1)
    cnv.deleteElement(elem2)
    cnv.deleteElement(elem3)
    cnv.deleteElement(elem4)

    if elem5:
        for e in cnv.traces:
            cnv.deleteElement(e)
    if elem5 == False:
        for e in cnv.tracesHistory:
            cnv.deleteElement(e)


def concatenateActivity(activityList):
    tmp = ""
    k = 0
    for activity in activityList:
        if k == 0:
            tmp = tmp + "" + activity + "\n"  # Activity title
            k = k + 1
        else:
            tmp = tmp + " • " + activity + "\n"  # Activities

    return tmp


def isVertical(coordinate):
    if coordinate == getCoordinate("D007"):
        return True
    if coordinate == getCoordinate("D014"):
        return True
    if coordinate == getCoordinate("D015"):
        return True
    if coordinate == getCoordinate("D016"):
        return True
    if coordinate == getCoordinate("IOO7"):
        return True

    return False


##########################

def getCoordinate(sensor):
    # region Dxxx - Doors
    if sensor == "D001":
        return [605, 767]

    if sensor == "D002":
        return [846, 10]

    if sensor == "D003":
        return [274, 464]

    if sensor == "D004":
        return [211, 314]

    if sensor == "D005":
        return [353, 457]

    if sensor == "D006":
        return [387, 696]

    if sensor == "D007":  # vertical
        return [956, 511]

    if sensor == "D008":
        return [791, 399]

    if sensor == "D009":
        return [791, 425]

    if sensor == "D010":
        return [789, 480]

    if sensor == "D011":
        return [926, 703]

    if sensor == "D012":
        return [702, 421]

    if sensor == "D013":
        return [557, 312]

    if sensor == "D014":  # vertical
        return [964, 565]

    if sensor == "D015":
        return [964, 603]

    if sensor == "D016":
        return [954, 417]

    # endregion

    # region Mxxx - Movement
    if sensor == "M001":
        return [645, 357]

    if sensor == "M002":
        return [561.5, 267]

    if sensor == "M003":
        return [562, 165]

    if sensor == "M004":
        return [562, 72]

    if sensor == "M005":
        return [672, 70]

    if sensor == "M006":
        return [671, 165]

    if sensor == "M007":
        return [671, 266]

    if sensor == "M008":
        return [755, 309]

    if sensor == "M009":
        return [786, 264]

    if sensor == "M010":
        return [787, 166]

    if sensor == "M011":
        return [784, 70]

    if sensor == "M012":
        return [906, 68]

    if sensor == "M013":
        return [903, 163]

    if sensor == "M014":
        return [903, 264]

    if sensor == "M015":
        return [874, 357]

    if sensor == "M016":
        return [874, 394]

    if sensor == "M017":
        return [875, 506]

    if sensor == "M018":
        return [874, 600]

    if sensor == "M019":
        return [754, 599]

    if sensor == "M020":
        return [752, 683]

    if sensor == "M021":
        return [644, 600]

    if sensor == "M022":
        return [645, 506]

    if sensor == "M023":
        return [645, 395]

    if sensor == "M024":
        return [645, 717]

    if sensor == "M025":
        return [548, 717]

    if sensor == "M026":
        return [552, 625]

    if sensor == "M027":
        return [70, 427]

    if sensor == "M028":
        return [190, 427]

    if sensor == "M029":
        return [288, 428]

    if sensor == "M030":
        return [287, 481]

    if sensor == "M031":
        return [154, 532]

    if sensor == "M032":
        return [154, 616]

    if sensor == "M033":
        return [154, 704]

    if sensor == "M034":
        return [258, 704]

    if sensor == "M035":
        return [261, 615]

    if sensor == "M036":
        return [257, 535]

    if sensor == "M037":
        return [349, 424]

    if sensor == "M038":
        return [372, 502]

    if sensor == "M039":
        return [372, 596]

    if sensor == "M040":
        return [372, 680]

    if sensor == "M041":
        return [371, 713]

    if sensor == "M042":
        return [290, 356]

    if sensor == "M043":
        return [190, 356]

    if sensor == "M044":
        return [197, 290]

    if sensor == "M045":
        return [72, 224]

    if sensor == "M046":
        return [72, 132]

    if sensor == "M047":
        return [71, 55]

    if sensor == "M048":
        return [186, 55]

    if sensor == "M049":
        return [186, 132]

    if sensor == "M050":
        return [188, 223]

    # endregion

    # region Ixxx - Items

    if sensor == "IOO7":  # vertical
        return [937, 510]

    if sensor == "I008":
        return [770, 198]

    if sensor == "I009":
        return [770, 222]

    if sensor == "I011":
        return [534, 330]

    if sensor == "I012":
        return [551, 347]

    return None
    # endregion


##########################

def setPosition(window, dataset, pos, tempo):
    if window.playState == False:
        tempo = 300

    sensor = dataset.iloc[pos]["Sensor"]
    sensorData = dataset.iloc[pos]["Sensor data"]
    timestamp = dataset.iloc[pos]["Timestamp"]
    otherInfo = dataset.iloc[pos]["Other info"]

    window.lastRead = sensor + " " + sensorData

    triggeredSensor = False
    '''GESTIONE DELLA STAMPA DEL PERCORSO '''
    if (sensor[0] == "M" or sensor[0] == "I" or sensor[0] == "D") and (
            sensorData == "ON" or sensorData == "OPEN" or sensorData == "PRESENT") and getCoordinate(
            sensor) is not None:
        triggeredSensor = True

        if len(window.chronoPos) > 0:
            tmp = (window.chronoPos[-1], getCoordinate(sensor))
            window.sensorPair.append(tmp)

        window.chronoPos.append(getCoordinate(sensor))
        window.chronoIndex = window.chronoIndex + 1
        window.traces = (window.drawRoute())

        if window.chronoIndex > int(re.split(' ', window.chronologyActive.get())[0]):  # Route history
            window.chronoPos.pop(0)
            window.sensorPair.pop(0)
            while len(window.chronoPos) > int(re.split(' ', window.chronologyActive.get())[0]):
                window.chronoPos.pop(0)
                window.sensorPair.pop(0)

    if triggeredSensor == False and len(window.chronoPos) > 0:
        window.tracesHistory = (window.drawRoute())

    listDoneActivities = []

    # Other info
    if otherInfo is not np.nan:
        fullActivities = getActivityList(str(otherInfo))

        if len(fullActivities) != 0:
            listDoneActivities.append(fullActivities[0])
            if '-' in otherInfo[0:3]:
                indices = getStartActivityIndex(otherInfo)
            elif '.' in otherInfo[0:3]:
                indices = getActivityIndex(otherInfo)

            for i in indices:
                listDoneActivities.append(fullActivities[int(i)])
                tempo += 300
    coordinate = getCoordinate(dataset.iloc[pos]["Sensor"])

    # region M SENSORS
    if dataset.iloc[pos]["Sensor"][0] == "M" and getCoordinate(dataset.iloc[pos]["Sensor"]) is not None:
        text = window.writeInfo("Movement detected on " + sensor + " - " + sensorData)
        time = window.writeTime("(" + timestamp + ")")
        info = None
        window.setPatientImg(False)
        if otherInfo is not np.nan:
            if window.notificationActive.get() == "In-window text":
                window.setPatientImg(True)
                info = window.writeMoreInfo("Activity detected:\n" + concatenateActivity(listDoneActivities))

            elif window.notificationActive.get() == "Pop-up window":
                window.setPatientImg(True)
                info = window.writeMoreInfo("Activity detected: check pop-up window for details.")
                showinfo("Motion detected", concatenateActivity(listDoneActivities))

        if coordinate is not None:
            sensorState = window.setSensorState(coordinate, sensorData)

        else:
            sensorState = None

        window.root.update()

        window.root.after(tempo, deleteElements(window, text, sensorState, time, info, triggeredSensor))

    # endregion

    # region D SENSORS
    elif dataset.iloc[pos]["Sensor"][0] == "D":
        text = window.writeInfo("Movement detected on door " + sensor + " - " + sensorData)
        time = window.writeTime("(" + timestamp + ")")
        info = None
        window.setPatientImg(False)
        if otherInfo is not np.nan:
            if window.notificationActive.get() == "In-window text":
                window.setPatientImg(True)
                info = window.writeMoreInfo("Activity detected:\n" + concatenateActivity(listDoneActivities))

            elif window.notificationActive.get() == "Pop-up window":
                window.setPatientImg(True)
                info = window.writeMoreInfo("Activity detected: check pop-up window for details.")
                showinfo("Motion detected", concatenateActivity(listDoneActivities))

        if coordinate is not None:
            sensorState = window.setSensorState(coordinate, sensorData)
        else:
            sensorState = None

        window.root.update()

        window.root.after(tempo, deleteElements(window, text, sensorState, time, info, triggeredSensor))
    # endregion

    # region I SENSORS
    elif dataset.iloc[pos]["Sensor"][0] == "I":
        text = window.writeInfo("Movement detected on item " + sensor)
        time = window.writeTime("(" + timestamp + ")")

        info = None
        window.setPatientImg(False)
        if otherInfo is not np.nan:
            if window.notificationActive.get() == "In-window text":
                window.setPatientImg(True)
                info = window.writeMoreInfo("Activity detected:\n" + concatenateActivity(listDoneActivities))

            elif window.notificationActive.get() == "Pop-up window":
                window.setPatientImg(True)
                info = window.writeMoreInfo("Activity detected: check pop-up window for details.")
                showinfo("Motion detected", concatenateActivity(listDoneActivities))

        if coordinate is not None:
            sensorState = window.setSensorState(coordinate, sensorData)
        else:
            sensorState = None

        window.root.update()

        window.root.after(tempo, deleteElements(window, text, sensorState, time, info, triggeredSensor))
    # endregion

    # region NO MOVEMENT DETECTED
    else:
        text = window.writeInfo("No motion detected")
        time = window.writeTime("(" + timestamp + ")")
        window.setPatientImg(False)
        window.root.update()
        window.root.after(0, deleteElements(window, text, None, time, None, triggeredSensor))
    # endregion


def setSpeed(val, obj):
    obj.velocity = val


def setSpeedFlow(val, obj):
    obj.playState = val


def setPause(obj):
    obj.pause.set(not (obj.pause.get()))


def setStop(obj):
    obj.stop.set(not (obj.stop.get()))


def setRestart(obj):
    obj.currentIndex = 0
    obj.restart.set(not (obj.restart.get()))
    setPause(obj)


def setNextPatient(obj):
    obj.next.set(not (obj.next.get()))


def setPreviousPatient(obj):
    obj.previous.set(not (obj.previous.get()))


elem = 1
diagnosis = pd.read_csv('diagnosis.txt', sep=" ", header=None)
diagnosis.columns = ["ID", "Diagnosis"]
lastFilter = "All (default)"
lastNotification = "In-window text"
lastContinue = "Continue with next patient"
lastChronology = "10 movements"
wantClose = False
restarted = False


def getFileString(id):
    if id < 10:
        s = "00" + str(id)
    elif id >= 10 and id < 100:
        s = "0" + str(id)
    else:
        s = str(id)
    return 'dataset/' + s + '.txt'


def searchNextPatient(obj, type):
    diagnosisID = obj.choicesDiagnosis.index(type)
    pos = obj.currentPatient

    while pos < 400:
        pos += 1
        if diagnosis.iloc[pos]["Diagnosis"] == diagnosisID or diagnosisID == 0:
            if os.path.isfile(getFileString(pos)):
                return pos
    return -1


def searchPreviousPatient(obj, type):
    diagnosisID = obj.choicesDiagnosis.index(type)
    pos = obj.currentPatient
    while pos > 1:
        pos -= 1
        if diagnosis.iloc[pos]["Diagnosis"] == diagnosisID or diagnosisID == 0:
            if os.path.isfile(getFileString(pos)):
                return pos
    return -1


while elem <= 400 and not wantClose:
    newElem = elem + 1
    try:
        dataset = pd.read_csv(getFileString(elem), sep=" ", error_bad_lines=False, header=None)
        dataset.columns = ["Timestamp", "Sensor", "Sensor data", "Other info"]

    except FileNotFoundError:
        print("Patient #" + str(elem) + " data not found")  # Terminal printing
        elem += 1

    else:
        dim = len(dataset.index)
        window = App("Patient #" + str(elem), dim, lastFilter, lastNotification, lastContinue)
        window.canvas.create_text(1150, 820, text="Monitoring patient #" + str(elem), font=("Purisa", 16, 'bold'),
                                  anchor=W)
        window.canvas.create_text(1150, 840,
                                  text="Diagnosis: " + window.choicesDiagnosis[diagnosis.iloc[elem]["Diagnosis"]],
                                  anchor=W, width=300)

        inPause = False
        inRestart = False
        inStop = False
        dim_ciclo = range(0, dim)

        timeDiff = 300

        window.currentPatient = elem
        changed = False

        while window.currentIndex < dim:
            window.slideBar.set(window.currentIndex)

            if window.pause.get():
                window.buttonPause.configure(image=window.imgResume)
                window.buttonStop.configure(image=window.imgRestart, command=lambda: setRestart(window))
                inRestart = True
                tmp = window.drawRoute()
                tmpInfo = window.writeTime("Process paused.")
                tmpLastData = window.writeInfo("Last data read: " + window.lastRead)
                inPause = True

                window.buttonPause.wait_variable(window.pause)

                while inRestart and window.restart.get():
                    setRestart(window)
                    window.currentIndex = 0
                    window.slideBar.set(window.currentIndex)
                    window.chronoIndex = 0

                    if window.sensorPair is not None:
                        window.sensorPair.clear()

                    if window.chronoPos is not None:
                        window.chronoPos.clear()

                    if window.traces is not None:
                        window.traces.clear()

                    if window.traces is not None:
                        window.tracesHistory.clear()
                    for e in tmp:
                        window.deleteElement(e)
                    inPause = False
                    if tmpInfo is not None:
                        window.deleteElement(tmpInfo)
                    if tmpLastData is not None:
                        window.deleteElement(tmpLastData)
                    window.buttonPause.configure(image=window.imgPause)
                    window.buttonStop.configure(image=window.imgStop, command=lambda: setStop(window))
                    inRestart = False
                    window.pause.set(not window.pause.get())
                    break

            if not window.pause.get() and inPause:
                for e in tmp:
                    window.deleteElement(e)
                inPause = False
                if tmpInfo is not None:
                    window.deleteElement(tmpInfo)
                if tmpLastData is not None:
                    window.deleteElement(tmpLastData)

                window.buttonPause.configure(image=window.imgPause)
                window.buttonStop.configure(image=window.imgStop, command=lambda: setStop(window))
                inRestart = False

            if window.stop.get() and not inRestart:
                result = askquestion("Exiting application", "Are you sure you want to close the application?",
                                     icon='warning')
                if result == 'yes':  # positive button
                    wantClose = True
                    break
                else:  # negative button
                    window.stop.set(not window.stop.get())

            checkNext = searchNextPatient(window, window.filterActive.get())
            checkPrevious = searchPreviousPatient(window, window.filterActive.get())

            if checkNext == -1:
                window.buttonNext.configure(image=window.imgNextDisabled, state=DISABLED)
            elif checkNext != -1:
                window.buttonNext.configure(image=window.imgNext, state=NORMAL)
            if checkPrevious == -1:
                window.buttonPrevious.configure(image=window.imgPreviousDisabled, state=DISABLED)
            if checkPrevious != -1:
                window.buttonPrevious.configure(image=window.imgPrevious, state=NORMAL)

            if window.next.get():
                changed = True
                lastFilter = window.filterActive.get()
                elem = searchNextPatient(window, window.filterActive.get())
                break

            if window.previous.get():
                changed = True
                lastFilter = window.filterActive.get()
                elem = searchPreviousPatient(window, window.filterActive.get())
                break

            lastNotification = window.notificationActive.get()
            lastContinue = window.continueActive.get()

            sensorTime = dataset.iloc[window.currentIndex]["Timestamp"]

            actualTime = Timestamp(sensorTime)

            if window.currentIndex != 0 or window.currentIndex != dim_ciclo:
                sensorTimePrecedente = dataset.iloc[window.currentIndex - 1]["Timestamp"]

                sensorTimePrev = Timestamp(sensorTimePrecedente)

                timeDiff = sensorTimePrev.secondsConverter() - actualTime.secondsConverter()

                if timeDiff > 5000:
                    timeDiff = 1000

            window.root.after(int(800 * window.velocity),
                              setPosition(window, dataset, window.currentIndex, int(timeDiff)))

            if window.currentIndex != window.slideBar.get():
                window.chronoIndex = 0

                if window.sensorPair is not None:
                    window.sensorPair.clear()

                if window.chronoPos is not None:
                    window.chronoPos.clear()

                if window.traces is not None:
                    window.traces.clear()

                if window.traces is not None:
                    window.tracesHistory.clear()

            window.currentIndex = window.slideBar.get()

            window.slideBar.set(window.currentIndex)
            window.currentIndex += 1

        if not changed:
            elem = checkNext
        if checkNext == -1 and checkPrevious == -1:
            showinfo("Closing the app",
                     "There are no more data to show with the current filter. The application will end immediately")
        if lastContinue == "Close the application":
            showinfo("Closing the application", "The application will be arrested")

        window.root.destroy()

        if checkNext == -1 and checkPrevious == -1:
            break

        if lastContinue == "Close the application":
            break
