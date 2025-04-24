## ✅ Forgejo Monitoring Dashboard - Checklist Overview

This dashboard monitors **Forgejo** (a self-hosted Git service) using **Prometheus** and **Grafana** to provide insights into system performance, repository activity, and user interactions.

---

### 🔌 Data Source Integration
- [x] **Prometheus** configured as the data source for Grafana.
- [x] **Gitea Metrics Exporter** used for Forgejo (compatible as Forgejo is a fork of Gitea).
- [x] Prometheus successfully scraping Forgejo metrics.

---

### 📊 Dashboard Setup
- [x] Imported and customized the [Gitea Grafana Dashboard]
- [x] Created new dashboard: [Forgejo Monitoring]
- [x] Modified panels to match Forgejo-specific monitoring needs.

---

### 🧩 Custom Panels Added
- [x] **Forgejo Overview** (Repos, Orgs, Users, Stars, Milestones, Issues, Labels, Releases)
- [x] **System Performance** (CPU, Memory, Disk I/O usage)
- [x] **Repository Metrics** (Issues by Repository)
- [x] **User Interactions** (Accesses, Watches)
- [x] **Application Tasks** (Webhook tasks, update tasks)
- [ ] **Metrics by Labels** (Panel added – awaiting labels to populate)

---

### ⚠️ Limitations
- [ ] Error rate metrics **not available** from Forgejo.
- [ ] Git activity metrics (push, pull, clone) are **not natively exposed**.

---

### 🔔 Alerting (Pending)
- [ ] Define alert rules (e.g., Forgejo down, high CPU).
- [ ] Configure alert routing (Grafana OnCall, Slack, Email).
- [ ] Test alerting system.

---

### 🧪 Testing & Validation
- [x] Panel queries tested and refreshing properly.
- [x] Metrics validated using: [Prometheus UI]
- [x] Dashboard JSON backup available.

---

### ➕ Add New Metrics
- [x] Duplicate an existing panel (⋮ > Duplicate).
- [x] Click **Edit** > Modify query with desired metric.
- [x] Save dashboard to apply changes.



