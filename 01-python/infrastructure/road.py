def draw_road(length=10, axis="horizontal"):
    # TODO: implement some variable checks
    VALID = ["horizontal", "vertical"]
    if axis not in VALID:
        # raise error
        raise ValueError("your axis is undefined")
    if axis == "horizontal":
        return draw_road_horizontal(length)
    else:
        for i in range(length):
            print("||")
    print()
    return


def draw_road_horizontal(length):
    for i in range(length):
        print("=", end="")
    return
