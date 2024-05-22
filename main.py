input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P0, 90)
    basic.pause(1000)
    pins.servoWritePin(AnalogPin.P0, 0)
})
makerbit.connectIrReceiver(DigitalPin.P0, IrProtocol.Keyestudio)
basic.forever(function () {
    basic.showString("" + (makerbit.irButton()))
})
basic.forever(function () {
    basic.showString("" + (makerbit.irButton()))
})
basic.forever(function () {
    if (makerbit.wasIrDataReceived()) {
        if (makerbit.irButton() == "24") {
            pins.servoWritePin(AnalogPin.P0, 90)
            basic.pause(1000)
            pins.servoWritePin(AnalogPin.P0, 180)
            basic.pause(1000)
        }
    }
})
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P3) > 100) {
        pins.digitalWritePin(DigitalPin.P12, 1)
    }
})
basic.forever(function () {
    let estado = 0
    if (input.lightLevel() < estado) {
        pins.servoWritePin(AnalogPin.P2, 90)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P2, 180)
        basic.pause(1000)
    }
})
basic.forever(function () {
    if (makerbit.wasIrDataReceived()) {
        if (makerbit.irButton() == "162") {
            pins.servoWritePin(AnalogPin.P2, 90)
            basic.pause(1000)
        }
        if (makerbit.irButton() == "34") {
            pins.servoWritePin(AnalogPin.P2, 180)
            basic.pause(1000)
        }
    }
})
