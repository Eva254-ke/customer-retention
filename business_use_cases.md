# Customer Retention Lab

## The Problem

B2C apps in Africa (ride-hailing, fintech, delivery, telco) lose 20–40% of users silently every quarter. These customers don't complain—they just stop using the product. Traditional win-back campaigns are:

- **Generic**: Batch emails with low open rates.
- **Slow**: Marketing teams need weeks to set up segments and copy.
- **Disconnected**: Prediction, copywriting, and delivery live in separate tools.

---

## The Solution

**Retention Lab** is an AI-powered retention platform that predicts churn, generates personalized messages, and delivers them via SMS using Africa's Talking SMS APIs.

| Step | What happens |
|------|--------------|
| 1. Upload | Bulk-upload customers from CSV or connect via API |
| 2. Score | AI scores churn risk based on engagement features |
| 3. Generate | Gemini writes a short, personalized SMS nudge |
| 4. Send | One-click delivery via Africa's Talking SMS |
| 5. Track | Log responses and measure reactivation |

**Result**: 5 to 15% lift in reactivation for at-risk cohorts, at a fraction of the cost of blanket campaigns.

---

## Target Customer

**Primary**: Growth / Lifecycle / Customer Success teams at B2C apps with a large number of users and user conversations

**Verticals** (in order of priority):

1. **Ride-hailing & delivery** – high churn, high SMS open rates, clear LTV per user.
2. **Fintech & lending** – dormant accounts = lost revenue; compliance requires direct comms.
3. **Telco & utilities** – large user bases, existing SMS infrastructure, need for personalization at scale.

---

## Business Model

### Revenue Streams

| Stream | How it works | Example |
|--------|--------------|---------|
| **Platform fee** | Monthly base for access + users | $500/mo for up to 50k users |
| **Inference usage** | Per-prediction charge | $0.005 per inference |
| **SMS delivery** | Pass-through + margin | $0.02 per SMS (varies by country) |

### Unit Economics (per 10k users/month)

| Item | Cost | Revenue | Margin |
|------|------|---------|--------|
| Gemini API (10k inferences) | ~$5 | $50 | $45 |
| SMS (2k sent @ $0.01 cost) | $20 | $40 | $20 |
| Platform fee (allocated) | — | $100 | $100 |
| **Total** | **$25** | **$190** | **$165 (87%)** |

### Pricing Tiers

| Tier | Users | Inferences | SMS | Price |
|------|-------|------------|-----|-------|
| Starter | 20k | 20k | 5k | $490/mo |
| Pro | 100k | 150k | 40k | $1,490/mo |
| Enterprise | 500k+ | Custom | Custom | From $3,500/mo |

---

## Integration Options

### 1. No-code (Dashboard)

- Upload CSV of customers.
- Use the web dashboard to run predictions and send SMS.
- Best for: Small teams, pilots, non-technical users.

### 2. API-first

- `POST /api/inference/predict/` – get risk score + AI message.
- `POST /api/communications/send-sms/` – send SMS directly.
- `POST /api/users/bulk-upload/` – ingest users programmatically.
- Best for: Engineering teams integrating into existing CRM/CDP.

### 3. Webhook / Event-driven

- Customer's backend pushes events to `/api/analytics/events/`.
- Retention Lab triggers predictions and messages automatically.
- Best for: Real-time, automated retention flows.

---

## Why Now

1. **AI cost collapse**: Gemini and similar models make personalized copy cheap and fast.
2. **SMS dominance in Africa**: 95%+ open rates; still the primary channel for transactional and marketing comms.
3. **Retention > Acquisition**: In a tighter funding environment, keeping users is cheaper than acquiring new ones.
4. **No incumbent**: No retention-focused SaaS built for African B2C apps with local SMS delivery baked in.

---

## Competitive Landscape

| Player | Weakness |
|--------|----------|
| Generic CRMs (HubSpot, Freshsales) | No churn prediction, no AI copy, weak SMS in Africa |
| Marketing automation (Braze, CleverTap) | Expensive, overkill for SMS-first markets |
| SMS providers (Africa's Talking, Twilio) | Delivery only—no intelligence layer |
| In-house scripts | Fragile, no UI, no Gemini integration |

**Retention Lab** is the **only** tool that combines prediction + AI copy + African SMS delivery in a single, affordable package.

---

## Summary

| | |
|---|---|
| **Use case** | Proactive churn prevention for B2C apps in Africa |
| **Model** | Platform fee + usage (inference + SMS) |
| **Integrations** | Dashboard, REST API, webhooks, CRM connectors (roadmap) |
| **Distribution** | Direct → Partner channel → Self-serve |
| **Differentiation** | AI + SMS + Africa-first, all-in-one |
