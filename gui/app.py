from appJar import gui

app = gui()


app.addLabel("welcome", "Welcome to the number game!")
app.setLabelBg("welcome", "blue")


app.go()
