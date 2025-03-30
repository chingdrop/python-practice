# File - cball.py
# Version 4
# Latest Version - Chapter 10

from src.classes.projectile import Projectile


def get_inputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def main():
    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)
    while cball.get_y() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.get_x()))


if __name__ == "__main__":
    main()
