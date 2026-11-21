# Label-batch batch_0105

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
Schrijf het resultaat naar `batch_0105.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: u9n5dp, 1apr8av, 5xxeh2).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD u9n5dp ===
SUBREDDIT: r/solotravel
DATUM: 2022-04-22  SCORE: 53  REACTIES: 114
TITEL: So I messed up: stinky feet, and am looking for advice
POST (source_id=post):
I'm on day 5 of a 19 day first-time onebag trip in Europe and I only brought one pair of shoes.

I don't typically walk as much as I have in the past few days and my feet, and shoes, are starting to stink. I've had this issue in the past but it's been a few years since and i didn't bring another pair of shoes because I was concerned about the space another pair of shoes would take up. Realizing i should've just kicked something else out but that's for next time.

It's not like a life ending issue but I am staying in hostels and don't want to stink up the rooms, esp as it gets worse, plus i just don't like it when my feet and shoes stink. Thankfully they're not too bad yet and I have the room to myself.

I'm planning on buying another pair of shoes in the morning and changing out socks and shoes around the middle of each day so neither pair gets used up too much, prob get back to the hostel and wash and dry my feet before i change them out. 

Probably buying more socks. I've seen people rec merino socks but not sure where I'll find some in Athens, near the Acropolis if anybody has any recommendations.

Prob gonna search for new insoles as well.

Just clipped my nails and gonna clip more frequently.

When I get back, I'll prob put all my shoes and socks through whatever cleaning recommendations I can find, so would happily take those as well 

Any other tips for better shoes/feet care and helping with current shoe stink?

Edit: To update, 

* got some sandals
* went to like 10+ stores and i did find ankle merino wool socks in one, but they were itchy and stiff and I've always heard merino is supposed to be amazingly soft and not itchy, so held off. 
* did find some bamboo socks so got some of those, esp since they were <€5
* Got anti fungal cream 
* Got bar soap since easier to clean with it than body wash
* Talcum powder
* new insoles
* Literally nowhere had gold bond but did see Scholl powder in a pharmacy early on, so going to head back there and see if it's for shoes
* Airing my shoes out now, washed my feet, bout to apply anti fungal, and using sandals for the next few days

Going to next city late tonight so I'll see if i can find new shoes over there. Aired my old shoes out last night and by the morning, they didn't stink, so hoping they are salvageable, even if after the trip.

Thanks for all the advice!! I'm reading through all the comments, just might take me a bit

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i5sivxv] (score 78, diepte 0) Do you wear socks? Did the shoes get wet (and what was your plan if the shoes did get wet...)?

Do you wash your actual feet every day with soap?

Go to the grocery store and buy baking soda. It's a natural odor absorbent.
[i5sizt0] (score 45, diepte 0) You must eliminate the source of the smell: bacteria. 

They are "eating" your sweat and converting it into a smelly substance.

So basically keep a strict hygiene regime regarding your shoes/socks and feet. 

Wash your socks and shoes with low-temperature disinfectant detergent and switch to Merino.

And wash your feet daily.
[i5srnos] (score 32, diepte 1) Ditto on the baking soda, dump some in your shoes overnight and they'll smell a lot better in the morning.
[i5slpju] (score 17, diepte 1 OP) Yes, i always wear socks. Yes, wash them everyday. Didn't plan for shoes getting wet, but should've.

Thanks I'll look for some baking soda
[i5sosfh] (score 17, diepte 0) Thank you for being aware of the issue. New shoes are probably a good idea. I remember being so embarrassed being out with shoes I kept near a litterbox when I could hear random people comment about it. I was just desensitized to the smell by thay point
[i5ti3eb] (score 12, diepte 2) Hostel front desk should be able to point you to a laundromat
[i5sn8xw] (score 11, diepte 0) Gold bond or similar antibacterial powder and an anti-fungal foot spray.

In the beginning, use it A LOT. Spray your bare feet every couple hours and pour 1 tablespoon of powder into each shoe (don't need to measure - guessing is close enough).

It can take a lot of applications to reverse especially since you're actively using them. 

That will cut down on new bacteria. Your shoes will still stink but only from close up. They shouldn't "radiate" stink that fills a whole room. 

If you don't have access to the above, another option is white vinegar + spray bottle. At the end of the day, saturate the hell out of them, inside and out. Reapply every couple hours in the evening and let dry overnight.
[i5smury] (score 10, diepte 0) I put cat litter in a tied sock and leave it in my shoes overnight. It really helps. Off brand litter from a supermarket is only a couple of euro.
[i5ssbd8] (score 10, diepte 0) I'm going to give you totally different advice - buy another pair of shoes and at least a few pair of socks. Its Athens - they have clothing stores.  Alternate wearing the new shoes with the pair you've brought. If the socks start to smell, throw them away. If an extra pair of shoes absolutely won't fit inside your onebag, than get a mesh bag (like a laundry bag) and a carabiner from a sporting goods store and clip them to the outside.   
 Unfortunately If your shoes/socks smell, there isn't a lot of mitigation you can do in-situ other than let them dry out and rest. There is *one* Hail Mary - if you can wrap the shoes in an airtight plastic bag and keep them in a freezer overnight, that will kill the smell for a bit, but you'll be without shoes for the night and it really has to be overnight - a few hours won't do anything. 

Another tip - I go out of my way to buy antimicrobial underwear, undershirts, and socks for travel, ESPECIALLY one bag travel. All it takes is one gross cotton t-shirt to make your entire bag stink.  
If you somehow find yourself back at the hostel and your shoes and socks are stinking, at least wrap them in a plastic shopping bag and bury them in your bag so they don't stink up the rest of the place.
[i5sm11r] (score 7, diepte 1 OP) I looked for a public place to clean clothes and haven't seen one nearby, but I'll check again. Do wash them daily but think I'm going to wash them like twice a day with once in th middle of the day for extra care
[i5tfb9m] (score 7, diepte 1) Tea tree oil is fantastic for treating fungal issues.  A little goes a long way. If you can, dilute it a bit with a carrier oil or lotion. If you can find tea tree soap, use that for your feet only and treat after with oil or antifungal spray or cream.
[i5slow2] (score 6, diepte 0) You have to soak your feet in salt water and wash. Apply antifungal foot spray or use antifungal essential oils.
[i5t3aim] (score 6, diepte 0) don’t switch shoes while wearing the same socks. you’ll just transfer the bacteria to the other shoes and create the same problem. if you find out how to kill the odor in the first pair pls let me know, I have the same problem with my work shoes lol.
[i5sscac] (score 5, diepte 0) When you lather soap on your feet, don't rinse it off immediately - leave it on for a a couple of minutes. Think of it as pre-soaking clothes or dishes - it takes some time for the detergent to loosen all the dirt and bacteria. Oh, and don't forget to lather between your toes. Once you're rinsing it off with water, use your hands to rub/wipe every area again. Mind you, soap works mechanically, not chemically.

Make sure that your feet, socks and shoes are completely dry before putting them on. Bacteria love humidity.

There shouldn't be any need for using anti-bacterial soap by the way, at least in the long run, as it also kills any good bacteria on your skin and thus make it easier for germs to multiply since your skin won't have it's own microbes to defend itself.

If you're wearing cotton socks then absolutely wash them on hot (60° celsius), and use vinegar instead of fabric softener to rinse. Vinegar neutralizes odours and doesn't leave a chemical residue that can, in my opinion, make bacteria multiply and smell worse. If you're using synthetic sport socks then don't ruin them with hot water, but please use sportswear detergent, which neutralizes odours and keeps your sportswear breathable. And no fabric softener, maybe some vinegar. Summer walking/running sneakers from a sportswear shop are meant for letting sweat out (they will have tiny holes in them), same goes for summer hiking boots from outdoor shops. If the weather's warm enough then why not buy a pair of hiking sandals or basic flip flops?
[i5uqlwl] (score 4, diepte 2) Are you using clothes/shoes with a lot of plastic? Like a 20% wool 80% plastic stretch mix? 

They turn into smell bombs in no time.

There's a reason why they are extremely unpopular among hikers and they are willed to pay a lot of money for merino.

You can start with merino socks. They aren't that expensive.
[i5t3i70] (score 4, diepte 1 OP) I've heard cat litter in the past but gonna try finding antifungal/ cleaning stuff first. If i don't, I'll get the cat litter. Thanks for the out of the box recommendation
[i5srmar] (score 4, diepte 0) Bamboo socks.
You'll never go back!
[i5sk991] (score 3, diepte 0) Talcum powder
[i5sksnn] (score 3, diepte 0) Powder spray. Wash your feet well, spray the hell out of the insides or your shoes. Wash your socks, spray your socks with the spray before putting them on. Spray inside the shoe before putting them on.

I had a similar issue when I had to take my shoes off at the airport they stunk the high heaven for the next couple days and I ended up just quickly going to a store and buying some powder spray. I'm sure there's some version of that in whatever country you're in.
[i5tftpc] (score 3, diepte 2) Try deodorant spray(preferred) or stick if you can't find gold bond stuff.
[i5t3w72] (score 3, diepte 1 OP) It's been an issue in the past and with all the extra work the shoes are doing now, I've been trying to stay conscious of it. 

And same, was super embarrassed cause id been desensitized to it when it got mentioned to me
[i5t2tuh] (score 3, diepte 1 OP) Yeah, i messed up on the socks. Got one pair of smartwool and the rest did say anti-odor and whatnot but guess they aren't that good.

I think I'm going to get a pair of sandals first and use those for the next few days to let my feet breathe for a bit before getting a new pair of shoes and more socks. Also, let my current shoes breathe and try some of the stuff here.

Don't want to toss the socks just yet, but I did bring Ziploc bags so going to lock the stinky socks in there and throw them to the bottom of my bag.
[i5t70uf] (score 3, diepte 2) hah I was going to suggest sandals, but I know they're not for everyone. Smartwool socks are the best - even if you had only one other pair, you could probably swap between the two the rest of the trip and be fine. I'm certain Athens has a sporting goods store that would have merino socks, although I don't know about the language barrier. An alternative idea - see if Amazon delivers to your hostel or a hostel in the future? Or see if someone back home could ship you a pair to somewhere on your trip?
[i5ssq6j] (score 3, diepte 0) Use higher quality shoes, change socks, wash your feet with water at least once during the day (just make sure they're dry afterwards). That should be it.  


A short anecdote:

When I went on my first solo trip at the age of 19, I thought it would be a good idea to save space in my backpack by not bringing any socks at all. A true backpacker can do without such things. So, I walked around without socks in a pair of the cheapest sneakers I could find.  
After a few days there was a squishy sound with every step i took, from the sweat and dirt in my shoes. A week in, I got scolded by a train conductor ('Please, put on your shoes. The smell...') and found that someone had put them in the garden of the hostel where I was staying.  
At that point, it was too late for socks - those sneakers had gotten a permanent smell of decaying animal carcass to them.  
I went to the nearest outdoor shop and bought a pair of nice sandals instead. They saved the trip both for me and for other people along the way.
[i5t65zc] (score 3, diepte 0) I have suffered with stinky feet and travelling for years..  So many people said change your socks, shoes, wash them etc etc, nothing ever worked. Not even a little bit. Still soaking wet stinky feet every day.


Now I live in Australia.. I haven't worn shoes for a long time. And I forgot all about my stinky feet..

Sandals, flip flops, bare feet. Are the only things that ever helped
[i5t6x6y] (score 3, diepte 0) I had stink foot SO BAD! I had to Leave my shoes outside and wash my feet on entering the every night for years. Then I put absorbine jr. on my feet every night for 3 nights… cured. Basically forever. Try it.
[i5tlcdv] (score 3, diepte 0) I wash my socks hot so all the bacteria is dead. Clean shoes from the inside. When my feet get sweaty they get wet, but not very smelly. Maybe that helps
[i5tu8ku] (score 3, diepte 0) You are in Greece?  Go buy a nice pair of Birkenstocks and let those dogs breathe
[i5uqcte] (score 3, diepte 0) Wool socks. 

I have really sweaty feet and when I wore cotton or polyester socks in the past, my feet STANK. Now, I only wear wool (Darn tough) and alpaca (Pacas) socks and they hardly stink. I can wear the same socks 2 days in a row and it'll be fine. Absolute game changer for me.
[i5uti7e] (score 3, diepte 0) Merino socks that’s the answer
[i5ux6fs] (score 2, diepte 3 OP) Not crazy expensive but hard to find in my experience. I'm going to see if my next hostel accepts packages and have some shipped there
[i5uyx46] (score 2, diepte 4) Have a look at Amazon and coordinate it with your hostel/hotel.

They have a lot of Merio stuff. Take care that the clothes are having a high percentage of Merino (Icebreaker, etc.).
[i5uzdoj] (score 2, diepte 6) Can speak for Smartwool and Icebreaker. Good stuff. But expensive as shite.

They will solve a lot of your problems.
[i5smowo] (score 2, diepte 1 OP) I'll prob rent a hotel room to soak because can't really in the hostel. Def will when I get home. 

I'll keep an eye out for antifungal spray/oils, thank you
[i5uk5fj] (score 2, diepte 2) It's been years but one time I bought a bucket because I was staying at a hostel but I needed to soak my feet in Epsom salt.
[i5uxe6e] (score 2, diepte 2 OP) Next time I go to a pharmacy/super, I'll keep an eye out for some. Thank you
[i5sn5sv] (score 2, diepte 0) Disinfectant spray for inside your shoes. Rotating shoes every second day, but carrying a second pair of socks for change during the day. 

Throughly washing and drying your feet morning and night. You could get a pack of baby wipes to keep on your bag if you want to do them middle of the day, too.
[i5t8zz0] (score 2, diepte 2) Good luck we live and we learn
[i5sqon7] (score 2, diepte 0) Baby powder
[i5srydg] (score 2, diepte 0) Use anti bacterial gel or hand sanitizer on your feet.
[i5t79ii] (score 2, diepte 2) You won’t need to do it daily, try once or maybe twice a week. I used to use it as a deodorant if I forgot to apply at home. I kept a bit in my desk. The stuff is made to kill bacteria, it works really well for that.
[i5t2dpx] (score 2, diepte 1 OP) These are actually pretty nice walking shoes so I'm annoyed at myself with possibly messing them up.

That is kinda horrifying tho lol. I do have multiple socks and am washing my feet daily but i think it's mostly wearing shoes for like 12+ hours while walking a ton and i do have a history of it. 

Gonna wash and dry my feet better though

Might get a pair of sandals first, thanks for the idea, and then the second pair of shoes a bit later. Let my feet breathe better during the day for a few days, avoid killing more socks and shoes, and try some of the remedies here on my shoes and feet over the next few days.
[i5t4e49] (score 2, diepte 1 OP) I'm planning on finding some sandals tomorrow to avoid killing a new pair of shoes lol.

I have in the past but don't remember exactly how. I'm going to thoroughly clean these when i get home, document the process, and hopefully that does it. Lol, I'll let you know if it kills the smell.
[i5t963i] (score 2, diepte 2) What kind of shoes are they? Anything similar to tennis shoes or light hikers should be fine to just put through the washing machine on a relatively gentle cycle (with a little bit of care to ensure the laces don't get tangled).  Air dry or dry in the dryer with bulky items like a full load of towels.
[i5uyvw4] (score 2, diepte 2) There's a lovely sandal place in Athens that custom makes sandals to your feet! Cant remember the name tho rn.
[i5uze7k] (score 2, diepte 3 OP) Darn, I'm leaving soon anyways, so prob wouldn't have had time to wait for them to get made
[i5t3rcd] (score 2, diepte 0) Additionally take the sole of your shoes out overnight, learned that in basic training with boots.

If they get wet buy a newspaper, Ball a few pages up and push them into the shoes. Change the paper once or twice.
[i5t5sc0] (score 2, diepte 0) Soak your feet in black tea
[i5t6fz9] (score 2, diepte 0) Try to hang your shoes up so they can dry fully at night, or put them on a rack so they get some air circulation. Fill them up with baking soda at night and then shake it out into the sink in the morning. 

Washing your feet obsessively during the day isn't going to fix this, I don't think. A second pair would help a lot.
[i5t91i2] (score 2, diepte 0) Use deodorant in your shoes and on your feet
[i5uyqho] (score 2, diepte 1 OP) Hadnt thought to use deodorant, but if current methods don't work, I'll try it out.
[i5thvgf] (score 2, diepte 0) From experience- leave your shoes outside the sleeping room either hanging from a window or outside in the hall (nobody sleeps there so less minding the smell). Shower as soon as you get in and switch to shower shoes for the evening. You can also buy gold bond and sprinkle it in your shoes but that works over time, and the above is the immediate solution. I agree with other commenters, switch out and buy socks frequently.
[i5tiek7] (score 2, diepte 0) I was traveling with my friends through Amsterdam, Brussels, and Frankfurt. We get to our hotel in Amsterdam after one day of travel and are greeted to an awful smell after a while, after investigation we realized it was friend L’s shoes. Thankfully we had a window that overlooked a small roof. Those shoes stayed outside at night! After days of walking and exploring it was time to leave, L decided it was best to just throw her shoes away in Germany before leaving and exposing a whole airplane to the stench. She did have a pair of flip flops though. 
If you are prone to sweaty feet like L she found that changing socks often, changing insoles and gold bond/ baby powder sprinkled in her helpful. Unfortunately like you we had to found out the hard way.
[i5tokjy] (score 2, diepte 0) Lysol the shoes, get new socks, get an anti fungal for your feet. Always wear sock with closed shoes.
[i5tub53] (score 2, diepte 0) Keep dryer sheets in your shoes while not being worn. Will help with the smell.
[i5u2o2y] (score 2, diepte 0) wool socks or even a wool blend will help so much. get the stink out of the shoes first - baking soda overnight will do the trick, and new insoles if that doesn’t work, then only wear wool socks on clean feet. i swear, i can have the nastiest sweatiest feet ever, but my shoes won’t smell at all. i think wool is naturally antibacterial or something, it works miracles! like i said though, make sure your shoes are clean and stink-free before you put your new wool socks in - give them the best chances to work, lol
[i5uy84t] (score 2, diepte 1 OP) Def going to try more merino wool socks when i get home. That's been one of the main recommendations
(57 reacties met lagere score weggelaten)

=== THREAD 1apr8av ===
SUBREDDIT: r/solotravel
DATUM: 2024-02-13  SCORE: 64  REACTIES: 114
TITEL: Getting cold feet
POST (source_id=post):
21f here. I'm planning on going to Japan in summer after I've finished university. I've always been quite sheltered but my dream has always been to travel. Finally I'll be free and able to do what I want, but I've been speaking to people about it and they've kind of scared me a little. One of my co-workers said it's crazy that I'm going to the other side of the world by myself and that it would be so scary for him. I know I'm not him, but I'm also an introvert and not that confident. That's what I'm hoping travelling will help, because if not now, when? But I can't help feeling as though I'm being stupid and naive. Another thing people have said is that by going alone I won't be able to share the experience with anyone and so it feels pointless. I can be easily swayed so these things have been getting in my head. Any advice or reassurance?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kq86nqx] (score 267, diepte 0) People who don't travel give terrible advice about traveling, and people who are scared to be alone give terrible advice about traveling alone. So, don't get too caught up in what those people say.

However, when traveling alone it's inevitable that sometimes you will second-guess yourself and experience some insecurities and self doubts, so try to see it as a chance to practice having healthy coping mechanisms for those self doubts.
[kq8hlfw] (score 64, diepte 0) Japan is a very safe country. You have little to worry about. Go and enjoy yourself. It's a good place to pick for a first trip.
[kq8zj3c] (score 35, diepte 0) 21f here. I'm planning on going to Japan in summer after I've finished university.

A: Congrats

 I've always been quite sheltered but my dream has always been to travel. Finally I'll be free and able to do what I want, but I've been speaking to people about it and they've kind of scared me a little. One of my co-workers said it's crazy that I'm going to the other side of the world by myself and that it would be so scary for him. 

A: Your co-worker is wrong - its super safe and easy to travel to Japan as a solo female. Make sure you download: google maps / google translate Japan (offline) / google lens (you take a picture of a word etc and it'll translate for you. Also download Navitime for navigation too

I know I'm not him, but I'm also an introvert and not that confident. That's what I'm hoping travelling will help, because if not now, when?

A: It's easier to travel when you are younger and regret kills dreams. So do it now. Plus the exchange rate from USD to Yen is really great right now. 

 But I can't help feeling as though I'm being stupid and naive. Another thing people have said is that by going alone I won't be able to share the experience with anyone and so it feels pointless.

A: There are local meet up groups or if you stay a hostel ; you can make friends and plans

 I can be easily swayed so these things have been getting in my head. Any advice or reassurance?

A:  Do your research, make a plan, take action. Also, don't try to cram so so much in one day. Focus on the top things you want to do first.
[kq879wd] (score 28, diepte 0) I was stupid and naive, an introvert and not that confident when I went on my first overseas trip in my early 20s. And I had a blast! 

(i am still also many of those things)

 Plenty of people had opinions on me bumbling off alone to the other side of the world, and it's only worth listening to those people who HAVE actually travelled.
[kq8azvu] (score 27, diepte 1 OP) Yeah that’s true. I’ll work on coping and hopefully feel better about it as it approaches
[kq8ywju] (score 21, diepte 2) Can you do a smaller solo trip before going to Japan?
[kq8jxyj] (score 18, diepte 0) Those are typical responses from people who have zero travel experience (I'm not talking about all inclusives or cruises). Don't be scared, Japan is likely one of the best places for first timer, extremely safe and people are helpful. And for the most part, you can get by with English in tourist spots. Transportation can seem a little daunting at first, but everyone is very helpful.
[kq9hmc6] (score 17, diepte 4) For being on the other side of the world, Japan is pretty traveler friendly from what I've heard! It's as good a place to start as any and if you're excited to visit it, that makes it the best place to get started! 

It will sometimes be scary and overwhelming, but I believe you can do it.  I was a very sheltered young adult and still felt "young" compared to my peers when I was done with uni, but I've been solo traveling on multiple continents now and I love it! 

It'll definitely be a learning experience, but I believe you'll have an amazing time. 

Realistically, you will probably run into some challenges so just know that and be prepared to roll with it and you'll be fine! Some things that helped my anxiety was always having a back up portable phone charger, some cash in both currencies, and figuring out the time difference to find a good time to call home every day. 

Good luck!
[kq9zvv2] (score 15, diepte 1) Exactly! My coworker
With no passport Said “I can’t believe you can’t flush the toilet paper In costa rica”.
Sir. STFU.  

I am not hear to absorb the ignorance of people who have never traveled.
[kqa4dlr] (score 15, diepte 1) Might just be the best place for solo travel lol
[kq9tb6t] (score 13, diepte 2) Also OP I am a woman and have travelled to just under 60 countries and been solo in over half of those 30 - once you're there its fine and it's genuinely a very liberating experience being able to do wherever you want. 


I went to Japan last year and it's genuinely the safest place I've ever been in my life - so clean, transport is extremely efficient and there's well-located affordable accommodation in all cities. You'll have a blast, it's an incredible place.
[kq9jku5] (score 12, diepte 0) One thing I’ll add: expect to be lonely. Loneliness is not a sign of failure. I met a lot of young travelers who think if they’re not meeting lifelong friends or having intense social connections then they’re “not good” at solo travel. 
Traveling can be lonely, especially in foreign countries. Embrace the loneliness, as it’s an essential part of the journey. It’s often an important reason folks like me enjoy solo travel rather than traveling with a companion.
[kq8b6ek] (score 10, diepte 1 OP) That’s comforting! You’re right, taking advice from people with no experience is pointless, you don’t know until you try. Thank you!
[kq9dm7p] (score 10, diepte 1) Also be prepared to carry your trash with you all day until you get back to your accomodation, because there are very few public bins.
[kq9artd] (score 10, diepte 0) People just tell you their own thoughts and fears, but that doesn't make them true for you. 

Everytime (even the first time) i traveled by myself i've met people on the first day. I've shared experiences with a lot of people and made some good friends while at it. None of them were people that i knew before. 

As for safety, the other side of the world is not that far. You should measure distance in flight duration, not in meters. A 14 hour flight away from home sounds fairly close, it's less than a day.
[kq9lqto] (score 9, diepte 0) If I listened to peoples opinion at home I never would’ve left the US. 

Coincidentally, the places people told me were most dangerous were my favorite and where I felt safest. 

Don’t take advice from anyone who hasn’t been to the area your going recently. 

You’ll never know if you enjoy solo traveling without giving it a real try.

Japan will be absolutely awesome!
[kq9ejfr] (score 8, diepte 3 OP) I was thinking about it but I’m on a budget so would have to lower it for Japan if I did this.
[kqazu9i] (score 8, diepte 1) Know you’ll make some mistakes (wrong train, wrong line-up, social faux-pas) and that is okay. Whenever I made a mistake people kindly corrected me.

Regarding clothes in the heat: I’ve been to Japan solo female several times, and didn’t realize until my last trip that some of my clothing choices were less than socially appropriate in a busy urban area (tank top, short shorts). As a middle aged woman, I was just aware that I was the only person in a crowd dressed that way. As a woman in your early 20’s, you might get a different response. Definitely recommend watching a bunch of YouTube videos - even if it just people wandering japan in the summer - to get an idea of the vibe.
[kqbe809] (score 7, diepte 3) This. Japan is a reasonable starter country for the newby in that it is safe and knowable. By knowable I mean you can find out everything you need to know and plan on it. Everything has a timetable and an acknowledged way to accomplish something. Prices are set and you aren’t left wondering if you’ve been had. Japanese people will help you and are super polite. They are quite concerned about embarrassing themselves due to their English but usually someone will be willing and able to translate a bit.

Other countries like India and China can be very different.
[kq9fc55] (score 7, diepte 1 OP) whoa. you just opened my eyes, 14 hours does sound like nothing in the grand scheme. thank you! and exactly, I’ll meet new people and make like minded friends
[kqb03eh] (score 7, diepte 1) And if you’re not lonely traveling solo, that’s okay too! I’m a huge introvert and find it blissful to have few interactions.
[kq9chvt] (score 6, diepte 0) I'll address the two specific points raised by the people you've been talking to:

**1.**

 Japan is so freakin' safe it is ridiculous.  Of course nothing is completely without risk, but it is extremely likely that you are less safe where you live right now than you will be in Japan.  I don't know where you live, but traveling to Japan will likely *increase* your safety.

**2.**

I can't quite figure out what the second person is saying.  Are they saying that you have to have someone with you to enjoy any experience?  Because that is just ludicrous.  

Or are they saying that *after* the experience you want to be able to talk about the experience with someone else that was there?  If this is what they mean, they are likely the same age as you.  When you are 21, your friends have been your friends for a large fraction of your life.  You think they will be your friends forever.  But the reality is, you will drift away from most of your friends as you travel through life.  Of course you make new friends.  This isn't a bad thing.  It is just reality.  

The chances that you can travel with someone at the age of 21 and then still have them in your life to reminisce when you are 50 are pretty damn small. 

If the person telling you this is significantly older than you, they are probably hoping you will get married in the next couple years, and want you to put off travel until you are married so you can enjoy traveling with someone else....then they will come up with a reason you should put it off until after you have kids...and then they will say you have to save up for your kids education and your house mortgage before you should travel.....and then they will say you should save up for retirement before you travel....and then they will say you shouldn't travel because you are old and what if you have health problems while you are away!

I had an interesting realization while raising kids with my wife.  I had certain experiences in my childhood that were really important parts of my childhood.  My wife had different experiences in her childhood that were really important parts of her childhood.  As we were raising our kids, we would each be trying to recreate those great experiences for our kids.  When ever we would talk and make plans for our kids, and one of us felt strongly about doing something and the other person just didn't see the importance of that thing, we would ask if that was something the other person did as a kid.  For example it was important to me that we went camping.  My wife didn't understand why.  It was important to my wife that we went skiing.  I didn't understand why.  But then we came to understand that we were each just trying to recreate our own childhoods for our kids.

What is the point of this ramble?

If someone is giving you advice, they are giving that advice from their own experiences.  If they are content with their life, they are basically telling you to do the same things they did.  

So if you are talking to someone who hasn't traveled, and they are giving you advice about an upcoming trip you are planning, it will pretty much *always* be bad advice.  In their mind, they never traveled.  Their life is good.  Therefore there is no point to travel.  In their mind there is no upside to travel and only downside.

Never listen to advice about travel from someone who doesn't travel.
[kq9d8zw] (score 6, diepte 0) Don't listen to that feedback, the reason they say it because they could not imagine traveling by themselves.  I've traveled to Japan, I wholeheartedly encourage you to go, and here's a few things that'll hopefully make you feel better:

1) Japan is one of the top safest countries in the world.  Seriously, I saw little girls riding the train at night by themselves without a worry in the air.  Now, this doesn't mean that you shouldn't watch your back, you should always be looking out for yourself, but seriously this is a safe country.

2) One of the observations that I had in Japan is that the Japanese culture actually kind of cater to the lone introverts.  Some restaurants will have the single booths with dividers, and you have everything you need at that booth.  Water, soy sauce, utensils, condiments, even a place to charge your phone.  Whether it's meant for the lone businessman to take his lunch, I dunno, but I saw this more than a few times.  It's also common for the locals to buy their single lunch / dinner at the train stations, and take them home to go.  

3) I've been to Japan multiple times, explored much of it on my own, and feel like there's still more to explore.  I rarely felt awkward or out of place as I visited shrines, temples, museums, parks, etc.  I did have the luxury of going to Izakayas with some friends at the end of the day though, but I think you'll be fine.  Enjoy as much as you can, but keep in mind that you could be back again some day.  Take pictures all the time of the beautiful scenery, the shrines and temples, and be sure to share with your friends / family afterwards so that they understand just how beautiful it is.

4) Getting around Japan is surprisingly easy for the English speakerwith little to no Japanese.  Google maps will tell you which train / bus platform to go to, which train, what time, and the signs will be in English at the stations.  They get lots of English tourists, and they are prepared for them.

5) I recommend doing it now, assuming that this isn't getting in the way of your work or education, and that you can afford it.  There is something freeing about solo travel, and it really helps give you some perspective on the rest of the world, and I think it makes someone wiser.  Maybe it sounds cheesy, but you'll never know until you try it.

If you need any tips for getting around Japan, check out the JapanTravelTips sub, lots of useful info posted every day.  Feel free to also ask me any questions if you want.  I have a cheat sheet of the top 20 or so Japanese phrases that I needed to get around, before I would use google translate, which was surprisingly rare.
[kq8xyq5] (score 5, diepte 0) Don't let people put you off because of distance, it's immaterial, a new country is a new country. Japan is a very easy country to travel in, it's very "westernised" in that it's modern and efficient but at the same time offers an entirely different culture and cuisine. Locals are exceptionally friendly, you only have to look at a map and already someone is offering to help. It's very safe.
[kq9ao8r] (score 5, diepte 0) Just do it. You’ll most likely really enjoy it. If you don’t you’ll just regret it anyway
[kq9g5sn] (score 5, diepte 0) Do it. Behave responsibly and you will be fine. Japan is a safe, developed country. My first solo trip did wonders for my self-confidence. Not everyone will be interested in your experiences but you will meet people and connect with them. It will be an enriching experience and you will be better off for it.
[kq9hk1x] (score 5, diepte 0) "Another thing people have said is that by going alone I won't be able to share the experience with anyone and so it feels pointless."  


That's so much BS. The joy of travelling solo is that you get to do and see what *you* want, 100% of the time, and what's more to the point than that? And I love "sharing" my experiences on my Facebook updates - my friends tell me that when I'm on a trip they'll check my page every day, to look at my pics and see what I'm doing.   


Confidence is learned. You never develop it if you don't push outside your comfort zone, and it's obvious that "everyone" never has.  Japan is a safe, easy and oh-so-interesting place to travel solo, a prefect pick for a first trip. You're going to have the best time.
[kq9nsxq] (score 5, diepte 0) Don't listen to that person. Your trip will literally be life changing. It will give you a new perspective that is impossible to get otherwise. Traveling by yourself is extremely rewarding and refreshing. You will grow as a person trying to figure out various situations. You may only get a few of these opportunities in your lifetime so take it while you can.
[kq96e82] (score 4, diepte 0) > but I'm also an introvert and not that confident. That's what I'm hoping travelling will help, because if not now, when? But I can't help feeling as though I'm being stupid and naive.


You're right, you aren't him. Seems like the concept of doing this on your own is cool enough for you that you booked the trip. Keep in mind, most people are afraid to go to a restaurant by themselves. So the prospect of travelling anywhere, be it near or far, is intimidating to a lot of people. And who knows, maybe you'll find out solo travel isn't for you. But you've got a dope trip planned out knowing you're going solo (Japan is awesome, by the way), so you've obviously put some thought into it already. Just don't let other people's insecurity about doing something alone influence. Go to Japan. Have a great time.



> Another thing people have said is that by going alone I won't be able to share the experience with anyone and so it feels pointless. 


Not to sound harsh, but fuck anyone that has told you this. Anyone in this sub that's done any solo travel can tell you it's complete nonsense.
[kqce8ch] (score 3, diepte 2) I think you picked the right country. I have hear Japan is exceptionally safe
[kqcw2tb] (score 3, diepte 1) This 100%, to non travellers it's akin to explaining why you love a sports team if they don't hate sports, they just won't get it.

I have solo traveled (as a man), and it's been awesome. Sometimes there's a twinge of loneliness, but it then just opens you up to meeting others. Looking back now, I really enjoyed the freedom and I think Japan is a great start!
(90 reacties met lagere score weggelaten)

=== THREAD 5xxeh2 ===
SUBREDDIT: r/solotravel
DATUM: 2017-03-07  SCORE: 63  REACTIES: 103
TITEL: Having cold feet...after waiting for my first solo trip for 3 months, I am having doubts...about to cancel the trip
POST (source_id=post):
My itinerary is:

Florence 12-17
Cinque Terre 17-20
Pisa/Lucca 20-21
Lisbon  21-27

Did all the research, reserved Airbnb/hostels and planned what I am going to visit and when. Trip seems to be balance between art/culture/hiking/and just relaxing.

However, now that I am getting closer to the actual travel date,   I am starting to have cold feet...making excuses that the weather might not be good, what if I get robbed, get injured while hiking...all kind of weird things as if traveling with friends would eliminate these unfortunate events. I am comfortable socially, also value personal time and space...However, being it my first solo travel is freaking the hell out of me. I am close to the point of just canceling the trip even though airfare and most reservations are nonrefundable. 

Any fellow solo traveler got into the same situation before your first trip alone? 

********************************

Update 1: Thank you all for the support. I have read all the comments and private messages I received, took notes and will follow recommendations. This is my packing list as a first update:

https://www.reddit.com/r/solotravel/comments/5yhtr8/my_packing_list_for_2_weeks_in_italyportugalthank/?st=j02w5w7o&sh=5fae2a7c

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dellxju] (score 208, diepte 0) Even if you do end up getting robbed and injured *and* the weather is bad on your trip (which is extremely unlikely to happen), you will definitely regret it more if you choose not to go at all. That is a promise.
[delq4fw] (score 42, diepte 0) I'm a 58 year old woman and I didn't do solo overseas travel until two years ago. Now I've been a lot of places. It is scary the first time. But, once you do it once, then the whole world opens up to you and you know you can go almost anywhere alone. I just got back from three months in India and Nepal. Don't wait unti you are 58.
[delllly] (score 22, diepte 0) I'm leaving for my first solo trip April 2. Haven't thought of cancelling it, but I think nerves about being robbed/injured/sick are pretty normal.

I traveled quite a bit in western Europe 5-6 years ago and I can tell you if you haven't been to the places on your itinerary they're all amazing. Lisbon is one of my favorite trips. Amazing food, great cheap hostels, active nightlife, beautiful architecture, ocean, parks. 

You've already paid the money and at one point you really wanted to go to these places so why not go and see what your curiosity was about? The weather might be crappy, you probably wont get robbed or injured but get travel insurance just in case and go have the time of your life!
[dem0jnk] (score 20, diepte 1) In 2 hours im going home after 4 months in guatemala\mexico dont cancel, please.  You'll learn alot and do this again.
[delq1gh] (score 14, diepte 0) DO NOT CANCEL! For real. I'm a 26 year old female and just got back from a 10.5 month solo backpacking trip. I travelled on a tight budget so I did mainly couchsurfing for accommodation and in some circumstances I even used Tinder to find a host. The worse thing that happened to me was losing my phone in Bali, and my credit card in La Spezia (nearest town to Cinque Terre). But both of those were replaceable. I've met someone who was robbed with a machete, people who lost their passport or had their laptop stolen. But even then, their trips were worth it. And chances are nothing bad will happen. I went to places like Paris and Barcelona and London and never got pick pocketed. Went to Bali and Bangkok and Malaysia and never had someone try to grab my purse and run. The places you are going to are low level crime areas, and if you are aware of your surroundings you are going to be fine! What you'll get out of this trip will be so worth the plunge. Get out there, see the world, try new foods, talk to the locals. Take it from a girl who walked around mafia run Naples at 3am, who didn't have a place to stay some nights till midnight, who relied on the hospitality of strangers. Everything will be fine. You're going to have an amazing trip and in the end it will be one of the best decisions you've made.
[dellpad] (score 13, diepte 1 OP) Thank you very much. Travel insurance is something I have not thought about.
[delm2wa] (score 10, diepte 0) Take a deep breath. If you're from the US, these places are undoubtedly safer than America. You aren't going to Mongolia, you're going to be in Europe and people will always be close by if you need help. Most people you encounter will have at least basic understanding of English. 

If you cancel, you're going to spend *years* regretting it. Not very many people travel to a different country on their own. It's a pretty big deal. You're going to learn a few things about yourself. You're going to learn a few things about humanity. 

After the trip is over you're going to look back and laugh about your worries. Take a deep breath and let yourself enjoy it.
[delmfa0] (score 10, diepte 0) I'm only 19 and started my first trip to SEA 6 weeks ago. I felt horrible leaving and the pressure of going to university overwhelmed me. I was honestly very close to just missing my flight and turning around. I went through with it though, hated my first day(I was in a hotel) but ever since that I have loved it. I already have extended my trip 4 months to the end of august. Stay in good hostels and you will have a blast. Worst situation: you waste two weeks of your life. Best situation: you have the time of your life. It's a low risk high reward opportunity
[delzh7n] (score 8, diepte 4) There's also really practical things you can do like have photocopies of your passport... one in your big bag, one in your everyday carry bag. Don't carry too much cash at one time, pay extra for an additional bank card and have one on you and one in your bag. Keep one of those little tiny strappy bags under your clothes... etc etc. I took every single precaution and didn't need any of it but man it made me feel safe and comfortable and have a lot more fun!!
[delmhmm] (score 8, diepte 0) I'm leaving on my first solo trip and I couldn't be thinking more the opposite. I can't wait for it to get here. 

But I think you would probably regret it if you didn't go.  You could end up loving it and going on a solo trip again.
[delpze0] (score 7, diepte 2) Definitely think about it! Check your credit card (that you used to buy air tickets?) for possible insurance, as well as work benefits, if you have it. Supplementing that with medical and travel insurance is recommended. Like World Nomads.
[delvr7n] (score 7, diepte 2) I didn't get travel insurance,  and I'm currently banned from the UK until I pony up the 2000 pounds I owe them for emergency room bills.
[dellzwq] (score 7, diepte 0) Hey man! The places you've mentioned seem really amazing. I'd say, just be aware of where you are and follow general safety precautions and you will be fine! First solo trips are always a little scary, but once you land in the place, you are going to love it! Research the places well based on your interests and have a great time there! Also if you stay in hostels, you get to meet other travelers! Good luck and have fun!
[delyxmd] (score 7, diepte 1) As someone whose husband and kids went to a place called Moron in **Mongolia** when my kids were 13 and 9 years old, I'd say that even Mongolia is a great place to visit.  Hardly anyone spoke English, and my family certainly didn't speak Mongolian and couldn't read the Cyrillic letters, but they still managed to have the trip of a lifetime.

Go.  Embrace.  Enjoy.  Please give us an update when you get back.  Good luck.
[delp13y] (score 7, diepte 0) Hey! Other than echoing what others have already said about you regretting it if you don't go-- I feel you on the anxiety thing. What was helpful for me for my first solo trip was getting a SIM card once I got to my destination so I could have internet wherever I went. That way, I could feel safe and assured in the ability to Google and plan and research things on the fly, and because I talk to my friends is much via texting apps already, I never felt alone because I could just share and live blog my experiences and reactions to a chat window. Also, you can ask a friend or family member to periodically check in on you via Find Friends or another location tracking app-- that plus letting people know where you are/what you're doing will free you from the fear that you'll just sort of disappear or that people won't know and find you if something happens. Have fun! It's an amazing, liberating experience to travel alone. You got this.
[delyt67] (score 7, diepte 0) DONT CANCEL. I am a drunk dude right now I think cancelling would be the biggest regret of your life. Yes, your worries are legitimate but as long as you are being careful you won't have any problems. trusst me on that.
[delpfj9] (score 5, diepte 1 OP) Thank you very much. I highly appreciate the encouragement from everyone here. Seems like I am overthinking it.
[deluxwb] (score 5, diepte 2) This is great advice. Staying connected will help with anxiety and help you feel safe and grounded.
[delmvp6] (score 4, diepte 2) No problem. You should journal your experience while you're there and then post a recap here when you get back
[delmjky] (score 4, diepte 0) I think you may just be getting a bit anxious in the anticipation of it all. Personally, I feel like I've been a bit anxious before a trip before, but typically either once I'm on the airplane or once I arrive it goes away. 

For me traveling is all about getting out of your comfort zone, that's my personal love of it (and meeting new people of course). I've had some stressful times in the midst of traveling, but when I look back on them now...I'm happy I have those stories.

I will tell you though if you don't do it, you'll regret it, and not just monetarily.
[delqnvc] (score 4, diepte 0) If you stay home, get robbed, lose your footing while crossing the street and get hit by a car - that would really suck.  You'll say to yourself - I could be in Italy right now.

JUST DO IT.
[delu7q2] (score 4, diepte 0) Nerves before a trip are not uncommon, especially for first time trips.

You could stay home and find the weather bad, yourself robbed or injured and having gone nowhere. 

The reward of your travel out weights the risk. You have a great itinerary. Go!
[delq7si] (score 3, diepte 2) I went with world nomads for travel insurance. Your credit card might offer insurance as well, so look into that!
[delzrp1] (score 3, diepte 3) Ouch...story time? Do you plan on going back?
[dem3r7o] (score 3, diepte 2) I would never leave the country without it.
[dem43eb] (score 3, diepte 2) yes the added peace of mind for insurance is definitely worth the money!
[delxyfr] (score 3, diepte 1) > I think nerves about being robbed/injured/sick are pretty normal.

I will also say that the first time it happens will be remarkably unremarkable in how simple it is to deal with.
[depl3fr] (score 3, diepte 3) Don't be scared of chicken buses, save yourself from the expensive tourist shuttles.
[dem0r6m] (score 3, diepte 2) That sounds interesting :D If you don't mind me asking, what did they do there?
[delnpx9] (score 3, diepte 1 OP) Yes, I see myself regretting this for the rest of my life if I don't do it.
[dem2scd] (score 3, diepte 1) Hey /u/sbay this "SIM card" tip is the shit...I'm currently sitting in the back of a cab in the middle of Bangkok, on my way to Jakarta for the next four days and I can tell you, having T-Mobile (USA) and unlimited international data (sometimes 2G, sometimes 3G or even LTE) for $10 extra a month is really helpful.

This is my (hundredth) solo trip and I'm loving every single minute of it, every single time. Started when I was 14, just taking the train in Germany and exploring or even going on a road trip to Amsterdam, has turned into flying to Shanghai, Bangkok, Mexico City for long weekend (when I was based on the west coast) or like now, traveling through Southeast Asia with a backpack and a small duffel bag for three weeks. I book hotels and hostels mixed, because I do also love my alone time, and if you meet someone you wanna bang, it's nice to be able to take them to your hotel. But hostels are where you meet the cool, adventurous, fun crowds of backpackers and solo travelers who had some of the same thoughts as you before leaving on their trips. 

Don't cancel. 

You'll regret it for the rest of your life.

If you do decide to go, let us know how it was.

P.S.: Getting SIM cards in other countries is super easy, plus SOOOO many places have free WiFi. (Not necessarily in Western Europe, but definitely in Asia)
[delrift] (score 3, diepte 0) 15 years after my first solo trip the night before any trip I'll still get a case of cold feet. I've yet to cancel a trip and have yet to have any catastrophe occur that makes me wish I hadn't gone on it. Even if something does happen (and the chances are very very low) then you'll learn something about yourself.  How will you handle the stress of being thrown off your plan? Part of traveling is getting to know yourself better, so don't think of bumps in the road as life ruiners, but as challenges to over come.  Also, you're going to have an amazing time. The best things in life are the ones that make you nervous.
[delskzg] (score 3, diepte 0) I actually got robbed (phone and wallet) and injured (toe infection) and don't regret traveling one bit. Just made for more interesting stories. Walking around a foreign city after getting robbed with a couple hundred euros in your shoe is certainly something you never forget!
[dem45my] (score 3, diepte 2) Man what are you so scared of. You could litterally walk around with your iphone 7, diamond rings and versace shoes in the shadiest areas of the city's you're going to, and nobody would touch you. Theres seriously nothing to be scared of, those places are much much safer than in the U.S. I've been to all those places you listed. you gotta chill
[deltkgu] (score 3, diepte 0) I have left my country by myself for around a month or more on five occasions. Every. Single. Time. I would start feeling the way you do about a week or two out. Just sick to my stomach and looking for a way out of it because oh my god what did I get myself into and why. And you know what? Every single time I had the time of my life, made new friends, and memories to last a lifetime.  I learned about myself and the world and came back a way better (not to mention more interesting) person. Nerves are inevitable, especially if you're a thinker and worrier like me. But I promise you you're going to have a fucking blast. There may be days where you wish you were home and are just tired and decide to just chill in your hostel or splurge on a private room to do so, but they will be far outweighed by the thrill of new sights and experiences.
[delv6vk] (score 3, diepte 0) **Get travel insurance**. I use world nomads.    
You will be fine, the trip will be amazing. I left for my first solo trip a year ago (just had my one year anniversary of travel yesterday actually) and the night I arrived in Bangkok I had a full blown anxiety attack.    
I have been robbed (pick pocketed, my cell phone), I've been in a motorbike accident and I've had my debit card skimmed. I've gotten sick and argued with fellow travellers.   
I have also proven to myself that I am capable, and that I am deserving of the fullfillment that comes from travel. I've seen things no one else has, I've camped on a sailboat under bats and stars in Australia.   
Sorry that turned into an about me; my point is that sometimes things go wrong but mostly they go better than you could have imagined. Don't cancel, you will regret it immensely.
[delvom1] (score 3, diepte 0) I was just as nervous before my first solo trip. I ended up in the emergency room overseas at 3am with kidney stones, a hostel in rome overbooked and made me sleep on a cot in the kitchen, I missed a train from Marseille to Barcelona, and I stayed at a hostel in France with no working toilet. It was an amazing adventure and I haven't stopped solo traveling since. Planning my 4th trip for may and June as we speak. All of those things you fear are unlikely to happen, but if they do happen, you'll have a story to tell,  an adventure to look back on. If you stay home, you'll only be stuck with regret.
[dem3wvm] (score 3, diepte 0) Don't cancel, if you need any help in Italy lmk.

I'm Italian living near Como, but can give you a hand if you need anything while solo in Italy. 

Cheers
[dem4tg8] (score 3, diepte 0) Ppl end up regretting the things they never did. Not the chances they took.
[dem5tmp] (score 3, diepte 0) Italy is incredible and by far my favorite country visited to date! It's just magical. As a lady in her twenties, I've visited places like Eastern Europe, Central America and Asia by myself. Of course due to my own cherished memories, I'd strongly urge you to go! 

I had apprehensions about traveling solo for safety reasons as well, so I never got drunk on solo trips and tried to minimize my traveling at night. Also, almost every time I stayed in mixed gender bedroom hostels, I'd be the only woman. nothing bad happened but I wouldn't do it again. I'd just prefer staying with other women in the future. 

Edit: and yes I always get cold feet, especially the day before. Either thoughts like, what am I doing! Or I'd get very disassociated from myself and my trip, kind of numb and not excited. Hard to explain. I get over it once I'm there!
[deniyd1] (score 3, diepte 2) So, Florence, check out this place: https://www.tripadvisor.com/Restaurant_Review-g187895-d1510081-Reviews-Trattoria_Anita-Florence_Tuscany.html

Someone on reddit told me to go there.  They studied in Florence for 6 months and said this was their favorite place.  They told me to get the "tortellini alla norcina"  Looking at my pics, it was 7.5 euro and came with free bread too.  Just look at it: http://i.imgur.com/mcamK3k.jpg

You can't say no.  The restaurant is like one block off the main strip, but just enough that you wouldn't find it unless you knew it was there.

In Cinque Terre, when in Vernazza, go here for some gelato: http://i.imgur.com/zF9hVXP.jpg

Someone said the following and they were right.  It's not ice cream, so skip the chocolate and ice cream flavors.  Get the fruit flavors as those are more fresh.  I think I got the 4 scoop, strawberry, melon, something else and lemon...which was the best.  OMG was it damn good!!!
[delrlfy] (score 2, diepte 3 OP) Will look into that..thank you.
[dem8s4o] (score 2, diepte 4) Kidney stones. I dream of going back, but I have retinitis and my travel time is limited. If I'm lucky I got another couple of years in me, so I gotta use any money I get to travel, not pay a bill.
[dem45qq] (score 2, diepte 2) lol even the robbing?!
[demd3dt] (score 2, diepte 3) You have your life. You're unlikely to lose all your stuff. You'll find a way to move onward.
[dem88j4] (score 2, diepte 1) i concur OP. and you'd see for yourself, that you can overcome anything that's thrown at you. you'd see how much a problem solver you are. (but don't overthink too much as well... i reiterate :P)
[delmfyf] (score 2, diepte 1 OP) Thank you very much...this is really helpful.
[delodqf] (score 2, diepte 0) i just did Florence, Cinque Terre, Pisa and multiple other Italian destinations solo. DO IT
[delor04] (score 2, diepte 2) weather was overcast but Florence was nice when i was there. maybe a little cold but barely. It rained a bit for me in Rome and in Milan, those got a little chilly.
(55 reacties met lagere score weggelaten)

