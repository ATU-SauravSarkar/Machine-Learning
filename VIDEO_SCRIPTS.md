# Video Scripts – ML Assignment 2

Each script is about **270 words**, which takes **about 1 min 50 s** at a normal speaking pace. That leaves some spare time under the 2-minute limit.

**Setup for every video:** have your webcam in a corner of the screen and the notebook open, with all cells already run. Scroll to each section as the **[SCREEN]** cue says.

**Tip:** the brief says *"you must not read from a script"*. Learn the **cue card** at the end of each script, and use the full wording only for practice. If you forget a word, use the cue card's key points and say it your own way. That sounds natural, and it shows you understand the algorithm.

---

## Video 1 – Polynomial Regression (Car fuel economy)

**[SCREEN: title + scatter plot]** *(0:00–0:20)*

"Hi, in this video I'm going to explain polynomial regression. My dataset is the Auto MPG dataset: about 400 real cars from the 1970s and 80s. I'm trying to predict a car's fuel economy, in miles per gallon, from its horsepower. As you can see in this scatter plot, the relationship isn't a straight line. MPG drops quickly at first, then flattens out."

**[SCREEN: "How Polynomial Regression works" cell]** *(0:20–0:50)*

"Normal linear regression fits a straight line: y equals b-nought plus b-one x. Polynomial regression adds powers of x, like x-squared and x-cubed, as extra inputs. The model is still fitted with least squares, so it chooses the coefficients that minimise the squared error. But because of those extra powers, the line can now bend. The degree controls how much it can bend."

**[SCREEN: degree 1 vs degree 2 plot]** *(0:50–1:10)*

"I split the data into 75% training and 25% test. The straight line underfits and misses the curve, with a test R-squared of about 0.57. A degree-2 curve follows the shape much better. R-squared goes up to 0.66, and the average error falls from 3.8 to 3.2 miles per gallon."

**[SCREEN: R² vs degree chart, then degree-15 plot]** *(1:10–1:40)*

"Then I tested degrees 1 to 15. Training accuracy keeps going up, because a more flexible curve can always fit the training points better. But test accuracy barely improves after degree 2, and at degree 15 the curve starts wiggling at the edges. That's overfitting: it's learning noise instead of the real pattern."

**[SCREEN: final equation + predictions]** *(1:40–1:55)*

"So I chose degree 2, the simplest model that captures the curve. For example, it predicts a 100 horsepower car does about 23 miles per gallon. The main lesson is to choose the degree using test data, not training data. Thanks for watching."

> **Cue card:** real cars, horsepower → mpg, curved · adds x², x³, still least squares, degree = bendiness · line R² 0.57 → quadratic 0.66 · train always ↑, test flat, degree 15 wiggles = overfit · pick degree 2, 100 hp ≈ 23 mpg, use test data

---

## Video 2 – K-Nearest Neighbours (Wheat varieties)

**[SCREEN: title + scatter chart]** *(0:00–0:20)*

"Hi, this video is about K-Nearest Neighbours. I'm using the Seeds dataset: 210 real wheat kernels from three varieties, Kama, Rosa and Canadian. I use two measurements, kernel length and groove length. On this chart, most Rosa kernels sit apart, while Kama and Canadian touch."

**[SCREEN: "How does KNN work?" cell]** *(0:20–0:50)*

"KNN is unusual because it doesn't really train. It just stores all the labelled examples. To identify a new kernel, it calculates the distance to every stored kernel, takes the K closest ones, and those neighbours vote. The most common variety is the prediction. Because it's all about distance, the measurements must be on a similar scale. Here both are in millimetres, so that's fine."

**[SCREEN: Step 4 chart + vote table]** *(0:50–1:10)*

"Here's the algorithm in action, with 5 neighbours. The star is a new kernel, and the black circles are its 5 closest kernels. The vote is 4 Kama to 1 Canadian, so KNN guesses Kama. The Canadian vote is there because this kernel sits where the two varieties meet."

**[SCREEN: K chart]** *(1:10–1:35)*

"To choose K, I used 5-fold cross-validation on the practice data only. K equals 1 scores 93%, because one unusual neighbour can flip the answer. That's overfitting. From K equals 17, the score drops to about 89%, because the vote includes kernels that aren't really similar. That's underfitting. The best was K equals 7, at 94.9%."

**[SCREEN: Step 6 results table]** *(1:35–1:55)*

"On unseen kernels it gets 50 out of 53 right, which is 94.3%. Every Rosa and Canadian kernel was correct. All 3 mistakes were Kama guessed as Canadian, the two varieties that touch on the chart. Thanks for watching."

> **Cue card:** 210 kernels, 3 varieties, kernel + groove length · no training, distance, K closest vote, both in mm · star example: 4 Kama, 1 Canadian → Kama · cross-validation, K=1 overfits, K≥17 underfits, best K=7 at 94.9% · 50/53 = 94.3%, 3 mistakes all Kama → Canadian

---

## Video 3 – Decision Tree (Penguin species)

**[SCREEN: title + pair plot]** *(0:00–0:20)*

"Hi, in this video I'll explain decision trees. I'm using the Palmer Penguins dataset: real measurements of 333 penguins from Antarctica, from three species, Adelie, Chinstrap and Gentoo. The features are bill length, bill depth, flipper length and body mass. In this plot you can already see that Gentoos have much longer flippers."

**[SCREEN: "How a Decision Tree works" cell]** *(0:20–0:50)*

"A decision tree is basically a flowchart of yes/no questions. To build it, the algorithm tries every feature and every threshold, and picks the split that makes the two groups as pure as possible. It measures purity with Gini impurity, which is zero when a group is all one species. Then it repeats on each group until the groups are pure or it hits a depth limit."

**[SCREEN: depth comparison table]** *(0:50–1:10)*

"If you don't limit it, the tree gets 100% on the training data by adding extra leaves for a few unusual penguins. That's overfitting. Cross-validation shows it doesn't help on new data, so I limited the depth to 3. That gives a small tree I can actually read."

**[SCREEN: tree diagram – point at each split]** *(1:10–1:40)*

"The first question is: is the flipper length 207 millimetres or less? That separates almost all the Gentoos in one step, which is why it's chosen first. On the short-flipper side, bill length splits Adelie, with short bills, from Chinstrap, with long bills. On the other side, bill depth picks out the Gentoos. The tree found the same rules we saw in the plot without being told."

**[SCREEN: confusion matrix + new penguins]** *(1:40–1:55)*

"On unseen penguins it's 95% accurate. The few mistakes are between Adelie and Chinstrap, which look similar. For example, a penguin with a 217 millimetre flipper and a thin bill goes right, then left, and comes out as a Gentoo. Thanks for watching."

> **Cue card:** 333 penguins, 3 species, 4 measurements · flowchart, best split = purest groups, Gini, repeat · no limit = 100% train = overfit → depth 3 · flipper ≤ 207 → Gentoo out; bill length = Adelie vs Chinstrap; bill depth · 95%, errors Adelie/Chinstrap, trace one penguin

---

## Recording checklist
- [ ] Face visible the whole time (the brief requires it)
- [ ] Notebook already run, zoomed so the text is readable
- [ ] Time a practice run and keep it under 2:00
- [ ] Save three separate video files, e.g. `YourName_A_PolynomialRegression.mp4`
