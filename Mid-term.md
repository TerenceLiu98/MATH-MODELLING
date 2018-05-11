# <center>Spring 2018 MATH4080 Case Studies in Mathematical Modeling Mid-term Projects</center>



<center>**Due Date: 13 May, 23:59**</center>

**Instruction:** Submit your answers and codes to SEPARATE links on iSpace. Late or incorrect submissions will not be graded. Each question carries the same weight.

1.( *Mixing tanks*) Two very large tanks *A* and *B* are each partially filled with 100 gallons of brine. Initially, 100 pounds of salt is dissolved in the solution in tank *A* and 50 pounds of salt is dissolved in the solution in tank *B*. The system is closed in that the well-stirred liquid is pumped only between the tanks, as shown in Figure 1.

[![1.png](https://i.loli.net/2018/05/11/5af51f6397c63.png)](https://i.loli.net/2018/05/11/5af51f6397c63.png)

 

(a)Use the information given in the figure to construct a mathematical model for the number of pounds of salt *x*1(*t*) and *x*2(*t*) at time *t* in tanks *A* and *B*, respectively.

(b)Find a relationship between the variables *x*1(*t*) and *x*2(*t*) that holds at time *t*. Explain why this relationship makes intuitive sense. Use this relationship to help find the amount of salt in tank B at *t* = 30 min.



<font color = "red">Answer:</font>

> (a) The differential equations corresponding to the given model are
>
> $\begin{align*} &\frac{dx_1}{dt} = (3 gal/min) (\frac{x_2}{100-t}lb/gal) - (2 gal/min)(\frac{x_2}{100+t}lb/gal) \\ &= \frac{3x_2}{100-t} - \frac{2x_1}{100 + t} \\ & \frac{dx_2}{dt} = (2 gal/min)(\frac{x_1}{100 + t}lb/gal) - (c gal/min)(\frac{x_2}{100-t} lb/gal) \\ &= \frac{2x_1}{100 + t} - \frac{3x_2}{100 - t} \end{align*}$ 
>
> The the system is:
>
> $\begin{align*} &\frac{dx_1}{dt} = \frac{3x_2}{100-t} - \frac{2x_1}{100 + t} \\ & \frac{dx_2}{dt} = \frac{2x_1}{100 + t} - \frac{3x_2}{100 - t} \text{ a long with the intial conditons } x_1(0) = 100, x_2(0) = 50\end{align*}$ 
>
> (b) According to the question 'The system is closed', that is to say the salt's quality will not be added or lost, we can get this equation: $x_1(t) + x_2(t) = 150$ ; at the point $ t = 30 $ we can get $ x_2 = 47.4 lb$  



---



2.( *Newton’s* *Law* *of cooling/warming*) As shown in Figure 2, a small metal bar is placed inside container *A*, and container *A* then is placed within a much larger container *B*. As the metal bar cools, the ambient temperature $T_A(t)$ of the medium within container $A$ changes according to Newton’s law of cooling. As container $A$ cools, the temperature of the medium inside container $B$ does not change significantly and can be considered to be a constant $T_B$ . Construct a mathematical model for the temperatures $T(t)$ and $T_A(t)$, where $T (t)$ is the temperature of the metal bar inside container *A*. Find a solution of the system subject to the initial conditions $T(0)$ = $T_0$ , $T_A(0)$ = $T_1$. 

(Assume here that the temperature, $T(t)$ of the metal bar does not affect the temperature, $T_A(t)$ of the medium in container *A*)

[![2.png](https://i.loli.net/2018/05/11/5af51f63b9fe0.png)](https://i.loli.net/2018/05/11/5af51f63b9fe0.png)

 

<font color = "red">Answer:</font>

> Assume that the coefficient between container B and container A is $k$ , According to the Newton Law of Cooling, we can get:
>
> The metal bar cools by conduction to container A, and loses heat at a rate proportional to the temperature difference so:
>
> $\frac{dT}{dt}=-k_1(T(t)-T_A(t))$
>
> Meanwhile container A has heat incoming from the metal bar, and is losing heat to container B, so
>
> So, 
>
> $\begin{align*} &\frac{dT_A(t)}{dt} = -k(T_A - T_B\\ &T_A- T_B = Ce^{-kt} \\ &T_A(0) -T_B = Ce^{-k0} = C \\ &T_1 = T_B = C\\ & \text{ so, } T_A(t) = (T_1 - T_B)e^{-kt} \\ &\frac{dT}{dt} = -K(T -T_A) \\ &\frac{dT}{dt} + KT = KT_A \\ &e^{Kt}\frac{dT}{dt} + KT = KT_A\\ &\frac{d(e^{K1})}{dt} = KT_Ae^{K1} \\&T = K(T_1 - T(B) \frac{e^{(K-k)t}}{(K-k)e^{Kt}} + C \\ &T(0) = T_0 \\ &C = T_0 -\frac{K(T_1-T_B)}{(K-k)} \\ &\text{We can get: } T(t) = K(T_1 -T_B) \frac{e^{(K-kt)}}{(K-k)e^{kt}} + T_o -\frac{K(T_1-T_B)}{K-k}  \end{align*}$
>
> 



---



3.( *Electoral* *system / Voting theory*) An electoral system is the system that determines how elections and referendums take place and how their results are arrived at. Different rules of voting may sometimes lead to different winner(s) even if the preferences of constituents remain the same.

Consider the following voting rules (assume only a single winner)

1.   *Plurality method*: A single round of election is held. The candidate who polls the most among their counterparts is elected.

2.   *Single runoff method*: A preliminary round of election is held and two candidates who receive the most number of votes advance to the final round. The final round is then based on the *plurality method*. The winner of the final round is chosen as the elect.

3.   *Instant runoff method*: Multiple rounds of election are held. In each round, the candidate who receive the least number of votes is eliminated. When there are only two candidates remaining, use the *plurality method* to determine the elect.

4.   *Coombs method:* Multiple rounds of election are held. In each round, the con- stituents are required to rank every candidate in terms of their preferences. The candidate who received the most number of votes for the last place is eliminated.

When there are only two candidates remaining, use the *plurality method* to determine the elect.

5.   *Borda*  *count:*  A single round of election is held.   The constituents are required    to rank every candidate in terms of their preferences. For each vote casted, the candidate in the last place gets 1 mark, the candidate in the second last place gets 2 marks, ..., the candidate in the first place gets *n* marks (*n* is the total number of candidates). The candidate who gets the highest mark is the elect.

(a)Consider the following voting results from 30 students on their favourite sports team. There are 4 teams and each student ranks them from the first (most like) and the fourth (least like). For example, 11 students vote B as the first, D as the second, C as the third and A as the fourth. Assume that the voters’ preferences do not change if multiple rounds of voting are necessary. For each voting rule above, determine the winner.

 

| Votes  | 11   | 10   | 9    |
| ------ | ---- | ---- | ---- |
| First  | B    | C    | A    |
| Second | D    | D    | D    |
| Third  | C    | A    | C    |
| Fourth | A    | B    | B    |

 

(b)Investigate the 2002 French presidential election. Which rule was used? Write a note to discuss the effect if $1\%$ of all voters for Jean-Marie Le Pen instead voted for Jacques Chirac in the first round (other votes remain unchanged - see the tables below).

You will need to get additional information on your own to draw the conclusion.

Table 1: Real result (first round)

| Candidate           | %         | Rank |
| ------------------- | --------- | ---- |
| Jacques Chirac      | $19.88\%$ | $1$  |
| Jean-Marie Le   Pen | $16.86\%$ | $2$  |
| Lionel Jospin       | $16.18\%$ | $3$  |
| .                   | .         |      |

Table 2: Hypothesised result (first round)

| Candidate         | %         | Rank |
| ----------------- | --------- | ---- |
| Jacques Chirac    | $20.88\%$ | $1$  |
| Lionel Jospin     | $16.18\%$ | $2$  |
| Jean-Marie Le Pen | $15.86\%$ | $3$  |
| .                 | .         |      |



<font color = "red">Answer:</font>

> (a) 
>
> 1. **Plurality method**: B is the winner
>
> 2. **Single runoff method**: for the first round we will get B and C; I assume that the  nine people who vote for A will vote C ( because in the first round those 9 people think C is better then B) then the result is C get 19 point and B get 11; C is the winner
>
> 3. **Instant runoff method**, First round we can  elminate A, then, we can get the second round data:
>
>    | Votes  | 11   | 10   | 9    |
>    | ------ | ---- | ---- | ---- |
>    | First  | B    | C    |      |
>    | Second | D    | D    | D    |
>    | Third  | C    |      | C    |
>    | Fourth |      | B    | B    |
>
>    we can eliminate D in the second round;
>
>    | Votes  | 11   | 10   | 9    |
>    | ------ | ---- | ---- | ---- |
>    | First  | B    | C    |      |
>    | Second |      |      |      |
>    | Third  | C    |      | C    |
>    | Fourth |      | B    | B    |
>
>    Then, when we get the third round data, we can easily get the answer: C(19) is the winner.
>
> 4. **Coombs method** In the first round, no candidate has an absolute majority of first-place votes, but B has the most last-place votes, is therefore eliminated.
>
>
>
> | Votes  | 11   | 10   | 9    |
> | ------ | ---- | ---- | ---- |
> | First  |      | C    | A    |
> | Second | D    | D    | D    |
> | Third  | C    | A    | C    |
> | Fourth | A    |      |      |
>
>    In the second round, B is out of the running , and so must be factored out. B was ranked first on First round's ballots, so the second choice of First round, D, get an additional 11 votes, but still not an absolute majority. This time, A is eliminated.
>
> | Votes  | 11   | 10   | 9    |
> | ------ | ---- | ---- | ---- |
> | First  |      | C    |      |
> | Second | D    | D    | D    |
> | Third  | C    |      | C    |
> | Fourth |      |      |      |
>
>    In the third round, D get 20 votes so D is the winner.
>
> 5. **Borda count**:
>
>    | Votes  | 11   | 10   | 9    |
>    | ------ | ---- | ---- | ---- |
>    | First  | B    | C    | A    |
>    | Second | D    | D    | D    |
>    | Third  | C    | A    | C    |
>    | Fourth | A    | B    | B    |
>
>    If we use Borda Count, the first place will get 4 points the last place will get 1 point.
>
>    | Votes | First       | Second       | Third       | Forth       | Total |
>    | ----- | ----------- | ------------ | ----------- | ----------- | ----- |
>    | A     | $1\times 4$ | 0            | $1\times 2$ | $1\times 1$ | 7     |
>    | B     | $1\times 4$ | 0            | 0           | $1\times 2$ | 6     |
>    | C     | $1\times 4$ | 0            | $1\times 2$ | 0           | 6     |
>    | D     | $0$         | $3 \times 3$ | 0           | 0           | 9     |
>
>    We can get D is the winner.
>
>    
>
> (b) I guest it is the **Single runoff method**; if $1\%$ of all voters for Jean-Marie Le Pen instead voted for Jacques Chirac in the first round, the order of the topic three will change:
>
> | Candidate         | %         | Rank    |
> | ----------------- | --------- | ------- |
> | Jacques Chirac    | $21.57\%$ | $1$     |
> | Lionel Jospin     | $16.18\%$ | $2$     |
> | Jean-Marie Le Pen | $15.17\%$ | $3$     |
> | $\dots$           | $\dots$   | $\dots$ |
>
> The Jean-Marie Le Pen would not have the chance to get in to the second round.



---

4.( *Secretary* *problem / Marriage problem*) Use simulation to demonstrate the secretary/marriage problem (refer to case study 5) with $N  = 10$ and $N = 50$ candidates,  respectively.  For   each $N$ , obtain the probability that the best candidate is chosen $p_N(k)$  for $k = 1, 2, ...N$

For each value of $k$, perform sufficient number of independent runs such that the $95\%$ confidence interval with $U_r ≤ 0.01$ is obtained for $p_N(k)$. Use your simulation results to plot a figure (see Figure $3$ as an example, the vertical error bar at each point represents confidence interval) to illustrate the relationship between $k$ an $p_N(k)$.

For more information, see: <https://en.wikipedia.org/wiki/Secretary_problem> or

<http://www.math.uah.edu/stat/urn/Secretary.html>

  [![4.png](https://i.loli.net/2018/05/11/5af51f63c054c.png)](https://i.loli.net/2018/05/11/5af51f63c054c.png)

<font color ="red">Answer</font> 



> Acorrding to this theory, assume that  we rejected the $r-1$ people and interview the after $n - r + 1$ people, if there is anyone who is better then the interviewee before, we will hire him/her. so the probebiliy of those $r-1$ is $0$ ; assume that we begin for the $r$ th, and the $k$ is who we want.
>
> the probebility of the best is:
>
> $ \begin{align*} P_r &= \sum_{k = r}^n P \text{($k$ th applicant is best and is selected) }\\ & = \sum _{k =r}^n P(\text{ $k$ th applicant is best}) P\text{($k$ th applicatn is selected | it is the best)}  \\ &= sum_{k = 4}^n \frac{1}{n} P(\text{ best of first $k  - 1$ appears before stage $r$) } \\ &= \sum_{k = r}^n \frac{1}{n} \frac{r-1}{k-1} = \frac{r-1}{n} \sum_ {k=r}^n \frac{1}{k-1}\end{align*}$
>
> because there is only one people can be called 'the best', so the probebility of the best is $\frac{1}{n}$ , whcich means: the probebility of the best is higher then others,
>
> $\begin{align*} &P_{r+1} \leq P_(r) \\ \ &frac{r}{n} \sum_{r+1}^r \frac{1}{k-1} \leq \frac{r-1}{n} \sum_r^n \frac{1}{k-1} \text{ if and only if } \sum_{r+1}^n \frac{1}{k-1} \leq 1\end{align*}$
>
> we see that the optimal rule is to select the first candidate that appears among applicants 
>
> from stage $r_1$ on, where $\begin{align*} r = min \left\{ r \geq 1: \sum_{r+1}^n \frac{1}{k-1} \leq 1\right\} \end{align*}$
>
> For $n \in N_+$:
>
> $p_n(k) = P(S_{n,k}) = \begin{cases} \frac{1}{n}, & k = 1 \\ \frac{k - 1}{n} \sum_{j=k}^n \frac{1}{j - 1},  &k \in \{2, 3, \ldots, n\} \end{cases}$
>
> I use Python to do the simulation:
>
> ```Python
> import math
> import random
> 
> NUMBER_OF_TESTS = 1000
> SIZE_OF_SAMPLE = 50
> 
> def generate_candidates(n):
> 	l = []
> 	for i in range(n):
> 		randPos = random.randint(0,len(l))
> 		l.insert(randPos, i)
> 	return l
> 
> def interview(candidates, m):
> 	n = len(candidates)
> 	assert (n > m)
> 	assert (n > 1)
> 	best_candidate = candidates[0]
> 	# find best candidate in the first m candidates
> 	for i in range(m):
> 		if (candidates[i] > best_candidate):
> 			best_candidate= candidates[i]
> 	# find a new better candidate
> 	for i in range(m, n):
> 		if (candidates[i] > best_candidate):
> 			return candidates[i]
> 	return None
> 
> def compute_best_m(n):
> 	return int(round(n/math.e))
> 
> if __name__ == "__main__":
> 	fileM = open("output_m.csv", "w")
> 	fileV = open("output_value.csv", "w")
> 	list_of_m = []
> 	for i in range(0, SIZE_OF_SAMPLE, 1):
> 		list_of_m.append(i)
> 	#list_of_m.append(compute_best_m(SIZE_OF_SAMPLE))
> 	current_best_success = 0
> 	current_best_m = 0
> 	theor_best_m = compute_best_m(SIZE_OF_SAMPLE)
> 	theor_best_success = 0
> 	for m in list_of_m:
> 		print m, "/", len(list_of_m)
> 		successCount = 0
> 		testCount = 0
> 		for i in range(NUMBER_OF_TESTS):
> 			candidates = generate_candidates(SIZE_OF_SAMPLE)
> 			bestCandidate = max(candidates)
> 			hiredGuy = interview(candidates, m)
> 			if (hiredGuy == bestCandidate):
> 				successCount += 1
> 			testCount += 1
> 		successRate = float(successCount)/testCount
> 		if (successRate > current_best_success):
> 			current_best_success = successRate
> 			current_best_m = m
> 		if (m == theor_best_m):
> 			theor_best_success = successRate
> 		fileM.write(str(m) + ",\n")
> 		fileV.write(str(successRate) + ",\n")
> 	print "theoretical value :", theor_best_m, "success:", theor_best_success, "> 1/e = ", round(1/math.e, 2)
> 	print "actual best m :", current_best_m, "success:", current_best_success
> ```
>
> 1. When the size o the sample is $50$ : 
>
>    we can get :
>
>    >  theoretical value : $18$ success: $0.354 > \frac{1}{e} =  0.3$
>    >
>    > actual best m : $14$ success: $0.404$
>
> 2. When the size of the sample is $10$:
>
>    We can get:
>
>    > theoretical value : $4$ success: $0.366 >\frac{1}{e}  =  0.37$
>    > actual best m : $3$ success: $0.406$
>
> [![success_m_graph.png](https://i.loli.net/2018/05/11/5af52141e7373.png)](https://i.loli.net/2018/05/11/5af52141e7373.png)
>
> 
>
> 

