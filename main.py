def on_received_number(receivedNumber):
    global RadioNum, Input1, Timer, Received, Input2
    RadioNum = receivedNumber
    if Step <= 3:
        NumCheck1()
    elif Step > 3:
        if Received == 0:
            Input1 = RadioNum
            makerbit.show_string_on_lcd1602("Input1: ", makerbit.position1602(LcdPosition1602.POS1), 8)
            makerbit.show_string_on_lcd1602("" + str((Input1)),
                makerbit.position1602(LcdPosition1602.POS9),
                1)
            Timer = 0
            Received = 1
        elif Received == 1 and Timer < 2:
            Input2 = RadioNum
            if Step == 5:
                makerbit.show_string_on_lcd1602("Input2: ", makerbit.position1602(LcdPosition1602.POS17), 8)
                makerbit.show_string_on_lcd1602("" + str((Input1)),
                    makerbit.position1602(LcdPosition1602.POS25),
                    1)
                NumCheck2()
            else:
                NumCheck3()
        elif Timer > 2:
            Received = 0
            Input1 = 0
            Input2 = 0
radio.on_received_number(on_received_number)

def NumCheck2():
    global Received, Input1, Input2, Step, Timer
    if Input1 == List2[0] and Input2 == List2[1] or Input1 == List2[1] and Input2 == List2[0]:
        basic.show_icon(IconNames.SMALL_HEART)
        Received = 0
        Input1 = 0
        Input2 = 0
        Step += 1
    else:
        basic.show_icon(IconNames.NO)
        basic.show_number(Input1)
        basic.show_number(Input2)
        Received = 0
        Input1 = 0
        Input2 = 0
        Timer = 0
def NumCheck1():
    global Step
    if RadioNum == List1[Step]:
        basic.show_icon(IconNames.YES)
        Step = Step + 1
    else:
        basic.show_icon(IconNames.NO)
def NumCheck3():
    global Received, Input1, Input2, Timer
    if Input1 == List2[2] and Input2 == List2[3] or Input1 == List2[3] and Input2 == List2[2]:
        basic.show_icon(IconNames.HEART)
    else:
        basic.show_icon(IconNames.NO)
        Received = 0
        Input1 = 0
        Input2 = 0
        Timer = 0
RadioNum = 0
Timer = 0
Received = 0
Step = 0
Input2 = 0
Input1 = 0
List2: List[number] = []
List1: List[number] = []
radio.set_group(1)
List1 = [1, 2, 3, 4]
List2 = [1, 2, 3, 4]
Input1 = 0
Input2 = 0
Step = 0
Received = 0
Timer = 0
makerbit.clear_lcd1602()

def on_forever():
    global Timer
    Timer += 1
    basic.pause(1000)
basic.forever(on_forever)
