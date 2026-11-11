# No-code procedure: check NSW legislation

Use this when the host cannot run code. It replaces the NSW legislation URL
helper in [this skill](SKILL.md) with steps a person or a browsing tool
follows. A spreadsheet cannot stand in for this: currency and commencement
are live facts read from the official site.

Method: [NSW legislation method](references/nsw-legislation-method.md).

## Steps

1. Search `legislation.nsw.gov.au` and open the status page of the title.
   Record the exact title, type, year and number, the website identifier
   (for example `act-1987-015`) and whether it sits in In force or Repealed.
2. For a historical date, open the Legislative history table of versions and
   pick the version covering the date. The site serves historical versions
   under an `inforce/<YYYY-MM-DD>` route; cite a page only if you opened it.
3. Read Status Information (Currency of version, Provisions in force, Notes)
   and the Legislative history for commencement and amending legislation.
4. Fill the record below only from pages actually opened. Write
   `not established` for any field not inspected.

## Record

| Field | Value | Page opened (URL) | Opened on |
| --- | --- | --- | --- |
| Title, type, year and number | | | |
| Website identifier | | | |
| In force or Repealed | | | |
| Version covering the requested date | | | |
| Currency of version | | | |
| Provisions in force and notes | | | |
| Commencement and amending legislation | | | |

## Result

If nothing was opened, return `NOT VERIFIED` with the steps above and ask the
person to supply the page text. Otherwise follow the skill's result contract
and say that the lookup was manual.
