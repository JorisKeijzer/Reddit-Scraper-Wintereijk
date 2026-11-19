# Label-batch batch_0085

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
Schrijf het resultaat naar `batch_0085.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 161hp7y, 1jj1edg, 1cafhjq).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 161hp7y ===
SUBREDDIT: r/BuyItForLife
DATUM: 2023-08-26  SCORE: 34  REACTIES: 82
TITEL: If you're looking for flip flops...buy Archies.
POST (source_id=post):
I am ROUGH on flip flops. And wear them TONS. I wear them in winter, summer, spring, fall. If I'm not in my flip flops, I'm either barefoot or at the gym. In spring 2022, I bought a pair of Archies flip flops, and they are the most durable flip flops I've ever owned. They are all 1 piece, so there is no separation at the toe or strap connections. What I'm most amazed by is the tread durability. I mostly wear them on gravel, blacktop, dirt, in my garden, at the lake, etc. And there's nearly no wear on the bottom of the shoe. They have decent arch support too. The real kicker is they supported me through my first pregnancy too- so they had even more weight to support. You can also throw them into the washing machine to get them squeaky clean again!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jxsufby] (score 34, diepte 0) Does this read like an advertisement to anyone else?
[jxt6a4v] (score 17, diepte 1) It does, but [post here](https://reddit.com/r/midcenturymodern/s/VbDy8mURDa) does show they are wearing them.
[jxtpl1a] (score 9, diepte 1 OP) Hahah it totally does read like an ad but I promise I'm being honest- I just love them so much. I saw someone's post here looking for sandal recommendations, and wanted to recommend these, but they weren't sandals- so I made my own post.
[jxvhrta] (score 7, diepte 3 OP) Let's look at rule #1 again... "products made to last that won't necessarily last a lifetime are accepted"
[jxtpnfl] (score 6, diepte 2 OP) Nice sleuthing 😂 I seriously wear them constantly
[jxs4qfv] (score 4, diepte 1 OP) See I've tried those, and chacos- really hated them. I think I hated the leather because it gets grimey and stinkyy
[jxs7keo] (score 4, diepte 0) Just ordered a pair in women's 10. I'm usually 9.5
[jxs4bn9] (score 3, diepte 0) Rainbow flip flops will last 10 years. The leather ones that is.
[jxs5hso] (score 3, diepte 0) Did you use their sizing system when you ordered?  I usually buy mine a little bigger to accommodate by wide Fred flinstone feet
[jxs6rnq] (score 3, diepte 1 OP) I usually wear a women's 10.5 but I got a women's 11
[jxs9p0m] (score 3, diepte 1 OP) Hope you like them as much as i do!
[jxscr2y] (score 3, diepte 0) Okabashi is my go to sandal. American made and recyclable.
[jxsn5v0] (score 3, diepte 0) All i see are chicken feet
[jxt32ri] (score 3, diepte 0) Reef Fanning for me.

I was a lifeguard, so they got regular heavy use. I also wore them a lot outside of work and even did a small mountain hike in them.

Still good after 15 years.
[jxs7ekf] (score 2, diepte 2) Thank you.
[jxs8klg] (score 2, diepte 0) They are THE best.
[jxscvuq] (score 2, diepte 1 OP) I always go American made when I can and it's good quality! I think I like these so much because they are smooth and squishy and I can wear them a long time. I've not found another flip flop that does that for me.
[jxsneiy] (score 2, diepte 0) Oofos
[jxsqiqw] (score 2, diepte 0) I just ordered a couple pairs today! Including the pair pictured.
[p422wfx] (score 2, diepte 2) Yes but it's true, it's true. 

Arches are the "Cats Meow"

I have a bad knee and I need arch support ;I needed something to hold up because I wear it everyday ,and I needed something easy to clean, in that case. Plus something that didn't wear out real quick. Archie's is all that and more.

Look ,I wear Birkenstocks, Hoka  Recovery slides, Skechers Arch fit. They all work for the bad knee but sometimes not easy to clean and maybe squeeze your feet. Use all of these, but Archie's is to  the go to "must" for summer. 

The only thing is they are not water shoes they will get a little slippery and the pouring down rain.

I'm going to go out on Amazon today and do my overdue review. Plus Amazon told me because I asked; it is safer to go to the Archie store on Amazon to make sure you get the authentic product.

Hey that does sound like an ad!
[jxuc9on] (score 2, diepte 2) Fair enough
[ovwunhq] (score 2, diepte 5) More like they mould to your foot shape
[omma2t5] (score 2, diepte 2) I’ll back you up. I’ve had mine for 3 years and they’re still like new. Crazy. I love them, too! I have posterior tibial tendon dysfunction - crappy arches and achy feet - not as supportive as Birkenstocks but WAY cuter and they don’t get stinky :)
[ovqjm9g] (score 2, diepte 3) Any issues with irritation between the toes or blisters at the sides ? You know like how jelly sandals do?
[ovtyad1] (score 2, diepte 4) No, but you have to know that they’re meant to be stretched a bit to fit your foot. The only time I have gotten a blister was when I had wet feet and my feet were pretty swollen. Bad combo. But I just wore them around Legoland for 2 days and my feet are fine. I did swap for my Brooks about halfway through, but I still got in a solid 5 hours each day. Jellies are the worst. I tried as a kid and wanted to be “cool” but I lost that fight. How are they back in style?! Also, buy direct - at least for your first pair, so you’re sure they’re the real deal. I’ve heard there are lots of fakes online.
[ovtyzu5] (score 2, diepte 4) Here is a video about adjusting the strap. I haven’t heard of a break-in period. I personally don’t believe in that. I buy Brooks sneakers and after 40+ pairs, only the leather ones needed a “break in” period be aide they squeaked. To me, shoes either fit, or they don’t :) https://youtu.be/jSTtm1MNKDs?si=jvOxIyEH-0L1nD0c
[jxsufto] (score 2, diepte 0) Just reminded me I need to buy a new pair this week. They are absolutely fabulous.
[jxvhlef] (score 2, diepte 3 OP) Yowza
[jxx2hy7] (score 2, diepte 0) As much as I hate crocs. The Crocs Crocband flipflops is probably the best they produced. https://media.crocs.com/images/t_pdphero/f_auto%2Cq_auto/products/11033_0A1_ALT110/crocs

I think its made from the same material of your archies flip-flops.

My crocs flip-flops is now 12 years old going strong
[jxzvusz] (score 2, diepte 0) I say olukai hands down just my 2 cents
[kxaveva] (score 2, diepte 1 OP) It worked for me! Just don't put it in the dryer
[lghumos] (score 2, diepte 2) Maybe just a one off but I don't think I'll buy another pair.  Might happen again and for a flip flop, kinda pricy.
[lpe4z7v] (score 2, diepte 0) Blew out a pair this morning - had them for YEARS and love love love them too
[mk9qipr] (score 2, diepte 0) What are the most popular liked colors? I have black looking for suggestions.
[jxrxtrg] (score 1, diepte 0) Hello /u/hhenryhfb! Thank you for your submission! The AutoMod thought that your post might be a request type post and has changed the flair accordingly, but if this was wrong feel free to change it back!

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/BuyItForLife) if you have any questions or concerns.*
[l90qa78] (score 1, diepte 1) See the videos on their website to accommodate wide feet. I have a wide foot and the flip flops are fine. A little too tight at first but I just stretched them out like their videos show. I’m ordering some slides next.
[jxs9uyv] (score 1, diepte 2) Love the color you ordered . I ordered Taupe to go with my nail color
[jxsa0y2] (score 1, diepte 3 OP) My pair is actually a brighter coral than this- matches my toenail polish
[l7fbb3y] (score 1, diepte 3) How was your sizing?? I'm on the fence between 10 and 11.. I'm a 10 but I find most slides fit small.
[l45q8e1] (score 1, diepte 1) I’m looking into this brand and am also anywhere from a 9 to 9.5. How was the size for you and how do you feel about them in general?
[l4tzz69] (score 1, diepte 2) Sizing was not a problem. 
They felt different, but I got used to them.
[l58be1p] (score 1, diepte 2) I typically wear a US 8.5 and I have to size down to the women's 7 in the slides and flips flops but I love them and have 3 pairs of flip flops and 2 pairs of slides. Lol
[l58h4gy] (score 1, diepte 3) I just got mine. I followed the “size up” advice and I definitely should have sized down 😅
[l58halh] (score 1, diepte 4) Yeah, I initially followed the size up and it was a bad idea. I exchanged mine for 2 sizes down 😂
[l87qg5x] (score 1, diepte 5) Thank you. This I needed to know. Looking at buying. I'll size down
[l87r141] (score 1, diepte 6) I'm typically a women's 8.5 and I got the men's 6/women's 7 if that helps at all. I could probably wear the 7/8 and be okay but my feet are skinny and the smaller one fits better.
[l8o0lkr] (score 1, diepte 7) Thank you. I ordered size down. I have wide foot. Shall know next week,,,😁
[l8o7ufw] (score 1, diepte 8) You'll probably be fine with that but I'm curious to know if it was just me so keep us posted lol
[mw3b14f] (score 1, diepte 1) I used to buy them but the toe strap always breaks . I feel they should at least last a year
[l5520mk] (score 1, diepte 1) No
[n00fqkh] (score 1, diepte 1) Oofos gave me shin splints every time I wore them.
[n7aym4m] (score 1, diepte 1) I live in oofos. I must have them in every color.
[p42dgg6] (score 1, diepte 3 OP) They get squeaky when my feet are wet or sweaty too. Which is pretty funny to hear me squeaking around like an old timey cartoon character
[l87q8eo] (score 1, diepte 2) I'm looking at these. My fear to go up a size may be too big. How did you find they fit?  Smaller than sized. I really appreciate your take. Ty
[l87qdlm] (score 1, diepte 3 OP) I found them right on. I normally wear a 10.5 and I got an 11. They're like a teeny bit big. But a 10 would have been too small
[l90px8t] (score 1, diepte 3) I’ve had a pair for about 3 weeks and my husband has the slides. We both ordered our normal size. A 10 for me and an 11 for him. They both fit perfectly. I’m still breaking mine in. My husband has been wearing his daily and they are forming to his feet. We are both getting older and we both needed more support rather than cheap flip flops, these are great!
[l9bv1aa] (score 1, diepte 4) Thank you. Mine arrived yesterday.  I too ordered my regular size. And glad I did. They fit.
[ovqjodf] (score 1, diepte 4) Breaking them in because they cause blisters ?
[ovyothk] (score 1, diepte 6) Do you think they’re good for wide feet ? Many reviews say too tight ?
[mqfgku4] (score 1, diepte 3) They have half sizes
[mxi6y1h] (score 1, diepte 4) I haven't seen half sizes. Where have you seen that?
[ovypcxu] (score 1, diepte 5) Yes pretty typical for Amazon items
[ovyozcw] (score 1, diepte 5) Thank you.   Yes and I think that plastic doesn’t actually ever break in.  My current leather sandals leave a brown stain on my wet soles of feet at water so I need something more ideal just for those situations
[jxthl2t] (score 1, diepte 0) Olukai
[jxtj11o] (score 1, diepte 0) I’d get a different color when I buy
[jxtslrw] (score 1, diepte 0) Fleshy !
[jxtxg56] (score 1, diepte 0) Love my navy blue Archies!
[jxv1cgv] (score 1, diepte 1 OP) With items like low profile flip flops- it's hard to find a long lasting pair. I wear them so often that I've probably gotten about the use time that the average wearer would get in 6 years, and there's no wear and tear. While I can't determine if they'll last me my entire life, they sure seem to be on track for a very very long time. I hope it helps someone avoid buying cheap flip flops they'll throw away after a summer.
[jxx4ryc] (score 1, diepte 1 OP) Have crocs changed material in the last like 10 years? They used to give me blisters.
[kxauqf6] (score 1, diepte 0) Archie’s flip flops changed my life. It’s the guilt in arch support. It goes straight to your back and like releases something. Idk butI loooove mine! My only complaint is they look nasty quickly with like weird stains and they don’t actually recommend the washing machine… so I’m about to try a scrub brush and dawn. Wish me luck!
[kxautoj] (score 1, diepte 1) Built in 😆
[l34wyuy] (score 1, diepte 0) These are the worst flip flops I have ever owned, they are the kind they should give you in prison because they are good form of torture, and you can't harm anyone else with you. They only kill your soul from within. 

In past month I have embedded my feet with gravel, thorns and walk through literal cat piss all because they are so uncomfortable, I would rather be barefoot and suffer the consequences than to wear these Satan inspired non-prada brand shoes.
[l551wb9] (score 1, diepte 1) No it's better than ordinary flip-flops.
[l58brc9] (score 1, diepte 1) You must have gotten the wrong size or something because I legit have 5 pairs now and love them.
[l50b062] (score 1, diepte 0) they're so much better than ugly, low-quality flip-flops.
[l76ayry] (score 1, diepte 0) I'm about to buy 2 pairs of the slides. Anyone have a coupon code? $120 yikes. They better be worth it.
[l76bbs7] (score 1, diepte 0) I have these flip flops in blue and love them. Best flip flops ever I swear. Great support and the only ones that don't hurt my back and knees.
[lbg57k2] (score 1, diepte 0) Hi lady. Do you have to "dragon claw" ur feet to keep these on?
[lbg5eui] (score 1, diepte 1 OP) Not at all! I can walk as if I were barefoot
[lbgv8gx] (score 1, diepte 2) Hmmmm... this is what u struggle with, I need a strap at the back with Sandals and flip flops. How long can you comfortably walk w these? Compared to trainers?
(20 reacties met lagere score weggelaten)

=== THREAD 1jj1edg ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-03-24  SCORE: 54  REACTIES: 82
TITEL: Someone washed their feet in the break room & dumped the water in the sink…
POST (source_id=post):
so there’s a massive issue at my FC where it seems like nobody is using the multi faith room to wash their feet and instead are continuing to wash them over the toilet and in the sink after being warned many times not to do that. 

And now they’re starting to wash them in the break room…where we eat…and then dumping the water in the break room sink.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mjjmo3d] (score 78, diepte 0) do you happen to work at DET6? ppl been complaining about this all week on the VOA board here😭😭
[mjjmy3v] (score 36, diepte 1 OP) haha yes
[mjjy0qo] (score 31, diepte 0) Who in the fuck has that much time when they need to be worried about their rates smdh 😒 🙄
[mjkpuog] (score 28, diepte 1) Post the voa board 😭😂😂
[mjjljou] (score 21, diepte 1 OP) certain religious require them to wash up before praying
[mjjt9d7] (score 20, diepte 0) https://preview.redd.it/2jzs9qeghpqe1.jpeg?width=640&format=pjpg&auto=webp&s=1272cae0cbfae10f800c2fcbc23c98e17e90b34f
[mjkyoo3] (score 20, diepte 0) I need to start a religion where I need to wash my ass before I pray and do it in the breakroom. Let's see how management would respond to that.
[mjkcop9] (score 16, diepte 0) Dude was doing it in the freaking shitters at my fc 😭
[mjkyihj] (score 15, diepte 1) It’s part of their religion and the faith room probably has like one bucket of water in it with god knows how many people of faith.
[mjkz075] (score 12, diepte 3) They’re allowed by law to practice their faith. They don’t get paid for their prayer time. It’s a non-paid break.
[mjjlrp3] (score 11, diepte 3 OP) lol it’s okay, I didn’t know that either until I started working here.
[mjk9yxj] (score 11, diepte 1) It's so bad. Gotta wait until the cleaning crew leaves just to get a decent bathroom.
[mjkz8hc] (score 10, diepte 5) Calm down AM
[mjkytvv] (score 9, diepte 2) They better be getting faith for their rates to be up cause wtf 😤
[mjjpyi2] (score 8, diepte 2) That’s awesome if your religion requires you to wash your feet before praying. Under no circumstance should it be done where people eat!!🤮

Oh but wait, Amazon caters to people with specific religious requirements..🙄 Carry on..
[mjjun0x] (score 8, diepte 0) We have an ablution room at ours. Sounds like you do, too. It’s supposed to be on the building tour at onboarding but knowing how my building is run, I’m sure a lot of people are never told. Sounds like a good thing to put as a resfresher on installments and startups. And then if people don’t follow it after reminder I think there’s gotta be some behavioral feedback opportunity there.
[mjjvmd7] (score 8, diepte 0) You have a multi faith room?
[mjkkeu3] (score 8, diepte 0) That happens when all the people that Amazon hires are mostly a nasty MF
[mjjlcfk] (score 7, diepte 0) Why are people cleaning themselves at work anyway? They can’t go a full 10-12 hours without having to give themselves a bird bath?
[mjkuf9z] (score 7, diepte 0) At our site the men's room stalls are all covered in nasty brown puddles. instead of using the provided station in the multi faith room or the extra foot wash tub we keep in the bathroom people just dump water on their feet in the stalls. 

If you're not extra carful you will absolutely get nasty brown water all over your pants
[mjjo9p3] (score 6, diepte 3) Respectful upvote
[mjl6yng] (score 6, diepte 1) No, that's exactly what the multi-faith rooms are for.
[mjjloa0] (score 5, diepte 2) Oh. Excuse my ignorance. HR.
[mjkprs2] (score 5, diepte 1) There is an abolition room
[mjl2ksw] (score 5, diepte 0) Yea its a religious thing. Some sites are building rooms just for that. Others cant or wont because of how much it will coast or not having the space to instale them or the landlord(yes some sites are rented and not own by amazon) wont give them the permission
[mjlgset] (score 4, diepte 2) I hated them for this reason. I had to keep fighting my managers and supervisors and hr to get me to do something else. They say they will if I show up on time everyday and then it was really unfair when I would see every single lady on accomadations and they would be so helpful with them. I tried getting on accomdations but they wanted me off accomdations because I wasn't doing anything in the building so i had to get off accomdations because they couldn't do it for me any longer and instead I see a lady in her 50's sitting down for the last part of the shift and not doing anything what so ever. It was so annoying to see other employees get accomadations approved because of their age and they're so helpful with them. They thought I was joking or something and the health team gave me the hardest times to get my accomadations approved because I guess they didn't believe me when I have disc buldges in my L4 and L5 area with minor scoliosis. I was put to stow and on some days they had me do some bull shit like fix the bags which require a lot of turning and lifting which fucked up my back even more and then they had me do simple things like clean carts and gather bags from carts or other areas and also they would put me to move carts and would tell me to step on it even if I was on accomdations they literally forced me to walker quicker. Then they would yell at me for stowing and having my rates low even though I was on accomodations and couldn't bend frequently. Then they were forcing me to get off work since they couldn't work with me with my accomdations anymore so I had to stop that whole process.
[mjjlfyp] (score 3, diepte 0) Ironic how they wash their feet to stay clean to pray. But end up washing feet in a public toilet sink. How in the world is that being clean. It’s nasty.
[mjnjoz7] (score 3, diepte 1) Haha DET1 also has this issue 😒
[mjjo26p] (score 3, diepte 0) I can’t see how we don’t have the best immune systems in the country.
[mjn9et7] (score 3, diepte 3) That makes zero sense 😂 What's funny about this is if we did a poll on who stinks the most, it's most definitely muslims. Do you forget that most come from areas with limited running water or hygiene products.
[mjouu52] (score 3, diepte 4) Im gonna be honest though at my site the stank people are mostly potheads rather than any specific religion.

I don't have any issue with people partaking in the devils lettuce but please, wash your clothes and don't smoke in the same room as your laundry. That stench is so potent
[mjp30id] (score 3, diepte 8) ![gif](giphy|eJRGSn0AQtF86UHDb9)
[mjmrrr2] (score 3, diepte 1) In our FC they take a water bottle to the bathroom stall
[mjmrwe7] (score 3, diepte 1) OnlyFeets
[mjl6eo2] (score 3, diepte 0) Wtf do you mean washing their feet? I’ve never heard nor seen this
[mjndd1y] (score 3, diepte 0) Yea it's highly weird how much Amazon is doing for this religion. It's basically being forced upon us. I do AFM work and the guys get an extra break which we have to cover their work lol The same guys make jokes of it because they know it's taking advantage. Next time I'm going to see if I can get accommodations for lent since they want to do this.
[mjned28] (score 3, diepte 0) Why is the multi faith room used to wash feet? Don’t they have a side room for that? That has a dedicated drain? My FC has that and no one does any of what you mentioned. 

I bet folks in your FC do that because their are pressured for time and it’s the easiest solution.
[mjqkrya] (score 2, diepte 1) Post the VOA 😂
[mjjrtv0] (score 2, diepte 0) Washing feet in the sinks is crazy work , that’s crazy when they could do that at home that’s just dirty asl
[mjkur78] (score 2, diepte 1) Welcome to Islam. Religion makes people do all kinds of wacky nonsense
[mjouawy] (score 2, diepte 3) Wacky nonsense like dumping your nasty feet water in the sink and all over the floor despite being given the tools to wash up in sanitary ways is what I was talking about.

But while we are at it wacky nonsense like worshiping a guy who married a 9 year old and slept with her when she was 11, starving yourself and calling it a cleanse and beating your wife for refusing to sleep with you are all things taken directly from the Quran. 

And don't think It's just Islam either I have similar criticisms for just about every religion including the catholics.
[mjp160e] (score 2, diepte 7) Same. But.. I lowkey miss it 😂😂 I’ll be back Friday 🙃
[mjl6pdl] (score 2, diepte 2) If they can get a bucket of water and take it to the break room, they can get a bucket of water and take it to the prayer room. So many concessions are already made for this and they continue to be gross!
[mjld3jg] (score 2, diepte 3) I do totally agree but idk what restrictions on it that Amazon places. Maybe Amazon only allows one bucket or smth
[mjl55kf] (score 2, diepte 1) I don’t care about my rates, I’m constantly taking off cause they keep putting me in the same spot all day after repeatedly telling me they cannot staff me in one spot all day. I can’t divert, build walls or waterspider all day but they will stick me on sort for a whole 10 hour shift after repeatedly telling them I have scolioses and can’t do it all day.
[mjkv73q] (score 2, diepte 2) What is that? I haven't seen any at any of the sites I have been too.
[mjl9d5z] (score 2, diepte 3) Some have it and some don’t. In my building we took our multi faith prayer room away.
[mjl0rvy] (score 2, diepte 0) Just take a picture with flash on and ask if they have an only fans
[mjq4la4] (score 2, diepte 1) One of my friends is Muslim. Muslims need to wash their feet before they prey. It’s called “wudu” I believe. Something abt ensuring cleanliness before you pray. My friend does it in the designated prayer room, but he has done it in the bathroom if there’s no special prayer room available.
[mkzavu3] (score 2, diepte 3) Iol, I always go outside for break.  Too many Amazonian smells in one spot for me I need some fresh air.
[mjo8jow] (score 2, diepte 0) Haha, apparently at our FC the multi faith room is their Mosque and they can do whatever they want in it. A bunch of people got caught sleeping by HR. They got really mad and demanded the rooms and pods to be cleaned and catered to them or it’s considered “Unclean”. Our FC had to remove over a ton of blankets, rugs, pillows, chairs, etc a few months ago.

Senior HR responded with it’s a “Mulit-faith” place and anyone is allowed to use it. Please do not leave anything in these areas. You can clock out and go to an actual mosque. 

Folks are not happy and every year they threaten a strike or 15-20 bum rush our Ops office rooms. They just don’t get it and are never seen again.
[mjou8vi] (score 2, diepte 0) At the old fc they had a wudu station but some of the guys would use the mandatory salah as an excuse to be lazy (which is a sin) and spend about forty minutes using the station while others waited, so a few of us just did so in the bathroom. Had to pray in other places too. May Allah SWT guide them
[mjpojw4] (score 2, diepte 1 OP) I use to work at that location too and I could’ve sworn that there was also certain bathrooms that had 1 stall dedicated to that as well, I’m not sure why they refuse to go to the Wudu area.
[mjpnj3h] (score 2, diepte 0) I’m so disgusted ….
[mjpqdzj] (score 2, diepte 0) I work RME at DET6. I’m a Muslim American. But even I am absolutely horrified at this news. We have a designated wash room for washing ourselves. Absolutely no reason we should be using bathrooms or BREAKrooms. Gross. I apologize on behalf of Muslims at Amazon
[mjprx6z] (score 2, diepte 0) Someone washed their feet in our toilets, broke 2 toilet seat off in the ladies room while doing so, which in turn meant we were down 2 working toilets for 3 weeks, because that's how long it took to get new seats ordered and installed..... in the meantime time we only had 2 stalls to use because there isn't multiple bathrooms as it's a smaller building...... which is very annoying when you got 30+ women trying to use the bathroom only at break times.
[mjjjtql] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[mjq7bub] (score 1, diepte 4) You can request Easter Sunday off as a religious exemption. Do it soon though
[mjmp8mn] (score 1, diepte 7) Username checks out, you definitely are dramatic.
[mknj06m] (score 1, diepte 1) It's actually pretty common to read on this sub.  That and smelly foods in the microwave.
[mkz8qso] (score 1, diepte 2) Dude the microwaves during break legit make me nauseous, like what are people microwaving, dead bodies?
[mjnq9qe] (score 1, diepte 0) Gross. But I got ya beat. Yesterday somebody purposefully took a dump on the floor of the men’s restroom and left the toilet paper they used to wipe their ass on top of the pile. This place is unreal.
[mjp7y43] (score 1, diepte 0) That’s why they take soap into the bathroom stall!
[mjpbvjb] (score 1, diepte 0) I am at hou3 and I see that all the time I mentioned it to the managers but nothing's ever done💀
[mjplmh3] (score 1, diepte 0) They have signs posted at DTW1 in the all the bathrooms saying not to do that. They even temporarily closed down the bathrooms next to the prayer spot to install a tub for feet and handwashing for Wudu. Have yet to see anyone actually use them though.
[mjqykvh] (score 1, diepte 2) Yes that’s exactly what I’m talking about. The bathrooms on the third floor has a stall with a small tub in it specifically for feet washing, yet I still see women washing their feet in the sink. Leaving the floors all wet and the bathrooms smelling like feet!
[mjppwkg] (score 1, diepte 0) That’s crazy 🤣
[mjq28kw] (score 1, diepte 0) That's nothing my daughter sent me pictures  of
*
 Indian lady washing  her feet in the sink. Literally, put her foot in the sink
[mjq314t] (score 1, diepte 0) https://preview.redd.it/bzvdufd4iwqe1.png?width=1440&format=png&auto=webp&s=496ad1adbea90df8cad2379876dbc72f2878114d

Bro look
[mjql66q] (score 1, diepte 0) That's very bad. It'll definitely cause serious bacteria spread.
[mjqtfgo] (score 1, diepte 0) My last building had 2 prayer rooms with the feet washers specifically for this!
[mjqx2m3] (score 1, diepte 0) Women wash their feet in the bathrooms!  There is a foot washing sink for you in the multi faith room! Why is no one talking about this !!
[mjr2268] (score 1, diepte 0) I just pee in the sink now
[mjr7hjd] (score 1, diepte 0) i would call them out if i walked in and seen them doing that.

![gif](giphy|RCX9vhBZu3oqM5SpwV)
[mkniuil] (score 1, diepte 0) This post seems satire but sadly I know it isn't.  I couldn't do it.
[mjmpxec] (score -1, diepte 8) Lmfao bro it's just a joke. Calm ur self down bro.
[mjmq39k] (score -1, diepte 8) Hence the emojis 🧐😭😂🙄
[mjk7qhu] (score -2, diepte 3) Only specific religions do they cater. They offer religious accommodation but if it’s anything to do with Christianity you can forget about it.
[mjl96ty] (score -2, diepte 2) Why would I wash my feet in a prayer room. 😒
[mjovlpo] (score -3, diepte 0) Remember this the next time you consider voting for a Democrat.
(4 reacties met lagere score weggelaten)

=== THREAD 1cafhjq ===
SUBREDDIT: r/Residency
DATUM: 2024-04-22  SCORE: 23  REACTIES: 81
TITEL: Stinky feet - advice needed
POST (source_id=post):
Hi guys
I recently noticed that I get really stinky feet at work (and only at work). Since I'm on my feet (and in my shoes) for many, many hours a day. Since I already shower once/day (at least), change my sock quite as often and don't have any other problems with body smell and also don't sweat a lot, I think it's either the shoes themselves (they're theoretically breathable, but made from a different material that can be washed) or the insoles (which I _have_ to use). I air both the shoes and the insoles out every night and also tried some UV-light that you put inside the shoes (no idea if this generally helps, it didn't for me). Washing the shoes also helps, but only for 2-3 days, and I cannot (and do not) want to wash them as often also since I find it a bit yucky to use my pwrsonal washing machine for this... 

Before buying 100 different pairs of shoes I wanted to ask for your advice. Maybe some of you had aimilar problems. Can you recommend me a brand of shoes and/or shoe deodorant I could use? They should be really breathable but still closed, as this is required from my hospital. 

Thanks in advance from me and my stinky feet :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l0rjt83] (score 73, diepte 0) I rotate two different pairs of “work shoes”, doesn’t totally eliminate the problem (mostly because I work out in them too), but it helps tremendously.
[l0rke2v] (score 40, diepte 0) White toe socks, heavy duty anti-fungal spray or powder. Use religiously, make sure your feet are completely dry before putting on socks.
[l0rlvjw] (score 27, diepte 0) Wool socks
[l0ru5cc] (score 26, diepte 0) Just ask that one nasty fucker on here that claims he showers once every 6-8 weeks and doesn’t stink. 


But seriously, change socks daily, shower daily, and if foot odor is still an issue, you can buy antibacterial sprays for your shoes that help. Also wearing thinner socks help prevent sweating too.
[l0rrqz0] (score 15, diepte 1) This is the correct answer.  I ditched cotton socks years ago and will never go back.
[l0s2enr] (score 13, diepte 1 OP) But what about my knees and toes?
[l0rk716] (score 10, diepte 0) Use white vinegar when you wash your shoes. You can also do regular foot soaks where you add a little vinegar to the water. What material are your socks?  Recommend merino wool.
[l0rp0qx] (score 9, diepte 0) dryer sheets in the shoes also help
[l0rpmy0] (score 9, diepte 0) Cotton or wool socks. Polyester lycra etc are stink inducing. It's not your shoes.
[l0s1wrj] (score 6, diepte 1 OP) Thanks, I'll try it for sure. Why white though? Because I can wash them at higher temperatures than colourful ones?
[l0rsobi] (score 6, diepte 0) Deodorant on your feet
[l0s5hq6] (score 6, diepte 2) Anti fungal foot powder in the shoes too.
[l0t4k8d] (score 6, diepte 0) Respiratory therapist who walked on average 10-17,000 steps at a busy level 1 here (for many years). 

2 pairs of work shoes that you rotate, wool socks, dr. Scholls foot spray before each shift is the way.
[l0rw1wt] (score 5, diepte 0) Lumi
[l0rxu6y] (score 5, diepte 0) Cheap socks and cheap shoes made it noticeably worse for me. I switched to higher quality tennis socks and white leather sneakers and feel my feet can at least somehow breathe now.
[l0ryx1m] (score 5, diepte 0) Cotton socks and sprinkle foot powder into your shoes.
[l0s1575] (score 5, diepte 0) Change the shoe, wear the shoe with always well soaped cleaned foot and clean socks. You can try crocs clogs or similar products for more breathability-less smell. In our country nearly nobody wears shoes at hospital.
[l0s1k2z] (score 5, diepte 0) Antibacterial soap on the feet when you shower and let it sit for a bit. Absolutely changed my world. I haven’t done it in years but it’s been good for like 10 years now.
[l0s5nw3] (score 5, diepte 0) Wash your feet with clorhexidine soap. Hibiclens or whatever you can steal from the supply closet.
[l0slsfa] (score 5, diepte 0) Panoxyl wash on feet
[l0tie4b] (score 5, diepte 0) Surprised there do not seem to be any comments questioning athlete's foot. Try Tinactin powder or whatever other antifungal medication you have access to.
[l0uh8my] (score 5, diepte 0) This is gonna be TMI but I literally had never had this issue before residency but all of a sudden a few months into intern year, my feet were practically walking stink bombs in my house after a long day, and the smell had colonized all of my socks/shoes so badly that I was starting to even smell my feet just sitting at my desk at work

I’ll say that I tried every home remedy; freezing the shoes overnight, filling them with baking soda, I always wore clean socks and washed my socks on high heat/highest wash setting, I used antibacterial sprays, vinegar scrubbed down the shoes themselves; at best each of these was just a bandaid

It only got better when I threw away every shoe and every sock that was carrying the smell. Started the rotation with a completely fresh slate for shoes/socks, and I’m now hypervigilant about deodorizing my feet before work, antibacterial spraying the shoes as soon as I get home, etc

Just wanted to throw that out in case nothing else in this thread works for you. If your case is severe/refractory then whatever’s causing the stink may be infecting it’s way into the very fabric of your shoes and socks, and if that’s a case a full closet reset may honestly be your best option
[l0u48hm] (score 4, diepte 1) change socks when they get sweaty, buy foot powder for your shoes
[l0wbduw] (score 4, diepte 1) Honestly buy three! Rotating shoes is the absolute key. It will solve your problems 100%, icing on the cake if you buy some foot powder and sprinkle it into your socks and into your shoes every morning. And once the shoes start to stink, I think they’re extremely difficult to bring back from that. Dig deep into your pockets, bite the bullet, and throw them out.
[l0t78ll] (score 4, diepte 2) I noticed dermatologists tend to recommend white socks made out of cotton
[l0rwxit] (score 4, diepte 0) Use antibacterial soap or hibiclens on your feet
[l0rolop] (score 3, diepte 1) This is my strategy.
[l0ro6wh] (score 3, diepte 0) Baby powder
[l0sctuv] (score 3, diepte 2) You could try smartwool or equivalent. Also try washing your feet with antibacterial soap - my brother of the stinky feet swears by dial.
[l0s3327] (score 3, diepte 1 OP) I do this already, but one of your fellow commenters mentioned letting it soak in, which I'll definitely try
[l0s2o6f] (score 3, diepte 1 OP) We have to wear closed shoes that we could run in, and crogs do not work with my insoles (and I do not find them comfy, which ofc is personal)
[l0s37ck] (score 3, diepte 0 OP) Thank you guys so much for all the recommendations, I'll give them a try for sure
[l0s3xmg] (score 3, diepte 0) Cheap 100% nylon compression socks stink like crazy. I changed to Sockwell that is a wool / rayon / nylon blend. Expensive but 100% worth it. No stink, better compression, more comfortable.
[l0s4m6p] (score 3, diepte 1 OP) I got nice cotton socks. Should better use compression socks as well, I suppose, but I just don't like them. I rather do vein gymnastics and fidget around :P
[l0s9gfq] (score 3, diepte 0) How about those who wear compression socks? It seems like such an unavoidable problem heh
[l0saeep] (score 3, diepte 0) use isopropyl alcohol on your feet, or at least keep em dry
[l0sbeqw] (score 3, diepte 0) First I washed my shoes then froze them for a few days to eliminate odour in my shoes. Then I started putting armpit deodorant on my feet which helped a lot.
[l0ss2zg] (score 3, diepte 0) If you're wearing your shoes on too tight, try wearing them loose. It worked for me!
[l0sy07w] (score 3, diepte 0) put baby powder in your shoes every morning
[l0t0wr1] (score 3, diepte 0) It's almost certainly moisture from your socks. Sorry you're allergic to wool. There are plenty of synthetic fabrics that wick moisture well, like Tencel. Darn Tough has a synthetic line called Coolmax that is 100% synthetic, and there are some hiking enthusiasts that insist on using them over wool, even for thru hikes. I do think Coolmax are inferior to wool for odor though.

I'm curious if you're actually allergic to wool or are just irritated by it. Some people are just irritated by the coarse fibers of certain wools. Have you ever reacted to cashmere or alpaca wool?
[l0t29gg] (score 3, diepte 0) I put antiperspirant deodorant on my foot directly before socks, then spray deodorant on the socks, and wear allbirds. With this, my feet went from literally horrendous to being a non issue
[l0t5zyu] (score 3, diepte 0) Try Mando. It works!
[l0tnk1l] (score 3, diepte 0) Check the bottoms of your feet to see if you have super tiny, shallow little pits in them aka pitted keratolysis, a bacterial infection that causes stinky feet. 

Regardless of whether you have PK, you can still use benzoyl peroxide wash or hibiclens on your feet in the shower to help with the smell.
[l0tsd6q] (score 3, diepte 0) 1. Air out your feet and shoes when you get back home. 

2. Charcoal absorbing packets in shoes. 

3. Rotate 2-3 pair of shoes if you can afford them so they are truly dry before next use. 

4. Chlorhexidine/benzoyl peroxide wash your feet daily. 

5. Gold bond powder in your socks before wearing them. 

6. Good quality socks.
[l0teye5] (score 2, diepte 2) Can’t find a good source for it now but I was told something about the dye provided a good environment for the bugs. It worked for me, but not suggesting it’s EBM!
[l0uxx1s] (score 2, diepte 3 OP) Very interesting theory 🤔
[l0uqgnu] (score 2, diepte 2) You can also bleach the hell out of white socks. Bleach and hot water wash will blast any funk-causing microbes. 

Also, seconding the other people recommending getting additional shoes to rotate, that extra time to air out helps. Maybe keep using that UV light on the pair that is resting for good measure.
[l0uux49] (score 2, diepte 2) Nylon are even worse
[l0s1qx6] (score 2, diepte 1 OP) This is a very good idea, unfortunately I'm allergic to wool. But I agree that wool is great for your "feet climate"
[l0rss9v] (score 2, diepte 0) Head and shoulders might work
[l0s2rq6] (score 2, diepte 1 OP) I think I really gotta try a spray
[l0sg8fb] (score 2, diepte 1) Buahahahahaha!! Cleanliness is merely just a state of mind

body odor included.
[l0s59n7] (score 2, diepte 0) I only ever word white cotton socks which seemed to keep the odor down especially since my feet sweat. Try putting foot powder in the shoes after wearing too.
[l0saw07] (score 2, diepte 0) I use charcoal scent absorber bits that i put in my shoes and i think they help
[l0sg7i6] (score 2, diepte 0) Shoes on a dryer at night will help too
[l0shrmv] (score 2, diepte 0) Copper yarn socks.
[l0u6qf0] (score 2, diepte 1) This!!
[l0utxev] (score 2, diepte 2) I use this stuff for everything, armpits, chest and back acne, feet, and It is amazing
[l0u6mq4] (score 2, diepte 0) Wash your feet with benzoyl peroxide bar soap. Idk if it’s true, but I heard that the odor causing bacteria are anaerobic, so benzoyl peroxide kills them. I wash my pits with it and I don’t need to use deodorant 🤷‍♀️
[l0u7da1] (score 2, diepte 0) Foot powder and well ventilated shoes
[l0u7rq4] (score 2, diepte 0) Do you have fungus? Hyperhidrosis? Last visit to your dermatologist? Last time you got a pedicure?

Address the problem at its root and skip home remedies.
[l0uxgx0] (score 2, diepte 0) Not sure of the mechanism but my wool socks stink way less than cotton socks. In cotton I can sometimes catch a whiff of my feet coming up from under the desk, but have worn wool 3 days in a row before deciding to change them out
[l0v3ubg] (score 2, diepte 0) crazy idea, but has anyone tried silica gel packets tucked in their shoes? might be a bit uncomfortable though on long days
[l0vdiwx] (score 2, diepte 0) I buy shoes I can wash for many reasons. Feet get stinky but also they can be cleaned easily if you get blood/vomit/poo on them.
[l0vlwj3] (score 2, diepte 1 OP) Mine are also washable, but I only wash them when I _have to_ and when I have enough time to let them dry, which is rarely the case. 
I wonder if the washability is part of the problem though, as the material is different from all my other shoes...
[l0vw8la] (score 2, diepte 0) Try Lume
[l0y5w4g] (score 2, diepte 0) Use baby powder inside the shoes 👟.
[l1bbiex] (score 2, diepte 0) Put some baking soda in your shoes.
[l0ri1vr] (score 1, diepte 0) Thank you for contributing to the sub! If your post was filtered by the automod, please read the rules. Your post will be reviewed but will not be approved if it violates the rules of the sub. The most common reasons for removal are -  medical students or premeds asking what a specialty is like, which specialty they should go into, which program is good or about their chances of matching, mentioning midlevels without using the midlevel flair, matched medical students asking questions instead of using the stickied thread in the sub for post-match questions, posting identifying information for targeted harassment. Please do not message the moderators if your post falls into one of these categories. Otherwise, your post will be reviewed in 24 hours and approved if it doesn't violate the rules. Thanks!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Residency) if you have any questions or concerns.*
[l0uzpms] (score 1, diepte 1 OP) Cotton, I'm allergic to wool (lanolin)
[l0s1ywc] (score 1, diepte 1 OP) Great idea
[l0s26rq] (score 1, diepte 1 OP) I use cotton already :). I just never have problems with different shoes (but I also do not wear them all day long, so...)
[l0uz5da] (score 1, diepte 3 OP) Smartwool sounds interesting, I'll look into it
[l0uxzoy] (score 1, diepte 2 OP) Maybe I should try to meditate more :P
[lj5ux5j] (score 1, diepte 2) Any update? And which soap ? We don’t have hibiblicens here
[l0s2ych] (score 1, diepte 1 OP) Use this kind of soap already, but I don't let it soak in - thanks for the tip :)
[lj5ulve] (score 1, diepte 1) Which soap do you have? And has it to contain chlorohixide glucomate? If yes how much percentage
[l0uyfud] (score 1, diepte 1 OP) Yeah, the material seems to be rather problematic. I don't wear them though, got cotton socks
[l0sb40j] (score 1, diepte 0) Exclude pitted keratolysis
[l0uy1gd] (score 1, diepte 3 OP) Will see if I can get this over here
(9 reacties met lagere score weggelaten)

