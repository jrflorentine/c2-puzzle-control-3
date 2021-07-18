def on_received_number(receivedNumber):
    global RadioNum, Step, Input1, Timer, Received, Input2
    RadioNum = receivedNumber
    for index in range(4):
        if Step == index and RadioNum == List1[index]:
            basic.show_icon(IconNames.YES)
            Step = Step + 1
        else:
            basic.show_icon(IconNames.NO)
    if Received == 0:
        Input1 = RadioNum
        Timer = 0
        Received = 1
    elif Received == 1 and Timer < 2:
        Input2 = RadioNum
        if Step == 3:
            NumCheck1()
        else:
            NumCheck2()
    elif Timer > 2:
        Received = 0
        Input1 = 0
        Input2 = 0
radio.on_received_number(on_received_number)

def NumCheck2():
    global Received, Input1, Input2, Timer
    if Input1 == List2[2] and Input2 == List2[3] or Input1 == List2[3] and Input2 == List2[2]:
        basic.show_icon(IconNames.HEART)
    else:
        basic.show_icon(IconNames.NO)
        Received = 0
        Input1 = 0
        Input2 = 0
        Timer = 0
def NumCheck1():
    global Step, Received, Input1, Input2, Timer
    if Input1 == List2[0] and Input2 == List2[1] or Input1 == List2[1] and Input2 == List2[0]:
        basic.show_icon(IconNames.SMALL_HEART)
        Step = 4
        Received = 0
        Input1 = 0
        Input2 = 0
    else:
        basic.show_icon(IconNames.NO)
        Received = 0
        Input1 = 0
        Input2 = 0
        Timer = 0
Timer = 0
RadioNum = 0
Received = 0
Input2 = 0
Input1 = 0
Step = 0
radio.set_group(1)
List1 = [1, 2, 3, 4]
List2 = [1, 2, 3, 4]

def on_forever():
    global Timer
    Timer += 1
    basic.pause(1000)
basic.forever(on_forever)
