# Currency audit — 28 October 2026

Scope: watch-register items and dated statements whose trigger dates fell
between the 24 September 2026 audit and 28 October 2026. A primary-source
pass followed on 2 November 2026.

## Method and limits

- A date scan of `plugins/legal-skills` for statements dated 25 September
  2026 to 31 January 2027 found the items below. Items dated after 28 October
  2026 (ADM commencement 10 December 2026, Joint Select Committee report
  30 November 2026, Children's Online Privacy Code 10 December 2026, WA PRIS
  breach scheme 1 January 2027) are still future and were left alone.
- On 28 October the egress proxy blocked the official publishers, so the first
  pass rested on web search and one OAIC page.
- On 2 November the official publishers were read directly from another
  machine. Home Affairs blocked automated access and has no archived copy;
  the PM&C page was read through a search-result scrape.
- None of this moves `lawCheckedOn`, which is an area-wide assertion.

## Results

| Area | Item | Finding | Status (2 Nov) |
| --- | --- | --- | --- |
| employment-fair-work | `clerks-award-working-from-home`; `policy-statutory-hooks.md` | [2026] FWCFB 281 (19 Oct 2026) and determination PR815538 insert clause 5A into the Clerks Award, in operation from 26 Oct 2026 (first full pay period on or after) | Verified on fwc.gov.au and fairwork.gov.au |
| employment-fair-work | `gender-undervaluation-priority-awards` | Stage 1 of five under [2026] FWCFB 231 / PR814029 operates from 1 Oct 2026. The award is the Health Professionals and Support Services Award 2020 (health professionals only), not the Health Services Award | Corrected from fwc.gov.au |
| employment-fair-work | `non-compete-ban` | Exposure draft only; an APH search found no Bill introduced. Treasury and law firms use different Bill titles | Strong evidence, not confirmation |
| aml-ctf | `amlctf-amendment-bill-2026` | Before the Senate (second reading moved 12 Oct 2026); no assent. The revised EM keeps the LPP-form change; the supplementary EM describes no House amendment to it | Verified on aph.gov.au (passed text not read) |
| aml-ctf | `lpp-ministerial-guidelines` | No final guidelines on the Federal Register (three searches); AUSTRAC still says the Minister "will issue" them; Home Affairs page unreachable | Not made on the public record (register lag possible) |
| ai-governance, privacy-cybersecurity | `oaic-adm-guidance`; `automated-decision-method.md` | APP Guidelines chapter 1 Version 2.0 updated 30 Sep 2026, with APP 1.7–1.9 fact sheets and flowchart | Verified on oaic.gov.au |
| ai-governance | `pmc-ai-infrastructure-consultation`; source-and-control method | Closed 5 pm AEDT 9 Oct 2026; page says outcomes "will be made available in due course" | Verified on pmc.gov.au |

## Next steps

- Recheck the Federal Register for the s 242A guidelines at the next audit.
- Read the AML/CTF Bill's third-reading text to confirm the LPP items.
- Close `oaic-adm-guidance` once the privacy skills have been run against the
  new guidance.
