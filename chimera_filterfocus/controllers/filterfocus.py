from math import ceil

from chimera.core.callback import callback
from chimera.core.chimeraobject import ChimeraObject
from chimera.core.constants import SYSTEM_CONFIG_DEFAULT_FILENAME
from chimera.core.manager import Manager
from chimera.core.systemconfig import SystemConfig

from chimera.util.enum import Enum

# M2Control States #
State = Enum("ACTIVE", "STOP", "ERROR", "RANGE")


class FilterFocus(ChimeraObject):
    __config__ = {
        "focuser": "/Focuser/0",
        "filterwheel": "/FilterWheel/0",
        "focus_filters": "U B V R I",
        "focus_difference": "-100 0 0 0 0",  # e.g. from V to U, move -100 (IN), from U to V, move +100 (OUT)
        "chimera_config": SYSTEM_CONFIG_DEFAULT_FILENAME,
        "m2control": None
    }

    def __init__(self):
        ChimeraObject.__init__(self)

    def __start__(self):

        self.sysconfig = SystemConfig.fromFile(self['chimera_config'])

        self.localManager = Manager(self.sysconfig.chimera["host"], 9090)

        self.offsets = dict(zip(self["focus_filters"].split(), [int(x) for x in self["focus_difference"].split()]))

        @callback(self.localManager)
        def filterChange(newFilter, oldFilter):
            if newFilter == oldFilter:
                return
            if newFilter not in self.offsets or oldFilter not in self.offsets:
                return

            self.log.debug("Moved from %s to %s" % (oldFilter, newFilter))

            diff = self.offsets[newFilter] - self.offsets[oldFilter]
            if diff == 0:
                return

            if diff < 0:
                diff = int(ceil(abs(diff)))
                self.log.debug("Moving focuser %i steps IN due filter change" % diff)
                self.focuser.moveIn(diff)
            elif diff > 0:
                diff = int(ceil(abs(diff)))
                self.log.debug("Moving focuser %i steps OUT due filter change" % diff)
                self.focuser.moveOut(diff)

            if self.m2control:
                self.m2control.calibrate(save=False)

        self.filterwheel = self.getManager().getProxy(self["filterwheel"])
        self.filterwheel.filterChange += filterChange
        self.focuser = self.getManager().getProxy(self["focuser"])
        if self["m2control"] is not None:
            self.m2control = self.getManager().getProxy(self["m2control"])
        else:
            self.m2control = None
