# 🧠 AIF-C01 Exam Traps Explained (theory + example trap)

The [trap sheet](EXAM-TRAP-SHEET.md) tells you **what** to pick. This guide tells you **why**, so you can handle a question you have never seen.

Each topic has the same four parts:

- **Theory:** the idea in plain words
- **The trap:** why the wrong answer looks attractive
- **Example:** an original mini scenario with the answer and why the others fail (not from any real exam)
- **Spot it:** the keyword in the question that gives it away

> All scenarios are invented for teaching. This guide contains no real exam questions and is not affiliated with AWS. Verify details against the [official exam guide](https://aws.amazon.com/certification/certified-ai-practitioner/).

**Jump to:** [Reading questions](#0-reading-the-question) · [Domain 1](#domain-1-ai-and-ml-fundamentals) · [Domain 2](#domain-2-generative-ai-fundamentals) · [Domain 3](#domain-3-applications-of-foundation-models) · [Domain 4](#domain-4-responsible-ai) · [Domain 5](#domain-5-security-compliance-governance)

---

## 0. Reading the question

### 0.1 "Most cost-effective", "least operational overhead", "fastest"
- **Theory:** these words tell you the *ranking rule*. Several options may work, but only one wins on that rule.
  - Cost: prompt engineering < RAG < fine-tuning < continued pre-training < training from scratch.
  - Overhead: fully managed or serverless beats anything you must build, host or patch.
  - Speed to deploy: a pre-trained AI service or a Bedrock API call beats building a model.
- **The trap:** picking the most powerful or most "correct" solution instead of the simplest that meets the need.
- **Example:** A team wants a support bot that answers from this week's policy PDFs, with the least operational overhead. Options: (A) train a custom model on SageMaker, (B) fine-tune a model on the PDFs, (C) Bedrock Knowledge Bases. **Answer: C.** A and B need training and go stale when the PDFs change. C is managed RAG, and new files are picked up by a sync.
- **Spot it:** "least effort", "no ML expertise", "managed", "quickly".

### 0.2 Absolute words
- **Theory:** AI has uncertainty built in. Nothing "guarantees", "eliminates" or "always" fixes accuracy, bias or hallucination.
- **The trap:** an answer that sounds reassuring ("RAG eliminates hallucinations").
- **Example:** "Which statement is TRUE about hallucination?" Pick "it can be reduced with grounding and human review", never "it can be fully eliminated with a larger model".
- **Spot it:** *always, never, only, guarantees, eliminates, completely.*

### 0.3 NOT / EXCEPT / LEAST
- **Theory:** the question flips. Three options are true; you must find the false one.
- **The trap:** your brain finds the first correct-looking option and stops.
- **Example:** "Which is NOT a hyperparameter?" Learning rate, batch size and number of epochs are. **Model weights are not** (they are learned parameters).
- **Spot it:** capital NOT, EXCEPT, LEAST. Cross out the true ones one by one.

### 0.4 "Choose two" and drag-and-drop
- **Theory:** each pick must be independently correct. Half right scores zero. For ordering, find the axis first (cost, effort, lifecycle step).
- **Example:** "Order from cheapest to most expensive": prompt engineering, RAG, fine-tuning, continued pre-training. Write the axis next to the list before you place anything.

---

## Domain 1: AI and ML fundamentals

### 1.1 Supervised vs unsupervised vs reinforcement
- **Theory:** the difference is the *feedback signal*.
  - Supervised: labeled examples (input + correct answer). Classification and regression.
  - Unsupervised: no labels; find structure. Clustering, dimensionality reduction, anomaly detection.
  - Reinforcement: an agent acts, gets rewards or penalties. Robotics, games, RLHF.
  - Self-supervised: labels come from the data itself (predict the next word). This is how foundation models are pre-trained.
- **The trap:** "labeled" sounds like "classified", so people call clustering supervised.
- **Example:** A shop wants to group customers into segments with no predefined groups. **Unsupervised (K-Means).** Predicting whether a customer will leave, given past leavers and stayers, is **supervised classification.**
- **Spot it:** "no labels", "discover groups" → unsupervised. "reward" → reinforcement.

### 1.2 Classification vs regression
- **Theory:** classification outputs a **category**; regression outputs a **number on a continuous scale**.
- **The trap:** *logistic regression* has "regression" in its name but is a classifier.
- **Example:** Predicting tomorrow's sales in dollars is regression. Predicting "fraud / not fraud" is classification.

### 1.3 Overfitting and underfitting
- **Theory:** a model can memorize or fail to learn.
  - Overfit: very good on training data, poor on new data (high variance). Fix with more data, regularization, dropout, early stopping, a simpler model.
  - Underfit: poor on both (high bias). Fix with a more complex model, better features, longer training.
- **The trap:** swapping bias and variance, or "fixing" overfitting with a bigger model.
- **Example:** Training accuracy 99%, test accuracy 70%. **Overfitting.** Adding layers makes it worse; adding data or regularization helps.
- **Spot it:** compare the training score with the score on unseen data.

### 1.4 Metrics: choose by the cost of being wrong
- **Theory:**
  - **Recall**: of all real positives, how many did you catch? Use when *missing* one is costly (disease, fraud).
  - **Precision**: of all you flagged, how many were right? Use when *false alarms* are costly.
  - **F1**: balance of both, good for imbalanced classes.
  - **AUC-ROC**: ranking quality across all thresholds.
  - **MSE/RMSE/MAE**: regression error.
  - **Accuracy** misleads when one class is rare (99% "not fraud" scores 99%).
- **The trap:** reaching for accuracy by default.
- **Example:** A rare-disease screener must not miss sick patients. Choose **recall**. A spam filter that must never hide real email leans on **precision**.
- **Spot it:** read what "a mistake" costs in the story.

### 1.5 Data hygiene and leakage
- **Theory:** split data into train, validation and test. The test set is touched once, at the end. Leakage means information from the test set influenced training, giving fake-high scores. Clean data first: handle missing values (imputation), outliers, duplicates, scale features, encode categories (one-hot).
- **The trap:** tuning the model on the test set "just to check".
- **Example:** Normalizing the *whole* dataset before splitting leaks test statistics into training. Fit the scaler on the training set only.

### 1.6 Parameters vs hyperparameters
- **Theory:** parameters (weights) are **learned** during training. Hyperparameters (learning rate, batch size, epochs, layers) are **set by you before** training and tuned by search (grid, random, Bayesian). **Gradient descent** is how weights are learned, not a hyperparameter search.

### 1.7 Pick the pre-trained AWS AI service
- **Theory:** match the **input type** and **job**:

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

- **The trap:** look-alike names and overlapping jobs (Textract *extracts* text, Comprehend *understands* it).
- **Example:** An insurer wants key-value pairs pulled from scanned claim forms. **Textract**, not Comprehend and not Rekognition.

### 1.8 Inference types
- **Theory:** real-time (low latency, steady traffic) · serverless (spiky or idle traffic, tolerates cold start) · async (large payloads, long jobs, queued) · batch (big offline datasets, no immediate answer).
- **Example:** A model used only a few times a day, no strict latency: **serverless inference**. A nightly scoring of 10 million rows: **batch transform**.

---

## Domain 2: Generative AI fundamentals

### 2.1 Tokens, embeddings, context window
- **Theory:** models read **tokens** (word pieces), not words. Cost and limits are counted in tokens. An **embedding** is a vector of numbers where similar meaning sits close together (powers semantic search and RAG). The **context window** is the max tokens of input plus output the model can handle at once.
- **The trap:** assuming "1 word = 1 token" or that a bigger context window is free.
- **Example:** A long contract does not fit in the context window. Options: chunk it and use RAG, or choose a model with a larger window (more cost and latency).

### 2.2 Temperature, top-p, top-k
- **Theory:** these control **sampling**, not knowledge.
  - Temperature high = more random and creative; low = focused and repeatable.
  - Top-p: sample from the smallest set of tokens whose probabilities add up to p.
  - Top-k: sample only from the k most likely tokens.
  - Max tokens caps length; stop sequences end generation.
- **The trap:** thinking temperature makes the model "smarter" or more accurate.
- **Example:** A tool that extracts invoice numbers must be consistent: **temperature near 0**. A brainstorming bot: higher temperature.

### 2.3 Hallucination
- **Theory:** the model produces fluent but false text because it predicts likely words, not verified facts. Mitigate with RAG (grounding), citations, lower temperature, guardrails with grounding checks, human review. It can never be fully removed.
- **The trap:** "knowledge cutoff" is different. A model that does not know yesterday's news is not hallucinating; it never saw that data. The fix is retrieval.

### 2.4 Prompt engineering techniques
- **Theory:**
  - Zero-shot: no examples. Few-shot: a few examples in the prompt. Chain-of-thought: ask for step-by-step reasoning.
  - Role/persona and clear format instructions. Negative prompts say what to avoid.
  - Prompt templates make prompts reusable.
- **The trap:** few-shot is *not* training. No weights change; the examples vanish after the call.
- **Example:** Answers are too long. Fix with a format instruction ("two sentences") and examples. Lowering max tokens only cuts the answer off mid-sentence.

### 2.5 RAG vs fine-tuning vs continued pre-training
- **Theory:** pick by *what you need to change*.

| Need | Choose | Why |
|---|---|---|
| Fresh or private facts, citations | **RAG** | Knowledge lives outside the model; update by re-syncing |
| Specific task format, tone, behaviour; you have labeled prompt/response pairs | **Fine-tuning** | Changes weights |
| Large unlabeled domain corpus to learn the language of a field | **Continued pre-training** | Self-supervised, no labels needed |
| Smaller cheaper copy of a big model | **Distillation** | Student mimics teacher |

- **The trap:** reaching for fine-tuning to "teach" the model new facts that change weekly.
- **Example:** A law firm has 50,000 unlabeled case files and wants the model to understand legal vocabulary: **continued pre-training**. A firm that wants answers quoting the latest regulations: **RAG**.

### 2.6 Evaluating text models
- **Theory:** **ROUGE** compares to reference summaries (recall-oriented). **BLEU** scores translation. **BERTScore** measures semantic similarity. **Perplexity** is fluency (lower is better). Use **human evaluation** for quality that numbers miss, and **benchmarks** (MMLU, HELM, GLUE) for comparison. Tie the choice to a business result.
- **The trap:** using accuracy or F1 for free text.
- **Example:** Evaluating a summarizer: **ROUGE** (plus human review). Evaluating translation: **BLEU**.

---

## Domain 3: Applications of foundation models

### 3.1 Knowledge Bases vs Agents vs Guardrails (Bedrock)
- **Theory:**
  - **Knowledge Bases**: managed RAG over your documents.
  - **Agents**: plan multi-step work and call tools through action groups (Lambda + API schema).
  - **Guardrails**: filter content and block topics, redact PII, check grounding on **input and output**.
- **The trap:** they are different layers. Guardrails do not retrieve data and do not control who may call the model (that is IAM).
- **Example:** A bot must book a meeting by calling a calendar API: **Agent**. It must never discuss competitors: **Guardrail with a denied topic**. It must quote HR policy: **Knowledge Base**.

### 3.2 On-demand vs Provisioned Throughput
- **Theory:** on-demand = pay per token, no commitment, for base models. **Provisioned Throughput** = reserved capacity (steady, high volume, predictable latency) and **is required to run a custom (fine-tuned) model.**
- **Example:** A team fine-tunes a model on Bedrock and wants to deploy it: they must buy Provisioned Throughput for it.

### 3.3 Bedrock vs SageMaker JumpStart
- **Theory:** Bedrock is a serverless API to many FMs (least overhead). JumpStart gives pre-trained models you deploy and host on your own endpoints (more control, more work).
- **Spot it:** "no infrastructure to manage" → Bedrock. "need custom container / full control of the endpoint" → SageMaker.

### 3.4 Chips: Trainium vs Inferentia
- **Theory:** **Trainium** trains. **Inferentia** serves predictions cheaply at scale. Easy to swap under pressure; remember "Trainium = Train".

### 3.5 RAG pipeline and vector stores
- **Theory:** documents are split into **chunks**, converted to **embeddings**, stored in a **vector store**. At question time the query is embedded, similar chunks are retrieved, and added to the prompt. Common stores: OpenSearch Serverless, Aurora/RDS PostgreSQL with pgvector, Neptune Analytics, MemoryDB, Amazon S3 Vectors.
- **The trap:** chunk size. Too large = noisy matches; too small = lost context.
- **Example:** Updating a policy: edit the document and re-sync the knowledge base. No retraining.

### 3.6 SageMaker tools mix-ups
- **Theory:**
  - **Ground Truth**: label training data. **A2I**: humans review predictions.
  - **Clarify**: bias and explainability (SHAP). **Model Monitor**: drift in production.
  - **Data Wrangler**: low-code data prep. **Pipelines**: orchestrate steps (MLOps). **Feature Store**: reuse features. **Model Registry/Cards**: version and document.
  - **Canvas** / **Autopilot**: no-code and automated ML.
- **Example:** Production model accuracy slowly drops as customer behaviour changes: **Model Monitor** (data drift), then retrain.

### 3.7 Deployment strategies
- **Theory:** **Blue/green** swaps traffic between two environments. **Canary** sends a small share first. **Shadow** copies live traffic to the new model without serving its answers. **A/B** compares two live variants.
- **Example:** Test a new model on real traffic with zero user risk: **shadow**.

### 3.8 Cost levers for GenAI
- **Theory:** smaller model, shorter prompts, capped output, caching, batch inference for non-urgent work, Provisioned Throughput for steady load, quantization or distillation to shrink a model.
- **Example:** Overnight bulk summarization of reports with no deadline: **batch inference**, cheaper than on-demand.

---

## Domain 4: Responsible AI

### 4.1 Bias and fairness
- **Theory:** bias comes from skewed data, labels, sampling or design. Fix with **diverse, representative data**, subgroup testing, and monitoring. A bigger model does not fix biased data.
- **Example:** A hiring model trained mostly on past hires from one group underperforms on others. Action: rebalance and evaluate per subgroup with **SageMaker Clarify**.

### 4.2 Explainability vs transparency vs interpretability
- **Theory:**
  - **Interpretability**: humans can understand the model's inner workings (linear models, trees).
  - **Explainability**: reasons for one specific output (SHAP, Clarify).
  - **Transparency**: openly documenting how the system was built, trained and should be used (Model Cards, AI Service Cards).
- **The trap:** treating the three as synonyms.
- **Example:** A regulator asks for documented intended use and limits: **transparency (Model Card)**. A customer asks why their loan was declined: **explainability**.

### 4.3 Human in the loop
- **Theory:** for high-stakes or low-confidence predictions, route to people (**Amazon A2I**). Removing human oversight entirely is the weak answer.

### 4.4 GenAI-specific risks
- **Theory:** toxicity, hallucination, IP/copyright exposure, privacy leakage, prompt injection. Controls: Guardrails, grounding, content filters, watermarking (AI-generated content provenance), review processes.

---

## Domain 5: Security, compliance, governance

### 5.1 Shared responsibility
- **Theory:** AWS secures the cloud itself (hardware, data centers, managed service software). **You** secure what you put in it: your data, IAM, encryption choices, prompts, guardrail settings, who may use models.
- **Example:** Who is responsible for deciding which employees may invoke a Bedrock model? **You (IAM).**

### 5.2 IAM vs Guardrails
- **Theory:** IAM decides **who and what may call** a service (least privilege). Guardrails decide **what content** the model may take in or produce.

### 5.3 CloudTrail vs CloudWatch
- **Theory:** **CloudTrail** records **who did what** (API call audit). **CloudWatch** records **how it is performing** (metrics, logs, alarms). **Bedrock model invocation logging** sends prompts and responses to CloudWatch Logs or S3.
- **Example:** "Who invoked the model last Tuesday?" is CloudTrail. "Is latency rising?" is CloudWatch.

### 5.4 Artifact vs Audit Manager
- **Theory:** **Artifact** downloads AWS's own compliance reports and agreements. **Audit Manager** gathers evidence about *your* resources for audits.

### 5.5 Macie vs Comprehend (PII)
- **Theory:** **Macie** finds sensitive data **stored in S3**. **Comprehend** detects PII **inside text you analyze**. Guardrails can redact PII in model input and output.

### 5.6 Prompt injection, jailbreak, prompt leaking
- **Theory:**
  - **Prompt injection**: user text overrides your instructions.
  - **Jailbreak**: tricking the model into disallowed output.
  - **Prompt leaking**: extracting the hidden system prompt or history.
  - Defences: input validation and sanitization, output filtering, Guardrails, least-privilege tool access, human approval for risky actions.
- **Example:** Both **input sanitization and output filtering** are needed; one direction alone leaves a gap.

### 5.7 Encryption and private access
- **Theory:** **KMS** for keys, **server-side encryption** at rest, **TLS/HTTPS** in transit, **VPC endpoints / PrivateLink** to keep traffic off the public internet, **Secrets Manager** for keys.
- **Trap:** a NAT gateway or internet gateway still leaves the traffic going through the internet path.

### 5.8 Compliance and governance names
- **Theory:** GDPR (EU privacy), HIPAA (US health data), PCI DSS (cards), SOC and ISO 27001 (security), **ISO 42001** (AI management system), NIST AI RMF (AI risk framework), EU AI Act (risk-tiered rules). Governance means lineage, documentation, retention, residency, audits, and clear ownership.

---

## Quick self-test (try before you check the sheet)

1. A model scores 98% on training data and 72% on new data. What is wrong, and name two fixes.
2. You need answers that cite the latest policy documents. RAG or fine-tuning? Why?
3. Name the single service for each: speech to text, scanned form extraction, enterprise search, bias detection.
4. A fine-tuned model must be deployed on Bedrock. What capacity option is needed?
5. Which tool tells you *who* called an API, and which tells you *how* it is performing?

**Answers:** 1) Overfitting; more data, regularization, early stopping, simpler model. 2) RAG, because the facts change and you need citations. 3) Transcribe, Textract, Kendra, Clarify. 4) Provisioned Throughput. 5) CloudTrail; CloudWatch.
