import gym
import torch
import numpy as np
import matplotlib.pyplot as plt


def run_episode(env,parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward
    pass

def random_search():
    return np.random.rand(4) * 2 - 1

def main():
    env = gym.make('CartPole-v1')
    total_rewards = []
    num_of_trials = 10000
    best_reward = 0
    best_params = None
    counter = 0
    noise_scaling = 0.1
    parameters = np.random.rand(4) * 2 - 1;
    
    for step in range(num_of_trials):
        counter += 1   
        
        new_parameters = parameters + (np.random.rand(4) * 2 - 1) * noise_scaling
        reward = run_episode(env,new_parameters)
        total_rewards.append(reward)
        if reward > best_reward:
            best_reward = reward
            parameters = best_params = new_parameters
            if reward == 200:
                print('200 achieved on step {}'.format(step))        

    print("Average Reward after {0} consecutive trails:{1}".format(num_of_trials,sum(total_rewards)/num_of_trials))        
    print("Best Reward:{}".format(best_reward))
    print("Best Params:{}".format(best_params))
    
    plt.figure(figsize=(12,5))
    plt.title("Rewards")
    plt.bar(torch.arange(len(total_rewards)), total_rewards, alpha=0.6, color='green')
    plt.show()
    
    env.close()
    env.env.close()

    


if __name__ == "__main__":
    main()




