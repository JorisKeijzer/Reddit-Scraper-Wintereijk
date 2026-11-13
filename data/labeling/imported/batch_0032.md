# Label-batch batch_0032

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
Schrijf het resultaat naar `batch_0032.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 17e359l, 14a8a50, 17tqyfm).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 17e359l ===
SUBREDDIT: r/goodyearwelt
DATUM: 2023-10-22  SCORE: 220  REACTIES: 55
TITEL: My feet have never been more happy. My wallet has never been more sad.
POST (source_id=post):
Longer post after waking up on a Sunday with no foot pain for the first time in years. (Last week was a Saturday morning without foot pain)

I did 8 hours walking and standing on concrete Friday night into Saturday and 14 hours Saturday into Sunday. I manage a security team of about 36 with my buddy. They realized pretty quickly that I am mechanically inclined so me and another guy whose main job in maintenance tackle things as they break during the weekend.

So I am constantly moving around from little issue to little issue. The occasional fight and a lot of peaceful walkout. I am spending a third of the time standing, a third walking, and a third crouched down or crawling into spaces to fix something.

Since I'm 300lbs and near 40 I've moved through a number of brands and all of them leave my feet screaming during the shift and the mornings after. Danners fit the ball of my foot pretty good but no nearly tight enough on the heel. Similar for most of the other brands I've tried over the year. These Nick's are still breaking in so a little tight around my big toe (my big toe is a half inch longer than my other toes and pretty bulbous) but the heel support is exactly what I needed.

I normally wear a 13 EE and took my measurements with the Nicks printable guide. Plus went to a shoe store. I am bewteen a 12.5 and 13 EE. I went with the 12.5EE and I think I made the right choice. 

The stitching and leather quality is beyond anything I have ever owned. I got these in brown chromexcel and this is my first time owning a Horween leather product. I like the balance of color, suppleness, but still stiff enough for its function that this leather gave. Even though I am going to be working in these boots I am glad I got thisnleather choice.

I ordered a second pair of Nicks. This time in builder pro cutters choice for the fast lead time. I didn't want to buy a second pair at these price points without first trying a pair out.

I am now about 30 miles and a week and a half in wearing them 3 days at the bar, and 4 days at the office job.

This was my first time buying a boot north of $450 and I wish I had made the leap a dozen pairs ago.

Some pictures of the boots before a light brushing and little LP over the scratches. The later pictures are after the clean up. I decided to treat them with LP given they are exposed to oil, beer, alcohol, food, cleaning products, vomit, and occasionally blood. I haven't trimmed the leather laces to length yet. Still deciding on exactly how I want to tie them.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k60trkw] (score 52, diepte 0) Buy once cry once
[k61y4p7] (score 42, diepte 2) https://preview.redd.it/ha7fnlq35vvb1.jpeg?width=3024&format=pjpg&auto=webp&s=52785bd2c58cff5a985ea93bc2c7ae8cf0e43ffa

… then this happens.
[k61qqjl] (score 41, diepte 1) But then you need a black pair.

Oh, then the exotic leather option for those dressy casual moments.

Then…
[k620gcy] (score 31, diepte 3) Can confirm.

https://preview.redd.it/geeqc6k78vvb1.jpeg?width=3904&format=pjpg&auto=webp&s=06a2de4193ba3af01e343e57f65b3ff81cc72371
[k611cv5] (score 11, diepte 0) I'm glad you found the value of a good quality boot/shoe. The initial cost to ownership is certainly the biggest barrier, but once you're over it, the comfort/fit, durability, and character they develop over time makes them worth it. Take care of them (as you certainly shall), and they will take care of you.

For what it's worth, irt the long laces, when I was in the military we were taught that the long laces on the paratrooper-style boots (like yours) were for wrapping a time or two along the top (keeps bugs/dirt out of the boots which minimizes heat/friction points where blisters may develop) after lacing and before finally tying.  Just remember to not tie too tightly as the feet expand a bit over the long hours walking so as to not get the boots too tight. But you've probably figured that out at this point.

Congrats. They look good!
[k620kus] (score 10, diepte 4) Salute. Very nice. I need to up my storage game. 
Where’d you get those stands if you don’t mind me asking.
[k6209oz] (score 6, diepte 1) It’s more like buy once, stop crying, buy more.

Four pairs of Nicks… speaking from experience.
[k64bebj] (score 6, diepte 1 OP) "Nick's Overlander" in custom configuration (big change is the logger heel instead of a block heel)

Here is the text of my order choices:

Overlander - Custom Configuration
Buy with Confidence: I understand that Nicks recommends ordering a half size shorter than my normal size, and I can return and exchange my boots if they are in a new condition. (Limited to one exchange per order)- Yes

Fitting method- Build to the size I select.

Boot Length- 12.5Boot

Width- EE - Wide

Boot Height- 8''

Pull Loop- Yes

Leather Style- Brown CXL

Top Style- Standard

Hardware Configuration-Hooks and eyes - RecommendedHook and Eye 

Color-Brass - Recommended

Polarthin-XP Insulation?- No

Toe Structure- Soft Toe

Toe Style- Standard

OutsoleV100 Lug - Standard

Edge ColorBrown - Not Available on light colored soles (HV, 2021 ...

Heel Profile- Logger

NICKS SKU- OVLD-HNW-MTO-CCS-PL-BRNCXL-STDT-H&E-BRASS-SFT- V100-BRNE-LOGHEEL
[k61dgjc] (score 5, diepte 0) Nicks hitting the cxl lottery again.

Really nice boots.
[k61v5lw] (score 5, diepte 1 OP) Oh yeah. Well office of a manufacturing factory. I've been there 13 years. They are all kind of used to me doing my thing. They do keep a pool on price is right style on when I will break my next office chair. I'm on chair number 5.
[k6341hu] (score 4, diepte 4) At least yours are different colors. Always crazy when someone has like 15 pairs of brown or black boots
[k61iw5m] (score 4, diepte 0) Nice boots! Looks like dog shit in the lugs lol
[k62fa0r] (score 3, diepte 5) Curious on that too. I’ve seen ones like these below but not great for boots and I like those way better too

[Somewhat similar](https://www.amazon.com/Neprock-Organizer-16-Upgraded-Organization%EF%BC%88White%EF%BC%89/dp/B0CC4DJ91Q/ref=zg_m_bs_g_23715177011_sccl_14/143-3770782-3025059?psc=1)
[k63jqff] (score 3, diepte 6) I’ve tried these and they’re too flimsy for boots.
[k63joio] (score 3, diepte 5) They’re plastic shoe organizers from ikea. They’re like a buck each.
[k61e00b] (score 3, diepte 2) Remember that leather laces are meant to be cut to size.
[k61j9x9] (score 3, diepte 4) LOL. I'm just playing around. The laces are fine and, being of the same material as the boot, will patina in turn with the boots. Also, the texture of the leather laces helps mitigate any unlacing as one walks (kinda like waxed laces). 

You may just have to trim them a bit (leave enough 'just in case') or double-tie them as is (make 'extra-big' loops to take up some of the slack of the laces and tie the loops over onto themselves one more time). We often double-tied them in the military as having extra-long laces came in handy should we be in any sort of 'survival' situation - tying a knife to the end of a long stick, securing poncho-liners as makeshift tarps, etc. Of course, no one actually needs to look at things that way today so that may be an antiquated pov on my part. Still, you'd be amazed how durable waxed, cotton laces (like military boot laces) or leather laces can be.

I have replaced boot laces for colorful ones in the past (I went orange on black boots and red on brown/tan boots) just for fun in the past. The laces I choose, honestly, were any available at a place that sells good boots. Where I'm at, a local farming supply store chain (i.e. Fleet Farm) was always great for this. I suspect probably any good boot/shoe store would do, though. Of course, you have to have a sense of humor to do this as one should expect a few looks, or rather thick skin. Who knows? You may actually like to go this route. If you do, keep the original laces as you never know if you may want to switch, or when the zombie apocalypse will hit.
[k6135hr] (score 3, diepte 0) I’m in same position foot size wise. Hard to find 12.5’s so I’ve always bought 13 D and put inserts in. Recently found a pair of thorogoods at the thrift in a size 12 and perfection. I honestly think the fact that they were used and already broke in was the key
[k63ikgm] (score 3, diepte 2) I wouldn’t use Obenaufs anymore. You ordered Brown chromexcel and regular oiling with obenaufs will destroy the depth of color and shine on your boots.

I would use Venetian shoe cream in a couple of months when your boots are due for their next treatment.
[k66e6dm] (score 2, diepte 3) >r/goodyearwelt

You have really good taste. In what country do u live where u have such a wide selection?
[k60zwqm] (score 2, diepte 0) how to tight them : [https://www.reddit.com/r/WorkBoots/comments/17dviqh/how\_do\_i\_tie\_my\_boots\_haha/](https://www.reddit.com/r/WorkBoots/comments/17dviqh/how_do_i_tie_my_boots_haha/)
[k6180eo] (score 2, diepte 1 OP) I tried the lace around the back. The length is just shy of what I need, unfortunately.
[k81uwt8] (score 2, diepte 4) If you're looking for length I'd suggest "King's Lacing" also called "Z lacing"
Gives you alot of length and works really well for leather lacing
[k61gqaw] (score 2, diepte 2) Ah... then buy bright red laces and strut those bitches like the rest of us!
[k61vtka] (score 2, diepte 6) Roger that! I've gone so far as to weave a belt out of 550 cord and resewed my BDUs' buttons with fishing line "just in case", so I'm that type of crazy. I've since settled down a bit, but something tells me the zombies are real...
[k616mo4] (score 2, diepte 0) Overlanders are so nice. I’m thinking about selling a few pairs of boots that don’t get much use and ordering a pair. How long did you have to wait for the order to come?
[k6197jx] (score 2, diepte 1 OP) I ordered them custom configuration March 2nd, 2023. I received my boots October 10th, 2023.

They are a hertitage line in CXL so longest standard leadtimes
[k63glta] (score 2, diepte 1 OP) HNW last. 

I have the Venetian Shoe Cream. You think I need that with the Obenauf's heavy LP?

In the spring, I am probably going to order a third pair in Polarthin-XP for 2024-2025 winter. I may try something jn the 55 last, see how that works for me.
[k63lbga] (score 2, diepte 3 OP) I mean, I was prepared for these to darken and not have the pull-up seen on Horween. These are work boots for me. I am really more concerned about the alcohol, cleaning products, vomit, oil & grease (both food based and petroleum) that these are exposed to. 

Will I get the same level of protection from the above with venetian?
[k63mf84] (score 2, diepte 4) They should. Venetian will have a layer of wax which should help with the spills.

I suppose with the work you’re doing, darkening and heavy wear is investable but my understanding is that obenaufs is better suited for the drier, heavier stiff work leathers.
[k63nt8m] (score 2, diepte 5 OP) Thank you for the advice. I believe I will try using the venetian only for the next conditioning. We will see how it goes in the weeks after that.
[k61ulsy] (score 2, diepte 0) You're wearing these in an office job haaha?
[k63jvh3] (score 2, diepte 0) How long is the wait on the cutters choice?
[k63kllp] (score 2, diepte 1 OP) Entering production this week is orders from October 12th through October 17th. I ordered mine on the 18th. Just missed this week's date.

(I know last week was through October 11th, since I looked when I placed the order)

https://nicksboots.com/lead-times
[k644e38] (score 2, diepte 0) What is the point of a kiltie? Anybody care to explain?
[k649z8j] (score 2, diepte 0) could you share brand and model?
[k6rpxn6] (score 2, diepte 2) thanks!
[k65hq6f] (score 2, diepte 0) Always like posts like this. 'Grats on a very nice purchase. Lots of good info, thanks.

One thing I'm curious about is the laces. It looks like they don't give you an option to choose another type, and I've never had luck with leather laces. The speed hooks always chew through them fairly quickly. Granted this was way back when I usually spent between $200-$270 on a pair, so I've just replaced them on my more expensive pairs if they came with them. I work with leather on the side, and I don't know if I'd trust even really thick veg-tanned leather to be much better than what I've experienced. Do you (or anyone else here) find that they last longer than a few months, or is there some benefit to using leather laces and just replacing when needed, instead of just buying some made of a more durable material?
[k65iybk] (score 2, diepte 1 OP) All the Nick's boots come with them. From the feel, I think they might be the same brown CXL that the boots are made of. I am not sure.

I keep a pair of aramid laces(plus I always have 550 paracord) in my bag at work. I figured I'd try them. I have to loosen the bottom laces everytime I put these one and then pull them tight again (I have a wide ball of my foot). So these are getting a work out, but so far, so good.
[k65qqao] (score 2, diepte 2) Yeah, really like the aesthetics. I do the same for field repairs. Always have a good length of paracord, and I'll throw some shrink tubing on the ends real quick and just keep using those until they need swapped out.

Again, great pair of boots. Every post like this nudges me a little closer at pulling the trigger on a pair of Nick's, specifically.
[k65sns3] (score 2, diepte 3 OP) Only advice I have is I wish I had done this years ago.
[k65n8vv] (score 2, diepte 0) How about your nose, with that big yellow dog shit squeezed into the tread?
[k66ymz1] (score 2, diepte 0) Gorgeous boots, and great write up. Curious if there is a thread about the profession of those who purchase these boots? I guess i'm most curious if guys wear them for style/comfort more than guys wearing them as function for their profession.
[k675bl4] (score 2, diepte 1 OP) None that I've seen. I assume a good percentage have bought Nick's primarily for their function
[k67fnva] (score 2, diepte 0) That brown CXL looks awesome, super underrated color
[k67gdub] (score 2, diepte 0) How can you wear these boots quickly? I always prefer chelsea. Even for a classic oxford it's still a pain to put on and put off.
[k7dfepr] (score 1, diepte 4 OP) I'm on the East Coast of the US
[k63och5] (score 1, diepte 2 OP) Does anyone know of a similar boot in Horween Dublin Greener Pastures haha?
[k613kuz] (score 1, diepte 1 OP) Debating on whether I want to use a logger knot
[k61em30] (score 1, diepte 3 OP) Yeah, they haven't been an issue yet. I've been lacing and tying them a few different ways. Some leave more lace left than others. I was kind of hoping the laces would stretch a little and I could tie them around the top of the boot. I'm not sure they are going to stretch that much.
[k61gud1] (score 1, diepte 3 OP) Which would you recommend?
[k61p19i] (score 1, diepte 5 OP) I keep aramid laces in my bag plus 550 paracord. But thanks for the advice haha
[k61pord] (score 1, diepte 1 OP) That's actually pizza they give at my bar for every drink. This guy was carrying his free pizza when tried to shove past my barback. I told him he had to leave. He told me he wasn't going to. I dumped his pizza onto the outdoor floor drain, and waffle stomped it down. Thought he would try to fight me but didn't. He left on his own. The girl he was with tried to fight me, pretty good shove, but was dragged out of the bar by co-worker. Then told police I punched her in the throat but we have cameras and the closest I came to touching them was taking away his pizza. (She dropped her pizza when she shoved me)
[k648lp9] (score 1, diepte 1 OP) My understanding is there are two functional reasons:

On these boots, the tongue is made of a softer, more supple leather. The kitties protects this leather from the laces and any dirt or grime that gets between the laces and the kiltie.

Since the leather is softer the kiltie adds a layer of stiffer leather between the laces and the top of your feet.

They also have an aesthetic aspect that I enjoy.
[k65no8c] (score 1, diepte 1 OP) "That's actually pizza they give at my bar for every drink. This guy was carrying his free pizza when tried to shove past my barback. I told him he had to leave. He told me he wasn't going to. I dumped his pizza onto the outdoor floor drain, and waffle stomped it down. Thought he would try to fight me but didn't. He left on his own. The girl he was with tried to fight me, pretty good shove, but was dragged out of the bar by co-worker. Then told police I punched her in the throat but we have cameras and the closest I came to touching them was taking away his pizza. (She dropped her pizza when she shoved me)"

From an earlier reply, it's a crushed pizza. Since it didn't have time to rot it didn't smell that bad.
[k67hyko] (score 1, diepte 1 OP) I have to loosen laces and tighten each time. Everything is still pretty stiff. Once my foot is seated and the laces correct, I am good for the whole day. 

I may have gotten lucky with the fit?

=== THREAD 14a8a50 ===
SUBREDDIT: r/ChronicPain
DATUM: 2023-06-15  SCORE: 35  REACTIES: 53
TITEL: Heel/ankle pain
POST (source_id=post):
Lately it's been hard to walk on my heel/ankle so I've been tip toeing but that's getting harder to do also I don't know what to do 😭😭
It hurts a lot to put pressure on my heel/ankle I just tips to help the pain

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jo94ahj] (score 96, diepte 0) That needs to be seen by a doctor. Now. Urgent care or ER. That swelling is insane. And if youre in so much pain you can't walk, that's an emergency.
[jo965r4] (score 74, diepte 0) Go to the ER that could be very serious.
[jo9aeuw] (score 47, diepte 0) Holy shit. I broke my ankle and it didn't look as swollen as that. Get it checked.
[jo9gjce] (score 42, diepte 0) If it’s swelling from diabetes you could loose your foot. HOSPITAL NOW
[jo92bw7] (score 30, diepte 0) You called anyone? This swelling obviously isnt right. Could be lot of things, most should be looked at now.....
[jo963m2] (score 25, diepte 0) Mother of god, OP! If you don't know why that swelling is happening, go to the hospital!

EDIT: I'm not trying to be shrill, I'm just really worried about you. 

FWIW: I got heel pain recently independent of the chronic pain that has been plaguing me since childhood; my GP prescribed Vimevo (I live in Norway, I don't know if it has other names) it is a a formulation of naproxen and esomeprazol - one for the pain and one to line the stomach.

It works very well, you might try it.

I hope you feel better soon xo
[joaciza] (score 23, diepte 3) All OP said is “I don’t know what to do” and that it’s getting worse, and the response is that even people with experience with chronic health issues are suggesting what OP needs to do is get this checked out. Telling someone to go to a doctor for suddenly worsening chronic pain is good advice, I’m shocked anyone would say otherwise when the risk here could be someone losing a foot, or worse. 

OP could be walking on a broken ankle and not realise because they’re already dealing with pain, OP could have something very seriously wrong with their ankle being masked by other conditions, and if you’re asking people what you should do when you’re experiencing a medical concern I think you probably expect the possibility of the reply being “please see a doctor”.
[joaiq1w] (score 21, diepte 0) You’re experiencing circulatory issues. Sure, the swelling is alarming, but the color of your right foot is also of concern. I highly recommend you seek medical treatment. In the meantime, elevate your legs above your heart.
[joa76j4] (score 20, diepte 1) I would think it's because as pain patients, we generally don't go to the ER or even the doc if we get hurt. We know what the ER doc will say, and it is costly, takes forever, and generally fruitless. As soon as they see you're on pain meds, forget it. 

Sometimes you have to have someone tell you that what's going on isn't ok. I fell on my hands a couple of months ago and it took my hubby several days to convince me to go to the doc. It hurt like hell, but I'm used to pain and I was gonna wait it out. Ended up needing an Ortho consult.
[jo9r1wj] (score 17, diepte 0) I hope you’re in the ER by now and that you will update us all at some point. That swelling does look rather worrisome.
[jo9kiah] (score 14, diepte 0) H O S P I T A L
[jobct38] (score 14, diepte 6) Then why are you relying upon your mother's assessment of the issue?
[joajntp] (score 12, diepte 3) OP clearly expressed this is not normal and they didn't know what to do. If they had been expressing frustration in an unchanging condition, irritation over the occasional, but expected, difficulty walking, or even concern over a slowly worsening condition I don't think the sub would have reacted this way. I agree with u/loosie-loo that this sub is a place where we sometimes need encouragement to seek out urgent/emergency care as we're prone to brushing off injuries or sudden changes in condition because are accustom to dealing with pain.
[job63za] (score 9, diepte 4) I don’t wanna freak you out, but… Unilateral swelling plus pain is a huge indicator of a potential clot.

I am not a doctor. This is not medical advice. I just have a clotting disorder, and… don’t brush this off. Go to the doctor. Do not pass go. They will want a d-dimer and an ultrasound, at MINIMUM. Depending on the cause, this is legit life-threatening.
[joakdvi] (score 7, diepte 2) Ok....Are you in the hospital rn?!?
[joc8uyi] (score 5, diepte 2) Let us all know how your appointment with your pcp goes! Sending you healing thoughts!
[joblguu] (score 5, diepte 0) You need a doc  that lymph edema is huge and im not a doc
[jocicig] (score 4, diepte 4) TBF, the majority of the posts were prior to OP’s comment that the swelling had been happening for six months and prior to mentioning they had a PCP visit scheduled. That information would have been helpful earlier.
[joa62ux] (score 4, diepte 0) I have to agree with everyone else that immediate medical attention is needed. So sorry for your pain. If you cannot make it to an urgent care or emergency room, I would ice it.
[joafi1i] (score 4, diepte 0) I'm starting to see more posts like these that are just bait. This picture probably isn't from op.
[joajnxs] (score 4, diepte 2) You can post in r/AskDocs, they’re pretty nice there.
[joaj8oj] (score 4, diepte 0) I know others have said this, but go to the emergency room immediately! Please! I know it's a horrible, stressful, difficult place, but this is what it's there for. Take care of you 💙
[jocnuk3] (score 3, diepte 5) Thank you, spicyhotcocoa, for voting on sneakpeekbot.

This bot wants to find the best and worst bots on Reddit. [You can view results here](https://botrank.pastimes.eu/).

***

^(Even if I don't reply to your comment, I'm still listening for votes. Check the webpage to see if your vote registered!)
[jocq2mv] (score 3, diepte 6) Did you go get your foot checked out?
[jode1rl] (score 3, diepte 6) Please cut your toenails and take care of your body, because she is special! She wants you to care.
[job2ng0] (score 3, diepte 1 OP) I'm thinking about going but I do have an appointment with my pcp tomorrow
[joc8y7s] (score 3, diepte 3) No, they really aren’t going to send a patient to the ER who has had symptoms for 6 months. The PCP is the best place for this.
[jod5w8h] (score 3, diepte 2) Well at this point I'm thinking you're at the PCP, so that's good. I hope you feel better!
[joaw9k6] (score 3, diepte 0) Holy shit go to the ER
[joah142] (score 2, diepte 1 OP) It's mine seriously it is
[joajovn] (score 2, diepte 3) Here's a sneak peek of /r/AskDocs using the [top posts](https://np.reddit.com/r/AskDocs/top/?sort=top&t=year) of the year!

\#1: [A thank you and happy ending.](https://np.reddit.com/r/AskDocs/comments/1367jjw/a_thank_you_and_happy_ending/)  
\#2: [Update on my husband with drooping mouth/other symptoms](https://np.reddit.com/r/AskDocs/comments/12rebr3/update_on_my_husband_with_drooping_mouthother/)  
\#3: [My fully vaccinated son (white, 7 years old, 4ft, 55 lbs) has no underlying health issues and is currently being treated for a sinus infection and Influenza A. A little girl in his class has cancer and we want to be as careful as possible. How long should we keep him home?](https://np.reddit.com/r/AskDocs/comments/zcpepu/my_fully_vaccinated_son_white_7_years_old_4ft_55/)

----
^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| ^^[Contact](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| ^^[Info](https://np.reddit.com/r/sneakpeekbot/) ^^| ^^[Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/o8wk1r/blacklist_ix/) ^^| ^^[GitHub](https://github.com/ghnr/sneakpeekbot)
[job1fsr] (score 2, diepte 2) Why aren’t you responding then? 

Have you injured that foot or ankle recently? Is this kind of swelling something which happens to you now and then? Have you ever seen a doctor when it’s like this?
[joc8zbo] (score 2, diepte 5) The good news here is that this doesn’t look like a clot. Remember that with clots you get the swelling because of the back flow of blood and for that to happen you need to have great vessels in the area, of which there aren’t any in the lateral ankle.

This is likely going to be more related to the joint itself. That doesn’t mean it shouldn’t be looked at, it absolutely should, but OP has an appointment with her pcp today, ant that’s reasonable for a problem that’s been occurring for 6 months.
[job74j2] (score 2, diepte 4) Are you a minor?
[joczzs2] (score 2, diepte 6) Then why don’t you go to a doctor? 

Several of us who spend time on a Chronic Pain sub, are telling you to please get your ankle checked out, stat.
[jobx2wz] (score 2, diepte 2) The pcp is going to send you to the ER. SAVE THEM THE TROUBLE AND YOU THE HOURS. GO.
[jobi0ps] (score 2, diepte 0) where exactly does it hurt.
[jobx183] (score 2, diepte 0) My father in law died from septic cellulitis in his heels that were less swollen.....
[joc9d44] (score 2, diepte 0) Echoing everyone else saying seek medical advice, but it looks to me like it could be Haglund's Deformity, bit hard to tell from the angle. The only way to know for sure and to start getting it  resolved will be scans.
[jocnte4] (score 1, diepte 4) Good bot
[joag0yg] (score 1, diepte 0) I fell down the stairs a couple days ago and I didn’t go get checked out, found a couple new bruises today when I showered. Now if I had swollen like that anywhere I would’ve went. I don’t go to the er but if one of my small feet was suddenly more than twice the size  one day I’d go get checked out too. Like if I woke up and saw that I’d go.
[joc96gv] (score 1, diepte 1) Why would you assume lymphedema? The only way to know that is by physical exam to see if there is or isn’t pitting?
[joc138p] (score 1, diepte 0) If this is about money, then go to an urgent care
[joc8qoj] (score 1, diepte 0) Please go to ER. If you’re broke get the charity papers so you don’t have to pay. This looks serious!
[jod56qn] (score 1, diepte 0) Go to a podiatrist. They are great on ankle foot issues. If you have an internist they may see you faster and would make a referral that will get you in faster. They may recommend a n orthopedic surgeon/specialist and they definitely want a referral. Go see someone that can see you the quickest. From the picture it’s obvious that something is happening and it doesn’t look good. Good luck and later you can tell us which doctor you went to for your foot/ankle. Don’t put it off.
[joej21x] (score 1, diepte 0) If you press on it with your thumb, does it leave an indentation? (It’s called pitting, Don’t do it if it hurts a lot obviously, I’m just wondering if it could be edema.)
[jok2gct] (score 1, diepte 0 OP) Update:PCP says arthritis and because I have a contract with my pain management doctor she can't prescribe me anything
[job2c6q] (score 0, diepte 3 OP) No injury my mom says it's pain and inflammation but I don't know the swelling has been there since December but the pain came and went until recently when it wouldn't stop hurting
[joc9wkh] (score -1, diepte 3) This has been an ongoing problem for 6 months. The ER isn’t going to do anything for this. They might apply a $50 ace wrap and give OP a $200 pair of crutches until she sees her PCP (who, by the way, she has an appointment today to see). Someone suggested she had a blood clot? In the area of the outside portion of her ankle… the one without great vessels so it’s not a clot.

This entire sub lost it’s damn mind over ankle swelling thats been happening for 6 months. JFC, if the people over on Ask Docs could see us now, they’d absolutely put it down to the type of hysterics they’d expect from a bunch of drug addicts who think that they know better than they do.

OP just wanted some tips on pain relief until she saw her PCP today, ffs.
[jobbmhb] (score -1, diepte 5 OP) Who me no I'm not
[jocj7vz] (score -2, diepte 5) Did anyone ask how long it’s been going on before screaming for OP to go to the ER? No. There were a lot of assumptions and hysterics.

Something as simple as, “if that’s brand new swelling, it needs to be seen urgently” over “you’re gonna lose your foot from ‘diabeetus’” and “it’s a clot, you need a d-dimer and an ultrasound!” etc, etc.

Lots of things can look scary without being scary and losing our collective minds over some chronic swelling on a chronic pain site is embarrassing. 

OP asked for tips for the pain. She got dozens of people screaming at her to go to the ER.
[joaabzg] (score -21, diepte 2) I… I’m honestly shocked that this is the response from this sub.

I totally sympathize with your statement and experience but the people in this thread are invalidating this persons request for conversation about her chronic condition and im just not gonna sit here and watch it without commenting.

OP is capable of communicating what they wish from us and its honestly, atleast it would be to me, very hurtful to see this community do exactly what we spend hours every day complaining about doctors doing to us - to one of us.
[jo9vg2z] (score -27, diepte 0) Why is everyone here telling someone posting in a *chronic* pain sub to go to the ER for something that is chronic?

I’d feel beyond disrespected if i shared my situation and instead is told that i dont understand what my damn ankle is doing. Clearly OP is posting here because they wanted support, not to be told to go to the ER….

Im sorry this is happening to you OP. Sending you lots of love from here. Hugs❤️

=== THREAD 17tqyfm ===
SUBREDDIT: r/goodyearwelt
DATUM: 2023-11-12  SCORE: 70  REACTIES: 53
TITEL: Alden Indy Review: My Feet's Savior
POST (source_id=post):
**Kick-off:**  
I've been deep into the Goodyear welt shoe game for a long while. I've had everything from Thursday Boots to stuff like Clinch and Vibergs. Alongside this, I got hooked on running, eventually hitting half-marathon status. But then, out of nowhere, my feet started rebelling – hello, plantar fasciitis. It started off feeling like regular arch/heel soreness, but then it just wouldn't quit, hanging around for a grueling two years. All my beloved boots turned into torture devices. I was down to Birkenstocks for any kind of comfort. I tried wearing shoes I didn't care for like Hokas, New Balance, Nike, etc., anything to help the pain but soft squishy shoes just made it worse. Eventually the podiatrist I saw said "ditch the soft rubber shoes and get something with firm arch support."

**The Indy Boot Steps In:**  
Facing continuous foot pain, I sadly started parting with my boot collection, piece by piece. I even tried those arch-support champions, the PNW boots, but my injured foot just couldn't handle the break-in. That's when I decided to give the Alden Indy boots a shot, thinking, “If these don’t work, it's Birks for life.”

**First Impressions:**  
The day the Indys arrived, I was a mix of hopeful and skeptical. I tried them on, did a few laps around the house. The arch support felt just right – noticeable but not too intense. Stepping outside for a real test, I immediately felt the pain. Despite all the hype about their immediate comfort, my feet were not on board. But their style won me over, so I decided to take it super slow with breaking them in.

**Two Months Down the Road:**  
By then, I had worked the Indys into my routine, wearing them around the house every other day. The initial outdoor trials still came with discomfort, but nothing too severe. Then, during a family walk, it dawned on me that the pain was fading. It wasn't perfect yet, but things were definitely looking up.

**Three Months and They’re Gold:**  
Fast forward another month, and the Indys were fully broken in, becoming my go-to for any outing. They transitioned from just bearable to genuinely comfortable. The transformation was amazing – my foot pain had subsided substantially (almost fully gone), and I was actually looking forward to walks. Had I had healthy feet, I'm sure these would've felt great in a matter of weeks.

**Life with the Boots :**  
These Indys haven't just been boots; they've been my trusty sidekicks through thick and thin.

There was this one time caught in a sudden rainstorm. I'm talking about the kind of downpour that makes you think you're in a movie. There I was, sprinting through puddles, expecting the boots to be a soggy mess. They held up like champs, keeping my feet surprisingly dry and comfortable.

Then there were those summer concerts. Dancing in a field, music's blaring, and the ground's turning into a mud-fest. These boots were caked in mud by the end of the night. Cleaned them up the next day, and they were good as new.

And let's not forget the casual hangouts. These boots have been spilled on more times than I can count – beer, soda, you name it. Each time, I thought, “This is it. They’re ruined.” But nope, a quick wipe and they’re back in business. They've been my go-to for date nights with the wife, adding just the right touch of rugged charm. 

I’ve worn them to cookouts where they've accidentally been baptized in barbecue sauce, and to snowy adventures where they've kept my feet warm and dry as I trudged through blankets of white.

In short, these boots have lived a life full of stories. From braving the elements to being part of my happiest moments, they've been more than footwear – they've been a part of my life's journey and foot recovery.

**Leather Care:**  
I've kept it real simple with these. Brush them before and after every wear with some conditioning twice a year. Once before the winter season and once after. That's it. They'll get the occasional wet rag treatment when they get salt from the streets, mud, etc. but I find that brushing is almost always sufficient on its own. If I notice some really ugly scuff, I use Shaphir's brown oiled conditioner and it does a great job at both conditioning and adding some of the color back. 

**Drawbacks:**  
Perhaps the only two drawbacks I have are the heel pads and ungusseted tongue. I've had to replace the heel pad on these 3 different times as they wear out incredibly fast. I've had Dainite heel pads that I've worn for years and still look new. I also wish the tongue was at least semi-gusseted. When they were new, I had to be very meticulous with the way the tongue rested on my foot to make sure it broke in correctly and not crooked where it slides to the side. They broke in nice and straight, but still wish this was changed by Alden.

**The Final Say – Worth Every Penny and Then Some:**  
Now, I know Weston from Rose Anvil and others have their opinions about these boots being overpriced, and yeah, maybe there are technically "better deals" out there in terms of materials for your buck. But, from my personal experience, these Indys are worth every single penny.

It's not just about the material quality or the brand name. It's about how these boots have literally transformed my walking experience. They've turned painful strides into comfortable strolls, something I hadn't felt in years. That kind of comfort? You can't put a price tag on it.

They've not just survived; they've thrived. And after all that, they're still going strong, looking great, and most importantly, keeping my feet pain-free. I'm sure everyone here can relate to something similar; you lose something you've always taken for granted and only then realize just how much you wish you could have it back. I got walks with my wife back, running in the yard with the kids back and not having to take a moment to stretch out my foot and sit down for a while.

So, yeah, I'll keep buying these boots, even if someone says there's a "better" deal out there. Because when you find something that works this well for you, you stick with it. The Alden Indys aren't just shoes; they're a part of my life. And for that, I'd pay any price.

**TL;DR:**  
Bottom line, the Alden Indy  have been a lifesaver for my feet. They turned what used to be painful walks into enjoyable strolls. If that's not a win, I don't know what is.

&#x200B;

https://preview.redd.it/htmjttqgqyzb1.jpg?width=3024&format=pjpg&auto=webp&s=339eee5779dacc28aa7e36bdbae81b386aeb7357

&#x200B;

https://preview.redd.it/n2igzsctqyzb1.jpg?width=3024&format=pjpg&auto=webp&s=5d422a7bf65cb2c4a3d63f1cab098b217784b868

&#x200B;

https://preview.redd.it/mwvthl20ryzb1.jpg?width=3024&format=pjpg&auto=webp&s=16fc494e58fdd2dcd8627c039a84ddcd27c777b5

&#x200B;

https://preview.redd.it/7v6qeib1ryzb1.jpg?width=3024&format=pjpg&auto=webp&s=256026230142a7c97a58d05dae2b2a54a361eb79

&#x200B;

https://preview.redd.it/8lquxn92ryzb1.jpg?width=1290&format=pjpg&auto=webp&s=a1ff08ba7d56ebdf41c497b02f422605f7923c43

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k8yqx67] (score 31, diepte 0) I am with you. The Alden Indy’s that I own are by far the best and most comfortable shoes that I have ever worn. I have always needed orthopedic shoes, and the Indy’s are the only shoes in my adult life that have fit the bill. I would pay almost any price for them, and they do last as long, longer than average, as you take minimal care of them. 

I respect Weston and what he does at rose anvil, but I think he has failed to see past what he, in his perspective, considers a pragmatic heuristic for evaluating these shoes. And he tends to apply his standards rather inconsistently; not calling this out as a bad thing. We all have our biases. But these shoes are much better than how he portrayed them. And the made in America aspect is worth the extra cost, at least to me.
[k8yxovg] (score 16, diepte 0) The worse thing about the Rose Anvil video is that anyone who disagrees is labeled a “fan boy” or Alden shill. I totally get that Grant Stone (as an example) makes boots with higher quality materials compared to Alden. But I have just about every boot model they make and I still can’t replace the comfort of the Indy boot. I don’t have foot issues but glad I have a set of Alden’s already broken in and ready to go should this happen to me down the line lol.
[k8zfd36] (score 15, diepte 1) Thursday should be on the same shit tier as Portland leathter, we demand justice
[k8ywzbt] (score 11, diepte 0) Thank you for such a thoughtful well written review!  This kind of deep long term experientially backed perspective is much more meaningful than a quick autopsy based analysis of materials.  Congrats on a great pair of boots that have helped take great care of your body!
[k903fg8] (score 10, diepte 0) Alden 405s were a kind of grail boot for me. I experienced comfort right away - like soul food for my feet. Unfortunately mine had  multiple QC issues
Your experience is what I hoped for. Alden delivered on comfort but now I’m without them and feeling let down by the company. My experience is just a one-off but still a major letdown on QC.

I agree about the Grant Stone Diesel. They have a hardier construction than the Indy and are a beautiful boot, not at all uncomfortable. But the the Indy arch and last are special.
[k8zro97] (score 8, diepte 1) I find the Trubalance last very comfortable but I found my AE Higgins Mill boots even more comfortable. I think you'll find many others will say their HM boots the most comfortable boots they own, yet no one gets upset when someone says that the AE boots are overpriced for their retail amount.
[k8zaqaj] (score 6, diepte 0) Awesome review, I’ve always said that getting my first pair of Trubalance was eye opening. I have many different pairs from different makers that fit me well, but I’ve never had a last fit me perfectly. 

Are those the 403 (brown cxl) with neocork sole?  If so then we have the same pair.
[k8yx40r] (score 5, diepte 0) I’m in the same situation 

How is the sizing between the PNW 55 and Alden Trubalance?
[k8zta3t] (score 4, diepte 0) Great review may I ask what is that jacket in the last pic it looks rad
[k93nqtp] (score 3, diepte 1) It's wild to me that a piece of footwear that you might be wearing for 10+ hours, isn't evaluated for **comfort.** The way Rose Anvil evaluates boots would be like if I evaluated noodle dishes, and did it on appearance and nutritional content *only* and completely discarded "taste/flavor" as a metric.  
 There should be a three-way balance (or more, depending upon what metrics we decide are most important) between durability, comfort, and appearance in *any* good review if **comfort** is one of the *key metrics.*
[k92eifi] (score 3, diepte 1) It’s AI written.
[k8zafux] (score 3, diepte 1) I wear the same size in PNW 55 (Nicks/Whites) as I do Trubalance, but I go up a width for Nicks/Whites.
[k8z7e4q] (score 3, diepte 0) Outstanding review!
[k8ztbb2] (score 3, diepte 1) ^[Sokka-Haiku](https://www.reddit.com/r/SokkaHaikuBot/comments/15kyv9r/what_is_a_sokka_haiku/?utm_source=share&utm_medium=web2x&context=3) ^by ^oman1205:

*Great review may I*

*Ask what is that jacket in*

*The last pic it looks rad*

---
^Remember ^that ^one ^time ^Sokka ^accidentally ^used ^an ^extra ^syllable ^in ^that ^Haiku ^Battle ^in ^Ba ^Sing ^Se? ^That ^was ^a ^Sokka ^Haiku ^and ^you ^just ^made ^one.
[k92s3ai] (score 3, diepte 1) One thing I can say, is that I don’t believe Rose Anvil is knowledgeable. He makes several mistakes in his videos and is bias due to the business relationship and paid reviews. One example was when he said the Alden cork sole would “hydroplane”, I have never slipped wearing my 403 when it was wet outside.
[k949dbw] (score 2, diepte 3) well, that might be- but these really aren't the same category of boot at all. Alden doesn't make *anything* with a safety or steel toe afaiaa, and that's going to almost be a requirement at a construction site. From what I understand the most popular "comfortable" work boots are going to be thorogoods, RW (setter, workz), Danner, and a few other brands that are all in the (essentially) 200-300 category, and have a safety toe.   


And the boots listed above are probably the BETTER options, a lot of construction workers not only don't have 600-700 to spend on a single pair of boots, they barely have 300 to spend. Not sure if it is still done, but there used to be a "work boot allowance" paid to workers to help them buy boots.  


So... while you're probably right, I'm not sure where that point belongs. Aldens aren't acceptable on a construction site in the grand majority of cases.  


Perhaps "comfort" is, unfortunately, a luxury category. It shouldn't be, but perhaps it is.
[k963nui] (score 2, diepte 4) By far the most seen boot on a job site is Thorogoods moc toe. I also see a lot of Redwing dynaforce and supersoles. Danner quarry boots and I do see a lot of lower quality boots like Ariats.
[k9dyxza] (score 2, diepte 5) I have literally never seen a pair of Thorogoods on a jobsite. Always Carolina, Georgia, Chippewa, Ad Tec, Timberland, Dickies, Wolverine, Carhartt, Ariat and Herman Survivor. Occasionally a Red Wing, which tends to be a one-time purchase once the guy realizes they're no better or worse than the less expensive brands. Brand new guys typically show up with Brama boots their first week and once they get their first or second paycheck, they come back with something useable.   


But no, twenty five years of jobsites in multiple industries in multiple states in multiple scales of labor skill, and not a single Thorogood. For that matter, no Nicks, Wesco, Whites, Aldens, Thursdays or Fryes, or any of the boots the internet obsesses over but average people have never heard of.   


Actual blue collar guys buy the lowest priced, moderately comfortable boot that meets the job requirements and maybe falls within their annual $100 equipment allotment, which is why you don't see Thorogoods at jobsites. Usually the guys that are wearing expensive boots are the guys in the office that don't actually do any labor work but want to pretend they're out in the field pounding nails, but those positions don't count as "at jobsite."
[k8zea0u] (score 2, diepte 1) From what I understand, most people wear the same in both. When I went to Alden Madison, they Brannock’ed me and said 8EEE Truebalance (same as my Nicks 55, my best fit) but did not have any in stock for me to try on. I have not since followed up.
[k8zuyd5] (score 2, diepte 1) I’m a 9F in the 55 and have Trubalance pair in 9E — they’re pleasantly tight/still really damn comfortable.  I do wear thin socks in em though, but thin are perfect for my climate.  An extra E would probably hit perfectly.
[k932kgg] (score 2, diepte 4) I am just pointing out what I think is a fair price for what you get. If you could get the Aldens at 40-50% off retail, then they would be a fair offer. I think AEs are a $250 boot and I think Aldens are a $350 boot.
[k91t2t9] (score 2, diepte 2) Idk why so many people been hating on him in this sub lately. I think he is doing us all a service by breaking down what it is we actually are paying for. I think it goes without saying that all boots (or shoes for that matter) should be comfortable after breaking them in, so giving the Indy’s credit for being comfortable is such a moot point. Objectively these boots are crazy overpriced for the materials used and assembly. Weston’s assessment was spot on. If they made them as well as red wings or White’s and charged the same, the price would be right imo.
[k92f8ov] (score 2, diepte 3) It's the fact that he doesn't apply the standards and critiques equally. Companies that pay him for a review are shown in a favorable light and people take what he says as an objective review.


He is loose with the truth in videos and he also sold email addresses despite stating he would not: https://www.reddit.com/r/Boots/s/MgjXyDOx5b
[k92rehr] (score 2, diepte 1) Agree with everything you say. Grant stone uses better material but man that 403 is just so comfortable and stylish, maybe not my coolest boot, but they one I would keep. But there are still a lot of Alden fan boys (check styleforum). The boot could fall apart in one wear and they would just ignore it.
[k93pf0w] (score 2, diepte 1) So if I evaluated hamburger restaurants and ignored **taste** as a metric, and only looked at price and the supposed quality of the beef, you'd be ok with that? Because that's what RA does, and it's why his reviews are shit when it comes to an item where *comfort* is a key metric.  


I mean, we don't leave these on a bookshelf on display. they get worn.
[k91uwkt] (score 2, diepte 0) > I know Weston from Rose Anvil and others have their opinions about these boots being overpriced

That dude only focus on materials and nothing else tbh (and even that he wasn't knowledgable). Yes he long term review the alden but it was biased imo. I don't think he know what's the focus of Alden is and seem to be comparing it to PNW.

But in general here and there, I realize he only talk about materials, and even then he doesn't long term it to see how it plays out.

The most recent example was him talking about affordable alternative and praising Grant Stone. He never once talk about the speed hook hardware or danite sole clone. My thought was this dude never long term these to be talking. The weak point of GS was those two. I got trickster's danite sole that last longer and the speed hook on red wing, wesco, truman, and nick of mine last longer.

Next year I'll get some Alden and actually wear it to see if it's good. I don't trust his review anymore.
[k9249yi] (score 2, diepte 0) Well written, I also think my Indy's are my most comfortable boots by far. I bought mine nearly 10 years ago, they were not as expensive as now and the competitive landskape was different too. Value is a difficult thing with these, they are definitely fragile compared to Viberg or English makes that I have in my rotation, but unique in their style and comfort.
[k92eehk] (score 2, diepte 0) Does everyone have to use AI to write their posts now?
[k93s6e2] (score 2, diepte 0) To anyone reading this, do you all have other boots that you find really comfortable?
[k940w8j] (score 1, diepte 2) >It's wild to me that a piece of footwear that you might be wearing for 10+ hours, isn't evaluated for comfort.

Go to a construction site and ask guys if their boots are comfortable and you might be surprised. Blue Collar guys don't take care of their bodies often times.
[k96acsr] (score 1, diepte 5) which is in that $250 - 300 price range (the thorogood). I've never worn a pair so I can't speak to comfort.
[k96l0y2] (score 1, diepte 6) Ya I think its cause most worker live paycheck to paycheck so they ain't gonna spend it on a boot, but a lot of jobs give out boot vouchers yearly. $100 to $200 range.
[k96jt05] (score 1, diepte 5) Work boots of that capability are waaaay overkill for my uses, but I always relate the story of when I was in the Redwing store looking for Rangers. While I was waiting for the man I spotted a banged-up old Dynaforce too far gone to rebuild so they used it as a “sample” for their tuff-toe composite dip. It was my size so I laced it up and walked around. It was the most comfortable boot I’d ever put on - perfectly fitted to my foot and beyond broken-in. I told the guy “Name your price” but they only had the one and wouldn’t sell anyway.
[k96a2pe] (score 1, diepte 4) Yes but you are intentionally watching a channel that has a blue collar POV. That’s why I made my comment.
(35 reacties met lagere score weggelaten)

