def on_button_pressed_a():
    music.ring_tone(262)
    soundExpression.giggle.play_until_done()
    basic.show_string("SRINIKETH")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.ring_tone(262)
    soundExpression.giggle.play_until_done()
    basic.show_string("PANEENDRA")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("SRINIKETH")
music.start_melody(music.built_in_melody(Melodies.DADADADUM),
    MelodyOptions.ONCE)
music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
    MelodyOptions.FOREVER)
input.calibrate_compass()
led.set_display_mode(DisplayMode.BLACK_AND_WHITE)
basic.show_arrow(ArrowNames.NORTH)
basic.show_arrow(ArrowNames.NORTH_EAST)
basic.show_arrow(ArrowNames.EAST)
basic.show_arrow(ArrowNames.SOUTH_EAST)
basic.show_arrow(ArrowNames.SOUTH)
basic.show_arrow(ArrowNames.SOUTH_WEST)
basic.show_arrow(ArrowNames.WEST)
basic.show_arrow(ArrowNames.NORTH_WEST)
basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.SKULL)
basic.show_icon(IconNames.GHOST)
basic.show_icon(IconNames.SQUARE)
basic.show_icon(IconNames.SMALL_SQUARE)
basic.show_icon(IconNames.SMALL_DIAMOND)
basic.show_icon(IconNames.SQUARE)
basic.show_icon(IconNames.SMALL_SQUARE)
basic.show_icon(IconNames.SMALL_DIAMOND)