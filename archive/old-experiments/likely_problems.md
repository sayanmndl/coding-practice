I’m preparing for the **LinkedIn Senior AI Engineer full-loop AI Coding round**.

I already reviewed LinkedIn’s onsite prep guide. The AI Coding round is described as testing **mathematical foundations, algorithmic problem-solving, and implementation skills for AI-related problems**, including probability, statistics, linear algebra, optimization, feature engineering, sampling, decision trees, neural-network fundamentals, and distributed-computing concepts. The problems are expected to be relatively compact implementations, followed by reasoning, tradeoffs, optimization, and follow-up questions.

I want to prepare this as an **interview coding problem bank**, not as a textbook.

## What I have already finished

I already completed the sampling section:

* Weighted random sampling using prefix sums + binary search
* Rejection sampling
* `rand7() -> rand10()`
* General `randM() -> randN()`
* `rand3() -> rand10()`
* Reservoir sampling
* Sampling without replacement / Fisher–Yates

Do not repeat these unless I explicitly ask.

## How to teach each problem

Go **one problem at a time**.

For every problem, use exactly this structure:

1. **Short concept explanation** — 2–5 sentences, enough to understand the idea
2. **Full realistic interview question**
3. **Derivation / intuition** — explain how I should arrive at the solution
4. **Clean Python solution from scratch**
5. **Walk through a small example**
6. **Time and space complexity**
7. **Why it works / mathematical proof**, when relevant
8. **Likely interviewer follow-ups and extensions**
9. **What I should say aloud while solving it in the interview**

Keep the implementation realistic for a **1-hour AI Coding interview**. Prefer concise Python and avoid unnecessary framework boilerplate.

If there are multiple implementations, first teach the simplest interview-worthy solution, then mention optimizations as follow-ups.

Also point out common traps that could cause a rejection.

---

# Problem bank

Work through these roughly in this priority order.

## A. Core ML + optimization — highest priority

1. **Median minimizes L1; mean minimizes L2**

   * Find the point minimizing sum of absolute distances
   * Find the point minimizing sum of squared distances
   * Derive why median vs mean is optimal

2. **KNN from scratch**

   * Classification
   * Distance calculation
   * Majority voting
   * Tie handling
   * Follow-up: normalization, KD-tree / ANN

3. **K-Means from scratch**

   * Assignment step
   * Centroid update
   * Convergence
   * Empty clusters
   * Follow-up: k-means++

4. **Logistic regression from scratch**

   * Sigmoid
   * Binary cross-entropy
   * Gradient derivation
   * Gradient descent
   * Regularization

5. **Linear regression**

   * MSE
   * Gradient descent
   * Closed-form solution
   * When to use each

6. **Decision-tree best split using Gini impurity**

   * Evaluate thresholds
   * Weighted impurity
   * Find best split

7. **Decision-tree best split using entropy / information gain**

8. **Stable softmax + cross-entropy**

   * Numerical stability
   * Subtract max
   * Gradient intuition

9. **Naive Bayes from scratch**

   * Prior
   * Likelihood
   * Laplace smoothing
   * Log probabilities

10. **Numerical gradient / gradient checking**

    * Finite differences
    * Compare analytical vs numerical gradient

11. **Single neural-network layer**

    * Forward pass
    * Activation
    * Backward pass
    * Matrix dimensions

12. **Two-layer MLP from scratch**

    * Forward
    * Loss
    * Backprop
    * Parameter update

---

# B. NLP / sequence algorithms — high priority

13. **Greedy decoding**

    * Given token probabilities at each step, generate the sequence greedily
    * Explain why greedy is not globally optimal

14. **Beam search**

    * Implement beam search for sequence decoding
    * Track top `k` hypotheses
    * Use log probabilities
    * EOS handling
    * Complexity
    * Follow-up: length normalization

15. **Viterbi algorithm**

    * Given transition probabilities, emission probabilities, and observations, compute the most likely hidden-state sequence
    * Dynamic programming
    * Backpointers

16. **Hidden Markov Model — Forward Algorithm**

    * Compute probability / likelihood of an observed sequence
    * Difference from Viterbi

17. **HMM decoding**

    * Transition matrix
    * Emission matrix
    * Initial probabilities
    * Most likely state sequence

18. **POS tagging with HMM + Viterbi**

    * Words = observations
    * POS tags = hidden states

19. **Edit distance / Levenshtein distance**

    * Insert
    * Delete
    * Replace
    * Dynamic programming

20. **Longest Common Subsequence**

    * Dynamic programming
    * Reconstruction if asked

21. **N-gram language model**

    * Compute next-token probabilities
    * Unigram / bigram / trigram
    * Sequence likelihood

22. **Laplace smoothing**

    * Apply to an n-gram LM or Naive Bayes
    * Explain unseen-event problem

23. **TF-IDF from scratch**

    * Term frequency
    * Inverse document frequency
    * Vector construction

24. **Cosine similarity**

    * Documents or embeddings
    * Handle zero vectors

25. **Bag-of-Words / vocabulary construction**

26. **CBOW**

    * Construct context → target examples
    * Compute simple context representation
    * Explain training objective

27. **Skip-gram**

    * Generate target-context training pairs
    * Explain difference from CBOW

28. **Negative sampling**

    * Construct positive and negative examples
    * Explain why it is cheaper than full softmax

---

# C. Transformer / decoding algorithms — high priority

29. **Dot-product attention**

    * Given Q, K, V, compute attention

30. **Scaled dot-product attention**

    * `QK^T / sqrt(d_k)`
    * Softmax
    * Multiply by V
    * Explain scaling

31. **Causal attention mask**

    * Build lower-triangular mask
    * Apply before softmax

32. **Top-k decoding**

    * Keep k highest logits/probabilities
    * Renormalize
    * Sample

33. **Top-p / nucleus sampling**

    * Sort probabilities
    * Cumulative probability
    * Keep smallest set whose cumulative mass >= p
    * Renormalize and sample

34. **Temperature scaling**

    * Apply temperature to logits
    * Explain `T < 1`, `T > 1`

---

# D. Numerical / statistics / production AI

35. **Feature normalization / standardization**

    * Mean/std
    * Min-max scaling
    * Avoid train/test leakage

36. **Online mean**

    * Update running mean without storing all values

37. **Welford’s online variance algorithm**

    * Numerically stable mean + variance

38. **Merge mean / variance from distributed workers**

    * Combine partial statistics correctly

39. **PCA from scratch**

    * Center data
    * Covariance matrix
    * Eigendecomposition / SVD
    * Project onto top-k components

40. **Log-sum-exp trick**

    * Numerically stable log of sum of exponentials

41. **Numerically stable sigmoid**

    * Avoid overflow for large positive/negative values

42. **Top-k selection**

    * Heap vs sorting
    * Complexity tradeoffs

43. **Confusion matrix**

    * TP, FP, TN, FN

44. **Precision, recall, F1**

    * Compute from predictions
    * Macro vs micro if asked

45. **ROC / AUC basics**

    * Compute threshold points
    * Explain ranking interpretation

46. **SGD**

    * Implement parameter update

47. **Momentum**

    * Velocity update

48. **Adam**

    * First and second moments
    * Bias correction
    * Parameter update

---

# E. Other short AI algorithms that may fit this round

If time permits, also cover:

49. **Perceptron update rule**
50. **Winnow algorithm**
51. **Gaussian likelihood / multivariate Gaussian basics**
52. **Gaussian Mixture Model E-step / responsibilities**
53. **One EM iteration for a simple GMM**
54. **Binary search over a model threshold / decision boundary**
55. **Feature hashing / hashing trick**
56. **Mini-batch iterator / shuffled batching**
57. **Class-balanced sampling**
58. **Gradient clipping**
59. **Early stopping logic**
60. **L2 regularization update**
61. **Dropout forward pass**
62. **Batch normalization forward pass**

---

## Priority guidance

If we run short on time, prioritize:

**Must do:**
1–18, 19, 23–24, 29–34, 39–41

**Strongly useful:**
20–22, 25–28, 35–38, 42–48

**Optional / fallback:**
49–62

Start with:

**Problem 1 — Median minimizes L1; mean minimizes L2**

and wait for me to say “next” before moving to the following problem.
