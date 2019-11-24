import retro
from spinup import ppo
import tensorflow as tf
import gym


def main():


    env_fn = lambda : gym.make('LunarLander-v2')

    ac_kwargs = dict(hidden_sizes=[64,64], activation=tf.nn.relu)

    logger_kwargs = dict(output_dir='path/to/output_dir', exp_name='experiment_name')

    ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=250, logger_kwargs=logger_kwargs)

    # pass
    ######------play movie -----------------
    # movie = retro.Movie('SuperMarioBros-Nes-Level1-1-000000.bk2')
    # movie.step()

    # env = retro.make(
    #     game=movie.get_game(),
    #     state=None,
    #     # bk2s can contain any button presses, so allow everything
    #     use_restricted_actions=retro.Actions.ALL,
    #     players=movie.players,
    # )
    # env.initial_state = movie.get_state()
    # env.reset()

    # while movie.step():
    #     keys = []
    #     for p in range(movie.players):
    #         for i in range(env.num_buttons):
    #             keys.append(movie.get_key(i, p))
    #     env.step(keys)
    #     env.render()

    ##########---------main RL program--------------
    # env=retro.make(game='SuperMarioBros-Nes',record='.')
    # obv=env.reset()
    # for i in range(10000):
    #     obs,rew,done,info=env.step(env.action_space.sample())
    #     env.render()
    # env.close()


if __name__=="__main__":
    main()
