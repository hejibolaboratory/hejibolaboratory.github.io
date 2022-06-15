from psychopy import visual, core, event
myWin = visual.Window((800.0,800.0),allowGUI=False,winType='pyglet',
    monitor='testMonitor', units ='deg', screen=0)
myWin.setRecordFrameIntervals()
psychopyTxt = visual.TextStim(myWin, color=(255,0,0),
                            text = u"PsychoPy is a GREAT tool",
                            units='norm', height=0.1,
                            pos=[0.5, 0.5],anchorVert="top",anchorHoriz="left")
psychopyTxt.draw()
myWin.flip()
core.wait(5.0)