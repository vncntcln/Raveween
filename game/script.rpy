label start:
    #Gameflow

    play music "audio/(opening) a night to remember.mp3" volume 0.1

    #Introduction - Story Telling
    call intro1
    
    #Black Screen - Title
    call title
    
    #Act 1 Scene 1 - at the party edges
    call a1s1

    #Black Screen
    call bscreen

    #Obsession
    stop music fadeout 3.0

    play music "audio/the 90s called.mp3" volume 0.1 fadein 3.0
    
    #Act 1 Scene 2 - at the party edges
    call a1s2

    #Lost
    stop music fadeout 3.0

    play music "audio/monster theme 1 a.mp3" volume 0.1 fadein 3.0

    #Transition to Act 1 Scene 3
    call transition2t3

    #Add Scene 3
    call a1s3

    #Together Starts
    stop music fadeout 3.0

    play music "audio/humans rule.mp3" volume 0.1 fadein 3.0

    #Add Scene 4
    call a1s4

    #Toxic
    stop music fadeout 3.0

    play music "audio/bauhaus a.mp3" volume 0.1 fadein 3.0

    #Add Scene 5
    call a1s5

    #Among Fear Begin
    stop music fadeout 3.0

    play music "audio/demon party.mp3" volume 0.1 fadein 3.0

    #Add Scene 6
    call a1s6

    #Together Chaos
    stop music fadeout 3.0

    play music "audio/from hell.mp3" volume 0.1 fadein 3.0

    #Add Scene 7
    call a1s7

    #Add Scene 8
    call a1s8

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

label transition2t3:
    image black = "images/bgs/black.png"
    scene black
    pause 1.0
    show text "Meanwhile"
    pause 1.0
    hide text with fade
    return