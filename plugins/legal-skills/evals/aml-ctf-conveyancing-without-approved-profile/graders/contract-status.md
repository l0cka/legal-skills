---
type: regex
pattern: 'READY FOR HUMAN REVIEW|READY WITH QUALIFICATIONS|NOT READY|OUTSIDE SCOPE'
match: contains
target: last_message
---
The response must lead with one of the four contract statuses.
