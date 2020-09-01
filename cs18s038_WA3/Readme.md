Indian Institute of Technology, Madras

CS6700: Reinforcement Learning

Reinforcement Learning Assignment-I Report

Rajan Kumar Soni - CS18S038

January 2020

- Contents

- 1 Implementation of (cid:15)-greedy and related plots

- 1.1 Related plots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

- 1.2

Inference from Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .- 2 Implementation of soft-max algorithm and related plots

- 2.1 Related plots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

- 2.2

Inference from Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .- 3 Implementation of UCB1 algorithm and comparing with (cid:15)-greedy and soft-max

- and related plots

- 3.1 Related plots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

- 3.2

Inference from Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .- 4 Implementation of Median algorithm and comparing with (cid:15)-greedy, soft-max

- and UCB1 and related plots

- 4.1 Related plots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

- 4.2

Inference from Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .- 5 Comparison of the above four algorithm as the number of arm grows

- 5.1 Related plots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

- 5.2

Inference from Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13- 6 References

Implementation of (cid:15)-greedy and related plots

- 1.1 Related plots

(a) Average reward per step

(b) percent Optimal action per step

![Im1](images/Im1)

![Im2](images/Im2)

- 1.2

Inference from Observation

- Referring to the ﬁgure (a) and (b) above:

- • I have plotted the curve for diﬀerent values of (cid:15) = 0.0 , .1, .01 and decaying epsilon .Above

plots are averages over 2000 runs with diﬀerent bandit problems

- • For (cid:15) = 0 , we are fully greedy towards best action at that moment, So not wasting any time

for exploration. The greedy method improved slightly faster than the other methods at thevery beginning, but then leveled oﬀ at a lower level. It achieved a reward-per-step of onlyabout 1, compared with the best possible of about 1.5 on this test-bed. It performs bad inlong run as it got stuck in performing sub optimal action.Although it is good for stationarydistribution with reward variance is zero.

- • For (cid:15) = .01, As it chooses the optimal action at that moment with .991 probability. As it

grows slow then greedy because it is also exploring to ﬁnd the optimal action. Although if itﬁnds the optimal action still it is exploring with probability .009.

- • For (cid:15) = .1, As it grows faster then (cid:15) =.01 and slower then greedy because it explores more

then (cid:15) =.01 so it found faster optimal action. found the optimal action earlier, but it neverselected that action more than 91% of the time. It is good if we have less number of stepsand high variance in rewards.

- • For (cid:15) = 0, the greedy method found the optimal action in only approximately one-third of the

tasks. In the other two-thirds, its initial samples of the optimal action were disappointing,and it never returned to it.

- • While the other two plot , keep exploring so founding of optimal action keep on increasing,

but the still not be able to pick 100% optimal action because they will still be exploring.- • For variable (cid:15)0.1 − .0001, As we can see in the ﬁgure, It is better then all others because it is

keep decreasing or dcaying exploration part. In the start it focuses more on exploration butas the time passes exploration keep decreasing so % optimal action keep on incresing.Implementation of soft-max algorithm and related plots

- 2.1 Related plots

(a) Average reward per step

(b) percent Optimal action per step

![Im3](images/Im3)

![Im4](images/Im4)

- 2.2

Inference from Observation

- Referring to the ﬁgure (a) and (b) above:

- • We can see plots for diﬀerent values of temperature .001, .005, .01, .05 , .1, .5. Here

soft-max algorithms selects an arm using Gibbs Distribution.

- • In this algorithm, temperature parameter controls the distribution of the actions.

- • for temperature close to 0, in above plot When t = .001 or t = .005. The arm having high

estimate will have very high probability and others will get get approx zero probability.Wecan see it is behaving like greedy one.

- • And as t tends to inﬁnity, the algorithms picks arms uniformly at random; what ever mean

estimate for each arm you have, all arms value will become close to zero. Since our rewardsare taken from standard normal distribution, so when t = 1, it will pick arms uniformly atrandom, hence will perform poorly as it will not be pulling optimal arm more times.

- • We can observe from the above plot for temperature values near to zero it performs mostly

exploitation, for 0 <=temperature <= 1 we can tune it for like (cid:15)-greedy by balancing theexploit and explore dilemma but for temperature > 1 it started to behave randomly at everystep it chose action uniformly.At temperature = inﬁnity updating the action reward estimatedoes not eﬀect the probability distribution of actions

- • In above graph, For temperature = 100 soft-max action selection becomes proper random

and because rewards means and reward itself coming from Gaussian distribution, so we cansee only 10% optimal action chosen.

Implementation of UCB1 algorithm and comparing with (cid:15)-greedyand soft-max and related plots

- 3.1 Related plots

(a) Average reward per step

(b) percent Optimal action per step

![Im5](images/Im5)

![Im6](images/Im6)

- 3.2

Inference from Observation

- Referring to the ﬁgure (a) and (b) above:

(cid:113) ln(t)

c

Nt(a ].

- • Formula used for Updating the mean estimate for every arm at time t: At = argmax[Qt(a) +

- • UCB1 algorithm is a simpler, more elegant implementation of the idea of optimism in the

face of uncertainty. It uses the fact that there is always uncertainty about the accuracy of theaction- value estimates, hence exploration is needed. Thus it would be to better to select nonoptimal arms according to their potential for actually being optimal, by taking into accountboth how close their mean estimates are to being maximal and the uncertainties in thoseestimates.

- • c > 0 controls the degree of exploration.The idea of this upper conﬁdence bound (UCB)

action selection is that the square-root term is a measure of the uncertainty or variance inthe estimate of a’s value. The quantity being max’ed over is thus a sort of upper bound onthe possible true value of action a,with c determining the conﬁdence level. Each time a isselected the uncertainty is presumably reduced: Nt(a) increments, and, as it appears in thedenominator, the uncertainty term decreases. On the other hand, each time an action otherthan a is selected, t increases but Nt(a) does not; because t appears in the numerator, theuncertainty estimate increases.

- • UCB1 guarantees that all arm will be selected and as the time passes arms having higher

estimate will be selected more and the arms having lower estimates selected less.

Refering to ﬁgure (a) and (b)

- • We can see on initial steps UCB1 more focused on exploration after that as its starts focusing

the arms having high estimate conﬁdence interval.UCB1 is self balancing because there is noparameter required to tune exploration although we can control the degree of exploration ,while in the case of softmax and (cid:15)-greedy exploration is at constant rate.

Implementation of Median algorithm and comparing with (cid:15)-greedy, soft-max and UCB1 and related plots

- 4.1 Related plots

- for delta = .1

- (a) Total number of samples vs epsilon for median Elimination

(b) percent Optimal retained vs epsilon for median Elimination(c) Average reward per step for median Elimination

(d) % optimal action per step for median Elimination- for delta = .05

- 4.2

Inference from Observation

- • The Median Elimination algorithm is an ((cid:15), δ)-PAC algorithm. In every round it eliminates

half of the bad arms, thus in log(k) steps it will return an arm within range of optimal armwith at least (1 δ) probability.

- • The sample complexity of the Median Elimination is O(k log( 3

δ )/(cid:15)2), where k is the numberof arms

- • From the above results we can see that as the epsilon and delta is decreasing Number of

samples required to satisfy ((cid:15), δ)-PAC also increasing. For given delta as the epsilon value![Im7](images/Im7)

![Im8](images/Im8)

![Im9](images/Im9)

![Im10](images/Im10)

![Im11](images/Im11)

![Im12](images/Im12)

- (a) Total number of samples vs epsilon for median Elimination

(b) percent Optimal action retained vs epsilon for median Elim-ination

(c) Average reward per step for median Elimination

(d) percent Optimal action retained per step for median Elim-ination

is decreasing percentage of optimal arm retained also got increased and for that number ofsample also got increased.

Observation for diﬀerent values of (cid:15) and δ

(cid:15)

.05

.08

.1

.3

.5

.05

.08

.1

.3

.5

δ

.1

.1

.1

.1

.1

.05

.05

.05

.05

.05

Total number of

samples

% optimal arm re-

tained

99.8

99.75

99.75

99.6

99.2

99.85

99.9

99.6

99.4

99.1

- • Also, we can observe that % optimal arm retained is relatively little less when (cid:15) is large,

because since we are taking less samples probability of eliminating optimal arm is more since(cid:15) is large. For example for (cid:15) = 0.05 δ = 0.05, total samples taken is 2582629 and percentage![Im13](images/Im13)

![Im14](images/Im14)

optimal arm retained is 99.85 while on other hand when error is allowed greater then .05 butless then .5 percentage optimal arm retained is 99.1. This is because in ﬁrst case we weremore restricted that is it took more sample and result got improved. Similar trend we can seekeeping epsilon value constant for delta = .1 and delta = .05, as we want more conﬁdence sonumber of samples increases and because samples increases in such amount that percentageoptimal arm retained also increases.

- • Thus, with these empirical observation, we can conclude that Median elimination algorithm

is indeed ((cid:15), δ)-PAC algorithm with sample complexity of O(k log( 3

δ )/(cid:15)2).

- • If we talk about the complexity of calculating Median. If we use sort algorithm it would be

O(k log(k) where k is the number of arms. We can use Deterministic linear time median-of-medians algorithm or randomized Monte Carlo for O(k) complexity.

- • we can see from the graph regret is maximum for Median Elimination for high bouning error

.9 and low conﬁdence .1. So for limited number of time steps me Median Elimination is notgood.

- Is ﬁnding median the rate-determining-step ?

- As we know in median elimination algorithm we can divide the algorithm in two parts sampling

- and ﬁnding median.We know that sampling complexity depend on epsilon and delta, it also depends

- on the type of distribution rewards while ﬁnding median complexity depends on number of arms.

- From the below table we can observe that,for given value of epsilon, delta as the number of arm

- increases ,rate of increases of Time taken by algorithm is more then rate of increase of Total time

- taken by ﬁnding median. So from here we conclude is not the rate determining step. But as the

- arm grows ratio (Time taken by algorithm)/(Total time taken by ﬁnding median) decreases. From

- here we can say that for small number of arms it is not rate determining but for large number of

- arms it an be.

(cid:15)

.05

.08

.1

.3

.5

.05

.08

.1

.3

.5

Observation for rate determining step(time interval in second)

number of armsδ

.05

.05

.05

.05

.05

.05

.05

.05

.05

.05

Time taken by al-

gorithm

0.126398

0.047517

0.0300

0.003837

0.00163 4.406e-05

23.202

9.112599

5.9413

0.696

0.268846

Total time taken

by ﬁnding median

0.000162

0.00012

0.000132

6.1e-05

0.0011

0.0012

0.0010

0.00093

0.00085

- Compare MEA with other algorithm ?

- MEA is an action elimina- tion algorithm which gaurentees ((cid:15), δ)-PAC, on other hand (cid:15)-greedy,

- Softmax and UCB1 are algorithm who selects arm..

- If the number of time steps is very large, then we can ﬁrst use MEA to ﬁnd out optimal arm

- with ((cid:15), δ)-PAC and pull that arm for remaining time steps, but if time steps are less than the

- sample complexity of MEA for ((cid:15), δ)-PAC, then we would do better using action selection algorithm

- like UCB1. We can see from the graph above in 1000 steps UCB1is selection optimal arm about

- 90% but Median elimination take more than 3000 steps even for very bad PAC Bound condition.

- We could also use both at the same time ,action elimination and action selection algorithm,

- when the number of arms is very large like 100000 or 10000000, in these case we can use Median

- elimination algorithm for ﬁrst few number of steps eliminate the big number of bad arms as it

- will remove half of the arms in every round, then use action elimination UCB1 algorithm on the

- remaining arms for the remaining time steps.

- 5 Comparison of the above four algorithm as the number of arm

grows

- 5.1 Related plots

(a) Average reward per step for 10 arm

(b) Average reward per step for 10 arm(c) percent Optimal action per step for 1000 arm

(d) percent Optimal action per step for 1000 arm- 5.2

Inference from Observation

- • Here we are Comparing the average performance of UCB1, Softmax and (cid:15)−greedy algorithm

on the 10 armed testbed and 1000-armed testbed over 2000 diﬀerent bandit problems for timesteps 1000 and 10000 repectively.

- • Thus, we run all three algorithms for 10000 100000 time steps. From the above graph We

observe that Softmax and epsilon greedy algorithm performs better in initial steps. As weknow that tuning the temperature parameter we can make softmax to behave like epsilongreedy.So we can compare only Softmax and UCB1. As in the case of Softmax, it will try topull arm which highest mean estimates with more probability and explore other arms withless probability. But UCB1 does not perform well in intial steps as it will do more explorationselects arms randomly which are not pulled enough time (Nt(a) is low) and who’s variance ishigh.

![Im5](images/Im5)

![Im15](images/Im15)

![Im6](images/Im6)

![Im16](images/Im16)

Figure 1: Comparison between 10 arm and 1000 arm performance for Median Elimination(a) Average reward per step for 10 arms

(b) Average reward per step for 1000 arms(c) percent Optimal action per step for 10 arms

(d) percent Optimal action per step for 1000 arms- • UCB1 explores more in initial time steps.In above graph Spike can be seen in UCB1,WE can

see in case of UCB1, As I have initialised all expected reward to zero.At t=1, it ﬁrst randomlyselect actio a. It N1(a) got incresed by 1 c

Nt(a ] and numerator ’t’ also got increased makingits variance reduced but for other arms only numerator got increased making their variancehigher , so in nest time step some other arm got selected having high variance. That is whywe see a jump in Average reward after 10th step in case of 10 arm and after 1000th step incase of 1000 arm.

(cid:113) ln(t)

- • Now, we run Median Elimination algorithm for 1000 armed-bandit case. And similar to

earlier case when epsilon is large, total samples required would be comparitively less andwhen epsilon is small more total samples would be required to achieve ((cid:15), δ)-PAC.

- • As we can see from above graph as we increase number of arms for given alpha and delta

regret also increases for Median Elimination.

- • But now as number of arms are 1000 it’s sample complexity would also be increase by 100x

compared to earlier case when there we 10 arms, which can be observed from below table andgraphs.

- • From above discussion we concluded that Median Elimination has maximum regret.

![Im18](images/Im18)

![Im17](images/Im17)

![Im19](images/Im19)

![Im20](images/Im20)

- Figure 2: Comparison between 10 arm and 1000 arm for Median Elimination for given δ = .05

(a) Total number of samples vs epsilon for 10 arms

(b) Total number of samples vs epsilon for 1000 arms- (c) percent Optimal retained action vs epsilon for 10 arms

(d) percent Optimal retained action vs epsilon for 1000 arms(cid:15)

.05

.08

.1

.3

.5

.05

.08

.1

.3

.5

δ

.05

.05

.05

.05

.05

.05

.05

.05

.05

.05

Observation for diﬀerent values of (cid:15) and δ

opti-

number

arms

arm

of

Total num-

ber of sam-

ples

%

mal

retained

Time takenby

algo-rithm

timeby99.7

99.3

99.7

98.4

97.3

99.6

99.4

99.5

98.4

97.8

2.07

.799

.52

.057

.02

205.2

79.12

51.2

5.56

2.12

Totaltakenﬁndingmedian.00014.00015.00014.000075.000070.00098.00099.00090.0007.00099- • As we can see from the above table Time taken by the whole algorithm is much more than

the time taken by median ﬁnding. Still here sample complexity is dominating here. But armsmuch much bigger median ﬁnding might dominate.

![Im11](images/Im11)

![Im21](images/Im21)

![Im12](images/Im12)

![Im8](images/Im8)

- 6 References

- 1 http://jmlr.csail.mit.edu/papers/volume7/evendar06a/evendar06a.pdf

- 2 https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf
