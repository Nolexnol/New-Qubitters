# Product Requirements Document (PRD)

**Project Name:** MTS LABS PHASE 1 FILE
**Team Name:** NEW QUBITTERS
**GitHub Repository:** [https://github.com/Optimus2007/New-Qubitters]

---

> **Note to Students:** > The questions and examples provided in the specific sections below are **prompts to guide your thinking**, not a rigid checklist. 
> * **Adaptability:** If a specific question doesn't fit your strategy, you may skip or adapt it.
> * **Depth:** You are encouraged to go beyond these examples. If there are other critical technical details relevant to your specific approach, please include them.
> * **Goal:** The objective is to convince the reader that you have a solid plan, not just to fill in boxes.

---

## 1. Team Roles & Responsibilities [You can DM the judges this information instead of including it in the repository]

| Role | Name | GitHub Handle | Discord Handle
| :--- | :--- | :--- | :--- |
| **Project Lead** (Architect) | [Aditya Raj] | [https://github.com/Optimus2007] |
| **GPU Acceleration PIC** (Builder) |[Muhammad Khizar] | [https://github.com/GHOST-Q1]
| **Quality Assurance PIC** (Verifier) | [Noble Agyeman-Bobie][ https://github.com/nolexnol],[Gbenga Oyeniyi][https://github.com/oyeniyi-gbenga],[Ravi Chandra Varma] | [https://github.com/kcravi912]
| **Technical Marketing PIC** (Storyteller) | [Muhammad Khizar] | [https://github.com/GHOST-Q1] | [@handle] |

---

## 2. The Architecture

### Choice of Quantum Algorithm
* **Algorithm:** QAOA with respect to MTS requirements


* **Motivation:**[Correlation with MTS and LABS, A defined Algorithm for optimization and combinational problems]Quantum Approximate Optimization Algorithm is a hybrid quantum-classical algorithm for finding approximate solutions to complex combinatorial optimization problems, using a quantum computer to explore potential solutions and a classical computer to refine parameters
   

### Literature Review
* **Reference:** "Evidence of Scaling Advantage for the Quantum Approximate Optimization Algorithm on a Classically Intractable Problem" (arXiv:2308.02342, August 2023). Ruslan Shaydulin, Changhao Li, Shouvanik Chakrabarti, Matthew DeCross, Dylan Herman, Niraj Kumar, Jeffrey Larson, Danylo Lykov, Pierre Minssen, Yue Sun, Yuri Alexeev, Joan M. Dreiling, John P. Gaebler, Thomas M. Gatterman, Justin A. Gerber, Kevin Gilmore, Dan Gresh, Nathan Hewitt, Chandler V. Horst, Shaohan Hu, Jacob Johansen, Mitchell Matheny, Tanner Mengle, Michael Mills, Steven A. Moses, Brian Neyenhuis, Peter Siegfried, Romina Yalovetzky, Marco Pistoia, 2023.
* **Relevance:** 
     Numerical investigation of QAOA on the low autocorrelation binary sequences (LABS) problem, which is classically intractable even for moderately sized instances. We will be using the concept from this paper to efficiently solve our problem. With fixed parameters, i.e. a defined sequence
---

## 3. The Acceleration Strategy
**Owner:** GPU Acceleration PIC

### Quantum Acceleration (CUDA-Q)
* **Strategy:** A QAOA Ansatz which is hardware efficient, We are yet to decide the nvidia gpu we use, but most certainly noise will be avoided. We will run a single step first instead of a list of sequences


### Classical Acceleration (MTS)
* **Strategy:** 
    "The standard MTS evaluates neighbors one by one. We will use `cupy` to rewrite the energy function to evaluate a batch of 1,000 neighbor flips simultaneously on the GPU."

### Hardware Targets
* **Dev Environment:** Qbraid (CPU) or local machine for logic, Brev L4 for initial GPU testing]
* **Production Environment:** TBD

---

## 4. The Verification Plan
**Owner:** Quality Assurance PIC

### Unit Testing Strategy
* **Framework:** PyTest
* **AI Hallucination Guardrails:** [How do you know the AI code is right?]
 By Step by step verification done by each member with respect to a refernce solution to make sure that our outputs and results are not inaccurate.

### Core Correctness Checks
* **Check 1 (Symmetry):** [Describe a specific physics check]
    * *Example:* "LABS sequence $S$ and its negation $-S$ must have identical energies. We will assert `energy(S) == energy(-S)`."
* **Check 2 (Ground Truth):**
    * *Example:* "For $N=3$, the known optimal energy is 1.0. Our test suite will assert that our GPU kernel returns exactly 1.0 for the sequence `[1, 1, -1]`."

---

## 5. Execution Strategy & Success Metrics
**Owner:** Technical Marketing PIC

### Agentic Workflow
* **Plan:** [How will you orchestrate your tools?]
    * *Example:* "We are using Cursor as the IDE. We have created a `skills.md` file containing the CUDA-Q documentation so the agent doesn't hallucinate API calls. The QA Lead runs the tests, and if they fail, pastes the error log back into the Agent to refactor."

### Success Metrics
* **Metric 1 (Approximation):** [e.g., Target Ratio > 0.9 for N=30]
* **Metric 2 (Speedup):** [e.g., 10x speedup over the CPU-only Tutorial baseline]
* **Metric 3 (Scale):** [e.g., Successfully run a simulation for N=40]

### Visualization Plan
* **Plot 1:** [e.g., "Time-to-Solution vs. Problem Size (N)" comparing CPU vs. GPU]
* **Plot 2:** [e.g., "Convergence Rate" (Energy vs. Iteration count) for the Quantum Seed vs. Random Seed]

---

## 6. Resource Management Plan
**Owner:** GPU Acceleration PIC 

* **Plan:** [How will you avoid burning all your credits?]
    * *Example:* "We will develop entirely on Qbraid (CPU) until the unit tests pass. We will then spin up a cheap L4 instance on Brev for porting. We will only spin up the expensive A100 instance for the final 2 hours of benchmarking."
    * *Example:* "The GPU Acceleration PIC is responsible for manually shutting down the Brev instance whenever the team takes a meal break."
