# No-code procedure: route a case citation

Use this when the host cannot run code. It replaces the citation parser of
[this skill](SKILL.md) with a manual parse. Judgement and the routing table
are enough; no calculation is needed. A manual parse proves nothing about
whether the decision exists.

Grammar: [case law verification method](../../references/case-law-verification-method.md).

## Steps

1. Copy each citation exactly as supplied.
2. Decide its type:
   - medium-neutral: `[YEAR] COURT NUMBER`, for example `[2023] HCA 12`;
   - reported: `(YEAR) VOLUME SERIES PAGE`, for example `(2020) 94 ALJR 1`;
   - case name only, for example `Smith v Jones`;
   - unknown, when it fits none of these. A reported form with the year in
     square brackets, such as `[1990] 1 Qd R 1`, is recorded as unknown, as
     the automated parse does; route it by court under the skill's step 3.
3. Read the court identifier (medium-neutral) or the report series
   (reported) and route it with the table in the skill's step 2.
4. A case name only is routed by any stated court or jurisdiction; if none is
   stated, ask which court decided it. Never guess a court from a name.
5. An unrecognised series or court identifier is `UNVERIFIABLE` until the
   court is identified.

## Worksheet

| Citation as supplied | Type | Year | Court identifier or series | Volume | Number or page | Issuing court | Route |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Result

Use the skill's result contract for each citation. In the Routing note write
`parsed manually`. Routing never outputs `VERIFIED`.
