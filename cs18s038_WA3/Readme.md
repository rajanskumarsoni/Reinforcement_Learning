CS6700 : Reinforcement Learning

Written Assignment #3

- • This is an individual assignment. Collaborations and discussions are strictly prohibited.

- • Be precise with your explanations. Unnecessary verbosity will be penalized.

- • Check the Moodle discussion forums regularly for updates regarding the assignment.

- • Please start early.

Deadline: ??- Author : Name.

- Roll Number :

- 1. (3 marks) Consider the problem of solving POMDPs using Deep Reinforcement Learn-

ing. Can you think of ways to modify the standard DQN architecture to ensure it canremember histories of states. Does the experience replay also need to be modiﬁed?Explain.

Solution: Modiﬁcation in Replay memory: Instead of keeping only currentstate and observation as one sample, we can keep for the past k states.

Modiﬁcation in DQN: No we have to use those k states to get to get the q value.It can be done in many ways.

• We can use simple autoencoder, concatenate the k states and get the com-pressed representation of the state and feed it to neural network to get q values.• We can use LSTM as well.

- 2. (4 marks) Exploration is often ameliorated by the use of counts over the various states.

For example, one could maintain a visitation count N (s), for every state and use thesame to generate an intrinsic reward (ri(s)) for visiting that state.

ri(s) = τ × 1

N (s)

However, it is intractable to maintain these counts in high-dimensional spaces, since thecount values will be zero for a large fraction of the states. Can you suggest a solution(s)to handle this scenario? How can you maintain an approximation of the counts for alarge number of states and possibly generalize to unseen states?

Solution: Since here we have to explore using given intrinsic reward .We can pa-rameterize the count. We can use neural net for input state and output count. wepass the state representation and and lets it outputs o(count) we can make target aso+1, and we can ﬁnd the loss (o + 1 − o)2 or we can assume o+1 as constant, as wehave to increase the value of o so we have to do gradient ascent.

Another approach is to use dynamic hashing techniques.

- 3. (5 marks) Suppose that the MDP deﬁned on the observation space is k-th order Markov,

i.e. remembering the last k observations is enough to predict the future. Consider usinga belief state based approach for solving this problem. For any starting state and initialbelief, the belief distribution will localize to the right state after k updates, i.e., thetrue state the agent is in will have a probability of 1 and the other states will have aprobability of 0. Is this statement true or false? Explain your answer.

Solution: This statement is false. The probability estimate of a state is a conditionalprobability. If the ﬁnal probability has to be 1, then all other probabilities shouldbe 1. Choosing some starting state with some prior distribution, this isn’t possible.- 4. (3 marks) Q-MDPs are a technique for solving the problem of behaving in POMDPs.

The behavior produced by this approximation would not be optimal. In what sense isit not optimal? Are there circumstances under which it can be optimal?

Solution: Since we solve the problem by assuming that you have access of state atthat point of time, now we are only doing heuristic for converting it an executionpolicy. So policy might not be optimal Given the uncertanity in state there mighthave better action to pick in terms of the total reward we get.

We can deﬁne an MDP, where the states are the belief states and the transitionsbetween the states is given by the computation performed to ﬁnding the belief states.Now, we can predict the next belief state, given the present belief state and the actionperformed by solving this MDP. In that case, the policies can be optimal as we aretrying to determine the original policy.

- 5. (3 marks) What are some advantages and disadvantages of A3C over DQN? What are

some potential issues that can be caused by asynchronous updates in A3C?

Page 2

Solution: DQN relied heavily on GPUs. A3C beats DQN easily, using just CPUs:A3C uses a ‘forward-view’ and n-step updates

Advantages of A3C over DQN:

• A3C is asynchronous, i.e. there are multiple agents working on the same problem.These updates make this model generalize well and also make it robust.

• Speed

• It is sample and memory eﬃcient.

• DQN relied heavily on GPUs. A3C beats DQN easily, using just CPUs

• A3C uses a ‘forward-view’ and n-step updates

Disadvantages:

• A3C doesn’t have an experience replay.

• A3C doesn’t have target network.

• Due to completely asynchronous updates, the aggregated updates will not be op-timal for multiple agents.

- 6. (6 marks) There are a variety of very eﬃcient heuristics available for solving determin-

istic travelling salesman problems. We would like to take advantage of such heuristics insolving certain classes of large scale navigational problems in stochastic domains. Theseproblems involve navigating from one well demarcated region to another. For e.g., con-sider the problem of delivering mail to the oﬃce rooms in a multi storey building.(a) (4 marks) Outline a method to achieve this, using concepts from hierarchical RL.Solution: Solution: Here, the ultimate goal is to deliver mail to the oﬃce roomsaccurately. The following are the list of things, the agent has to do to completethe process.: 1. Locate where the building is.

2. Navigating to the building location.

3. Locate the oﬃce rooms.

4. Navigate to the oﬃce rooms.

5. Locate the receiver.

6. Select the correct mail to deliver.

7. Deliver the mail

8. Exit the room.

9. Exit the multi storey building.

Lets considering solving the above problem using MaxQ. Lets assume abovesteps as subtask.Ex- - Navigation to diﬀerent level of ﬂoors, Navigating to dif-ferent oﬃce rooms, Selecting the mail to be deliver.As our main task is not thatmuch critical so if we have sub optimal policy it would be of no danger. sincewe know that each task is itself a smdp. we can deﬁne diﬀerent options at indiﬀerent task.

Page 3

Navigation to diﬀerent level of ﬂoors task can have options like Going to ﬂoor 6,going to ﬂoor 7 etc. Generally we use argmax and epsilon for selcting an option.We can deﬁne heuristic function over states or over option. we can use heuristicto select between the option.We can explore with epsilon and select the optionsusing heuristic.In this way instead of learning q values we can learn heuristicsor we can combine both heuristic and q values . In this we can modify optionframework to use heuristic.

(b) (2 marks) What problems would such an approach encounter?

Solution: Because it is heuristic not guaranteed to have optimal policy.

There is no way how to evaluate policy.

Deﬁning or ﬁnding a heuristic is also a problem.

It can be too comlplex. if we use environment speciﬁc heuristics then it wouldnot be transferable.

- 7. (6 marks) This question may require you to refer to https://link.springer.com/content/pdf/10.1007/BF00114727.pdf

paper on average reward RL. Consider the 3 state MDP shown in Figure 1. Mentionthe recurrent class for each such policies. In the average reward setting, what are thecorresponding ρπ for each such policy ? Furthermore, which of these policies are gainoptimal ?

(a) (3 marks) What are the diﬀerent deterministic uni-chain policies present ?

Solution:

1. π(A) = a1, π(B) = a1, π(C) = a2

2. π(A) = a2, π(B) = a1, π(C) = a2

3. π(A) = a3, π(B) = a1, π(C) = a2

4. π(A) = a3, π(B) = a1, π(C) = a3

5. π(A) = a2, π(B) = a1, π(C) = a3

(b) (3 marks) In the average reward setting, what are the corresponding ρπ for eachsuch policy ? Furthermore, which of these policies are gain optimal ?

Solution: Solution:

Policies are numbered according to above sequence

1. 1

Page 4

2. 0.5

3. 0

4. 1

5. 1

policy 1,4,5 are gain optimal.

- Figure 1: Notation : action(reward, transition probability). Example : a1(3, 1) refers to

- action a1 which results in a transition with reward +3 and probability 1

Page 5

![Im1](images/Im1)
