# Customer Retention Lab – Business Use Cases & Pricing

## 1. Proactive Churn Prevention for B2C Apps

**Who it’s for**  
Ride‑hailing, food delivery, fintech, e‑commerce, telco and subscription apps with large consumer bases.

**Problem**  
High silent churn from low‑engagement customers who never complain but simply stop using the product.

**Solution**  
Use the Retention Lab to:
- Score churn risk for targeted segments (e.g., last active > 14 days, low transaction volume).
- Generate personalized Gemini messages nudging return (discounts, new features, reminders).
- Deliver messages via SMS using the integrated communications service.

**Workflow**  
1. Export users from CRM/warehouse and bulk‑upload via CSV.  
2. Use presets (high/medium/low risk) or custom features (city, rides, spend, segment).  
3. Run inference to get risk + suggested message.  
4. Approve or edit copy and send SMS directly.  
5. Track response and conversion via `/api/analytics/events/`.

**Value**  
- 5–15% lift in reactivation for at‑risk cohorts.  
- Reduced blanket campaigns; more targeted, lower‑cost outreach.

**Recommended pricing**  
- Platform fee: **$500/month** base for up to 50k profiled users.  
- Usage: **$0.005 per inference** and **$0.02 per SMS** (pass‑through + margin).  
- Pilot: 30‑day free trial capped at 5k inferences / 2k SMS.

---

## 2. Customer Support Save Desk (CS Operations)

**Who it’s for**  
Support teams handling cancellations, downgrades and repeated complaints.

**Problem**  
Agents handle save opportunities inconsistently; lack structured way to prioritize who to “fight for”.

**Solution**  
- Connect support/CSAT data as features (tickets opened, low CSAT events).  
- Use Retention Lab to prioritize high‑risk accounts and generate tailored save offers.  
- Trigger SMS follow‑ups after tough interactions or when a case is resolved.

**Workflow**  
1. Daily export of accounts with low CSAT / many tickets → bulk upload.  
2. Agents open the dashboard, filter by highest churn risk.  
3. For each account, generate a personalized message (apology, credit, upgrade, callback link).  
4. Log outcomes as analytics events for ROI reporting.

**Value**  
- Higher save rate on at‑risk customers.  
- Standardized, high‑quality messaging for front‑line teams.

**Recommended pricing**  
- Seat‑based add‑on to core platform: **$50/agent/month** (min 5 agents).  
- Includes up to 500 inferences per agent; above that, **$0.004 per inference**.

---

## 3. Dormant User Win‑Back Campaigns

**Who it’s for**  
Marketing & lifecycle teams responsible for re‑engagement.

**Problem**  
Batch email win‑back campaigns have low open rates and weak personalization.

**Solution**  
- Use churn risk + behavioural features (last purchase, category, city).  
- Generate short SMS win‑back offers more likely to be seen and acted on.  
- A/B test messages via segments (e.g., discount vs content‑driven).

**Workflow**  
1. Segment: `last_active_days > 30`, `segment in ['churned', 'at_risk']`.  
2. Upload to Retention Lab and run inference.  
3. Split by segment/city and send tailored SMS variants.  
4. Measure reactivation (return sessions, orders) via analytics.

**Value**  
- Increase ROI on dormant cohorts that otherwise generate no revenue.  
- Fast experiment loop for message/offer design.

**Recommended pricing**  
- Campaign bundle: **$2,000 per campaign** (up to 200k users) including:  
  - 200k inferences  
  - 50k SMS (SMS carrier fees extra if high‑cost routes)  
- Additional volume at usage rates (same as Use Case 1).

---

## 4. VIP / Enterprise Account Nurturing

**Who it’s for**  
Account Management / Customer Success teams with high‑value B2B accounts.

**Problem**  
CSMs have limited bandwidth; some VIP accounts go quiet before renewal without proactive contact.

**Solution**  
- Feed in engagement metrics (logins, feature adoption, ticket volume).  
- Use churn risk + Gemini to draft check‑in messages or renewal nudges.  
- Let CSMs review/edit and send via SMS or manually via email.

**Workflow**  
1. Monthly export of all accounts 90 days pre‑renewal with usage data.  
2. Bulk upload and compute risk per account.  
3. CSMs filter by high‑risk, high‑ARR cohort.  
4. Generate outreach scripts, personalize lightly, send, and track responses.

**Value**  
- Higher renewal rates on key accounts.  
- More consistent CSM motions across regions/teams.

**Recommended pricing**  
- Enterprise plan starting at **$1,500/month** for up to 200 managed accounts.  
- Includes 10 CSM seats, unlimited inferences on those accounts, and 5k SMS.

---

## 5. Onboarding & First‑Week Support Nudges

**Who it’s for**  
Growth, product & support teams focused on activation.

**Problem**  
New signups drop off before seeing core value; support only hears from a small vocal subset.

**Solution**  
- Use Retention Lab to identify low‑engagement new users and send helpful, human‑sounding nudges.  
- Include links to help center, support WhatsApp, or quick‑start flows.

**Workflow**  
1. Daily job pushes new users + basic usage stats as features.  
2. Run inference and generate onboarding nudges.  
3. Auto‑send SMS for highest‑risk new signups; leave others for email.

**Value**  
- Improved Day‑1 / Day‑7 activation metrics.  
- Fewer “I signed up but never used it” churn cases.

**Recommended pricing**  
- Add‑on to any plan: **$300/month** for up to 20k new users per month, 20k inferences, 5k SMS.

---

## 6. Incident & Outage Incident Communication (Support‑Led)

**Who it’s for**  
Ops, SRE, and Support teams.

**Problem**  
During incidents, support gets flooded with tickets and communication is inconsistent.

**Solution**  
- Maintain pre‑defined incident segments (by geography, product line).  
- Quickly upload affected users and send clear, empathetic SMS updates.  
- Use Gemini to adapt templates based on impact and ETA.

**Workflow**  
1. Identify affected cohort (e.g., `city = 'Nairobi'`, `segment = 'loyal'`).  
2. Upload / select cohort, choose an “incident” preset.  
3. Generate message, legal/comms reviews, send SMS.  
4. Optionally follow up with resolution message and survey.

**Value**  
- Reduces inbound volume during incidents.  
- Improves trust via fast, transparent updates.

**Recommended pricing**  
- Included in Pro and Enterprise plans.  
- SMS + inference usage charged per normal rates.

---

## Packaging & Plan Suggestions

To simplify sales conversations, you could package the above into 3 tiers:

### Starter
- Target: Early‑stage products, up to 20k MAU.  
- Includes:
  - 20k inferences/month  
  - 5k SMS/month  
  - Basic dashboard + bulk upload  
- **Price:** **$490/month**

### Pro
- Target: Growing B2C / B2B companies with dedicated CS or growth teams.
- Includes:
  - 150k inferences/month  
  - 40k SMS/month  
  - Bulk upload + users, analytics, and incident workflows  
  - 10 CS/Support seats  
- **Price:** **$1,490/month**

### Enterprise
- Target: Large enterprises with complex data and many agents.
- Includes:
  - Custom inference & SMS volumes (starting at 500k inferences, 150k SMS)  
  - Unlimited dashboard users  
  - Priority support & onboarding assistance  
  - Optional on‑prem / VPC deployment  
- **Price:** from **$3,500/month** (quote‑based)

---

## Notes on Pricing

- SMS carrier fees vary by country; the above assumes a margin on top of the raw provider cost.  
- Gemini API costs can be passed through or baked into the per‑inference rate.  
- For new regions or early lighthouse customers, you can discount base fees by 20–40% in exchange for case studies.
