# Label-batch batch_0148

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
Schrijf het resultaat naar `batch_0148.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(6 threads: bxt32k, ceznoe, rj75dg, 3d08zh, 8dvxiu, wvjshm).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD bxt32k ===
SUBREDDIT: r/rheumatoid
DATUM: 2019-06-07  SCORE: 10  REACTIES: 21
TITEL: Copper bracelets and CBD oil
POST (source_id=post):
My mum has been suffering with RA for a few years now (7/8) with methotrexate on a friday leaving her in bed for most of saturday. 

Recently though (6 months/ year) her flare ups are becoming more regular and steroid injections are a regular thing now which give her a few weeks of relief.

Whenever I mention that she has RA people always say the same things.. "my mum has arthritis in her hands but she wears a copper bracelet has she tried that?" 
Or "she should try CBD oil its a miracle cure-all blah blah." 

I guess this is half a vent and half a quesyioning plea.

Are there actually any natural remedies that anyone here has had success with? 

Also she has been told she may have to move to a biological remedy.. any ideas/experiences with this kind of treatment?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eq9fepk] (score 18, diepte 0) If she’s having a bad go of it for that long, the mtx isn’t working. Time to add a biological imo 

Tried CBD, no luck for me. Others have had some symptom relief with CBD (you mean for symptom relief, not as a “cure”, right?)

As for the copper bracelet.... just no.
[eq9geho] (score 11, diepte 0) If someone has arthritis 'in' a specific joint, then they don't have RA - I find that most people don't really understand the difference.

CBD definitely helps some people, but it doesn't do anything for me without some THC in the mix. Even then, I don't think that the CBD actually helps my symptoms, but it stops me from feeling as high from the THC and lets me be functional.

But yes, I agree - I'm tired of everyone having an aunt/grandmother/hairdresser with a 'natural' arthritis cure. Fuck you - I'm going to continue to inject this chemo drug into myself once a week and smoke my pot.
[eq9m6mn] (score 6, diepte 4) Biologics are a quantum leap over MTX and other dmarts.  Hopefully she has good insurance they are very expensive but Honestly they are the closest thing to a miracle drug.  I'm surprised her doctor has gone to regular steroid injections before trying a biologic.
[eq9gist] (score 4, diepte 1 OP) Yeh it gets old explaining that one to everyone right?

In seriousness does smoking weed actually help? I've suggested it to her but with work and things I think she's worried about the risks over the anecdotal benefits
[eq9gwao] (score 4, diepte 2) I find that it helps me a lot, but not in the same way as other painkillers. It doesn't necessarily kill the pain (although it does help somewhat with inflammation) but it sort of disconnects me from the pain. If I think about it, I can recognize that it is there, but I'm able to easily distract myself from it. 

Obviously there are risks to inhaling smoke, regardless of whether it is tobacco or cannabis, so I always recommend vaporizers or edibles to people. That said, smoking the first few times just to see if you like it or not before shelling out a couple of hundred dollars for a vaporizer is probably a good idea.

I definitely do *not* recommend edibles for a new user, because if you don't like the effects, you can be stuck with them for 8 hours, and that sounds awful.

Also, I live in Canada and it is completely legal here, medical and recreational. I even had a prescription for about a year before it became legal. Now I'm able to grow 4 plants in my yard, and being able to grow your own medicine is a pretty cool experience.
[eq9i12u] (score 4, diepte 0) Calming the mind helps calm the body and vice versa. CBD and cannabis help take the edge off for me and I don’t need them in combination. It’s either/or. Of course, these don’t help everyone so she needs to find what helps her relax.  For example, getting ready to go to bed can be an dreaded time for me because I know it’s very likely that intense pain will disturb my sleep. So I try to calm down before going to bed. It really does help somewhat with the pain as well as initially falling asleep. I also keep CBD cream on my nightstand for any joint explosions in the middle of the night. It is expensive so I only use as needed.

Copper bracelets sounds ridiculous but I guess I would be willing to try it. It can’t hurt, right?
[eq9k3k9] (score 4, diepte 0) My brother in law is convinced his copper bracelet works. He's the only person I know who has had any success with that kind of thing.

I did speak to my doctor about CBD. He wanted to make it clear that it isn't in any way a miracle cure (he pointed out that if it were a cure, no one in countries where it's legal would still be in debilitating pain) and that it's really only going to take the edge off the symptoms.

I haven't tried it, a couple of friends say it takes the edge off their chronic pain, but it certainly isn't all it's hyped up to be.

I think if she's having this many flares, she needs to talk to her rheumatologist about adding another medication.
[eq9kufc] (score 4, diepte 0) CBD is a real thing and it has chemical properties that doctors can understand.

&#x200B;

Magnets are everywhere.   Crazy powerful magnetic fields exist in our daily lives and we are not effected by it at all.

Ask your brother in law if he has ever been in an MRI machine.  Or taken a subway, or walked under some power lines.   All these things induce far greater magnetic influence all around us compared to a stupid copper bracelet.    People claim crazy shit all the time, but big claims require big proof.

CBD has that proof.   Magnetic nothingness has a claim on nothingness.  Copper does not react to magnets.  It does conduct electricity well, but hold a magnet up to a penny and see.

Either does incense and good wishes.  They don't help either.   :)

&#x200B;

lol... tell your brother in law he could have saved some money and just kept a bunch of pennies in his pocket instead of buying a bracelet for .....$20?  lolroflmao
[eq9l6p2] (score 3, diepte 1) If he really believes in the copper bracelet, it is probably the placebo effect. That said, if it helps, then there isn't any harm in it.
[eq9vyss] (score 3, diepte 0) Copper bracelets are 100% snake oil
[eq9fi4g] (score 2, diepte 1 OP) Haha a cure. Good one. 

Yeh I think the doctor has agreed that the mtx isn't working anymore. What is a biological though? Honestly sounds scary.

Have you actually tried a copper bracelet though? /s
[eq9jayx] (score 2, diepte 2) Biologics are Enbrel, Humira, etc.

Enbrel hurts like hell (for me) to inject, but it was a game changer!
[eq9jnp9] (score 2, diepte 3 OP) That sounds pretty hopeful! I think it was the name of it making her a bit anxious. I just want to see some improvement or more good days you know?
[eq9h0ia] (score 2, diepte 3 OP) Worth thinking about then. Think I see what you mean about the disconnection. Thanks for your help! Will update if I ever convince her to try smoking!
[eq9kxrm] (score 2, diepte 3) Came here to say basically this but I'll reinforce what was said instead.

  I was told by my dispensary that the THC and CBD act as carriers for another so one wo the other is less effective.  And also was told the CBD cancels out the euphoric effects of THC in nearly a 1/1 ratio.  

I take Humira  and leflunomide and  use CBD like I would nsaids for temp pain relief instead of nsaids but not as a cure 

Good luck w figuring out what works because everyone is different.
[eq9ho76] (score 2, diepte 2) Yes it really helps. Definitely give it a try
[eqbltew] (score 2, diepte 1) I can't take NSAIDs so my options are tylenol, opiods, steroids or pot. I don't want to start opiods, really not interested in the side effects. I prefer CBD to THC because I dislike feeling impaired. Cannabis takes the edge off, enough that I haven't been desperate enough to take opiods. CBD with a THC is generally more effective and I do have a strain that is mixed that helps me sleep too. I've been on low dose prednisone almost 3 years now and would really like to get off it but it does more to control my pain by reducing the inflammation than any other option.
[eq9oejc] (score 2, diepte 0) No luck with copper bracelet, CBD helps me relax but no big change in the arthritis. 

I do take Hemp Oil which helps a little.

Agree with other user.   If your mom is still suffering, the meds need updated.

Steroids do not slow the progression of the disease.  They only provide temporary relief from joint pain.

Methotrexate does sometimes help with slowing the progression of the disease.  However, if she's suffering, it's not working.  Time for something else like a biologic (Enbrel, Humira, Remicade, etc.)

Don't ignore the frequent flare ups.  Don't let it destroy her joints and make it impossible for her to dress herself or walk. 

Arthritis is a debilitating disease that usually is an aggressive, lifelong battle.
[eq9w2sg] (score 2, diepte 1) Humira is EXPENSIVE.  The cash price in the USA is over 5,500 dollars/month.  There are other Monoclonal antibodies/ biosimilars, but AbbVie/Abbot is fighting like the devil to keep them off the market.  If you live in Switzerland Humira is 882 dollars/month.  Medicine does not have a free market and needs to be regulated. edit misplaced zeros in Humira price
[eqao80z] (score 2, diepte 2) Not arguing with your point that they are too expensive, but for those of us with insurance and a pre-authorization cleared by your doctor/insurance company, many of the biologics are covered under a co-pay.  Enbrel was $35 dollars a month for me, and Humira, which I just started, is $5 after their co-pay discount card.   Many of the makers of biologics have patient assistance programs as well to help.  

Just pointing this out as they shouldn't be discounted because of price.  It's not fun to deal with, but if you work with your doctor and insurance company, there is probably an option to try them.
[eqa0d33] (score 1, diepte 2) Yup. The constant “your too young to have arthritis “ ...sigh...

=== THREAD ceznoe ===
SUBREDDIT: r/Frugal
DATUM: 2019-07-18  SCORE: 17  REACTIES: 19
TITEL: Middle of summer, solar reflective emergency blankets, and not a single day of 'it's just way too hot in here' yet.
POST (source_id=post):
Caveat:  I have single pane windows.

Previous summers, I would wake up to morning sun, and really stuffy air. Come home to baking hot interior where I could feel everything glowing with heat.  And that's with windows open.

So last summer I tried putting up solar blankets in the windows in a rough shod manner.  I went from sweating shirtless in a 400f oven, to a much more tolerable 200f (does anyone do cooking?  It's basically almost nothing, although it does make for a very juicy picnic shoulder) in tshirts and pants.

So over the winter/spring, I went full experimenter/decorator mode. Bought a ton of solar blankets, and a ton of rare earth magnets and metal washers, and cut and taped the blankets to fit invisibly behind my drapes with the washers and magnets used to hold them in place reliably without tape.  I think I have about 150 square feet of the stuff lining my windows/drapes.

Over the winter, while the air was cold, the chill wasn't that bad, and I suspect it was from the fact that radiant heat was bouncing back into the room.  That's all fun and games and hopeful thinking.

But this summer has been definitive. Zero hot days at all.  Pants and long sleeve shirts. Blankets.  All of it. Windows closed most of the time.

If I read my thermometer, it's 78f.  Zero issues mid afternoon.  

If I had a IR temp gun, I'd suspect everything in the room is that temp.  My human IR temp gun definitely tells me that everything I touch is much cooler than 101f (human body temp).

How am I still cool at 78f, when most people say that they're melting at the same temp?

Probably because at 78f, all the objects in the room are still absorbing all the heat that *radiates* away from my body.   From the floor to my desk, to my dresser.

I'm the hottest thing in the room, and this bleeding of radiant energy is what is keeping me cool.

I've had some 85f nights in the room.  Still completely fine.  A bit warm, maybe sleeping on top of the sheets, but no sweltering where I can't sleep/exist.  An 85f bed is still cooler than my 100f body.  The bed, and all the furnishings haven't been baked to a 120f battery of radiant energy.  And even if the air is warmer than 85f, air is an insulator, and it holds very little, and is a very poor conductor of heat.

So if you're absolutely sweltering and baking, and when you touch your furnishings and they all feel warm to the touch and hotter than you, maybe consider lining all your window coverings with a reflective barrier.

If you don't believe me, try this smaller experiment.  Cover the top of your blanket/bed with solar blankets.  It won't absorb all the heat from the day, and when you sleep in it at night, you won't be bombarded by the ceiling and all your furnishings hitting you witl what I would guess by 200-300watt IR quartz heater.

I can't find the Ted Talk, but there was one about how ancient civilzations made ice in the middle of the dessert.

How did they do that?  They insulated a platform from all the  immediate surroundings.  So where did all the heat energy go?  *It radiated out into the blackness of outer space.*  Blew my mind.  Through all that air, it went into outer space.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eu63h7c] (score 12, diepte 0) Our HOA has a clause about not putting anything reflective in windows.  I ended up using Gila Heat Control film which works but probably is not as effective as solar blankets.
[eu7ebzi] (score 7, diepte 0) >101f (human body temp).

98.6 is body temp.  101 and you're running a low grade fever. Get that checked out if your temp is consistently 100 or more.
[eu6p8cd] (score 3, diepte 0) For future reference, if it's hotter outside than inside, keep the windows closed.  If there's a little breeze, it may feel cooler, but all you're doing is letting hotter air in and cooler air out until the temperature equalizes.
[eu6nh1c] (score 2, diepte 2) That is so cool! Thank you for sharing!

Was reading about the window and tin foil and thought that was a little bit wasteful if you're considering cost. That stuff gets wrinkled or torn in your stuck putting on new stuff. So I actually got a 25 foot roll of reflectix at the hardware store. I honestly can't remember how much I paid but I want to say it was in the $10 range. The nice thing is you if you cut that like a millimeter larger than the area you're pressing it into it'll hold itself in there. I put it in all of the windows that face East. I'm on the bottom of a very tall building and I've not seen my thermostat get higher than 76 which is totally bearable in the dry heat.  I close my windows first thing in the morning and they stay closed until I go to bed. and that's two specific Windows one on the east side and one on the west side so that air can pass through during the night and move things around. We've had some hundred degree days lately and I have scheduled my furnace fan to alternate on and off throughout the day and that has definitely helped too!
[eu8i8hu] (score 2, diepte 4) It's a condo 😊 and I don't use the reflectix for insulation per say I put it in the window to reflect the sunlight from coming in and baking the room steaming hot. reflectix works best if there is an air barrier between the glass and the actual reflectix.
[eu72fpq] (score 2, diepte 0) >and taped the blankets to fit invisibly behind my drapes with the washers and magnets used to hold them in place reliably without tape.    

that's a mighty LPT !
[eu9f6c2] (score 2, diepte 1) Body temperatures for healthy adults is, like with most anything, a range of temperatures.  There's a distribution.  For some people, 97°F is "normal"; for others, it can be over 99°F.
[euawadw] (score 2, diepte 4) I will definitely redo the doors and windows and leave a gap between the glass and the mylar blankets. This was basically a trial run to see how much of an impact their would be. And it is quite a bit. I also looked at a smoke tinted clear vinyl to apply. It's much sturdier and I'm sure it would help. I'm still playing around with options but I'm
[eu8fh66] (score 1, diepte 3) So you don’t have you’re own roof? That matters a lot. It sounds like you live in an apartment building. Perhaps you’re benefiting from the lower temperatures your neighbors are probably operating at?

I’m in a single story house and the center has a cathedral style roof (no attic) with dark asphalt shingles. I think I could wrap my entire house in reflective material and it would still be crazy hot on a day like today without AC!

Good post. Reflective idea is indeed a winner. I saw a flat roof once coated with the ultra white rubber like membrane product. It was so bright you couldn’t readily look at it without sun glasses. The astronauts on the ISS could probably pick out they building. The owner carefully measures electricity usage and said that saves him a ton of money.
[euczreo] (score 1, diepte 2) There is but once you break 100, there’s something going on
[eu9fops] (score 1, diepte 0) I did the same thing. I put the mylar blankets on my south and east facing windows. It really helps in the summer. They are a pain to put on the patio doors but it was worth the time and effort. I can't remember how much they were but I bought 20 of them for under $1 each.
[eu9rrak] (score 1, diepte 2) I have fingerprints on my mylar blankets. The oil on my skin apparently reacts to the heat reflecting off the blankets. It actually looks like a really dirty crime scene although it's all a yellow color instead of black. I've never tried the double sided painters tape. I'll give that a try. I spritzed the window with water to help smooth it out but I wonder if just a drop of dish soap would give it more time to move it into place.
[eubsv6w] (score 1, diepte 0) Reflective stuff on windows? Looks very trashy imo.

&#x200B;

A good alternative might be a bug screen from Solar Screen. Their mesh/screen is angled in different angles so that it blocks the sun 90% and so forth. It gives privacy from outside too. It still lets sunlight in but is indirect. Might be an option
[euecg1x] (score 1, diepte 1) I got reflective curtains on amazon. They look normal and work great. And I live in *Phoenix Arizona*
[eubyjti] (score 1, diepte 0) Unless you get the black ones.  My house faces west. That means my office, living room, and two bedrooms get pounded all day. It has paid for itself and my handyman neighbor. I have mini blinds and double backed drapes on all windows except for one for the cat tree. The black window film made all the difference.

=== THREAD rj75dg ===
SUBREDDIT: r/physiotherapy
DATUM: 2021-12-18  SCORE: 1  REACTIES: 0
TITEL: Foot Pain / Plantar Fasciitis Pain Treatment with Magnetic Field Therapy
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 3d08zh ===
SUBREDDIT: r/askscience
DATUM: 2015-07-12  SCORE: 1  REACTIES: 0
TITEL: [Engineering]Why does my car produce strong magnetic fields, and is there a feasible way to eliminate them?
POST (source_id=post):
I discovered something interesting and a little perturbing with a vehicle I just recently purchased (a 2004 [Mitsubushi Outlander](https://en.wikipedia.org/wiki/Mitsubishi_Outlander))

The clock in the dash didn't work, so I removed it an replaced it with a (pretty high end) nifty [magnetic compass](http://www.mauriprosailing.com/us/1-Ritchie-Explorer-Compasses/RITV57W2.html).  I knew that the compass might have accuracy problems, being so close to the radio and other electronics.  However, I wasn't expecting it to not work *at all*...it's rigid pointing north-northeast no matter which direction the car is facing.

So, suspecting the presence of a large magnetic pull somewhere near the dash, I download an magnetic sensor app to my smartphone.  The sensor seems pretty accurate when testing around the house (shoots up when held near magnets, running appliances, etc).

Using this app in my car, I discovered that not only is there a strong magnetic field near the dash....but almost the entire car seems magnetized.  I saw the magnet sensor start edging up even standing just *three or four feet* away from the vehicle....which is kind of alarming, given that magnetic attraction decreases exponentially.

Here's what I found with the sensor, which measures in µT (microteslas?).  Standing around the house or outside, it normalizes around **40 µT**.  (I assume this ambient reading mostly comes from the phone itself).  Here's what it looks like around no real magnetic fields: [Screenshot of Android app](https://lh3.ggpht.com/ZSI5lFXRvBTSlL6y6YAhwe_V5TJF0OKAYjlx3BB6wrZPkqxlc4Mx1LuUPpcD1sv7srjf=h900-rw)

Testing all around and inside my other cars, it stays nominal (~30-50µT) unless held almost directly on things like the hood above the battery, or right on top of the gas tank.  So this leads me to believe that cars shouldn't generally exhibit significant magnetic fields.

**But here are the readings around the 2004 Outlander:**

Anywhere inside the large trunk area:  130 to 200 µT  (note- the sensor maxes out at 200)

Backseats, chest level:  50-60 µT

Backseat floorboards: 50-60 µT

Frontseats, chest level: 90-100 µT

Frontseat floorboards: 200 (max) µT

Anywhere near (within 4 inches)  the dashboard: 180-200 (max) µT 

Car roof, inside or out, held 4 inches away:  100-150 µT

Under the hood: Varies, but never under 100 µT, and usually stays at ~200 µT

Walking around the perimeter of the car, within 2 feet: Varies, but usually around 100-150 µT.  Shoots way up near certain components, like door handles and taillights.

All of these measurements were taken with the car ***off and not running***.
-------------------

So...it seems like the car generally has a magnetic field inside and out of well over 100 µT, except the curious dead-spot in the backseats, and shoots to god-knows-what near certain things like the dash, roof, engine, and front floorboards.

Finally, my questions are:

1. **Are there any potential health risks for long term exposure** driving this car, assuming my dinky free android app is at all a reliable indicator?  I don't want to sound like the crazy brother in Better Call Saul, but seriously that's weird to see a sensor shoot to max in some places where you will be sitting for hours at a time, when it doesn't even go anywhere near that high near a running microwave or within 6 inches of a 4" ceramic magnetic plate (both of which I tested on).

2.  **Is there a feasible way to degauss the car?**  Maybe a silly question, but could I build or buy some kind of hand held degausser and run it over the most magnetic seeming areas and hope it might work?  Something like [this](http://www.eiwellspring.org/tech/Degausser.htm), or [this] (http://www.amazon.com/Waldom-Degaussing-Coil-Color-Power/dp/B00011UYJU/ref=sr_1_4?ie=UTF8&qid=1436701208&sr=8-4&keywords=degausser&pebp=1436701210821&perid=1090ZPG4SRWV2E2QBPF7).  Could these harm anything else in the car?

3. **Could the magnetic fields inside this car potentially affect data drives?** If I transport a computer, say, could the hard drives be wiped or corrupted?

4.  **Any idea what could be causing this**, or might have magnetized the car in the past?  As I said, it is a recent used purchase.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 8dvxiu ===
SUBREDDIT: r/skeptic
DATUM: 2018-04-21  SCORE: 522  REACTIES: 91
TITEL: There's no proof acupuncture helps relieve pain so taxpayer shouldn't foot bill
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dxqvhx0] (score 44, diepte 0) proof isn't the right word. 
There is no good evidence is what it should say
[dxqo9cr] (score 33, diepte 0) Facts don't matter anymore.
[dxqxmfn] (score 26, diepte 2) I am in utterly no way supporting alt med. I was just commenting cause it's a pet peve of mine how people throw the word proof around
[dxqojs3] (score 24, diepte 0) placebo works
[dxqxe4a] (score 16, diepte 1) Then let’s pay for m&ms instead of acupuncture.
[dxqrh7w] (score 15, diepte 1) As a matter of fact they don't.
[dxqrte1] (score 11, diepte 2) here you can see placebo working
[dxqtdma] (score 11, diepte 1) [No.](http://edzardernst.com/2016/07/acupuncture-found-to-be-pointless/)

Edzard is *the* leading authority when it comes to research on alternative medicine, and his conclusion from the wall of text I linked to above is:

>Acupuncture has been studied for decades and the evidence that it can provide clinical benefits continues to be weak and inconsistent. There is no longer any justification for more studies. There is already enough evidence to confidently conclude that acupuncture doesn’t work. It is merely a theatrical placebo based on pre-scientific myths.   All health care providers who accept that they should base their treatments on scientific evidence whenever credible evidence is available, but who still include acupuncture as part of their health interventions, should seriously revise their practice.  There is no place for acupuncture in Medicine.
[dxqtt3b] (score 11, diepte 1) That is not the case. 

Trial after trial has dismantled every claim of acupuncture. 

Acupuncture works by interacting with meridian lines of the body? Nope. There's a bunch of trials showing that it doesn't matter where they put the needles, the effects are the same. 

Acupuncture works because the needles are inserted into the body? Nope. There's a bunch of trials comparing acupuncture to the person not inserting needles at all, but instead, for instance, poking then adhering needles to the body. 

Steve Novella has gone over the research for acupuncture many times. Here's one of the most recent ones. 

https://sciencebasedmedicine.org/false-claims-for-acupuncture/
[dxr6ktf] (score 11, diepte 0) As a chronic pain patient and a sceptic there's something I'd like to point out.

Chronic pain is incredibly hard to treat, and the programme I did they a hospital taught us that if something works for you and isn't actually doing you damage, continue it.

Chiropractic I'm very much against because the risk to benifit ratio is way off.

Acupuncture or dry needling however has very little risk of performed with sterile tools.

I've never tried it myself, but I probably will at some point. I don't think it will do much for me but for the sake of feeling any relief I'd go in with an open mind.

There are definite psychological components to chronic pain and it's treatment. The placebo effect can be extremely effective if you find a way of triggering it. Even if acupuncture is just an elaborate ceremony that results in the central nervous system reducing the alert level it could be effective for pain.
[dxqubpl] (score 10, diepte 5) As brief as I can make the placebo (summarizing the article may be hard) without (hopefully) misleading: So over the course of any condition there are peaks and troughs in the status of a patient (feel better at the peaks, worse at the troughs). The placebo effect that most try to use to validate this sort of thing, as there are multiple placebo effects, is when the appearance of a peak happens to coincide with the taking of the placebo in a trial. So the effect is due to random chance and cannot be "harnessed" in any way. Additionally, people try to ascribe a "mind over matter" thing to it. Whereas you can train your mind to *ignore* the symptoms of a condition your body, when measured, still shows predictable damage.
[dxqthi0] (score 8, diepte 3) So not joking, and not understanding placebo.

https://sciencebasedmedicine.org/is-harnessing-the-power-of-placebo-worthwhile-to-treat-anything/
[dxrahsk] (score 8, diepte 2) You have to charge a lot for those M&Ms to increase the placebo effect. I'm not even kidding, the greater effort and cost associated with a placebo treatment seems to be a big factor in the perception of effectiveness.
[dxri06w] (score 8, diepte 7) > Then you might as well be a Calvinist Christian demanding his/her way to psychological well-being on people.



What the? That makes no sense. What part of “I don’t want my tax dollars spent on things that aren’t proven to work” don’t you understand?


I don’t want homeopathy using my tax dollars either. Same deal.


If they want to waste their money, let them go to an acupuncturer.
[dxqtct5] (score 7, diepte 2) Does placebo work sometimes? yes.
[dxr69oj] (score 7, diepte 3) If you expect to see a connection when X, and then there's no connection at X at the expected time frame, this absence of evidence is indeed evidence that the connection is absent. If there are little to no studies proving a link here, I think it's fair to say that the absence of evidence is evidence of the absence.

Edit: connect to connection
[dxqrbe9] (score 6, diepte 1) I can't tell if you are joking or not so I'm going to ask; you joking?
[dxqs7t7] (score 6, diepte 3) Yes, and it's foolish of them to do that (and shows a fundamental misunderstanding of the placebo effect). But that still doesn't answer my question whether s/he was joking.
[dxr18hh] (score 6, diepte 5) Placebo controlled trials aren’t there to test interventions or drugs against the ‘power of the placebo.’ 

Rather the placebo is used to show what the likely biases and errors in testing are and to help control for them. 

This is very different from what the general public tend to perceive as placebo.
[dxrsi6r] (score 6, diepte 2) So even though it provides relief to someone living in constant pain you don't want them to have affordable access to it?
[dxrho7m] (score 5, diepte 5) If something can’t stand the rest of science, I dont want it offered as a health benefit on tax dollars.
[dxrsmx5] (score 5, diepte 4) I mean that's objectively wrong. Relief can't be measured in some scale. If a person who's suffering says it brings them relief, it brings them relief and there's plenty of people who say this brings them relief.

It might only be a placebo effect, but given how much chronic pain is based in central nervous system responses which can be heavily influenced by our stress levels, why is it not believable that some people might find relief from this process?
[dxrsxde] (score 5, diepte 6) If it helps people avoid more expensive medications it could potentially reduce costs associated with their care.

I said in my original comment it should be about risk and reward. If it's low risk and provides relief it seems reasonable to me. As long as it's not being sold as something that is not, like a cure for herniated discs or CRPS all on it's own, but chronic pain treatment is holistic by nature, and not in the wooey sense.

Pain clinics are allied health services incorporating medical doctors and medicines, physio, psychology, occupational therapy, as a start. The pain programme I did through a state funded hospital even included Tai Chi classes. Not because they believed in any energy flow or anything like that, but because they've found positive responses to it from pain patients.

Also I'm pretty sure I've been clear that I believe any benefit from acupuncture is probably the placebo effect, but if there's a safe method of reliably triggering it why is that a problem?
[dxqwitx] (score 4, diepte 6) Hmm I'll have to read the article, thanks. I have a painful chronic condition that frequently flares and wanes. There are so many factors like sleep, diet and stress that seem to influence my symptoms. Untangling what triggers and what helps continues to be the hardest part of managing this disease for me, even after a decade of careful medically-supervised trial and error.
[dxrflw4] (score 4, diepte 7) Testing can be hard. Even harder when you have a limited sample size and a delayed response. I fix computer systems for a living, and sometimes it is really hard to know if an action fixed a problem, or it fixed itself. "I uninstalled this program and rebooted, now it is faster" is it faster because I uninstalled the program, or because I rebooted, or maybe it isn't actually faster, as I wasnt timing anything with a stop watch. That's a pretty controlled test, compared to all the complications of living life. It doesn't surprise me that it is hard for you to find the source of your trouble.

That's a double edged sword, because people often mistake non-sense with what made them feel better, when it could have been a million things, including time.
[dxre65h] (score 4, diepte 6) Exactly. Thanks.
[dxrn811] (score 4, diepte 3) [The above link provided](https://sciencebasedmedicine.org/is-harnessing-the-power-of-placebo-worthwhile-to-treat-anything/) by /u/theBuddhaofGaming is very helpful:

>Unfortunately, none of this has stopped what Steve Novella refers to as the “placebo narrative” from insinuating itself into lay discussions of medicine. That narrative proclaims in breathless terms (as Steve put it) the “surprising power of the placebo effect” without putting it into reasonable perspective or even really defining what is meant by “placebo effect.” First, as we have tried to explain time and time again here, **there is no single “placebo effect.” There are placebo effects. Second, the only really correct reference to “the placebo response” or “placebo effect” is the outcome measured in the placebo arm of a clinical trial. The problem is that, all too often, discussions of placebo responses conflate the placebo effect measured in a clinical trial with all the other various placebo effects that add up to the response that is measured in that trial. Those effects include reporting biases, researcher biases, regression to the mean, conditioning,** and many other components that contribute to what is measured in the outcome of a clinical trial. Another common misconception about placebo effects is that they are somehow “mind over matter,” that we can heal ourselves (or at least reduce our symptoms) through the power of will and mind. This is not true. Placebo effects are not the power of positive thinking.
[dxrdy53] (score 4, diepte 3) However proof of the absence  of evidence is. And many alt meds have been tested and failed. Including acupuncture.
[dxredw5] (score 4, diepte 3) Plenty of doctors prescribe totally useless treatments. They’re no different than anyone else. They are discouraged  by the fact that  they have no traditional medical treatments and so resort to alt treatments because “why not - can’t hurt”. Of course they don’t realize it does hurt - people think these alt treatments have medical usefulness. 

Doctors are not scientists or researchers.
[dxrmu74] (score 4, diepte 7) Should we be spending tax dollars on phrenology? If a "doctor" opened a phrenology clinic would you support tax dollars being spent there?
[dxrkenc] (score 3, diepte 2) Um....... no, placebo is not statistics. The placebo effect is a direct, dramatic medical result. I think you may be confused, because your semantics policing is just a touch off.

edit: the more I reread this the more puzzled I feel. Yes, the placebo effect does work. A placebo is a term for a physical object or treatment administered, and is not a statistic. When I was getting my psych degree I read far too many studies that use placebos. I promise a placebo is an actual phenomenon and physical process, and not simply a statistical term.
[dxqsszr] (score 3, diepte 1) **Fascia**

A fascia (, ; plural fasciae ; adjective fascial; from Latin: "band") is a band or sheet of connective tissue, primarily collagen, beneath the skin that attaches, stabilizes, encloses, and separates muscles and other internal organs. Fascia is classified by layer, as superficial fascia, deep fascia, and visceral or parietal fascia, or by its function and anatomical location.

Like ligaments, aponeuroses, and tendons, fascia is made up of fibrous connective tissue containing closely packed bundles of collagen fibers oriented in a wavy pattern parallel to the direction of pull. Fascia is consequently flexible and able to resist great unidirectional tension forces until the wavy pattern of fibers has been straightened out by the pulling force.

***

^[ [^PM](https://www.reddit.com/message/compose?to=kittens_from_space) ^| [^Exclude ^me](https://reddit.com/message/compose?to=WikiTextBot&message=Excludeme&subject=Excludeme) ^| [^Exclude ^from ^subreddit](https://np.reddit.com/r/skeptic/about/banned) ^| [^FAQ ^/ ^Information](https://np.reddit.com/r/WikiTextBot/wiki/index) ^| [^Source](https://github.com/kittenswolf/WikiTextBot)   ^]
^Downvote ^to ^remove ^| ^v0.28
[dxuepmm] (score 3, diepte 4) You didn't argue that though, do you have an argument for that claim?
[dxrr9yp] (score 3, diepte 3) Why are you wrong? No evidence of a treatment effect means you can say things like "we can't detect a difference between this treatment and doing nothing." But does that mean there is no effect? Not necessarily. You might devise a more sensitive test in which an effect might be detected. It's this same line of thinking that means you can reject null hypotheses, but you can never accept them. You can however, fail to reject them 😉. Long way of saying, I agree with your initial statement, Wakedays.
[dxr34ys] (score 3, diepte 0) I have something done off and on that is proven to work (at least I thought).   I was told it was called dry needling but when I looked that up its not exactly what they do.  I had spinal fusion and got back pain.  I also have just a ball of muscle that formed where the worst scoliosis is and where the bar is.  They insert acupuncture needle but it has barbs on the end.    They twist the fashia and it causes huge spasms that leave me sore for days but then the ball of muscle gets a lot better.  I thought this was the only acupuncture ever proven but now I can't even find online what it is called (since when I look up dry needling they have no barbs).  So..... Maybe I'm an idiot?
[dxrhgbs] (score 3, diepte 3) We’re talking about acupuncture. Sure you can make the argument that we need to look after the homeless before this, but that isn’t what we’re here to talk about.


Acupuncture doesn’t work and I don’t want to pay for it with my tax dollars.
[dxrhm9r] (score 3, diepte 4) If it gives people in a hopeless situation a modicum of comfort, then I do want to pay for it, and I think you are selfish (in this area, anyway.  Of course I don't know you).  To the polls!
[dxrzplc] (score 3, diepte 8) Because at least with acupuncture they are getting what they ask for. You don't have to lie to them about it and it can still potentially work for them
[dxqruig] (score 2, diepte 3) Very Poe. Much confused.
[dxr8ii3] (score 2, diepte 6) Interesting! I haven't heard this about placebos. I've always heard that they can actually cause a real-world effect.

But then you said otherwise, and I looked into it myself, and yeah, recent research suggests that may not be the case.

I'm curious if the same may be true of nocebos though.
[dxtrw5h] (score 2, diepte 3) Alternative medicine, even if just placebo,can be really positive, especially on terminal cases.
[dxyftwb] (score 2, diepte 5) Yes they are evidence - just a very low form of it. No amount of anecdotes manifest into a "fact', but they are still information that can lead you to truths, so they are evidence.
[dxr8uar] (score 2, diepte 1) Well, skeptics can sometimes start to look down on people that fall for scams. It's tempting to do that, since you "know" better. But people who fall for scams are not idiots. Some very intelligent people commit fallacies and some very intelligent people fall for scams. It's even harder when people you know, trust, and love make recommendations. On top of that, the people who sell snake oil are often convinced themselves that their remedies work. Hell, I admit that I've been suckered before. In my case, it was a street hustler who convinced me to part with $50 out of generosity.

I don't know if you've fallen for a scam, as I haven't looked into it. But be careful.
[dxrea6l] (score 2, diepte 1) Not acupuncture. More likely some kind of counterirritant treatment. Same mechanism as using capsaicin to irritate nerves which blocks pain caused by muscular or skeletal issues. 

Or like physical therapy - deep tissue massage which has some effectiveness.
[dxrfc7e] (score 2, diepte 1) > Even if acupuncture is just an elaborate ceremony that results in the central nervous system reducing the alert level it could be effective for pain.


This isn’t reason enough for us to foot the bill.
[dxrpys7] (score 2, diepte 9) What does phrenology have to do with sugar water? Phrenology used to be all of those things, an established institution from the product of a high culture, and it is no longer because it was lambasted and not tolerated. You are correct, it is no different from sending someone to a pastor, and I would not support tax dollars going to a pastor for the purposes of medical healing.

So here is a hypothetical: if I, (with the specific intention of bilking a bunch of rubes) were to get phrenology established again and get a whole bunch of people supporting it enough that I could activate the placebo effect equal to or greater than acupuncture in my patients would you support me then being able to receive money from the government? What if now I genuinely believe the bullshit I am peddling, if I get my thing (in this example phrenology) as established as acupuncture do I then get to start making money off of it from the government? Should scientologists be able to bill the government for audit sessions?
[dxrro62] (score 2, diepte 10) Well argued.  I'm not compelled that acupuncture is equal in bullshit to phrenology, but more importantly, I'm reluctant to take away something from those who are suffering chronic pain when know real alternative exists.  There's little research to support massages, either, but I'm not opposed to them being on the menu for therapy either.
[dxrss6r] (score 2, diepte 5) It’s not acupuncture, it’d be the placebo effect. We shouldn’t have to pay for something that does nothing. Imagine how wide the net would be if you included every twig, herb and rock that relieves pain?
[dxyg40m] (score 2, diepte 1) Studies have actually shown that the placebo effect is higher when the people actually know about the placebo. 

It’s mostly related to the common medical knowledge that when medical professionals care about you the outcomes is more positive. 

So the treatment itself is worthless (and it should be since that’s what a placebo means) but the results are from the very act of being in a study. 

You’d have done better by getting some therapy. 

Of course about 75% of all back pain resolved itself so again you wasted your money, you supported someone who’s treatments are worthless.
[dxrycsv] (score 2, diepte 0) Anyone I speak to who is pro AP says it has been proved to work. When I point out that most studies say, "..it has been proved to be work... at about the same level as placebo", they say that means it works.
[dxqs2pn] (score 1, diepte 2) It’s not even uncommon for doctors to prescribe placebo and for insurance to pay for it.  However, they often don’t pay for things where either the  evidence is weak or the mechanism of action is unknown.
(40 reacties met lagere score weggelaten)

=== THREAD wvjshm ===
SUBREDDIT: r/army
DATUM: 2022-08-23  SCORE: 20  REACTIES: 62
TITEL: What are the best shoes for running?
POST (source_id=post):
Been thinking about this and I assume some Joe’s would like to know. 

When you run you want good support and cushioning. If you have flat feet you want arch support and maybe inserts. 

If you have wide feet, which I didn’t know was a thing till the army. Get wide shoes. 

Right now I think the Endorphin Speed 3’s by Saucony are fantastic. Saves your knees with a little compression and they lace up great. I have them in 10.5 wides. Great shoe. What you wearing?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ilfnzqh] (score 24, diepte 0) Super dependent on your running style and arch. I got run form and feet analyzed and a dedicated run shop and the shoes they recommended me did wonders. I personally use the Brooks Adrenaline GTS 22 if I'm going for time, and the Brooks Beast if I'm going for endurance or just want to run.
[ilfq8fq] (score 17, diepte 0) I got a pair of nike zoomx vaporfly next %. They cost a pretty penny and ngl they are some of the most uncomfortable shoes for just wearing or walking around in but I immediately got faster run times when I put them on. They have a carbon fiber plate in the sole, which makes them feel extra "springy". 

I don't wear them for every run though. I have some regular nikes I wear on most run days. When I train with regular shoes I have to work harder to maintain the same pace. So, when I put the next% shoes back on I can usually push my pace a little faster than before.
[ilft9mw] (score 12, diepte 0) Find a running specialty store. One name I know of is Fleet Feet. Don’t know where you are but Google will be your friend.  A good store will take the time to help you out. Good running shoes aren’t cheap but they shouldn’t cost you an arm & a leg as well.
[ilfn3ei] (score 10, diepte 0) The best running shoes I've ever owned were made by a Swiss company called On. I got them at a running store, and I've never felt better in a pair of shoes before. They aren't cheap, mine were $110 I think, but my runs aren't terrible for me anymore so it's worth the money.
[ilfneut] (score 10, diepte 0) [Hoka Bondi series](https://www.hoka.com/en/us/mens-road/bondi-8/1123202.html)
[ilg68eg] (score 10, diepte 0) Heelys
[ilfxvkb] (score 9, diepte 1) I went from 13:20 to 12:40 two mile time in one day by buying these shoes. Made me feel young again.  

Definitely not an every day shoe though.
[ilfzxa1] (score 9, diepte 0) I swear by Hokas. They’re light and comfortable. Little pricey, but I also believe you should never go cheap quality on shoes if you plan to use them a lot.
[ilfpxxc] (score 7, diepte 1) I second getting your form analyzed at a run shop. It took me 5 minutes, it was free, and it significantly improved my running form. 

Brooks are also great shoes, I use them as well.
[ilg80de] (score 7, diepte 0) White shoes make you run faster
[ilgdovu] (score 7, diepte 0) TLDR: Build a rotation of at least 2 shoes. Insoles help a ton. Go to a store where they scan your foot, and see what they offer.

What has saved my plantar fasciitis was investing in a good pair of insoles, typically not cheap but I love my Currex runs. I just interchange them to whatever I’m going to run with. Now I have a few, and even have those or super feet in my boots too.

As for shoes it’s dependent on so many things. Gait, foot strike, do you under/over pronate(meaning what kind of support you may need), going fast or slow, etc…. I think having a shoe rotation of at least 2 shoes, but optimally 3 is best. Why? Because if you wear the same shoes for everything you kill them much faster. With wear and tear, and the impact absorption - gotta let the shoe recover as well. 

Daily trainer - Ol’ reliable. For those everyday miles, where you can pickup the pace, or slow it down a bit if you need to. Need to be comfy, and take a beating since you’ll use the shit out of them. Your workhorse shoe.

Recovery shoe - Having a slow and steady shoe, for those long or easy days to save the legs is important. Also gives time for your daily trainer to breathe and recover. 

(Bonus) Speed/tempo - For your tempo and all out runs. There are daily trainers that can do both fine, but as some stated in earlier comments like a mention of the Nike ZoomX Vaporfly Next %, those are fast shoes. It’s not easy going slow in something that propels you forward with a carbon plate in it. Will definitely shave off some of your run time, and the energy return is greatly improved so you can go faster easier essentially.

Type in “Running store” in google or Yelp and call the places around you to ask if they do a foot analysis. You go there and sometimes walk on a fancy biometric scanner or run on a treadmill, sometimes both. Then based on your foot arch, and how you land, they’ll suggest shoes for you. Great place to start.

If you’re lost for what kind of shoes you’d buy this dude Seth James Demoor on YouTube is nuts and runs in all sorts of stuff. He does in-depth reviews of running shoes, but he is biased towards loving lightweight shoes. 

[https://runrepeat.com](https://runrepeat.com) this is a great site to see what runners are saying about shoes.

Also buy good socks lol. More of a comfort thing, but it can matter. A soldier is nothing without healthy feet. Just like when you slapped on those fox river or darn toughs and your boots felt 10x better the first time, same applies for good running socks. Shocker! 

I don’t know if you give a shit but here’s my rotation: 
Daily - Hoka Mach 4, Saucony Speed 1/2. 
Recovery - Nike Invincible Run 1, Saucony Triumph 19
Speed - I just use my Hoka or Speeds since I can pick it up in either, but I can pick it up faster in the Speeds because of the nylon rocker that’s built in.
[ilg5ht1] (score 6, diepte 0) I'm a fan of ASICS. Used them since basic training.
[ilg33le] (score 5, diepte 0) My feet hurt and hokas make them not hurt.
[ilgey97] (score 4, diepte 1) This is the way. There really isn’t a “best” pair of running shoes, but there is a pair that is “best” for your foot type and training goals. Any specialty store should be able to help you out. I go to a fleet feet in Minneapolis, they’re legit.
[ilg4nwj] (score 3, diepte 1) Bondi 7’s 🤌🏽 for the flat footed peeps
[ilfn6ya] (score 2, diepte 1 OP) Mine were around that too but it’s worth it. And they’re quality.
[ilfwdqb] (score 2, diepte 1) My fav shoes were also Ons, but in a model they only made once and in one color. I have had 5 other pairs from them and they all suck. The design on the bottom is so egregiously stupid, too, if you ever run on rocky paths or gravel. 

I’m in my second pair of Brooks Hyperion Tempo and they are a fast, light, neutral trainer. I’m not running anything more than 5-6 miles right now, though, and have a grand total of zero foot problems so this kind of shoe works for for me.
[ilfo73s] (score 2, diepte 1 OP) That’s a great point you bring up. Endurance running vs hauling balls   

I love a good say hi to the neighbors run.
[ilgnobb] (score 2, diepte 1) These shoes are so good that they are super controversial in long distance running.
[ilh0jc3] (score 2, diepte 1) This. Go to a running store and bring your old shoes with you. They will have you do some tests and look at your old shoes to find the best one for you.
[ilfvn2s] (score 2, diepte 0) What most people don’t know is running shoes have different technology for different foot types. What works for one may not work for another.

As everyone else said, go to a run specialty store for an analysis. Then try on different models. Be prepared; a good pair of running shoes is usually $100+.
[ilhsh2y] (score 2, diepte 1) I second that, my go to is the Solstice XT, short fast runs I will use the Vanish.  They really fucked up when they went away from the original version of the ONE, I suppose the Torin replaced the OneV3, but I haven't tried that shoe yet.
[ilj178j] (score 2, diepte 2) Is it worth buying the Vanish, considering the steep price ?
[ilga7mz] (score 2, diepte 0) Like others have said, go to a running store for gait analysis. When you find a shoe or shoes that work for you, check out Zapppos.com. Prices are better, shipping is free, return shipping is free, they have a 10% mil discount off all items (including sale) and they ship to APOs. 
Also note that brands change their styles. So the Brooks Ghost 15 may be a completely different shoe than the 13 and 14. 
We have been consistent Brooks customers for years. Saucony does a nice mix of springy and support. I bounce between the two brands.
[ilgctvu] (score 2, diepte 0) Check out HOKAs. They're lightweight and designed to help with proper running form. I'm going to get myself a pair of them soon, and I've heard nothing but good things about them.
[ilim51o] (score 2, diepte 1) If you have legit plantar fasciitis you can get really nice custom orthotics made free of charge. Life changing.
[ilgxa35] (score 2, diepte 0) AF1s and yeezy’s
[ilgxvg3] (score 2, diepte 1 OP) Give me two perrr I need two perrrrr
[ilh1tx4] (score 2, diepte 0) I can concur on the endorphins speed 3, they’re god tier and definitely helped me on time.
[ilh855x] (score 2, diepte 0) Saucony Jazz or Shadows so you don't look like a dork like everyone else.  No one looks good in running shoes.
[ilhi3iw] (score 2, diepte 2) > Sarah Underwood

Who's that?  Is that all she's going to be wearing?
[ilhj5xc] (score 2, diepte 4) It's nice that she was in Playboy
[ilhpna2] (score 2, diepte 0) Hoka challengers
[ilihl6n] (score 2, diepte 0) I like my Brooks
[iljd5tu] (score 1, diepte 1) Huh. Neat. I'll have to find a place near Campbell like this. My old ass needs every bit of help to ease running stress on these bones.
[ilgijmy] (score 1, diepte 1) The only shoes I will use when I wanna run like the wind.
[ilfvpay] (score 1, diepte 0) For me hoka has been my go too. Heard great thing about ON. Brooks as well their toe box doesnt work for my toes. I have wide feet and have a knee with some mileage. Hokas help me still run a 14min acft
[ilfwvk8] (score 1, diepte 0) Shoes that fit your feet and are meant for running. Don't skimp on some cheap shit.
[ilfxz3c] (score 1, diepte 0) I hate shoes other people love, and love shoes other people hate. The best thing for me (and you) is going to a specialty running store, having a thorough assessment, and then trying them on. Don’t buy based on color or price. I’ve wasted so much money that way… go based on your needs.
[ilfynxn] (score 1, diepte 0) I have a bunch of shoes for different situations. 
Currently in the mix: Nike ZoomX Vaporfly Next%, Saucony Endorphin Speeds, Hoka Speed Goats, Hoka Mach 4, and Hoka Bondi.
[ilhhecn] (score 1, diepte 1) This. Bondi all day
[ilg0smb] (score 1, diepte 0) Go to fleet feet and have them do an analysis. It’s free and game changing
[ilg7sbs] (score 1, diepte 0) Running shoes' best kept secret. Altras Torin (Not Ultras, but Altras)
[iljbkjj] (score 1, diepte 3) I think so, since I really use for shorter fast runs or speedwork, and those only account for about 5 to 10 percent of my total mileage so they don't get used all too much. I do like how thin the sole is and it's a good reminder for when your footstrikes starts to get lazy.
[iljc72x] (score 1, diepte 4) You have me convinced. Will get one before the Army ten miler.
[iliulo5] (score 1, diepte 2) Yeah I got them. Mine weren’t great though. They had me stand in a box with sand for the mold, and I got these orthotics that were OK. My wife got to go to a private practice where they had her feet scanned, and hers were made with carbon fiber and cork they seemed amazing lol. Mine are OK for standing, but certainly not for running :/ 

I’m trying to get some from a private practice with a scanner, where’d you get yours? Also, do you use them to run?
[iliwb92] (score 1, diepte 3) Ahhh, I got mine in recruiting so I was referee to a private practice. Probably a much better product than from Fort Wherever.
[ilntoq5] (score 1, diepte 2) You can get a prescription for insoles and have them filled at the brace shop in the base hospital. The kind they use here are pinnacle power steps and they are very good.
[ilgej2a] (score 1, diepte 0) Hoka Hoka Hoka Hoka. 
 I’ve ran my entire life, TF and XC in college and I swear by Hoka.
[ilgk1ur] (score 1, diepte 0) It all depends on the individual, I'd recommend going to the nearest Fleet Feet or other professional *running* shoe store (not just a normal shoe store) and ask them for advice.
[ilgv6lz] (score 1, diepte 0) I feel a lot better running in barefoot shoes (not the toe shoes, but the minimal type). I feel like I get shin splints more often when I have a set of regular runners on. I've never done a crazy long run in barefoots though, so I've only got a limited use case.
[ilh05gw] (score 1, diepte 0) Feet
[ilhgv5f] (score 1, diepte 1 OP) Not even Sarah Underwood?
[ilhimoq] (score 1, diepte 3 OP) Sarah Jean Underwood can make shoes look fantastic. She’s a smokeshow.
[ilhd6cy] (score 1, diepte 0) I used to be a distance runner but I always really liked Nike free run not sure if you can find a color in regs, and just your basic ASICS work well too if your in pts.
[ili9asp] (score 1, diepte 0) Brooks are pretty damn good for running
[iliglse] (score 1, diepte 0) New Balance have always done well for me. Asics have as well. You just want to make sure that you’re replacing them often enough so that you don’t harm your feet or your run time.
[ilihgps] (score 1, diepte 0) Me and my brother are both in and have the same feet problems with running, flat feet and I get shin splints like crazy, after testing out shoes I found nike Pegasus 39 to work wonders
[ililssf] (score 1, diepte 0) I don’t run in them, but I just started wearing Hoka’s at wrok(ICU nurse) and they are the best things I’ve ever had on my feet. I went to a specialty running store with gait analysis. If you can find something like that around you, it’s the way.
[iljxaix] (score 1, diepte 0) Brooks and hoka. Just find a store that actually looks at your foot and how you land
[ilh8mkb] (score 0, diepte 0) Well, it’s probably got a lot to do with too many people can’t run correctly to begin with. Myself included. 😂

Heel striking ruins legs.
[ilg5u9z] (score -2, diepte 1) Hoka is just a big hunk of EVA. It feels good at first, but it’s heavy and wears out quickly.

