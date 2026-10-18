# 🧠 AIF-C01 Exam Traps Explained (theory + examples)

The [trap sheet](EXAM-TRAP-SHEET.md) tells you **what** to pick. This guide tells you **why**, so you can handle a question you have never seen.

Each topic has the same parts:

- **Theory:** the idea in plain words, with a simple picture where it helps
- **In more detail:** how it works underneath, so you can reason about variations
- **The trap:** why the wrong answer looks attractive
- **Example 1 and Example 2:** original mini scenarios, with the answer and why the other options fail
- **Spot it:** the keyword in the question that gives it away

> All scenarios are invented for teaching. This guide contains no real exam questions and is not affiliated with AWS. Verify details against the [official exam guide](https://aws.amazon.com/certification/certified-ai-practitioner/).

**Jump to:** [Study plan](#-how-to-use-this-before-your-exam-date) · [Reading questions](#0-reading-the-question) · [Domain 1](#domain-1-ai-and-ml-fundamentals) · [Domain 2](#domain-2-generative-ai-fundamentals) · [Domain 3](#domain-3-applications-of-foundation-models) · [Domain 4](#domain-4-responsible-ai) · [Domain 5](#domain-5-security-compliance-governance)

---

## 📅 How to use this before your exam date

Three tools work together: this guide (**why**), the [trap sheet](EXAM-TRAP-SHEET.md) (**what to pick**) and the [interactive checklist](https://chathurangavkd.github.io/AWS-Certified-AI-Practitioner-AIF-C01/trap-checklist.html) (**tick them off, quiz yourself**).

| When | Do this | Time |
|---|---|---|
| **7 days before** | Read this guide one domain per day (Domains 1 to 5, plus section 0). Do the self-test at the end. | 30 min/day |
| **3 days before** | Open the checklist and use **🎯 Quiz me**. Mark "Got it" or flag "Review later". | 45 min/day |
| **2 days before** | Filter the checklist by **⚑ Flagged**. For each, re-read its topic here to understand *why*. | 40 min |
| **1 day before** | Read the trap sheet top to bottom once, then clear the remaining **To do** items. No new topics. | 60 min |
| **Exam morning** | Skim sections 0, 6 (look-alike pairs) and 11 (final checklist) of the trap sheet. Sleep and arrive early beat last-minute cramming. | 15 min |

**On exam day:** read the *last line* of each question first (what is it asking?), find the ranking word (cost, overhead, fastest, NOT), strike out options that fail the hard requirement, and never leave a question blank (there is no penalty for guessing). Flag hard ones and come back.

---

## 0. Reading the question

### 0.1 "Most cost-effective", "least operational overhead", "fastest"
- **Theory:** these words give the *ranking rule*. Several options may work, but only one wins on that rule. It is like getting to a nearby shop: a taxi, a bus and walking all work. If the rule is "cheapest", you walk.
  - Cost: prompt engineering < RAG < fine-tuning < continued pre-training < training from scratch.
  - Overhead: fully managed or serverless beats anything you must build, host or patch.
  - Speed to deploy: a pre-trained AI service or a Bedrock API call beats building a model.
- **In more detail:** first strike out options that fail the *hard requirement* (what the solution must do), then apply the ranking rule to the survivors. The rule is only a tiebreaker among options that already work.
- **The trap:** picking the most powerful or impressive answer instead of the simplest one that meets the need.
- **Example 1:** A team wants a support bot that answers from this week's policy PDFs, with the least operational overhead. (A) train a custom model on SageMaker, (B) fine-tune a model on the PDFs, (C) Bedrock Knowledge Bases. **Answer: C.** A and B need training and go stale when the PDFs change. C is managed RAG; new files are picked up by a sync.
- **Example 2:** A company must read text from scanned receipts and has no ML staff. (A) train a custom OCR model, (B) Amazon Textract, (C) open-source OCR on EC2. **Answer: B.** A needs training and hosting, C means you patch and scale servers. Change the stem to "highest accuracy on an unusual format, and we have ML engineers" and A becomes defensible. The words around the question decide it.
- **Spot it:** "least effort", "no ML expertise", "managed", "quickly", "cost-effective".

### 0.2 Absolute words
- **Theory:** AI is probabilistic. Nothing "guarantees", "eliminates" or "always" fixes accuracy, bias or hallucination. A weather forecast says "70% chance of rain", not "it will never rain".
- **In more detail:** exam writers use overconfident wording as a wrong-answer signal, mostly in questions about accuracy, bias, hallucination and security. Not every absolute is false ("data in transit is encrypted with TLS" is fine), so check the topic.
- **The trap:** an answer that sounds reassuring ("RAG eliminates hallucinations").
- **Example 1:** "Which is TRUE about hallucination?" Pick "it can be reduced with grounding and human review". Reject "it can be fully eliminated with a larger model".
- **Example 2:** "Setting temperature to 0 makes the model always factually correct" is false. Temperature 0 makes output *repeatable*, so the model can repeat the same wrong answer every time.
- **Spot it:** *always, never, only, guarantees, eliminates, completely, 100%.*

### 0.3 NOT / EXCEPT / LEAST
- **Theory:** the question flips. Three options are true; you must find the false one.
- **In more detail:** circle the negative word, then label every option T or F as a plain statement. The answer is the odd one out. Do not stop at the first familiar true statement.
- **The trap:** your brain finds a correct-looking option and stops.
- **Example 1:** "Which is NOT a hyperparameter?" Learning rate, batch size and number of epochs are chosen by you. **Model weights are not**; they are learned parameters.
- **Example 2:** "Which is NOT a feature of SageMaker Ground Truth?" Labeling workflows, active-learning auto-labeling and workforce management are. **Training your production model is not.**
- **Spot it:** capital NOT, EXCEPT, LEAST, "which is false".

### 0.4 "Choose two" and drag-and-drop
- **Theory:** each pick must be independently correct. Half right scores zero. For ordering, find the axis first (cost, effort, lifecycle step).
- **In more detail:** for "choose two", test every option as true or false. If three look true, find the one that fails the exact wording of the stem.
- **Example 1:** "Which TWO reduce prompt-injection risk?" Input validation and output filtering/guardrails. A larger model, a higher temperature or turning off logging do not help.
- **Example 2:** "Order from cheapest to most expensive": prompt engineering, RAG, fine-tuning, continued pre-training. Write "cost" in the margin first, then sort.
- **Spot it:** "(Choose two)", "Select all that apply", two columns to match.

### 0.5 Words in the stem that point at a service
| Clue | Likely answer |
|---|---|
| "latest", "company documents", "cite sources" | RAG / Knowledge Bases |
| "tone", "style", "labeled examples" | Fine-tuning |
| "unlabeled domain text", "domain vocabulary" | Continued pre-training |
| "multi-step", "call an API" | Bedrock Agents |
| "block topics", "redact PII" | Bedrock Guardrails |
| "who called", "audit" | CloudTrail |
| "latency", "errors", "alarm" | CloudWatch |
| "bias", "explain predictions" | SageMaker Clarify |
| "drift in production" | SageMaker Model Monitor |
| "human review of predictions" | Amazon A2I |

---

## Domain 1: AI and ML fundamentals

### 1.1 Supervised vs unsupervised vs reinforcement
- **Theory:** the difference is the *feedback signal*. Supervised = labeled examples. Unsupervised = no labels, find structure. Reinforcement = an agent acts and gets rewards. Self-supervised = labels come from the data itself (predict the next word); this is how foundation models are pre-trained.
- **In more detail:** supervised learning is like studying with an answer key. Unsupervised is sorting a pile of photos into groups without being told the groups. Reinforcement is training a dog with treats. Semi-supervised mixes a little labeled data with a lot of unlabeled data.
- **The trap:** "labeled" sounds like "classified", so people call clustering supervised.
- **Example 1:** A shop wants customer segments with no predefined groups. **Unsupervised (K-Means).**
- **Example 2:** Predicting whether a customer will leave, using past leavers and stayers, is **supervised classification**. A robot learning to walk from reward signals is **reinforcement learning**.
- **Spot it:** "no labels", "discover groups" → unsupervised. "reward", "agent" → reinforcement.

### 1.2 Classification vs regression
- **Theory:** classification outputs a **category**; regression outputs a **number on a continuous scale**.
- **In more detail:** ask "could the answer be 17.3?" If yes, it is regression. Binary classification has two classes (spam/not), multiclass has more.
- **The trap:** *logistic regression* has "regression" in its name but is a classifier.
- **Example 1:** Predicting tomorrow's sales in dollars is regression.
- **Example 2:** Deciding "fraud / not fraud" is classification, even if the model first produces a probability like 0.93.

### 1.3 Overfitting and underfitting
- **Theory:** a model can memorize or fail to learn. Overfit = great on training data, poor on new data (high variance). Underfit = poor on both (high bias).
- **In more detail:** overfitting is a student who memorized last year's paper and fails a new one. Fixes: more data, regularization, dropout, early stopping, a simpler model. Underfitting is a student who barely studied. Fixes: more complex model, better features, longer training.
- **The trap:** swapping bias and variance, or "fixing" overfitting with a bigger model.
- **Example 1:** Training accuracy 99%, test accuracy 70%. **Overfitting.** Adding layers makes it worse; more data or regularization helps.
- **Example 2:** Training 62%, test 60%. **Underfitting**; add features or use a more expressive model.
- **Spot it:** compare the training score with the score on unseen data.

### 1.4 Metrics: choose by the cost of being wrong
- **Theory:**
  - **Recall**: of all real positives, how many did you catch? Use when *missing* one is costly.
  - **Precision**: of all you flagged, how many were right? Use when *false alarms* are costly.
  - **F1**: balance of both, good for imbalanced classes.
  - **AUC-ROC**: ranking quality across all thresholds.
  - **MSE/RMSE/MAE**: regression error.
- **In more detail:** accuracy misleads when one class is rare. If 1% of transactions are fraud, a model that says "not fraud" always scores 99% and catches nothing. A confusion matrix (true/false positives and negatives) shows where the errors are.
- **The trap:** reaching for accuracy by default.
- **Example 1:** A rare-disease screener must not miss sick patients. Choose **recall**.
- **Example 2:** A spam filter that must never hide a real customer email should favour **precision**. A single score balancing both on imbalanced data: **F1**.
- **Spot it:** read what "a mistake" costs in the story.

### 1.5 Data hygiene and leakage
- **Theory:** split data into train, validation and test. The test set is used once, at the end. Leakage means information from the test set influenced training, giving fake-high scores.
- **In more detail:** clean data first: handle missing values (imputation), outliers and duplicates, scale features, and encode categories (one-hot). Fit scalers and encoders on the training set only.
- **The trap:** tuning the model on the test set "just to check".
- **Example 1:** Normalizing the whole dataset before splitting leaks test statistics into training.
- **Example 2:** A model scores 99% in testing but 60% in production. Check for leakage, or for data that differs from real-world data.

### 1.6 Parameters vs hyperparameters
- **Theory:** parameters (weights) are **learned** during training. Hyperparameters (learning rate, batch size, epochs, layers) are **set by you** before training and tuned by search (grid, random, Bayesian).
- **In more detail:** **gradient descent** is how weights are learned, so it is not a hyperparameter search method. SageMaker automatic model tuning runs the search for you.
- **Example 1:** "Which is NOT a hyperparameter tuning technique?" Pick gradient descent over grid, random or Bayesian search.
- **Example 2:** Raising the learning rate is a hyperparameter change; the learned weights are not something you set.

### 1.7 Pick the pre-trained AWS AI service
- **Theory:** match the **input type** and the **job**.

| Input | Job | Service |
|---|---|---|
| Image / video | objects, faces, moderation | Rekognition |
| Scanned doc / form | extract text, tables | Textract |
| Text | sentiment, entities, PII | Comprehend |
| Audio | speech to text | Transcribe |
| Text | text to speech | Polly |
| Text | translate | Translate |
| Conversation | chatbot | Lex |
| Documents | enterprise search | Kendra |
| History | recommendations | Personalize |
| Time series | forecast | Forecast |

- **In more detail:** Textract *extracts* text from a document; Comprehend *understands* text you already have. Lex builds the conversation; Kendra searches your content. A common pipeline: Transcribe (speech to text) → Comprehend (sentiment) → Translate.
- **The trap:** look-alike names and overlapping jobs.
- **Example 1:** An insurer wants key-value pairs from scanned claim forms. **Textract.**
- **Example 2:** A call center wants the mood of recorded calls. **Transcribe, then Comprehend**; neither alone does both jobs.

### 1.8 Inference types
- **Theory:** real-time (low latency, steady traffic), serverless (spiky or idle traffic, tolerates cold start), async (large payloads, long jobs, queued), batch (big offline datasets, no immediate answer).
- **In more detail:** think of a restaurant. Real-time is a waiter at your table, serverless is a food truck that only appears when customers come, batch is catering a big order overnight.
- **Example 1:** A model used a few times a day with no strict latency: **serverless inference.**
- **Example 2:** Scoring 10 million rows overnight: **batch transform.** Sub-second fraud checks on steady traffic: **real-time endpoint.**

---

## Domain 2: Generative AI fundamentals

### 2.1 Tokens, embeddings, context window
- **Theory:** models read **tokens** (word pieces), not words. Cost and limits are counted in tokens. An **embedding** is a vector of numbers where similar meaning sits close together. The **context window** is the maximum tokens of input plus output the model can handle at once.
- **In more detail:** "unbelievable" may be several tokens. Embeddings power semantic search: the query and each document become vectors, and the closest ones are retrieved. A larger context window allows longer prompts but usually costs more and adds latency.
- **The trap:** assuming 1 word = 1 token, or that a larger context window is free.
- **Example 1:** A long contract does not fit in the context window. Options: chunk it and use RAG, or pick a model with a larger window.
- **Example 2:** Searching "reset my password" should also find "forgot login credentials". That is semantic search using **embeddings**, not keyword matching.

### 2.2 Temperature, top-p, top-k
- **Theory:** these control **sampling**, not knowledge. Higher temperature = more random and creative; lower = focused and repeatable.
- **In more detail:** top-p samples from the smallest set of tokens whose probabilities add up to p. Top-k samples only from the k most likely tokens. Max tokens caps length, and stop sequences end generation.
- **The trap:** thinking temperature makes the model smarter or more accurate.
- **Example 1:** A tool that extracts invoice numbers must be consistent: **temperature near 0**.
- **Example 2:** A brainstorming bot for slogans: a **higher temperature** (and/or higher top-p) gives more varied ideas.

### 2.3 Hallucination
- **Theory:** the model produces fluent but false text because it predicts likely words, not verified facts.
- **In more detail:** mitigations are RAG (grounding), citations, lower temperature, guardrails with a grounding check, and human review. It can be reduced, never fully removed.
- **The trap:** confusing it with **knowledge cutoff**. A model that does not know yesterday's news never saw that data; the fix is retrieval, not "less hallucination".
- **Example 1:** A bot invents a refund policy that does not exist. Ground it with a Knowledge Base and require citations.
- **Example 2:** A model gives last year's price list. That is a cutoff problem, solved by RAG with current data.

### 2.4 Prompt engineering techniques
- **Theory:** zero-shot (no examples), few-shot (a few examples in the prompt), chain-of-thought (ask for step-by-step reasoning), role/persona, clear format instructions, negative prompts (what to avoid).
- **In more detail:** prompts are cheap to change and need no training, so they come first in the cost ladder. Prompt templates make prompts reusable with variables.
- **The trap:** few-shot is *not* training. No weights change, and the examples vanish after the call.
- **Example 1:** Answers are too long. Add a format instruction ("two sentences") and an example. Lowering max tokens only cuts the answer off mid-sentence.
- **Example 2:** A math word problem is answered wrongly. Add "think step by step" (**chain-of-thought**).

### 2.5 RAG vs fine-tuning vs continued pre-training
- **Theory:** pick by *what you need to change*.

| Need | Choose |
|---|---|
| Fresh or private facts, citations | **RAG** |
| Specific task format, tone, behaviour, with labeled prompt/response pairs | **Fine-tuning** |
| Large unlabeled domain corpus to learn a field's language | **Continued pre-training** |
| Smaller cheaper copy of a big model | **Distillation** |

- **In more detail:** RAG leaves the model unchanged and adds knowledge at question time, like an open-book exam. Fine-tuning teaches a new habit, like training for a specific job. Continued pre-training is extra general reading in a field.
- **The trap:** using fine-tuning to teach facts that change weekly.
- **Example 1:** A law firm has 50,000 unlabeled case files and wants the model to learn legal vocabulary: **continued pre-training.**
- **Example 2:** A firm wants answers that quote the latest regulations: **RAG.** A team with 2,000 approved question/answer pairs wanting a consistent brand voice: **fine-tuning.**

### 2.6 Evaluating text models
- **Theory:** **ROUGE** compares to reference summaries. **BLEU** scores translation. **BERTScore** measures semantic similarity. **Perplexity** is fluency (lower is better).
- **In more detail:** use **human evaluation** for quality numbers miss and **benchmarks** (MMLU, HELM, GLUE) for comparing models. Tie the choice to a business result.
- **The trap:** using accuracy or F1 for free text.
- **Example 1:** Evaluating a summarizer: **ROUGE** (plus human review).
- **Example 2:** Evaluating machine translation: **BLEU**. Comparing two models for fit to your task: human evaluation plus benchmarks.

---

## Domain 3: Applications of foundation models

### 3.1 Knowledge Bases vs Agents vs Guardrails (Bedrock)
- **Theory:** **Knowledge Bases** = managed RAG over your documents. **Agents** = plan multi-step work and call tools through action groups (Lambda + API schema). **Guardrails** = filter content, block topics, redact PII and check grounding on input and output.
- **In more detail:** they are different layers and often combined. Guardrails do not retrieve data, and they do not control who may call the model (that is IAM).
- **The trap:** treating them as alternatives.
- **Example 1:** A bot must book a meeting by calling a calendar API: **Agent.**
- **Example 2:** The same bot must never discuss competitors: **Guardrail with a denied topic.** It must quote HR policy: **Knowledge Base.**

### 3.2 On-demand vs Provisioned Throughput
- **Theory:** on-demand = pay per token, no commitment, for base models. **Provisioned Throughput** = reserved capacity for steady, high-volume traffic with predictable latency, and it is **required to run a custom (fine-tuned) model.**
- **In more detail:** on-demand suits experiments and spiky use. Provisioned suits production load you can predict. Batch inference is cheaper still for non-urgent bulk jobs.
- **Example 1:** A team fine-tunes a model on Bedrock and wants to deploy it: they need Provisioned Throughput.
- **Example 2:** A prototype used a few times a day: on-demand.

### 3.3 Bedrock vs SageMaker JumpStart
- **Theory:** Bedrock is a serverless API to many foundation models (least overhead). JumpStart provides pre-trained models you deploy and host on your own endpoints (more control, more work).
- **Example 1:** "No infrastructure to manage" → Bedrock.
- **Example 2:** "Need full control of the endpoint and container" → SageMaker (JumpStart).

### 3.4 Chips: Trainium vs Inferentia
- **Theory:** **Trainium** trains models; **Inferentia** serves predictions cheaply at scale.
- **In more detail:** the names help: Trainium has "train", Inferentia has "infer". GPUs (P/G instances) are the general deep-learning option.
- **Example:** "Lowest cost for high-volume inference" → Inferentia. "Cost-efficient large model training" → Trainium.

### 3.5 RAG pipeline and vector stores
- **Theory:** documents are split into **chunks**, turned into **embeddings**, and stored in a **vector store**. At question time the query is embedded, similar chunks are retrieved and added to the prompt.
- **In more detail:** common stores include OpenSearch Serverless, Aurora/RDS PostgreSQL with pgvector, Neptune Analytics, MemoryDB and Amazon S3 Vectors. Chunk size matters: too large = noisy matches; too small = lost context.
- **Example 1:** A policy changes. Edit the document and re-sync the knowledge base; no retraining.
- **Example 2:** Answers feel off-topic. Check chunk size and retrieval settings before blaming the model.

### 3.6 SageMaker tool mix-ups
- **Theory:** **Ground Truth** labels data; **A2I** gets humans to review predictions; **Clarify** detects bias and explains predictions; **Model Monitor** watches drift; **Data Wrangler** prepares data with low code; **Pipelines** orchestrates steps; **Feature Store** reuses features; **Model Registry** versions models; **Model Cards** document them; **Canvas/Autopilot** are no-code and automated ML.
- **Example 1:** Accuracy slowly drops as customer behaviour changes: **Model Monitor** (data drift), then retrain.
- **Example 2:** An analyst with no coding skills wants to build a prediction model: **SageMaker Canvas.**

### 3.7 Deployment strategies
- **Theory:** **Blue/green** swaps traffic between two environments. **Canary** sends a small share first. **Shadow** copies live traffic to the new model without serving its answers. **A/B** compares two live variants.
- **Example 1:** Test a new model on real traffic with zero user risk: **shadow.**
- **Example 2:** Release to 5% of users first and expand: **canary.**

### 3.8 Cost levers for GenAI
- **Theory:** a smaller model, shorter prompts, capped output, caching, batch inference for non-urgent work, Provisioned Throughput for steady load, and quantization or distillation to shrink a model.
- **Example 1:** Overnight bulk summaries with no deadline: **batch inference.**
- **Example 2:** Cutting latency and cost on a large model: **distillation** (small student learns from a large teacher) or **quantization** (lower-precision weights).

---

## Domain 4: Responsible AI

### 4.1 Bias and fairness
- **Theory:** bias comes from skewed data, labels, sampling or design. Fix with **diverse, representative data**, subgroup testing and monitoring.
- **In more detail:** a bigger model does not fix biased data. Evaluate performance per subgroup, not just overall.
- **Example 1:** A hiring model trained mostly on past hires from one group underperforms on others. Rebalance data and test per subgroup with **SageMaker Clarify**.
- **Example 2:** A face tool works poorly on some skin tones because the training photos were not representative. Fix the dataset, not the temperature.

### 4.2 Explainability vs transparency vs interpretability
- **Theory:** **Interpretability** = understanding the model's inner workings (linear models, trees). **Explainability** = reasons for one specific output (SHAP, Clarify). **Transparency** = openly documenting how the system was built, trained and should be used (Model Cards, AI Service Cards).
- **The trap:** treating the three as synonyms.
- **Example 1:** A regulator asks for documented intended use and limits: **transparency (Model Card).**
- **Example 2:** A customer asks why their loan was declined: **explainability.**

### 4.3 Human in the loop
- **Theory:** for high-stakes or low-confidence predictions, route to people (**Amazon A2I**).
- **Example 1:** Medical or legal decisions that affect people keep a human reviewer.
- **Example 2:** A design that removes all human oversight from a sensitive process is the weak answer.

### 4.4 GenAI-specific risks
- **Theory:** toxicity, hallucination, IP/copyright exposure, privacy leakage and prompt injection.
- **In more detail:** controls are Guardrails, grounding, content filters, watermarking (provenance of AI-generated content) and review processes.
- **Example:** A model might reproduce copyrighted material: the risk is **intellectual property**, and the answer involves review and legal safeguards, not temperature.

---

## Domain 5: Security, compliance, governance

### 5.1 Shared responsibility
- **Theory:** AWS secures the cloud itself (hardware, data centers, managed service software). **You** secure what you put in it: data, IAM, encryption choices, prompts, guardrail settings and who may use models.
- **Example 1:** Who decides which employees may invoke a Bedrock model? **You, through IAM.**
- **Example 2:** Who patches the physical servers behind Bedrock? **AWS.**

### 5.2 IAM vs Guardrails
- **Theory:** IAM decides **who and what may call** a service (least privilege). Guardrails decide **what content** the model may take in or produce.
- **Example:** "Block users from asking about medical dosage" → Guardrail. "Only the data-science team can invoke this model" → IAM.

### 5.3 CloudTrail vs CloudWatch
- **Theory:** **CloudTrail** records **who did what** (API call audit). **CloudWatch** records **how it is performing** (metrics, logs, alarms).
- **In more detail:** **Bedrock model invocation logging** sends prompts and responses to CloudWatch Logs or S3.
- **Example 1:** "Who invoked the model last Tuesday?" → CloudTrail.
- **Example 2:** "Is latency rising?" → CloudWatch.

### 5.4 Artifact vs Audit Manager
- **Theory:** **Artifact** downloads AWS's own compliance reports and agreements. **Audit Manager** gathers evidence about *your* resources for audits.
- **Example:** "Download AWS's SOC report" → Artifact. "Collect evidence that our accounts meet a framework" → Audit Manager.

### 5.5 Macie vs Comprehend (PII)
- **Theory:** **Macie** finds sensitive data **stored in S3**. **Comprehend** detects PII **inside text you analyze**. Guardrails can redact PII in model input and output.
- **Example:** "Scan our S3 buckets for exposed personal data" → Macie.

### 5.6 Prompt injection, jailbreak, prompt leaking
- **Theory:** **prompt injection** = user text overrides your instructions. **Jailbreak** = tricking the model into disallowed output. **Prompt leaking** = extracting the hidden system prompt or history.
- **In more detail:** defences are input validation and sanitization, output filtering, Guardrails, least-privilege tool access and human approval for risky actions.
- **Example 1:** Both **input sanitization and output filtering** are needed; one direction alone leaves a gap.
- **Example 2:** An agent that can delete records on request needs narrow permissions and approval, to limit "excessive agency".

### 5.7 Encryption and private access
- **Theory:** **KMS** for keys, **server-side encryption** at rest, **TLS/HTTPS** in transit, **VPC endpoints / PrivateLink** to keep traffic off the public internet, **Secrets Manager** for keys.
- **The trap:** a NAT or internet gateway still sends traffic over the internet path.
- **Example:** "Keep Bedrock traffic private inside the VPC" → interface VPC endpoint (PrivateLink).

### 5.8 Compliance and governance names
- **Theory:** GDPR (EU privacy), HIPAA (US health data), PCI DSS (cards), SOC and ISO 27001 (security), **ISO 42001** (AI management system), NIST AI RMF (AI risk framework), EU AI Act (risk-tiered rules).
- **In more detail:** governance means lineage, documentation, retention, residency, audits and clear ownership.
- **Example:** "Which standard covers an AI management system?" → ISO 42001.

---

## Quick self-test (try before you check the sheet)

1. A model scores 98% on training data and 72% on new data. What is wrong, and name two fixes.
2. You need answers that cite the latest policy documents. RAG or fine-tuning? Why?
3. Name the service for each: speech to text, scanned form extraction, enterprise search, bias detection.
4. A fine-tuned model must be deployed on Bedrock. What capacity option is needed?
5. Which tool tells you *who* called an API, and which tells you *how* it is performing?

**Answers:** 1) Overfitting; more data, regularization, early stopping, simpler model. 2) RAG, because the facts change and you need citations. 3) Transcribe, Textract, Kendra, Clarify. 4) Provisioned Throughput. 5) CloudTrail; CloudWatch.
