# You can place the script of your game in this file.

init:
    $ left = Position(xpos=0.1, xanchor=0.1,)
    $ center = Position(xpos=0.5, xanchor=0.5,)
    $ right = Position(xpos=0.9, xanchor=0.9,)
    $ question = 0
    
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image brian = "brian.png"
image bg black = "#000000"
image bg intro = "intro.png"
image bg shower1 = "shower1.png"
image bg shower2 = "shower2.png"
image bg shower3 = "shower3.png"
image bg shower4 = "shower4.png"
image bg shower5 = "shower5.png"
image bg bus = "bus.png"
image bg lobby = "lobby.png"
image bg hotelroom = "hotelroom.png"
image bg door319 = "door319.png"
image bg museum = "museum.png"
image bg door316 = "door316.png"
image bg opening1 = "opening1.png"
image bg opening2 = "opening2.png"
image bg opening3 = "opening3.png"
image bg opening4 = "opening4.png"
image bg opening5 = "opening5.png"
image bg opening6 = "opening6.png"
image bg opening7 = "opening7.png"
image bg opening8 = "opening8.png"
image bg opening9 = "opening9.png"
image bg opening10 = "opening10.png"
image bg opening11 = "opening11.png"
image bg opening12 = "opening12.png"
image bg opening13 = "opening13.png"
image bg opening14 = "opening14.png"
image bg opening15 = "opening15.png"
image bg opening16 = "opening16.png"
image bg opening17 = "opening17.png"
image bg opening18 = "opening18.png"
image bg opening19 = "opening19.png"
image bg opening20 = "opening20.png"
image bg opening21 = "opening21.png"
image bg opening22 = "opening22.png"
image bg opening23 = "opening23.png"
image bg opening24 = "opening24.png"
image bg opening25 = "opening25.png"
image bg opening26 = "opening26.png"
image bg opening27 = "opening27.png"
image bg opening28 = "opening28.png"
image bg opening29 = "opening29.png"
image bg opening30 = "opening30.png"
image bg opening31 = "opening31.png"
image bg opening32 = "opening32.png"
image bg opening33 = "opening33.png"
image bg opening34 = "opening34.png"
image bg opening35 = "opening35.png"
image bg opening36 = "opening36.png"
image bg opening37 = "opening37.png"
image bg opening38 = "opening38.png"
image bg opening39 = "opening39.png"
image bg opening40 = "opening40.png"
image bg opening41 = "opening41.png"
image bg opening42 = "opening42.png"
image bg opening43 = "opening43.png"
image bg opening44 = "opening44.png"
image bg opening45 = "opening45.png"
image bg opening46 = "opening46.png"
image bg opening47 = "opening47.png"
image bg opening48 = "opening48.png"
image bg opening49 = "opening49.png"
image bg opening50 = "opening50.png"
image bg opening51 = "opening51.png"
image bg opening52 = "opening52.png"
image bg opening53 = "opening53.png"
image bg opening54 = "opening54.png"
image bg opening55 = "opening55.png"
image bg opening56 = "opening56.png"
image bg opening57 = "opening57.png"
image bg opening58 = "opening58.png"
image bg opening59 = "opening59.png"
image bg opening60 = "opening60.png"
image bg opening61 = "opening61.png"
image bg opening62 = "opening62.png"
image bg opening63 = "opening63.png"
image bg opening64 = "opening64.png"
image bg opening65 = "opening65.png"
image bg opening66 = "opening66.png"
image bg opening67 = "opening67.png"
image bg opening68 = "opening68.png"
image bg opening69 = "opening69.png"
image bg opening70 = "opening70.png"
image bg opening71 = "opening71.png"
image bg opening72 = "opening72.png"
image bg opening73 = "opening73.png"
image bg opening74 = "opening74.png"
image bg opening75 = "opening75.png"
image bg opening76 = "opening76.png"
image bg opening77 = "opening77.png"
image bg opening78 = "opening78.png"
image bg opening79 = "opening79.png"
image bg opening80 = "opening80.png"
image bg opening81 = "opening81.png"
image bg opening82 = "opening82.png"
image bg opening83 = "opening83.png"
image bg opening84 = "opening84.png"
image bg opening85 = "opening85.png"
image bg opening86 = "opening86.png"
image bg opening87 = "opening87.png"
image bg opening88 = "opening88.png"
image bg opening89 = "opening89.png"
image bg opening90 = "opening90.png"
image bg opening91 = "opening91.png"
image bg opening92 = "opening92.png"
image bg opening93 = "opening93.png"
image bg opening94 = "opening94.png"
image bg opening95 = "opening95.png"
image bg opening96 = "opening96.png"
image bg openingfinal = "openingfinal.png"
image kathy = "kathy.png"
image kathy angry = "kathyangry.png"
image kathy frustrated = "kathyfrustrated.png"
image kathy pouting = "kathypouting.png"
image passport = "passport.png"
image security = "security.png"
image bg terminal = "terminal.png"
image tyler = "tyler.png"
image tyler angry = "tylerangry.png"
image tyler baggage = "tylerbaggage.png"
image tyler pushed = "tylerpushed.png"
image tyler pushedflip = im.Flip("tylerpushed.png", horizontal=True)
image tyler shocked = "tylershocked.png"

# Declare characters used by this game.
define t = Character('Tyler', color="#ffffff")
define j = Character('Jimbo', color="#ffffff")
define k = Character('Kathy', color="#ffffff")
define s = Character('Selena', color="#ffffff")
define m = Character('Monica', color="#ffffff")
define c = Character('Silver Crow', color="#ffffff")



# The game starts here.
label start:

# opening animation

scene bg opening1 with Dissolve (.25)

scene bg opening2 with Dissolve (.25)

scene bg opening3 with Dissolve (.25)

scene bg opening4 with Dissolve (.25)

scene bg opening5 with Dissolve (.25)

scene bg opening6 with Dissolve (.25)

scene bg opening7 with Dissolve (.25)

scene bg opening8 with Dissolve (.25)

scene bg opening9 with Dissolve (.25)

scene bg opening10 with Dissolve (.25)

scene bg opening11 with Dissolve (.25)

scene bg opening12 with Dissolve (.25)

scene bg opening13 with Dissolve (.25)

scene bg opening14 with Dissolve (.25)

scene bg opening15 with Dissolve (.25)

scene bg opening16 with Dissolve (.25)

scene bg opening17 with Dissolve (.25)

scene bg opening18 with Dissolve (.25)

scene bg opening19 with Dissolve (.25)

scene bg opening20 with Dissolve (.25)

scene bg opening21 with Dissolve (.25)

scene bg opening22 with Dissolve (.25)

scene bg opening23 with Dissolve (.25)

scene bg opening24 with Dissolve (.25)

scene bg opening25 with Dissolve (.25)

scene bg opening26 with Dissolve (.25)

scene bg opening27 with Dissolve (.25)

scene bg opening28 with Dissolve (.25)

scene bg opening29 with Dissolve (.25)

scene bg opening30 with Dissolve (.25)

scene bg opening31 with Dissolve (.25)

scene bg opening32 with Dissolve (.25)

scene bg opening33 with Dissolve (.25)

scene bg opening34 with Dissolve (.25)

scene bg opening35 with Dissolve (.25)

scene bg opening36 with Dissolve (.25)

scene bg opening37 with Dissolve (.25)

scene bg opening38 with Dissolve (.25)

scene bg opening39 with Dissolve (.25)

scene bg opening40 with Dissolve (.25)

scene bg opening41 with Dissolve (.25)

scene bg opening42 with Dissolve (.25)

scene bg opening43 with Dissolve (.25)

scene bg opening44 with Dissolve (.25)

scene bg opening45 with Dissolve (.25)

scene bg opening46 with Dissolve (.25)

scene bg opening47 with Dissolve (.25)

scene bg opening48 with Dissolve (.25)

scene bg opening49 with Dissolve (.25)

scene bg opening50 with Dissolve (.25)

scene bg opening51 with Dissolve (.25)

scene bg opening52 with Dissolve (.25)

scene bg opening53 with Dissolve (.25)

scene bg opening54 with Dissolve (.25)

scene bg opening55 with Dissolve (.25)

scene bg opening56 with Dissolve (.25)

scene bg opening57 with Dissolve (.25)

scene bg opening58 with Dissolve (.25)

scene bg opening59 with Dissolve (.25)

scene bg opening60 with Dissolve (.25)

scene bg opening61 with Dissolve (.25)

scene bg opening62 with Dissolve (.25)

scene bg opening63 with Dissolve (.25)

scene bg opening64 with Dissolve (.25)

scene bg opening65 with Dissolve (.25)

scene bg opening66 with Dissolve (.25)

scene bg opening67 with Dissolve (.25)

scene bg opening68 with Dissolve (.25)

scene bg opening69 with Dissolve (.25)

scene bg opening70 with Dissolve (.25)

scene bg opening71 with Dissolve (.25)

scene bg opening72 with Dissolve (.25)

scene bg opening73 with Dissolve (.25)

scene bg opening74 with Dissolve (.25)

scene bg opening75 with Dissolve (.25)

scene bg opening76 with Dissolve (.25)

scene bg opening77 with Dissolve (.25)

scene bg opening78 with Dissolve (.25)

scene bg opening79 with Dissolve (.25)

scene bg opening80 with Dissolve (.25)

scene bg opening80 with Dissolve (.25)

scene bg opening81 with Dissolve (.25)

scene bg opening82 with Dissolve (.25)

scene bg opening83 with Dissolve (.25)

scene bg opening84 with Dissolve (.25)

scene bg opening85 with Dissolve (.25)

scene bg opening86 with Dissolve (.25)

scene bg opening87 with Dissolve (.25)

scene bg opening88 with Dissolve (.25)

scene bg opening89 with Dissolve (.25)

scene bg opening90 with Dissolve (.25)

scene bg opening91 with Dissolve (.25)

scene bg opening92 with Dissolve (.25)

scene bg opening93 with Dissolve (.25)

scene bg opening94 with Dissolve (.25)

scene bg opening95 with Dissolve (.25)

scene bg opening96 with Dissolve (.25)

scene bg openingfinal with Dissolve (.25)
    
scene bg black with Dissolve(1)

centered "1 May, 10:05 AM - Airport"

scene bg intro with Dissolve(1)

pause 3.0

scene bg terminal with Dissolve (1)
show tyler baggage with Dissolve(.25)

"Hmm... Where did I put that card..." 

show tyler shocked with Dissolve(.25)

t "Oh..."

show tyler with Dissolve(.25)

"Hi, My name is -"

"???" "..."

show tyler pushed with Dissolve(.15):
    linear .15 xalign 0.85
show brian with Dissolve(.15)

t "...?!" 

"What the?"

"???" "Move it kid"

hide brian with Dissolve(.25)
show tyler pushed:
    linear .25 xalign 0.5
    
t "...?!" 

show tyler pushedflip:
    linear .15 xalign -0.05
show security with Dissolve(.15)


"Again?"

hide security with Dissolve(.25)
show tyler angry with Dissolve(.25):
    linear .25 xalign 0.5


t "...Where are they going in such a hurry?" 

show tyler shocked with Dissolve(.25)

t "Hey... What's this?"

show passport with Dissolve(.25):
    yalign .5 xalign .5

"Someone dropped their passport. - Passport retrieved."

show passport:
    linear .75 xalign 2.0 yalign -1.0
show tyler baggage with Dissolve(.25)

t "...That guy must have dropped it after bumping into me... I Guess I should go and return it before going to the bus stand."

hide passport
show tyler with Dissolve(.25)

"Now where was I... oh yes. My name is Tyler Fox... I'm a recent graduate student majoring in criminal psychology."

"Today I'm at the airport... well... there's a few reasons why I'm in a foreign country."

"The First reason being that I couldn't get a graduate job after graduating... another is because I felt like I needed to get away after breaking up with my ex... but the biggest reason... is because a certain famous thief, who had declared that he be stealing the world's biggest diamond on display in this country."

"And If he is successful... this artifact will be the 7th artifact that he had successfully stolen."

"As a psychology student, this is a very interesting subject... There are so many questions as to why he decides to steal; how she manages to escape every single time; and why he is compelled to announce her target before stealing it..."

"I plan to go to the museum where they the artifact will be displayed and be part of the witness when he appears."

t "Hmm... It would be great if I could capture him in action..."

show tyler shocked at left with Dissolve (.25)
show kathy at right with Dissolve (.25)

"???" "Excuse me, do you know where the bus stand is?"

show tyler with Dissolve(.25)

t "Oh, sure yeah... just over there."

t "Hey..." 

menu:

    "Ask if she wants to go together":

        t "I'm heading there myself, shall we go together?"

        "???" "Oh, hmm..."

        t "... I Don't bite, I swear."

        "???" "Haha, well... alright, I don't see why not."

        t "The name's Tyler by the way. Tyler Fox"

        k "I'm Kathy, Nice to meet you. Kathy... Cat"
        
        show tyler shocked with Dissolve(.25)

        "Kathy... Cat? of all things..." 
        
        show tyler with Dissolve(.25)

        t "What a coincidence, our last names are both animal labels."

        k "I know right? How weird is that!"

        t "...so... why come to this country?"

        k "Oh you know... Just holidaying and stuff... I came to meet a friend here who's a big fan of a band that I like. We're definitely going to go to their concert on the 5th of may."

        t "ah... I see, sounds great. I'm here because-"
        
        show tyler shocked with Dissolve(.25)

        k "Hey, Hold up, I'm going to go toilet for a bit okay?"

        t "Oh... uh... sure"

        show kathy angry with Dissolve(.25)

        k "Here hold my stuff, and you better not leave without me okay?"

        t "okay..."

        show tyler with Dissolve(.25)
        show kathy with Dissolve(.25)
        hide kathy with moveoutright

        t "There she goes..."

        t "Hmm... There's a lock on all of her luggages, that's rather excessive... Oh? There's a magazine sticking out of the side pocket, Guess I'll take a read while waiting."

        "Magazine retrieved"

    "Be awkward and wait for the next bus.":

        ""
        
scene bg black with Dissolve(1)

centered "1 May 11:00 AM - Bus ride" 

#bus sound start

scene bg bus

show kathy at right
show tyler at left

k "Thanks for waiting for me"

t "No problem"

"well... since she's being cute about it... I guess half an hour wasn't too long..."

k "So tell me Tyler, What cha gonna do here?"

t "Oh I'm here to catch Silver Crow in action."

k "Silver Crow? you mean the Jewel thief?"

t "Yeah! Well... he doesn't only steal jewels... He always aims for the major attraction on display and does it in a grand and dangerous manner... Nobody knows why."

t "I'm actually going to a friend I've met online who is also interested in this after dropping my bags at the hotel."

k "haha, yeah, I've heard about Silver crow but I've never really paid enough attention to the details."

show tyler shocked with Dissolve(.25)

t "Oh... yeah, sorry for the nerd talk... "

show tyler with Dissolve(.25)

k "So have you met this online friend before?"

t "Oh no, I've never even seen a picture of her, she is quite shy you see."

show kathy frustrated with Dissolve(.25)

k "Ooh... you like those type do you?"

t "Oh no no, we are strictly friends! We're just meeting  because of our matching interests."

show kathy with Dissolve(.25)

k "Well... tell me more about her! what's her name?"

"Why is she so interested?" 

t "...Her name is Selena Bella, She just loves The Silver crow. Apparently it's because she loved phantom thief fictional characters as a child. You know... like... magic kaito and Lupin and stuff..."

k "What's... that?"

t "Some Japanese anime characters."

k "Oh I see... she sounds like a nerd..."

t "Haha, well I guess we're both nerds."

t "Anyways! Silver Crow is like a dream come true for her."

k "hmm... Can you describe her to me?"

t "I told you, I've never seen her."

k "Surely she's told you what she looks like since you're going to meet her? How would you know when you see her?"

t "Well... she told me she will be in the museum filming and taking pictures... She's going to wear an orange beanie, she wears glasses, and..."

"She has a tattoo of lupin on her hip... but Kathy doesn't need to know that"

t "... and she sent me one picture of her."

k "well... show me the picture then!"

t "Well... no harm done I suppose..."

"Here it is."

#Picture of Selena added into inventory

k "Well... it looks like you've got it all planned out huh?"

t "I guess... So... what about you?"

k "Oh you know, I'm here to watch a band I like... The Bagelboys, Ever heard of them?"

t "Oh yeah... I... sort of."

k "Yeah! I came all the way to this country just to see them live! I guess I'm a nerd too! <E"

t "haha... a different kind of nerd perhaps."

k "What does your parents do for a living?"

t "Oh... my dad used to be a doctor."

k "used to be?"

t "Yeah, they died 2 years ago in a car crash..."

k "Oh... I'm so sorry..."

t "Oh no, don't be, I've cried my fair share and now i'm fine..."

"as fine as I'll ever be..."

k "I don't know how that must have felt... I would never know the feeling of losing my parents..."

t "...eh?"

k "I'm an orphan you see... I've never met my parents in my life. I grew up in an orphanage."

t "Oh wow... I've never met an orphan before..."

k "I suppose the maid that took care of me as a child is kind of like a mom to me, I haven't seen her for years though, haha."

t "Well that makes us both alone without family... I think we'll get along fine."

k "... Yeah..."

t "Oh... oops..."

k "?"

t "Ah... Nothing, I just forgot to return this passport I found at the airport... I Guess I'll return it later."

show kathy frustrated with Dissolve(.25)

k "!? Where did you find it?"

t "On the ground? Someone must have dropped it."

k "... You should return it"

t "Yeah I will"

show kathy with Dissolve(.25)

k "Shall I return it for you?"

t "Oh no, don't worry about it. I'll return it later."

#Halt, Stop

k "Ah... We're here."

scene bg black with Dissolve(1)
#Scene change - Hotel Lobby

scene bg lobby

show tyler with Dissolve(.25)

t "Mmm... Not too shabby..."

"I wonder what my room will look like"

show tyler shocked with Dissolve(.25)

j "Hello sir, My name is Jimbo, how may I be of assistance?"

show tyler with Dissolve(.25)

t "Ah yes... I've booked a room here. Here's my passport."

j "right away sir. Here's your cardkey, Room 319."

t "Thanks."

j "Is there anything else you I can do for you sir? I'm here to answer any questions you have."

label butlerquestions1:

menu:

    "Ask about tourist attractions":

        label butlerquestions11:

        t "So... What's there to do here?"

        j "Well sir... Truth is I don't really know what's so great about this place."

        t "Wha..."

        j "But from what I've heard from other tourists.... most are either here for the Silver Crow or the Bagelboys. Oh... but not so much theBagel boys anymore."

        "Not anymore? Hmm... I'm not really interested to begin with... should I pry further?"
        
        $ question = question | 1
        if question == 7:
            jump butlerquestion1finish
            
        else:
            jump butlerquestions1

    "About these Bagelboys...":

        label butlerquestions12:

        j "They're a popular band consisting of 4 male members. They Debut last year, and are due to perform in 3 days... at the South concert hall."

        t "Ah... Okay..."

        j "Word has it though, one of them was involved a scandal yesterday and the band members are fighting each other... now the concert might be cancelled due to the whole situation."

        "Oh my... I wonder if Kathy has found out about this..."
        
        $ question = question | 2
        if question == 7:
            jump butlerquestion1finish
            
        else:
            jump butlerquestions1

    "Silver Crow! That's what I'm here for.":

        label butlerquestions13:

        j "Ah... I see, Well... Silver Crow is still losing."

        t "Losing?"

        j "Yeah, I've been counting. You're here for Silver Crow, so that adds one to 13 people here for Silver Crow and 41 Here for BagelBoys."

        t "...Right."
        
        $ question = question | 4
        if question == 7:
            jump butlerquestion1finish
            
        else:
            jump butlerquestions1

label butlerquestion1finish:

menu:

    "Ask about tourist attractions":

        jump butlerquestions11

    "About these Bagelboys...":

        jump butlerquestions12

    "Silver Crow! That's what I'm here for.":

        jump butlerquestions13

    "Nah I'll be alright, Which way to the elevator?":

        $ question = 0

        j "Turn left on that corner sir, I've got to warn you though, the elevator is quite slow."

        t "No worries, See ya."

        j "Have a pleasant stay sir."

#Screen Fade out

scene bg black with Dissolve (1)

#Scene change - Room door 319

scene bg black with Dissolve(5)

scene bg black with Dissolve(3)

scene bg door319

"Finally... took me 15 minutes just to get up here cause some dumb kid pressed all the buttons in the elevator"

t "Hm...? The cardkey is not working... Oh wait... the door is unlocked. That's really strange... Did the cleaners forget to lock the door or something?"

#Screen Fade out

scene bg black with Dissolve(3)

#Scene change - Hotel Room

scene bg hotelroom

"Hotel room smells fresh with a hint of Jasmine"

t "Mmmm... I wish my own room at home smells like this."

#click sound

t "...Click?"

"She locked me out... Getting dressed probably"

#animation code

scene bg shower1 with Dissolve (1)
$ renpy.pause(1.0)
scene bg shower2 with Dissolve (1)
$ renpy.pause(1.0)
scene bg shower3 with Dissolve (1)
$ renpy.pause(.5)
scene bg shower4 with Dissolve (1)
$ renpy.pause(.25)
scene bg shower5 with Dissolve (1)
$ renpy.pause(.5)

"Before I realize it, She was standing in front of me with a mean look in her eye."

k "You pervert!... How did you get into my room? I should call the security and have you removed!"

t" But... This is MY room, See? I have a card key."

scene bg black with Dissolve(.25)
scene bg hotelroom with Dissolve(.25)
show tyler at left with Dissolve(.25)
show kathy angry at right with Dissolve(.25)

k "Oh...? let me see... your card key says that you are in room 319. That's next door, you idiot."

t "What? No way, you're the one mistaken, see...?" 

#(Kathy fades, reveal room 316)

scene bg door316

show tyler shocked at left with Dissolve(.25)

"...Wha? 316?? but... but... I checked! I double checked!"

show kathy frustrated at right with Dissolve(.25)

k "...Okay mister... I don't care how you got in, but you owe me... you owe me BIG."

t "Okay okay, it's my fault, I'm sorry."

show kathy pouting at right with Dissolve(.25)

k "Sorry ain't gonna cut it Tyler."

t "Well... What do you want me do?"

k "I'm going to go shopping after I rest."

t "Yeah?"

k "You're coming with me."

t "Eehh?? But... But I can't! I have to meet Selena at the museum at 3."

k "...Would you rather I make a big fuss with the hotel and have you kicked out for breaking into my room?"

t "...but I didn-"

k "You practically saw me naked! I don't care what you say, you clearly owe me."

t "Okay... um... how 'bout this... I'll meet Selena today... and you can have me for the whole day tomorrow."

k "But I want to go now!"

t "Come on, we're all tired, and I don't want to make my friend mad.... help me out please?"

show kathy with Dissolve(.25)

k "... Fine, tomorrow then. I'll wait for you at the lobby at 9:00 AM, you better not be late."

hide kathy with moveoutright
show tyler at center:
    linear .35 xalign 0.5

t"Phew... I must be jetlagged to mix up the rooms like that, I should get a quick snooze before meeting Selena"

scene bg black with Dissolve(1)

centered "1 May 3:20 PM - Museum"

scene bg museum

show tyler angry with Dissolve(.25)

"Crud, I overslept I hope Selena is still there."

show tyler angry at left:
    linear .35 xalign .1
show tyler shocked with Dissolve(.25)

"???" "Are you Tyler?"

t "Are you... Selena?"

s "Yup, like my beanie?"

show tyler with Dissolve(.25)

"Well... someone that looks as good as advertised on photo for once"

t "Uh... Sure do! Sorry I'm late."

s "Late? Oh no worries! I would have been here waiting for Silver Crow to appear whether you were here or not."

t "Haha, you sound as outgoing as you are online... I thought you'd be more reserved in real life like you said."

s "Well..."

t "...."

s "..."

"... I guess she IS quite reserved."
t "So, what's the situation?"

s "I'm quite excited, Silver Crow will appear sometime before the 5th... I hope that he will appear when the museum is still open like all his other heist."

t "That makes the two of us, I'd actually like the police to catch him in action so I can see him upclose... but That's probably not going to happen."

s "Of course it's impossible! Silver Crow will never get caught. Silver Crow is too good for that! He's so amazing, He's like Lupin! flying"

"She's gone fangirl mode huh..."
t "Haha... Well Since we're here for the first time, why don't we take a picture?"

s "Sure! we'll use my camera!"

t "Take one with my phone camera too please"

#-Obtained Momento of museum- 

t "Well anyways, listen, something came up and I won't be here tomorrow."

s "Oh? That's no good, what if the Silver crow comes tomorrow?"

t "I know, but I can count on you to have it all on camera yes?"

s "Yeah, definitely, I won't miss a single scene even if..."

"???" "Hey You! No Cameras allowed in the museum!"

s "Eeek!"

"???" "Hand it over now!"

s "Gotta run! Slow her down!"

t "Uh... You got it!"

t "Uhm... wait, are you the security here?"

m "I'm the head security actually... The name's Monica Black... and I should have you DETAINED for obstructing justice!"

t "Uh... Whaaat.... Can't you just let her off with a warning this time?"

m "No can do, that wouldn't be fair to the other owners of the cameras I've detained."

t "There are others?"

m "...Only one today actually, but they can have it back once they leave the museum."

t "Ah... okay"

m "you... look mighty suspicious..."

t "I...I do?"

m "Height... Hair colour... stature... Feminine  looking face... why... you match the profile of the notorious Silver Crow!"

t "H... Hey now... No one has seen the Silver Crow, he could be a Shorty for all we know... and my face is not feminine!"

m "No... I've seen him, I let my guard down the first time he appeared... Finally, I've been stationed at the place he's targeted once again... This time I swear I will capture him."

label monicaquestions1:

menu:

    "So... you've seen him!? Wow, what's he like?":

        m "Pay attention! I just said he looks like you."

        t "But... I mean... how does he dress?"

        m "Well... He wore a silver masquerade mask that covers the eyes, and a silver cloak..."

        t "Odd... wouldn't he attract attention like that?"

        m "He always clouds himself with a weird white smoke bomb, that's why no one knows where he comes  and escapes from."

        jump monicaquestions1

    "So... what's the plan on catching silver crow?":

        m "That's classified information boy! You think I could just give out information like that to a Silver crow suspect???"

        t "Silver Crow?...suspect? Who? Me?"

        m "Don't play dumb with me, I could have you detained now and foil all your plans, but I'd rather catch you in action. Mmm... yess... How satisfying it will be when I have your hands cuffed..."

        "Ooookay...."

        jump monicaquestions1
        
    "I thought the museum that hosts the biggest diamond in the world would be bigger...":

        m "This museum? It's an antique, I'm surprised The diamond jewel is set for display here."

        t "Maybe it's a fake?"

        m "No, it's real. I think the owner is a big fan of Silver Crow and she doesn't really care if Silver Crow steals the diamond."

        m "She didn't even bother with hiring security, Me and other security features were hired by the insurance company... boy they were sweating bullets when Silver crow announced the next target."

        "Talk about dedication... This one is worth millions..." 

        jump monicaquestions1
        
#Gotta break the chain Alcatrez

t "Well... thanks for the information Monica"

m "THATS OFFICER BLACK TO YOU MISTER."

t "yes officer..."

"Guess it's time to go home... Oh wait... There is something else I should do..."

t "The Passport! I might as well return it to the authority."

t "By the way officer, I think I should give this to you... I found it at the airport."

m "Ah... very well.... give it here."

t "Okay see you then..."

m "Wait!"

t "Uh yea?"

m "You found this at the airport?"

t "yes"

m "WHY DIDNT YOU SUBMIT IT THEN AND THERE YOU IMBECILE?"

t "Wow, hey, I forgot okay? It's not a big deal..."

m "... I'll have you know that we had this man deported back to his country this morning because he was suspicious and didn't have his passport."

t "Uh... Whoa, why would you do that?? Shouldn't you give him some time to find the passport?"

m "Well... now I'll be getting a long lecture from my superiors... Nope, can't have it. Here you go."

t "Eh...? You're giving it back to me?"

m "He's going to get issued a new one back in his home country anyway, so don't worry about it kid."

"Gee... talk about an irresponsible officer..."

t "Okay..."

t "If that's all officer... I'll be on my way..."

#Screen Fade out

scene bg black with Dissolve(1)

#2 May 9:00 AM - Hotel lobby

scene bg lobby

t "Hey Kathy"

k "Ready to go?, remember, you're paying today."

t "What?? This is the first time I've heard of this!"

k "Why would I want you to come with me shopping if you're not going to pay??"

t "I dunno.... maybe carry the bags... company or something?"

k "Oh please... My sexy naked body is worth a lot more than that."

t "But..."

"I didn't even see you naked..."

k "- No buts! Off we go to the mall!"

"Well... darn, I hope I won't have to carry much clothes..."

#Screen Fade out -Play Date Scene

scene bg black with Dissolve(1)

#2 May 4:00 PM - Hotel door

"Geh... I'm dead tired..."

t "Well... That was surprising... You didn't buy any clothes at all..."

k "Of course not! does It look like I'm following fashion with this pink grub?"

t "Well... no... but I never thought you'd spend holiday times buying machines and cables and gadgets."

k "Yeah... well... I need these for something. It wasn't too expensive, was it?"

t "I wouldn't say that..."

"but I guess I'm thankful they're not wasted on branded clothes."

t "Still... What are you going to do with a 100m Cable wire?? and a Motor?"

k "Well that... is a secret ;]"

t "Okay well, I'm gonna go to my room now, See ya later"

k "Oh wait wait, close your eyes! I've got something for you."

t "Oh? what is it?"

k "Just close your eyes!"

t "Well... okay"

"She's not going to...?"

#heart beat music...

k "Okay open up."

t "uh... a girly cat necklace... Totally my style..."

k "You know it's rude to take off a present from a girl. Be sure to wear it at least while you're in the same country as me. :]"

t "Well... yeah sure."

k "oh and here. Kiss"

t "W... Whoa."

k "You're a nice guy Tyler, have fun catching the silver crow!"

"Hm... Guess she wasn't so bad after all."

t "I Guess I should meet Selena at the museum now."

#Screen Fade out

scene bg black with Dissolve(1)

#2 May 10:00 PM - Museum

scene bg museum

t "Hmmm... looks like nothing's happening today too huh? The idea sounds a lot more exciting... but in reality, there is nothing exciting about waiting for hours, is there?"

s "I don't really care, Silver crow is going to come and I'm going to be here when he does."

t "You must really be a big fan huh..."

s "The biggest. Numero uno."

"Hrmh... I thought it might be fun hanging out with Selena alone, but she doesn't really talk much..."

"my mind keeps wandering to Kathy and what we did today... I feel rather to be thinking of her while with another girl though."

s "Well... Looks like that's the end of today's watch."

t "Yeah, I'll see you tomorrow morning."

s "See ya."

#Screen Fade out

scene bg black with Dissolve(1)

#2 May 11:00 PM - Hotel room

scene bg hotelroom

t "Hmm? Kathy's room door is open, hmm... Maybe I'll thank her properly for the necklace."

"Well... She did kick me out last time I went in uninvited... Guess I should knock... Hmm...?"

#Scene change

#Door - chain

"What... what is that??? A wig... and a masquerade mask?"

t"What are they doing in Kathy's room?"

"Could it be...? Argh... I'm going to take a picture of this with my mobile."

#-Snapshot- Picture of mask obtained

"There are too many questions...Yet... Yes...it makes sense... I should definitely ask her tomorrow..."

#Screen Fade out

scene bg black(1)

#3 May 10:30 AM - Museum

scene bg museum

s "Mornin!"

t "Heys, morning."

s "You okay? you look like you didn't sleep a wink."

t "Haha, there's just something on my mind..."

"Hmm... I've tried knocking on Kathy's room but no reply... where could she have gone...?"

s "Well... Cheer up! maybe today's the day Silver Crow appears, I've got a good feeling about today"

t "Perhaps you're right..."

"I have a feeling she might appear today too..."

s "I'm definitely right! You just wait."

"Okay... Silver Crow could strike at any moment now... Where..."

k "Heyas!"

t "W...WHOA ....you scared me"

k "Gee Tyler, you look like you've seen a ghost!"

t "Well... I wasn't expecting to see you here."

k "Well... I don't see why not? Ah... Oh Don't worry... I don't intend to interrupt your date ;]"

t "Oh.... wha? no no, that's not what I mean"

k "Well... aren't you going to introduce us?"

t "What... oh yes... Selena, meet Kathy. Kathy, Meet Selena."

s "... Hi?"

k "Hi ^_^"

"Selena has a blank expression on her face... is she... angry? That's not important right now, I need to talk to Kathy"

t "Uhm... Kathy, I need to ask you something... in private."

k "sure! I'll head down over the quiet corner over there by the stairs."

t "I'll be back soon Selena."

s "Yeah, sure."

#Screen Fade out

scene bg black with Dissolve(1)

#Museum (outside)

k "So... What's up?"

t "I've figured it out..."

k "Figured what out?"

t "...The Identity of Silver Crow... It's you. Kathy Cat."

k "Oh? and how did u figure that?"

t "A few hints and clues... First of all... The Bagelboys..."

t "You've bought the tickets for tomorrow's concert?"

t "Do you know the band members names?"

t "Are you still going to watch the concert tomorrow night?"

t "Did you know about the special event for tomorrow's concert?"

k "Why... yes of course... I just don't have them with me right now..."

t "But you are still going to watch it right?"

k "Of course"

t "Well... That's impossible because the concert is cancelled!"

k "Wh... What? How?"

t "You're not really a fan are you? I mean... you are actually here for Silver crow... but you wanted to avoid suspicion... that's why you said you're here for BagelBoys."

k "That's ridiculous! Don't be silly, Just because I didn't know about their concert being cancelled doesn't mean I'm not a fan! I know everything about them. You name it, I know it."

t "I wouldn't be surprised Kathy... Since you've got one of these magazines on the airplane. It tells you everything you need to know about Bagelboys inside."

k "Ah..."

k "Okay, So what if I'm a big fan of Silver Crow... That doesn't mean I AM silver crow."

t "I thought so too... but why else would you buy a motor and a long cable wire??"

k "..."

t "They're equipments you need for your next heist huh?"

k "urk..."

k "You have no evidence whatsoever that I'm the Silver Crow."

t "Your room was open last night."

k "So?"

t "I took a photo with my phone... you've got a wig and a masquerade mask with a beak. It's a wee bit too suspicious since I know... Silver Crow's signature is in fact... the mask he wears... or should I say... 'She'."

k "Hmmm... you certainly have a wild imagination Mr Fox... as much 'evidence' as you have... you certainly do not have enough to convict me of anything in court... "

k "...But having you find out is part of the plan"

t "Yes... What? but... I can prevent you from thieving tonight if I convince the head security to detain you for the remaining duration of the diamond display."

k "Ah... Well... that won't be necessary. You won't be speaking to her anytime soon..."

t "?"

#-SMACK-

t "Ugh..."

k "Sweet dreams Mr. Fox"

#Screen Fade out

scene bg black with Dissolve(1)

#Place and time... Unknown

t "Huh...? Where am I...?"

t "Am I... Am I on the roof?? why am I on the roof... Why is there a rope tied on my waist..."

t "There's a hole on the ground in front of me..."

c "..."

t "You...! wait!"

#Silver Crow disappears

t "She... She jumped! I've got to follow her! I need to catch her!"

t "Ugh... I sure hope this rope is long enough to reach the bottom floor."

t "I'm rather hesitant about this... but... I gotta do it."

"So much... smoke... This must be the smoke bomb Silver Crow always use to hide her presence"

t "The Diamond... it's gone!"

t "Kathy must have taken it... I need to look for her!"

"ah... I touched something.... a hand!"

t "Gotcha!"

t "..."

m "Nope... I got you!"

#Smoke fades out

t "Monica!"

m "Got ya Mr. Silver Crow. Hand over the item you stole!"

t "What? No, the real one just jumped down from the roof, I came here following her!"

m "Oh? Well... I've got you right here... cape and all..."

t "Cape? No... wait... this... THESE AREN'T MINE! someone dressed me up while I was unconcious!"

m "oh please... you're obviously grasping at straws now... if you want me to listen... show some evidence or alibi."

t "Wait... my Phone!"

t "... Yes! Still got it, here officer, look at this picture."

m "I'm looking at it... great evidence against yourself you got there. I'm going to confiscate that."

t "No... It's not my room!"

m "You are Silver Crow"

t "No! I've been framed! The real Silver Crow is a woman!"

m "Oh give up! Who do you accuse of being the real Silver Crow?"

t "Her name is Kathy... Kathy Cat... She lives in the hotel room next to mine."

m "Never heard of her."

s "Gasp... Tyler... you're the Silver Crow?"

t "Selena! No I'm not the Silver Crow! It's Kathy!"

s "So... You are Silver Crow."

t "What? No! Kathy, I introduced you to her didn't I?"

s "Umm... You did introduce me to Kathy..."

t "Yes! Yes! see? I'm not lying! She's th-"

s "...but when you did, you pointed to that cat necklace you're wearing"

t "No! This is a gift from Kathy... and you've met her!"

s "I'm sorry... but I've never met such a person."

"W-What?? What does this mean!?"

m "Well... you're coming with me pal."

#Fade scene...

m "Well... We still couldn't find the diamond... Where did you hide it pal?"

t "... What's... happening?"

m "...Sigh..."

m "Okay Tyler... We've had a doctor examine you."

t "..."

m "He thinks you might have a rare disease which causes you to have multiple personalities. A Dissociative identity disorder or common people would say it... multiple personality disorder."

m " Personally... I don't buy it."

t "..."

m "...You have multiple personalities inside you, and the silver crow is one of them. That's why you only remember certain parts of your trip..."

t "... the fade times..."
"it's because I'm playing an Iphone game and the fade time is just the boring stuff that I skip..."

s "It makes sense... all his personalities are named after animals... Crow, Fox, Cat."

m "...Yeah... I think we've heard enough... you're most likely mentally ill, heck I wouldn't be surprised if you think none of us are real people."

m "Rest assured, we have places suitable for you regardless of what the court decides on what to do with your crime."

t "Am I really the Silver Crow...?"

m "No doubt about it. We've got piles of evidence to prove it."

m " we've checked your wallet, and found the receipts for a motor... a long cable wire... Hydrochloric acid... all which was found on the scene of the crime."

t "That... Kathy bought them all..."

m "... The receipt says they're paid using your credit card."

t "Well.. it's a long story but... I paid for her shopping..."

"hmm... am I really..."

m "...Secondly, we found the item packaging in your room."

t "Wait... what??"

m "-and of course I caught you at the scene of the crime, even though you do not have the stolen item, this is enough to take you in for further questioning."

t "No... It can't be... Is there... nothing else I can do?"

menu:

    "Accept your fate":
    
        ""
    
    "There's a contradiction here...":

        ""

t "No."

m "No?"

t "I'm not the Silver Crow, and I can prove it."

m "Oh? how will you do this?"

t "Lucky for me... the evidence is still in this very room."

t "If I'm not Silver Crow... then there's only one conclusion... Someone is lying... Selena... is lying."

t "And here's the evidence to prove it."

#-Submit Item- Momento.

t "I took this picture as a momento when I first came to the museum... but what's important is the girl wearing the orange beanie and the lupin tattoo on her hip."

s "Ah?"

m "What about it?"

t "I think... The Selena with us right now... is an impostor! This person is the real Selena Bella!"

m "... Did you say... Selena Bella? Why... She's the spoiled niece of the owner of the missing diamond."

t "Yes.. ye- WHAT? Well... I'll be damned"

m "She's kinda chubby  huh..."

t "Uh... yeah..."

"...Note to self: Don't trust myspace angle photos in the future."

m "So you're saying this Selena is a fake... Well then, where is the real one?"

t "The real Selena never met me... She's is really shy you see... She probably had to struggle to talk to me in real life... I don't think she had the courage to talk to me while I'm with someone else."

t "This is probably why the impostor approached me first before I could look around for the real Selena."

m "There is only one way to find out the truth. Okay missy...Let me see a  form of ID on you."

s "Oh my... I'm not Selena Bella... Well... I am... but um... There can be more than one Selena Bella in this world right?  I think there is some miscommunication here..."

t "Liar! you told me you were waiting for Tyler when we were at the museum. you knew my name as well as Selena's character profile... I've told you in the bus! I've only told Kathy ever since I came to this country! That's how you-"

s "Wait a moment... I'm not Kathy... I mean... you told me yourself... you've seen both Kathy and me at the museum before... that means I'm not Kathy."

t "oh... Good point..."

t "Regardless, you are not who you claim to be."

m "Just show us an ID"

s "I... don't have any with me."

m "Well... We have no good reason to detain you without evidence Miss Belle. Come along now Mr. Fox"

t "Wait!"

m "?"

t "What she said just now... She said... \"I'm not Kathy\" ...which means Kathy exists as a person, and this imposter knows who she is."

m "So... what does this mean?"

t "It means... Miss imposter here... is working with Kathy... The Silver Crow..."

m "How did you deduce that?"

t "Simple! first of all... Only Kathy knows that I'm supposed to meet with Selena Bella, and Kathy has seen this picture of Selena... That's why I originally deduced that this impostor is Kathy... However, I've seen both of them together at the same time... therefore... Either Silver crow hired a henchmen..."

t "Or..."

m "...Or?"

t "...It means... The Silver Crow... is not just one person... The Silver Crow... is a team!"

s "..."

m "Miss... Bella?"

s "... You're smarter than we give you credit for, Mr. Fox."

t "!!"

m "!!"

s "We don't want anybody to know all of our secrets... We vowed to never kill in our operations... but it seems like we'll have to make an exception this time... "

m "!! That gun!"

#-Bang-

t "Officer!"

m "Ugh... She got my leg..."

s "...I stole from your pelt while you were distracted officer... We've never had to kill anyone before... this may be the first... any last words Mr. Fox?"

t "...Why me? Why make such complicated plan just to convince me that I am the Silver Crow and frame me to be The Silver crow?"

s "... As fate would have it... One of our accomplices was detained for a stupid reason... We've had our heist planned in advance and each member had a specific role you see... Since one member was taken out early... We've got holes in our plan."

t "Then... why are you still here? Why didn't you run away?"

s "It was just a slight miscalculation... None of your concern."

t "No... I think I know the reason why you didn't run away... as well as who your 'accomplice' is..."

t "You wanted to recover ...\"This\""

#-Shows passport-

s "Wha... That's..."

t "...The fact that I have this with me... is probably why your colleague was deported... and why I'm in this mess to begin with."

t "Kathy probably noticed I had it in my possession and decided to formulate this plan."

t "You really need this passport don't you... You wanted to avoid getting a new one because it would be quite a hassle for someone leading a double life to obtain a new passport."

s "... Well, also that your physique and hair color is similar to him... It's very uncanny."

s "but yes...Well done Mr. Fox, Too bad I'm still going to kill you... and after I kill you, I will have that passport and it will all be over..."

m "No... Stop!"

s "Quiet, you also know too much officer... rest assured, I will kill you after I Kill Mr. Fox."

s "Well then, Mr Fox...farewell..."

"Is this... The end...?"

#-Bang-

t "!!"

m "!!"

s "!!??"

t "Kathy?!"

s "What is the meaning of this!?"

k "I agreed to join this group on the condition that we would not kill... That was the deal!"

s "Ugh... Are you betraying us?"

k "No! You are the one betraying us!"

s "Ugh... You were always the soft one... Fine! we will discuss this later... We must leave, NOW!"

#Smoke!

t "!!"

k "...Sorry Mr Fox..."

t "Kathy?"

k "We didn't mean to cause you so much trouble... The plan was just for you to get detained for awhile... and Once Silver Crow pulls up another heist, you would have been free to go..."

t "... Wait... I've got a lot more questions to ask you"

k "...Some other time perhaps."

k "Good bye Mr. Fox... I... I really did enjoy our date."

t "Wait! ...Gah! How do they just disappear like that?"

#Smoke fades...

t "Officer... are you okay?"

m "I'm fine... They got away huh...?"

t "Yeah... Though I get the feeling we'll see them again though..."

#Screen fade...

#Epilogue- Ending  1

"It has now been 2 months since then... I'm back home and life is back to normal."

"I haven't  heard from Kathy since then, but today... new rumors surfaced about the return of the Silver Crow."

"I don't know if it's the same Silver Crow I had encountered... but then again...my target is no longer Silver Crow..."

"Kathy Cat... Just you wait... I'm going to capture you if it's the last thing I do."

#End - Episode 1
