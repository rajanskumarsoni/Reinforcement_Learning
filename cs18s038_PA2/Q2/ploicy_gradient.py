#!/usr/bin/env python

import click
import numpy as np
import gym
import matplotlib.pyplot as plt


# from chakra import chakra
# env = gym.make('chakra-v0')
# exit(1)
def include_bias(ob):
    p  = ob.tolist()
    g =list(p)
    g.append(1)
    return g

def update_theta(theta, lr, grad):
    # print("theta", theta.shape, "grad", grad.shape, grad)
    theta -= lr*grad
    # print("theta", theta)
    return theta

def update_beta(beta, lr, current_state, next_state, reward, gamma):
    
    ob_1 = include_bias(current_state)
    ob_2 = include_bias(next_state)
    # print("wedwe", reward)
    s = reward + gamma*(beta.dot(ob_2))-beta.dot(ob_1)
    # print("s",s)
    p = 2*(s)*(np.array(ob_1))
    
    beta += lr*p
    # print("beta", beta)
    return beta

def log_policy_derivative(theta, state, action):
    ob_1 = include_bias(state)
    # print("ob_1",np.array(ob_1))
    p = np.matrix(action - theta.dot(ob_1)).T
    # print("p",np.array(p).shape)
    q = np.array(ob_1)[np.newaxis]
    # print("q",np.array(q))
    p = p.dot(q)
    return p


def chakra_get_action(theta, state, rng=np.random):
    ob_1 = include_bias(state)
    mean = theta.dot(ob_1)
    #r = rng.normal(loc=mean, scale=1.)
    r = rng.normal(loc=mean,scale=1.)
    
    return r		 

@click.command()
@click.argument("env_id", type=str, default="chakra")
def main(env_id):
    # Register the environment
    rng = np.random.RandomState(1)

    if env_id == 'chakra':
        from rlpa2 import chakra
        env = gym.make('chakra-v0')
        get_action = chakra_get_action
        obs_dim = env.observation_space.shape[0]
        action_dim = env.action_space.shape[0]
    else:
        raise ValueError(
            "Unsupported environment: must be 'chakra' ")

    env.seed(2)

    # Initialize parameters
    theta = rng.normal(scale=0.01, size=(action_dim, obs_dim + 1))
    beta = rng.normal(scale=0.01, size=(action_dim +1))
    episode_length = 100
    iterations = 100
    batch_size = 1000
    gamma = 0.99
    lr_theta = .05
    lr_beta = .5
    average_episode_length = []
    average_reward = []
    for i in range(iterations):

        grad_sum = 0

        
        batch_average_reward = []
        batch_average_episode_lenth = []
        for j in range(batch_size):
            current_state = env.reset()
            log_probability = []
            store_states = []
            rewards = np.zeros(episode_length)
            for k in range(episode_length):
                # print("k",k)
                
                action = get_action(theta, current_state, rng=rng)
                next_state, reward, decision, _ = env.step(action)
                rewards[k] = reward
                
                #env.render()
                der = log_policy_derivative(theta, current_state, action)
                log_probability.append(der)
                beta = update_beta(beta, lr_beta, current_state, next_state, reward, gamma)

                # print("bro",goal,next_state)
                store_states.append(current_state)
                if decision :
                    # print("fuck",decision)

                    break
                current_state = next_state
            # print("erfeferfreferfe",len(rewards))
            #print(len(log_probability))
            batch_average_reward.append(sum(rewards))
            batch_average_episode_lenth.append(len(log_probability))
            returns = 0
            
            for k in np.sort(range(len(log_probability)))[::-1]:
                #print("returns", returns)

                returns = rewards[k] + gamma*returns
                # beta += lr_beta*(returns-include_bias(store_states[k]))*np.array(include_bias(store_states[k]))
                
                grad_sum += (gamma**k)*log_probability[k]*(returns - beta.dot(include_bias(store_states[k])))
  
        grad_sum = grad_sum/(np.linalg.norm(grad_sum) + 1e-8)
            
        average_episode_length.append(batch_average_episode_lenth)
        average_reward.append(batch_average_reward)
        # print("erfeferfref3234erfe",len(np.mean(batch_average_reward, 0)))

        theta = update_theta(theta, lr_theta, grad_sum)
        print("iteration", i, "episode_length", episode_length)
        print("theta", theta)
        print("theta", beta)

        # print(len(np.mean(average_reward,1)))
    plt.plot(np.arange(batch_size)   , np.mean(average_episode_length,0))
    plt.xlabel("episode")
    plt.ylabel("average_episode_length")
    plt.show()
    plt.close()
    plt.plot(np.arange(batch_size), np.mean(average_reward,0))
    plt.xlabel("episode")
    plt.ylabel("average_reward")
    plt.show()
    plt.close()
    np.save('theta', theta)
    np.save('beta',beta)








    # while True:
    #     ob = env.reset()
    #     done = False
    #     # Only render the first trajectory
    #     # Collect a new trajectory
    #     rewards = []
    #     while not done:
    #         action = get_action(theta, ob, rng=rng)
    #         next_ob, rew, _, _ = env.step(action)
    #         ob = next_ob
    #         env.render()
    #         rewards.append(rew)

    #     print("Episode reward: %.2f" % np.sum(rewards))

if __name__ == "__main__":
    main()
