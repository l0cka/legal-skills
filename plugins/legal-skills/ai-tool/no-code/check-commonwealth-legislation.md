# No-code procedure: check Commonwealth legislation

Use this when the host cannot run code. It replaces the Federal Register of
Legislation lookup in [this skill](SKILL.md) with steps a person or a
browsing tool follows. A spreadsheet cannot stand in for this: the status
and version of a law are live facts read from the official register.

Method: [register method](references/register-method.md).

## Steps

1. Search `legislation.gov.au` for the title and open its official title
   page. Record the Title ID (`C` for an Act, `F` for a legislative
   instrument), the name, the collection and whether it is an Act or an
   instrument.
2. Open the All versions page. Pick the compilation whose start and end
   dates cover the requested date. Record the compilation number, Register
   ID, start date and end date.
3. Read the status history and any amendments that have commenced but are
   not yet incorporated.
4. Open Downloads and confirm the authorised PDF stamp before calling a
   version authorised.
5. Fill the record below only from pages actually opened. Write
   `not established` for any field not inspected.

## Record

| Field | Value | Page opened (URL) | Opened on |
| --- | --- | --- | --- |
| Title and Title ID | | | |
| Act or instrument; collection | | | |
| Compilation number and Register ID | | | |
| Compilation start and end dates | | | |
| Status (in force, repealed, ceased) | | | |
| Commenced amendments not yet incorporated | | | |
| Authorised PDF stamp seen | | | |

## Result

If nothing was opened, return `NOT VERIFIED` with the steps above and ask the
person to supply the page text or the compilation. Otherwise follow the
skill's result contract and say that the lookup was manual.
