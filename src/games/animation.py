# File - animation.py
# Version 2
# Latest Version - Chapter 11
# Multiple-shot cannonball animation

from math import sin, cos, radians, degrees
from src.classes.graphics import *
from src.classes.projectile import Projectile


class Launcher:

    def __init__(self, win):
        """Create inital launcher with angle 45 degrees and velocity 40
        win is the GraphWin to draw the launcher in.
        """

        # draw the base shot of the launcher
        base = Circle(Point(0, 0), 3)
        base.setFill("red")
        base.setOutline("red")
        base.draw(win)

        # save the window and create initial angle and velocity
        self.win = win
        self.angle = radians(45.0)
        self.vel = 40.0

        # create inital "dummy" arrow
        self.arrow = Line(Point(0, 0), Point(0, 0)).draw(win)
        # replace it with the correct arrow
        self.redraw()

    def redraw(self):
        """undraw the arrow and draw a new one for the
        current values of angle and velocity.
        """

        self.arrow.undraw()
        pt2 = Point(self.vel * cos(self.angle), self.vel * sin(self.angle))
        self.arrow = Line(Point(0, 0), pt2).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

    def adj_angle(self, amt):
        """change angle by amt degrees"""

        self.angle = self.angle + radians(amt)
        self.redraw()

    def adj_vel(self, amt):
        """change velocity by amt"""

        self.vel = self.vel + amt
        self.redraw()

    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)


class ShotTracker:
    """Graphical depiction of a projectile flight using a Circle"""

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot, angle, velocity, and
        height are initial projectile parameters.
        """

        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""

        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.get_x() - center.getX()
        dy = self.proj.get_y() - center.getY()
        self.marker.move(dx, dy)

    def get_x(self):
        """return the current x coordinate of the shot's center"""
        return self.proj.get_x()

    def get_y(self):
        """return the current y coordinate of the shot's center"""
        return self.proj.get_y()

    def undraw(self):
        """undraw the shot"""
        self.marker.undraw()


class ProjectileApp:

    def __init__(self):
        self.win = GraphWin("Projectile Animation", 640, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10, 0), Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)

        self.launcher = Launcher(self.win)
        self.shots = []

    def update_shots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and shot.getX() < 210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive

    def run(self):

        # main event/animation lopp
        while True:
            self.update_shots(1 / 30)

            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break

            if key == "Up":
                self.launcher.adj_angle(5)
            elif key == "Down":
                self.launcher.adj_angle(-5)
            elif key == "Right":
                self.launcher.adj_vel(5)
            elif key == "Left":
                self.launcher.adj_vel(-5)
            elif key == "f":
                self.shots.append(self.launcher.fire())

            update(30)

        self.win.close()


if __name__ == "__main__":
    ProjectileApp().run()
