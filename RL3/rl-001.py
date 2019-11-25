import retro
def main():
    pass
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

    #########---------main RL program--------------
    env=retro.make(game='SuperMarioBros-Nes',record='.')
    obv=env.reset()
    for i in range(10000):
        obs,rew,done,info=env.step(env.action_space.sample())
        env.render()
    env.close()


if __name__=="__main__":
    main()
