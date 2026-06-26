# Define the fade transform
transform fade_to(duration=5.0):
    alpha 0.0
    linear duration alpha 1.0

# Create a screen with the fading overlay
screen darkening_overlay(duration=5.0):
    # This adds a black rectangle that fades in
    add Solid("#000") at fade_to(duration)

screen whitening_overlay(duration=5.0):
    # This adds a black rectangle that fades in
    add Solid("#d8d0b5") at fade_to(duration)
