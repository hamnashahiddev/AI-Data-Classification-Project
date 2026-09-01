# Contributing to the DecodeLabs AI Training Kit

Thanks for your interest in this repo! This project holds the Industrial
Training Kit projects for the DecodeLabs AI Engineer Batch 2026. It's
primarily a personal learning portfolio, but contributions, fixes, and
suggestions from fellow interns or reviewers are welcome.

## Ways to contribute

- **Bug fixes** — found a broken script or a wrong output? Open an issue
  or a pull request.
- **Improvements** — cleaner logic, better comments, added test coverage,
  or performance tweaks are all welcome.
- **New examples** — extra sample inputs, edge cases, or usage examples
  that make a project easier to understand.
- **Documentation** — typo fixes, clarity improvements, or missing setup
  steps in the README.

## Before you start

1. Check open [issues](../../issues) to see if your idea or bug is
   already being discussed.
2. For larger changes, open an issue first to discuss the approach
   before writing code — this avoids duplicated effort.

## Getting set up locally

```bash
# 1. Fork and clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a project to confirm your setup works
python3 rule_based_chatbot.py
python3 data_classification.py
```

## Making changes

1. Create a new branch for your change:
   ```bash
   git checkout -b fix/short-description
   ```
2. Keep changes focused — one fix or feature per pull request.
3. Follow the existing code style:
   - Clear, descriptive variable and function names
   - Docstrings/comments explaining the *why*, not just the *what*
   - Keep functions small and single-purpose (matches the "IPO"
     Input → Process → Output structure used throughout this kit)
4. Test your changes locally before submitting:
   ```bash
   python3 <project_file>.py
   ```
5. Commit with a clear message:
   ```bash
   git commit -m "Fix: handle empty input in chatbot loop"
   ```

## Submitting a pull request

1. Push your branch:
   ```bash
   git push origin fix/short-description
   ```
2. Open a pull request against `main`, describing:
   - What the change does
   - Why it's needed
   - How you tested it
3. Be responsive to review feedback — small revisions are normal.

## Code of conduct

Be respectful and constructive. This repo exists as a learning space, so
feedback should help contributors grow, not discourage them.

## Questions?

Reach out via:
- 📧 decodelabs.tech@gmail.com
- 🌎 www.decodelabs.tech

Thanks again for helping improve this training kit!