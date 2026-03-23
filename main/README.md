# 🔐 Password Toolkit — Main Branch (Merged)

This is the **main** branch — the final merged application combining all 4 feature branches.

## Features Included
| Feature                | Branch                              | Route       |
|------------------------|-------------------------------------|-------------|
| Password Generator     | feature/password-generator          | `/`         |
| Strength Checker       | feature/password-strength-checker   | `/strength` |
| Mask / Unmask Toggle   | feature/password-mask-toggle        | `/mask`     |
| Password Validator     | feature/password-validator          | `/validator`|

## How to Run the Full App
```bash
cd main
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
# Visit http://localhost:8080
```

## API Endpoints (All Active)
| Method | Endpoint       | Feature           |
|--------|----------------|-------------------|
| GET    | /api/generate  | Password Generator |
| POST   | /api/strength  | Strength Checker  |
| POST   | /api/mask      | Mask Toggle       |
| POST   | /api/validate  | Validator         |

## How This Was Built (Git Simulation)
This folder represents the state of the `main` branch **after** all 4 feature
branches were merged via Pull Requests.

In a real team workflow:
1. Each member worked in their own feature folder/branch
2. Each opened a Pull Request on GitHub
3. Code was reviewed and approved
4. Branches were merged into `main` one by one
5. Merge conflicts in `main.py` and `routes/` were resolved manually

See the root `README.md` for the full Git workflow guide.
