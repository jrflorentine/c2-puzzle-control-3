radio.onReceivedNumber(function (receivedNumber) {
    RadioNum = receivedNumber
    if (Step <= 3) {
        NumCheck1()
    } else if (Step > 3) {
        if (Received == 0) {
            Input1 = RadioNum
            Timer = 0
            Received = 1
        } else if (Received == 1 && Timer < 2) {
            Input2 = RadioNum
            if (Step == 4) {
                LCDShow()
                NumCheck2()
            } else {
                LCDShow()
                NumCheck3()
            }
        } else if (Timer > 2) {
            Received = 0
            Input1 = 0
            Input2 = 0
        }
    }
})
function NumCheck2 () {
    if (Input1 == List2[0] && Input2 == List2[1] || Input1 == List2[1] && Input2 == List2[0]) {
        basic.showIcon(IconNames.SmallHeart)
        Received = 0
        Input1 = 0
        Input2 = 0
        Step += 1
    } else {
        basic.showIcon(IconNames.No)
        Received = 0
        Input1 = 0
        Input2 = 0
        Timer = 0
    }
}
function NumCheck1 () {
    if (RadioNum == List1[Step]) {
        basic.showIcon(IconNames.Yes)
        Step = Step + 1
    } else {
        basic.showIcon(IconNames.No)
    }
}
function NumCheck3 () {
    if (Input1 == List2[2] && Input2 == List2[3] || Input1 == List2[3] && Input2 == List2[2]) {
        basic.showIcon(IconNames.Heart)
    } else {
        basic.showIcon(IconNames.No)
        Received = 0
        Input1 = 0
        Input2 = 0
        Timer = 0
    }
}
function LCDShow () {
    makerbit.showStringOnLcd1602("Input1: ", makerbit.position1602(LcdPosition1602.Pos1), 8)
    makerbit.showStringOnLcd1602("" + (Input1), makerbit.position1602(LcdPosition1602.Pos9), 1)
    makerbit.showStringOnLcd1602("Input2: ", makerbit.position1602(LcdPosition1602.Pos17), 8)
    makerbit.showStringOnLcd1602("" + (Input2), makerbit.position1602(LcdPosition1602.Pos25), 1)
}
let RadioNum = 0
let Timer = 0
let Received = 0
let Step = 0
let Input2 = 0
let Input1 = 0
let List2: number[] = []
let List1: number[] = []
radio.setGroup(1)
List1 = [
1,
2,
3,
4
]
List2 = [
1,
2,
3,
4
]
Input1 = 0
Input2 = 0
Step = 0
Received = 0
Timer = 0
makerbit.clearLcd1602()
basic.forever(function () {
    Timer += 1
    basic.pause(1000)
})
