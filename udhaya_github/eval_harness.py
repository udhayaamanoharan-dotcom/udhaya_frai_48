# GitHub Upload and Push – Step by Step

## A. Create your repository
1. Sign in to https://github.com/.
2. Select the **+** button → **New repository**.
3. Repository name: `club-expense-claim-checker`.
4. Choose **Private** if your faculty has not asked for a public repository.
5. Do not add a README, .gitignore, or license on GitHub because this folder already contains them.
6. Select **Create repository**.

## B. Open the project folder
1. Extract the ZIP file.
2. Open VS Code.
3. Select **File → Open Folder** and choose `club_expense_claim_checker`.
4. Check that `.gitignore` is present. In VS Code, enable viewing hidden files if needed.
5. Copy `.env.example` to `.env` and fill in your private API details. Never upload `.env`.

## C. Push using VS Code terminal
Open **Terminal → New Terminal** and run these commands one at a time:

```bash
git init
git add .
git status
git commit -m "Add project specification and input datasets"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/club-expense-claim-checker.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Use the exact repository URL shown on your GitHub repository page.

If Git asks you to identify yourself, set your Git commit name and email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```
Use the email associated with your GitHub account if you want commits linked to your profile.

## D. Make at least 3 meaningful commits
Do not make three empty commits. Make changes, then commit each stage:

```bash
git add docs/SPECIFICATION.md claims.csv budgets.csv
git commit -m "Complete approved specification and sample inputs"

git add main.py system_prompt.txt
git commit -m "Implement LLM extraction and claim decision rules"

git add tests docs README.md .gitignore
git commit -m "Add evaluation tests and project documentation"

git push
```

If you already committed some of these files in the first commit, make a meaningful improvement before creating the next commit. Each commit should represent real work.

## E. Verify on GitHub
1. Refresh your repository page.
2. Confirm `main.py`, CSV files, `README.md`, `.gitignore`, `system_prompt.txt`, `docs/`, and `tests/` are visible.
3. Confirm `.env` is NOT visible.
4. After running the program, add generated files from `outputs/` if your faculty requires output files in the repository. The `.gitignore` intentionally excludes generated output files by default.
5. Copy the repository URL for your final submission.

## Common problems
- `git is not recognized`: install Git, restart VS Code, and try again.
- `remote origin already exists`: run `git remote -v`; if the URL is wrong, use `git remote set-url origin YOUR-REPOSITORY-URL`.
- `rejected/non-fast-forward`: check the GitHub repository contents and follow the GitHub guidance before force-pushing. Do not use `git push --force` as a first fix.
- Login prompt: complete GitHub's browser authentication. GitHub account passwords are not accepted as Git HTTPS passwords; use the browser sign-in flow or a supported credential manager.
