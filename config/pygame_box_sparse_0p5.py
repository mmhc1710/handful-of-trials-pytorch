from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from config.pygame_base import PygameBoxWallsConfigModule


class PygameBoxSparseConfigModule(PygameBoxWallsConfigModule):
    @staticmethod
    def obs_cost_fn(obs):
        positions = obs[:, :2]
        goals = obs[:, 2:]
        deltas = (positions - goals)
        distances = (deltas ** 2).sum(dim=1).sqrt()
        return (distances >= 0.5).type(obs.dtype)


CONFIG_MODULE = PygameBoxSparseConfigModule
