"""
GCode M557 
Example: M557 P1 X30 Y40.5

Set the points at which the bed will be probed to compensate for its plane being slightly out of horizontal. The P value is the index of the point (indices start at 0) and the X and Y values are the position to move extruder 0 to to probe the bed. An implementation should allow a minimum of three points (P0, P1 and P2). This just records the point coordinates; it does not actually do the probing. See G32. 

Author: Elias Bakken
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
"""

from GCodeCommand import GCodeCommand
import logging


class M557(GCodeCommand):

    def execute(self, g):
        if g.has_letter("P"):
            index = int(g.get_value_by_letter("P"))
        else:
            logging.warning("M557: Missing P-parameter")
            return 
        if g.has_letter("X"):
            X = float(g.get_value_by_letter("X"))
        else:
            logging.warning("M557: Missing X coordinate")
            return 
        if g.has_letter("Y"):
            Y = float(g.get_value_by_letter("Y"))
        else:
            logging.warning("M557: Missing Y coordinate")
            return         
        self.printer.probe_points[index] = {"X": X, "Y": Y}

    def get_description(self):
        return "Set probe point"
