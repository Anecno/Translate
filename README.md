# Translate
Suitable for translation tasks where there is no due time pressure and high-quality
is the priority.

## Notes

1. This is a skill I use for my own work. If you intend to reuse it, please adapt it to your own circumstances and constraints.

2. The project includes several safeguard files designed to keep AI systems from skipping important steps. Unless you have a stronger way to keep those steps visible and enforceable, I recommend keeping these files and adapting them to your own workflow.

3. Deep-research methods are described only briefly. You may use more flexible approaches where appropriate.

4. In my own workflow, I have largely moved away from direct CLI calls. Instead, I use Codex to write prompts and then send those prompts myself through web interfaces.

   There are three reasons for this. First, web interfaces often provide stronger models for translation tasks. Second, this workflow is more transparent: I can inspect the prompt directly and revise it before sending it. Third, high-quality translation cannot be achieved by asking a large language model to produce a final answer in one pass. What I would call the external entropy of human thought — human judgment, disagreement, revision, and interpretive friction — is especially important.

   As the repository description suggests, this project is best suited to users who have enough time to weigh words carefully. It is also better suited to users who are fluent in at least one foreign language and do not need to rely on the skill as a black-box translator. Multilingual input and the workflow outputs can both preserve traces of human external entropy, helping calibrate the direction of translation. In one past project, reading the divergent-analysis output allowed me to manually synthesize the translation I wanted most.

5. Reference standards, research directions, and reviewed GitHub projects are listed in [`translate-v2/REFERENCES.md`](./translate-v2/REFERENCES.md). Dictionary references used in NotebookLM are listed in [`Dictionary-References.md`](./Dictionary-References.md).
