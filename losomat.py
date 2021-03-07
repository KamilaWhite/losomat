from random import choice
import random


names = ["Adamina ", "Makryna ", "Lukrecja", "Eustazy ", "Gniwko  ", "Zygfryd "]
COMPANY_1 = ["FOO_1_desktop", "FOO_1_mobile", "FOO_2_desktop", "FOO_2_mobile", "FOO_3_desktop", "FOO_3_mobile"]
COMPANY_2 = ["BAR_1_desktop", "BAR_1_mobile", "BAR_2_desktop", "BAR_2_mobile", "BAR_3_desktop", "BAR_3_mobile", "BAR_4_desktop", "BAR_3_mobile"]
new_environments = []

print ("\n\nWelcome: %s" % ', '.join(names))
print ("\n\n         Today I will chose a DESTYNY for you...")

select = input("\n\nRepeat here from available environments 'COMPANY_1', 'COMPANY_2' or type 'NEW' to enter yours: ").strip().upper()

if select == 'COMPANY_1':
    print("\n\nThe result of the draw is:")
    for name in names :
        a = random.choice(COMPANY_1)
        print (' ' + name + " take " + a)
        COMPANY_1.remove(a)
    if len(COMPANY_1) != 0:
        print("\n\nNot selected Environments: %s" % COMPANY_1)

if select == 'COMPANY_2':
    print("\n\nThe result of the draw is:")
    for name in names :
        a = random.choice(COMPANY_2)
        print (' ' + name + " take " + a)
        COMPANY_2.remove(a)
    if len(COMPANY_2) > 0:
        print("\n\nNot selected Environments: %s" % COMPANY_2)

if select == 'NEW':
    new_environments = input("\n\nPlease, type an environments: ").strip().replace(' ', '').split(",")
    print("\n\nThe names you have entered so far: %s" % new_environments)

    while True:
        add_next = input("\n\nWould you like to add more environments? If yes - type more, if no - type 'n': ").strip().lower().replace(' ', '').split(",")

        if add_next[0] != 'n':
            new_environments = new_environments + add_next
            print("\n\nThe names you have entered so far: %s" % new_environments)

        else:
            print("Ok, I will randomly choose from those entered")
            break

    print("\n\nThe result of the draw is:")
    for name in names :
        a = random.choice(new_environments)
        print (' ' + name + " take " + a)
        new_environments.remove(a)

    if len(new_environments) != 0:
        print("\n\nNot selected Environments: %s" % new_environments)