from random import choice
mylist=['1','2','3']
while True:
    yourchoice=input('if you want to play mad libs enter yes, otherwise no ')
    if yourchoice=='yes':
        templates_choise = choice(mylist)
        if  templates_choise == '1':
            number = (input('type a number '))
            masure_of_time = input('type masure of time ')
            mode_of_transportation = input('type mode of transportation ')
            abjective = input('type an abjective ')
            abjective_2 = input('type an abjective again ')
            noun = input('type a noun ')
            color = input('type a color ')
            part_of_body = input('type a part of the body ')
            verb = input('type a verb ')
            number2 = (input('type a number again '))
            noun2 = input('type a noun again ')
            noun3 = input('type a noun again ')
            part_of_body2 = input('type a part of body again ')
            verb2 = input('type a verb')
            noun4 = input('type a noun again ')
            abjective3 = input('type an abjective again ')
            silly_word = input('type a silly word ')
            noun5 = input('type a noun ')
            templates1 = (f'''it was about {number} {masure_of_time} ago when I arrived at the hospital in a  
            {mode_of_transportation} the hospital is a {abjective} place there are a lot of  
            {abjective_2} {noun} here. there are nurses here who have {color} {part_of_body}.  
            if someone wants to come in my room i told them that they have to {verb} first. 
            i have decorated my room with {number2} {noun2}. Today i talked to a doctor and they 
            were wearing a {noun3} on their {part_of_body2}. Iheard that all doctors {verb2} {noun4} 
            every day for breakfast. The most {abjective3} thing about beaing in the hospital 
            is the {silly_word} {noun5}.''')
            print (templates1)
        elif templates_choise == '2':
            persons_name = input('type a persons name ')
            noun6 = input('type a noun ')
            abjective_feeling = input('type an abjective feeling ')
            verb3 = input('type a verb ')
            abjective_feeling2 = input('type an abjective feeling ')
            animal = input('type an animal ')
            verb4 = input('type a verb again ')
            color2 = input('type a color ')
            verbing = input('type a verb (ending in ing) ')
            adverb_ending_in_ly = input('type an adverb (ending in ly) ')
            number3 = input('type a number ')
            measure_of_time = input('type a measure of time ')
            color3 = input('type a color ')
            animal2 = input('type an animal ')
            number4 = input('type a number ')
            silly_word2 = input('type a silly word ')
            noun7 = input('type a noun ')
            templates2=f'''This weekend I am going camping with{persons_name}.
                   I packed my lantern, sleeping bag, and{noun6}.I am
                   so {abjective_feeling} to {verb3} in a tent. I am {abjective_feeling2}
                   we might see a(n) {animal}, I hear they`re kind of dangerous. While
                   we`re camping, we are going to hike, fish, and {verb4}. I have heard
                   that the{color2} lake is great for {verbing}. Then we
                   will {adverb_ending_in_ly} hike through the forest for {number3}
                   {measure_of_time}. If I see a {color3} {animal2} while hiking, I am going
                   to bring it home as a pet! At night we will tell {number4} {silly_word2}
                   stories and roast {noun7} around the campfire!!'''
            print(templates2)
        elif templates_choise == '3':
            proper_noun_persons_name = input('type a persnons name ')
            adjective31 = input('type an abjective ')
            color31 = input('type a color ')
            animal31 = input('type an animal ')
            place31 = input('type a place ')
            adjective32 = input('type an adjective ')
            megical_creature31 = input('type a megical creature (plural) ')
            adjective33 = input('type an adjective ')
            megical_creature32 = input('type a megical creature (plural) ')
            room_in_the_house = input('type a room in the house ')
            noun31 = input('type a noun ')
            noun32 = input('type a noun ')
            noun_plural = input('type a noun (plural) ')
            adjective34 = input('type an adjective ')
            noun_plural32 = input('type a noun (plural) ')
            number31 = input('type a numner ')
            measure_of_time31 = input('type measure of tume ')
            verb31 = input('type verb (ending in ing) ')
            adjective35 = input('type an adjective ')
            noun33 = input('type a noun')



            templates3 = f'''Dear {proper_noun_persons_name}, I am writing to you from
                 a {adjective31} castle in an enchanted forest. I found myself here one
                 day after going for a ride on a {color31} {animal31} in {place31}. There
                 are {adjective32} {megical_creature31} and {adjective33} {megical_creature32}
                 here! In the {room_in_the_house} there is a pool full
                 of {noun31}. I fall asleep each night on a{noun32} of {noun_plural} and
                 dream of {adjective34} {noun_plural32}. It feels as though I have lived
                 here for {number31} {measure_of_time31}. I hope one day you can visit,
                 although the only way to get here now is {verb31} on a {adjective35} {noun33}!!'''
            print(templates3)
    elif yourchoice=='no':
        break
    else:
        yourchoice = input('if you want to play mad libs enter yes, otherwise no')




