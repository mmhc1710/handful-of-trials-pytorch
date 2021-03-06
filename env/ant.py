import gym
from multiworld.core.flat_goal_env import FlatGoalEnv


def create_ant_flat():
    env = gym.make('AntFullPositionGoal-v0')
    env.hide_goal = False
    return FlatGoalEnv(
        env,
        append_goal_to_obs=True,
    )
