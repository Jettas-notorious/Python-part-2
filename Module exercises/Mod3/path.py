try:
    stream = open("C:\\Users\\Jettas\\Documents\\NGI modules\\Python part 2\\Module exercises\\Mod3")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)

