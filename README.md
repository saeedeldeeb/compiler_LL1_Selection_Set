# Algorithm to find selection sets
1. Find nullable rules and nullable nonterminals.
2. Find Begins Directly With relation (BDW).
3. Find Begins With relation (BW).
4. Find First(x) for each symbol, x.
5. Find First(n) for the right side of each rule, n.
6. Find Followed Directly By relation (FDB).
7. Find Is Direct End Of relation (DEO).
8. Find Is End Of relation (EO).
9. Find Is Followed By relation (FB).
10. Extend FB to include endmarker.
11. Find Follow Set, Fol(A), for each nullable nonterminal, A.
12. Find Selection Set, Sel(n), for each rule, n.
# Step 1. Find all nullable rules and nullable nonterminals:
• All є rules are nullable rules.
• The nonterminal defined in a nullable rule is a nullable nonterminal.
• All rules in the form A → BCD...
• where B, C, D, ... are all nullable non-terminals, are nullable rules;
the nonterminals defined by these rules are also nullable nonterminals.
# Step 2. Compute the relation Begins Directly With for each nonterminal:
• A BDW X if there is a rule A → αXβ such that:
▪ α is a nullable string (a string of nullable nonterminals).
▪ A represents a nonterminal and X represents a terminal
or nonterminal.
▪ β represents any string of terminals and nonterminals.
# Step 3. Compute the relation Begins With:
• BW is the reflexive transitive closure of BDW.
• In addition, BW should contain pairs of the form a
BW a for each terminal a in the grammar.
# Step 4. Compute the set of terminals First(x) for each symbol x in the grammar.
• First(A) = set of all terminals b, such that A BW b
for each nonterminal A.
• First(t) = {t} for each terminal t.
# Step 5. Compute First of right side of each rule:
• First (XYZ...) = First(X)
U First(Y) if X is nullable
U First(Z) if Y is also nullable
# Step 6. Compute the relation Is Followed Directly By:
• B FDB X
• if there is a rule of the form A → αBβXγ
• where β is a string of nullable nonterminals, α, γ are
strings of symbols, X is any symbol, and A and B are
nonterminals.
# Step 7. Compute the relation Is Direct End Of :
• X DEO A
• if there is a rule of the form: A → αXβ
• where β is a string of nullable nonterminals, α is a
string of symbols, and X is a single grammar symbol.
12
c DEO S (from rule 1)
A DEO A (from rule 2)
b DEO A (from rule 2, since A is nullable)
c DEO B (from rule 4)
# Step 8. Compute the relation Is End Of :
• X EO Y
• EO is the reflexive transitive closure of DEO.
13
c DEO S
A DEO A
b DEO A
c DEO B
c EO S
A EO A (from DEO)
b EO A
c EO B
(no transitive entries)
c EO c
S EO S (reflexive)
b EO b
B EO B
# Step 9. Compute the relation Is Followed By:
• W FB Z
• If W EO X and X FDB Y and Y BW Z
• then W FB Z
# Step 10. Extend the FB relation to include endmarker:
• A FB ← if A EO S where A represents any nonterminal
and S represents the starting nonterminal.
15
c EO S
A EO A (from DEO)
b EO A
c EO B
(no transitive entries)
c EO c
S EO S (reflexive)
b EO b
B EO B
S FB ← because S EO S
# Step 11. Compute the Follow Set for each nullable nonterminal:
• Fol(A) = {t: A FB t}
• Fol(A) = {c} since A is the only nullable nonterminal
and A FB c.
16
S → ABc
A → bA
A → є
B → c
# Step 12. Compute the Selection Set for each rule:
• i. A → α
• if rule i is not a nullable rule, then Sel(i) = First(α)
• if rule i is a nullable rule, then Sel(i) = First(α) U Fol(A)
1
