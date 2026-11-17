# Label-batch batch_0064

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
Schrijf het resultaat naar `batch_0064.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 10iru42, sosif2, 1juty75).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 10iru42 ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-01-22  SCORE: 103  REACTIES: 192
TITEL: Feels so weird when the AMs beg you to take vto. One of my AMs practically groveled at my feet trying to get me to leave anyone else’s ams doing this?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j5gf7kf] (score 86, diepte 0) Yeah, Vto is primarily a cost savings action. As AMs their job is to VTO as many allowed or as many as possible.
[j5gd6uz] (score 76, diepte 0) I've got a manager who does the same thing, the other night he had like 9-10 people retaping the floors because we didn't have enough work and every time he passed by he'd ask how that VTO was sounding lol.
[j5h2tky] (score 45, diepte 0) No VTO. Only VET
[j5hezyg] (score 28, diepte 1) Last time we did that tape garbage. I legit went to the break room for 2-3 hrs. Went back the last 45mins.
[j5ha6vy] (score 27, diepte 1) Same here, with surge pay too.
[j5gcwun] (score 23, diepte 0) No, but I’ve been hearing ops telling pick managers we have to start running as lean as possible and to pay close attention to headcount
[j5gua7f] (score 21, diepte 1) They literally sent a full month of vto out yesterday to my fc lmao
[j5gdiha] (score 20, diepte 0) It cause none of the AMs/OM wants to write a wash that says “tph sucks cause not enough people took vto” 😅 Idk about grovel but I’d definitely check with my team consistently in case someone wanted to go home later, found a ride, etc. I count it even with all the times they ask me for VTO, brings a nice power balance 😂 They’re allowed to say no to my request and I’m allowed to say no to their request
[j5gpx1s] (score 19, diepte 0) Send them my way I'd love a vto day haha
[j5grit7] (score 17, diepte 0) My PA did that earlier this week! Today I went in and it was dead and like a ghost town. I ask my PA do need me today? She was like well… We could use you, but we don’t need you because we’re above head count, so it’s up to you if wanna go or stay… I told her to scan my badge and she said thank you! Lol
[j5g4f2d] (score 16, diepte 0) Been there, but not in a while. At the time I rode the bus to work and worked night shift. Had absolutely no way to leave had I taken VTO.
[j5gr0qc] (score 14, diepte 0) "MTO or nothing"
[j5gw4pj] (score 12, diepte 0) What don’t you understand? Their bosses are screaming at them to reduce headcount. They are just trying to keep their jobs. Doesn’t mean you have to leave at all in but sometimes everyone of us is trying not to get fired
[j5g6f6v] (score 10, diepte 1) Yeah as a DS manager this is false. No cash incentives. All for metrics, specifically one called Cost or TPH. Aka how much can you process with minimal headcount. Everyday a plan is made based off volume, that gives managers the needed HC for the shift based of set rates. When the shift starts, and it is over headcount, the managers job is to VTO down to headcount in order to hit cost. If they can perform the days volume with less than the planned headcount, cost will be even better. And senior leadership wants/pushes for that so managers are heavily pushed into it too. We have to pretty much show we are doing our best to minimize our headcount lol
[j5g9zxm] (score 10, diepte 3) You clearly didn’t read or understand my comment. I am disagreeing with you. No bonuses, no cash incentives. Not in the 3 years I’ve worked as a manger here
[j5jlkl7] (score 10, diepte 3) Yea, won’t be doing that…
[j5g4tw6] (score 9, diepte 1) No there’s not lol it’s just helps the buildings metrics if work is slow otherwise sr ops freaks out about a low tph
[j5hu9z9] (score 9, diepte 1) Theyve made me and a few others do that before. Didnt hear one peep about VTO. At this point I’m convinced VTO is site specific or I’m on some sort of blacklist.
[j5gm0rv] (score 9, diepte 0) Nope, but man would I love some. Been almost a whole year since I've seen VTO.
[j5gwko7] (score 9, diepte 1 OP) I’m not like making fun of them or anything gotta do what you gotta do, just never experienced it till now and wanted to know if it was common.
[j5he7hn] (score 9, diepte 2) Likewise been like that all month.   Hell I wish an AM would beg me to take VTO.
[j5hu3x0] (score 9, diepte 0) We don’t have that problem at mine, most people are begging to take VTO.
[j5gx3w4] (score 8, diepte 1) Same, I was getting a ride when I was offered vto, couldn’t take it if I wanted to
[j5h0lkz] (score 8, diepte 1) That's not just a TPH thing thats a throughput thing, depending on your building type sometimes you don't have the safety valve of tranship, so in the event they start overpicking you run risk of putting everything in AGL.
[j5h72ir] (score 8, diepte 2) This time of year yes. Q1 has the lowest consumer spending so backlog is normally low on top of Peak labor levels. It will gradually improve until the summer
[j5j6sqh] (score 8, diepte 1) Then their bosses/GM bosses need to do THEIR jobs and MAKE ENOUGH VTO slots IN THE MORNING AVAILABLE to Associates. You know BEFORE WE HAVE TO LEAVE OUR HOMES FOR WORK. 

Especially if you don't live in the local area where your FC is and need to commute over 40mins to get there. Especially  when there is inclement weather (snow, ice, rain etc.) out. If these $300K+ Total Compensation Lvl 6+  upper managers could actually just perform their managerial jobs EFFECTIVELY for JUST ONCE. Gauge/estimate/forecast the supply of merchandise coming in on the trucks (in the early morning and again at 2pm  in the day). We associates wouldn't have to be made to suffer for THEIR inability to do simple math on the headcount...
[j5j6dl7] (score 7, diepte 1) They do that shit cause they know it kills your knees. Theyre pieces of shit
[j5jmnb2] (score 7, diepte 1) If labor plan has the VTO hours at least. Otherwise not nearly as common as it could be
[j5h3brj] (score 7, diepte 0) Last year at this time, they were begging at stand-up.
[j5g3tnh] (score 6, diepte 0) It's just pathetic, isn't it? 😂🤣 I had one asking me on the hour by the hour. Sometimes it feels like borderline harassment.
[j5jke6z] (score 6, diepte 1) And this is horrible, the company makes millions/billions - they can keep paying ppl and be happy they have workers who want to work. But this is me venting my hate towards Amazon
[j5jzhhh] (score 6, diepte 2) AMZL doesn't make money.
[j5hqqpy] (score 6, diepte 1 OP) Its so hard to say no to vto
[j5j8gx2] (score 6, diepte 0) Tier 3 here, they usually send me to do their dirty work. I’ve had to go wall to wall in AFE (OB) pack side several times asking AAs if they want VTO. It’s usually not a problem and there’s quite a bit of interest but once we get heavy into VTO season it could be more of a struggle. That’s exactly right, who ever mentioned the cost cutting measure. Even if they’re pushing VTO hard, you do not have to take it, you’re scheduled to work, and if there’s no work, so be it. However when we run into this issue we tend to labor share our entire department elsewhere (pick, ship dock, vrets. Interest in VTO tends to skyrocket once word gets around about labor sharing.
[j5jbzep] (score 6, diepte 0) Meanwhile at my FC:
“Hey clown! You going nowhere! I got you for ten hours!”
[j5hc8n7] (score 5, diepte 0) I’m a PA and I’ve never witnessed AMs beg people to take VTO, upper management never lets us VTO unless the volume is stupid low and I have way too high of a headcount, with standbys. It’s likely because the volume is way too low and upper management is breathing down their necks and getting on them about their headcount being too high.
[j5kmyb0] (score 5, diepte 3) Make sure you wear a Toga.
[j5js7fl] (score 5, diepte 0) Just tell them no, they can't make you go home.  And if they do it better be paid
[j5ipt0m] (score 4, diepte 2) Site specific
[j5jobat] (score 4, diepte 2) Sure. That’s exactly why they do it.
[j5irn3o] (score 4, diepte 0) If people applied for full time work dont try to make it part time to save your ass. If they didn't write their name down.. leave them alone and let them make their peasant wages.
[j5k6l0e] (score 4, diepte 2) Very philosophical.. I will ponder this on a mountain top and come back with an answer.
[j5h1481] (score 3, diepte 2) They don't, they just don't want to have to write a bridge on why they lost hours. If your shift is nights, your OPS doesn't want to be on a call at 11AM explaining why they lost hours, they want to be home in bed asleep.
[j5kl85o] (score 3, diepte 1) I spent $40 to go home via Uber when I was in that situation..not cheap, especially when also factoring lost income while taking VTO.
[j5hqul0] (score 3, diepte 1) My manager was just saying the same thing. Need to run low and keep the ones here busy.
[j5hwr27] (score 3, diepte 1) When things slow down they shift focus from output to costs.
[j5ji9w9] (score 3, diepte 2) Yeah it’s so bad especially when they don’t have enough of the scrapers and u have to use ur fingernails
[j5jrj3p] (score 3, diepte 3) I wish I would scrap a dusty ass floor with my nails... You better be joking!!!
[j5jhfdu] (score 3, diepte 2) They are hiring and training new people for seasonal positions at some sites and need them to have work so they can get the practice in. Us vets are eating through all the work so they thinks it’s easy like that all year. When it starts to pick up, they will have a hard time because they are used to a slower workflow. At other sites, they simply don’t have enough work for everyone. Hence why they said they are letting go 18,000 workers this year.
[j5ialio] (score 3, diepte 2) And that's how they get you🤣 took a full week vto and said never again
[j5j2f4w] (score 3, diepte 3) I only worked two full shifts in November 2022. Then last week I took 37 hours of VTO. I just can’t help it lol
[j5jough] (score 3, diepte 4) Don’t need or want the money, huh?

Must be nice.
[j5k07kh] (score 3, diepte 5) Today I went in promising myself I’d get 40 hours this week. Clocked in at 7:30. After my AM asked me twice I finally caved at 9:30 and took VTO lol
[j5jod4r] (score 3, diepte 2) We don’t get surge pay. :(
[j5h9ubl] (score 3, diepte 1 OP) it is they cant force you to leave.
[j5hcf9p] (score 3, diepte 1 OP) Probably, our outbound volume was only a couple thousand today.
[j5hdmtw] (score 3, diepte 2) That would be why lol. I think AMs at my FC (at least where I am in outbound) haven’t been put in that kind of predicament because our AAs for the most part are always begging for VTO, and the ones that do take it are plentiful enough.
[j5hpz9e] (score 3, diepte 0) I’ll take all the VTO I can get I don’t want to change my schedule. Lol
[j5iabjl] (score 3, diepte 0) My pa's are chill they ask I say yes or no they leave lol
[j5jpne0] (score 2, diepte 4) idk if it’s the tape they use but even if u get some up it’s impossible to peel with even a scraper or finger nails
[j5jtfeg] (score 2, diepte 5) I do 5S quite frequently. The only tape I can’t get up with my finger nails is the shit that’s been practically forged into the concrete flooring by the OP’s. The rest of the stuff comes up pretty easily.
[j5gg03o] (score 2, diepte 0) Is it because OPs are pushing AMs to do this? If so I feel sorry for AMs. I mean some of them suck, but if an AM is groveling I can't imagine what their superiors are demanding.
[j5ilf54] (score 2, diepte 1) It's above the OPs it's the seniors taking direction from the regionals
[j5j2sfu] (score 2, diepte 5) Having a 3 day weekend is nice from time to time. When VTO was sent out last Thursday for Friday I was all over it!
[j5josee] (score 2, diepte 2) Chinese New Year. China shuts down for damned near 3 weeks. The vast majority of our product comes from China.
[j5iv3n4] (score 2, diepte 2) > I’m not like making fun of them or anything gotta do what you gotta do, just never experienced it till now and wanted to know if it was common.

With post holidays yes. Average consumer is out of disposable income. Also the economy sucks, and the stock price blows. So corporate is looking to cut ASAP.

For FC/retail thats VTO/hiring freeze. For corporate and external divisions its layoffs. Only AWS really remains untouched.
[j5gwv3t] (score 2, diepte 0) Yep my AM always tells me it's to save the depts hours cuz apparently IB is capable of running out of hours according to him and he's gotta save as much time as he can by VTOing ppl
[j5idutk] (score 2, diepte 1) “You guys might want to be grabbing up that VET before that V turns into an M.” Literally called 50s that day. Now there’s rumors of 60s
[j5jlr2z] (score 2, diepte 2) If they do 60’s they won’t have anyone left to work…
[j5jtkh7] (score 2, diepte 4) Man. I’d love 10 hours of OT a week.
[j5kzar5] (score 2, diepte 6) The secret there is pick up on the days you would work if they call MET and then if they call it you are already scheduled 🤷🏼‍♀️
[j5he2ph] (score 2, diepte 3 OP) Yeah, most people who wanted vto today took it the night before. So they already vtod like everyone and needed to vto even more during that shift. Honestly by the time I left there had to only be like 8 people there not including the management n stuff.
[j5hqoej] (score 2, diepte 0) My manager got me yesterday. He asked, I instantly caved, and he was the one who got excited. 🤣
[j5jpnjn] (score 2, diepte 2) Real easy for me. I’d rather do nothing in the warehouse for $18.50 an hour than do nothing somewhere else for $0. Further, I’m not accumulating PTO or vacation time if I’m busy not getting paid.
[j5iq9tr] (score 2, diepte 1) Same
[j5j2pik] (score 2, diepte 1) They can’t. Full time is 40 hours. They only thing they can force is MTO and that defeats the purpose for them.
[j5iot0b] (score 2, diepte 0) TLDR:  Amazon needs you to VTO in order to remain profitable.

Amazons order fulfillment system is based on volume per head counts (which is completely illogical, but whatever, works for them i guess) So when the volume of items needed is less than the needed head count, and they dont have "other" tasks for individuals to do, they are forced to VTO in order to get that head count lower, in order to boost their support rate, which is a number that they use to determine if the shift was profitable or not.  Hence why AMs will beg for folks to VTO.
[j5ir83a] (score 2, diepte 0) I’m coming to your site so they can vto me lol
[j5mj3w6] (score 2, diepte 1) Second this. The shear horror, disgust, and angry looks on my coworkers faces when their told to labor share to another dept says it all.
[j5jcler] (score 2, diepte 0) Jan and Feb is VTO heaven
(112 reacties met lagere score weggelaten)

=== THREAD sosif2 ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-02-10  SCORE: 79  REACTIES: 189
TITEL: Just finished 2nd week ugh 😩, how long does it take for feet to get used to 10hr shifts?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hwaw0zw] (score 83, diepte 0) About a month take care of your body eat well hydrate take vitamins get enough sleep good shoes
[hwavhry] (score 75, diepte 0) Been here almost 10 years…my body and feet will never get used to it. Eventually, you’ll get to where the pain is manageable. Good luck.
[hwavysl] (score 40, diepte 2) The question is, what have I not done? Lol
[hwavslx] (score 36, diepte 1 OP) 10 years!!!  What have you been doing???
[hwaxg2q] (score 25, diepte 0) Man, week 4 here and I took pto the last 4.5 hours of my shift today so I could get an early start at recouping.  They call us "industrial athletes " but as someone who was a pretty competitive college athlete, my body had waaaay more time to recoup.  My saving grace has been my insoles, if you don't already have some...get them, you'll tell an immediate difference. I use the dr. Scholls work inserts and now my feet are the least of my worries.
[hwb23h9] (score 21, diepte 4) So I started as a packer in AFE and that’s what I’ll always be, regardless of all the things I know.
[hwba2dn] (score 17, diepte 2) Oh gosh no coffee red bull and vending machine meals duh 🙄
[hwayxbl] (score 12, diepte 0) 6 weeks, honestly. A year and a half later they still hurt but nothing like that pain I remember from my first months. your body will adapt. Good insoles are also what made the difference for me. Epsom salt soaks and massage (pop your shoes off on breaks and quick massage then too!) when you get home. Ice them, wrap them in a heating pad, whatever feels good. I promise it gets better!!!
[hwavk3y] (score 11, diepte 0) first month is always rough
[hwbucof] (score 10, diepte 4) I’m in a traditional building that’s one of the oldest in the network. With that being said, slam has to be the easiest. My favorite is problem solve.
[hwbw663] (score 10, diepte 6) Slam is where you add dunnage and tape the boxes with an automatic taper. It’s probably different in other buildings tho. I believe now a packer will dunnage, tape, and slam out(print the shipping label) their own packages maybe? Like I said, I’m in an old building with old equipment. It didn’t take me long to get to problem solve. I got there by being willing to learn anything and everything. I told my pa and manager that’s what I wanted to do and eventually I got to learn how to do it. My favorite department for problem solve though has to be customer returns. I get a feeling of major gratification of making sure everything gets processed right so people can get their money back.
[hwdkbou] (score 10, diepte 2) When I first started that was my goal. I done everything I was supposed to do. I was very much involved. After about 3 years I realized it’s not worth it. Amazon is very demanding of it’s leaders. I value my home life. I value not having the added stress that comes with being a tier 3 and above. About 3 months ago I interviewed for 3 different tier 3 roles and was inclined for all 3 but with no offer. Then I was offered a PA role but declined it. I just couldn’t bring myself to accept it. It’s really not worth it. PAs make $2 more than me and have tons of things to do. I don’t want that kind of pressure. I want to take vto and personal leaves and vacation when I want and as a tier 3, you can’t do that. I’ve held several seasonal roles and I’m good with that. My dreams of moving up has faded. I just wanna do my job then bounce at the end of the day. If someone wants to move up, I encourage it. I always love seeing tier 1s move up and get that vest. I especially love seeing someone move up that I was an ambassador to. It’s a feeling that I can’t describe.
[hway7az] (score 10, diepte 0) like to say maybe another week but if your a potato maybe 2 more weeks. i used to use a tennis ball for self massaging my feet, even if I didn't feel pain but for sure sore. if you still feel pain or soreness maybe the sneakers aren't working for you. try something that is a bit more elevated or try wide size. hiking shoes work for me, not too tight and the soles are firm. used to wear running sneakers, never gave me problems at the previous job but was suffering when I started with Amazon.
[hwbd5gg] (score 8, diepte 2) I will change departments when I start getting bored. There’s so many things to do in an fc. I’m just now running out of new things. Also, friendships help a lot. So long as I have someone to chitchat with, I’m good.
[hwbm1nj] (score 8, diepte 0) Composite toe instead of steel toe, compression socks, actually measure your feet and get nice insoles instead of a random dr.scholls from cvs, vitamins with magnesium supposedly help with muscles cramps and recovery, foot rollers or balls, soak with epson salt, learn the right stretches; muscles in your shins + calves affect foot muscles, night splints to hold your feet at a 90 degree angle while they rest, lose weight.

Tons of options, I just started going down the list and checking everything I could. No foot pain after week 2.
[hwb0kwr] (score 7, diepte 3 OP) Ok, so what position do you like best?
[hwddtqs] (score 7, diepte 1) A DECADE? Jesus I don't think I have it in me to last that long
[hwdudn9] (score 7, diepte 1) Yes for me it took about a month. Im at Amazon fresh associate so i was picking groceries like the wind Lmaoo. I use to always soak my feet with epsom salt 🤷🏻‍♀️
[hwbl18x] (score 7, diepte 0) Tip - On your rest days don’t completely rest - you should still walk a bit and get blood circulating through your lower body.
[hwe1fh7] (score 6, diepte 4) Every building is different and everyone’s experiences are different. I never said I was happy to be there. Amazon gives me excellent benefits and there’s no other job that will allow me to come and go as I see fit. In all my time with amazon, I’ve never been written up. I have had 1 coaching for rate and that was something that was beyond my control. You make this job what you want it to be. I’m not happy about all the rules they have in place and I’m very vocal about my disdain for the place. Most days I’d rather stab myself with a fork than pull into that parking lot but I still do it because I need and like those benefits. I’ve thought about leaving more times than I can count but I know what it’s like to actually work for a company that doesn’t value their employees and the shit pay that comes with it. I know plenty of people that has been with amazon for a lot longer than I have that have never had the desire to be more than a low level warehouse worker. Working at amazon doesn’t make me cruel or thoughtless. It makes me a human that is constantly finding the positives outweighs the negatives. When shit is getting to be to much for me, I’m taking a personal leave to reset myself. I have a family that depends on amazon. I’m grateful for the opportunities that they have given me. I was a single mom with a 5 year gap in my work history when I got my job there.  I’ll shit on amazon just like the next person but at the end of the day, it pays my bills, gives me ample opportunity to not be there, and allows me to give my family quality healthcare. No place of employment is perfect. You deal with shit everywhere you go unless you are self employed. It all boils down to what works for you and what doesn’t.
[hwawbiw] (score 6, diepte 0) It took me a month , soaking your feet and body in epsom salt will help a lot it helps with score muscles and score body hope this helps
[hwb0lcs] (score 6, diepte 0) Takes about a month to get institutionalized and realize this is your new life
[hwb7qem] (score 6, diepte 0) It took me about 4-5 weeks to fully adjust to it. Just continue to take good care of your feet. Stretch them out, roll them out, ice them, soak them really whatever they need
[hwb2iyy] (score 5, diepte 2) They are just too heavy for me.  I wear some puma tennis shoes that are super lightweight.  I'm hoping I can get by with wearing them.
[hwb484b] (score 5, diepte 3 OP) Actually they’re composite so very light lol
[hwbcoyo] (score 5, diepte 0) That's the neat part they don't!
[hwdxtli] (score 4, diepte 3) This place is depressing as hell. The constant monitoring of productivity is so inhumane. Why anyone wants to perpetuate this system is beyond me. You have to be a little cruel or thoughtless to be happy working in this type of environment.
[hwec25j] (score 4, diepte 6) If I ever decided to move up I would try to make a change to the environment. If you are good to your associates, your associates are good to you. My building isn’t micromanaged. I work in a laid back fc. If I’m doing my job and hitting rate, no one says anything to me. I’ve noticed in all my years there, new AMs are the worst when it comes to staying on top of performance. It’s like they have to prove themselves or something. This place is far from perfect and more than likely I’ll never move up in a position that I’m over associates and if I did, I would offer help to someone struggling instead of just giving shitty feedback and moving on to the next person to give more shitty feedback. We are the ones that make amazon. If most of the leaders would understand this, it would be a much better place to work.
[hwemobi] (score 4, diepte 4) That sounds nice and all but it’s not for me. I just want to do my job and go home.
[hwbc8cq] (score 4, diepte 0) It takes a bit. A few months and you’re used to it. And I’m a Flats Waterspider in Outbound so I’m walking all day (nearly 10 miles a shift). Peak is terrible though. Don’t think your legs can get used to walking 55 hours a week.
[hwbdoul] (score 4, diepte 0) Change of socks and foot powder works for me. Yea I get strange looks on break, but DGAF!
[hwburfr] (score 3, diepte 5) What is slam? And how did u get to problem solver? I can start from T1 right?
[hwfhdrc] (score 3, diepte 7) I’m in customer returns, and I have to say it sucks when the rest of your crew rather smoke their pen or constantly FaceTime throughout the entire shift! But managers only come around to tell me to put my mask on correctly lol
[hwbbwgu] (score 3, diepte 1) And I thought my 3 years there were rough... How do you manage the boredom, I'm honestly getting burnt out
[hwderxi] (score 3, diepte 2) I have faith in you if it’s something you want to do. My goal is 15 then I’ll retire from amazon…maybe. Lol
[hwej6hx] (score 3, diepte 2) Nah, I’m good with what I do. Don’t want all the stress.
[hwdz1nc] (score 3, diepte 1) Get enough sleep.  By that do you mean sleeping an entire day off away? After 3 yrs that is only way I have found to get (slightly) enough sleep. Idk about day shift but working 630pm to 5am doesn't make it easy to get 8 hrs a day those that I work...
[hwb1w1i] (score 3, diepte 1 OP) I’ve got Timberland Pro work boots and the soles in them are actually thicker than the dr. Scholls I bought from the drugstore
[hweqb6p] (score 3, diepte 3) People think that only the weight of the shoe is what’s going to tire you out but in reality it’s also the padding on the footwell, tennis shoes no matter how lightweight are going to kill your feet.. some hiking boots is a better option, they are designed to be walked on for long periods of time or distances and are in my opinion the best for an Amazon warehouse.. they are light weight but also have proper padding and insoles. I run though 10 hour shifts like nothing.. and everyone just wonders how I do it with my “heavy” boots 😂 what they don’t know is that they aren’t regular old boots but hiking boots. Every time I see someone limping or walking all tired I look at their shoes and see the problem.. they all wear tennis shoes, Jordan’s, shoes like that lol some horrible shoes that I don’t know the name off that have a funny looking sole but that I’m pretty sure is useless.. but only looks functional. Idk this is just what I have noticed and experience.
[hwcbull] (score 3, diepte 1) Love this comment simply because I don't think people realize how “athletic” this work can be. I'm in a DSP now and we are straight up running a triathlon every night.
[hwcdj08] (score 3, diepte 3) Yes they get it. I worked at UPS before when I was fresh out of college and waiting to find a job in my career path. So I knew Amazon would be physically hard when I came back to the warehouse industry after covid happened and lost my job. UPS is more of a sprint though. You're basically power lifting for 6 hours straight. I met my bf there, so he gets it.  I lost a shit ton of weight at UPS  and came home with bruises all over everyday though, so my family believed me. I've been an athlete my entire life and I've never been in better shape then when I worked at UPS. 

As far as how I do it... Eh I'm older now and not in as good of shape, but I was an athlete most of my life and open water swim so I'm used to endurance stuff. Basically I just treat it like I would any other sport. I try to keep up with drinking enough water, I try to make sure I’m eating well etc. I also am older now and need to ice my body every once in a while. I either cold water swim or just ice my feet. And I take a shit ton of ibuprofen😅
[hwazpbs] (score 3, diepte 0) Get a good quality pair of insoles. Ones made for work boots since normal cheaper insoles will wear out extremely quickly.

I'd  recommend Georgia Boot AMP LT insoles. They make a world of a difference for me.
[hwb7on2] (score 3, diepte 0) Been at this three months now and my feet still hurt but after awhile they don't hurt as bad.
[hwb9t8p] (score 3, diepte 1 OP) I’m in Canada, never heard of zappos lol
[hwba8i8] (score 3, diepte 2) Shhhh lol Amazon owns a shoe company and we get free shoes twice a year.
[hwb9kkh] (score 3, diepte 0) I'd suggest getting cheap $25ish dollar sketchers with memory foam from ross and some insoles. They helped a ton! Get cheap because... If you have foot odor you will be getting new shoes often. Once every few months often if you can manage. Them being super light weight helps too.
[hwe1cr3] (score 3, diepte 1) Strange looks at break time..if ur taking off ur shoes and socks in the break area I would imagine those looks are of revulsion..no offense but I would say it's a safe bet ur dogs ( in other words ur feet.)
 don't smell like anything in the realm of pleasant
[hwbh7gi] (score 3, diepte 0) it took me about a month, first two weeks I would come home and cry lol but hang in there and it’ll get better! good luck :)
[hwblb50] (score 3, diepte 0) 4 weeks or so. Insoles are great! Also, after work, soak ur feet in ice water.Just for a few seconds at a time until u can keep them in for a min. I’d do this off and on for 30 min and it really helps ur feet heal and recover after so much use. It’s REALLY miserable and I feel so sorry for u. I remember
[hwbomt6] (score 3, diepte 0) I'm a 290 pound guy and the first 2 weeks was HELL. I wanted to quit so bad because it hurted just standing. Idk but some miracle happened and at the 3rd week my feet magically stop hurting. Its just little pain now... I'm not sure why, no new shoes or anything.
[hwboqmi] (score 3, diepte 0) Get some good shoes and break them in on your days off. I've been there since December and it does get easier, for me at least. Maybe two weeks before I was able to go the whole day without limping lol. But if it's a stowing day for me, it's always a little more rough
[hwd14uy] (score 3, diepte 0) Hey! Are you eating well and hydrating? For the first 2 weeks my feet and whole body hurt. I was even coming home and having extremely painful muscle spasms in my legs and even my feet. Highly recommend Tylenol 8 hr extended release. It doesn’t get rid of the pain but it takes that sharp edge off. Eat extremely well and fuel your body. That helps a lot with muscle and any other soreness. And plain waster isn’t the best it’s good for you but when you work at Amazon you need propel Gatorade Powerade stuff like that. But congrats on making it through your first 2 weeks. You’re doing great.
[hwdecxi] (score 3, diepte 0) You should be good in a month or two. I work 12 hr shifts so when they pull me in for 10 hrs it's a breeze
[hwbtzfd] (score 2, diepte 3) Oh wow 10 years!!!! What your favorite position? Or what do u think is the easiest?
[hwbxt03] (score 2, diepte 8) In my building, after the packer packed the order it was placed on the conveyor to be taken to slam. There someone would put the bubbles in the box then someone would tape the box. Then it would go down to be weighed and get the shipping label. We are no longer an outbound building. It’s been a minute since I’ve been in AFE. It’s always been so wild to me how it’s not standard across the buildings. I should be able to go to any fc and know how everything is done. I guess the basics are the same but the set up is a bit different.
[hwbyonf] (score 2, diepte 10) We had that too but it was it’s own department.
[hwbzmlx] (score 2, diepte 12) I hated pack singles 😂. AFE was where I started tho so I guess I’m biased. I loved going to a full wall and cleaning it out. It was soothing to me as weird as it sounds. If I had a good rebinner it was even better.
[hwf4nlg] (score 2, diepte 10) It’s all depending on what you want from the job. I don’t want to move up. I just want to do my job and go home.
[hwfi3bf] (score 2, diepte 8) In case you haven’t noticed, there’s a bunch of slackers that work at amazon lol.
[hwff2hz] (score 2, diepte 2) I don’t recommend anyone to stay more than 2-5 years at a job unless your plan is to move up to management. If you stay at tier 1, what ends up happening is you make less or equal to the new people with little to no experience. That’s not an Amazon thing but just how things work now.
[hwjdgs6] (score 2, diepte 3) Yeah I don't stay at a job longer than 2 years or so, I bounce around if I don't plan on moving up
[hwdhizh] (score 2, diepte 1) Have you considered moving into management?
[hwdmw7d] (score 2, diepte 4) Thanks. My senior leaders are always encouraging me to apply. Maybe one day I will.
[hwe02ph] (score 2, diepte 4) I concur ..so much so that ur comment deserves an award.
[hweinsd] (score 2, diepte 1) You should be making damn near 100k or some type of corporate job now at amazon
[hwelk6j] (score 2, diepte 3) Loading fat ass boxes and hearing average workers complaining is annoying. Id be sitting in some corporate office rn making 80+k if i were u
[hwf70nl] (score 2, diepte 2) I’m totally taking this as a compliment. Thank you.
[hwf7i0z] (score 2, diepte 4) Thank you very much.
[hwbwgd2] (score 2, diepte 3) So… monster and coffee. 

But I have coffee and water, coffee on my way in and water through out the day. But then I start to decline during the day pull out a random ass energy drink. Then drink water after I finish the energy drink to replenish my hydration more.
[hwby5kc] (score 2, diepte 4) Don't forget your electrolytes potato chips cheese-its ...the tears of your beaten down PA
[hwbylf6] (score 2, diepte 5) 💀 

I like my PA’s but hate one of my OP’s managers. 

I buy protein from the break room cause I keep forgetting to buy some from the store, I get like cliff bars and nature valley bars, but sometimes I do get potato chips. These get me through the day sometimes if I’m really not beaten down cause after break, time either flies or it goes like 5% slower.
[hwf2n24] (score 2, diepte 4) I specifically make sure I have a shoe that works for my feet, im too old for them suckers to be barking all night.  I'll definitely look into the hiking boots though, you make a good point about "made for Long distance".  Since I stay on that little padded area I just want clouds under my feet.  I see folks that don't have proper shoes and I want to cry for them..
(114 reacties met lagere score weggelaten)

=== THREAD 1juty75 ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-04-09  SCORE: 399  REACTIES: 179
TITEL: R.I.P to everyone's Feet
POST (source_id=post):
Extra cushion socks, gel insoles, don't matter. After working here, these shit stompers are cooked.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mm52gdi] (score 258, diepte 0) When I first started back in 2020, safety shoes weren't mandatory. All I had to do was buy a pair of Dr. Scholls insoles and I was good. Didn't start getting callusses until the safety shoes were actually made mandatory.
[mm533tw] (score 82, diepte 1) Facts!! I loved being able to wear my own shoes back then.
[mm5ccha] (score 79, diepte 2) Definitely miss those days. I also miss being able to clock in/out through the app.
[mm56rtl] (score 73, diepte 0) Bruh the callus on my feet
 I never had them lol before and I am grating my feet like Parmesan monthly. Like  please yall ruining the foot pic selling potential. 😭 now i am going to be a case study  on the effects of prolonged wear and standing in composite toe.
[mm597w2] (score 35, diepte 2) I work on the ship dock and one day, I was water spidering and I had to get a go cart from a trailer. Well, the wheels got caught on a screw that had been hammered flat on the trailer floor(I have no idea how that trailer passed inspection because there were like 40 screws like that) and the go cart tipped over and landed on my foot. Those go carts are about 150 pounds and if I wasn't wearing safety shoes, I'd have a broken foot
[mm576xm] (score 35, diepte 0) Arch-only inserts are often overlooked.  Often the arch is the issue.  Insoles tend to lift the whole foot which doesn't change much for your arch.  It can be your foot flattening that causes heel pain, as the tendon connects there and pulls.

I use these. 4 sizes.  I find I use the small and medium most often.  It all depends on your arch and how much arch is in your shoe.  They don't have to be exact and you may find your left and right prefer different sizes.  I just slip them in and they stay in place.

Before I found these I would make arch inserts by hand, using paper towels and clear shipping tape.  Folding it into a flat rectangle.  They'd last over a year.  I made them oversized, as they pack down over time, and when you first put them in they feel too large but you also instantly feel the relief, if that is one of your issues.  

https://preview.redd.it/3uy76d1yvpte1.png?width=1147&format=png&auto=webp&s=c2d48062e90798243f89f1e17cd0fce102f2cf2f
[mm5jo0t] (score 31, diepte 0) The safety shoe scam was just an insane tax write off
[mm52yok] (score 28, diepte 0) I’m thankful my feet are now bricks and no longer hurt. xD
[mm5ate1] (score 27, diepte 0) Thanks to Amazon I learned what a bunion is and how painful it is 🥲
[mm589ad] (score 26, diepte 1) Yeah i do only pick/pack right now too so im destroying my feet for no reason lmao, I worked at ups lifting 150lb packages in normal running shoes but god forbid I lift 25lbs(max) w no safety shoes!
[mm5g4ll] (score 23, diepte 3) True.  They suck except when they save your toes.
[mm5e6zs] (score 23, diepte 0) R.I.P to my legs. All the squats you have to do to lift those heavy items out the bottom bins.
[mm507dz] (score 22, diepte 0) Yup shit is ass
[mm5wk6u] (score 21, diepte 4) Me too… missed punch all day every day
[mm5bixq] (score 19, diepte 1) Lol I'm so sorry but the foot pic selling comment and your screen name has been cracking up!
[mm5iq3b] (score 18, diepte 5) Poor English gets you a pass on a lot of things!
[mm57uh8] (score 18, diepte 0) And lower back, because the body isn’t meant to stand up for 9+ hours a day.
[mm6asz3] (score 17, diepte 0) It’s the safety shoes. 5 years of wearing cheap running shoes and my feet were perfect. Now my whole back and legs are messed up from the toe and foot pain and traveling nerve damage.
[mm5jbtc] (score 16, diepte 0) Check your insurance... I get free custom orthotics with my plan.  3D scanned from a podiatrist and all.  You can use them in any shoe.  They are 10x better than any solution you can buy at a store
[mm5kxfe] (score 15, diepte 6) Absolutely does. I’m gonna start parlez vousing when I get in trouble.
[mm5p4k5] (score 15, diepte 0) The best part of my work day is getting to my car and putting on my Crocs for the drive home. It's like I've been wearing cinderblocks all day.
[mm5fvt7] (score 14, diepte 3) doing this as we speak
[mm6drfc] (score 13, diepte 2) I’m sure they smell incredible.
[mm5cphk] (score 13, diepte 0) https://preview.redd.it/51052yce2qte1.png?width=3024&format=png&auto=webp&s=11d1c6c321716714c9b84e8c03b6fc3f5997a38b

Uh-oh. Came straight from a Dr Appointment. Does anybody’s work shoes hurt the tops of your feet?
[mm5ezir] (score 13, diepte 0) RIP we all have calloused and hard feet like those old people
[mm5hw9v] (score 12, diepte 4) Nope. Least it seems not at some facilities. I know people that were totally abusing it though lol. One guy was running late clicked in a mile away. One even had the balls to click in at homer  ur. But his English was poor, so it was ok.
[mm5g1zy] (score 12, diepte 1) All it took was some missing toes. Man oh man. The good old days. Would give up 2 toes to go back.
[mm7lnuv] (score 12, diepte 1) Lol the messed up part is whenever I drop something on my foot at work it always lands above the safety toe 🙃 😅 😂
[mm6rfum] (score 12, diepte 1) Yabba dabba do
[mm5i7uj] (score 10, diepte 0) Yeah safety shoes are definitely foot killers. I’m to the point I’d rather take my chances with a crushed foot anymore. My days off are spent running around in crocs or slides for everything now. I hate Amazon.
[mm7ho5p] (score 9, diepte 1) God I miss being able to wear my air maxes I miss Covid Amazon so much
[mm587xe] (score 9, diepte 1) The blue is one of my old handmade ones and the beat up one is a heavily used Pedag.

https://preview.redd.it/igpqkrhqxpte1.jpeg?width=600&format=pjpg&auto=webp&s=39c2c4396da966d442e40efd725f6f85df0d486f
[mm5fz40] (score 8, diepte 3) clock in/out through app is not available anymore?
[mm5bloo] (score 8, diepte 0) https://preview.redd.it/dvti9ed81qte1.jpeg?width=3024&format=pjpg&auto=webp&s=a8437d599528eed1eb4dbce4ca7e1c3af40699de

pain and suffering
[mm6cwrn] (score 8, diepte 1) And varicose veins from the shoes too. But the nerve damage. I hate it
[mm84kza] (score 7, diepte 1) I'm a safety manager and I miss when safety shoes weren't mandatory.  Hate them too.
[mm5i41x] (score 7, diepte 0) Speak for yourself, my shoes don't make my feet hurt. It's the hours that make my feet hurt
[mm5wynm] (score 7, diepte 0) I like to do one size up + no-tie shoelaces 😽👌🏻
[mm5xxla] (score 7, diepte 0) I have a pair of the Airwalk SDs, and they're the second most comfortable shoes I own. First most comfortable shoes I own are Crocs. I wear the Airwalks everywhere. No insoles needed. I did get a half size larger than my regular size, and I also got the wide version. Best bet is to trace your feet on a piece of paper, and measure the widest and longest points to get a good fitting shoe. I bet half the commenters here have shoes too small for their feet.
[mm52def] (score 6, diepte 0) the waterspiders take care of everyone's feet
[mm54tqx] (score 6, diepte 0) I took like 8 dual Advil/Tylenol pills during a 10-hour shift and they made no difference.
[mm5fvto] (score 6, diepte 0) Fr dude, i get home and immediately start doing some ankle rolls and stretch my legs and feet. Within the 3 years ive been here, my feet got abs
[mm5kwzm] (score 6, diepte 0) Fr omg my feet hurt so bad after I can barley walk with these safety shoes :(
[mm5tfxv] (score 6, diepte 0) Yeap I have a pinched nerve near my ankle.  Didn't matter what insoles, shoes, or specialized podiatrist orthopedics I used.  This isn't natural, even horses don't stand this long.
[mm6lp4h] (score 6, diepte 0) You need compression socks.
[mm71v9r] (score 5, diepte 1) Bet you still could
[mm5gccm] (score 5, diepte 1) Only for the first 10 minutes. And then I dont notice. I do have inserts, but when Im not at work I rock my smiley slippers...unless Im mowing the grass 😝

https://preview.redd.it/lhcqgypn6qte1.png?width=1080&format=png&auto=webp&s=e7f3968176a4cc981f228b35452014a8eb5dae35

Theyre scuzzy and threadbare but I love them so much 🤷🏿‍♀️
[mm90qxb] (score 5, diepte 1) I got free insoles from my orthopedic and it was a lifesaver. The free insoles we get through Zappos gave me plantar fasciitis. The pain was horrible! Since I started using the ones from my orthopedic the pain finally went away.
[mm609oa] (score 5, diepte 0) Yeah I got planters foot permanently they'll eventually have to amputate be thankful of you ain't got it also
[mm6rprs] (score 5, diepte 0) I got flat feet and it's destroying my ankles 😭
[mm6uf15] (score 5, diepte 0) I know all to well. My feet have purple busted varicose veins. I don't even have the complete full feeling of my feet anymore since Amazon.  I'm gonna need compensation for pain and suffering now. Amazon pay up!
[mm6uavm] (score 4, diepte 2) Sketchers are okay too
[mm858ou] (score 4, diepte 1) So there is a way to still wear your normal shoes.  My site had a dramatic increase of stress fractures in feet (still have a few each month).  

There is a proactive shield that goes on top of your shoes that covers from front of ankles to end of toes. You need a doctor’s note and approval.
[mm6tq1z] (score 4, diepte 1) Yes I got them too but after 2 months I think I killed them 🤣🤣🤣
[mm5wt0q] (score 3, diepte 4) Yeah, I got lucky. I had all the wheels unlocked and pulled it out, and it instantly got caught. The moment I felt it tipping i carefully let go and quickly stepped back and it landed directly on the composite toe and saved my toes. I had to lift the go cart to free my foot and I immediately escalated to my am. The om came from pack side to check if I was okay and luckily I was, and I definitely voiced my concern for the safety of that trailer, which was then yellow tagged and taken off the door.
[mm6g09x] (score 3, diepte 1) Gotta get the right ones. The Reebok Work composite stink for me (constriction made my toes rub together- ouch), but the New Balance I got have been much better.
[mm83za8] (score 3, diepte 2) Nope sorry you are wrong. It could have been building dependent but I’ve been in 3 sites in 3 different states and non of them required safety shoes until after Covid.

About a month before hey what is this new illness there was a new offer of hey get these shoes, wear them in and the dept with the most (in a group pic) gets a pizza party.   We did the pic and then everyone changed back to their normal shoes. My dept won but we never got the pizza.  2 months later was the era of unlimited UPT.  Safety shoes were suggested but they didn’t care until around late 2020 early 2021.
[mm8onps] (score 3, diepte 1) My arches were fine wearing lightweight Kuru's.


These safety shoes have fucked my feet. They aren't desired for the type or durstion of activity we're doing. No regard for flexibility.
[mm8rdh5] (score 3, diepte 1) I just got first callus and I thought I was the exception to the rule because I get pedicures once a month but no 😭😭😭. My feet hurt so bad. I’m too young to feel this way. Amazon got me out here and walking like an 87 year old woman. If y’all have any tips at all please let me know
[mm54a4c] (score 3, diepte 0) Amen brother, no matter what shoes I've bought, insoles and extra relief for strain. My toe pain will always make me suffer along with spending the rest of day walking with cinderblock legs 😫
[mm8nyyl] (score 3, diepte 1) Nah some dudes will pay extra for those callused feet
[mm79zze] (score 3, diepte 1) Thanks. I didn’t even know this was an option or a thing. I have somewhat no arch and my feet hurt a lot but when I wear Burks they seem to feel much better.
[mm57ynh] (score 3, diepte 0) I know how bad it sucks. Do you soak your feet? Massage/stretch your feet or have a foot massage roller? I have a massage mat as well that I'll put under my legs and feet while I relax or fall asleep that way. I also apply heat but that is a case by case basis and probably would depend on your situation.
[mm5iyl5] (score 3, diepte 1) I think that’s what I’m working on now too.  And I got extra wide shoes that actually fit pretty good this last round. No idea why the pain that area all if a sudden. Let me go find the link, couple gals at work are wearing g these over regular shoes. But I was told dayshift it’s a no go, but nights it’s ok…..I bought a pair, have t tried them yet. I can’t wear my regular tennis shoes lately because Amazon safety shoes have jacked up my feet so bad.
[mm64kli] (score 3, diepte 1) I almost thought that was Sharon Osbourne
[mm5htde] (score 3, diepte 0) I know it's for liability but man, I'm just on Count. Please let me stop using safety shoes
[mm665lf] (score 3, diepte 1) Oh wow that's nuts
[mm5msn0] (score 3, diepte 0) Get a brannock device to find your actual shoe size.  Why ?  https://brannock.com/pages/instructions-fitting-tips

Find out your arch type, then get the correct insole.  Use the superfeet tool.   https://www.superfeet.com/pages/insole-finder

Your feet may get tired but these steps should help a lot.  It made things better for me in many ways.
[mm5rl0m] (score 3, diepte 0) You can wear your regular shoes and just by your own composite toe covers.

https://a.co/d/9SMPn1l
[mm5y1n7] (score 3, diepte 0) Reebok makes some fairly lightweight safety shoes.  I suggest you try those.  I would rather wear those than my outside shoes.
[mm69dc1] (score 3, diepte 0) Not gonna lie, I did drop an empty tote on my toe today with my regular shoes on amd it did hurt for like 2 minutes. They are very soft toed. What trips me out is safety and security come walking through for whatever and nobody noticed. I hope i can make it the last 2.5 hours. LoL
[mm6bo7c] (score 3, diepte 0) Elevated calf raises every day. You’re welcome.
[mm6zraj] (score 3, diepte 1) Get some kind of arch support else you will ruin your knees !!!  I have the same flat feet as my mother, she had to get two new knees, you don't want that. Arch support !!!
[mmc6i3p] (score 2, diepte 5) They get caught u can still do it but only on the Amazon wifi B4 you leave the building atleast at our site u still can
[mmc69t9] (score 2, diepte 3) You still can u just have to be in the building I do it at the front lobby all the time or I just fix a missed punch lol
[mm9cy49] (score 2, diepte 2) Stow is a breeze compared to pick. Way less movement and when ws are lazy you sit with out of work andons for 30 mins at a time sometimes. Peak is great bc they're so fucking busy the spiders get slow
[mmat970] (score 2, diepte 2) LITERALLYYYYY
[mm7t2dn] (score 2, diepte 1) Those shoes started my feet aches too
[mmbbv51] (score 2, diepte 2) I purchased a few of those toe covers I even wore them with my Crocs one day 🤣
[mmbrq2z] (score 2, diepte 2) I've worn Keen shoes (they have a line for women) for years, even during my pregnancy and long days my feet never hurt, I really recommend them
(103 reacties met lagere score weggelaten)

