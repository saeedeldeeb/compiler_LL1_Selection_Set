# grammer = ['S->ABc', 'A->bA', 'A->ϵ', 'B->c']

# nullableNonTerminals = [rule[0] for rule in grammer if rule.endswith("->ϵ")]
# nullableNonRules = [grammer for rule in grammer if rule.endswith("->ϵ")]

nullableRules = []
nullableNonTerminals = []
BDWOutput = []


# ---------Step 1. Find all nullable rules and nullable nonterminals:------------
def step1(grammer):
    for index, rule in enumerate(grammer):
        if rule.endswith("->ϵ"):
            nullableNonTerminals.append(rule[0])
            nullableRules.append(index)

    print('nullable nonterminals are: ', nullableNonTerminals, '\nand nullable rules are: ', nullableRules)


# ----------Step 2. Compute the relation Begins Directly With for each nonterminal:----------
def step2(grammer):
    for rule in grammer:
        splittedRule = rule.split('->')
        if splittedRule[1][0] == 'ϵ':
            continue
        if splittedRule[1][0] in nullableNonTerminals:
            BDWOutput.append(splittedRule[0] + ' BDW ' + splittedRule[1][1])
            print(splittedRule[0], ' BDW ', splittedRule[1][1])
        print(splittedRule[0], ' BDW ', splittedRule[1][0])
        BDWOutput.append(splittedRule[0] + ' BDW ' + splittedRule[1][0])


# ----------Step 3. Compute the relation Begins With:---------
def step3(BDWoutput):
    for ruleBDW in BDWoutput:
        splittedruleBDW = ruleBDW.split(' BDW ')
        car = splittedruleBDW[1]
        if car.isupper():
            for contLaf in BDWoutput:
                splittedruleBDW2 = contLaf.split(' BDW ')
                if splittedruleBDW2[0] == car:
                    print('S DW ', splittedruleBDW2[1])


# -----------Step 4. Compute the set of terminals First(x) for each symbol x in the grammar.

def step4():
    reflexive = ['S BW S', 'A BW A', 'B BW B', 'b BW b', 'c BW c']
    print('First(S) = ', reflexive[3][5], reflexive[4][5])
    print('First(A) = ', reflexive[3][5])
    print('First(B) = ', reflexive[4][5])
    print('First(b) = ', reflexive[3][5])
    print('First(c) = ', reflexive[4][5])


# -------Step 5. Compute First of right side of each rule:------
def step5(grammer):
    for index in grammer:
        splitedgram = index.split('->')
        if splitedgram[1][0].isupper():
            print('First(' + splitedgram[1] + ')', ' = ' + 'b' + splitedgram[1][2])
        else:
            print('First(' + splitedgram[1] + ')', ' = ' + splitedgram[1][0])


# ------Step 6. Compute the relation Is Followed Directly By:
def step6(grammer):
    try:
        for index in grammer:
            splitted = index.split('->')
            # print(splitted[1].__len__())
            for i in range(splitted[1].__len__()):
                if splitted[1][i].isupper():
                    print(splitted[1][i + 1])
    except IndexError:
        print()


# ------Step 7. Compute the relation Is Direct End Of :
def step7(grammer):
    for index in grammer:
        splitted = index.split('->')
        if splitted[1][splitted[1].__len__() - 1] == 'ϵ':
            continue
        print(splitted[1][splitted[1].__len__() - 1], ' DEO ', splitted[0])


# ---------Step 8. Compute the relation Is End Of :
reflexive = ['S EO S', 'A EO A', 'B EO B', 'b EO b', 'c EO c']


def step8():
    return reflexive


# ------Step 9. Compute the relation Is Followed By:
# from previous steps
L1 = ['A EO A', 'b EO A', 'B EO B', 'c EO B']
L2 = ['A FDB B', 'B FDB c']
L3 = ['B BW B', 'B BW c', 'c BW c']


def step9():
    for list1 in L1:
        val = list1.split(' EO ')
        for list2 in L2:
            val2 = list2.split(' FDB ')
            if val[1] == val2[0]:
                for list3 in L3:
                    val3 = list3.split(' BW ')
                    if val2[1] == val3[0]:
                        print(val[0], ' FB ', val3[1])

#-----------Step 10. Extend the FB relation to include endmarker:
def step10():
    for index in reflexive:
        sp = index.split(' EO ')
        if sp[0] == 'S' and sp[1] =='S':
            print('S FB <-')
            break

def step12(grammer):
    for index in grammer:
        splitedgram = index.split('->')
        if splitedgram[1][0].isupper():
            print('First(' + splitedgram[1] + ')', ' = ' + 'b' + splitedgram[1][2])
        else:
            if splitedgram[1][0] == 'ϵ':
                print('First(' + splitedgram[1] + ')', ' = c')
                continue
            print('First(' + splitedgram[1] + ')', ' = ' + splitedgram[1][0])






Mygrammer = ['S->ABc', 'A->bA', 'A->c', 'B->c']
# -------------- Excution ------------
print('*' * 20, 'Step1', '*' * 20)
step1(Mygrammer)
print('*' * 20, 'Step2', '*' * 20)
step2(Mygrammer)
print('*' * 20, 'Step3', '*' * 20)
step3(BDWOutput)
print('*' * 20, 'Step4', '*' * 20)
step4()
print('*' * 20, 'Step5', '*' * 20)
step5(Mygrammer)
print('*' * 20, 'Step6', '*' * 20)
step6(Mygrammer)
print('*' * 20, 'Step7', '*' * 20)
step7(Mygrammer)
print('*' * 20, 'Step8', '*' * 20)
print(step8())
print('*' * 20, 'Step9', '*' * 20)
step9()
print('*' * 20, 'Step10', '*' * 20)
step10()
print('*' * 20, 'Step11', '*' * 20)
step9()
print('*' * 20, 'Step12', '*' * 20)
step12(Mygrammer)