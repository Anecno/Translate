---
name: translate-v2
description: "Codex workflow localized multi-agent serial relay translation skill. Trigger only for explicit translation work: '翻译这段', '把 X 翻成 Y', 'translate to', '古文今译', '汉译日', or a source text/file plus target language. Do not trigger for discussing the skill/spec, implementing Phase work, code changes, or general terminology explanations."
metadata:
  status: public-draft
  phase: 1
  version: "0.3.12-public-original-preserved"
  current_spec: spec-v0.3.12.md
  localized_from: <upstream-skill-source>
  localized_for: <codex-runtime-dir>
  updated: 2026-06-29
---

# translate-v2 — Codex Fork Entry

This is a public Codex workflow copy of the upstream `translate-v2` skill. The core
translation algorithm remains `spec-v0.3.12.md`; this file only adapts the
runtime controller, paths, memory boundaries, and whiteboard protocol for the
Codex-led workflow.

Project companion boundary: Antique Game Within Game / 《古董局中局》 may provide
canon and context; `translate-v2` remains authoritative for relay topology,
scoring, checkpoints, convergence, and artifact schemas.

## 0. Trigger Boundary

Use this skill only when the user is asking for real translation work:

- "翻译这段..." / "翻译以下文本"
- "把 X 翻成 Y" / "X 译 Y" / "汉译日" / "日译汉" / "中译英"
- "translate this to ..." / "translate the following"
- "古文今译" / "今译古文" / "白话译文言"
- A source text or file path plus a target language

Do not trigger for:

- Discussing this skill, its spec, phases, implementation, or migration
- General word lookup, terminology explanation, or commentary without a source
  text to translate
- Code work related to translation tooling

## 1. First Action

Before running a translation relay, read:

1. `NOTES.md` if present.
2. This `SKILL.md` for Codex workflow runtime differences.
3. `spec-v0.3.12.md` for the translation algorithm and output schemas.

Do not use other files in this directory as execution authority unless the
user explicitly asks for historical audit. In particular, `SKILL-v0.1.md`,
`spec-v0.1.md` through `spec-v0.3.11.md`, and `HANDOVER.md` are historical
reference only; they may contain stale actor order, scoring, paths, or
checkpoint rules. During audits, they may be read only to identify stale
pollution risks, never to override `NOTES.md` + this `SKILL.md` +
`spec-v0.3.12.md`.

Precedence rule: when `spec-v0.3.12.md` conflicts with this file about actor
names, relay order, whiteboard paths, memory access, or report ownership, this
Codex workflow entrypoint wins. The spec remains authoritative for the translation
method, scoring schema, checkpoint logic, and artifact contents.
If startup `AGENTS.md` rules mention translate-v2 and conflict with this
entrypoint about runtime topology or artifact schema, use this entrypoint and
`NOTES.md`; keep `AGENTS.md` safety, privacy, memory, and dispatch gates in
force.

Prompt placement rule: in every baton prompt, `spec-v0.3.12.md` §3.1
translation principles must appear at the top as the generation compass, while
§3.2 three-layer 14-dimension scoring must appear at the bottom as the
post-hoc yardstick. These mechanisms are parallel and non-substitutable; do not
merge, reorder, or use one to perform the other's function.

Gate order rule: for any translate-v2 prompt, dispatch, user-facing artifact,
final answer, or Antique translation-prep related file write, run
`scripts/translate_v2_contract_gate.py` before web/whiteboard preflight,
artifact lint, or file delivery. Generic preflight success is not sufficient
for translate-v2; the skill-specific gate must pass first.
For 《古董局中局》 translation tasks, any file write during prep or output must
state which state-machine gate applies: 小D prep-helper prompt only, 小D-authored
prep package forwarded for user audit, user-reviewed prep package complete, or
explicit accident/review work with no translation/prompt/dispatch.
Language-surface gate: 小D/本地 prep-helper 的 `译前上下文包` and every member
raw capture are formal relay inputs, not informal scratch. Before a prep
package is sent to the user for audit, run
`scripts/translate_v2_artifact_lint.py --type prep-package <path>`.
Immediately after each baton raw capture, run
`scripts/translate_v2_artifact_lint.py --type baton-raw <path>`
before using that raw as N-1/N-2, round archive material, checkpoint evidence,
or final-report evidence. For Antique Game tasks, also run
`scripts/lint_chinese_main_artifact.py`
on prep/raw Markdown that will feed the relay. These files must use Chinese
main narrative for analysis, wrapper headings, explanations, scores, reasons,
and convergence probes; target-language candidates, schema keys, model names,
paths, and author reference samples may remain in their required languages.
If this gate blocks, repair the wrapper or re-request a Chinese-main baton;
do not carry the blocked raw forward as formal evidence.

Do not read Claude Code `claude-mem` or `<external-agent-private-memory>` as part
of normal Codex operation. If old CC memory files are needed as historical
evidence for a specific translation run, ask the user first and treat that as an
explicit bridge request.

## 2. Codex Fork Runtime

Controller:

- Codex is the main conductor in this fork.
- The old upstream spec often says "CC"; in this localized runtime read that as
  "the current conductor", meaning Codex, unless the text is explicitly about
  the Anthropic member as a reviewer.
- Do not write to the CC-led whiteboard at `<legacy-collab-workspace>` or
  `<legacy-whiteboard-thread-dir>` unless the user explicitly asks to back-port.

Primary whiteboard paths:

- Threads: `<collab-thread-dir>`
- Task board and deliverables: `<collab-workspace>`
- Public Codex workflow archives: `<collab-archive-dir>`
- Round reply drops: `<relay-raw-dir>`
- Web relay scratch prompt: `<relay-prompt-scratch>`
- User uploads: `<relay-upload-dir>`

Final translation outputs:

- Primary output directory: `<translation-output-dir>/`
- Project-specific override: when a task also triggers the
  `antique-game-within-game` skill for 《古董局中局》, final translation-only files
  and final analysis reports must be written under the chapter subdirectory:
  `<translation-output-dir>/《古董局中局》/<部章>/`.
  Existing local pattern uses compact chapter folders such as `第一部第三章`,
  `第一部第四章`, and `第一部第八章`. Create the matching folder if missing.
  These examples are not defaults: derive `<部章>` from the current target
  chapter path/title, chapter card, or explicit user-provided scene location.
  Never reuse the previous Antique Game chapter folder as a fallback; if the
  current chapter cannot be determined, stop and ask/locate it before writing
  final files.
  When this project override is active and 小D is used to draft the
  `译前上下文包`, give it this corresponding chapter output directory and require
  it to inspect all existing `*Translation-report*.md` files in that chapter
  directory by source passage/task identity. Translation prep and chapter
  ingestion use the same report-reading rule: group every chapter report by
  exact source passage/task, then read the latest report in each distinct group
  (filename timestamp preferred, else mtime). Only duplicate reports for the
  same source/task collapse to one latest report. Do not take one latest report
  for the whole chapter, and do not filter the directory down to only the
  current target passage. If the chapter has no reports, record
  `NO_TRANSLATION_REPORTS_FOR_THIS_CHAPTER`. Do not provide a curated pile of
  report files.
  This override applies only to final `Translation*.txt` and
  `Translation-report*.md` deliverables; ordinary non-《古董局中局》 translate-v2
  tasks continue to use the primary output directory.
- Default behavior is to create new, task-specific files in the selected output
  directory and never overwrite existing `Translation.txt` /
  `Translation-report.md` unless the user explicitly asks to overwrite.
- Recommended names:
  `YYYYMMDD-HHMMSS-{topic}-Translation.txt` and
  `YYYYMMDD-HHMMSS-{topic}-Translation-report.md`.
- Translation-only files contain only the final translated text.
- Reports and long-term translation artifacts also live under the same primary
  output directory unless the user explicitly asks for another location.
- Optional convenience mirrors such as `<translation-output-dir>/Translation.txt`
  should be created only when explicitly useful or requested.

## 3. Relay Topology

The upstream canonical relay was:

`哈士奇 -> 小D -> Codex -> 逗比 -> CC`

In the Codex-led workflow, the user has swapped the Codex and CC positions. Use
this operational mapping:

1. `哈士奇` via `ask_husky`: first-baton review and polish.
2. `小D` via `ask_xiaod`: reasoning review and polish.
3. `CC` via `ask_cc`: Anthropic-side review and polish.
4. `逗比` via `ask_doubi`: ByteDance-side review and polish.
5. `Codex conductor` in the main tab: in CLI mode, final-baton review and
   polish; in all modes, checkpoint summary, output/report writing, archive
   ownership, divergence analysis, and user decision handling.

`ask_cc` must be an automatic headless call. Do not ask the user to copy/paste a
prompt into Claude Code. If `ask_cc` fails because Claude Code is not logged in
for headless use, stop and report that infrastructure blocker instead of
silently replacing CC.

`ask_codex` is not part of the normal relay chain in this fork. Use it only for
explicit side reviews, verification, or user-requested extra Codex perspectives;
do not insert it as the routine third baton.

Default runtime channel:

- Default to `网页版接力` for translation tasks.
- Use `CLI 端接力` only when the user explicitly says to use CLI/API/MCP relay
  for that task, for example `CLI 端接力`, `CLI 版接力链`, or `走 CLI`.
- Do not ask the user to choose the runtime channel when they have not
  specified one; record the default as `网页版接力`.
- CLI mode uses the normal Codex workflow chain above.
- Web Relay Mode keeps the same baton order and translation algorithm, but maps
  the execution endpoints to Web counterparts:
  `哈士奇 -> 哈基米`, `小D -> 老D`, `CC -> 小克`,
  `逗比 -> 包子`, `Codex conductor/final baton -> 小G`.
- 哈基米 / Gemini Web first baton must use the target-language NotebookLM
  dictionary when one is available. For uncertain translation choices
  (vocabulary, collocation, idiom, register, key terms, or important
  interpretation points), instruct 哈基米 to consult the NotebookLM dictionary
  for the target language first: Chinese target -> Chinese dictionary, English
  target -> English dictionary, Japanese target -> Japanese dictionary, and
  future target languages -> that target language's dictionary once introduced.
  If the target-language dictionary is not yet introduced, do not force a
  dictionary step; follow the prior 哈基米 first-baton workflow. If the
  target-language dictionary exists but does not answer the uncertainty,
  哈基米 may use ordinary web search for target-language usage evidence; if the
  source text's meaning, semantic boundary, allusion, concept, or factual
  reference is unclear, 哈基米 may also use ordinary web search to confirm the
  source interpretation under the normal source-boundary rules. Do not consult
  the source-language dictionary merely because it is available, and do not let
  web search override user/source/context authority for story facts or add
  unsupported meaning beyond the source.
- In Web Relay Mode, 小G is the fifth ordinary relay baton and produces the
  final-baton review/polish candidate. Codex remains the conductor but does not
  substitute its own local translation baton for 小G. After 小G's raw output is
  captured, Codex performs the round archive, checkpoint judgment, divergence
  analysis, final judging/reporting, and user-facing synthesis.
- Web Relay Mode is not web Deep Research. Deep research remains an explicit
  checkpoint/startup action and must not be smuggled into ordinary relay
  batons.

Sensitive-topic downgrade:

- If the source text involves high-risk political or jurisdictional topics,
  skip domestic providers per the Codex whiteboard rules.
- Default downgrade chain: `哈士奇 -> CC -> Codex conductor`.
- Do not silently send sensitive source text to `小D` or `逗比`.

## 4. Dispatch Rules

Keep the spec's serial relay principle:

- No closed-book parallel replacement for the relay.
- No skipping or reordering batons except the sensitive-topic downgrade above or
  an explicit user instruction.
- No switching between CLI/API and Web endpoints unless the user explicitly
  chose that channel or explicitly changes the channel mid-run.
- Every baton reviews the previous baton before producing a revised version.
- For normal batons, include N-1 and N-2 context as described in
  `spec-v0.3.12.md`.
- The main Codex conductor may inspect the whole trajectory when acting as the
  CLI final baton and when producing reports.
- In Web Relay Mode, Codex inspects the whole trajectory only after 小G's
  fifth-baton output has been captured; Codex's post-baton duties are
  archiving, checkpointing, divergence analysis, final judging/reporting, and
  user decision handling, not replacing 小G's relay turn.
- Where `spec-v0.3.12.md` assigns final-baton duties, round checkpointing,
  even-round divergence analysis, final blind judging, BWS comparison, or final
  reporting to "CC", read that as "Codex conductor" in this fork, except that
  in Web Relay Mode the fifth relay baton itself is 小G while Codex keeps the
  non-baton conductor/report-owner duties.
- Where `spec-v0.3.12.md` defines Web Relay Mode, preserve this Codex workflow's
  swapped relay order and only replace the endpoint type. The user still owns
  the runtime-channel choice.

Round archives:

- One round equals a complete five-baton cycle in the normal chain.
- Each baton raw capture must pass the `baton-raw` artifact lint before it can
  be included in the combined round archive. If a member's substantive answer
  is usable but Codex's raw wrapper is English-only, repair the wrapper first
  and rerun the lint; if the member answer itself is not Chinese-main, request
  a restatement or mark the baton invalid instead of silently normalizing it.
- At the end of each round, write one combined archive under:
  `<relay-raw-dir>/YYYYMMDD-HHMMSS-translate-r{N}-{topic}.md`
- Report the path, byte count, and a one-sentence judgment to the user; do not
  inline every baton transcript in the main chat.

Checkpoint:

- Stop after each full round and wait for the user.
- The user may choose to continue, revise constraints, request deep research,
  or accept the final translation.
- Deep research remains outside the relay and requires explicit user approval.
- At each checkpoint, record enough state to survive context compaction:
  current round/baton, latest candidate, locked user decisions, open disputes,
  required next baton prompt inputs, round archive path, and any research TODOs.
- Before changing tabs or after a heavy research pass, write a handover snapshot
  under `<handover-dir>/`.

Final-output gate:

- The conductor may generate final `Translation*.txt` and
  `Translation-report*.md` artifacts only in one of two cases:
  1. the translation text has reached strict three-baton convergence, and the
     user explicitly says at checkpoint that they are satisfied / accepts the
     final translation / asks to close out;
  2. a round ends without convergence, but the user explicitly selects one
     preferred translation from the available candidates and asks to use it as
     the final output.
- Strict convergence, reviewer recommendation, or a member saying "ready for
  final" is not enough by itself. Without one of the two user-confirmed states
  above, the conductor must stop at checkpoint and must not create final
  output files.

## 5. Required Startup Inputs

Collect these before the first baton. Ask only for missing required items.

1. Source text or file path.
2. Target language.
3. Context, audience, era, or source background when available.
4. Genre and style contract: identify the target text as fiction/dialogue,
   literary prose/essay, poetry/lyrics, academic paper, legal/technical text,
   news, etc. Translation is constrained re-creation: the target must read as a
   credible finished instance of that genre while still preserving source
   meaning, information density, explicit/implicit balance, sound/cadence where
   relevant, and auditable anchors. Do not treat "literal" as word-order
   copying. Also identify the sound contract when relevant: read-aloud
   smoothness, sentence-length alternation, film-line cadence, prose rhythm,
   rhyme/alliteration/assonance, chain repetition / 顶针, or intentionally plain
   professional cadence. If the text is
   dialogue/live speech/chat/character voice, also identify the spoken register
   target: natural oral fragments vs formal speech, degree of politeness,
   age/status/relationship pressure, and whether non-standard or non-native
   wording should be preserved as character voice. Ask whether the desired
   effect is raw speech, controlled cinematic dialogue, polished literary
   dialogue, or deliberately broken speech; do not assume all oral scenes
   should be heavily fragmented.
5. Special constraints: terminology, formatting, punctuation, taboo terms.
6. Prosody/sound requirements: poetry, lyrics, drama, rap, rhythmic prose, or
   any passage where sentence length, read-aloud flow, light rhyme,
   alliteration/assonance, repetition, 顶针, or film-dialogue cadence matters.
7. Optional author reference sample: the user may provide their own translation
   in another language (often English) to show authorial intent, creative
   strategy, cadence, compression, or target-handfeel. This is optional; do not
   ask for it as a required input and do not assume it exists. When provided,
   treat the source text and author reference as dual author evidence, not as a
   master/subordinate pair and not as "source locks facts, reference locks
   style". Both may constrain facts and both may reveal style. If their routes
   diverge, identify the divergence axis and choose a target-language strategy
   that fits the requested genre and target-language conventions while keeping
   source anchors auditable.
8. Machine translation draft(s): Google and DeepL when available; Google only
   when DeepL does not cover the source/target pair.
9. External-entropy level: user-authored, user-mastered, or needs research.
10. Sensitive-topic answer: whether political/jurisdictional screening is needed.
11. Runtime channel: default `网页版接力`; use `CLI 端接力` only when the user
    explicitly specifies CLI for this task.

## 6. Output Schema

Follow the upstream spec exactly for final artifacts:

- Translation-only output contains only the final translated text. By default,
  write it to a new task-specific file under the selected output directory, not
  to the legacy fixed `Translation.txt` name. For 《古董局中局》 tasks that also
  use `antique-game-within-game`, the selected output directory is the matching
  `output/《古董局中局》/<部章>/` chapter folder.
- Translation report output contains trajectory, rationale, syntax/morphology
  analysis, statistics, sound/cadence or prosody notes when applicable,
  research TODOs, and compliance self-check. By default, write it to a new task-specific report
  file under the selected output directory, not to the legacy fixed
  `Translation-report.md` name.
- R2/R4/R6... divergence/non-divergence analysis includes syntax/morphology
  analysis. It may be embedded as a dedicated section inside the even-round
  combined archive; a separate divergence report file is optional rather than
  mandatory unless the user asks for one or readability requires it.
- Syntax/morphology analysis must follow `spec-v0.3.12.md`
  `current syntax/morphology rule`: do not write a summary-only version. Include
  sentence overview, phrase/particle/honorific breakdown, dependency JSON,
  key lexical morphology, strategy tags, and direct-vs-conversion audit. A
  short source text means finer granularity, not a shorter analysis.
- If a round stops early at a convergence checkpoint, the checkpoint archive
  still needs the same syntax/morphology minimum for the converged candidate.
- The Codex conductor writes the even-round divergence/non-divergence analysis
  section or optional standalone report, and writes the final translation
  analysis report.

## 7. Hard Nos

- Do not use Claude Code memory as an automatic dependency.
- Do not use CC-led whiteboard paths as primary runtime paths.
- Do not confuse discussion of this skill with invocation of the skill.
- Do not split a coherent text into paragraph-level independent translations
  unless the user explicitly asks for that tradeoff.
- Do not let machine translation drafts override the user's stated evidence or
  research findings.
- Do not confuse constrained re-creation with free rewriting. Genre-credible
  target prose is required, but Addition, Omission, Mistranslation,
  Hallucination, background-expansion, and unanchored plot/emotion changes
  remain hard failures.
- Do not write analysis into `Translation.txt`.
- Do not start web Deep Research without explicit user approval. Default
  `网页版接力` counts as approval for the ordinary Web relay endpoints in that
  run, but not for Deep Research.
