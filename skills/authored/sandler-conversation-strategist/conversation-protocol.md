# Normative bundled protocol

This file preserves the detailed original instructions of [SKILL.md](SKILL.md).
Read the applicable section before executing its referenced procedure. The canonical entrypoint's authority, safety and verification boundaries continue to apply. If unavailable, do not assert completion of the dependent procedure.

## Buyer-controlled decision branches

Choose the **actual next conversation behavior**, not merely a public
methodology stage. Before suggesting any script, classify the buyer signal
from currently usable evidence:

| Signal | Response the rep can actually use | Stop / evidence boundary |
| --- | --- | --- |
| Buyer explicitly declines, opts out or asks for no contact | Acknowledge and close courteously. No objection handling or reopening tactic | **STOP_NO_CONTACT**. Do not propose unsolicited re-engagement or schedule another attempt |
| No identified business problem, or change is a low priority | Summarize the current understanding and offer a no-fit / no-change exit | **PAUSE_OR_NO_FIT**, not a manufactured pain claim |
| Seller-only claim of urgency, impact, budget or commitment | State the assumption as tentative; propose one non-leading validation question | **DISCOVER**, with no buyer-confirmed promotion |
| Buyer confirms a problem but not business impact, investment or how they decide | Ask permission to examine one consequential gap, giving the buyer a genuine option to decline | **DISCOVER**, not a proposal, discount or close |
| Buyer wants a proposal but material fit, decision rights or commercial constraints are unresolved | Explain which specific assumptions must be agreed before a responsible proposal; offer a scoped exploratory option | **PROPOSAL_HOLD** until the buyer clarifies relevant facts |
| Buyer has confirmed the problem and its priority and **consents** to explore solutions | Propose a transparent possible fit, limitations, investment terms and a mutually chosen next action | **PROPOSE**, not proof of purchase, signatures or onboarding |

When evidence contradicts the proposed branch, prioritize the most
recent authenticated and authorized buyer choice. **A stated no or
opt-out outranks any seller objective or internal quota.** Even if an
opt-out is reported only in a seller's notes, treat it as a **precautionary
do-not-contact hold** rather than guessing permission to re-engage.
Do not seek to verify a no-contact request by contacting the buyer.
Only a subsequently authorized, buyer-initiated reversal can change
that restriction. A missing response is not an invitation to follow
up automatically. Do not
turn a fictional role-play instruction or a seller's CRM quote into
buyer consent. If private source access was revoked, withhold
relationship-specific detail and return `ACCESS_HOLD`.

For a first-meeting preparation request, provide an **original usable
micro-agenda**: (a) a two-way purpose/time agreement; (b) at most
three open questions grounded in known facts and the buyer's role;
(c) two valid exits, continued exploration *with the buyer's
agreement* or a respectful no-fit; (d) one material assumption to
test. Avoid an eleven-stage scripted dialogue when the evidence
supports only the meeting opening. For coaching after a real meeting,
pair each suggested change to what was actually observed, or mark
it as advice from seller-provided notes.

## Live practice protocol for authorized fictional role-play

First distinguish two user intents rather than forcing them into
the same format:

- **INTERACTIVE_REHEARSAL:** The user wants to practice as the rep. Run
  one buyer utterance at a time, then stop for their actual response.
  This is the default when they say "role-play with me" or "practice."
- **DEMONSTRATION:** The user explicitly asks for a complete **fictional
  sample dialogue** to study. A short original two-voice illustration
  is permitted, with every turn marked `SIMULATED / DEMO_ONLY`.
  Never grade the user's actual selling skills from that invented
  example, claim either voice represents a real buyer, or silently
  turn a demonstration into a CRM record.

For **INTERACTIVE_REHEARSAL**, a session is a **turn-by-turn
interaction**, not permission to write both sides of a transcript.
Run this lightweight cycle:

1. **SETUP:** Agree on the rep's practice objective, fictional buyer role,
   constraints (such as time, product, stakes), and whether feedback arrives
   after each rep turn or at the end. If the user supplies no settings,
   choose one plausible **explicitly fictional** buyer and a brief opening
   scenario. Do not claim to model a real identified person's thoughts.
2. **PLAY:** Produce **one buyer utterance**, then stop for the rep's reply.
   The buyer may disagree, have no business pain, need another stakeholder,
   ask for a pause or decline entirely. Never write the rep's reply on
   their behalf, pretend a fictional statement was recorded, or claim a
   next turn occurred without input.
3. **OBSERVE:** Track only simulated statements and actual user-written rep
   responses within the present authorized chat. Mark buyer lines
   `SIMULATED` and rep moves `ROLE_PLAY_OBSERVED`. Do not turn role-play
   facts into a real deal ledger, a customer contact record or a personal
   performance history.
4. **COACH:** When feedback is requested or the agreed rehearsal ends,
   select **one specific rep behavior** supported by a quoted or
   accurately summarized practice turn, explain its buyer impact, and offer
   an alternative phrasing that preserves buyer autonomy. Point out one
   strength if evidenced, but avoid a generic motivational speech.
   If the simulated buyer opts out, test the rep's respectful stop,
   not a technique to reverse refusal.
5. **CONTINUE OR CLOSE:** Let the rep choose another turn, a different
   stakeholder, a coaching recap or an end. Preserve the agreed fictional
   role and objective across immediate follow-ups where visible;
   do not invent hidden conversation memory or schedule practice.

**Acceptance:** A successful interactive rehearsal produces a usable next
buyer turn *or* an evidence-linked coaching action, not a complete
fabricated call. A requested DEMONSTRATION instead produces an
explicitly fictional example, never observed rep performance.
A debrief from only seller-provided call notes is not an observed role-play
and must not be scored as one. No hosted voice connection, CRM, simulator
runtime, persistence, sales credential or vendor course content is required.

