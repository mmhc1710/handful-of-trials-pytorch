from gym.envs.registration import register
from multiworld import register_all_envs

register_all_envs()

register(
    id='Pygame2D-v0',
    entry_point='env.pygame:create_pygame_2d',
)

register(
    id='SawyerPushFlat-v0',
    entry_point='env.sawyer:create_sawyer_push_flat',
)

register(
    id='AntFlat-v0',
    entry_point='env.ant:create_ant_flat',
)

register(
    id='PygameBox2D-v0',
    entry_point='env.pygame:create_pygame_box_2d',
)

register(
    id='MBRLCartpole-v0',
    entry_point='env.cartpole:CartpoleEnv'
)

register(
    id='MBRLPusher-v0',
    entry_point='env.pusher:PusherEnv'
)

register(
    id='MBRLReacher3D-v0',
    entry_point='env.reacher:Reacher3DEnv'
)

register(
    id='MBRLHalfCheetah-v0',
    entry_point='env.half_cheetah:HalfCheetahEnv'
)