# Label-batch batch_0118

## Instructies
Je bent een marktonderzoeker voor een Nederlands e-commercemerk dat koperen inlegzolen gaat verkopen. Je codeert Reddit-threads over voeten, voetklachten, schoenen en inlegzolen volgens een vast codeboek.

Regels:
- Citaten (quotes.text) zijn ALTIJD letterlijk en exact uit de bron overgenomen, inclusief spelfouten. Nooit samenvatten, vertalen of verbeteren in dat veld. nl_meaning is een getrouwe vertaling, geen reclametekst.
- Codeer alleen wat er staat. Verzin geen beroep, diagnose of situatie die niet genoemd wordt; gebruik dan null of een lege lijst.
- Scheid eigen ervaring (first_hand=true) van advies uit de tweede hand, diagnoses door vreemden en reclame van fabrikanten.
- Neem ook tegengeluiden en negatieve ervaringen mee: wat NIET werkt is net zo waardevol als wat wel werkt.
- Noteer elke vermelding van koper, magneten, acupressuur of reflexologie, ook sceptische, in 'copper'.
- Een Reddit-reactie bewijst geen klinische werking. Zet claims_risk op 'medical' bij aandoeningen of behandelclaims, 'material' bij materiaalclaims (koper, antibacterieel, geur), anders 'comfort_only'.
- medical_red_flag bij diabetes, neuropathie, gevoelloosheid, branden/tintelen, infectie, (stress)fracturen of ernstige zwelling.
- marketing_insight_nl is een hypothese voor ons merk, geen feit; beloof daarin nooit genezing of pijnvermindering.
- Is de thread niet over voeten/schoeisel/zolen (bijv. een toevallige zoekmatch), zet relevant=false en houd de rest minimaal.

## Opdracht
Label elke thread hieronder volgens het schema `ThreadLabel` in `vocscraper/schema.py`.
Schrijf het resultaat naar `batch_0118.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 6vtuty, 3l83yr, 1qa9sts).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 6vtuty ===
SUBREDDIT: r/weddingplanning
DATUM: 2017-08-24  SCORE: 19  REACTIES: 77
TITEL: Any brides wearing/wore very low heels or flat shoes for their wedding?
POST (source_id=post):
Hey all

Just over two weeks till the big day and I would please love some empathy and to hear some other opinions on this issue: So are there any other brides who only plan to wear very low/kitten heels or even flats at their weddings due to being unaccustomed to heels?

I myself almost never wear heels. (In the last 7 years or so I have worn high heels exactly once.) For my wedding I opted for very low block heels so I can look elegant but won't spend the day in pain. Not to mention all the stairs I will have to go down in my venue. These are the shoes I picked:

https://www.amazon.co.uk/dp/B01N74WGW6/ref=wl_it_dp_o_pC_S_ttl?_encoding=UTF8&colid=3BZSK9BPU8DAH&coliid=I3VAXQNF5RL5GH&psc=1

I loved them when I saw them, and am still crazy about them. They go so well with my youthful wedding dress (A princess-like gown from Sincerity) and furthermore they have my personality written all over them. Not to mention that after the wedding I can still wear them on other occasions e.g. business meetings/presentations.


The only reason I need to vent is because my mom bloody hated that they weren't high enough when she saw me wearing them. (Even though she originally picked this pair when I asked her opinion on two choices which included these) 
I know I shouldn't care about what other people think since they are my shoes and no one else's, but when the only opinion I have heard so far is hers - and given the way she criticised the heck out of them just because the heel wasn't very high - has made me slightly down and almost second guess my opinion for the first time during wedding planning.
(To give you an idea: During my first dress fitting with them, she insisted that I had 'ruined' the wedding already because of this, and that there was no way this wedding could be perfect now; she got so bitter that even the seamstress/saleswoman raised eyebrows at her at the fitting.) 


So what do you all think? Is it weird that I don't want to wear taller heels? Is there anyone else out there not going for extra high heeled shoes? Would please love some opinions!


Thanks and I will finish by saying congratulations to all brides who just got married, and best of luck to all brides to be! Hope your weddings were/will be all you dreamed of and deserve! x

**EDIT: Thank you so so much all of you for your reassurance and the awesome comments on my shoes, they really cheered me up, and it was lovely to see all your gorgeous shoes too! It's really nice knowing there are people who are like minded who just don't mix with heels.**

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dm2ytgl] (score 29, diepte 0) Pfffft it's YOUR wedding. Other people's opinions shouldn't matter. I'm wearing Kate spade glitter keds for my wedding despite the fact that my fiancé is 1 foot taller than me. I know I'd rather look comfy then wear heels that will hurt all night.
[dm2y9gk] (score 17, diepte 0) I'm wearing flats. I'm 5'10 and my FH is 6'1. Even though he's the kind of guy who is like "yeah babe wear the sky high heals!" And doesn't care if I'm taller, I definitely want to look and feel pretty and "dainty" on my wedding day. Being so tall has always been a sense of insecurity for me so I don't want to escalate that forever with wedding pictures where I'm taller than my FH. Luckily there's some gorgeous flats these days
[dm2ztov] (score 9, diepte 0) I'm wearing flats. I didn't even consider anything else because although I can walk in heels for a little I always feel like I'm concentrating on it and they're never comfortable. No one's really going to see my shoes anyway. I've known several other brides that wore flats too.
[dm2xyci] (score 7, diepte 0) Your mom is being weird.  I've told plenty of people who work in the wedding industry that I'm planning to wear flats, and they all enthusiastically agreed that that was a good idea.  You're going to spend a ridiculous amount of time on your feet on your wedding day; why be uncomfortable?  

I know some women also switch shoes for the reception, but then isn't their hemline all wrong?  That seems like it would be worse than wearing flats the whole time, especially if they're going to be covered by a dress most of the time.
[dm2xyz2] (score 7, diepte 0) im not. i can walk in high heels, but only for about an hour or two. i decided to go with a pair that i could wear all day without issue (hopefully!). They are around 1.5 inch heels.  https://www.dsw.com/en/us/product/betsey-johnson-maibel-pump/371560
[dm2y3ox] (score 5, diepte 0) I am wearing custom made Chaco's (river and hiking sandals like Teva). I wear high (4+ inches) regularly, but I don't want to worry about what length to hem my dress and want to be in comfy flat shoes for the dancing portion. So they are what I'll wear the whole day. I'm just embracing the fact that my FH is 6'7" and I am 5'3"

I really like your shoes!
[dm2xfbe] (score 4, diepte 0) Mine are very similar, only instead of a closed shoe its more of a strappy sandal.  https://www.nordstromrack.com/shop/product/2033341/free-people-marigold-block-heel?color=BLUE%20GREE
They are only 5cm tall and I love them.  Like you, I almost never wear heels.  I plan on cutting a rug during my wedding too so high heels would be pointless because they would be off before any real partying happened.  

Ignore your moms opinion.  Almost no one will see your shoes.  I guarantee no one will remember them.  What is most important is that you like them and you are comfortable.
[dm34ko2] (score 4, diepte 0) Even though I'm all of 5'2" I'm wearing flats to my wedding. I've never been able to wear regular heels comfortably, and lately even kitten heels get painful after an hour or so (one of my go-to Halloween costumes is Velma from Scooby-Doo, and I had the PERFECT kitten-heeled brown Mary Janes I wore with it but they got super uncomfy over time, plus they're dead now anyway). Plus the venue is outside and we'll be walking down the aisle on grass, so I wouldn't want to chance heels getting stuck in the dirt and me faceplanting in front of everyone I love.

I always saw myself getting married in Chuck Taylors, and my shoes are 99% there- they're knockoff Chucks from Target that I embellished with loads of Swarovski crystals on the toe and ribbon laces. They're super cute, comfortable as heck, and most importantly they are exactly what I wanted!
[dm35ort] (score 4, diepte 0) I'm wearing Kate Spade glitter Keds the whole time. I don't wear heels normally and love these shoes. Also, we are at an outside venue and Im a klutz so it's also kind of a No-tripping strategy. 😜
[dm37jrt] (score 4, diepte 1) Me too!! I just got them yesterday and they're beautiful. I have horrible plantar fasciitis and can't wear anything without support (which eliminates almost all flats, heels, and sandals). I can put my inserts into the keds easily. 

https://www.keds.com/en/keds-x-kate-spade-new-york-champion-glitter/14126W.html?dwvar_14126W_color=WF57753&sma=sm.00001awchhsqzze42wq43ah5qhmzn
[dm2xowj] (score 3, diepte 0) I'm just wearing flats, they're gold and glittery and have a see through mesh. I'm 5'0 and FH is 6'3. Me wearing heels doesn't really gap the height difference so I'm not gonna bother be uncomfortable in the woods haha
[dm2yqgl] (score 3, diepte 0) I NEVER wear heels (I have knee problems and have since high school so not only are they uncomfortable, but I never learned to walk in them so I look like a freaking baby moose talking it's first steps when I try) so, I am absolutely wearing flats and rocking them! I bought a cute pair of flats from Target and flat booties from Toms and I'll wear whichever is more comfortable.
[dm358s5] (score 3, diepte 1) Same! And so are all my bridesmaids (and grandmother). I can't wait to be the most comfortable one at my wedding!
[dm43115] (score 3, diepte 1) I'm wearing those too!! They're so cute.
[dm37p8q] (score 3, diepte 0) These are mine! I can't walk in heels to save my life.  http://i.imgur.com/QK2AWkc.jpg
[dm39hgl] (score 3, diepte 0) I'm wearing rose gold Tieks for the ceremony and then maybe switching into Keds high tops. I don't own heels and can't walk in them so it would be pretty weird to wear them for my own wedding.
[dm2xjoc] (score 2, diepte 1 OP) Aww thank you. Your shoes are gorgeous too - so chic and glamorous but still classy. 

Best of luck to you and your fiancé for your wedding day and for the rest of your lives too. :)
[dm2xp02] (score 2, diepte 1) 5 ft | 1.52 metres  
6'3" | 1.91 metres ^metric ^units ^bot ^| ^[feedback](https://www.reddit.com/message/compose?to=cannawen&subject=metric%20units%20bot&message=I%20think%20your%20bot%20is...%20%5BPlease%20include%20a%20link%20if%20you%20are%20reporting%20a%20bug%20about%20a%20specific%20comment!%5D) ^| ^[source](https://github.com/cannawen/metric_units_reddit_bot) ^| ^[stop](https://www.reddit.com/message/compose?to=metric_units&subject=stop&message=If%20you%20would%20like%20to%20stop%20seeing%20this%20bot%27s%20comments%2C%20please%20send%20this%20private%20message%20with%20the%20subject%20%27stop%27.%20If%20you%20are%20a%20moderator%2C%20please%20go%20to%20https%3A%2F%2Fwww.reddit.com%2Fr%2Fweddingplanning%2Fabout%2Fbanned%2F) ^| ^v0.6.1
[dm2xz34] (score 2, diepte 1) 1.5 inches | 3.8 cm ^metric ^units ^bot ^| ^[feedback](https://www.reddit.com/message/compose?to=cannawen&subject=metric%20units%20bot&message=I%20think%20your%20bot%20is...%20%5BPlease%20include%20a%20link%20if%20you%20are%20reporting%20a%20bug%20about%20a%20specific%20comment!%5D) ^| ^[source](https://github.com/cannawen/metric_units_reddit_bot) ^| ^[stop](https://www.reddit.com/message/compose?to=metric_units&subject=stop&message=If%20you%20would%20like%20to%20stop%20seeing%20this%20bot%27s%20comments%2C%20please%20send%20this%20private%20message%20with%20the%20subject%20%27stop%27.%20If%20you%20are%20a%20moderator%2C%20please%20go%20to%20https%3A%2F%2Fwww.reddit.com%2Fr%2Fweddingplanning%2Fabout%2Fbanned%2F) ^| ^v0.6.1
[dm3v235] (score 2, diepte 2) Oh god, these are so cute and so affordable! I feel like everyone else gets dress regret and I get shoe regret...
[dm39d7i] (score 2, diepte 1) I got wedding chacos too! They just happened to have a pattern this year in our colors so I ended up with those. I wore flat gold sandals for the ceremony, then changed into chacos during cocktail hour.
[dm3lbqj] (score 2, diepte 1) Hi fellow tall bride! I'm 5'11" & FH is barely over 6'. I just wanted to remind you that you will look gorgeous & feminine & dainty on your wedding day. Tall girls get to feel that way too! Don't be insecure--although, girl I totally get it--own it. You will be drop dead gorgeous.
[dm37onm] (score 2, diepte 1) "I look like a freaking baby moose"

Stealing this if people ask why I'm not wearing heels. Hahaha!
[dm42rjm] (score 2, diepte 1) Preach!  We are getting married outside and I don't want to deal with heels.  FH will just tower over me.  Like he does every other day.
[dm2ytnk] (score 2, diepte 1) 2 inches | 5.1 cm ^metric ^units ^bot ^| ^[feedback](https://www.reddit.com/message/compose?to=cannawen&subject=metric%20units%20bot&message=I%20think%20your%20bot%20is...%20%5BPlease%20include%20a%20link%20if%20you%20are%20reporting%20a%20bug%20about%20a%20specific%20comment!%5D) ^| ^[source](https://github.com/cannawen/metric_units_reddit_bot) ^| ^[stop](https://www.reddit.com/message/compose?to=metric_units&subject=stop&message=If%20you%20would%20like%20to%20stop%20seeing%20this%20bot%27s%20comments%2C%20please%20send%20this%20private%20message%20with%20the%20subject%20%27stop%27.%20If%20you%20are%20a%20moderator%2C%20please%20go%20to%20https%3A%2F%2Fwww.reddit.com%2Fr%2Fweddingplanning%2Fabout%2Fbanned%2F) ^| ^v0.6.1
[dm2z6fj] (score 2, diepte 0) I splurged on some very fancy flats and I LOVE them. I feel like a princess and best part - I CAN WALK! I never wear heels and didn't plan to start on a day I wanted to feel my absolute best!
[dm2zmd1] (score 2, diepte 1) 5'4" | 1.62 metres  
6'4" | 1.93 metres ^metric ^units ^bot ^| ^[feedback](https://www.reddit.com/message/compose?to=cannawen&subject=metric%20units%20bot&message=I%20think%20your%20bot%20is...%20%5BPlease%20include%20a%20link%20if%20you%20are%20reporting%20a%20bug%20about%20a%20specific%20comment!%5D) ^| ^[source](https://github.com/cannawen/metric_units_reddit_bot) ^| ^[stop](https://www.reddit.com/message/compose?to=metric_units&subject=stop&message=If%20you%20would%20like%20to%20stop%20seeing%20this%20bot%27s%20comments%2C%20please%20send%20this%20private%20message%20with%20the%20subject%20%27stop%27.%20If%20you%20are%20a%20moderator%2C%20please%20go%20to%20https%3A%2F%2Fwww.reddit.com%2Fr%2Fweddingplanning%2Fabout%2Fbanned%2F) ^| ^v0.6.1
[dm32fo0] (score 2, diepte 0) I wore the flatest flats in all the land and danced the night away!
[dm34tjv] (score 2, diepte 0) I'm wearing flip flops because my feet are wide and even when trying on wide width bridal shoes they don't fit. I tried flats too and the lining on the top rubs my toes and is uncomfortable. So I decided to say fuck it and just bought some cute bridal flip flops.
[dm355vo] (score 2, diepte 0) I'll be wearing flats. I can't stand heels and I would be miserable. Wear what makes you comfortable! Nobody else has to feel your feet hurt, so their opinion shouldn't matter
[dm382ec] (score 2, diepte 2) I didn't know they make this color?! How cool! I got the cream ones... [My Keds](http://i.imgur.com/tJFBb1E.jpg)
[dm4xvjq] (score 2, diepte 1) I wore those for my wedding! They were comfortable all night.
[dm3acpc] (score 2, diepte 0) Even with a 9" height difference between us (I'm 5'9 and he's 6'6), I'm happily wearing flats. Nothing turns me into a cranky whiner quite like having sore feet (OK, ok,being hangry does it, too), so I picked some metallic gold flats that feel good on my feet. No one is going to see them, anyhow.
[dm2yqxc] (score 1, diepte 2) Thanks!  Same to you bb!
[dm4efxz] (score 1, diepte 1) You are correct; I'm wearing fairly low wedges for the wedding and changing into keds for the reception and my dress had to be hemmed for the keds.
[dm3lbsr] (score 1, diepte 2) 5'11" | 1.80 metres ^metric ^units ^bot ^| ^[feedback](https://www.reddit.com/message/compose?to=cannawen&subject=metric%20units%20bot&message=I%20think%20your%20bot%20is...%20%5BPlease%20include%20a%20link%20if%20you%20are%20reporting%20a%20bug%20about%20a%20specific%20comment!%5D) ^| ^[source](https://github.com/cannawen/metric_units_reddit_bot) ^| ^[stop](https://www.reddit.com/message/compose?to=metric_units&subject=stop&message=If%20you%20would%20like%20to%20stop%20seeing%20this%20bot%27s%20comments%2C%20please%20send%20this%20private%20message%20with%20the%20subject%20%27stop%27.%20If%20you%20are%20a%20moderator%2C%20please%20go%20to%20https%3A%2F%2Fwww.reddit.com%2Fr%2Fweddingplanning%2Fabout%2Fbanned%2F) ^| ^v0.6.1
[dm2yahk] (score 1, diepte 0) I just posted asking for feedback on my whole ensemble with my flat shoes :) http://imgur.com/a/vFom5
[dm3nrox] (score 1, diepte 1) Oh my! That's a gorgeous ensemble! Love your belt and headpiece especially. And your shoes kind of match your flowers too! It will all look so amazing on you (is it a fall wedding, just out of curiosity?)
[dm3ypdg] (score 1, diepte 2) Yep!
[dm35alb] (score 1, diepte 2) Right!!! Barely anyone will even notice my shoes. No need to be uncomfortable all day!
[dm4344u] (score 1, diepte 2) Exactly!!!
[dm433mp] (score 1, diepte 2) I love them so much!!!!
[dm2yti9] (score 1, diepte 0) I am wearing 1 inch block heels. I want to be comfy on the day of. Plus, I am 2 inches shorter than FH.
[dm2zfsw] (score 1, diepte 0) I wore a 2 inch heel because I'm 5'0 and the best man is 6'9. Didn't matter what I put on, still short. And those teeny heels were still uncomfortable and I ended up barefoot in the grass like 5 minutes after he ceremony.
[dm2zm8r] (score 1, diepte 0) I'm 5'4, FH is 6'4 and the rest of the bridal party is also tall. I don't wear heels much so I'm wearing wedges for the ceremony and exchanging them for flats immediately after.
[dm321yx] (score 1, diepte 0) Going with flats here! I rarely wear heels ( although I do like the occasional dress up in them!) however for the wedding day I want something comfortable I don't have to worry about all day or have to change out of.

My only problem is finding ones that fit! (I would love a pair of mint ballet flats, but none of the cute and affordable ones I've found come in a size 11 :/)
[dm34nsq] (score 1, diepte 0) I wore blinged our sandals that had like a .75in heal and I was so comfortable! My FI is an inch taller than me on a good day and I didn't want to tower over him. It was perfect
[dm34vkf] (score 1, diepte 0) I like your shoes and think you should wear whatever you want for your wedding (And your mom is being unreasonable).

That being said, if you are looking for another option you could check out "flatform" shoes. I also cannot walk in heels at all, the last time I wore heels was grade 8 grad. I do own a pair of cute flatform sandals though, and find them really easy to walk (and dance!) in, and they give me a bit of height so my face isn't in the armpit of my 6'5" fiance in every picture. Bonus: they are trendy right now so I am seeing them everywhere!
[dm3dqnh] (score 1, diepte 3) I got some 1" platform Keds with the Rifle Paper Co. print. They are high enough that I am still taller than my fiancee in her wedge sandals which I liked. They are so comfy! I thought they were a bit narrow at first but once I wore them for a day they were very comfortable.
[dm4ej87] (score 1, diepte 3) I got [these!](https://www.keds.com/en/keds-x-kate-spade-new-york-champion/14124W.html?#q=lace+keds&ref=lace%20keds&dwvar_14124W_color=WF57485&start=1&sma=sm.001yt0tyf12l3fjov1814v3mqk9ym)
[dm4jseo] (score 1, diepte 3) I got the cream as well, but that's before I got a blush colored dress (something I NEVER expected to love) so I'm considering returning for the rose gold version.
[dm3l2ed] (score 1, diepte 1) Hahahah ditto. I bought the white ones, and I knew even before we got engaged that I'd be wearing them. I am the single most accident-prone person I know, and not in the cute "oops I dropped things!" Or "I wobbled on my feet!" But in the like "I tripped over air and slammed my face into a brick wall" or "somehow in throwing a ball I hurt my hip" kind of way. I've successfully worn heels exactly zero times out of the fifty times I've tried. We're getting married in a forest and I laugh just thinking about my MIL saying I could get some "nice low heels"... lady, I sprained my ankle in 1" kitten heels on flat ground. Hard nope.
[dm35s7f] (score 1, diepte 0) I'm 6'2. I don't wear heels...ever. So I will be wearing ballet flats.
[dm37kne] (score 1, diepte 0) I got little heels -- my sister called them Queen Elizabeth shoes. But they were blue and they were comfortable and I love them.
[dm38g4d] (score 1, diepte 1) Omg, SO SO pretty! Do you know if they sell flat versions of those shoes?! I'm IN LOVE!
[dm7p8r2] (score 1, diepte 2) Thank you! I am not sure :( they are Betsey Johnson! I believe I did see some similar flats but I don't think they were rose gold!
[dm7p7e4] (score 1, diepte 2) That's awesome to hear! Did you have to wear anything with them? Like those little pads? I am hoping they don't cause blisters
[dm7pah7] (score 1, diepte 3) Nope! I packed some band aids just in case and didn't need them.
(19 reacties met lagere score weggelaten)

=== THREAD 3l83yr ===
SUBREDDIT: r/Fitness
DATUM: 2015-09-16  SCORE: 24  REACTIES: 75
TITEL: How do you keep your feet planted during a squat?
POST (source_id=post):
Every time I do squats, I end up leaning on the front of my toes. Someone told me I need to be planted on the back of my heals. But somehow I keep shifting the weight towards the front. Any tips?

UPDATE: Thanks everyone! It's definitely helped. I think I need to get my hip muscles stronger, but the wider stance suggested made things easier. I was doing ''should width apart'' but apparently that wasn't wide enough.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cv4000n] (score 46, diepte 0) Yes, you should be planted on your *heels.* There are no priests, shamans, druids, or healadins around in the gym.

Tips? Google. Seriously. There are thousands of guides already written about this, and plenty of youtube videos. 

Find what works for you.
[cv40x8e] (score 42, diepte 1) >you should be planted on your *heels.* There are no priests, shamans, druids, or healadins around in the gym.

lol I bet you've never even been to OPs gym

How dare you say that his gym lacks a shaman
[cv46e26] (score 15, diepte 5) I mean I was just hoping you had some basis
[cv3zssb] (score 13, diepte 0) You need to work on your ankle mobility. Do that.
[cv41q7u] (score 11, diepte 0) Your mobility probably sucks, especially in your achilles tendon.
[cv44fki] (score 11, diepte 0) http://stronglifts.com/squat/#Heels_Come_Up

Check this out.
[cv44udr] (score 8, diepte 2 OP) STL GYMs man....
[cv44ltt] (score 8, diepte 0) I widened my stance. Instantly fixed it.
[cv45vi9] (score 6, diepte 1) I thought this was just a cue? When I squat I make sure the weight is evenly distributed across the whole bottom of my foot, and that no part comes off the ground.
[cv49dsx] (score 6, diepte 1) I lift at a private barbel club who's members are really into norse mythology and heathen type shit. Might be able to find you a shaman.
[cv40vhi] (score 5, diepte 0) What kinda shoes do you wear to the gym? 

I ask because when I first started going to the gym, I wore tennis shoes which had gel bottoms. This is bad. 

If you don't have a pair already, invest in some hard bottomed shoes. No need for fancy lifting shoes. I bought a pair of Chuck Taylor's after some research and my life changed. Went from 175lb deadlift to 350lb. Similar changes in squats. Seriously, these shoes will 100% keep the weight on your heels and help form/posture/lift.
[cv44v9x] (score 5, diepte 1 OP) So I defy gravity? I'm going to pull a Neo.......
[cv462g7] (score 4, diepte 3) I don't believe you
[cv41p33] (score 4, diepte 0) Normally, gravity does it for me.
[cv48vnd] (score 3, diepte 2) You don't need to. Just do one of the mobility routines in the FAQ, with particular attention being paid to the Achilles.
[cv43iq3] (score 3, diepte 0) People here are suggesting that your ankle is the problem, but it's probably not. You workout your ankle well because you walk all the time, but you probably don't squat all the time or go into any lower sitting positions and don't work out your thigh muscles.

You need to stretch and strengthen the following muscles:

Hip flexor muscle group - the illiacus, psoas major and rectus femoris muscle.

Hip extensor group (hamstrings) - there's three muscles here but you usually work them all in unison.

Also your hip adductors, if they are tight that could also be contributing to your lack of mobility.

The ankle is the last place to look, IMO, and if you do look, Google something called "mobilisation of the talus." This is what most people have (instead of erroneously assuming they have tight calf muscles) but you should IN ADDITION to that also stretch your calf muscles (the gastrocnemius and soleus).

I highly suggest /r/flexibility for this. There's a hip flexor month (will cover you for those muscles) and if you look at the sticky that says "Don't know where to look?" you'll find excellent dynamic exercises for your hamstrings. There should be exercises for adductors there as well.
[cv46fl5] (score 3, diepte 0) If your form is correct but your body simply isnt able to perform the technique properly you may have poor mobility in your hips and/or ankles. Check out these videos with Kelly Starrett about mobility when squatting:

http://www.mobilitywod.com/propreview/squat-quick-test-is-it-tight-ankles-or-tight-hips-community-video/

He goes into a lot more detail in this video 
https://youtu.be/3WOpb8PrrSc?t=32m10s
[cv4i0et] (score 2, diepte 3) High school of origin? 

Mandatory question between fellow St. Louisians.
[cv4da2z] (score 2, diepte 1) What about mistweaving monks?
[cv40n0j] (score 2, diepte 0) Take two 10lb plates and stand, shoulder width apart with the back half of each of your feet on it. Place hands in goblet squat formation. Now squat, you should notice that it is considerably easier to drop your hips back to parallel, if not below. If that alleviates your problem you have ankle mobility issues/tight calves.
[cv41lbg] (score 2, diepte 0) Try and lift your big toe up a little bit as you squat down, that will force you to stay on your heels.
[cv44vok] (score 2, diepte 1 OP) True. I've never played a sport, so.....
[cv4h8d0] (score 2, diepte 3) I started doing 'third-world' squats every day to improve flexibility in that area.  Did wonders.
[cv4g5xz] (score 2, diepte 1) Can you talk about the talus mobilization for a bit? I have very tight ankles, and I feel tightness in the front of the ankle when I try and stretch, not my calves. how would I go about fixing this?
[cv44w1a] (score 2, diepte 1 OP) TY
[cv44lmi] (score 2, diepte 0) I want to preface that I've only been lifting a few months so take my advice with a grain of salt. 


I've had this problem for quite a while , and one of the trainers at the gym noticed that on the way up, I often bend forward at the hip and end up almost tipping over. I never have tipped over, but I fear that at a higher weight, I will. 

The trainer suggested a strengthening of my core so I can hold the bar up and not lose that core tightness when I try to drive up. He suggested planks in all directions.
[cv4cb1x] (score 2, diepte 3) Oh. In the video he said "try to squat with your feet touching each other" that's where I lose my balance if I went ATG.
When I do normal squat (high bar placement yet I'm told I should be squatting low bar placement since that's what my squat looks like) my feet are a little bit wider than should width apart, point outwards at a 15-25degree angle
[cv49vq8] (score 2, diepte 0) Maybe bring your tush back more?
[cv3zzg2] (score 1, diepte 0) Got a video?  How far apart are your feet?
[cv4p0ph] (score 1, diepte 4 OP) Hazelhood West man....
[cv40ihm] (score 1, diepte 0) Grab a light bar and just practice your form. Feel around a bit with your posture and it will come to you.
[cv4pcjv] (score 1, diepte 1) just bought chuck taylors for this specific purpose. I was lifting in running shoes and it was fucking up my balance.
[cv40vk2] (score 1, diepte 0) You could be doing a "good morning". It's a normal problem that happens when the hips shoot up faster than chest, leaving you with a forward lean and the weight on your toes. 
You need to brace you core before the squat, like you would if someone were to punch you in the stomach. Also make sure to drive your back into the bar as you go up.
[cv50jzd] (score 1, diepte 4) me too
[cv429go] (score 1, diepte 0) Video would certainly be helpful. As one person mentioned, could be related to poor ankle mobility. Equally, it could be the hip. Experiment with a variety of stances to see which allows you to achieve the range of motion you are looking for while maintaining a lengthened spine. Feet spaced wider than shoulder width and toes turned out around 30 degrees will position the hip joint for greater mobility than a narrow, toes straight stance.

I'll  normally try to keep some weight through the balls of my feet during the squat with an emphasis on pressing the rearfoot/heels into the ground.

You might also find goblet squats helpful as you work on mobility/technique.
[cv4377p] (score 1, diepte 0) Lift your toes. Not like the whole foot, but just pull your toes back in your shoes. Also make sure you aren't leaning forward under the weight and practice mobility stretches like the third world squat.
[cv43bn0] (score 1, diepte 0) I find looking up a little bit at a spot on the wall the whole squat helps me keep my form correct for heavier weights.
[cv4j3o3] (score 1, diepte 2) You need to force your talus to slide backwards when you dorsiflex (bring your foot closer to your shin). Take a look at this article:

http://b-reddy.org/2012/09/20/ankle-mobility-mobilizing-the-talus/

I've been doing the exercise with the band and I've gone from not being able to get my knees over my toes, to being able to get them WELL over my toes.
[cv4pkdf] (score 1, diepte 2) > No amount of ankle flexibility is going to stop the basic mechanics of how a lever works

except with more ankle flexibility, the basic mechanics of a lever don't apply as soon. infinite ankle flexibility can mean your knees almost touch the ground before your heels start to lift.

edit: but I agree with your stance width advice over ankle-flexibility advice
[cv4vbqo] (score 1, diepte 3) Your heels dont come up due to inflexibility they come up due to balance. Once your knees go in front of your feet your body only has two options to stay balanced: bend at the waist and stick your ass out or maintain your spine angle by letting your heels come up.

I dont mind the downvotes but people just reurgitate the same information without understanding whats actually happening.
[cv54nyz] (score 1, diepte 1 OP) This. This. This. Definitely helped!
[cv58vxr] (score 1, diepte 2) Awesome! Glad I could add a bit of help :)
[cv4679f] (score 1, diepte 0) ~~I used to suffer from the same problem when I started squatting. My PT advised me to put some light weights under my heels so when I squat I try to press on them with my heels thus the weight is on my heels.~~

and yeah, squatting barefoot  is better than squatting with running/non-flat shoes (at least for me), now I just wear some normal flat shoes when I am not doing cardio and exercising legs.

edit: just read [this](http://stronglifts.com/squat/#Heels_Come_Up) this is better advice
[cv49wkx] (score 1, diepte 1) rip no audio for me. Don't know why (for first link)
Although, I can squat properly and push through my heels (sometimes even letting my toes in the air to put more pressure on heels) yet I can't hold a pistol squat position nor squat atg with both feet touching each other. I never thought of myself as having a 'mobility problem' so really dont understand the whole point of 'mobility in ankles' when I feel fine while squatting
[cv4c2yd] (score 1, diepte 2) Aren't your feet supposed to be at least shoulder width apart?
[cv4m50q] (score 1, diepte 4) Im still learning all this stuff myself as im suffering through some similar issues as you but mine are actually keeping me from working/lifting at the moment. From what I understand putting your feet together and performing the squat test puts your body at its end range of motion or most extreme range of motion. It may not be the proper form for squatting under load but its a good test to see if your lacking mobility in your hips or ankles as its a position Kelly feels every healthy person should be able to acheive. Same thing with that Pistol position he shows in the second video. Hes basically saying if you cant get into this position and maintain it youve got a mobility problem.

Hes got a lot of videos that go over how to remedy these issues after youve figured them out at http://www.mobilitywod.com/ but I think you have to pay to access the best videos.
[cv571gi] (score 1, diepte 5) "if your lacking mobility in your hips or ankles as its a position Kelly feels every healthy person should be able to acheive" I could go to all my friends in Track, or go to the football team, and I'd say only 5% could hold the pistol squat, and only 15% could squat with feet touching each other (and these people are all athletes) I personally believe it's not mobility and more of strength requirement/stabilizing muscles. I stretch every day that I exercise so I have no idea what stretches I am missing out on? I run + bike so why do I not have this mobility?

Anyways. Besides that, as for YOU. My biggest tip , practice body weight squats with shoulderwidth apart, toes pointed outwards, and when you go down, lift your toes off the ground, (imagine you are sitting down and your legs are already touching the chair) you just bring your butt down (bend knees to the point where you wont lose balance tho) and just press through heels as you go up.
[cv62ehg] (score 1, diepte 6) Kelly Starrett works with professional athletes who cant do the pistol position but are still professionals despite having some mobility issues. You would have to pick up his book "Becoming a Supple Leopard" for a real in depth analysis on all the reasons your body is failing at certain positions but Kelly has said in the past that he believes static stretching is not beneficial to mobility.

I was able to find another free video regarding how to improve your mobility for your squat and pistol position. I wish I could provide you with more but the best videos require a subscription to his website. 

https://www.youtube.com/watch?v=_Gwgm3s2EQ0

You can view Kelly's Youtube channel here for the rest of his free videos. Theres a lot of good information in them though sometimes I do feel like he talks too fast to keep up with.

https://www.youtube.com/channel/UCnnB4zDBqZHhQ4uLTAX8eYA
[cv6dppr] (score 1, diepte 7) Uhm. I was getting at that you have to be strong to hold the pistol squat... lol
[cv49dsv] (score 1, diepte 0) Lean back, sit into your heels, drive heels into the ground and clench those glutes to power up.

Sounds like you should try some barefoot squats. If you do low bar, try high bar. Drop your weight to work on technique until you can do it without leaning forward. Do box squats (sit on then tap on a bench at the bottom) to train you to rock back. If you keep digging your toes in you'll be on the fast track to plantar fascitis and back issues.
[cv4a3e0] (score 1, diepte 0) I lift my toes in the air to ensure I'm on my heels. Tip from a friend in high school and it's stuck and worked well
[cv4c65i] (score 1, diepte 0) Sounds like a mobility or form issue.  Knees too far forward,  back angle too flat given bar position, collapsing back position in the hole etc.
[cv4ccrg] (score 1, diepte 0) Stick your butt out more and you will stay on your heels
[cv4clk9] (score 1, diepte 0) If you squat in flat shoes/chucks.... CURL YOU'RE TOES. this should help until you get used to it. Try it on your warm up sets.
[cv4faiz] (score 1, diepte 0) Your knees are probably travelling forward quite a bit as you descend into the squat. There's only so more dorsiflexion with have (ankle flexibility), when you use it up, for the knee to travel forward more, the heels have to come off the floor. Do some goblet squats and practice on your form.
[cv4fhyx] (score 1, diepte 0) My buddy squats on a 2.5 plate under his heels.  


Works for him.
[cv4gc5l] (score 1, diepte 0) Probably a mobility issues like others have said.

One little trick that I learned when I first learned how to lift was curling my toes inside my shoes when I squat. I helps keep the weight on the heels.
[cv4hn64] (score 1, diepte 0) I've read that everyone squats different and that people with longer shins tend to not be able to place their full foot on the ground while being totally parallel, so personally, I do not stress it.
[cv4i09n] (score 1, diepte 0) Get shoes with a reduced drop. Seriously, you want to be as close to flatfooting it as possible, best thing I ever did for my form.
[cv4i6y0] (score 1, diepte 0) I take my shoes off. I really feel that's the best way. Squatted in shoes, doesn't feel natural, without, you get perfect connection with the floor.
[cv4iapt] (score 1, diepte 0) I'd seriously start with just doing bodyweight squats and focus on form, then add weight. I wear Adidas Powerlift shoes, which are flat as hell and seriously help me drive through my heels. Equally, I'd get a pair of Converse and squat in those, or put some tiny plates (1.25KG's probably) under your heels so you have slight elevation. 

When you squat, just focus on driving through your quads, glutes and hamstrings, it'll come with time as well so don't sweat it.
[cv4iw28] (score 1, diepte 0) Practice 3rd world squatting for a few minutes every day. You need to stretch brah
[cv4kyz8] (score 1, diepte 0) Push through your heel
[cv4mjn5] (score 1, diepte 0) The vast majority of people squatting who haven't researched and really worked on form start the squat with forward knee travel rather than backward hip travel.  They try and keep their back "straight" when in reality they are trying to keep their back vertical.  

When you get over the fear of bending at the hips most people will naturally begin to squat deeper and have the weight in their heels as it should be.  The cues "hips back" and "nipples over the toes" have helped many people i've seen in person adjust their form in just 1-2 sets with much better balance and 4-6 inches of better depth.
[cv4mncq] (score 1, diepte 0) In my experience, there could be a number of things causing that. I somewhat have that problem, but I wear lifters now and can squat fine. If no lifters, try tossing a couple 2.5's on the ground and keeping your heels on them throughout the squat. It's basically the same concept as wearing a lifter.
[cv4npl4] (score 1, diepte 0) Ankle mobility and body proportions can cause this. If you want to feel firmly planted in the floor buy some good lifting shoes like adipowers. They are expensive but are worth it. They will also help with ankle mobility issues.
[cv4ogto] (score 1, diepte 0) My squat form was terrible to begin with (still is). 

I found practicing on a smith machine helped. It doesn't prepare you for using a barbell but it helped me make sure I was doing the right things with my feet, knees, and hips.
[cv4osns] (score 1, diepte 0) Plant your heals. Put the bar lower on your back. Do low bar back squats. Keep your back at the correct angle and this should stop it from coming forward which forces you forward. 

Check out Alan thrall on YouTube.
[cv4s4yh] (score 1, diepte 0) Main issue I found that helped me was shoes. I have a pair of normal Nike athletic shoes but the balance in a lot of these shoes are meant for other purposes or have too much cushion. I'd try a flat shoe or I personally just do barefoot/with socks. IMO it allows you to drive more easily off your heel and you have less support under your toes which helped me sit back more
[cv5161m] (score 1, diepte 0) How about box squats? Get a chair, proceed like you would sit down but do the sit down motion slow. You should feel how the weight is on your heels as your butt is going to land on the chair. Break at the knees. When you want to stand up, stick your chest out and try to get up with only the heels touching the ground. You should be leaning forward pretty much since you shift your gravity point. When you have the feel for the heels, do the same with the foot flat on the ground.

Hope it helps.
[cv53dhq] (score 1, diepte 1 OP) I think I'll try the box squats, I always thought it was ''cheating'' to do them, lol .
[cv5poyy] (score 1, diepte 2) Yeah just do them until you are confident in your form, after that you may do normal squats. :D
[cv53g92] (score 1, diepte 0 OP) Best, cheap flat shoes?
[cv4jqy4] (score -2, diepte 1) I dont understand how this advice always gets overshadowed by "ankle mobility". If your knee goes in front of your foot your heel is going to come up. No amount of ankle flexibility is going to stop the basic mechanics of how a lever works
(2 reacties met lagere score weggelaten)

=== THREAD 1qa9sts ===
SUBREDDIT: r/Residency
DATUM: 2026-01-11  SCORE: 23  REACTIES: 70
TITEL: Real talk. What shoes do you wear for work and how do you like them?
POST (source_id=post):
I’ll start, I’m wearing black Sketchers Slip-on Loafers and they’re ok but my feet are pretty tired by the end of the day and I want something better

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nz18bah] (score 45, diepte 0) Hoka.

They're big and bulky and I feel like a clown wearing it. My knees still hurt but I'm not dying at the end of the day
[nz1duzq] (score 33, diepte 0) EM: 

crocs specialist. A $30 shoe that was more supportive than any sneaker, and lasted 2 years before needing to be replaced. And that’s despite 
 hitting 12-15k steps per shift. 

Bonus points for being easier to clean than any other shoe ever.
[nz19vpq] (score 22, diepte 0) I wore Birkenstocks during anesthesia
[nz1bs1o] (score 13, diepte 0) I’ve got both hokas and on clouds. I love my hokas best but I’ve improved the on clouds tremendously by adding cloud sole insoles. 

Oh, and good quality compression socks are a must if you have tired legs/feet at the end of the day.
[nz1ru8t] (score 12, diepte 1) After hearing so many people’s recommendations, I finally tried them and they were TERRIBLE for me. They feel so unstable on the ground. I never got used to them. My feet hurt after every time I wear them.
[nz2cepo] (score 11, diepte 0) Brooks.
[nz34jmw] (score 11, diepte 0) Birkenstocks baby, nothing compares. Not even wack ass hokas that the nerds wear
[nz2o68d] (score 9, diepte 0) Don’t sleep on a good pair of lightweight hiking boots! The soles will save your feet for real. Bonus points for vibram
[nz1nmof] (score 8, diepte 0) I’m IM. Depends on who the attending is. If it’s someone who is long winded and makes us stand for more than two hours, my trusty danskos. Otherwise I rotate between Nike slides, hoka, Birkenstocks, and onclouds to match my scrubs
[nz1h4a1] (score 7, diepte 0) IM. Birkenstocks because I’m a dirty hippie. Got at least half of my residency also to cross over to the crunchy side.
[nz29ozj] (score 6, diepte 1) Hoka!
[nz1eai0] (score 6, diepte 0) Oofos
[nz347rh] (score 6, diepte 0) IM. Altras due to zero drop. Standing in one place all day means heel toe drop is a no no
[nz3jsxh] (score 6, diepte 0) Dansko clogs all day
[nz1slqd] (score 5, diepte 2) I gave up on mine several times initially. But past a certain time, somehow they became  lot more comfortable. I'm guessing the break-in time is longer because the material is thicker....
[nz73utb] (score 5, diepte 1) Big ups for the hoka crew.
[nz1lfif] (score 5, diepte 0) Brooks Glycerin for clinic/office. Xtratufs for OR. I’m OMFS
[nz1dtev] (score 4, diepte 0) North Face Alta Mesa 500. Amazing cushioning. Kind of blocky like Hokas are, but no heel pain and you can get them under $100
[nz30xtl] (score 4, diepte 1) Which ones? The Boston clogs or the Birki ones made with polyurethane? I love my clogs but I am always terrified to bring to work bc they'll get dirty and not easy to clean. I see a lot of ppl with the birki ones tho
[nz3yulf] (score 4, diepte 0) Vans. Love em.
[nz84zoa] (score 3, diepte 3) Mach 6. People said it’d feel like walking on clouds smh
[nz8ersu] (score 3, diepte 4) Gotta go Bondi
[nz19wri] (score 3, diepte 0) What specialty. Makes a difference
[nz1gdxe] (score 3, diepte 0) Ortho feet
[nz1lsin] (score 3, diepte 0) Ultraboost Parleys
[nz1zkts] (score 3, diepte 0) Calzuro all day every day
[nz8oyh9] (score 3, diepte 1) Love my Brooks Ghosts
[nz55v4o] (score 3, diepte 0) Whatever you choose, replace them every 1-2 years and wear compression stockings.
[nz838rg] (score 2, diepte 2) Which model did you try? I got tested and needed stability shoes so the Arahi were the only ones that worked for me. On my third pair now
[nz8gwfb] (score 2, diepte 5) Really hard to spend another $140 on a shoe brand when the first experience was terrible. My random $70 Nike/Adidas/Puma/NewBalance work way better.
[nz8h7tn] (score 2, diepte 6) They are actually 175.
[nzg6mv0] (score 2, diepte 4) I feel the same way as you about hokas. Def did not feel like walking on clouds. I decided to burn some more money and tried calzuros and absolutely love them. I had to wear my hokas for an outpatient rotation cuz my bright blue clogs wouldn't be appropriate and I missed my calzuros soooo much that month.
[nz1bn3r] (score 2, diepte 0) IM. Triple blacks On Cloudlit and classic grey 9060v6 new balance
[nz2c655] (score 2, diepte 1) Agree on the socks - they’re game changing n
[nz4x5cz] (score 2, diepte 1) Do they make your feet sweat and stink?
[nz35ijb] (score 2, diepte 2) A lot of people wear bostons, I got Londons so I can put the heel up if needed, though 90% of the time I just have the heel down
[nz1rmgq] (score 2, diepte 0) LeBron XX. Light yet super comfy and padded all over. Calzuros for call cause it’s easy to slip on/off for getting into/out of bed lol
[nz28mjk] (score 2, diepte 0) Vibram fivefingers.

Freaking love them
[nz8p5h4] (score 2, diepte 2) Literally the best.
[nz4sz9q] (score 2, diepte 1) Lmao
[nzhkprd] (score 2, diepte 0) Crocs mellow clogs>>>
[nzi0nx7] (score 2, diepte 0) Psych: Brooks & Compression socks. I'm running around the hospital often seeing consults. They work wonderfully and look great.
[nzm26bj] (score 2, diepte 0) IM:
Ive been using black Allbirds through med school and residency. Each pair lasts 2-3 years and i rarely have foot pain
[nz171rb] (score 1, diepte 0) Thank you for contributing to the sub! If your post was filtered by the automod, please read the rules. Your post will be reviewed but will not be approved if it violates the rules of the sub. The most common reasons for removal are -  medical students or premeds asking what a specialty is like, which specialty they should go into, which program is good or about their chances of matching, mentioning midlevels without using the midlevel flair, matched medical students asking questions instead of using the stickied thread in the sub for post-match questions, posting identifying information for targeted harassment. Please do not message the moderators if your post falls into one of these categories. Otherwise, your post will be reviewed in 24 hours and approved if it doesn't violate the rules. Thanks!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Residency) if you have any questions or concerns.*
[nz5txf3] (score 1, diepte 2) Ish, the crocs do too. At least there’s some ventilation on the sides, but I kinda get by with wool socks.
[nz1nrsj] (score 1, diepte 0) Female IM resident with ankle instability here. I like Cloves with Superfeet insoles for inpatient, and for clinic, I have two pairs of Born Toby Duo clogs (one black, one brown) that I match to my outfit. My feet very rarely hurt.
[nz1xx33] (score 1, diepte 0) Florsheim 🔥
[nzb0d62] (score 1, diepte 1) I want to downvote you sooo badly.
[nzb2xjq] (score 1, diepte 2) Lol, I have no shame. 

Personally, I love 'em, but I also grew up going barefoot everywhere and my preferred footwear is flip flops. So, yeah
[nz2mcyb] (score 1, diepte 0) New balance 1080s. They are super soft and help me with being on my feet all day. I have long and narrow feet so they are one of the few choices I have
[nz2xisg] (score 1, diepte 0) EM doc: oofos all the way
[nz356rz] (score 1, diepte 0) Oofos clogs are great in the OR. Comfy, waterproof (urology) and relatively cheap
[nz38xrg] (score 1, diepte 0) IM: Rothy’s clogs best I’ve worn hands down
[nz39bdq] (score 1, diepte 0) Cole Haan Grand Crosscourt Downtown sneakers. Running shoe comfort, looks like a sporty brown or black leather dress shoe, can wipe ‘em down with wipes. Win win win.
[nz3nz5v] (score 1, diepte 0) Hoka or cowboy boots
[nz3pzt6] (score 1, diepte 0) Ascis gel kayano. Nothing is better than that!!!
[nz3xgo1] (score 1, diepte 0) Cloves. Like being able to wipe them off easily, and they come in fun colors.
[nz43q3z] (score 1, diepte 0) Kurus or Altras all day (EM but wear them for my off service rotations too). Love that wide toe box.
[nz4k00u] (score 1, diepte 0) Brooks Ghosts if I’m wearing scrubs (I’m FM). Only shoes that don’t make my feet/knees hurt no matter how many steps I put in (I’m an old).

Birdies loafers (am girl) if I have to wear business casual, but thankfully that’s pretty rare.
[nz4lsh1] (score 1, diepte 0) Orthoboot on one foot, crocs on the other. Nobody expects you to run to anything, they clean up easily, and if you need to get up to do something just ask someone else to do it and they'll oblige.
[nz4o0yc] (score 1, diepte 0) On clouds. I couldn’t justify the cost. Until the fucking things lasted well over 2 years. Super comfortable.
[nz4op51] (score 1, diepte 0) Brooks revel v7
[nz5p8v3] (score 1, diepte 0) Oxfords.
[nz5q7y1] (score 1, diepte 0) ASICS Gel Nimbus clear Hokas by a pretty large margin. But Hokas look pretty.
[nz628v9] (score 1, diepte 0) General Surgery. Nike KillShot 2.
[nz6mgpv] (score 1, diepte 0) EM. I like clogs. Tried Danskos but they were too heavy. Like Clazuros better and they can easily be cleaned
[nz7gsu1] (score 1, diepte 0) FM attending
Merril jungle mocs, danskos, Clark's, born and spring step are all in my rotation 
I also have two pairs of Sperry loafers I wear occasionally 
Or my leather boots which get broken out occasionally
[nz9fkgp] (score 1, diepte 0) Yeezy 350 v1. The comfiest shoe i have ever owne md and look good too.
[nz9kfun] (score 1, diepte 0) TBH the FIGS new balances have been my favorite. Hospitalist
[nz9l0ov] (score 1, diepte 0) Love my chaco paonia slides, similar to a Boston birk but not as wide a fit. Wore on surgery and floors and they have held up great so far.
[nza5w4k] (score 1, diepte 0) Nike air maxes. Bonus if you get a cool colorway.
[nzabnav] (score 1, diepte 0) I wear On shoes, specifically the Cloud series. They are lightweight with good cushioning and keep my feet comfortable during long days of standing and walking.
[nzafehh] (score 1, diepte 0) The pink new balance 530s. 
Can’t abandon my whimsy like that 🧚
[nzbfoq3] (score 1, diepte 0) EM: Topo recovery shoes in the with a fluid repellent spray. Comfy and sheds fluids.
[nzcfcm9] (score 1, diepte 0) Anesthesia. Alternate between Calzuros and danskos
[nzd4fej] (score 1, diepte 0) New balance highly under rated. I’ve tried hoka, on cloud and they’re the best bang for your buck and the last. My hokas fall to pieces.
[nzedyme] (score 1, diepte 0) Nike Dunk SB 

Any model/colorway 

I’ve recently dabbled into Air Jordan’s
[nzg6avn] (score 1, diepte 0) 4th year med student applying gen surg. I scribed for nearly 5 years prior to med school and was constantly on my feet and never found good shoes. Herniated two discs 3rd year and tried what felt like every shoe under the sun before settling on calzuros. I swear by them now.
[nz1ir52] (score 0, diepte 0) Charcoal Adidas Gazelle sneakers.

