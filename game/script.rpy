label start:
    #Gameflow

    #Introduction - Story Telling
    call intro1
    
    #Black Screen - Title
    call title
    
    #Act 1 Scene 1 - at the party edges
    call a1s1

    #Black Screen
    call bscreen

    #Act 1 Scene 2 - at the party edges
    call a1s2

    #Black Screen
    call bscreen

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