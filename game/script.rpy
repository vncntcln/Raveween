# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define p = Character("Poliana", color="#FF885B")
define o = Character("Onyx", color="#16325B")
define aj = Character("Ajax", color="#16423C")
define am = Character("Amalia", color="#821131")
define pc = Character("Poliana & Amalia")

image a1 = im.Scale("images/bgs/a1.jpg", 1920, 1080)
image a2 = im.Scale("images/bgs/a2.jpg", 1920, 1080)
image a4 = im.Scale("images/bgs/a4.jpg", 1920, 1080)


image poliana = "images/poli/Poliana.png"

# The game starts here.

label start:
    #Gameflow

    #Introduction - Story Telling
    call intro1
    
    #Black Screen - Title
    call title
    
    #At the party edges
    call s1p1

    #Black Screen - Title
    call bscreen

    return

label intro1:

    scene a2 with fade

    "We live in a mysterious world, under the chains of our virtues and vices we follow along society's path…"

    "What you are about to see, is the story of those who endure adversity while enveloped by anxieties and the dread of being, those immersed in a path of distrust, those that are lost in the eternal diversity of life, those who look."

    "In the search for good times, we get blindsided by what stops us, the ones who keep moving, to the beat of the music, to the beat of the soul, are our subject today."

    "May you keep moving as well."

    return

label title:
    image black = "images/bgs/black.png"
    scene black
    pause 1.0
    show text "PARTY OF FEAR"
    pause 1.0
    hide text with fade
    return

label bscreen:
    scene black
    pause 1.0
    hide text with fade
    return

label splashscreen:
    #$renpy.movie_cutscene("c.webm")
    return

label s1p1:
    scene a4
    show poliana happy

    p "Oh good God! We’re finally here!"

    o "Yeah, it was funny how we almost got lost on the way here"

    p"We almost got lost!? I didn’t notice it, I was trusting you 100\%...\ Wait a minute"

    p "Oh my God! That music fucking slaps! I wonder who is playing right now"

    o "You get sidetracked really easily, Poliana! I’ve have no idea as to who is playing right now, I forgot to check the timetable before coming here, but I believe it should be either DJ Lau or DJ Elk by the way the beat is progressing"

    p "Huh, we should go check the main stage soon! But wait, have you heard from Janice? Wasn’t she supposed to be here already?"

    o "Well, as she got here earlier, she must be lost somewhere on the party… We should go looki*"

    aj "Sorry to interrupt fellas, how are ya doing? Does any of ya have a lighter so I could light my cig?"

    p "…"
    
    p "That’s strange, he looks a tad bit too young to be here, but he has the voice of some old hooligan, I wonder where he came from."

    o "Hm… Are you sure you are allowed here buddy?"

    o "He looks even younger than Poliana, should I worry about his ID? I know that a party in an abandoned warehouse isn’t expected to follow some strict rules…"

    aj "WHAT OF COURSE I AM! I just got a pretty good skin care routine… Anyway, sorry if we got started on the wrong foot mate, the name is Ajax"

    p "Be sure to take it easy buddy, my name is Poliana!"

    o "And I’m Onyx"

    aj "Poliana and Onyx! Great names!"

    aj "So! What do you guys expect from this ‘MONSTROUS’ Rave!?"

    o "Welp, I dunno to be honest, I got my invitations late and wasn’t expecting to come here before only like, two days ago, so my only hope is to have fun!"

    o "Yeah, that’s what I want, I hope grandma is alright, she insisted on me coming even though today was the penultimate chapter of our favorite ‘novela’, I hope we get to watch it together soon."

    p "Hmmm, I just wanna have a good time with my friends, and maybe even meet some cool new people!"

    p "Honestly I just wanna drink enough till I forget my own name, what a shitty week I had."

    o "And what about you Ajax?"

    am "Well, I hope to meet with some old acquaintances and eat some good dinner here soon, the munchies are killing me!"

    p "Wait! There’s food at this party? That’s cool as hell, I might go looking for that later!"

    o "…"

    o "That’s weird, from what I read before, there would be no food here, only alcohol, I wonder if it was a recent addition."

    aj "Hahaha, sure, good luck, I already know where I’m gonna be filling meself up though!"

    aj "Anyway, it was a good chat, see ya ‘round later, thanks for the lighter!"

    o "What a strange little guy…"

    p "For sure, but he seems inoffensive at least."

    o "Yeah, I guess so, anyway, we should go looking for Janice, she must be feeling lost!"

    am "Excuse me, have you seen…"

    pc "We almost got lost!? I didn’t notice it."

    return