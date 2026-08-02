---
description: Finalize a Python exercise by running PM review and creating the defense document.
agent: senior-python-developer
---

Finalize this exercise: $ARGUMENTS

Definition of done:
- Identify the target module and exercise, such as `M04 ex0`.
- Ensure the implementation and tests are reviewed.
- Delegate to `senior-qa-testing` if QA has not already approved the exercise.
- Delegate to `pm-reviewer` after implementation and QA approval.
- Do not call the exercise done until `Mxx/doc/defensa-exN.md` exists and reflects the approved code.
- If the exercise was already pushed without the defense document, create the defense document now and tell the user it must be committed and pushed as a follow-up.

Return the implementation status, QA status, defense document path, and any follow-up commit/push needed.
