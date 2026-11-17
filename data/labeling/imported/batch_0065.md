# Label-batch batch_0065

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
Schrijf het resultaat naar `batch_0065.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1giv7iw, 15j6w7o, 1tly0gp).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1giv7iw ===
SUBREDDIT: r/Costco
DATUM: 2024-11-03  SCORE: 651  REACTIES: 178
TITEL: 11374 got a new price checker 🤦‍♀️ mounted six feet off the ground
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lv8d3fa] (score 741, diepte 0) Putting short people in their place
[lv932s3] (score 266, diepte 0) https://preview.redd.it/lee3rr8ggryd1.jpeg?width=968&format=pjpg&auto=webp&s=541c65d869950359c7e3ffffea4968b42aef5047

Quit being short
[lv8m6es] (score 236, diepte 1) That's the price we pay for always being comfortable on Airplanes.
[lv8enks] (score 149, diepte 0) Is that to protect it from pallets as they move them around the warehouse? Give the person in charge at the front the feedback that they at least need to tilt it so the screen can be read.
[lv8wuia] (score 104, diepte 1) No, tall person perk only.

Soon we will convert Costco to only allowing tall people.
[lv8utrc] (score 85, diepte 0) Basically, all short folks in the future. Haha

https://preview.redd.it/lxspvmjn8ryd1.png?width=1920&format=pjpg&auto=webp&s=da8b067d41887e2343f550e168f447bff472b9dd
[lv8h8uq] (score 70, diepte 1) *They got little cars that go beep, beep, beep
They got little voices goin’ peep, peep, peep*
[lv9jd9r] (score 60, diepte 1) Don't do my penis next
[lv8jcmx] (score 54, diepte 1 OP) maybe you do, but it's mounted   
too high for you to have noticed.
[lv8ozeh] (score 51, diepte 2) You should see what Costco looks like at 7am. There’s pallets on almost every isle. I work in the bakery and sometimes can’t even get our product to the tables because there’s too many pallets in the way.
[lv90e05] (score 43, diepte 0) Do costcos need price checking machines? I don't think I've ever seen a price tag missing from a costco shelf.
[lv94qr1] (score 41, diepte 2) > Soon we will convert Costco to only allowing ~~tall~~ **Costco-sized** people
[lv8pfbw] (score 40, diepte 0) It only works on high prices.
[lv9jpzg] (score 39, diepte 1) What about when you snag something awesome from someones else's cart but you don't know the price
[lv9ouky] (score 35, diepte 2) And fitting into clothes and cars more easily

And generally living longer 

Being tall actually kinda sucks
[lv8g704] (score 32, diepte 0) Lmao what in the fuck, I'm 6'1" and would bust out laughing if I saw that, who the hell installed it? A resurrected andre the giant?
[lv961ih] (score 25, diepte 2) Unexpected Randy Newman
[lv8uey8] (score 23, diepte 4) You’re wrong everywhere. Every single aisle sees pallet and forklift traffic. Look what the drug aisle product is built on top of. Pallets. There isn’t really a low-traffic forklift area. The place is designed to get massive amounts of product replaced and refilled every day within just a few hours of the morning.
[lv8nwcw] (score 23, diepte 0) Have to be this tall to ride the price checker.
[lv8sxac] (score 19, diepte 2) Why do you type like you’re writing a poem lmao
[lv98k6a] (score 18, diepte 1) Dad.   Stop.
[lv8pogn] (score 17, diepte 3) > isle

aisle
[lvadqkb] (score 17, diepte 3) Username checks out.
[lv9iro9] (score 15, diepte 1) They got grubby little fingers


and dirty little minds 


They're gonna get ya every time
[lv8ups0] (score 15, diepte 0) you took this at an intentionally deceptive angle or you're 3 ft tall. Why is your camera at that man's butt level?
[lv9qoia] (score 14, diepte 3) I’m 5’10. 

Am I tall or short?! 

Around 5’7” folks I feel like an NBA all star… around my 6’ friends I just get pats on the head when I do something good.

HOW AM I SUPPOSED TO FEEL?!?!
[lv9r1eg] (score 14, diepte 4) Depends on your sex, for a male that’s pretty average in the US. For a female, that’s pretty damn tall
[lv8v3a3] (score 14, diepte 4) I know I knew that but I feel like I’ve only typed out the word aisle like 2 times in my life. Thank you
[lv8ma19] (score 14, diepte 0) What's the scanning range?  If it picks up 3-4ft away, there's no problem.
[lv9n0k8] (score 14, diepte 2) Please provide 1 standardized object in the same plane as the phallus (banana for scale may result in inaccurate measurements)
[lv8zo2v] (score 13, diepte 4) https://preview.redd.it/rm7hxoj6dryd1.jpeg?width=3024&format=pjpg&auto=webp&s=93476a57afa8a8f3d47809d9ef53efd53e8b244c

This is what the freezer aisles look like
[lv95y78] (score 11, diepte 1) If tall people can reach for the tall stuff on a shelf , short people can get the short shelf items
[lv9c1wu] (score 11, diepte 2) https://preview.redd.it/e48vcp1toryd1.jpeg?width=186&format=pjpg&auto=webp&s=281010960d6bbf2221796c9e08dfa5f0adb0c767
[lv8ivmw] (score 11, diepte 0) Our store doesn’t even have one.
[lv9fw4z] (score 11, diepte 1) What app did you use to do that? I’m assuming it allows you to use the known dimensions of the outlet box to calculate other dimension? V cool.
[lv9xoht] (score 10, diepte 0) Price checks be like

https://preview.redd.it/tcr35dyaasyd1.jpeg?width=1080&format=pjpg&auto=webp&s=852c56c15b51809c56c64c6e132004856507dfaf
[lv9mk0n] (score 9, diepte 2) There are many similar apps but I used imagemeter
[lva51qb] (score 9, diepte 1) when will they learn?
[lvb96b2] (score 8, diepte 6) >AM I TALL OR SHORT?!

Yes
[lv8ox7x] (score 8, diepte 1) Someone who didn’t read the SOW. I’ve done grocery store installs before and all the documentation takes into account ADA. This is not compliant.
[lv9jkas] (score 8, diepte 1) I showed that to my partner and seriously died laughing. 

Can't wait to hold up a box of Madras Lentils to that thing soon like it's the holy grail
[lv9xlmo] (score 8, diepte 2) Any penis, long or short or thick or thin, is a blessing
[lva8754] (score 8, diepte 1) In my line of business, this is what we call forced perspective
[lv9aofq] (score 8, diepte 0) Finally something for us tall people.
[lv96grt] (score 6, diepte 2) Despite my joke I agree. This was a mistake on the store’s part.
[lv98tgn] (score 6, diepte 5) Now 3, a 50% increase.   Congratulations!
[lv8y34t] (score 6, diepte 3) And how far does the wheelchair need to pull back so they can read the screen?
[lv9rdis] (score 5, diepte 2) Good why do smaller people need bulk items anyway. Isnt all they eat like lettuce or something?
[lv8g19a] (score 5, diepte 0) Everything in Costco is big…..
[lv8pixu] (score 5, diepte 1 OP) that would be hilarious...  
if it read prices off random items  
down in passing shopping carts.
[lv96uzq] (score 5, diepte 1) Most Costco stores do not have price checkers but there are some states and jurisdictions that do require them, so Costco will comply.  I’m not sure about  mounting it six feet in the air though…. Someone probably got tired of having to repair it non stop after getting rammed by shopping carts, etc.
[lv9xs1x] (score 5, diepte 2) You joke, but people do this
[lv9259s] (score 5, diepte 0) Don't look directly at the beam.  Seriously.
[lvaxbg8] (score 4, diepte 4) I’m tall lol. I wear a size 15 shoe.  Some days I hate it, if you’re tall too you can’t tell me you don’t feel the same trying to fit into vehicles that weren’t made for you
[lv96iff] (score 4, diepte 2) Teamwork makes the dream work.
[lv8t6r0] (score 4, diepte 1) those other places dont have 6-10 forklifts moving 100s of pallets by them every morning.  this one is in a high volume location, at waist height it would only last a few days before its pulverized.
[lv96hjm] (score 4, diepte 3) But the scanner also has to be within reach. I was just involved with opening a new facility and ADA required nothing be more than 48” high, looking up retail the requirements are no more than 36” high. This would be 3ft taller than allowable (unless they have another one at the required height).
[lv8z0sd] (score 4, diepte 0) One of the things I like about Costco is that all prices are clearly displayed.  Why is a price scanner needed?
[lvcp9xe] (score 4, diepte 3) [ADA reach range](https://www.ada-compliance.com/images/ada-2012/ADA-AB16.gif)

With this, all you have to do is hold the object up to the bottom scanner. So the test for compliance here would be to hold an object up at 48" above the floor and see if it scans. If you have to hold the barcode higher than that, it is indeed a violation.
[lv98skr] (score 4, diepte 0) That’s not 6’
[lvactbc] (score 3, diepte 5) Male.

#AM I TALL OR SHORT?!
[lvalc7f] (score 3, diepte 8) Ask her to teach you how to dunk.
[lvbqtw8] (score 3, diepte 5) I'm not even tall and I feel this, I'm 5'9 and taller in the torso than legs and I have trouble getting in to most cars without hitting my head or contorting my body in ridiculous ways.
[lvc0q89] (score 3, diepte 3) Needs more pixels
[lvaed9g] (score 3, diepte 6) Hahaha Costco would shame me for that percentage of increase
[lv8yot2] (score 3, diepte 1) Ours doesn't, either. I've always just read the sign above/below the product.
[lv9kcbe] (score 3, diepte 1) Yes, members come to us all the time for a price check
[lvcxavv] (score 3, diepte 4) But the bottom of the scanner is only 42” above the floor so this isn’t an issue. OP is just using perspective to make it look higher
[lv95ely] (score 3, diepte 0) Finally an appropriately sized scanner.
Now I just need appropriately sized toilet bowls, counter tops, sinks, door ways, sedans, and desk.
[lv9o37g] (score 3, diepte 1) This is in Queens. Honestly I’m more shocked to see the aisles fairly clear. This Costco is usually a war zone not matter time/day of the week.
[lvaagxs] (score 2, diepte 4) Man or women? If male you are above average which is 5’9” in the USA. If you are female you are tall because the average height in the USA is 5’4”.
[lvad0j2] (score 2, diepte 6) Above average, nice height. No woman is going to consider you short at all.
[lvad7lk] (score 2, diepte 7) My wife is 6’1” and pats me on the head and tells me when I have been good, so confused.
[lveg79a] (score 2, diepte 4) Above average, but not officially Tall.
[lvaclcj] (score 2, diepte 3) Works well for dating and a little bit for your career... but practically ya, it sucks.
[lvcwi07] (score 2, diepte 4) Always?
[lvecxul] (score 2, diepte 4) Children’s pants are right there though. But I get it, that’s the other end of the extreme. I guess I should have  said being average height is the most convenient option lol
[lv8nn6y] (score 2, diepte 1) Haha, you did not just go there! 😂 Savage!
[lv9ui04] (score 2, diepte 2) Happy Cake Day Maria_Chicago!!
[lv8t75a] (score 2, diepte 1) And frail and disabled people as well.
(108 reacties met lagere score weggelaten)

=== THREAD 15j6w7o ===
SUBREDDIT: r/AmazonFC
DATUM: 2023-08-05  SCORE: 99  REACTIES: 174
TITEL: Just got out early on my first day because my feet felt like exploding
POST (source_id=post):
Today was my first day working at amazon. I work 30-40 hours a week on 10 hour shifts(1 hour break in between). At a DS not an FC, hope it doesn't matter much since im just ranting. I started out fine, learning how everything works and all, but 4 hours in my feet started throbbing. I thought I could push through but 7 hours in I couldn't handle it anymore and asked for a break. It still hurt a lot after my break so I ended up going home early. I feel guilty and downtrodden because I had told myself I would work for 2 months of my summer vacation without calling in sick to save up money for college but I'm already off to a bad start. Is this normal or am I too physically weak?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[juy7kpp] (score 66, diepte 0) Takes time to get used to. Need better shoes/insoles. Idk how different a DS is from an FC, I've only been at an FC, but day 1 should be the easiest. Since you left early tho, you might have to redo your day 1
[juycdkf] (score 24, diepte 2) Those safety shoes suck ass. Yeah get some new insoles. I've gotten like 4 pairs off zappos and can't wear any. Just bought some Tim's for mountain climbing lol. They look the part. Well, like someone else said, if it's still too rough after a couples weeks maybe look for something else. Not worth destroying your body
[juy8vw9] (score 23, diepte 0) Stick it out two weeks without taking vto.  After two weeks if you're still in agony I'd look for something else.
[juy94ug] (score 17, diepte 1 OP) Yeah I used the safety shoes they gave me, I wasn't allowed to wear my normal shoes that were desgined for support. I'll have to look into insoles. I've worked a bit at an fc too but this was way more rough. Had to load boxes from a conveyor belt onto the cart the whole time basically. This was techincally my second day since my first was just an orientation.
[juyrdjl] (score 12, diepte 0) Don't make promises you can't keep.  Amazon floor is made of 40% adamantium 40% vibranium and 20% Boba fett armor.
[juyazf8] (score 11, diepte 0) It’s the shoes. My feet hurt every now and then with the safety shoes on.
[juyusb1] (score 9, diepte 0) Size up half a shoe size.  Your feet probably swelled up.
[juyuy8q] (score 9, diepte 0) I was in excruciating pain too when I first started at a DS. Felt like I was walking on knives. Every step I was wincing. First few weeks I was popping 1000mg of Tylenol during lunch

Getting the right shoes and inserts helped. As well as just getting used to it. But by the end of shift there’s still a pretty good amount of pain 

I’m using my benefits and will be seeing a podiatrist soon to get custom orthotics however which should see a significant change
[juyvkst] (score 9, diepte 0) Almost a year in, and the pain never stops. You just get used to it or you quit. That’s about all there is to it. Insoles help for a bit, but then the pain comes back. Changing your shoes helps for a bit, but the pain comes back. You can’t escape it. You can try to manage, but it won’t go away.
[juymozr] (score 8, diepte 1) Lol that isn't gonna help their foot pain. I know because I was in excruciating pain for months. I also left early on my third day because of the pain. The pain never went away and I had to get on medication for the pain. Have I said "pain" enough?
[juyth8u] (score 8, diepte 0) Normal for your first week or so. After a month; you’ll get use to it. Buy good insoles and compression socks and sleeve. That’ll help a lot.
[jv0s88d] (score 7, diepte 2) Day 2 (after orientation) is NOT your easiest day, dunno what the above commenter is smoking. Your body doesn't understand why you're on your feet for eleven hours with two half hours breaks in-between (or however your DS breaks it up). It takes time for your body to respond, usually about a week. 

Your shoes may indeed be part of the problem. Everybody responds differently to different shoes, so take your co-workers' advice about a specific pair with a grain of salt. I would definitely try returning your shoes and looking for a new pair. You can try another pair from Zappos. Note: you do not have to wear Zappos specifically, but they do have to be approved by safety if you're going to go elsewhere. And for the love of God, don't wear tennis shoes that "look like safety shoes" because you WILL DROP STUFF ON YOUR FEET. It's inevitable. 

Be kind to yourself above all. This is not an easy job on the physical side, especially during this initial period. Stretch even if you feel dumb doing it. Take your breaks, and use your PTO and UPT wisely. Best of luck.
[jv0eeih] (score 7, diepte 1) Yup this right here. My body took about a week and a half to adapt to the physical toll of working here.
[juzemus] (score 7, diepte 0) I've been working at Amazon for 2 years 2 months and I don't feel anything anymore. After awhile you will get use to it.
[juyy1wd] (score 6, diepte 3) I recommend the sketchers work with memory foam they are literally so comfy
[juzi8dt] (score 6, diepte 0) What kind of shape are you in? I see 300 pound motherfuckers working at our site all the time 😆
[juyynfk] (score 5, diepte 4) I tried the memory foam. They completely destroyed my feet. Felt like I was walking on needles after each shift. I liked the shoes but I took out the memory foam insoles and put in diff ones
[juyxuyr] (score 5, diepte 2) Pretty much as long as you get shoes that LOOK like they're safety shoes, nobodies gonna bat an eye tbh. Honestly after a week or two when you don't have learning breathing down your neck and then switch back to your normal shoes. As long as they're not flashy you should be fine.
[juz4cp5] (score 5, diepte 1) 20% Beskar???
[juzas9u] (score 5, diepte 1) I hope you’re kidding. Almost every person that works at any amazon has a hard first few days/weeks, and if you didn’t, consider yourself lucky. This isn’t cut out for everyone.
[juyu2os] (score 4, diepte 2) I feel like they posted in the wrong thread 😂 Talking about treats in a thread about foot pain
[juz95h7] (score 4, diepte 1) That is how I described my pain. It was like walking on knives. Never felt foot pain like that in my life and that was before safety shoes were required.
[juyxyp6] (score 3, diepte 2) Sketchers work with memory foam are so comfy
[jv17chz] (score 3, diepte 3) I told every new person that came to our DS that they needed shoes with high toes to prevent the gray carts from being able to snake your instep bones.. then one day I wore the sneaker type and dang near broke my foot with a cart lol.
[juyueia] (score 3, diepte 3) fr they obviously don't understand the level of pain we are talking about
[juyocjs] (score 3, diepte 0) Get the shoes that says “do the best” I honestly dont know what they are actually called but you can buy some from amazon for around 40-50 bucks and they are very comfortable. I wore timbs that used to hurt my feet at the 5 hour mark of the 10 hour shift. I can’t believe i used to put up with that for a year
[juz4hh0] (score 3, diepte 2) They are work shoes, how are they not allowed?
[juypwl9] (score 3, diepte 0) Just go head and quit
[juzkuq3] (score 3, diepte 1) > 40% vibranium and 20% Boba Fett armor.

THAT is why everyone's feet hurt so much. Makes so much sense. 

(Might as well be. Their floors are the worst!)
[juz2fe2] (score 3, diepte 0) I work in a DS and just finished my 3rd week. My feet kill me every day. But I went from walking maybe 5000 steps to over 30K in one day. Most days I average about 23K. I keep telling myself I'll adjust but some days are harder to believe that than others lol I'm a fairly active person and I definitely feel every step when I clock out at end of day. LoL
[juz6gi9] (score 3, diepte 0) Someone suggested double socks. I tried it and I don't know how it works, but it helps!
[juzfl83] (score 3, diepte 0) I mean tapping out on your first day isn’t a good sign. Idk what you job was before but if you can make it a few hours of standing how are you gonna do 40 hour weeks standing for ten hours.
[juzokp5] (score 3, diepte 0) I wonder what Jeff Bezos would say if he had to wear those Zappos safety shoes for 10-12 hours/day?
[juzsv76] (score 3, diepte 0) Dont be a pussy
[jv0m9op] (score 3, diepte 0) Place your bets everyone. Chances are this one won’t make it past the second week. Maybe three weeks since it’s a DS and not an FC. Delivery stations are small potatoes compared to a warehouse.

Don’t give up. Trust me, those pains go away. It took 3 weeks and after that it was smooth sailing. The problem with the majority is they give up too easily. Remember, the people you saw today at work in your day one class. Within 3 weeks maybe only 5 percent of them will remain. After a year it’s likely nobody will be left except you.

Be a soldier and fight your way thru the first few weeks.
[jv16wjs] (score 2, diepte 5) You might be flat footed. I get the same way with soft insoles.
[juzatfs] (score 2, diepte 5) For me personally I love memory foam and I’ve had my favorite pair of sketchers for 3 years that I nearly wear everyday and still great and still comfy and haven’t worn out. Idk that is just how I feel and I’m just glad my feet like them. Like I said my feet get very sore easily and hokas and sketchers are the only thing I wear
[juzkj2y] (score 2, diepte 3) Not when you wear a wide and they literally never have any wides in your size. If you have bigger feet you're SOL.
[jv00drt] (score 2, diepte 5) I'm a 9.5-10 and they never, ever have anything in stock. Tried a different work Skechers and they were awful and hurt two hours into a shift.
[jv2wpb0] (score 2, diepte 3) Yes you literally just keep the box that your shoes come in. Go to Zappos or call their number and they email you a shipping label. Then just to go a post office print the label and return them for the same pair or a different one. Your welcome lol
[juyuvsu] (score 2, diepte 1) Bruh what
[juyizee] (score 2, diepte 0) 2-3 weeks you will be doing okay it sucks at first
[juypvfp] (score 2, diepte 1) I was told today that they are starting to tell people those aren’t allowed. Technically they never have been but they are starting to enforce it at my site
[jv0mwvh] (score 2, diepte 3) Because they aren’t “Amazon approved”
[jv2v3o8] (score 2, diepte 5) I heard it was due to how slippery those shoes get. I have a pair and They are very slick on the bottoms. And you’re definitely right about the deal with zappos. I wish they would worry about getting everyone in the damn safety shoes and then worry about what specific type people have on.
[juyrr1r] (score 2, diepte 1) They’re $25 or around that on Temu
[juzbypg] (score 2, diepte 3) They're not the proper code / type of work shoe. They have actually always been banned never enforced. Out at RNT9 and we got the message today. Just because your WASH hasn't done anything about it doesn't mean there won't be. They're banned. Check this sub reddit
[juzbzrh] (score 2, diepte 3) It's an osha violation
[juz4fa6] (score 2, diepte 0) Drink a beer like i do every break 😂
[jv0p6xy] (score 2, diepte 1) I worked during the pandemic and a lot of my new coworkers came from a white collar lay-off; they weren’t used to standing/physical labor. Most of them tapped out by first break on 12s, didn’t even make it to lunch… or their second week!
[jv18kdv] (score 2, diepte 2) During peak 2021 or DS started with just me as the only day shift front and back half AA for a month, then we got 2 a week for the duration and of those 2 , 1 would quit after the 1st 6 hour shift... we were working 5 x6s but recently became real boys and moved to 4 x10s lol.
[jv1z4qv] (score 2, diepte 3) I opted the five 12s in April 2020 until they stopped double rate OT I think in August that same year. I came from a job that paid me 12.50 an hour, on 3rd with a premium! My paychecks were federal exempt too because I made so little prior AGI, and I was paid $1,400 a week before I became an official warehouse employee at Amazon [until they paid officials weekly from biweekly I’d believe October that same year]. Pain or not, once I got used to my paychecks I definitely got used to my shoes! Can’t beat $38 an hour for robot work… but I feel bad for folks now, underpaid for the massive aftershock from the pandemic isn’t a good enough statement, especially those in Whole Foods - they got jammed and slammed.
[jv06teu] (score 2, diepte 0) Insoles. These shoes are built for protection. Not comfort, unfortunately.
[jv3c1pp] (score 2, diepte 0) The best advice I can give is don't wear safety shoes. Wear black ultraboost 22s. Doesn't matter if it's against the rules.
[jv3odr7] (score 2, diepte 0) Zappos has an amazing return policy so if ur not feeling the ones I have, return em and try something different. Read the reviews ppl leave. I have Merrill boots and they work perfectly imo. Good luck and keep ya head up. DET1 CHECK IN
[jv44i19] (score 2, diepte 0) Switch to an FC. The DS are too much work for a normal person. Trust me. Don’t do this to yourself.
[jv5rbjm] (score 2, diepte 0) Matter of opinion. I worked DS for 3 years. Now fulfillment for 3 years. Running on concrete for 10 hours was worse for me. Day 1 training emphasized wearing a good shoe and insoles. When I switched to fulfillment I found it a relief. The right shoe does make a big difference. Find a brand that works for you. Get a couple of pair and switch them. Wear one pair for few hours, then change to another pair.  Depends on what you are doing. Just a suggestion.
[jv6drnw] (score 2, diepte 0) https://preview.redd.it/dsbrynp5rpgb1.jpeg?width=1290&format=pjpg&auto=webp&s=f92cf189d1b6d692b45373b35a409da016eb2dbb

HIGHLY RECOMMEND YOU GET THIS!! if your FC/DS hasn’t banned these shoes hop on it NOW. honestly these shoes literally ended foot pain for me along with many people that bought it and honestly, for $50 it’s one of the best shoes compared to any of Zappos shoes I’ve bought that doesn’t come close to the level of comfort these shoes got
[jvcz45c] (score 2, diepte 0) You have to break the shoes in and your feet are not used to you standing so long.  I Take ibuprofen b4 work, after each  5hours.  I work 12.  I take shoes off at breaks.
[jvjh29p] (score 2, diepte 0) I wear new balance with aluminum safety toe. Looks like a tennis show but safe and comfortable. Just change insoles when the OEM ones wear out.
[juy5rq8] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[juyytiv] (score 1, diepte 5) I wonder if it was the shoes I just barely got. Because I have feet problems and the shift went by so fast and my feet felt so amazing the whole shift.
[juyyxr0] (score 1, diepte 5) [the shoes](https://www.zappos.com/p/skechers-work-bulkin-balran-comp-toe-gray-black/product/9483321/color/1114)
[juyz6b2] (score 1, diepte 5) But also it could be because I love sketchers. I went from wearing regular sketchers to work sketchers so I knew these would be comfy for me
[juz0o6q] (score 1, diepte 6) Idk it's odd. I had a pair of sketchers with memory foam that I just wore out and about and my feet were fine. But when I got the work ones my feet were dead. Ig my feet just weren't getting the proper support for a 10 hour shift
[juzai8q] (score 1, diepte 4) Memory foam sucks dick. Gel feels a whole lot better and lasts longer. When I had memory foam insoles I had to change em out every month. Now I can go like 3 -5 months on a pair of insoles and be comfy the whole time
[juyxwt7] (score 1, diepte 2) Wear the sketchers ones! There are good you get a 110$ credit for any shoes
[juzkop1] (score 1, diepte 4) I do wear wide I’m a 6 to sometimes 6.5 wide. Always a wide
[jv0ko8b] (score 1, diepte 2) There is a pair you can get from amazon that have the wait I took a picture of what the composite needs to be

https://preview.redd.it/rr6zlreh1hgb1.jpeg?width=3456&format=pjpg&auto=webp&s=39a658487087727a3dd2b29a2d0b41566c47af35

The ASTM whatever and they are real comfortable. I have a regular pair of the same shoes too. They are around 50 bucks I see people at work with them all the time but I would double check if they are okay because every site may be different let me get a picture and post under my comment well if you want them
[jv1s6xb] (score 1, diepte 3) Idk what you're smoking but OP didn't specify that it was their day 2 until I commented that. The original post literally says it was their first day
[jv1b0oz] (score 1, diepte 2) Look up reviews of shoes. Like best safety shoes for x y z
It took me a while to find a good pair (I like the merril work shoes for standing and skechers max cushioning for walking but with different insoles)
Depends on your feet. Also, some people take a month or two to get used to working amazon. I work in a tns(traditional non sort) fc but I started at a ds.

If you can afford it, custom orthotics are the way to go

 As your first job out of high school, this is one of the most lenient jobs you might ever have. Your time is your time with the exception of vacation (at least 24 hours and excluding blackout dates like peak in December and prime day in july)
[jv06x3y] (score 1, diepte 1) If theybhit 5 hours, they're cool I think. But honestly. Another day one isn't the worst thing. Lol. "OH NO! 3 DAYS OF ZERO WORRIES ABOUT RATE AND QUALITY!"
[jv217nd] (score 1, diepte 2) I didn't know the 5 hour thing. They always act like you *can't* leave day 1 lol
[juzfvwt] (score 1, diepte 1) You can always return your Zappos shoes and get a different or new pair. Even if you like the shoes you have and they get worn out just return them and get a fresh pair for free.
[jv0ugo9] (score 1, diepte 2) So you can return worn pairs still??
[jv2vob3] (score 1, diepte 2) How
[jvd42eq] (score 1, diepte 3) Call the number for Zappos and they’ll get your email and send you a shipping label to return them.
[jv0u60q] (score 1, diepte 2) Are you eating inflammatory food. Like chips and soda lunch meat fast food...some  People have no idea what diet does to pain in the body
[jv0uaxl] (score 1, diepte 2) Yeah but do you understand the effect of flammatory food on the body...chips soda fast food fried food. That will make your pain 1000 times worse
[juylzf1] (score 1, diepte 0) if ur not used to doing at least 6 to 8 miles a day it will hurt.ost of my former jobs and roles were standing up and away from a desk, and I walk routinely on my own time. it will adjust given time and calibration, definitely need the best inserts you.can get. I suggest the most expensive ones like $30-40.
(100 reacties met lagere score weggelaten)

=== THREAD 1tly0gp ===
SUBREDDIT: r/Construction
DATUM: 2026-05-24  SCORE: 89  REACTIES: 174
TITEL: Been working in boots for 10 hours a day in the heat. Now both my feet have peeling skin between the 2 smallest toes. I change socks and clean/dry my feet right after work, but what else can I do to stop this?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[onj0da8] (score 97, diepte 0) Gold bond in your socks.
[onj03te] (score 76, diepte 0) Video call a nurse hotline and see if it's athletes foot.
[onj195r] (score 65, diepte 2) Gold bond in your socks.
[onj2e5y] (score 53, diepte 0) Change socks halfway through the day or more often depending on conditions.  You are describing Trench Foot
[onj1byy] (score 51, diepte 0) Boot dryer
[onjqemx] (score 39, diepte 1) One step further to get rid of the athletes foot that is already there.

Miconazole powder.
[onj1ofy] (score 36, diepte 1) And cycle between 2 pairs of boots, leather takes a long time to dry out
[onj1jhy] (score 35, diepte 1) Had same thing happen when I was working construction few years back. The peeling between toes is classic athlete's foot territory - moisture gets trapped there even with good sock changes. Get some antifungal powder to put in your boots before work, makes huge difference for preventing it from coming back.
[onj1jvv] (score 32, diepte 3) Speak English, doc, we ain't scientists!
[onj8dzw] (score 29, diepte 1) Some nice wool socks like darn toughs are antibacterial/microbial and keep your feet cool in summer and warm in winter, wick sweat pretty well, and darn tough will replace them once you wear them out, forever. Lifetime warranty for socks can’t be beat.
[onj3ign] (score 23, diepte 2) Alternating between two pairs bought at the same time will make them last way longer than buying two pairs of boots in a row.
[onj2owr] (score 22, diepte 0) Apply topical antifungal cream every day before putting on socks.  It’s a lifestyle
[onjk2bl] (score 17, diepte 1) Yes or no, it's cheaper just to go buy the cream and try it
[onj4bcz] (score 17, diepte 2) Put talcum powder in your boots each morning. It absorbs the water/sweat to help keep your feet dry. It'll also help kill bacteria. Also be sure to leave your work boots in a place that'll dry them out between shifts.

It'll also help to change your socks midway through your shift. You may need to see a doctor because you might already have athletes foot. It's a fungal infection that you want to nip in the bud. It can easily spread and become jock itch, which is much worse.
[onktcbf] (score 16, diepte 2) It sounds counterproductive, but darn tough wool socks keep my feet in great shape even on the hottest days. I swear by them.
[onjrlmu] (score 13, diepte 3) FYI, it's not actually talcum powder anymore. Many, if not most companies have stopped using talc.
[onj1b51] (score 12, diepte 0) Antifungal foot powder or spray, on your clean dry feet, in your socks and in your boots.
[onj4f5i] (score 10, diepte 1) Sock changing was paramount for me.   Good sucks helps as well.   I also change my t-shirt and underwear on lunch.   Feeling dry feels so good.  

I wear slides without socks during lunch, and on. T way to and from the jobsite and after work.
[onj7isl] (score 10, diepte 2) I never understood why some guys would drive to and from a site in boots, during a shift I can’t wait to get those hot heavy fuckers off my feet
[onj4z0o] (score 10, diepte 0) You have athlete's foot
[onj7t0o] (score 9, diepte 6) The factories and job sites where guys worked in literal clouds of the stuff with only a wet bandana around their face are where all the mesothelioma and cancer rates came from.  Even then, it took more than 2 years of working in those conditions to bring about more than a 5% chance of long term sickness. 

You’ll be harmed a 100x more by cutting hardieplank or quartz or concrete without full PPE than you will a bit of talc on your feet.  James Hardie company of Hardie products that we use today is the same company that made so much asbestos siding over the years and fought to cover up any harmful effects.
[onjat0r] (score 8, diepte 0) Gotta get wool socks.
[onjvbbb] (score 8, diepte 0) A former FMF Doc's advice:

Medicated Gold Bond in the socks during the day. Cream on the feet at night (with lightweight or dress-socks to bed)

Also socks- get good ones, nothing that comes in a pack of 20, nothing from any box store. If you can, swap them around lunch (more goldbond)- I recommend bamboo hiking socks. ex: EcoSox

Insoles - people always overlook this. If your feet aren't supported well it makes a bunch of other things worse. I recommend superfeet green or orange (break-in sucks for a few days)

Boots - don't wear the winter gortex stuff in the summer. If they just won't breathe consider taking them to a cobbler to put in mesh grommets. This makes the biggest difference.

Source: Doc that had to say the same thing every day to about 100 Marines while in deserts all over the globe. Drink water, take Motrin 😆
[onn9tak] (score 7, diepte 1) Yall need to stop wearing heavy ass leather boots…not just for the sweat but for the weight too.

You’ll be blown away by how much better you feel at the end of the day by just finding the *lightest* pair of hiking shoes/boots with safety toe you can find.

They are rated/OSHA approved.  They’re way lighter.  Way more comfy.

Who wants lead feet?  1lb on the feet is 5lb on the back.
[onjj26c] (score 7, diepte 3) I blame a lot of my back and knee issues on my boats.  Since I’ve retired I wear mostly zero shoes and can’t stand to wear my boots at all.    I prefer bare feet honestly.   It takes a lot to get me to even put shoes on anymore.

I personally think the entire work boot safety culture needs to be reexamined. 

The trades wear hard enough on the body.   Work boots are the equivalent of a welding your shock absorbers rigid on an automobile.   Your feet can’t do their job and protect your knees and back from the impact created during walking.    The weight is super bad as well.   Honestly I compare it to increasing rotating mass on a truck but putting larger wheels and tires on it.   It wears out all the suspension parts faster.   What do you think the heavy boots are doing to your joints.

No one cares though because once you’re worn out it’s your problem.

It’s crazy to watch YouTube videos of guys working in foundries in India with sandals  on.     They will be smelting, forging, welding, basically bare foot.
[onjrigj] (score 6, diepte 4) Many companies use corn starch or other non-talc bases now. Including Gold Bond.
[onj25ud] (score 6, diepte 0) Get those boots off asap every day. Put em on a boot dryer and spray em with anti fungal spray.  Shower immediately every day and keep your lamberfeeties open to air as much as possible, no socks, no slippers, let them dawgs breath. Toe separators ain’t a bad idea either if it’s real bad.
[onk3nr1] (score 6, diepte 0) You need more than one pair of work boots so that they can dry out between uses.
[onn9wzs] (score 5, diepte 2) Also. Make sure to dry the fuck out of your feet after a shower.  If you're socking up right away you'll never get rid of it
[onj7z6a] (score 5, diepte 7) No doubt, all the more reason not to introduce more clouds of shit to what we already breathe in on the job.
[onjy0b7] (score 5, diepte 5) It was (in baby powder). No, it wasn't (safe). They've stopped using talc in baby powder
[onjzqf8] (score 5, diepte 2) Good sucks are why some of us go to work to begin with :)
[onn8t2a] (score 5, diepte 3) Wool can keep you cooler or warmer if I remember correctly. I think it’s a fiber that responds to body temp.
[onj602u] (score 4, diepte 5) True, but it also gets asbestos contamination from where it’s mined frequently, and I’m not fucking around with potentially breathing in mesothelioma dust when there’s an alternative.
[onjlqxe] (score 4, diepte 3) Jock itch sucks so much ass
[onj0l9h] (score 4, diepte 0) Put on some toe separators before you go to sleep. Really helps with pain and fatigue too. 

Your feet are also probably crammed into a boot that isn’t ideal for your feet shape so, think about whether it’s time for a change.
[onjonun] (score 4, diepte 4) No my ass would’ve injured myself in India no doubt. I’m one clumsy motherfucker. Tough tho…
[onjw88s] (score 4, diepte 1) Vinegar soak is a little more civilized.

I have done it the other way too
[onjeq4s] (score 4, diepte 1) To add on, spend the extra money and scoop some nice merino wool socks, they’ll keep the feet dry

Big fan of darn tough socks, expensive but lifetime warranty is a nice trade off, get the thick ones not the thin hiking ones.
[onj4vcb] (score 3, diepte 3) Talc’s carcinogenic but you can use cornstarch.
[onj74rs] (score 3, diepte 6) I've been looking for a good alternative to talc for this exact reason. I'll give corn starch a try once it warms up enough in my area to need it
[onj7on2] (score 3, diepte 2) Toe box on thorogoods is not as big as you think. Coming from someone with triangle shaped feet, and toes being the hypotenuse. Keen Cincinnatis/liberty are better, but still not as much room as I’d like, since I wear bearfoot/zero drop shoes, I’m used to being able to stretch my lil piggies all the way out.
[onmasgo] (score 3, diepte 1) Boot dryer changed my life. Helps with odor too
[onot90f] (score 3, diepte 3) Very Expensive Socks, but not as expensive as hospital treatments for infections.
[onj2rtb] (score 3, diepte 0) Don't wear cotton with boots either.   Try wool.
[onj640m] (score 3, diepte 0) Surprised nobody has said to pee on them in the shower.  Its an old foke remedy but it worked for me.
[onl3o9u] (score 3, diepte 0) I wear merino wool socks and that solved my 14 hour a day in boots issues
[onlehft] (score 3, diepte 0) Wool socks. Don’t wear cotton.
[onj5m4l] (score 2, diepte 4) I could be wrong but I read that it's harmful to breath in, not to apply to the foot. Do your own research and use it at your own risk. Be safe out there
[onjy4ln] (score 2, diepte 7) Modern Gold Bond uses corn starch, most (all?) brands of similar powder do now
[onjf3ya] (score 2, diepte 4) Isn’t baby powder the same thing? Should be safe, right?
[onkhfap] (score 2, diepte 4) Interesting. I had no idea
[onj6fx8] (score 2, diepte 2) Its a foot powder, antifungal too
[onj2xjd] (score 2, diepte 1 OP) I wear thorogoods, the toe box is super spacious
[onj7wv3] (score 2, diepte 3) I wear barefoot steel toe Jim greens, it’s the comfiest boot I’ve ever worn.
[onlt2z7] (score 2, diepte 3) If they're expensive then it's worth an extra step or two taking care of them. Leather can get too dry so applying leather balm every so often can possibly help with cracking, flexibility, and water resistance

It's dependant on your trade and climate you work/live in so how often and how much varies

I'm pretty sure leather balm is boujee Vaseline for those on a budget
[onmd4pe] (score 2, diepte 4) As a mechanic, I get free daily coatings of oil to forever maintain the waterproofing 🤣
[onl85o2] (score 2, diepte 1) Have you ever put warm boots on in the winter?  😇😇
[onj1nrc] (score 2, diepte 0) Clean and dry your feet thoroughly. Slather your feet in Vaseline and put on an old pair of socks right before you go to bed and you'll be amazed at what a night or two of this will do for your feet. I deal with the same issue
[onj264g] (score 2, diepte 0) Absolutely nothing if your anything like me. Im healthy AF but have always sweat worse than a fat kid. It's the main reason I don't want to work in the trades anymore. I sweat all the way through my pants and clothes and boots too and have to walk around like that all day soaked. Never fully drying out. My clothes used to develop a musty smell that would never wash out.I'm just not built for it....it's gross. Can make the same in any factory somewhere and not have to deal with all the bulshit too
[onmkpke] (score 2, diepte 3) Autocorrect strikes again.
[onp3cfb] (score 2, diepte 4) It’s a small price to pay for healthy feet.
[ono3p2k] (score 2, diepte 2) Wool is the key. Saved my feet thru 35 years in a steel mill.
[onj2edh] (score 2, diepte 0) Gotta get those on a boot dryer as long as you can every night.
[onj2fgb] (score 2, diepte 0) Get a boot dryer. You might think your boots are dry every morning but i can assure you they aren’t.
[onj35uk] (score 2, diepte 0) Sounds like athletes foot. Highly contagious if it is.
[onj3fk6] (score 2, diepte 0) You probably need an extra pair of boots to swap out so they can be completely dry. Dry between each toe after you shower. Powder your feet every day. When you feel that tell-tale tickle of athletes foot, use the cream immediately. I’m very prone to this. Do these things, you’ll be good.
[onj4jyo] (score 2, diepte 0) I recommend using really good socks. Thick, full wool socks. I worked in southeast Asian (over 100 F) shipyards and never had an issue in my 4 years there. If that doesn’t work, then your boots are probably too big if you have a fungal infection. Even if you do have a fungal infection, my above points are still true… get boots that fit properly and buy good socks.
[onj5330] (score 2, diepte 0) Anti fungal spray and powder. I recommend the blue gold bond powder, put some in boots at beginning of day and when removing. Place in front of fan to dry in evenings, 100% wool socks, or cotton, and a fresh pair of socks to put on if you soak through or for when you get off work. I always kept slides/flip flops in the car to remove my boots as soon as I get to the vehicle. Keeps the car nice too
[onjazfs] (score 2, diepte 0) More breathable shoes.
[onjbp3k] (score 2, diepte 0) Too much sweat from socks. Switch to merino wool socks. They’re naturally anti bacterial and do a great job of wicking away moisture and getting rid of smell. I use darn tough and even after a 30 degrees c day they don’t smell.
[onjc1w4] (score 2, diepte 0) Tea tree soap.


---


Tea tree oil needs dilution before going on skin, btw.
[onjfu3a] (score 2, diepte 0) Gold bond boots

Merino wool socks 

Keep feet dry 

Powder them doggies after work and let them air dry
[onjhhrm] (score 2, diepte 0) Been where you are. Ended up with cellulitis of my foot and it blew up the size of a football one night while I was sleeping. Here’s my current routine.

1: Good boots! 
2: If you don’t need waterproof, don’t wear waterproof it just traps the moisture
3: boot dryer and use it every day!
4: Athletes Foot powder spray, even when you don’t have it. It just keeps them dry and helps keep infection from occurring.
5: Good socks!!! I can’t recommend merino wool enough. Even in the summer, just buy the thin ones they don’t get hot I promise. (Actually I really recommend compression ones, they make a world of difference)
6: change socks, but I prefer to strip off the socks and put on flip flops/slides at my truck after shift. Don’t matter if it’s winter, I got heat in the truck.
7: Wash. Your. Feet. I mean good, make sure to get between the toes. Then dry them good before putting on slippers or socks.
8: Really dry those newly clean feet. I actually use a hair dryer to get them nice and dry ESPECIALLY BETWEEN THE TOES!
9: get a podiatrist!

Good luck buddy, I don’t envy you. But it is survivable
[onoog6k] (score 2, diepte 1) Or blow the corpsman for some mole skin 😆
[onjz9ea] (score 2, diepte 0) That's athletes foot.

Get better socks, and spray some tenactin or whatever kinda athletes foot shit you want on your feet before work.

I'd also recommend a boot dryer to keep the moisture outta your boots.
[onk4qrf] (score 2, diepte 0) More breathable boots (traditional all leather suck) and wicking socks that you change at each break
[onk78fz] (score 2, diepte 0) Wear merino wool hiking socks. Pricey but bad feet are costlier
[onkwvb3] (score 2, diepte 0) Wool socks 🧦
[onl9cvv] (score 2, diepte 0) Merino wool socks and boots that will breathe.
(97 reacties met lagere score weggelaten)

