# Label-batch batch_0108

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
Schrijf het resultaat naar `batch_0108.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: nwx2nu, 1szbhei, phae1r).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD nwx2nu ===
SUBREDDIT: r/solotravel
DATUM: 2021-06-10  SCORE: 133  REACTIES: 73
TITEL: Fellow expats and long term travelers that have been grounded at home since March 2020, how are you feeling?
POST (source_id=post):
Hey y'all,

I guess I'm just trying to start a discussion with other long term travelers and expats who either made or were forced to make the decision to return home during this time. How are you? Where are you? What are your plans for when it's all over?

I graduated from college a few years ago and then promptly set off around the world with no plans to stop. This may or may not have been ideal but it's what I wanted to do. Then, just as I started a new dream job in a new country, bam, covid, sent home to figure it all out. 

Almost a year and a half later, I still do have itchy feet. However, I'd be lying if I said I didn't feel disconnected or confused about travel going forward. Does anyone else feel like they can't even remember what it was like to live that lifestyle anymore? Or can't really get in touch with why they were doing it? I know logically, but it just seems strange and distant at this point.

I still plan on getting back out there, but I have to say, I just kind of feel a bit confused now. I can't wait to travel again, but like I said, I feel very disconnected from that world now. Purely because I haven't had any choice but to give up hoping for it for a long time. 

I'm in the states. With the rate of things here and being vaccinated, things seem to be in this strange halfway normal purgatory. It's really surreal.

Anyways, anyone else relate?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h1c9gxt] (score 49, diepte 0) Not myself. I have been on the journey for so long that being home was strange. I felt depressed through a lot of it. I had built a life and it was a good life and to have that ripped from me left an emptiness. Going on a road trip this summer here in America and started creating an outline and finally felt myself again.
[h1bsigv] (score 33, diepte 0) I’m in a very similar situation, I’m from the UK and went straight into travelling after I finished uni, I was living in Canada and having a blast when the pandemic hit and have now been back home for the past year. My plan was to head to Australia after Canada but who knows how long it’ll take for them to open their boarders. I have very itchy feet as I planned years ahead what places I wanted to work/travel to and suddenly I can’t and now I feel like my life is on hold. I can’t even get some important things out of the way while I’m home because of covid like getting my drivers license and applying for my Irish passport, it’s all so frustrating! My family tell me its time to start my career and settle but I can’t give up yet, I don’t think I can stay in one place that long! You are totally right with saying it’s like purgatory I feel the same way
[h1dcpx3] (score 23, diepte 0) I am in the opposite situation. I am an American living in South Korea and I have been here the entire pandemic, minus a trip to Taiwan in January 2020 (when the pandemic was just getting serious in Wuhan).  I haven't been back to the US since August of 2019 and I don't think I will be able to go back until January of next year.

It fuckings sucks. I miss my family.

Being in Seoul has been good overall since they actually flattened the curve and kept the virus mostly under control. However, there are still a lot of restrictions and the vaccination rollout has been a total mess. I am also getting a little tired of the shenanigans you have to deal with as an expat here.
[h1dlgox] (score 20, diepte 0) I have to be honest, the pandemic really showed how spoiled the travel community is. I think a lot of it has to do with the fact that being confined to a single place, having no duties or responsibilities looks bad. It's easy to look busy if you're constantly traveling but it exposed a lot of my friends who were "travel bloggers"  as people who just live off their parents.

On top that, the lockdown really exposed the selfishness of this community.  So many people saying that things didn't apply to them. They were taking precautions,  it's their right to travel. A long standing idea I had that was confirmed is that backpackers think they're better than the countries they go to and most of them think they're vastly superior to the people and places they go to..I really soured to the travel community over covid because of how unwilling it was to take a step back and help society recover.
[h1ck0jl] (score 15, diepte 1) Bruh
[h1d8uf3] (score 9, diepte 0) By return 'home' i'm assuming you mean return to your birth country? I don't have a home there and returning there would have been financially ridiculous so I chose to go elsewhere. I'm over it. I'm leaving back to Europe and my semi normal life in a few weeks and I cannot wait!
[h1dpufn] (score 9, diepte 0) I’m 27, up to around 50 countries, lived in Cambodia, China, The Uk. I’m from Australia. I came back home after a short trip to Singapore and Europe (for study) at the start of COVID. I’ve felt identity-less over the past year or so. My girlfriend is French and lives in Paris. We’ve done long distance since we met while studying in China in 2019. 

And so… I applied for a Masters program in Paris, one of the best in the world for what I want to do. And some how I got in. I get to move to be with her and live in Europe again, living with her in Paris and also studying at an amazing university. 

Right now I’m just worried about money. The degree is expensive and I need to borrow a lot of money to pay for it. I’m also excited and since I found out, I’ve been overwhelmed with the feeling of needing to get out and explore again.
[h1eaae0] (score 8, diepte 1) Follow presence with the current moment and you will find that perception of self, expectations of self, and anticipations are all distractions from the present. Travel will come, adventure will return as it can. Keep on, and ground yourself in appreciation for being in the position that you are :)
[h1eachf] (score 8, diepte 2) I left my job to become a writer. But I found that traveling (at least my style) is cheaper than living at home. Discontent creates consumerism. I was always buying something  hoping it would add happiness but all I really needed were more time and freedom.
[h1c88fd] (score 7, diepte 0) Yeah, I hear you. I came back to the States after nearly two years away; my longest stint ever. I've traveled a bit here: Raleigh, New Orleans, Miami, but have mostly stayed with family in NYC. It's hard for sure. 

I'm actually wondering whether I should start to travel again, probably stay in Mexico since it's not too far away, OR, just move to a different city for 6mos-1yr while I wait for this all to die down. That kinda counts as travel, right? And at least I'll be in my country of residency. 

There are so many places I want to see right now but they're DEF not ready for foreigners. 

Nothing really helpful to say other than yah, totally get that feeling of being in limbo.
[h1cotfh] (score 6, diepte 0) After 15 years of vagabonding and living abroad, seriously feeling it.
[h1dscy3] (score 4, diepte 1) I'm also from the UK, but did the opposite to you, Australia first and then Canada after uni. With summers of working at festivals around Europe. I did feel like I needed a break so moved to a UK city a few months before the pandemic.

Now the batteries are charged and I can't wait to go. In the last year and a half I've managed to get a job as a part time remote Web dev (we'll see if I can keep it) but i might be able to go digital nomad.

As for actually travelling I do feel nervous about what the countries will be like to move around in. Will be hard to get around? Will things be open? Hard to meet people etc?
[h1d49z8] (score 4, diepte 0) I’ve saved so much money, and it has given time for me to spend more time with my friends (our country isn’t badly affected by COVID) more than I would had I had the opportunity to travel, so overall it hasn’t been that bad for me
[h1dzwbk] (score 4, diepte 1) Same here. We are expats is Cambodia and we've been here through the whole pandemic. Rumor is vaccines will come to our city in July and borders will open in Q4. We're hoping to visit family in the US this fall but who knows if that will really happen.
[h1e57tq] (score 4, diepte 2) Oof I'm in Vietnam and I wouldn't expect borders to open here til 2022 summer at the earliest.
[h1dyxil] (score 3, diepte 1) I’m in a very similar situation for you. Praying Australia or NZ opens up their borders before too long. Being stuck in UK is far from ideal, god Canada was lovely though ey
[h1en0f2] (score 3, diepte 1 OP) I totally relate. I have some family and friends here and there kind of subtly saying things and putting crafty pressure on me to stay. I love them dearly, but as you know, when you were born like this you really can't shake it. I don't want to give up on my dreams abroad. We may feel weird right now, but one day this will all be a distant dream.
[h1c5cji] (score 3, diepte 0) Same position here.  I’ve always enjoyed traveling.  Just started a new position where I travel to install equipment.  Just spent a few months in France earlier this year, I was really excited, and made the most of what I could.  But overall, it was a terrible experience; nightly curfew, 10 km travel restriction, maybe half of the stores open.  None of the ski lifts were operating. Most cable cars were closed.  It’s difficult enough trying to communicate with locals, but the covid situation made it so much worse.  I spent probably 90% of my off time in my hotel room.  Now I’m back in the states and have traveled to NY; better situation with most places opening up, but tourism is still suffering.  The tourist center just a block away is still closed, and any nearby activities get quickly swarmed by locals desperate to get out of their house; my hotel has literally doubled in capacity as soon as NY lifted a bunch of restrictions.  Until the tourism sector begins to recover, I think we may be in limbo for a bit
[h1d5xne] (score 3, diepte 1) I’m the same, currently planning to move to London just to get a taste of travel within my own country while everything else is closed off
[h1dwetg] (score 3, diepte 1) I’m in a similar situation. I moved here to Perth from America in January 2020 to be with my partner. I literally don’t know the next time I’ll be able to visit my elderly parents and friends back home and be able to return here. After handling the pandemic so well the Australian government has fucked up the vaccine and none of the higher ups seem to be in a rush to get out of this thing
[h1ems3a] (score 3, diepte 3 OP) I was in Vietnam for a couple years and left literally right as covid started (didn't leave because of covid, at that time it was still only in China). I really feel for all my friends over there, locals and expats, right now. Also, the visa situation right now sounds nuts!
[h1di9v5] (score 3, diepte 0) So, I’ve spent 4 years living and traveling around the world and in the beginning of 2019 I’ve decided to return home to focus more on career development. 
Well, let me tell you, that was an absolute shitshow. I was just about to hand in my resignation and go do fuckall once again when COVID hit. 
The little joys I’ve had from being home, all disappeared when that happened and I was struggling throughout the entire 2020. 
Early 2021 wasn’t better, but I’ve focused on that freaking career development and finally it paid off, I received another offer and moved away from home country so I’m a happy expat once again. 

Moral of the story, don’t go back home if you don’t like being home.
[h1dpg7e] (score 3, diepte 0) Australian here. Before 2020, I had a lot of plans - I was going to travel to the US/Mexico, India and Russia in 2020 and then move to Berlin for 1 year in 2021. At first when the lockdown happened, I thought maybe late 2021-22 I could travel overseas again but it’s becoming more and more clear that the world will be locked away for quite some time, and I think excluding potential travel bubbles and NZ of course. That said, although I have itchy feet I have taken the chance to travel Australia more, this year I’ve travelled to the Blue Mountains, Bermagui and now I’m in WA about to do a road trip from Perth to Broome. I’m grateful for the chance I got to travel overseas before and domestically now - but I’ve had a lot of reflection and there there were several parts of life I was struggling with and avoiding with travel. I’m now a lot more financially stable and have finally committed to therapy. So although I can’t wait to travel overseas, and I’m disappointed I can’t - it’s not something I can control and it’s time to improve my life in other ways. ❤️
[h1eqjl6] (score 3, diepte 0) It’s been shitty.

I’m not a long term traveller but usually go away at least 6 times a year. Currently working in a super monotonous job and travelling is my escape. Living in the U.K, where the weather isn’t great and holidaying at home is super expensive has made the last year and a half unbearable.

The weird plus side (I suppose) is that I’ve saved enough for a deposit to buy my first home. It was definitely eye opening to realise how much of my income I was spending on my passion. I’m also reconsidering my career path so I’ve been brushing up on my skills and looking at other opportunities.

I personally won’t be travelling again until all restrictions are lifted. I love the enhanced safety protocols like mask wearing and hand sanitisers on public transport, but it ruins other experiences for me. I can’t wait to get back to tiny crowded bars, dancing with strangers and mingling at hostels.
[h1e8s7c] (score 2, diepte 3) Me too! Can’t imagine indoor snowboarding was remotely comparable to whipping through the tress surrounded by stunning mountains. Ahh no I’m starting to miss it more and more just thinking about it now
[h1dsmw4] (score 2, diepte 1) How did you become the mother of an adult?
[h1eh80m] (score 2, diepte 2) Yah, maybe that's the move. Out of curiosity, where would you move to? I love London. On my list of places to live.
[h1en5rm] (score 2, diepte 3) I’m moving to south London, I’m luckily that I have a family member there that’s offered to let me stay with them! It’ll be nice to explore somewhere.
[h1es327] (score 2, diepte 4) Nice. Best of luck to you!
[h1dtre2] (score 2, diepte 2) I want to travel the US when it's safe to do so. Is it popular with travellers?
[h1f0epk] (score 2, diepte 3) it varies city to city but the hostels here in San Diego are busy and fun rn
[h1f6edj] (score 2, diepte 3) You're mentally ill.
[h1dmroc] (score 2, diepte 1) How did you afford itn
[h1gs1q2] (score 2, diepte 4) Lol the visa situation is nuts and why I'm leaving. I was about to redo my work permit and decided no thanks to a $1500 bribe.
[h1dgwvb] (score 2, diepte 0) I was grounded in the Caribbean, so... Yep... Pretty good.
[h1drv4a] (score 2, diepte 1) Bonne chance!
[h1en3z5] (score 2, diepte 1 OP) Congrats for getting in :) I'm sure Paris will be amazing. Cheers!
[h1eyjmp] (score 2, diepte 1 OP) I totally hear you. A lot of me doesn't even want to travel much till things are almost completely back to normal because I think it might just depress me to go somewhere but have it be some weird locked down version of what I remember. 

I'm really hoping that by mid 2022 things will really be on the way up all over the world.
[h1gcqy5] (score 2, diepte 0) I’m honestly more depressed than I have been in years, I feel like I’m treading water and I’m going to be stuck here working a dead end job for the rest of my life. I don’t even leave the house any more
[h1iwj2z] (score 2, diepte 1 OP) No, i had a dependable income, I went abroad to work 🙂and then continued to do so but was sent home due to Covid. I’ve had no trouble dating abroad either! I know it’s not the norm, but I’ve never been conventional
[h1e8lc1] (score 1, diepte 2) Man I miss Canada so much! Went indoor snowboarding the other day and it’s just not the same 😅
[h1c7n5q] (score 1, diepte 0) I'm sort of nervous. My travel facility expires at the end of July. I've contacted my immigration agent and started the process to get another RRV, but I'm in limbo right now until there's a determination made and it may be several more weeks before I know. I've been trying to wait out travel restrictions and quarantine requirements until going back but I might have to tough it out and deal with the hassle if I don't hear something very soon.
[h1fn1m7] (score 1, diepte 5) Thank you!
[h1dlh7r] (score 1, diepte 1) Why not travel the US? I've spent 2 months in Arizona and SoCal so far
[h1eh5db] (score 1, diepte 3) Right now, I really don't know. I caught wind of people coming here to get vaccinated, that's about it.
[h1egvqc] (score 1, diepte 2) Are you traveling around as in like, exploring different towns, etc?

I traveled around Europe (and a tiny bit of Africa) for a little over half a year then got an apartment there for a little over a year. I like to travel as slowly as I can and I'm kinda like a "park it in one spot" person. 

I'm learning that 3mos in a place leaves the heart too achy but may 6mos is the sweet spot. I also run my own business and love to establish new routines. I don't know about hopping around the States like I would a diff country. 

ALSO, I am a shit driver. If I move I will also take driving lessons. I could take some here but there's so much traffic that the instructors don't let you do any actual driving. It's like the driving equivalent of football. All start and abrupt stop, repeat repeat repeat.
[h1dl6wq] (score 1, diepte 1) Umm...well ...That escalated rather quickly.
[h1db2ej] (score 1, diepte 0) Just working (saving up far more than I planned to pre pandemic though) and counting down the days until I start traveling again next spring.
[h1e555a] (score 1, diepte 1) Eyyy what up I'm in the same boat in Vietnam! Leaving next month to go home tho!
[h1ddavh] (score 1, diepte 0) Moved to Russia a year ago and have been teaching here. Everythungs wuite normal here atm and has been for a few months. Only thing In worried about is taxes in America. When the pandemic hit I completely forgot about taxes. But I really didn't make much money here anyways. Because of the pandemic and Russia taking 30 percent from my pay.
[h1e9630] (score 1, diepte 1) The sour feeling I had towards travel culture for not being able to travel myself was curbed a bit by the fact that between the years 2015—2020, travel was more popular and EASY to an extent never seen before by mankind, and we were spoiled to a point we may never return to. Tourism will return, but the behaviors and mindsets defining responsible travel, adequate time off, and what one does during a trip and the reason for going that makes I worth it could all change going forward. I do expect that for some time we will all bump into travelers who, when asked what they are doing or why they are traveling after COVID, their response will be "because COVID" or "because I can and it's my time" which wouldn't bother me so long as they are contributing to a better travel culture and/or support the local area
(23 reacties met lagere score weggelaten)

=== THREAD 1szbhei ===
SUBREDDIT: r/BarefootRunning
DATUM: 2026-04-29  SCORE: 22  REACTIES: 72
TITEL: After 13 years living barefoot, I got plantar fasciitis... what do I do now?
POST (source_id=post):
I switched over to barefoot shoes 13 years ago: Altras (e.g., Lone Peaks) for trail running and nordic hiking, and Lems (e.g., Primals and Laguna) for work and casual outings. I honestly can't recall every model over the years because I go through shoes frequently. 

Anyway, I'm 39 now (145lb, 5'7"), and developed plantars fasciitis 3 months ago. A podiatrist told me I need more supportive footwear with big heel cushions and side support as well as orthotics (I do have high arches). I've also been doing my toe pullbacks and a couple of wall stretches daily that the podiatrist recommended, as well as rolling my foot on an iced water bottle... but I'm still having the heel pain after 3 months. Any recommendations? Is more supportive footwear and orthotics necessary? I'm not keen on how high rise footwear feels, but if it must be, let me know.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oj0uik8] (score 35, diepte 0) My mom had this issue. She stopped working out and used insoles for 3 months. Hers were a lot of micro tears that caused the inflammation. Once it was healed then she moved back to barefoot shoes and she's been fine. 

She also did some stretching, ice, and anti-inflammatories.
[oj1g50s] (score 13, diepte 0) My doc said the same thing. Orthotics, NEVER walk around barefoot, support, cushion. It's bullshit.

If you are not strength training, start. Actively stretch your foot while you are still warm and every time you sit down. Build a solid stretching routine after runs and workouts. Reducing your baseline inflammation will also help immeasurably. Be purposeful and regimented with this and it will go away.
[oj0vj1t] (score 12, diepte 0) I was finally able to kick my plantar fasciitis with a calf stretcher device called a pro stretch. Three times a day, 30 seconds on the right foot, 30 seconds on the left and so on for four minutes at a time. Takes a week or two but it works for me. Gives a deeper stretch than a towel or other methods have.
[oj1w7iy] (score 9, diepte 0) The only thing I've found to help with plantar fasciitis is lots and lots of calf raises.
[oj1t0m6] (score 8, diepte 0) I got PF for the first time last fall after over a decade in barefoot shoes. I also have a bad ankle on that side with multiple sprains, but nothing bad enough to require surgery or anything. 

It was horrible for a few weeks, but I went to PT and it’s been fine for 6 months now with zero issues and wearing all the same shoes I wore before l. None of the foot stretches and foot rolling did anything btw, especially the stuff on the bottom of the foot. It was all in my calf and the calf and ankle strengthening and stretching is what fixed it. 

So don’t panic yet. Don’t get orthotics, though some cushiony insoles can be a life saver in the early days just to help you get around with less pain.
[oj20rla] (score 8, diepte 0) You need a podiatrist who knows running.  And supports the idea of barefoot.  That is VERY hard to find. The problem is not in your feet actually.  It is the tightening of your calves that then pull your Achilles and cause inflammation at the heel.  Stretch your calves a lot more.  Use a “Slant board for calf stretching“ which is a product you can search for.
[oj0nako] (score 7, diepte 1) Did you happen to lose body mass when you modified your diet? Not trying to be a negative nancy but that is a WHOLE lot more likely than those dietary components directly trigger plantar fasciitis. Systemic inflammation doesn't typically manifest in acute, localized pain like plantar fasciitis and using "just reduce your inflammation" as a panacea is unscientific.
[oj0z0n5] (score 7, diepte 1 OP) That's encouraging, thanks for sharing.

You said it was your mom, so I'm not sure if you'd be able to answer this, but when you say stopped working out, do you mean she was pretty sedentary for 3 months? Do you think something that's not as much impact on the feet, like cycling or kayaking maybe, would be okay?
[oj0zqxs] (score 6, diepte 2) She only did what was necessary (like walking around work) and completely stopped all other physical activity. If you need to be active id probably pick things that used your upper body.
[oj19gw3] (score 5, diepte 0) I got plantar fasciitis for the first time in my life when I tried Whitin shoes after wearing vivos and Splay for a couple years. Turns out that the toe spring on their shoes causes PF. It took me a while to figure it out. If you didn’t have a change of shoes when yours developed, thats probably not the issue, though…
[oj1hgth] (score 5, diepte 0) I had a very similar story to this. Long time barefoot adopter - solved my nearly two decades of shin splints. Then, for seriously no apparent reason, got PF for the first time in my life. 

This video solved it for me, and I still do the heel stretch before every run or hike. 

https://youtu.be/72p58Iy6u7M
[oj4tc9r] (score 5, diepte 0) Sorry to hear this!

I say the following with the utmost concern for your health. This is not a pedantic or gatekeeping point but a serious, serious distinction. You have absolutely *not* been "living barefoot" if you're wearing shoes. There's a huge, huge difference between a strip of manufactured tread snugly fit to the bottom of your foot and exposing your super, super sensitive bare skin to hard, harsh, unforgiving ground.

I have many pairs of minimalist shoes and sandals. They're great. I also do a lot of serious training in totally bare feet. The two things are not at all the same. Shoes, sandals and totally bare feet are all crucial tools with specific use cases and no one is "better" or somehow "more" than the other. But they are very, very different.

Think on what all shoes allow you to do on a routine basis: push past your limits. With that strip of tread and a snug fit you don't feel pain when you over-extend your legs and feet out past their optimal range whether walking, hiking or running. That manufactured grip sends a signal to your body to over-leverage it. You get used to that crutch of grip.

Take the shoes off, expose that super sensitive skin to hard, harsh, unforgiving ground and now you feel it *immediately* when you over-extend. That kind of feedback is hugely crucial instruction on how to move in optimal ways.

You will never be strong enough or have enough mobility to handle repeated abuse to the body. When I was 39 I was about ready to give up running because I was constantly injured. I figured it was because I was getting older and "running is hard on the body." I also had high arches. I used to twist my ankles all the time doing nothing fancy, in fact.

I'm 53 now and training for yet another 50k trail ultra. I run in a mix of minimalist shoes, huarache sandals and totally bare feet. In fact, *most* of my running is in totally bare feet. I'm fit and healthy because I've let those bare feet instruct me on optimal movements. I've only twisted my ankles twice in the last 14 years and both times it was doing something stupid and the experience was a reminder to be more careful. In fact, both times I had footwear on.

If I spend too much time training in footwear my old, bad habits start to creep back in. When I feel the signs of injury start to creep up I go back to more running in totally bare feet on hard, harsh, unforgiving ground. It's like a master reset.

Orthotics, cushioning and support can be a trap. They immobilize your feet and let them get weaker over time. Then you need different orthotics and even more support so the feet and ankles get even weaker. It's a downward spiral.

This is a sport like any other. The most important part is doing the sport *well*. Fitness and strength supplement that but they shouldn't be the foundation of it. Sub-optimal movements will always lead to injury, frustration and setbacks. Better movement will always best apply your strengths. Without better movement you just end up fighting against yourself.
[oj0rgoi] (score 3, diepte 1 OP) Hm, that's really interesting and I appreciate the recommendation, although I'm not sure it's going to be doable for me to completely change my diet. For context, firstly, I'm not sure what classifies processed oils but I only use cold-pressed EVOO and avocado oil. And there are minimal refined carbs (and sugars) in my diet already. I worked really hard starting in 2018 and finally eliminated most processed foods from my diet by 2023... I'm not 100% but my monthly spot checks usually show 85% adherence. Honestly, I'm not going to get to 100% because of some other health issues that I won't bother getting into. I am glad it worked for you though, I know refined sugars can contribute to inflammation, so it makes sense why a diet change would help.
[oj43uy7] (score 3, diepte 3) Did she try swimming or any non weight bearing activity?
[oj5bzf1] (score 3, diepte 4) She just completely stopped all exercise until it was healed. She didn’t want to keep aggravating it
[oj0ynvc] (score 3, diepte 1 OP) Oh, wicked, I think there's one of these kicking around my house actually! I'll give it a try.
[oj0yqdw] (score 3, diepte 0) Why did you see a podiatrist? They see the world and the body through such a narrow lens. Feet problems often have little to do with the feet. But a podiatrist can't bill your insurance for treating you if they look at your knees or hips or back or shoulders. Their entire industry goes completely contrary to the schools of thought which lead to a healthier and happier life.
[oj1vx2t] (score 3, diepte 1) I definitely agree with this! You can do a lot in the gym without stressing your PF! Leg extensions, hamstring curls with a machine or exercise ball, adductors, upper body. I’d skip things like deadlifts, farmer carries, anything where you actually have to lift some heavy that will put a lot of pressure on your feet. Cuz it really sucks to finally get on top of your PF and then be way out of shape and have to start over. When you’re ready, calf raises…but honestly, make sure you clear those with your PT, those need to be done progressively and a LOT.  Getting your PT to identify areas of weakness or imbalance in your core, sometimes PF is a result of those. You’ll get there!
[oj0ty3r] (score 2, diepte 2) Not only ultra-processed foods can cause the systemic inflamations. And if you have other issues, that actually could be the case that there's something else.
[oj14huq] (score 2, diepte 5 OP) Yeah, I'm 90% in range now, which is quite good for type 1s
[oj1cytk] (score 2, diepte 0) I had it last year I got a knees over toes type slant board and stretched the crap out of my calves.  My calves were so tight. I had some work shoes that were really tight and I kept wearing them cause they were spendy. I threw them away as soon as I noticed they made my feet hurt worse. I also did a lot of calf raises at the gym. For me it was the shoes. I transitioned between regular shoes and barefoot. I noticed that running and walking in traditional runners really made my body hurt. I was also rucking quite a bit and I took a break from that. The plantar fasciitis only lasted about 4 months. I did not stop walking or working out.
[oj1d5y2] (score 2, diepte 0) How strong are your legs and glutes. In my case, taking care of them at the gym changed it radically.
[oj4vt7c] (score 2, diepte 1) Go barefoot gradually.  Naturally stretch out your foot.  When I read Born to Run, it convinced me to get back in touch with the earth. 15 years ago.   I don’t run but feet and ankles are super strong.
[ojs4v7p] (score 2, diepte 1) I spent 3 years fighting PF. Took breaks from running, stretches, protocols, inserts, different shoes, etc….

I started a kettlebell routine and things started getting better. Added in weighted reverse lunges and poof. Magically gone after years of chasing this BS. 

All of that to say, strength training is your friend and you don’t have to be crazy about it. Literally five weighted reverse lunges on each side every day and its been gone for 3 months now.
[oj1xel6] (score 2, diepte 0) Getting a fascia massage (Rolfing) in my feet fixed my plantar fasciitis, after years of suffering and two useless podiatrists and their useless, expensive orthotics.

Good ol' Dr Scholl's insoles work well if you can use them, but for me the problem didn't go away completely until the fascia massage.
[oj3l4vi] (score 2, diepte 0) Go to a physiotherapist not a podiatrist. Podiatrists alwayssss recommend orthotics and special footwear when they need specific strengthening exercises most likely.  I've had tendonitis a long time and podiatry just recommended insoles .. my physio has given me a ton of exercises over the past 6 months and the lumps on my tendons have really gone down! It's actually soxing the problem, not just using an orthotic to treat symptoms
[oj3oaj5] (score 2, diepte 0) Take magnesium- I’ve had PF act up periodically for the last 15 years. I do a lot of running and tight calves seems to trigger it. Magnesium helps with hydration and loosens muscles. Also stretching and I have a massage gun that can help it when it does flare up. Good luck, it’s not a fun thing to deal with
[oj3wai7] (score 2, diepte 0) Strength training solved everything for me. Especially training the lower parts - glutes/hamstrings/...
[oj6tqjp] (score 2, diepte 1) When I was 39 I was about ready to give up running because I was constantly injured. I figured it was because I was getting older and "running is hard on the body." I also had high arches. I used to twist my ankles all the time doing nothing fancy, in fact. I did all my running in cushioned, supportive shoes.

Change running to hiking, and this has been my experience. Weak ankles (broken bones, torn ligaments, endless twisting). Plus impossible foot cramps that would have me on the ground for 30 min before I could keep going. High arches as well. Now that I'm completely barefoot, I've taken up running, and I'm hiking/walking/running at least 60-70 miles a week. Part of the reason I can do so much is that I immediately feel pain or discomfort when I land badly, and I can correct what I'm doing wrong, preventing injury. 

I never thought that I'd be more fit in my 40s than any other era of my life prior, but here we are.
[oj849fi] (score 2, diepte 2) Amazing how easy it is when you're moving optimally instead of fighting against yourself, isn't it? :)
[oj0tzww] (score 1, diepte 3) So you don't think losing 20 KG (45 ish lbs) had anything to do with the pain going away? I'd put money on you losing weight since the pain comes from stress and inflammation of the area. It probably felt like that diet caused systemic inflammation to be reduced, but realistically not eating oils and carbs made you lose weight quickly. I'm glad it worked for you, but reducing whatever you think bad carbs and oils will probably not work for most.
[oj0ygnx] (score 1, diepte 3 OP) Other issue is type 1 diabetes, hence needing to eat some refined sugars if my blood sugar is low. And yes, I guess it's possible that T1D contributed to the plantars faschiitis. It's a lot to get into managing a chronic disease like that and iykyk.... but really just looking for other people's takes on if supportive footwear is necessary. I appreciate that you cleared yours up with a diet change, I just don't know if I can change that much more in my diet to really make a drastic shift in my foot health.
[oj0zy26] (score 1, diepte 4) I actually was a bit interested in the diabetes and came along a few doctors who have T1D themseves and who keep their blood sugar in the normal range.

Dr Bernstein, for instance.
[oj10foi] (score 1, diepte 4) Also Andrew Koutnik, PhD metabolic health.
[oj2tu9s] (score 1, diepte 1) Not sure why you are getting downvoted when this is such a common issue. In general, a high percentage of ultraprocesssed food and ingredients in a person's diet causes a constant "baseline inflammation", which is responsible for a whole host of aches and pains, not to mention serious health conditions.

For anyone, switching to a whole food diet is one of the best things they can do for themselves and it's guaranteed to reduce inflammation and any related pain.
[oj338xh] (score 1, diepte 3) "all what you need for life" okay, enjoy life without fiber and water, I guess.
[oj35dm8] (score 1, diepte 4) We cannot digest the fiber. It is totally useless as nutrient. But it creates irritation and bloating. IDK why people like so much to make winds.
[oj32tqd] (score 1, diepte 2) Longer a "food" can stay on shelves - more of what works as conservant it contains. Sugar, trans fats, salt. The food industry like to put all these in all "foods". It can stay on shelves for years.
[oj2alzc] (score 1, diepte 1) Do you know if it is all their shoes? I randomly have a pair of their Mary Jane shoes I wear instead of flats. I was considering trying some of their other ones but I'm mostly used to xeros casuals.
[oj2gxcm] (score 1, diepte 2) It’s been on every model I’ve seen. Does the end of toe of the shoe sit completely flat against the ground? Every pair I’ve seen curves up at the toe.
[oj1dmgj] (score 1, diepte 0) Toe squat Vajrasana!
[oj2ljo0] (score 1, diepte 1) All hail Jeff!! He’s the man
[oj2k7ey] (score 1, diepte 1) Any exercises they have you do that aren't well known?
[oj3ymdd] (score 1, diepte 2) Not really. Lots of calf raises, balance stuff, squats.
[oj1y0am] (score 1, diepte 0) Two words: New Balance
[oj2c4ve] (score 1, diepte 1) This. And get a cork ball to help you massage your calves, that's worked a lot better for me than stretching. Consider supportive insoles until the inflammation goes down
[oj23s90] (score 1, diepte 0) Keep in mind that I'm not a doctor or a physical therapist. 

Talk to a doctor and a physical therapist and see if it could be related to having a tight/weak calf and Achilles. And then see if eccentric calf raises or calf loading would be appropriate treatment to help out. 

Why? Because I was not targeting foot pain. I was specifically targeting an Achilles injury. After about 3 weeks of doing the eccentric calf raises consistently, my foot pain went away. It was not specifically plantar fascitus. But the great and wonderful internet tells me that plantar fasciitis could be related. 

So again, talk to your medical providers. If you don't have the time, money, or insurance to go do PT, there are a plethora of videos about eccentric calf raises from physical therapist and physiotherapist on YouTube. The huge thing is you start with very small load. Meaning, yes you're just using body weight, but don't do 100. Absolutely don't do 100. The first day you do like three sets of eight. And you do that three times a week for like 3 weeks. And then you can start increasing based on how you're progressing. And I'm going to tell you that you should probably train each calf equally which will help out with downhill hikes and runs anyway. 

By the way. I've seen a podiatrist about my achilles pain and they have told me that I needed raised up shoes like running shoes. Like about a half inch lift. They're just not that proactive about wanting to actually fix the problem like a physical therapist would be. A good doctor of physical therapy(DPT) wants to get you back to functioning in your lifestyle, which in this case is trail running.
[oj2mesn] (score 1, diepte 0) i found for me it was related to posterior chain tightness. i took a break from treadmill running but nothing else. increased quad, hamstring and calf stretching, and it eventually abated. I did wear my high stack altras during recovery and got some heel cups for a little drop when it was painful.
(33 reacties met lagere score weggelaten)

=== THREAD phae1r ===
SUBREDDIT: r/Frugal
DATUM: 2021-09-03  SCORE: 230  REACTIES: 72
TITEL: I finally found some not-too-ugly foam slides (in my size!!!) at the thrift store, but they make a weirdo squelching noise when I walk because my feet suction onto them 😅 Any suggestions for making them shut up?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hbh38ok] (score 96, diepte 0) Baby powder or cornstarch?
[hbhxkxh] (score 84, diepte 0) Socks.
[hbhml5s] (score 73, diepte 0) This is really strange but it works for me! Rub a stick of deodorant on your the bottom of your heel.
[hbh41ih] (score 64, diepte 0) A hole punch, where the suction happens. >BAM< no more suction.
[hbhn9jp] (score 62, diepte 1 OP) This sounds so tempting, but I feel like with my luck I'll step on a perfectly placed nail lol
[hbimrso] (score 40, diepte 1) 😐 I’ll have to try thing. Foot farts while wearing Birkenstock’s gets embarrassing
[hbhtqgp] (score 36, diepte 3) Or drill some holes in your foot!
[hbhfhed] (score 23, diepte 0) I have the same issue with some shoes. Pfft pfft pfft smak  Uggh FWIW actual Crocs dont do this to me. I think its the bumpy bits in the sole. If you shop around you can find slides for $20 which in crocs pricing is a deal . lol

I can tell you what i have tried out of desperation that hasn't worked. lol What does work is donating them to goodwill. 😉

Tape on the shoe- Note: I didnt try hockey tape. I tried K tape. It gets hot sweaty, moves around and then leaves a sticky spot so you add another dimension to the noises your feet make when walking. haha

Giant fabric bandaids that you use on your knees. I put those on the arch of my foot. I used bandaids because i figured the pad part might help. These were slightly more successful and what I use for shoes I love and will never wear to anyplace totally quiet. lol

Powder works for a little bit. It also looks really gross because it gets where you can see it. And super gross once your foot starts to sweat. 

If you do end up with something that works let us know. Im sure we arent the only ones.
[hbi6l0u] (score 22, diepte 2) Me too! Actual foot deodorant spray works well too
[hbhtmp9] (score 21, diepte 2) Doesnt need to be a hole through to the ground, grooves that run along the surface your foot rests on (must be a name for that?!) to allow air in & out would have the same result... a dremel might be good for this but failing that you could use a Stanley blade/craft knife..... anything to break the seal!
[hbhk3ga] (score 19, diepte 1) Dyson doesn't like this idea
[hbhtyrq] (score 19, diepte 4) Actually, just glue the slide onto your foot so air cant get in in the first place!
[hbhukrl] (score 19, diepte 0) walk on your hands
[hbh40rx] (score 18, diepte 0) Sometimes those stickies for inside of shoes to keep your heels and the ball of your foot from moving can help :)

Edit: call to ball
[hbiamfv] (score 17, diepte 1) Is this a joke?
[hbhtu9o] (score 16, diepte 1) I came here to say this.
[hbh43bc] (score 11, diepte 0) Strip of hockey tape should act as a bleeder. Either that or a straw sized hole through the sole…
[hbjkug9] (score 11, diepte 1) Socks and Birks are good. Legitimately wear mine with socks 90% of the time
[hbi3q8h] (score 11, diepte 0) I have not found a permanent solution but Goldbond powder or spray-on works a bit. My actual Birks do this and the first time I met my husbands extended family they made a gigantic farting noise in front of everyone and I wanted to die.
[hbkflly] (score 9, diepte 2) I have farting Birk's too. I've had to stop wearing them if I'm going somewhere quiet.
[hbifvjm] (score 8, diepte 5) Yes. Gorilla glue foot to shoe. Perfect.
[hbij44n] (score 8, diepte 6 OP) This is strictly an E-6000 household 😅
[hbijegd] (score 7, diepte 1 OP) Thank you for your experience!!! I posted in this sub because I thought you'd all have better suggestions, but maybe I should have put it it r/ zerowaste lol. I try to only buy things new when I absolutely cannot get them secondhand, so I was super super excited to find these shoes :'( I'm set on making them work because I'm unlikely to find anything better lmao.
[hbl7io7] (score 7, diepte 3) Haha I feel so much less alone now. I didn’t realize other people have farting shoes, too.
[hbio3e8] (score 7, diepte 1) I came here to say this. 😂
[hbk5ryd] (score 7, diepte 2 OP) The whole point of getting them was so I don't have to put on socks for sand volleyball, or when I'm just going downstairs for 3 seconds )': I feel so cheated lmao
[hbibxjx] (score 5, diepte 3) Hot knife would do the trick
[hbim5f8] (score 4, diepte 2) Yeah I understand totally. They would make good house shoes. We don't wear our shoes in the house but my feet hurt if I go barefoot all day so I started wearing generic crocs in the house. That has helped a lot.
[hbi1lvk] (score 4, diepte 0) Socks 🧦
[hbinqcj] (score 3, diepte 1) Yes, have these in all my sandals. They would fix this.
[hbi5z49] (score 3, diepte 0) Embrace the squelch…
[hbihri1] (score 3, diepte 0) I've used moleskin padding. I find that it adheres well
[hbiyjof] (score 3, diepte 0) While I hated the big retailers, Walmart sells these new for pretty cheap, for those who can't find them elsewhere. I think they were CAD$12
[hbj9lpr] (score 3, diepte 0) Knee high white gym socks
[hbjdh39] (score 3, diepte 0) Powder
[hbh55sb] (score 2, diepte 1 OP) Oooh, I'll have to look up hockey tape! Thank you (:
[hbi5ios] (score 2, diepte 0) Use just a pin
[hbi70yw] (score 2, diepte 0) I’ve heard using antiperspirant on your feet works
[hbi9v9a] (score 2, diepte 0) I got these same ones from target..same sound..as i walk
[hbiahyu] (score 2, diepte 0) Socks
[hbidsnh] (score 2, diepte 0) Search for noise reducing/suppressing shoe pads. They’re what they use in movies so shoes don’t make noise
[hbijhao] (score 2, diepte 1 OP) No 😅 I love them
[hbiqx3f] (score 2, diepte 0) Talcum powder works too
[hbirb5a] (score 2, diepte 0) Baby powder
[hbis2pi] (score 2, diepte 0) I've never been ashamed of my foot farts, but now i kinda am 😩
[hbjvg75] (score 2, diepte 1) Got a pink pair for CAD $10 and matching ones for my daughter for $5 this summer from Walmart. They’re not super comfy for me though and didn’t have enough traction to wear most places other than taking out the trash. I think next summer I might spend a bit more to invest in a good durable pair.
[hbizb4i] (score 2, diepte 0) Put them back in the donation bin.
[hbj0rqs] (score 2, diepte 0) Did you look for a volume knob?
[hbh2t3g] (score 1, diepte 0) Hey mickier, thank you for your image contribution! We like to have discussions here on r/frugal. To avoid your post being removed; 

**If you're posting something you made, repaired or refurbished**, please leave a top-level comment under your post explaining how or why you went about it, how much it cost, how much time it took, etc., and share the recipe or materials needed. 

**If you're posting a general image**, please leave a comment explaining how it relates to frugality and any other details you'd like to share! Thank you for participating in r/frugal!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Frugal) if you have any questions or concerns.*
[hbhu5uu] (score 1, diepte 0) If it’s sweat-related, you could try a waterproofing spray on the soles?
[hbi3olv] (score 1, diepte 0) I put those felt insoles in my Crocs to stop this. It might not work as well without adhesive in an open toe shoe.
[hbi3sac] (score 1, diepte 0) Lol nope I have the same problem 🤣
[hbkfnlj] (score 1, diepte 1) I'm trying this today!
[hbipj8n] (score 1, diepte 0) WD-40
[hbiqsmd] (score 1, diepte 0) Socks
[hbis41y] (score 1, diepte 0) Honestly those shoes look a size or two too big for your feet...
[hbispyg] (score 1, diepte 0) A little hole pierced thru the bottom.
[hbiu1sq] (score 1, diepte 0) Do what they do with those style sandals [in prison](https://64.media.tumblr.com/10bf4e0cd783ea71816b4758ed767e1d/tumblr_pqa8a2WIle1w2xn30_1280.png): wear white crew socks.
[hbrnjxi] (score 1, diepte 2) That's the issue with footwear! I love mine way more than any flipflops or slides I've ever had, but holy if I haven't had a hard time with shoes that others have sworn by.

Burkenstocks aren't inherently a big spend though. Expensive and durable is sometimes far more frugal than cheap and fragile/fast wearing. I think my mum has worn the same pair of burkenstocks about 1/4 of the days in the year since 2000 and only had them resoled once.
[hbj0s77] (score 1, diepte 0) Foot powder
[hbjpoa3] (score 1, diepte 0) Skin-coloured toe socks.
[hbjwy9e] (score 1, diepte 0) Go without the shoes ;-) . Easiest solution :D
[hbkc5yx] (score 1, diepte 0) Drill a few holes in the sole
[hbkd6ac] (score 1, diepte 0) Vasaline
[hbkigps] (score 1, diepte 0) I have a few pairs of these foam slides, the black ones are weirdly the only ones that make my feet fart. FYI they’re like $7 at Walmart so pretty cheap. 

Also, I embrace the foot fart. It makes me laugh.
[hbtx7lz] (score 1, diepte 1 OP) I wanted sandals so I can stop messing up my regular shoes at sand volleyball places, and check it out! I got some! (: I'm very happy with them lmao, I call them The Birkencrocs.
[hbhi967] (score 0, diepte 0) Take a piece of sand paper or even a Brillo pad and rough up the spot that squeaks
[hbii3op] (score 0, diepte 0) Return them to the thrift store. Or toss.
[hbsl71i] (score 0, diepte 0) What do you mean for not-too-ugly? These are the ugliest pair I ever seen
[hbit8db] (score -1, diepte 0) Throw them in the trash bin!

