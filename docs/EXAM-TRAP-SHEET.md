# 🪤 AIF-C01 Exam Trap Sheet (last-day review)

**Tick them off as you go:** open the [interactive trap checklist](https://chathurangavkd.github.io/AWS-Certified-AI-Practitioner-AIF-C01/trap-checklist.html). It turns every trap below into a checkbox, shows overall and per-section progress, and saves it in your browser.

Read top to bottom in about 45 minutes. Each row is **"if you see X, pick Y, and don't fall for Z"**.
Written from the public exam guide domains in original wording. It contains **no real exam questions and no text copied from any exam-prep vendor**. It is an independent study aid, not affiliated with or endorsed by AWS, and should be checked against the [official exam guide](https://aws.amazon.com/certification/certified-ai-practitioner/).

**Exam facts:** 65 questions (50 scored, 15 unscored) · 90 min · pass 700/1000 · no penalty for guessing, so never leave a blank.
**Weights:** D1 AI/ML fundamentals 20% · D2 GenAI fundamentals 24% · D3 FM applications 28% · D4 Responsible AI 14% · D5 Security/governance 14%.

---

## 0. Test-taking traps (apply to every question)

| Trap | Rule |
|---|---|
| "Most **cost-effective**" | Cheapest that meets the need: prompt engineering < RAG < fine-tuning < continued pre-training < training from scratch. On-demand < provisioned only for spiky or low volume. |
| "**Least operational overhead**" | Fully managed / serverless (Bedrock, Rekognition, Comprehend, Textract, Transcribe, Translate...) beats SageMaker custom builds or EC2. |
| "**Fastest** to implement" | Pre-trained AI service or Bedrock API, not building a model. |
| "**No ML expertise** / no data scientists" | AI services, SageMaker Canvas (no code), Bedrock. |
| "Needs **latest/private company data**" | RAG (Knowledge Bases), not fine-tuning. |
| "Change **tone/style/domain behaviour** permanently" | Fine-tuning, not RAG. |
| Two answers both sound right | Pick the one that is AWS-native and managed, and uses the exact keyword in the stem. |
| Absolute words (**always, never, only, guarantees**) | Usually wrong, especially about accuracy, bias or hallucination ("eliminates", "guarantees"). |
| Service name look-alikes | Re-read: Rekognition vs Recognition, Comprehend vs Comprehend Medical, Lex vs Kendra, Polly vs Transcribe. |

---

## 1. Domain 1: AI/ML fundamentals

### Definitions that get swapped
| Term | Correct meaning | Common wrong swap |
|---|---|---|
| AI ⊃ ML ⊃ Deep Learning ⊃ GenAI | Nested sets | Treating them as separate |
| Supervised | **Labeled** data (classification, regression) | Confusing with "has a supervisor" |
| Unsupervised | **Unlabeled**; clustering, dimensionality reduction, anomaly detection | Not "no data" |
| Reinforcement learning | Agent, environment, **reward**; robotics, games, RLHF | Not labeled data |
| Self-supervised | Labels derived from the data itself (next-token prediction); how FMs are pre-trained | Not unsupervised clustering |
| Semi-supervised | Small labeled + large unlabeled | |
| Classification | Discrete category (spam / not spam) | vs regression |
| Regression | **Continuous number** (price, temperature) | vs classification |
| Clustering | Group similar unlabeled items (customer segmentation) | vs classification |
| Inference | Using a trained model to predict | vs training |
| Batch inference | Large offline datasets, no latency need | vs real-time endpoint |
| Real-time inference | Low latency, steady traffic | |
| Serverless inference | Intermittent traffic, tolerates cold start | |
| Async inference | Large payloads, long processing, queued | |

### Fitting problems (high-yield)
| Symptom | Diagnosis | Fix |
|---|---|---|
| Great on training, bad on new data | **Overfitting** (high variance) | More data, regularization, simpler model, early stopping, dropout |
| Bad on both | **Underfitting** (high bias) | More complex model, more features, train longer |
| Train fine, production degrades over time | **Data drift / model drift** | SageMaker Model Monitor, retrain |
| Bias-variance | High bias = underfit; high variance = overfit | Don't reverse them |

### Metrics: pick by the business cost
| Situation | Metric |
|---|---|
| Missing a positive is costly (cancer, fraud) | **Recall** (sensitivity) |
| False alarms are costly (spam filter flags real mail) | **Precision** |
| Imbalanced classes, need balance | **F1** (accuracy is misleading when imbalanced) |
| Overall classifier quality across thresholds | **AUC-ROC** |
| Regression error | **RMSE / MAE / MSE**; R² is explained variance |
| Machine translation | **BLEU** |
| Summarization | **ROUGE** |
| Semantic similarity of generated text | **BERTScore** |
| Language model fluency | **Perplexity** (lower is better) |
| Cluster / multiclass breakdown | **Confusion matrix** |

### Data & lifecycle
- Split: train / validation / test. **Test set is never used for tuning.**
- Feature engineering, normalization, handling missing values come **before** training.
- Hyperparameters are set **before** training (learning rate, batch size, epochs); parameters/weights are **learned**.
- Data leakage = test info leaks into training, giving falsely high scores.
- ML lifecycle: business goal, data collection, EDA, preprocessing, train, tune, evaluate, deploy, monitor, retrain. **MLOps** = automate this (SageMaker Pipelines, Model Registry).
- **Don't use ML** when a simple rule or deterministic logic solves it, or when you have no data.
- Black-box vs interpretable: linear regression and decision trees are explainable; deep neural nets are not.

### Pick the AWS AI service (pre-trained, no ML skill)
| Need | Service | Trap |
|---|---|---|
| Image/video: objects, faces, moderation, celebrities | **Rekognition** | Not for text docs |
| Extract text, forms, tables from scans/PDFs | **Textract** | vs Rekognition text-in-image; vs Comprehend (analyzes text, doesn't extract it) |
| Sentiment, entities, key phrases, language, PII in text | **Comprehend** | Medical text → **Comprehend Medical** |
| Speech → text | **Transcribe** | vs Polly (reverse) |
| Text → speech | **Polly** | |
| Translate languages | **Translate** | |
| Chatbot (voice/text), intents/slots | **Lex** | Not for doc search |
| Enterprise search over docs with NL answers | **Kendra** | Lex = conversation; Kendra = search |
| Recommendations / personalization | **Personalize** | |
| Time-series forecasting | **Forecast** | |
| Fraud detection | **Fraud Detector** | |
| Contact center AI | **Connect** (+ Contact Lens analytics) | |
| Code suggestions / dev assistant | **Amazon Q Developer** (formerly CodeWhisperer) | |
| Business assistant over company data | **Amazon Q Business** | Q Developer is for code |
| BI natural-language dashboards | **Amazon Q in QuickSight** | |
| Human review of low-confidence predictions | **Augmented AI (A2I)** | Not Ground Truth |
| Label data (humans + active learning) | **SageMaker Ground Truth** | vs A2I = review predictions |
| Medical transcription | **Transcribe Medical / HealthScribe** | |
| Document/data discovery of PII in S3 | **Macie** | not Comprehend |
| Detect industrial equipment anomalies | Lookout for Equipment / Monitron | |

---

## 2. Domain 2: Generative AI fundamentals

### Core vocabulary
| Term | Meaning | Trap |
|---|---|---|
| Foundation Model (FM) | Large pre-trained model adaptable to many tasks | Not task-specific |
| LLM | FM for text, built on **transformers** | |
| Transformer | Self-attention architecture | Not RNN-based |
| Token | Chunk of text; **billing and context limits are in tokens** | Not words |
| Embedding | Numeric vector capturing meaning | Similar meaning = close vectors |
| Context window | Max tokens input + output the model sees | Larger = more cost/latency |
| Diffusion model | Image generation by denoising | Stable Diffusion, Titan Image |
| GAN | Generator vs discriminator | Older approach |
| VAE | Encoder-decoder, latent space | |
| Multimodal | Handles several data types (text + image) | |
| Hallucination | Confident but false output | **Cannot be fully eliminated**; mitigate with RAG, grounding, guardrails, lower temperature |
| Prompt | Input instruction | |
| Non-determinism | Same prompt can differ run to run | |

### Inference parameters
| Parameter | Effect |
|---|---|
| **Temperature** ↑ | More random / creative. ↓ = focused, deterministic (use for factual or extraction tasks) |
| **Top-p** (nucleus) | Sample from smallest set of tokens whose cumulative prob ≥ p. Lower = less diverse |
| **Top-k** | Sample from the k most likely tokens. Lower = less diverse |
| **Max tokens / length** | Caps output length (cost control; truncation if too low) |
| **Stop sequences** | Tokens that end generation |
| Trap | None of these *teach* the model new knowledge. They only change sampling. |

### Prompt engineering
| Technique | Use | Trap |
|---|---|---|
| Zero-shot | No examples | |
| Few-shot | Provide examples in the prompt | No weights change, unlike fine-tuning |
| Chain-of-thought | "Think step by step" for reasoning | |
| Role / persona + system prompt | Set behaviour | |
| Negative prompting | Say what to avoid | |
| Prompt template | Reusable structure with variables | |
| **Prompt injection / jailbreak** | User overrides instructions | Mitigate: Guardrails, input validation, least privilege |
| Prompt leaking | Extracting the system prompt | |

### Lifecycle & customization ladder (cheapest → priciest)
1. Prompt engineering
2. **RAG** (add external knowledge at query time)
3. **Fine-tuning** (labeled prompt/response pairs; changes weights; needs **Provisioned Throughput** on Bedrock)
4. **Continued pre-training** (unlabeled domain data, e.g. legal corpus, to teach domain vocabulary)
5. Train from scratch (rarely correct)

| Choose | When |
|---|---|
| RAG | Fresh/private data, need citations, data changes often |
| Fine-tuning | Specific task/format/tone, labeled examples exist |
| Continued pre-training | Large **unlabeled** domain corpus |
| Distillation | Make a smaller cheaper model mimic a large one |
| Instruction tuning / RLHF | Align with human preference |

### FM evaluation
- **Human evaluation** for subjective quality; **Bedrock Model Evaluation** supports automatic (BLEU/ROUGE/BERTScore) and human/LLM-as-judge.
- **Benchmarks:** GLUE, SuperGLUE, MMLU, HELM, BIG-bench. Business metric > benchmark for real choice.
- Choose a model by: modality, quality, latency, cost, context length, language support, licensing, region availability.

---

## 3. Domain 3: Applications of foundation models (28%, the biggest)

### Amazon Bedrock traps
| Feature | What it is | Trap |
|---|---|---|
| Bedrock | Serverless API to FMs (Anthropic, Amazon Titan/Nova, Meta, Mistral, Cohere, AI21, Stability) | **Your data isn't used to train base models**; not in the AWS Marketplace sense |
| **Knowledge Bases** | Managed RAG (chunk, embed, store in vector DB, retrieve) | RAG ≠ fine-tuning |
| **Agents** | Multi-step task orchestration, calls APIs via **Action Groups** (Lambda + OpenAPI) | Not just chat |
| **Guardrails** | Content filters, denied topics, word filters, **PII redaction**, grounding check; works on input and output, any model | Not IAM |
| Model Evaluation | Compare models | |
| Provisioned Throughput | Reserved capacity; **required to run custom (fine-tuned) models**; commitment 1/6 months or no commitment | On-demand is for base models |
| On-demand | Pay per token, no commitment | |
| Batch inference | Cheaper for non-urgent large jobs | |
| Model customization | Fine-tune / continued pre-train | |
| Playground | Test prompts | |
| Prompt management / flows | Version prompts, build workflows | |
| Model Distillation | Smaller model from larger | |

### RAG architecture
`Docs → chunk → embed (Titan Embeddings/Cohere) → vector store → query embed → similarity search → augment prompt → LLM`
- Vector stores: **OpenSearch Serverless** (default for Bedrock KB), **Aurora PostgreSQL (pgvector)**, **RDS PostgreSQL pgvector**, Neptune Analytics, MemoryDB, DocumentDB, MongoDB Atlas, Pinecone, Redis Enterprise.
- Chunking too big = noisy retrieval; too small = lost context.
- RAG **reduces** hallucination, doesn't remove it. No retraining needed when docs change; just re-sync.
- Similarity metric: cosine / Euclidean / dot product (semantic search, not keyword).

### SageMaker (know the one-liners)
| Component | Job |
|---|---|
| **JumpStart** | Pre-trained models + notebooks; deploy/fine-tune open FMs |
| **Canvas** | No-code ML for analysts |
| **Studio / Notebooks** | IDE |
| **Data Wrangler** | Prepare/visualize data (low-code) |
| **Feature Store** | Reuse features across teams (online/offline) |
| **Ground Truth** | Labeling |
| **Clarify** | Bias detection + explainability (SHAP) |
| **Model Monitor** | Drift / data quality in production |
| **Model Cards** | Document model (intended use, risk) |
| **Model Registry** | Version/approve models |
| **Pipelines** | MLOps CI/CD workflows |
| **Experiments** | Track runs |
| **Autopilot / AutoML** | Auto-build models |
| **Role Manager** | Least-privilege personas |
| **Neo** | Optimize for edge |
| **Debugger** | Training issues |
| **Training Compiler / HyperPod** | Faster / resilient large-scale training |

**SageMaker JumpStart vs Bedrock:** Bedrock = serverless API, least overhead. JumpStart = more control, you host the endpoint.

### Compute & cost
- **Trainium** = training chips; **Inferentia** = inference chips (cheaper per inference). Don't swap.
- GPUs (P/G instances) for deep learning.
- Quantization / smaller models cut cost and latency.
- Cost levers: choose smaller model, shorten prompts, cap max tokens, caching, batch, Provisioned Throughput for steady load.
- Pricing models: pay-per-token (on-demand), provisioned (hourly), batch discount.

### Agents & orchestration
- Agent = LLM that plans, reasons (**ReAct**), calls tools, loops.
- **Bedrock AgentCore**, **Strands Agents** (open-source SDK), **Model Context Protocol (MCP)** for tool access, **Agent-to-agent (A2A)**.
- Memory: short-term (context) vs long-term (store).

### Application patterns (what to choose)
| Scenario | Answer |
|---|---|
| Chatbot over internal wiki, current data | Bedrock Knowledge Bases (RAG) |
| Chatbot that books travel via APIs | Bedrock Agents |
| Prevent toxic/PII output | Bedrock Guardrails |
| Summarize call transcripts | Transcribe + Bedrock |
| Semantic search | Embeddings + vector DB |
| Customer-specific tone from examples | Fine-tune |
| Compare 3 models for a task | Bedrock Model Evaluation |
| Generate images | Titan Image Generator / Stability |
| Natural language to SQL/BI | Q in QuickSight |
| Dev productivity | Q Developer |
| Stream long responses to UI | Bedrock `InvokeModelWithResponseStream` / Converse stream |

---

## 4. Domain 4: Responsible AI (14%)

### Dimensions of responsible AI
Fairness · Explainability · Privacy & security · Transparency · Veracity & robustness · Governance · Safety · Controllability.

| Concept | Meaning | Trap |
|---|---|---|
| **Bias** | Systematic unfairness from skewed data or design | Fixing it needs diverse/representative data, not just a bigger model |
| Types | Sampling, selection, measurement, historical, confirmation | |
| **Explainability** | Understand *why* a prediction was made | vs **Transparency** = disclosing how the system works/is built |
| **Interpretability** | Understand model internals (simple models) | |
| Fairness metrics | Disparate impact, demographic parity | Evaluate on subgroups |
| **Veracity** | Output is truthful/accurate | |
| **Robustness** | Resilient to bad/adversarial input | |
| Toxicity | Offensive output | Guardrails, filtering |
| Intellectual property | FM may reproduce copyrighted data | Legal risk |
| Environmental | Training has high energy use | |
| Human-in-the-loop | Human reviews decisions | A2I |

### Tools
| Need | Tool |
|---|---|
| Detect bias in data/model; SHAP explainability | **SageMaker Clarify** |
| Document model purpose/limits | **SageMaker Model Cards** |
| Review low-confidence outputs by humans | **Amazon A2I** |
| Filter harmful GenAI content | **Bedrock Guardrails** |
| Monitor quality/bias drift | **Model Monitor** |
| Track AI governance | **SageMaker Role Manager / Model Governance** |
| AWS transparency docs | **AWS AI Service Cards** |
| Data lineage | Glue Data Catalog / Lake Formation |

### Dataset hygiene
- Diversity, inclusivity, **curated sources**, balanced classes, representative of users; label quality checks.
- **Synthetic data** can augment under-represented groups but can also amplify bias.
- Model transparency trade-off: more accurate usually means less explainable.
- Mitigating **hallucination**: RAG, grounding, human review, lower temperature, citations. **Not** "bigger model."

---

## 5. Domain 5: Security, compliance, governance (14%)

### Shared responsibility
- **AWS:** infrastructure, hardware, managed service software (security **of** the cloud).
- **Customer:** data, IAM, encryption choices, prompts, app config, guardrails, who may use the model (security **in** the cloud).

### Services map
| Need | Service | Trap |
|---|---|---|
| Who can call Bedrock/which models | **IAM** policies (least privilege) | Guardrails ≠ access control |
| Private connectivity, no internet | **VPC endpoints / PrivateLink** | NAT/IGW still goes through internet |
| Encrypt at rest | **KMS** (customer-managed keys); S3 SSE | Bedrock encrypts by default |
| Encrypt in transit | **TLS** | |
| Audit API calls | **CloudTrail** | |
| Metrics, logs, alarms; Bedrock invocation logging | **CloudWatch** | CloudTrail = who did what; CloudWatch = performance/logs |
| Config compliance drift | **AWS Config** | |
| Find PII in S3 | **Macie** | |
| Threat detection | **GuardDuty** | |
| Vulnerability scanning | **Inspector** | |
| Secrets (API keys) | **Secrets Manager** | Not hard-coded |
| Compliance reports/agreements | **AWS Artifact** | Not Audit Manager |
| Automate audit evidence | **Audit Manager** | |
| Policy-wide guardrails across accounts | **Organizations SCPs** | |
| Best-practice review | **Trusted Advisor / Well-Architected** (has ML & GenAI lenses) | |
| Data governance & fine-grained lake access | **Lake Formation** | |
| Sensitive data masking in prompts | **Guardrails PII filter / Comprehend PII** | |

### Data & privacy rules
- Bedrock: prompts/completions **are not used to train** base FMs or shared with model providers. Fine-tuned copy is private to you.
- Apply **data minimization**, anonymization/masking, retention limits, encryption, and access control to training data.
- **Data residency / sovereignty**: pick the Region; note cross-region inference profiles can route elsewhere.
- Compliance frameworks: **GDPR** (EU privacy), **HIPAA** (health, BAA), **PCI DSS** (cards), **SOC**, **ISO 27001/42001** (42001 = AI management system), **NIST AI RMF**, **EU AI Act** (risk-tiered).
- Governance: data lineage, source citation, provenance, versioning, documentation, regular audits, review policies.

### GenAI-specific threats (OWASP LLM themes)
| Threat | Mitigation |
|---|---|
| Prompt injection / jailbreak | Guardrails, input sanitisation, least-privilege tool access |
| Sensitive data disclosure | PII redaction, access control, don't train on secrets |
| Data / model poisoning | Trusted sources, validate training data, lineage |
| Excessive agency | Limit agent permissions; human approval for risky actions |
| Insecure output handling | Validate/escape model output |
| Model theft / DoS | IAM, throttling, quotas |
| Supply chain | Vet third-party models/libs |

---

## 6. Top 25 "look-alike" pairs (the usual wrong-answer sources)

| # | Pair | Distinction |
|---|---|---|
| 1 | RAG vs fine-tuning | Facts that change vs behaviour/style |
| 2 | Fine-tuning vs continued pre-training | Labeled pairs vs unlabeled corpus |
| 3 | Guardrails vs IAM | Content safety vs access control |
| 4 | CloudTrail vs CloudWatch | Audit trail vs metrics/logs |
| 5 | Clarify vs Model Monitor | Bias/explain vs drift in prod |
| 6 | Ground Truth vs A2I | Label training data vs review predictions |
| 7 | Lex vs Kendra | Conversation vs enterprise search |
| 8 | Comprehend vs Textract | Understand text vs extract text |
| 9 | Rekognition vs Textract | Image/video content vs document structure |
| 10 | Polly vs Transcribe | TTS vs STT |
| 11 | Q Business vs Q Developer | Company knowledge vs coding |
| 12 | Bedrock vs JumpStart | Serverless API vs self-hosted models |
| 13 | Trainium vs Inferentia | Train vs infer |
| 14 | Precision vs recall | False positives vs false negatives |
| 15 | Overfit vs underfit | Memorise vs too simple |
| 16 | Temperature vs top-p/top-k | Randomness scaling vs candidate pool |
| 17 | Few-shot vs fine-tuning | Prompt examples vs weight updates |
| 18 | Explainability vs transparency | Why a decision vs how system is built/disclosed |
| 19 | Parameters vs hyperparameters | Learned vs set by you |
| 20 | Batch vs real-time inference | Offline bulk vs low-latency |
| 21 | On-demand vs Provisioned Throughput | Pay per token vs reserved (needed for custom models) |
| 22 | Artifact vs Audit Manager | Download AWS reports vs collect your evidence |
| 23 | Macie vs Comprehend | PII in S3 vs PII in text analysis |
| 24 | Model Cards vs AI Service Cards | Your model docs vs AWS service docs |
| 25 | Embedding vs token | Vector of meaning vs text chunk |

---

## 7. Extra edge cases worth a last look

| Edge case | Rule |
|---|---|
| "NOT" / "EXCEPT" / "LEAST" questions | Re-read the stem, find the three true statements, pick the false one. Mark them and recheck. |
| "Choose two/three" | Every chosen option must independently be correct. A half-right pair scores zero. |
| Drag-and-drop / ordering | Order by the stated axis (cost, effort, lifecycle stage). Don't reuse an item unless the stem allows it. |
| Guardrails apply to **inputs and outputs** | They block denied topics, harmful content, PII, and can check grounding. They don't replace IAM. |
| Fine-tuned model on Bedrock | Runs only on **Provisioned Throughput**. |
| Base-model data privacy | Your prompts/outputs aren't used to train base FMs. |
| RAG fixes stale knowledge | An LLM can't know events after its training cutoff. Retrieval adds current data. |
| Overfitting vs underfitting | Great on train and poor on new data = overfit. Poor on both = underfit. |
| Accuracy on imbalanced data | Misleading. Use precision, recall, F1. |
| Human in the loop | Prefer it for high-stakes decisions and low-confidence predictions (A2I). |
| Explainability tool | **Clarify** (SHAP) for features. Model Cards for documentation. |
| Compliance reports | **Artifact** downloads AWS reports. **Audit Manager** gathers your evidence. |
| Least privilege | The answer to most "who can access" questions: narrow IAM roles/policies, not broad admin. |
| Encryption | At rest = KMS. In transit = TLS. Private network path = PrivateLink / VPC endpoints. |
| Low latency + steady traffic | Real-time endpoint. Spiky/idle = serverless. Big offline = batch. |
| Cheapest customization | Try prompt engineering first, RAG second, fine-tune only if those fail. |
| Hallucination | Mitigate (RAG, grounding, low temperature, human review). Never "eliminate". |
| Absolute claims | "Guarantees", "always", "eliminates all" are almost always wrong. |

## 8. Gap-fill after checking all 5 domains

### Domain 1: algorithms, data prep, deployment
| Topic | Rule |
|---|---|
| Algorithm to task | Linear/logistic regression and **XGBoost** = tabular; **KNN** and **decision tree / random forest** = classification/regression; **K-Means** = clustering; **PCA** = dimensionality reduction; **CNN** = images; **RNN/LSTM/transformer** = sequences/text. |
| Ensembles | **Bagging** (random forest) reduces variance. **Boosting** (XGBoost) reduces bias by fixing prior errors. |
| Transfer learning | Reuse a pre-trained model for a new task with less data. Fine-tuning is a form of it. |
| Data cleaning | Handle **outliers**, missing values (**imputation**), duplicates. Do this before training. |
| Encoding | **One-hot** encoding turns categories into numbers. Normalization/standardization puts features on one scale. |
| Class imbalance | Oversample (e.g. SMOTE), undersample, or use F1/recall instead of accuracy. |
| Data augmentation | Create varied copies of existing data (flip/crop images) to boost data and robustness. |
| Text prep for NLP | **Tokenization** splits text. **Stemming/lemmatization** reduce words to roots. **TF-IDF** weights important words. **N-grams** capture phrases. |
| NLP vs computer vision | NLP = text/speech (Comprehend, Translate, Lex). Computer vision = images/video (Rekognition). |
| Deployment strategies | **Blue/green** = switch traffic between two environments. **Canary** = small share of traffic first. **Shadow** = copy traffic, not served. **A/B** = compare two live variants. |
| Where to run | Cloud for scale, **edge** (SageMaker Neo, IoT Greengrass) for low latency/offline, hybrid for both. |
| Learning toys | **DeepRacer** = reinforcement learning with a car. **DeepLens** = camera for deep-learning learning projects. |
| ML lifecycle frame | CRISP-DM style: business understanding, data, modelling, evaluation, deployment, monitoring. |

### Domain 2: GenAI
| Topic | Rule |
|---|---|
| Model families on Bedrock | **Claude** (Anthropic) text/multimodal, **Titan** and **Nova** (Amazon), **Llama** (Meta), Mistral, Cohere (also embeddings/rerank), AI21, Stability AI (images). |
| Tokenization in LLMs | Text becomes tokens before embeddings. Pricing and limits count tokens. |
| Pros of GenAI | Adaptability, speed, personalization, creativity. Cons: hallucination, nondeterminism, bias, cost, IP risk. |
| Business metrics for GenAI | Cross-domain performance, conversion rate, average revenue per user, efficiency, customer lifetime value. Not just model accuracy. |
| Interpretation of **LLM-as-a-judge** | A model scores another model's outputs on criteria such as correctness and faithfulness. Cheaper than human review, still verify. |

### Domain 3: FM applications
| Topic | Rule |
|---|---|
| Bedrock Flows / Prompt Management | Flows = visual workflow of prompts, KBs, agents. Prompt Management = versioned prompts. |
| Bedrock Data Automation | Extracts structured data from documents, images, audio and video. |
| Amazon Q Apps | Build small GenAI apps from conversation inside Q Business. |
| Evaluation of RAG | Check **faithfulness/groundedness** and retrieval relevance, not only answer fluency. |
| Kiro | Agentic IDE for spec-driven development. Q Developer remains the coding assistant answer. |
| Inference profile / cross-region | Routes requests across Regions for throughput. Mind data residency. |

### Domain 4: Responsible AI
| Topic | Rule |
|---|---|
| Privacy techniques | **Differential privacy** adds noise to protect individuals. **Federated learning** trains without moving raw data. Anonymize/mask before training. |
| Watermarking | Marks AI-generated content for provenance (Titan Image Generator adds invisible watermarks). |
| Responsible dataset | Inclusive, diverse, balanced, curated, with documented sources. |
| Transparency vs explainability | Transparency = how it was built and used. Explainability = why one output happened. |

### Domain 5: Security and governance
| Topic | Rule |
|---|---|
| Resource tagging | Tag AI resources for cost allocation, access control and governance. |
| Model invocation logging | Turn on in Bedrock to capture prompts/responses to CloudWatch Logs or S3 for audit. |
| Data governance strategies | Data lifecycle, logging, residency, monitoring, retention, source citation, lineage. |
| Standards | ISO 27001 (security), **ISO 42001** (AI management), SOC, NIST AI RMF, EU AI Act (risk tiers), GDPR, HIPAA. |

## 9. Weak-spot revision by exam task

Priority order after a self-assessment (lowest score first). Re-read the linked sections of this sheet in this order.

| Task | What to drill |
|---|---|
| **3.4 Evaluate FM performance** | Metric to task: ROUGE (summaries), BLEU (translation), BERTScore (semantic similarity), perplexity (fluency), F1/AUC (classification), MSE/RMSE (regression). Use human evaluation plus benchmarks, and check business outcomes (conversion, efficiency), not just model scores. |
| **1.2 Practical AI use cases** | Match the service to the need: Rekognition, Textract, Comprehend, Transcribe, Polly, Translate, Lex vs Kendra, Personalize, Forecast, Fraud Detector. Also know when **not** to use AI (simple rules suffice, no data). |
| **4.2 Transparent and explainable models** | Transparency = how it was built and used (Model Cards, AI Service Cards). Explainability = why one output (Clarify, SHAP). Interpretability = understandable internals. Simpler models are more explainable but may be less accurate. |
| **5.2 Governance and compliance** | Artifact vs Audit Manager, Config, CloudTrail, Macie, Lake Formation. ISO 42001, NIST AI RMF, EU AI Act, GDPR, HIPAA. Data lineage, retention, residency. |
| **3.1-3.3 FM design, prompting, training** | RAG vs fine-tuning vs continued pre-training, Provisioned Throughput for custom models, prompt techniques (zero/few-shot, chain-of-thought, negative prompts), temperature/top-p/top-k. |
| **2.3 AWS GenAI infrastructure** | Bedrock vs JumpStart, Trainium vs Inferentia, Knowledge Bases, Agents, Guardrails. |

## 10. Concept clarifications (frequently confused ideas)

General concepts that are easy to confuse. They are original one-line rules, not questions, scenarios or answer options from any exam or course.

| Concept | Rule to remember |
|---|---|
| N-grams | A window of n slides one word at a time, so 3 words give trigrams ("w1 w2 w3", "w2 w3 w4"...). Not single words or non-overlapping chunks. |
| Serverless inference | Idle periods between traffic spikes and tolerable cold starts: choose **Serverless Inference**, not an always-on real-time endpoint. |
| ROUGE | Summarization quality. BLEU is translation. |
| Controlling answer length | Specify the format in the prompt and give examples. Capping max tokens only truncates the output. |
| Hyperparameter tuning vs training | Grid/random/Bayesian search tune hyperparameters. **Gradient descent** optimizes weights during training; it is not a hyperparameter search method. |
| Quantization | Converts weights from high to lower precision (32-bit to 16/8-bit): smaller, faster, cheaper. |
| Distillation | Small student learns from large teacher. Don't swap with quantization. |
| Forward diffusion | The step that adds noise. Generation is the reverse (denoising) step. |
| Knowledge cutoff | A model not knowing recent events is a training-data cutoff, not hallucination. Fix with RAG or retrieval. |
| Shadow deployment | New model version runs in parallel on live traffic without serving its answers, to compare safely. |
| CloudWatch for Bedrock apps | Operational monitoring (latency, errors, invocation logs). CloudTrail is for who called what. |
| AutoML (SageMaker Autopilot/Canvas) | Automates algorithm choice, feature handling and tuning for fast model building. |
| RAG vector stores | Besides OpenSearch/Aurora pgvector, Amazon S3 Vectors can now store embeddings. |
| Decision tree | A classification/regression model that is easy to explain. |
| Human oversight | In high-stakes or sensitive uses, fully removing human review is the weak design. Keep a human in the loop. |
| Cross-account access | Use IAM roles and resource policies for controlled access, not shared long-lived keys. |
| Instruction-based fine-tuning | Needs **prompt/response pairs**. Raw unlabeled documents are not the input. |
| Continued pre-training | Many **unlabeled** domain documents (legal, medical) to teach vocabulary and context. Labeled pairs mean fine-tuning. |
| Transcribe custom terms | **Custom vocabulary** for specific words and their display form. A custom language model suits much larger domain text. |
| Well-Architected ML Lens | The lifecycle starts with **business goal identification**, then data, model, deploy, monitor. |
| SageMaker Inference Recommender | Automates load testing to choose instance type and endpoint config. |
| Real-time endpoint | Low-latency responses with steady traffic. Not batch, not serverless. |
| Batch Transform | Large datasets, no immediate response needed. |
| Data Wrangler vs Pipelines | **Data Wrangler** = low-code data prep. **Pipelines** = orchestrate ML workflow steps. |
| Unsupervised vs supervised | **K-Means** is unsupervised clustering. **Linear regression** predicts a continuous number. |
| Ground Truth | Labels data (humans and automation). It does **not** train models. |
| Bedrock Playground / PartyRock | Playground to test prompts and models. PartyRock = no-code GenAI app builder. |
| Prompt engineering | Improves the **input** to a pre-trained model, not its weights. |
| Customization cost order | Prompt engineering, RAG, fine-tuning, continued pre-training, training from scratch (cheapest to priciest). |
| Metric purpose | F1 = classification balance. MSE = regression error. Perplexity = language model fluency. BERTScore = semantic similarity. |
| Embeddings | A vector database query is converted to an **array of numbers**, then similarity-searched. |
| Jailbreaking | Tricking the model into producing disallowed content. |
| Interpretability | Humans can understand the model's inner workings (vs explainability = why a given output). |
| Bias test: prompt stereotyping | Checks whether a model encodes stereotypes across prompt variations. |
| Prompt-attack kinds | Attacks may switch the persona, override instructions, or try to extract the system prompt or history. |
| Bedrock monitoring | **CloudWatch** for health/performance. Invocation logging goes to a CloudWatch Logs log group (or S3). |
| AUC | Compare classifiers across all thresholds, independent of one cutoff. |
| JumpStart | Browse and deploy many pre-built models and algorithms inside SageMaker. |
| Comparing FMs | Combine **human evaluation** with **benchmark datasets**. One alone misses quality or comparability. |
| Fine-tuning data | Must reflect the real-world distribution the model will see, and be clean and representative. |
| Top-p / top-k | Filter out low-probability tokens from sampling. |
| Prompt leaking defences | Sanitize and validate inputs, and filter outputs. Both directions. |
| Jailbreak risk | The main concern is output that violates policy or safety rules. |
| Data protection basics | **TLS/HTTPS** in transit and **server-side encryption** at rest. |
| BLEU/ROUGE use | Text summarization and machine translation. |
| Computer vision | Image/video understanding tasks: pick it for visual content. |
| Bedrock latency factors | Provisioned throughput, model size and complexity, and network latency between app and model. |
| Bedrock benefits | Lower cost and complexity, and managed access to many FMs. It does not guarantee the best accuracy and does not remove your responsibility for ethical use. |

## 11. Final-hour checklist

- [ ] Can I name the AI service for each of: image, doc, text, speech, translate, chatbot, search, recommend, forecast, fraud?
- [ ] RAG vs fine-tuning vs continued pre-training, with a trigger phrase for each
- [ ] Precision/recall/F1/AUC/BLEU/ROUGE/BERTScore: which when?
- [ ] Temperature, top-p, top-k, max tokens effects
- [ ] Bedrock: Knowledge Bases, Agents, Guardrails, Provisioned Throughput, Model Evaluation
- [ ] SageMaker: Clarify, Model Monitor, Model Cards, Ground Truth, A2I, JumpStart, Canvas
- [ ] Shared responsibility and who owns what
- [ ] IAM / KMS / PrivateLink / CloudTrail / Macie / Artifact roles
- [ ] Responsible AI dimensions and tools
- [ ] Hallucination is **mitigated, never eliminated**; "guarantees" answers are wrong
- [ ] Answer every question; flag and return; watch the clock (~80 s per question)

> Tip: AWS adds and renames services (for example CodeWhisperer became Q Developer). Verify any single name against the current official exam guide.

---
**Integrity note:** use this sheet to learn concepts. Do not share, request or trade actual exam content: it breaks the AWS Certification Program agreement and can lead to a banned certification.
