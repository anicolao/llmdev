# Case Study: anicolao/diku
## LLM-Powered MUD Player Development Journey

**Repository:** [anicolao/diku](https://github.com/anicolao/diku)  
**Description:** A Diku MUD player that uses LLM APIs to play text adventure games autonomously  
**Language:** JavaScript (Node.js)  
**Created:** September 24, 2025  
**Development Period:** ~5 days (Sept 24-29, 2025)  
**Total Issues:** 30 issues (28 closed, 2 open)  
**Project Scope:** AI-powered game playing client with TUI interface  

**Analysis Date:** October 22, 2025  
**Analysis Method:** Manual analysis of GitHub issues (API rate limits prevented automated analysis)

---

## Executive Summary

The diku repository represents a **unique case study in AI building AI** - using GitHub Copilot to create an LLM-powered autonomous game player. This meta-project demonstrates rapid iteration cycles with **30 GitHub issues processed in ~5 days** (~6 issues/day).

**What Makes This Special:**
- **Meta AI Development**: Using Copilot to build a system that uses LLMs (Ollama/OpenAI) to play games
- **Extremely rapid iteration**: 30 issues in 5 days shows aggressive development pace
- **Progressive enhancement**: Clear evolution from basic concept to sophisticated TUI application
- **Problem-solving under constraints**: System prompt complexity, model capability limitations

**Key Statistics:**
- **30 total issues** (28 closed, 2 open as of Sept 29)
- **~6 issues/day** average velocity
- **100% Copilot-driven** (all issues tagged as Copilot tasks)
- **Rapid turnaround**: Most issues closed same day

---

## The Development Story Arc

### Phase 1: Vision & Initial Design (Sept 24, Day 1)

#### Issue #1: Project Foundation
**Original Prompt:**
> "The goal of this project is to create a Diku MUD player that uses the ollama API to get responses from an Ollama LLM and successfully play a Diku MUD. The specific MUD I am thinking of is arctic. Write a README.md for this repository and propose an INITIAL_DESIGN.md for how to implement the MUD client."

**Additional Requirements:**
- Document all prompts in PROMPTS.md for future reference
- Record every commit's prompt and issue number

**Key Insight:** The developer established a "prompts as documentation" pattern from day 1, creating a meta-record of the development process itself.

**Result:** Foundation documents created - README, INITIAL_DESIGN, PROMPTS tracking system established.

### Phase 2: Basic Implementation (Sept 24, Days 1-2)

#### Issue #3: TUI Implementation
**Prompt:** "Modify UI to use a fancier TUI layout, with a window for Diku interaction in dark mode, and status and debug messages in other panels. User should hit enter to accept each command."

**Pattern:** Moving from basic console to sophisticated terminal UI
- Multi-panel layout
- Dark mode aesthetics
- User approval workflow for debugging

#### Issue #5: Copilot Instructions Setup
**Pattern:** Establishing development best practices early
- Shows meta-awareness of using Copilot effectively
- Building scaffolding for better AI collaboration

### Phase 3: TUI Refinement (Sept 24, Days 2-3)

#### Issue #7: Layout Improvements
**Problem:** "Text isn't properly cleared, messages garbled, box too small"
**Solution:** Reorganize to wide left column (main output + debug), narrow right column (LLM status + user input)

**Iteration Pattern:** Visual/UX issues discovered through actual use, fixed iteratively

#### Issue #9: Character Memory System
**Problem:** "Bot/LLM can't remember usernames created"
**Approach:** Request design doc only (CHARACTER.md) for review before implementation

**Key Pattern:** **Design-first for complex features** - Same pattern seen in dikuclient case study

### Phase 4: Core Functionality (Sept 24-25)

#### Issue #11 & #13: Character Management Implementation
**Prompt:** "Read CHARACTER.md and implement what is described, no more or less"

**Pattern:** Human reviews design, approves, then Copilot implements exactly as specified
- Separation of design and implementation phases
- Clear scope boundaries

### Phase 5: LLM Interaction Refinement (Sept 25-26)

Series of rapid issues improving LLM prompt engineering:

#### Issue #15: NPC Interaction Help
**Problem:** "LLM having trouble interacting with characters"
**Solution:** Add system prompt instructions to send 'help' command first, stick to suggested vocabulary

#### Issue #17: Command Format Issues  
**Problem:** LLMs generating natural language ("ask girl for guide") instead of keywords ("ask girl guide")
**Solution:** Rewrite system prompt to emphasize keyword-driven commands vs natural language

#### Issue #19: Model Capability Limits
**Recognition:** "OSS models too small/incapable of solid instruction following"
**Solution:** Add OpenAI API support alongside Ollama for more capable models

**Key Insight:** The developer recognized when the problem was model capability, not code - and expanded model options rather than fighting the limitation.

### Phase 6: Context & Prompt Engineering (Sept 25)

#### Issue #21: Context Window Management
**Problem:** "Context window too small"
**Solution:** Replace "10 most recent messages" with token-based estimation (<100k tokens), remove oldest messages except system prompt

**Pattern:** Scaling strategy - move from simple heuristics to proper resource management

#### Issue #23: Scrolling & Logging
**Problem:** "TUI doesn't support scrolling panels"
**Solution:** Add `mouse: true` and `keys: true`, create log files `logs/<panelname>.<date>.log`

**Pattern:** Observability - make everything reviewable later

#### Issue #25 & #27: Game State Understanding
**Issue #25:** Remove ANSI escape sequences interfering with client
**Issue #27:** Add prompt explaining game status format ("56H 118V 1499X 0.00% 0C T:60")

**Pattern:** Teaching the LLM to understand the game's language and conventions

### Phase 7: Interaction Improvements (Sept 25)

#### Issue #29 & #31: Input Handling
**#29:** Interpret literal commands 'return'/'enter' as newline
**#31:** Display login banner instead of hardcoded prompt

**Pattern:** Handling edge cases discovered through actual gameplay

#### Issue #33: Response Queueing
**Problem:** "Each new game output sends new LLM request → repetitive actions, failure to react"
**Solution:** Queue MUD messages while LLM response pending, only prompt after command sent and response received

**Key Pattern:** **Async state management** - Don't spam the AI, give it time to think and act

### Phase 8: World Navigation (Sept 25-27)

#### Issue #39: Pager Handling
**Problem:** "Game prompting with pager [press return for more; q to quit], LLM ignoring it"
**Solution:** Update prompt so LLM knows to only send commands to `>` prompts, obey `[]` options

#### Issue #41: Display Corruption
**Problem:** "Garbage characters in LLM status box"
**Status:** Open issue - ongoing problem with text rendering

#### Issue #43: Pathfinding Assistance
**Problem:** "LLMs having trouble remembering paths and pathfinding"
**Solution:** Suggest solutions (likely graph-based navigation system)

#### Issue #45: Auto-Exit Detection
**Problem:** "Room connectivity often wrong due to failed movements, LLM sitting, etc"
**Solution:** Never label exits from movement attempts, auto-send 'exits' command in each new room, parse output to build graph, correct previous room IDs

**Pattern:** **Don't trust inference, verify explicitly** - Auto-query for ground truth

### Phase 9: Advanced Navigation (Sept 27-29)

#### Issue #47: Backup Strategy
**Problem:** Character data backup approach
**Solution:** Log rotation style (characters.json.1 through .9, oldest discarded)

#### Issue #49: Library Switch Attempt
**Problem:** Screen corruption issues
**Attempted Solution:** Switch from `blessed` to `ncurses` library
**Status:** Closed but issue #41 suggests problem persists

#### Issue #51: Room ID Disambiguation
**Problem:** "Multiple rooms with same name confuse wayfinding"
**Solution:** Make ID = `title + first_sentence + exits_abbreviation` (e.g., `sample_room_this_would_be_a_boring_sample_room_NEW`)
**Instruction:** "DO NOT write backward compatibility code, just implement new scheme"

**Pattern:** **Break backward compatibility for correctness** when necessary

### Phase 10: Polish & Cleanup (Sept 29)

#### Issue #53 & #55: Debug Output Routing
**#53:** Route character_manager.js logs to debug panel
**#55:** Find/replace ALL console.log/error to TUI debug panel, verify with `git grep console`

**Pattern:** **Cleanup sweeps** - Systematic elimination of technical debt

#### Issue #57: Repository Trimming
**Prompt:** "Trim repository: remove all demo code, all backward compatibility code. Keep only tests of production code and production code itself"

**Pattern:** **Aggressive pruning** - Keep codebase lean and focused

#### Issue #59: System Prompt Simplification
**Problem:** "System prompt too long and complicated"
**Goal:** "Make it possible for smaller models to successfully play the game"
**Approach:** Review and reorganize, add planning instructions for smaller LLMs
**Status:** Open - current focus

---

## Prompt Analysis

### Most Effective Prompt Patterns

#### 1. **Problem-Context-Solution Pattern**
**Example (Issue #51):**
```
Problem: Multiple rooms with same name
Context: Wayfinding confused by title-only IDs  
Solution: Include title + first sentence + exits
```
**Why Effective:** Clear problem definition + concrete solution approach

#### 2. **Scope Control Pattern**
**Example (Issue #9):**
"Write *only* the design document, CHARACTERS.md, for review and approval"

**Why Effective:** Prevents over-implementation, enables human review before committing to approach

#### 3. **Verification Pattern**
**Example (Issue #55):**
"`git grep console` should find nothing when change is complete"

**Why Effective:** Provides concrete success criteria

#### 4. **Explicit Constraint Pattern**  
**Example (Issue #51):**
"**DO NOT** write code for backward compatibility, just implement the new scheme"

**Why Effective:** Prevents Copilot from over-engineering when simplicity is desired

### Prompt Evolution Over Time

**Early prompts (Issues #1-#10):** Vision and architecture focused
- Establishing project structure
- Choosing frameworks and approaches
- Setting up development patterns

**Mid-project (Issues #11-#35):** Feature implementation and refinement
- Implementing designed features
- Fixing integration issues
- Improving UX based on usage

**Late-project (Issues #37-#59):** Optimization and polish
- Addressing edge cases
- Improving LLM prompt engineering
- Cleaning up technical debt
- Optimizing for smaller models

---

## Iteration Patterns

### Quick Wins (Single-Day Issues)
Most issues closed same day they were opened, suggesting:
- Clear problem definitions
- Well-scoped changes
- Effective prompts
- Rapid Copilot turnaround

### Complex Issues (Multi-Step)
**Issue #43 (Pathfinding):** Required suggestion phase
**Issue #45 (Auto-exit):** Complex solution with multiple components
**Issue #51 (Room IDs):** Backward-incompatible redesign

### Open Issues (Struggling)
**Issue #41:** Display corruption - tried library switch (Issue #49), still not resolved
**Issue #59:** System prompt complexity - current focus, attempting to enable smaller models

**Pattern:** When issues stay open, it's usually **architectural challenges** or **external limitations** (model capability), not simple bugs

---

## Development Patterns

### 1. **Design-First for Complex Features**
- Issue #9: Request design doc before implementation
- Prevents wasted work on wrong approach
- Enables human review and approval

### 2. **Aggressive Iteration Velocity**
- ~6 issues/day average
- Most issues closed same day
- Rapid feedback loops with the MUD game

### 3. **Meta-Documentation**
- PROMPTS.md tracks every prompt used
- Creates learning artifact for future reference
- Shows awareness of building knowledge base

### 4. **Progressive Enhancement**
- Started simple (console output)
- Added TUI (Issue #3)
- Enhanced with panels and logging (Issue #23)
- Refined interaction patterns (Issues #29, #31, #33)

### 5. **Test-Driven Development via Actual Use**
- Many issues discovered by actually playing the game
- Real-world testing reveals edge cases
- Feedback loop: play → discover issue → fix → play

### 6. **Cleanup Sweeps**
- Issue #55: Systematic console.log removal
- Issue #57: Remove all demo and backward-compat code
- Keep codebase clean and maintainable

### 7. **Recognizing Fundamental Limitations**
- Issue #19: Recognized OSS model limitations, added OpenAI option
- Issue #59: Attempting to simplify for smaller models
- Shows pragmatism over stubbornness

---

## What Went Well

### 1. **Rapid Development Pace**
30 issues in 5 days is exceptional velocity. The combination of:
- Clear, well-scoped prompts
- Copilot's implementation speed
- Quick human feedback/approval
Created a highly efficient development cycle.

### 2. **Progressive Complexity**
Started simple, added sophistication iteratively:
- Console → TUI → Multi-panel TUI
- Simple commands → Context management → Path finding
- Single model (Ollama) → Multiple options (OpenAI)

### 3. **Meta-Awareness**
The PROMPTS.md tracking and Issue #5 (Copilot instructions) show the developer thinking about the AI development process itself, optimizing collaboration.

### 4. **Design-First When It Matters**
Issue #9's "design doc only" approach prevented implementation churn on character memory system.

### 5. **Concrete Success Criteria**
Prompts like "git grep console should find nothing" provide unambiguous verification.

---

## Challenges & Learning

### 1. **LLM Prompt Engineering is Hard**
Issues #15, #17, #27, #39, #59 all relate to getting the LLM player to understand the game correctly.

**Learning:** Teaching an LLM to play a game is harder than teaching it to write code. Game-playing requires:
- Understanding domain-specific conventions
- State management across many turns
- Planning and strategy
- Adapting to unexpected situations

### 2. **Model Capability Ceiling**
**Issue #19:** OSS models struggling with instruction following
**Issue #59:** System prompt too complex for smaller models

**Learning:** Sometimes the solution isn't better code, it's a more capable model. But there's still value in optimizing for smaller models (cost, latency, privacy).

### 3. **Display Rendering Issues**
**Issue #41:** Still unresolved display corruption
**Issue #49:** Library switch didn't solve it

**Learning:** Some problems are deeply technical and resist quick fixes. The TUI rendering issue persisted despite multiple attempts.

### 4. **Async State Management Complexity**
**Issue #33:** Preventing LLM request spam required careful queuing logic

**Learning:** AI agents operating in real-time environments need thoughtful async handling to avoid race conditions and resource waste.

### 5. **World Model Accuracy**
**Issue #45:** Inferring room connectivity from movement was unreliable

**Learning:** **Don't trust inference when you can verify** - Explicitly query for ground truth (exits command) rather than guessing.

---

## Best Practices Demonstrated

### 1. **Scope Control**
Use "design doc only" or "no more, no less" to prevent over-implementation.

### 2. **Verifiable Success Criteria**
Provide commands to verify completion: "git grep X should find nothing"

### 3. **Explicit Constraints**
State what NOT to do: "DO NOT write backward compatibility code"

### 4. **Iterative Refinement**
Start simple, enhance progressively based on actual usage feedback.

### 5. **Meta-Documentation**
Track prompts and decisions for future learning and reference.

### 6. **Problem Recognition**
Know when the issue is model capability vs code quality, choose appropriate solution.

### 7. **Aggressive Cleanup**
Periodically sweep for technical debt (console.log removal, demo code deletion).

---

## Key Takeaways

### For Developers Using AI Tools:

1. **Fast iteration beats perfect planning** - 30 issues in 5 days shows small, frequent changes work better than big bangs

2. **Prompt specificity matters** - Compare vague "fix the layout" vs specific "put it on the right as narrow box"

3. **Test in real usage** - Many issues discovered by actually using the MUD player, not theorizing

4. **Design-first for complexity** - Request design docs for complex features before implementation

5. **Provide verification criteria** - "git grep should find nothing" is better than "remove all console.log"

6. **Know your model's limits** - When OSS models struggle, consider more capable models rather than endless code tweaking

7. **Document your prompts** - Future you (and others) will thank you for the PROMPTS.md

### For AI-Assisted Development:

1. **Meta-projects are viable** - Using AI to build AI systems works, but has unique challenges

2. **Prompt engineering for agents is different** - Teaching an LLM to play a game is harder than teaching it to write code

3. **Progressive enhancement works** - Start with MVP, add sophistication based on real feedback

4. **Cleanup matters** - Periodic sweeps for technical debt keep codebase maintainable

5. **Explicit beats implicit** - Auto-query for exits rather than inferring from movement

---

## Comparison with dikuclient

Both projects by the same developer, different domains:

**Similarities:**
- 100% Copilot-driven development
- Rapid iteration velocity (3.5-6 PRs/issues per day)
- Design-first approach for complex features
- Progressive enhancement strategy
- Meta-awareness (prompts tracking, Copilot instructions)

**Differences:**

| Aspect | dikuclient | diku |
|--------|-----------|------|
| **Domain** | MUD client for humans | MUD player for LLMs |
| **Complexity** | Terminal UI + WebSocket proxy | LLM prompt engineering + game AI |
| **Development Period** | 18 days | 5 days |
| **Work Units** | 63 PRs | 30 Issues |
| **Scope** | ~20K lines Go | Smaller, more experimental |
| **Main Challenge** | Feature implementation | LLM behavior control |
| **Open Issues** | Few, mostly complete | 2 open, ongoing challenges |

**Insight:** Building software **for humans** (dikuclient) was more straightforward than building software **for AI to use** (diku). The diku project struggled with prompt engineering complexity and model capability limits - challenges unique to meta-AI development.

---

## Conclusion

The diku repository demonstrates that **rapid, iterative AI-assisted development** is viable even for complex, novel domains like building AI game players. The project achieved remarkable velocity (30 issues in 5 days) through:

- Clear, specific prompts with concrete success criteria
- Progressive enhancement from MVP to sophisticated features
- Design-first approach for complex features
- Real-world testing driving iterative improvements
- Pragmatic recognition of model capability limits

The ongoing challenges (Issue #59 - system prompt complexity, Issue #41 - display corruption) show that some problems resist quick solutions, particularly when they involve fundamental architectural questions or external constraints.

**For the broader community:** This case study shows both the power and limits of AI-assisted development. When problems are well-defined and verifiable, AI can move incredibly fast. When problems involve "teaching AI to teach AI" or dealing with complex async state management in real-time systems, more iteration and human insight are required.

The developer's practice of documenting every prompt in PROMPTS.md creates a valuable learning artifact, showing that the best AI-assisted development isn't just about writing code - it's about building knowledge and understanding of how to collaborate effectively with AI tools.

---

## Appendix: Methodology

This case study was created through manual analysis of the anicolao/diku repository's GitHub issues due to API rate limiting. The analysis:

- Reviewed all 30 GitHub issues (28 closed, 2 open)
- Traced development from Issue #1 through Issue #59
- Identified patterns in prompts, iterations, and solutions
- Compared with dikuclient case study for cross-project insights
- Focused on actionable learnings for other developers

**Limitations:** Without automated deep analysis (rate limit prevented tool usage), some metrics like exact commit counts per issue, time-to-close distributions, and detailed prompt effectiveness scoring are not available. The analysis relies on manual review of issue descriptions and their stated prompts.

**Future Work:** When rate limits allow, running the llmdev deep analysis tool on this repository would provide:
- Quantitative iteration metrics
- Prompt effectiveness scoring
- Detailed timeline analysis
- Commit-level pattern detection
