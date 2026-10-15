# UC3.3_SOMES

Domino piece repository for **UC3.3 SOMES** (sustainable energy workflow: OneData I/O, MRK/PV/battery simulation, investment KPIs, dashboard).

- SPICE GitLab: [use-cases/uc3/UC3.3_SOMES](https://gitlab.spice-platform.eu/use-cases/uc3/UC3.3_SOMES)
- SPICE Harbor: `harbor.testbed.spice-platform.eu/partner/uc3/uc3_3_somes:0.1.35-group0`
- Workflow import pack: [workflows/UC3.3_SOMES](https://gitlab.spice-platform.eu/use-cases/uc3/workflows/-/tree/main/UC3.3_SOMES)

## Repository layout (production)

| Path | Purpose |
|------|---------|
| `pieces/` | Domino pieces and shared `common/` helpers |
| `pieces/catalog/` | Default PV/battery catalog JSON (bundled in images) |
| `dependencies/` | Container build (`Dockerfile`, `requirements.txt`) |
| `config.toml` | Registry, version, repository metadata |
| `.domino/` | Compiled piece metadata (updated by CI) |
| `sus_onedata.customization` | **Import in Domino** (Workflows editor → Import) |
| `sus_onedata.json` | GitLab workflows pack only (not Domino UI) |
| `requirements_0.txt` | Python deps reference for Domino organize |

## Domino deployment

1. Connect this GitLab repo as a **Pieces Repository** in Domino.
2. Wait for CI on `main` (after `config.toml` change) to build Harbor images.
3. Import **`sus_onedata.customization`** in the Domino workflow editor (not `.json`). Regenerate after edits:
   `python scripts/sync_onedata_customization.py`
   Set workflow **Secrets** (optional if using code defaults):
   - `onedata_onezone_host` — e.g. `data.spice-platform.eu`
   - `onedata_token` — your OneData access token (not stored in git)
   - `onedata_output_dir` — e.g. `onedata:///YourSpace/run`
4. Seed static inputs on OneData under `inputs/` (load, prices, scenario, etc.) before the first run.

## GitLab CI / Harbor

Pipeline builds and publishes piece images to Harbor on push to `main` when `config.toml` changes.

Set these CI/CD variables (Settings → CI/CD → Variables). Mark secrets as **Masked**:

| Variable | Description |
|----------|-------------|
| `CI_PUSH_TOKEN` | Project access token with `write_repository` (+ `api`) |
| `CI_RELEASE_TOKEN` | Project access token with `api` |
| `CONTAINER_REGISTRY` | `harbor.testbed.spice-platform.eu` |
| `CONTAINER_REGISTRY_USERNAME` | Harbor user/robot (e.g. `partner`) |
| `CONTAINER_REGISTRY_PASSWORD` | Harbor password from vault |

`config.toml` `REGISTRY_NAME` must use namespace `harbor.testbed.spice-platform.eu/partner/uc3`. `REPOSITORY_NAME` must be **lowercase** (Docker image tag rules).
