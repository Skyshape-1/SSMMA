
# Git & GitHub Command Cheat Sheet

---

## 1. Basic Workflow: Local to GitHub

### Initialize a Repository and Push Code to GitHub
```bash
git init                          # Initialize a Git repository in your local project folder
git add .                         # Stage all changes for commit
git commit -m "Initial commit"    # Commit changes with a message
git remote add origin <repo-url>  # Link local repo to GitHub remote
git branch -M main                # Rename the branch to 'main' (if not already)
git push -u origin main           # Push code to GitHub and set upstream
```

### After Making Code Changes Locally
```bash
git status                        # View changed files
git add .                         # Stage all changes
git commit -m "Describe changes"  # Save a commit with a meaningful message
git push                          # Push committed changes to GitHub
```

---

## 2. Branching

### Create and Switch to a New Branch
```bash
git checkout -b feature-xyz       # Create and move into a new branch
```

### Switch Back to an Existing Branch
```bash
git checkout main                 # Switch back to the main branch
```

### Push the New Branch to GitHub
```bash
git push -u origin feature-xyz    # Push the branch and track it on GitHub
```

---

## 3. Workflow: Feature Branch Lifecycle

This section outlines the standard workflow for creating a feature branch, updating code, and merging it into the main branch.

### Diagram of the Workflow

```
   Local Repository                    GitHub Remote Repository
------------------------            -----------------------------
|                        |          |                           |
|  git checkout -b X     |          |                           |
|        ▼               |          |                           |
|  Edit & commit code    |          |                           |
|        ▼               |          |                           |
|  git push -u origin X  |   ====>  |  feature branch appears   |
|                        |          |                           |
|  git checkout main     |          |                           |
|  git pull origin main  |          |                           |
|  git merge feature-X   |          |                           |
|  git push              |   ====>  |  main branch updated      |
|  git branch -d X       |          |                           |
|  git push origin --delete X  ==>  |  feature branch removed   |
------------------------            -----------------------------
```

### Detailed Steps

1. **Create a new branch locally** to work on a specific feature:
   ```bash
   git checkout -b feature-X
   ```

2. **Make code changes**, then stage and commit:
   ```bash
   git add .
   git commit -m "Implement feature X"
   ```

3. **Push the new branch to GitHub** to create it on the remote:
   ```bash
   git push -u origin feature-X
   ```

4. Once development is complete, **switch back to the main branch**, and ensure it is up-to-date:
   ```bash
   git checkout main
   git pull origin main
   ```

5. **Merge the feature branch into main locally**:
   ```bash
   git merge feature-X
   ```

6. **Push the updated main branch** to GitHub:
   ```bash
   git push
   ```

7. **Delete the feature branch locally and remotely**:
   ```bash
   git branch -d feature-X
   git push origin --delete feature-X
   ```

---

## 4. Merging Branches

### Merge a Feature Branch into Main
```bash
git checkout main                 # Switch to the main branch
git pull origin main              # Ensure it's up-to-date
git merge feature-xyz             # Merge changes from feature branch
```

---

## 5. Resolving Merge Conflicts

Detailed information on how to resolve merge conflicts is covered in this YouTube tutorial:

**How to Resolve Merge Conflicts in GitHub**  
[https://www.youtube.com/watch?v=RGOj5yH7evk](https://www.youtube.com/watch?v=RGOj5yH7evk)

---

## 6. Deleting Branches

### Delete a Local Branch
```bash
git branch -d feature-xyz         # Safe delete (if already merged)
git branch -D feature-xyz         # Force delete (if not yet merged)
```

### Delete a Remote Branch
```bash
git push origin --delete feature-xyz
```

---

## 7. Pulling vs Pull Requests

| Concept            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `git pull`         | A Git command that downloads and merges changes from a remote repository into your current local branch |
| Pull Request (PR)  | A GitHub feature that allows you to propose changes from one branch (often a feature branch) into another, enabling review and collaboration before merging |

---

## 8. Summary Table of Common Commands

| Task                             | Command |
|----------------------------------|---------|
| Initialize repository            | `git init` |
| Stage changes                    | `git add .` |
| Commit changes                   | `git commit -m "message"` |
| Push to GitHub                   | `git push` |
| Create branch                    | `git checkout -b branch-name` |
| Switch branches                  | `git checkout branch-name` |
| Merge branches                   | `git merge branch-name` |
| Delete local branch              | `git branch -d branch-name` |
| Delete remote branch             | `git push origin --delete branch-name` |
| Pull from remote                 | `git pull origin branch-name` |
