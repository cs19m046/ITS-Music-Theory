import random

# Variables
skills = ('Read key', ) 
params = ('KeyColr', )
param_values = {'KeyColr': ('White' , 'Black' , 'All')}
nskill = len(skills)
nparameter = len(params)
answer = 0

# Tables
potential_tbl = [[[200, 450, 950]]]
learning_lvl = [0]

# Learning functions
activity_pot = [0]
reward_pot = [0]

def learning_potential():
    print("\n(fn) Learning potential:")
    for n in range(nskill):
        print("--skill",n)
        q = 0
        for m in range(nparameter):
            print("----parameter", m)
            a_m = activity[m]
            q += potential_tbl[n][m][a_m]
        activity_pot[n] = int(q/nparameter)
    print("= q_activity >>", activity_pot)

def fill_rewards():
    print("\n(fn) Fill rewards")
    for n in range(nskill):
        reward_pot[n] = int(activity_pot[n] - learning_lvl[n])
    print("= q_activity - learn_lvl", reward_pot)

# Activity picking functions
activity = [0]

def greedy_pick(parameter_no):
    print("\n :: Greedy expert")
    m = max(bandit_wts[parameter_no])
    print(">>> >>>Max Bandit wt. :", m)
    pos = bandit_wts[parameter_no].index(m)
    print(">>> >>>Max bandit loc. :", pos)
    return pos

def uniform_pick(parameter_no):
    print("\n :: Exploration expert")
    p = params[parameter_no]
    q = param_values[p]
    length = len(q)
    pos = random.randint(0, length-1)
    print(">>> >>>Picking random bandit loc. :", pos)
    return pos

def pick_activity(g):
    print("\n(fn) Pick activity")
    for n in range(nparameter):
        print("Parameter >",n)
        prob = random.randrange(0,100,1)/100
        print("Probability = ",prob)
        print("Activity picked for parameter",n)
        if prob<g:
            activity[n] = uniform_pick(n)
            print("Uniform pick >>>", activity[n])
        else:
            activity[n] = greedy_pick(n)
            print("Greedy pick >>>", activity[n])
    learning_potential()
    fill_rewards()
    print("activity >> activity_pot >> reward_pot", activity, activity_pot, reward_pot)

# Bandit functions
bandit_wts = [[1, 1, 1]]
keys = {    'White':
            ['c', 'd', 'e', 'f', 'g', 'a', 'b'],

            'Black':
            ['c sharp', 'd flat','d sharp', 'e flat','f sharp', 'g flat','g sharp', 'a flat', 'a sharp', 'b flat'],

            'All':
            ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c sharp', 'd flat','d sharp', 'e flat', 'f sharp', 'g flat', 'g sharp', 'a flat', 'a sharp', 'b flat']
	}

def update_learning(answer):
    totl_reward = 0
    for n in range(nskill):
        if answer==1 and reward_pot[n]>0 or answer==-1 and reward_pot[n]<0:
            learning_lvl[n] = learning_lvl[n] + int(reward_pot[n]/10)
            totl_reward += reward_pot[n] 
    return int(totl_reward/nskill)

def update_bandit_wts(mean_reward):			
# Takes mean reward from update learning func
    for i in range(len(activity)):
        a_i = activity[i]
        bandit_wts[i][a_i] = int(bandit_wts[i][a_i] + mean_reward)
    print("\n>> >> >> New Bandit Wts:", bandit_wts)    

# Piano prompt functions
def activity_name():
    s = ''
    i = 0
    for p in params:
        q = param_values[p]
        a = activity[i]
        r = q[a]
        s += r
        i += 1
    return s

def prompt(filename):
	key_list = keys[filename]
	pos = random.randint(0, len(key_list)-1)
	print(key_list)
	return key_list[pos]
	
# Run
def runactivity():
    print("=="*30)
    print("Learning lvl:", learning_lvl)
    print("--"*30)
    print("\n(fn) Run activity")
    g = 0.25
    print('Gamma:', g)
    pick_activity(g)
    filename = activity_name()
    p = prompt(filename)
    return p

