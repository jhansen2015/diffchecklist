# diffchecklist - A resumeable checklist of diffs between two revisions

Initial version will be console based.

Design:
* Written in Python
* Identity files that have changed between two `git` revisions
* Generate a console based checklist for working through each file
* Upon executing with revision id(s), the first file in the list is automatically open in the default file diff tool
* Upon closing the diff tool, the checklist will save the state (if two revision ids have been specified), auto-advance to the next item, mark it, and open the diff tool.
* Subsequent invocation will resume where the last invocation left off.

Thoughts:
* The checklist can be generalized to:
** List of items
** Per item invocation action
** Per item success action
** Per item failure action

Additional ideas:
* Provide a comment
* If the second revision id is the current revision in the workspace, provide the ability to begin editing the current version
* If the second revision id is the current revision, allow the file to be reverted, i.e. undo any changes to it.
