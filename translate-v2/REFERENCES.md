# References and Design Influences

This page documents standards, research directions, and open-source projects
that informed the public `translate-v2` package.

It is not a claim of certification, formal compliance, or code provenance.
The workflow is a personal translation aid. References listed here may be used
as conceptual background, scoring inspiration, or comparison material; code is
not copied unless the package explicitly says so and the license boundary is
kept.

License status for GitHub projects was rechecked on 2026-06-30.

## Implemented Or Adapted In This Package

- A custom three-layer, fourteen-dimension review schema built on an
  MQM-style analytic backbone, expanded for literary and cultural translation.
- Severity weighting inspired by GEMBA-MQM/GEMBA-style MQM scoring:
  `critical = 25`, `major = 5`, `minor = 1`, and
  `punctuation_minor = 0.1`.
- Multi-run final judging with outlier filtering and reciprocal-rank weighted
  aggregation.
- Best-Worst Scaling as a relative comparison method between candidate
  translations.
- TREQA-style reader reachability checks: a translation should preserve enough
  information for a target-language reader to answer core comprehension
  questions.
- DeepL and Google Translate baselines as practical comparison anchors when
  the target language is supported.
- Serial multi-agent relay review with explicit context carryover, checkpoints,
  report contracts, and validation scripts.

## Translation Standards And Quality Frameworks

Reviewed as background or process references:

- [MQM / Multidimensional Quality Metrics](https://themqm.org/)
- [ISO 17100](https://www.iso.org/standard/59149.html)
- [ISO 18587](https://www.iso.org/standard/62970.html)
- [ASTM F2575](https://www.astm.org/f2575-25.html)
- TAUS DQF / DQF-MQM
- LISA QA Model
- SAE J2450
- GB/T 19363.1
- GB/T 19682
- T/TAC 1-2016 and other TAC translation/localization standards

These are used as quality-management and terminology references. They do not
make this package an accredited translation-service system.

## Translation Theory Background

Reviewed as literary and functional translation background:

- Yan Fu's Xin-Da-Ya framework.
- Fu Lei's spirit-resemblance theory.
- Qian Zhongshu's sublimation theory.
- Xu Yuanchong's Three Beauties, Three Transformations, and reader-oriented
  Three Joys.
- Gu Zhengkun's plural complementary standards.
- House's translation quality assessment model.
- Reiss text typology.
- Nord's functionalist translation brief and text-analysis framework.
- Toury's descriptive norms.
- Venuti's domestication and foreignization.
- Holmes/Toury map of translation studies.

These theories inform the literary judgment layer. They are not treated as a
single universal scoring formula.

## Machine Translation And LLM Evaluation Background

Reviewed as metric or evaluator background:

- BLEU, METEOR, TER, and chrF.
- BLEURT and BERTScore.
- COMET, COMET-22, COMET-Kiwi, xCOMET, and MetricX.
- GEMBA and GEMBA-MQM.
- AutoMQM.
- Prometheus 2 and PandaLM.
- WMT Metrics Shared Task methodology.

These metrics are useful for triage, reranking, or diagnostic inspiration, but
generic automatic metrics are not used as the sole final judge for literary
translation.

## LLM-Era Translation Research Directions

Reviewed as research background, not copied as implementation:

- TransAgents.
- DELTA.
- DUAL-REFLECT.
- MAPS.
- SAMAS.
- CHORUS.
- LitMT and related literary MT work.
- PARDEN-style stability ideas.
- TREQA.
- Belebele, JobResQA, LiT, and LITRANSPROQA-style comprehension or
  round-trip evaluation.
- Paratextual explicitation for culturally dense texts.

These projects and papers shaped the package's preference for role separation,
document-level memory, explicit critique, and reader-task evaluation.

## Deep Research Notes

The current public spec was also distilled from non-bundled deep-research notes on:

- Western translation quality evaluation frameworks for literary multi-agent
  pipelines.
- Translation quality evaluation in the 2024-2026 LLM era.
- Chinese academic and professional translation quality standards.

Those notes are not bundled in this package. Their role was to shape the design
inventory and prevent the spec from relying on one narrow standard.

## GitHub Projects Reviewed

| Project | License status checked on 2026-06-30 | How it affected this package |
|---|---:|---|
| [maats0519/maats_mqm](https://github.com/maats0519/maats_mqm) | GitHub API did not detect a license | MQM-style prompt and schema reference only. No code copied unless licensing is separately confirmed. |
| [xunbu/docutranslate](https://github.com/xunbu/docutranslate) | MPL-2.0 | Converter, file-I/O, and glossary-pipeline ideas only. Any copied MPL-covered file must keep its license boundary. |
| [machinewrapped/llm-subtrans](https://github.com/machinewrapped/llm-subtrans) | MIT text in repository license file | Checkpoint, retry, rate-limit, and provider-architecture ideas. |
| [zh-plus/openlrc](https://github.com/zh-plus/openlrc) | MIT | QA/report-schema ideas only; the audio workflow is not copied. |
| [Skytliang/Multi-Agents-Debate](https://github.com/Skytliang/Multi-Agents-Debate) | GPL-3.0 | Concept-only influence for structured critique. No code, prompts, or role templates copied. |
| [nicepkg/gpt-runner](https://github.com/nicepkg/gpt-runner) | MIT | Comparison-only; not adopted as a runtime route. |

## Projects Reviewed But Not Adopted

The following were reviewed or mentioned during design, but are not code
sources for this package:

- Koharu: GPL-3.0; no code copied.
- BabelDOC: AGPL-3.0; no code copied.
- PDFMathTranslate: AGPL-3.0; no code copied.
- HiMATE: no confirmed public license in the reviewed notes; no code copied.
- M-MAD: no confirmed public license in the reviewed notes; no code copied.
- DITING: rejected after review; not adopted.

