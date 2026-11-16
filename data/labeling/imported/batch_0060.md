# Label-batch batch_0060

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
Schrijf het resultaat naar `batch_0060.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 13rjdgb, etykrf, 1aqdypo, 5d97m7).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 13rjdgb ===
SUBREDDIT: r/Residency
DATUM: 2023-05-25  SCORE: 125  REACTIES: 99
TITEL: How do you get your feet not to smell like death during a 24 hour shift?
POST (source_id=post):
During my 24h shifts I have a couple of hours of mandated sleep, but its too embarrassing to take off my shoes to lay down in the bed. I would have to admit my coworker sleeping in the bed next to me for severe toxic fume inhalations. 

Not U.S. btw.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jlkjo31] (score 141, diepte 0) You may need to buy new shoes. This happens to me when my shoes get old. Also baby powder applied directly to your feet helps before putting your socks on
[jlklycg] (score 57, diepte 0) 1. Wash your feet daily
2. Dry your shoes and sole separately (useless if the stink has begun) AND use dryer sheets when not wearing
3. Use running socks
4. Buy 2-3 pairs of shoes and rotate between them
5. (If you can't afford a new pair try using 40-50% alcohol-solution and spray it into the shoe and perhaps buy new sole-inlays)
[jlkr00f] (score 49, diepte 0) Fun new word, its called bromodosis. Usually, it's caused by types of bacterial or yeast populations. To stop it, we need to eradicate the existing population and stop creating their ideal habitat.

- Ensure your feet are 100% dry before putting on shoes. Don't jump out of the shower and throw your shoes on, they're still wet. If that needs to happen, take your shoes off while reviewing charts in the AM so they can airdry. Do this periodically as able throughout the day. 
- If you're on a 24 hr shift, plan to change socks halfway through.  
- Spray all shoe insides with alcohol (can buy online or just make your own). This will kill the bacterial populations. If it's more of a yeasty thing (can differentiate based on nail appearance) vinegar can be helpful. This may need to be a daily thing until the populations are completely destroyed. Alcohol will start to degrade glues and leathers, so be judicious in use. 
- Alternate foot wear. This gives them time to dry out.
- Talc and other powders can help absorb the smells and can be temporarily useful. However, they are typically cornstarch based and will be feeding the bacteria/yeast.
[jlklxo1] (score 47, diepte 0) Good socks. I wear heavy duty smartwool myself. They are 50/50 wool and silk. They wick away any sweat and feel amazing. ER nurse for 16 years.
[jlkoo81] (score 23, diepte 1) Costco has really nice Kirkland brand wool socks
[jlktgal] (score 19, diepte 1) I have stink foot. To add to all the above: synthetic fabrics tend to stink a lot more than natural fibers. Almost anything merino wool you can wear for a couple days with minimal stink. Also there are cedar pouches you can put in your shoes when not wearing them. Never don’t wear socks.
[jlkq9y9] (score 16, diepte 1) Wool socks are the key. Change then mid shift if you have to. They are a game changer and once you start wearing them you'll never go back to anything else.
[jlkl4ou] (score 14, diepte 0) Try Lume cream or Carpe powder..works like a charm.
[jlkrk2d] (score 10, diepte 2) If shoes are the tires and feet are the suspension, socks are the shock absorbers. We don’t think of them much, but good ones make for a comfy ride.
[jlku7gu] (score 10, diepte 0) Just drench your smelly feet with axe body spray. That should ensure that no coworkers stay nearby you long enough to complain.
[jll2lam] (score 9, diepte 1) Yep! Usually time for new shoes
[jlkw61n] (score 9, diepte 1) Rotate shoes
[jllpfvu] (score 7, diepte 3) Nah, you’re good, I was agreeing with you
[jlkssci] (score 6, diepte 3) For real. I've seen recommendations here for thin running socks, which is like the worst thing you could do, synthetic which retains bacteria, poor wicking, poor durability, zero space between your foot and insole for air flow, and, as you mention, zero shock-absorbing. Nothing beats a mid-weight, mid-height, high merino wool content sock. Bombas, SmartWool, etc.
[jllkr26] (score 5, diepte 2) sorry, I'm not a native english speaker :< should've said change lol
[jlko523] (score 5, diepte 0) Foot powder in your socks before you put them on.
[jlkwi98] (score 5, diepte 0) Drug stores/grocery stores carry Hibiclens (chlorhexidine), use it on your feet everyday in the shower. 

Also, as already has been pointed out, you may have a foot skin infection. If you have peeling/scaling/mild blistering in between and around the toes, then for sure you do. 

If so treat first with clindamycin or mupirocin; and if those don’t work, consider an anti-fungal

Then either get rid of your current footwear and buy new; or thoroughly bleach all your shoes (if they are washable) and let them dry COMPLETELY before wearing again

Also, only wear socks that are bleach-able, and wash them with bleach every time
[jll8ybr] (score 5, diepte 0) I'm not sure why reddit is showing me this sub reddit. I'm not in the medical field,  but I can recommend anti-microbial socks to keep your dogs from barking. They're a little bit more expensive than normal socks they got silver threaded in, but IMO worth it. Did a 23 hr kitchen shift once, goldbond powder and socks kept a pretty good lid on it.
[jlklbta] (score 4, diepte 0) This only happens to me when I’m wearing thick non athletic socks. When I wear my Nike dri fit socks this doesn’t happen. Also depends on the shoes I’m wearing.
[jllfesz] (score 4, diepte 1) Shoe deodorant spray helps too. I walk everywhere in chi. Target had them.
[jlkplr9] (score 4, diepte 0) You take a shower, change scrubs, undewear, and socks. I even take a different pair of shoes for the night portion. This way, I trick myself into thinking this a whole new shift. It works for me.
Also, foot powder helps.
[jlkuig3] (score 4, diepte 0) I had this problem. Acquire seven pairs of shoes and wear them in strict rotation one day a week each.
[jlky4oc] (score 3, diepte 1) Mando, Lume's manly version of the cream
[jll8b4v] (score 3, diepte 1) Darn tough works well for me
[jllqqt2] (score 3, diepte 1) Specifically, wash your feet before putting on your shoes (ie shower before work) and try getting a stiff shower brush to actually clean them. 

I rock climb and wear climbing shoes without socks for a couple hours, the smell is atrocious if I go after work without showering
[jlkqfkm] (score 3, diepte 0) Wash feet in vinegar water
[jll9z13] (score 3, diepte 1) I had this once a few years ago and bought a foot spa to soak my feet in chlorhexidine (diluted obviously). After about two weeks of doing it every night and buying fresh shoes and socks it totally fixed the problem - it's been about 6 years and hasn't come back!
[jlmeuoz] (score 3, diepte 0) Stay out of the puddles of mystery fluid on the floor of the morgue
[jllpi4r] (score 2, diepte 4) Yeah, I mean thin socks of any kind suck for extended wear.  But I have no issues with thicker moisture wicking synthetics, I have quite a few pairs of pro compression. They’re pretty durable and my feet are fine at the end of the shift.
[jlnl1m6] (score 2, diepte 2) Darn tough and sockwell compression socks are the real winning moves.
[jllnk3g] (score 2, diepte 1) For people who prefer plant based options, hemp does a good job too with moisture wicking.
[jllomle] (score 2, diepte 1) I prefer rapid dry compression socks.  I use the variety designed for marathoners.  They wick away moisture and keep me from finding my feet have turned into sausages at the end of a 24 mostly spent on my feet having walked like 15 miles.  Plus they come in fun designs and colors.
Love my smart wool socks in the winter. It they can get hot and don’t provide an compression.
[jlkn2r2] (score 2, diepte 0) Depends on how busy you are on call, but i always had time to brush my teeth before going to bed on call. Then wash your feet, put on fresh socks. And get some new shoes  or crocs like clogs.
[jlkqjcw] (score 2, diepte 0) Soak the inside of your shoes with 90% isopropyl overnight. Like really soak them. Eliminates the smell for at least for 3-7 days
[jlkvb2h] (score 2, diepte 0) Multiple shoes you rotate through during the week. Always make sure socks and shoes are dry before putting them on. 

Bring a clean change of socks and swap them out mid shift as well. 

My feet smell clean all week long.
[jm2dj2s] (score 2, diepte 6) This is a clinical diagnosis, treatment is empirical, culture is rarely done

The findings are not "raging", most patients don't even realize they have it, or think their feet are normal.

I said "mild" blistering, which is common between and around the toes

The cause is multi-factorial, but one specific diagnosis is "pitted keratolysis" which you can look up
[jlljsu1] (score 2, diepte 0) My dawgs used to always be barking until I got some gold bonds foot powder. I put some on my dawgs before I put my socks, and put some in my kicks along with some disinfectant spray. Works wonders
[jllrhl2] (score 2, diepte 0) Wool socks and crocs/Birkenstocks
[jllrnbe] (score 2, diepte 0) In addition to great suggestions others have made, try cedar shoe trees. These will help your shoes dry and will absorb some odor. The plan: 1. Wash and dry your feet. 2. Wear merino wool socks. Smartwool or Darn Tough are two good brands. 3. Rotate your shoes to allow at least one day between wearing . 4. Wear shoes with quality leather uppers. 5. Use shoe trees.
[jllstm6] (score 2, diepte 0) Lysol disinfectant spray the inside of your shoes and then use Arid Xxtra Dry spray on your feet.
[jlma0bd] (score 2, diepte 0) Lume Body Wash & Lume Deodorant (rub the cream kind on your feet) & cotton socks!
[jlmjzlu] (score 2, diepte 0) When you save someone’s life, the impending death needs somewhere to go.  Just before you hit the rack go out in front of the hospital and dump your shoes out into the garden, NOT THE TRASH CAN!  People will wonder what you are doing. Tell the truth. People need to know the kind of stress you are dealing with.  BTW thwarted death smells WAY worse than impending and actual death. I’m sorry no one told you this before you entered medicine
[jlnjm9v] (score 2, diepte 0) Change socks every 12 hours. Avoid waterproof shoes.
[jlkhoof] (score 1, diepte 0) Thank you for contributing to the sub! If your post was filtered by the automod, please read the rules. Your post will be reviewed but will not be approved if it violates the rules of the sub. The most common reasons for removal are -  medical students or premeds asking what a specialty is like or about their chances of matching, mentioning midlevels without using the midlevel flair, matched medical students asking questions instead of using the stickied thread in the sub for post-match questions, posting identifying information for targeted harassment. Please do not message the moderators if your post falls into one of these categories. Otherwise, your post will be reviewed in 24 hours and approved if it doesn't violate the rules. Thanks!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Residency) if you have any questions or concerns.*
[jlnyoxz] (score 1, diepte 1) Commented before I saw this, but I’ll say here as well that Lume is amazing!
[lpw56pl] (score 1, diepte 3) if shoes were tires and horses were feet
[jlnr7xk] (score 1, diepte 2) bamboo socks are great too
[m53284g] (score 1, diepte 1) Which socks brand?  And how are they in summer. I’m a firefighter and curious what may help
[m532zud] (score 1, diepte 2) SmartWool. And they with great in summer. I wear the heavy duty hiking ones.
[jlku9m4] (score 1, diepte 1) This! I have sweaty feet and adderall makes them even sweatier thus stinkier. I powder my shoes regularly to soak up moisture both when I’m putting them on and taking them off when they just sit there. Could buy new shoes, but those will stink too so foot powder to the rescue
[jlkoze2] (score 1, diepte 0) Get new shoes and rotate between them. Find Amlactin or Kerasal or a scrub to help exfoliate your feet. Wear wool socks. Keep your nails short.
[mmcg9fq] (score 1, diepte 1) I have begun spraying with alcohol and then microwaving my shoes right after. I have gotten another microwave to do this. Also it may effect the shoes potentially but with the shoes in question I don’t care
[jlkskom] (score 1, diepte 0) Shoes that have a plastic sole and holes on the side of the shoe for the shoes to breath. Crocs are honestly some of the best. I recently bought the echo clogs (looks like a cross between yeezys for some reason), and the literide crocs (looks like sneakers).
[jlkt2ht] (score 1, diepte 0) Wash them good. And wool socks.
[jlku9qf] (score 1, diepte 0) All of the above and spray your feet and shoes with deoderant after every shower
[jm0ph5b] (score 1, diepte 1) What is the peeling/scaling/blistering?
[jm0t16w] (score 1, diepte 2) I’m not sure I understand your question 

I meant peeling OR scaling OR mild blistering

Do you not understand what these terms mean?
[jm0wdfi] (score 1, diepte 3) My question is what is the cause. I'm thinking that you believe tinea is the cause. If prescription medication (eg econazole) fails what else could be the cause ? Does anyone ever test this stuff or does everyone just assume tinea?

Edit: just re-read and you suggest mupirocin as first line treatment so you might have a bacteria in mind. What bacteria?
[jm0y0m0] (score 1, diepte 4) No, I would treat bacteria first 

According to my dermatologist wife (not one of their main diagnoses, but they see it enough), first line therapy is clindamycin, and second line is “pick something”
[jm136xh] (score 1, diepte 5) But what bacteria is causing skin peeling and open wounds like that? Clinda is prescription only, so there's hundreds of people with trench foot using OTC topical creams when they have a raging bacterial infection? 

Is this why we're seeing chronic wounds progress to nec fasc?
[jm3nhq7] (score 1, diepte 7) Thank you!
[jlkx4ku] (score 1, diepte 0) Foot deodorant spray, it’s a thing
[jlkxszr] (score 1, diepte 0) Several changes of socks
[jlkxzxi] (score 1, diepte 0 OP) Soak your feet in water w baking soda and a bit of vinegar. Scrub them and put Vicks on them once dried, learn this from a wound nurse. It works 🤷🏽‍♀️ I do this every shower.
[jlkzm4v] (score 1, diepte 0) All the above and mint flavored tea bags in the shoes daily
[jlkzqu6] (score 1, diepte 0) Get new shows and rotate the shoes and socks allow them to dry out. Use some powder to keep the shows clean while you work. I learn this from hanging out at nurse station.
[jll0vwm] (score 1, diepte 0) Paka socks leather shoes
[jll4jsw] (score 1, diepte 0 OP) Also! These help: extra foot bath middle of day, alcohol spray, foot peels, powders, medical check for fungi with treatment if necessary, 2-3 pairs of work shoes that you rotate to allow others to dry, boot dryers or a cheap box fan in front of your extra shoes to help them dry faster.
[jll56ll] (score 1, diepte 0) Clip your toenails, get a scrubber for the shower (East Asian stores have great rough ones). Lather up, and rub out the subungual and intertriginous areas at the end of every shower. Dry well. Get white athletic socks so you can bleach them, use a fresh pair every day.
[jll5sis] (score 1, diepte 0) OP — I’ve tried it all and there’s one method that I’ve settled on as it’s 100% effective. Rub your feet with zinc oxide powder (non-nano). Super cheap too. Don’t waste money on foot deodorants and powders. They mostly don’t work all that well. It’s not enough to keep your feet clean and dry and clean — they WILL perspire and lingering bacteria will feed.
[jll5uve] (score 1, diepte 0) Ugh I had the same issue, and I’m a girl. So embarrassing and I would just keep my shoes on and my feet not touching the bed. This was intern year. ONLY thing that worked for me was to throw away the stinky shoes, get new ones with a breathable insole (memory foam is a NO NO) and alternate the use. Of course, washing your feet daily, clean socks etc, but for me, once the shoe was stinky, I could not save them.
[jll8z1f] (score 1, diepte 0) Darn Tough socks have a lot of wool options that hold up against odor. Also there are shoe sprays around that are basically reverse spray cans you hit the inside of your shoes with. 

That being said, even with the above I come home and take my shoes off and it’s “damn I need some soap” time.
[jll9ssb] (score 1, diepte 0) That’s the neat part, you don’t.
[jllbahm] (score 1, diepte 0) I swear by Dr. Scholl’s Odor-X Spray
[jllbjhz] (score 1, diepte 0) A few strategies! 

1. Bring a fresh pair of socks and change ~halfway through your shift 
2. You can take the insoles out of your shoes, throw them in the wash and then then air dry. Most of the smell comes from the insole
3. Wash feet daily with soap and water
4. Arm and hammers baking soda based shoe spray also works wonders, i bring it with me on 24 call shifts, and spray it in my shoes when I get a chance to take them off and lay down
[jllcbqh] (score 1, diepte 0) New shoes 

Drysol spray [aluminum chloride ] . You can also get it in powder
[jllckc9] (score 1, diepte 0) I got you. 

As someone who had smelly feet most of life until med school here are some tips 

1) Throw away all of your old shoes and get news ones. This is the most important step. Yeah it sucks but they are growing bacteria/fungus that you are just not going to be able to get rid of, and its easy to cross contaminate, even when you change shoes during the day.  I would also recommend buying new socks and throwing away the old ones, but not as important as buying new shoes 

2) Wash your feet with Antibacterial soap for feet, 

3) Dry your feet completely before putting on socks, you can use talcum powder or deodorant if your feet are sweaty 

4) If you have any evidence of Athlete's foot (itchy, dryness, flaking) use terbinafine 

5) Use a clean pair of socks every day, and change socks when you change shoes. 

6) If its really bad, bring a plastic bag to put your shoes in and extra pair of socks when you are in the call room. 

I went from not being able to take off my shoes in a locker room (because of the smell) to being able to take off my shoes whenever I want with zero smell.
[jlleilr] (score 1, diepte 0) Leather shoes make the difference. "Man made uppers" on the shoe label is death to feet. Leather is the way to go to avoid your feet stewing in their own sauce and smelling up the place.
[jlletn4] (score 1, diepte 0) Leather soled boots or shoes breathe better, plus wear pantherella wool socks.  Likely the best you can manage.
[jllphio] (score 1, diepte 0) Drown yourself with Axe body spray
(27 reacties met lagere score weggelaten)

=== THREAD etykrf ===
SUBREDDIT: r/ems
DATUM: 2020-01-25  SCORE: 465  REACTIES: 99
TITEL: Don’t keep you feet on the dash UPDATE
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ffjduei] (score 194, diepte 0) Absolutely wild, I saw the x-ray post a couple days ago, wow!
[ffjkyno] (score 166, diepte 1) I would just throw ketamine at that until it didnt bother me any more.

Anybody in that much pain will add so much stress to the scene and transport. Just put em out.
[ffjg15y] (score 153, diepte 1) Hmmmm.....could be a dislocation.

Let's get an x-ray to confirm.
[ffjfmqj] (score 126, diepte 0) I thought an update would be how the patient is doing.
[ffjg5if] (score 119, diepte 2) "Mild crepitus during palpation"
[ffjl7nk] (score 117, diepte 2) Personally, this is my solution to all my problems. On and off the rig.
[ffjkbia] (score 110, diepte 0) Legit question. Like how would you deal with transporting that. Like extricating them, and then moving them onto the cot.

Like obviously you won't see that injury  until they're extricated from the vehicle (unless they're conscious and tell you "hey my femur head is poking out"). 

Also, this is a good reminder of why it's important to get patience who meet the critea "trauma naked". I know some people in my department value modesty too much.
[ffjspu6] (score 100, diepte 1) Butt naked—->position of comfort with splinting and void padding as appropriate—>as much analgesia as you can manage without getting fired—->transport
[ffjqad0] (score 83, diepte 2) They are now
[ffjq8qc] (score 51, diepte 3) Far out man.
[ffjwh2d] (score 45, diepte 3) for sure. realistically i'd probably just take multiples of 5x9's and 4x4's soaked in saline and dress what appears to be the femoral head to prevent gross contamination at the site. it's probably already fucked from an infection standpoint but if i can keep the fibers and hairs from my truck out of it that's a plus.
[ffjx6l5] (score 45, diepte 1) It’s for medical reasons and the bits are blurred out. Chill man.
[ffjq35l] (score 41, diepte 1) I would fucking hope so
[ffjmo8f] (score 37, diepte 0) Imagine trying to do the wound care for that over the weeks and not trying to get staph
[ffje94t] (score 34, diepte 0) That is disturbing
[ffjw3mv] (score 31, diepte 2) Agreed, maybe consider some wet to dry dressing as well to keep it covered and moist.
[ffk29x4] (score 26, diepte 1) It took me 15 seconds to figure out what it was. Holy crap.
[ffjxn7v] (score 26, diepte 1) Yes, ahe is also a child apparently. I can't even comprehend this poor girls pain.
[ffk1wu3] (score 24, diepte 4) good for you doc, never said it was educational, i said it was medical, and not porn.  But now that you put it in my mouth, it is educational, pictures are educational. This is a sub for EMS, we enjoy seeing medical pictures, we get people trauma naked and don't start jacking it. My point was this isn't porn. I can't call a doc a retard on the job, but i'll call you one right now. Is reading comprehension not part of the MCATS?
[ffjoz5m] (score 23, diepte 0) Is...is this patient a girl?
[ffjrkcy] (score 22, diepte 4) Hmmm.....could be bursitis.

Let's get a CT to confirm.
[ffju4u2] (score 21, diepte 1) Its /r/ems, and labeled NSFW. What did you expect?
[ffk3tx4] (score 21, diepte 6) I'm not.
[ffkagk5] (score 20, diepte 3) 68W?

You want me to change my socks and stop having unprotected sex with thots off base?
[ffkay81] (score 20, diepte 2) This guy manages scenes and circumstances.
[ffk0etj] (score 20, diepte 2) there are no clues to identity. are you sexually stimulated? i don't know if you've seen porn, but this isnt it,  it's medical.
[ffkb62p] (score 18, diepte 3) That’s the ketamine u/kenks88 is talking about. Better living through chemistry.
[ffkqc5z] (score 18, diepte 3) My guy I’m not claiming to know the persons intentions that posted this photo but stuff like this doesn’t happen every day and tbh I’m glad I saw it; it’s super neat and sparked a discussion of “what would you do”. If you’re thinking of this in a sexual way you’re fucked in the head.
[ffjflul] (score 17, diepte 0) Noooooooooooo
[ffk7ekg] (score 16, diepte 4) I for one found it educational to read how various people would extracate a patient with this type of injury, treatment, and transport. As a doc patients arrive to you, but ems we need to trouble shoot care in the field. Had no idea it was even a child till I scrolled down further. Child or adult, I never went over this kind of injury in school. Also educational to prevent people from putting legs on dashboard.
[ffll20p] (score 16, diepte 1) This is real certified trauma shit. I'm a former EMT turned dispatcher and the vast vast vast majority of calls are usually just people who are sick to varying degrees.

After a few nights of "I've been having knee pain the entire day but it's 3am and NOW I want to go hospital" you'll be looking forward to "EMS 5, MVA unknown injuries..." 

And even then, most of them don't look like this. Don't be skittish.
[ffk2d4l] (score 15, diepte 1) Or the parent(s) being charged with a crime.
[ffkalpx] (score 15, diepte 2) I’ll admit one of my mental coping games is I tell myself pain is like an on/off switch and somehow there’s a limit to how badly she’s feeling this
[ffjje8o] (score 14, diepte 3) The question is, what came OUT of their leg.  Let's just stay the inside stuff is now on the outside.
[ffjo5kv] (score 12, diepte 3) There you go

https://www.reddit.com/r/medizzy/comments/esicmt/legs_were_up_on_the_dashboard_during_a_car_crash/?utm_medium=android_app&utm_source=share
[ffkpmb7] (score 12, diepte 0) My ex used to do this. I asked her not to every time. Thankfully myth busters has a sfw yet convincing video about the perils of being dumb
[ffkozyg] (score 10, diepte 4) You forgot the 800mg Motrin and to drink water
[ffjejlt] (score 10, diepte 1 OP) Oops forgot glooking
[fflajnn] (score 10, diepte 0) I’m an EMT student who’s just started taking classes, it’s pictures like this that make me think maybe this isn’t the job for me...
[fflnewa] (score 10, diepte 1) Most calls arent trauma patient and the few that are generally arent this severe. Most are car accident related around here or sometimes related to house/yardwork and are fairly straightforward as far as rating back to what you get taught during certification. 

I wish I ended up with more calls like this tbh so I could do what I signed up for...Anyway, not to try to discourage you or gatekeep, but I recommend evaluating if you truly want to become an EMT as we all see and must be ready to treat people who can be missing quite a bit of themselves or come up on scene where people are in pieces. Is it for you? It's up to you. Just be aware you could be the guy who sees all the worst stuff whilst working long hours. Everyone has different tolerances. Think about it
[ffk7inf] (score 8, diepte 6) What does that even mean?   I don't care if this guy is the medial director of a level 1 trauma center and two auxiliary burn units,  he's a retard.   Sadly we've all known retard doctors,  docs are people too,  their title gives them no right to speak nonsense and have it heard as if it is any more special than if the janitor went off on a tirade about something.   Stop being a tool.
[ffk8jxs] (score 8, diepte 6) By the look of your profile your one sad, disrespectful piece of shit.
[ffk6kym] (score 8, diepte 2) You're a moron,  this is well enough anonymized medical image, you need to just go sit in the corner and reconsider what is actually a right and a wrong in the world.   Serious question though,  what the fuck is wrong with you?
[ffl090h] (score 7, diepte 1) Femur head sticking out of her groin
[ffjzi0n] (score 6, diepte 2) [Here you go!](https://www.reddit.com/r/medizzy/comments/esicmt/legs_were_up_on_the_dashboard_during_a_car_crash/?utm_medium=android_app&utm_source=share)
[ffm6n61] (score 6, diepte 2) When the K hole starts looking like a gravity well
[ffkbzr3] (score 6, diepte 4) Exactlyyyy
[ffkw7i0] (score 6, diepte 5) Reading this gave me great joy.
[ffk6qn9] (score 6, diepte 4) If it isn't for INFORMATIONAL ( no one said  educational but it definitely is)  purposes,  what pray tell do YOU see it as,  cos we,  we see it as informational,  you,  I don't know what kind of mind you have on those shoulders,  but clearly you're seeing something no one else here sees. A bit obsessive with your view of this photo.  You seem to have some weird hangup,  I guess you've not been around these parts much,  cos this is pretty par for the course,  HIPAA is fine with this,  you can go sit in the corner and untie your little crotch knots this has you all tied up with.
[ffksdqh] (score 6, diepte 0) I have no idea what I’m looking at
[ffjl43m] (score 5, diepte 1) Link?
[ffjeoby] (score 5, diepte 2) What went into their leg?
[fflnqrc] (score 5, diepte 1) Depending on how Gucci I was feeling this may just be an RSI on scene prior to removal from the vehicle
[ffk5emt] (score 5, diepte 6) Weird
[ffka1mc] (score 5, diepte 1) On one hand, this is a fascinating case from a medical perspective.

On the other, taking pictures of patients crosses a personal boundary for me.

Fortunately my org policy is crystal clear.
[ffjzglw] (score 4, diepte 2) [Here you go!](https://www.reddit.com/r/medizzy/comments/esicmt/legs_were_up_on_the_dashboard_during_a_car_crash/?utm_medium=android_app&utm_source=share)
[fflzkgo] (score 4, diepte 1) > Legit question. Like how would you deal with transporting that. Like extricating them, and then moving them onto the cot.

Turn the patient's lights off and then stabilize with a vacuum mattress.
[ffkr4hp] (score 4, diepte 5) Yeah you’re right, it was wrong of me to say that. The way the dude I was originally replying to sounded that way and it could have been misconstrued. I’m on the back half of a 24 so I’m pretty tired, but my point still stands regarding the first part of the comment I just posted. You don’t normally see this and it’s nice to have a discussion of “how would you manage this”. I feel bad for the poor kid, but it helps us be better able to help someone else in the field if this were (ever) to happen. Which I hope it doesn’t cause it looks like it sucks.
[ffm8tpp] (score 4, diepte 1) I guarantee you like 99% of people in EMS have never seen something like this before. Not to say we don’t see awful injuries but this is an exceptional case
[ffkwhaf] (score 3, diepte 7) Amen
[ffkfchc] (score 3, diepte 4) I’m an RN and I agree, this picture, if taken and posted without consent, is definitely crossing the line. The X-ray was anonymous and acceptable as educational intent. This is a photo of a minor in a horribly unfortunate circumstance. Her shirt could be recognized and used to identify her. What if one of her classmates finds the photo and passes it around?
[ffkn61b] (score 3, diepte 0) Dear frightening gods.
[ffjzcpa] (score 2, diepte 1) Link to the x-ray?
[ffl79j1] (score 2, diepte 2) do you know what happened to the patient?
[ffova60] (score 2, diepte 3) The injury is a pretty unique one, just wait until the parents find out someone has an unedited nude of their child on their phone. Losing your job will be the LEAST of your concerns
[ffmeztn] (score 2, diepte 1) People responding that this is “anonymized” are missing the point. You need to both anonymize images like this and also have consent to share or publish it, which the photographer almost certainly did not have. It’s also 100% a violation of hospital policies.
[ffmhwoq] (score 2, diepte 2) you absolutely zero evidence there was no consent by parents.
[ffmmze8] (score 2, diepte 1) I'm not an EMT but I did work in a hospital and l dealt with my fair share of uncontrollable situations. I found that thinking about general things a head of time and what I wanted to do or how I wanted to react helped. You tell yourself a head of time that if things get dicey I still need to do X. Also trust in your training and the advice you get from real EMTs. Lastly the first time you go through something stressful/challenging is always hard. Just stick to the basics and do what you're trained for. You'll get through it.
[ffn997j] (score 1, diepte 3) Thank ya boss man!
[ffpwe1w] (score 1, diepte 3) I'm probably the last person to ask, but I don't think the injury you see in the image is life threatening.
[ffq1xdy] (score 1, diepte 4) probably not, but seeing a doctor after this will at least calm you
[ffksj9v] (score 1, diepte 1) [Yes](https://www.reddit.com/r/ems/comments/es0ngs/dont_put_your_feet_on_the_dash/ff8rnws/)
[ffowcob] (score 1, diepte 7) Interfacility EMS is in full force in this convo...
[ffp46ta] (score 1, diepte 4) I don’t, because if I see something like this, which I haven’t,  I don’t have time to take photos, but where do you think trauma photos come from? You know, all the ones in text books you surely have read. There’s no evidence there wasn’t permission. Do I work in the medical field? No I work at blockbuster
[ffpq7v1] (score 1, diepte 5) Textbook photos are not obtained from 3rd party random EMS providers.

Have fun explaining permission to an employer who will not be down with a minor’s photo being posted on the internet.
[ffot1ms] (score 1, diepte 1) Lol, people are downvoting me for asking a legit question as the OP took a photo of a child’s genitals
[ffk43uz] (score 1, diepte 0) Wow
[ffkjns1] (score 1, diepte 0) I can’t tell if this is the front side or back side?
[ffmydwu] (score 1, diepte 1) Coming home with these injuries or putting her legs on the dash?
[ffmyr91] (score 1, diepte 2) Putting her legs on the dash
(18 reacties met lagere score weggelaten)

=== THREAD 1aqdypo ===
SUBREDDIT: r/Serverlife
DATUM: 2024-02-14  SCORE: 1662  REACTIES: 97
TITEL: Contracted party... Almost kissed their feet!
POST (source_id=post):
Thought it could be a mistake until thanking them after.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kqcbrdn] (score 748, diepte 0) I woulda been like you need me to come over and clean ur house too?
[kqcejep] (score 375, diepte 1 OP) Contracted 13 top private room, but dropped 2 down to 11.

Contracted minimum was 1500 but after cocktail and wine ended up there.
[kqcdpj9] (score 350, diepte 0) How many people and how many damn items did they order??? Lol that’s a huge bill
[kqdq0i0] (score 168, diepte 1) That would have been hard for me to say while blowing whomever paid.... /half joking?
[kqccti5] (score 160, diepte 0) Dammm that’s a month rent and car payment for me
[kqcesuj] (score 104, diepte 2) Wtf!!!! That’s awesome!!!! Congrats!
[kqcfq80] (score 101, diepte 0) I thought it said poo 😂
[kqcd99y] (score 97, diepte 1 OP) Same! January and up until tonight has been scary slow.

Still can't rely on one night to catch up though.
[kqcg2pd] (score 62, diepte 1) You get a car payment and rent for 700?! Is it a shoebox and 2014 Honda civic ?
[kqcg4hq] (score 55, diepte 1 OP) I used math to confirm that that was not the case😉
[kqchtgi] (score 53, diepte 3 OP) Happy cake day!
[kqce1ks] (score 52, diepte 0) Plus the 1/4 grat is just pure beauty. Congrats dude
[kqcei9l] (score 35, diepte 0) Where do these people work that get these insane tips? I haven’t served in over a decade, I would for that kind of money though lol.
[kqcg5gg] (score 26, diepte 2) I’m including the gratuity also 😂
[kqcfchq] (score 25, diepte 1 OP) I didn't have to but definitely shared.
[kqclbxx] (score 24, diepte 1) Have you ever seen bottles of wine on a menu that cost $200 or more? That type of place is going to add up to this kind of total for 11 people 4-7 bottles of decent wine plus $50-100 per person for food maybe a round of cocktails is another $200 then add tax and fees
[kqhrq7z] (score 20, diepte 2 OP) That's why I ALMOST kissed their feet.
[kqcjcto] (score 20, diepte 4) Thank you 🙏🏼
[kqdimlp] (score 20, diepte 3) Its a contracted party, in their contract they agreed prior to service to a 25% gratuity for the staff. The 2nd line is for additional grauity, they tipped an additional $700. this came after service.
[kqcht5f] (score 20, diepte 0) Gotta love the double grat
[kqdjg72] (score 18, diepte 5) This check was $2372. Both grauities go to the server. Their total tip was $1255 over 50% on a ~2500 check
[kqcg4b1] (score 18, diepte 0) ![gif](giphy|BPJmthQ3YRwD6QqcVD|downsized)
[kqcf8j4] (score 17, diepte 0) I'm sure you deserve that and more! Hope you didn't have to share it!
[kqcdgnv] (score 15, diepte 0) I would’ve shined their shoes for them 👞
[kqcmpn6] (score 15, diepte 1) I’m so glad I wasn’t the only one who thought this.
[kqcg8lg] (score 13, diepte 3) Didn’t even see that lol. Still, in 2024 that’s pretty good.
[kqcfyua] (score 13, diepte 2) That's nice of you! You're a better person than me! 😂
[kqci3ia] (score 11, diepte 1 OP) Sure didn't ask if they were sure it not.
[kqcx6h9] (score 10, diepte 2) I'm not from the us, how does this work? Looks like there are to different *"gratuities"*. Are these distinct from each other in some way?
[kqdjl7n] (score 10, diepte 6) Yo that's sick. Glad it happened to somebody!
[kqcelad] (score 10, diepte 1 OP) Happy cake day!
[kqchlbo] (score 9, diepte 2 OP) Or multiply by a roommate. Live in Boston so that's definitely not paying full rent.
[kqdifrg] (score 9, diepte 1) Added together That's 60% of my rent and I live alone🥲 gotta love the average rent in my cory literally doubling in the past 10 years
[kqcgk7n] (score 9, diepte 1 OP) Coups and bow tie at work... ✔️
[kqckmmc] (score 8, diepte 0) That looks like a Darden ticket 🥳 if so I’ve had some pretty good contracted parties as well
[kqch0ni] (score 6, diepte 1) If you multiply that by 4? Where do you live?
[kqcmlgd] (score 6, diepte 3) Happy Cake Day!
[kqdj2wo] (score 6, diepte 4) So does the contracted 25% go to the severs or the business?
[kqcerjm] (score 6, diepte 2) Thank you 🙏🏼
[kqcui7r] (score 6, diepte 1) Expensive and busy restaurants
[kqggzdf] (score 6, diepte 1) I work at Hotel Drover Autograph Collection in Fort Worth Texas and our servers gets this size tips consistently. Just gotta find the right place!😁
[kqcfclb] (score 6, diepte 0) bro…. ain’t no way…
[kqcxiyk] (score 5, diepte 3) They are adults capable of financing a $3,000 dinner.  They are not only capable of making their own decisions, but they are likely better at making life decisions for themselves than I would be for them... given our relative situations, I feel this fact is taken as obvious.
[kqdng7s] (score 5, diepte 3 OP) Contract was discussed prior along with gratuity. 

I was happy with their agreed 25 percent gratuity so need for me to trick them into a double dip.
[kqcrdw4] (score 5, diepte 0) Hell Yeah! Good for you.  Im not a gambler, because I get it every day with my tables.  But these kind of tables give me the ‘jackpot’ feeling.
[kqce4hl] (score 4, diepte 0) Sheeeeesh!!! <3
[kqhse3f] (score 4, diepte 2 OP) Where do I send my resume?
[kqckvn3] (score 4, diepte 0) That is awesome and they are amazing.
[kqcn9a9] (score 4, diepte 0) I wanna work where you are holy shit
[kqdnocm] (score 4, diepte 1 OP) The 25 percent was already agreed upon in the contract.
[kqd9ro7] (score 3, diepte 1) Happy cake Day
[kqchcvh] (score 3, diepte 0) YAS!
[kqctw9j] (score 3, diepte 0) The way they corrected the 7 makes it look like the tip line says “poo” and the 11 year old boy inside of me (I’m just a crude, middle aged AFAB woman) was like “heh…it says poo”
[kqdnxxf] (score 3, diepte 1 OP) Doesn't always work out in my favor, but tip out is based on sales. Would it easier with 12.. if I didn't share.
[kqd6tfo] (score 3, diepte 0) Bet they didn't realize they already tipped 25%
[kqdbysu] (score 3, diepte 0) Wait OP did you get autograt & the listed tip as well?
[kqessys] (score 3, diepte 1 OP) Their company.
[kqffag7] (score 2, diepte 3) I’m in MA too! But central. I found a little spot in the middle of (wealthy) nowhere and make AMAZING money. So happy to see you hit it!! Congrats!!
[kqgpq3h] (score 2, diepte 2) is this at a capital grille?
[kqxlbx2] (score 2, diepte 2) Ur so real for that…also yayyy! Glad you got a good tip ☺️🫶
[kqir2xi] (score 2, diepte 1) I am still trying to figure out what it says
[kqfap1e] (score 2, diepte 4) Probably a work dinner… at my work if it’s under $300 per head I don’t even need to submit a receipt ($500 per head for executives), so I usually tip exorbitantly when I’m expensing dinners
[kqsr3by] (score 2, diepte 4) I would say it's very unscrupulous to not double check in this situation. All it would take: "hi, I see you left a very generous tip, thank you, just wanted to make sure you were aware an auto grautity had been applied already".

I have a team leader role at my company and I take my team out for dinner once a year. We would rack up this kind of bill and get pretty drunk, maybe not notice the auto grat and just tip out of habit. However I'm not swimming in money and my kids could use that 700 dollars. If I noticed this the day after I'd be fucking pissed. To imply that someone spending this money on an evening out is less entitled to their own money is... Kind of sociopathic.
[kqdnz2x] (score 2, diepte 4) Ah gotcha, couldn't tell from the previous comment. Congrats on the recognition of a great job
[kqcq5zi] (score 2, diepte 0) POO ——
[kqctl2v] (score 2, diepte 1 OP) Could of kept most, tip out is based on sales.  

Tonight was a win but can go both ways.
[kqctbry] (score 2, diepte 1 OP) 💯
[kqcytdw] (score 2, diepte 0) That’s amazing!! Happy happy day!!
[kqd81tq] (score 2, diepte 0) Thought it said “poo”
[kqdpmbn] (score 2, diepte 0) Congratulations!
[kqe6ahm] (score 2, diepte 1 OP) ?
[kqe2lyd] (score 2, diepte 0) Congrats!
[kqe92xo] (score 2, diepte 0) I thought it said “IOU” at first
[kqeg2nr] (score 2, diepte 0) Nice! Good job!
[kqek9ka] (score 2, diepte 0) But can you do it again?? 

JK JK JK, very jealous, congrats homie!
[kqekwc7] (score 2, diepte 0) Fuckin noice!
[kqf4r9j] (score 2, diepte 0) Plans for the 700 doughnuts you got
[kqfrbr2] (score 2, diepte 0) I would have washed their feet with precious oils and dried them with my hair, ala a Bible story. Shit, I'm bald.
[kqgg1xo] (score 2, diepte 0) Good job!!!
[kqh6kle] (score 2, diepte 0) Damn! That's a 50% tip. I've occasionally picked that up on small checks, but never like that. Congratulations!
(24 reacties met lagere score weggelaten)

=== THREAD 5d97m7 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2016-11-16  SCORE: 84  REACTIES: 96
TITEL: BIFL or at least a couple of years... Shoes
POST (source_id=post):
So I recently found BIFL and realize that I am clueless and have always bought cheap and replaced often and trying to change my way of thinking.

Now I need to pick a new pair of shoes for work, I typically wear jeans and khakis, with button up shirts (tucked in), no tie.

I typically buy no name brand $30 brown shoes that I constantly complain about hurting my feet and that start looking horrible after 2 months of wear.  My main concern is comfort as my arches always hurt in dress/business casual shoes and I am wondering if its the cheap shoes I buy.

Any suggestions?  I normally wear a size 13 with my clown feet.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[da2q1kz] (score 30, diepte 0) If you want to get into BIFL or at least buy it for long term shoes, the defacto entry level brand seems to be Redwing. The Iron Rangers and Beckmans are great boots. They're constructed using a Goodyear welt so they can be resoled. Check out /r/goodyearwelt for more. 

Disclaimer: I own both the IRs and the Beckmans.
[da2w2bn] (score 17, diepte 0) There are two things to look for in a shoe that will last: first it needs to have a welted sole (there will be stitching around the bottom between the sole and the upper), which is necessary for easily replacing soles (which wear out much faster than the rest of the shoe). The second thing to look for is leather that is thick and preferably unlined; if there is leather on the outside, but a layer of cloth on the inside, it's a bad sign since a lot of cheapskates use cloth to make the leather feel thicker than it actually is. 

Keywords to look for: Full-grain leather, Welted/Goodyear Welt, Vibram Sole,

Keywords to avoid: "Genuine Leather" (this is actually an industry term that refers to a cheaper, thinner kind of leather than "full-grain")

Chippewa, Thorogood/Weinbrenner, and Golden Fox are good places to start when you're looking for boots and oxfords that are business-casual and last five or more years. 

Red Wing and Wolverine (which were suggested in this thread) are more the kind of boot you get after you know exactly what you want. 

reddit /r/goodyearwelt should be able to give more specific advice
[da2wszd] (score 16, diepte 0) Alden or Allen Edmonds
[da32hdf] (score 11, diepte 0) I wear Dr. Martens because they come with a lifetime warranty.

http://drmartensforlife.com/
[da329te] (score 10, diepte 0) FYI, long ago I read a rule of thumb: three pairs of shoes worn alternately last as long as five pairs bought sequentially.
[da323s1] (score 9, diepte 1) I have 6 pairs of AE's. One of them is 6 years old that's gone through 2 re-soles. With a bit of polish, it looks like new. 

Edit: Have to add that I am tough on my shoes. Oil industry, plenty of cobble and gravel walking, in rain, sludge, whatever. Also I used to completely abuse them by wearing them every single day. AE fanboi for life here...wearing their Higgins Mill today.
[da2zcav] (score 8, diepte 1) I second both of these. I work on concrete floors all day and wear Red Wing 606s daily. My weekend boot is the Iron Ranger and my dress shoe is the Beckman Oxford. All are fantastic shoes that I've owned for over 3 years. My 606s are worn for 11 hour days 5-6 days a week and are still comfortable and durable, 3 years later. My Beckmans make great formal or dress-casual shoes, and my IRs look great in nice jeans on weekends. Cannot go wrong with Red Wing.
[da2v1tq] (score 8, diepte 0) People seem to like Ecco and Cole Haan for comfort but I can't speak to the durability of either.
[da31t0z] (score 8, diepte 2) I disagree on the Ecco. They are very durable for wearing to the office for years.
[da2t74g] (score 7, diepte 0) Also - SAS. These are probably the shoes your grandpa wears (worn?). They aren't stylish but go with khakis, are made in the US, and good for your feet!
[da2x2jq] (score 7, diepte 0) Keens! I have flat feet, they are gloriously comfortable. And I am still going strong after two years.... which is unheard of for me, since I normally kill shoes within a year.
[da2xtvj] (score 7, diepte 0) I have had good luck with merrel shoes personally. They make a slip on that usually lasts me 3-4 years of light, most days use.
[da3a8df] (score 7, diepte 3) Yes, but "common sense" is often wrong.  Especially when it is "common sense" being used to retroactively try to find an explanation for some "rule of thumb" that is questionable.  What needs to dry out exactly?  The rubber?  The waterproofed leather?  Or just the lining?  Is a damp lining going to cause the rubber to wear out faster?  What if the lining isn't damp?  How do you know how long it takes for the lining to dry out?  What if it is summer and you live where the humidity is 80% so they simply will never get drier than that?
[da2va39] (score 6, diepte 2) There's also the Redwing Classic Oxford if you want a little more dressed up, but same rugged construction.
[da32l11] (score 6, diepte 2) Ill never understand how someone can be so stupid as to say "there are better alternatives" and list zero. Unbelievable.
[da2yry6] (score 6, diepte 1) My Merrel Moab Ventilator is the best walking shoe I ever owned, however it does not last long..

I take daily [outside] walk which are between 1 mile and 7 miles [depending on other life factors].

I go through about 2 pairs a year.  And their quality control appears to have nose dived within the past 2-3 years.  

For me; the space behind the right heel wears out first.

I also have a pair of Merrel Hiking boots which only gets worn a couple of times a month at most.  I also have a pair of black Merril sneakers which I usually wear to clients because they look more 'fancy' than regular sneakers.  I Expect both of these sets of shoes to last a lot longer than my daily walking shoes.
[da30xvs] (score 6, diepte 0) Clarks Desert Boots have always lasted a few years for me.  I have three pairs of various use and for different uses.  They look great with jeans or chinos and are pretty standard issue for mfa. Go down a size to a size 12 and they should fit great.  Get the original ones with the crepe soles and beeswax color.
[da2vjvu] (score 5, diepte 1) Those are fashion brands, there are far cheaper brands that are more comfortable and longer lasting.
[da387tf] (score 5, diepte 2) Yes, shoe's need time to dry out between wearings, so if you have more than one (2 or 3 at a minimum), they will last much longer if you don't wear the same pair two days in a row.
[da2z6og] (score 4, diepte 2) I got a pair of Red Wing desert chukka boots and they are really durable and I get compliments on them all the time. They're a little more dressy than regular work boots from Red Wing.
[da2tn5h] (score 4, diepte 1 OP) HAHA those are what my Grandpa wears! I never even considered them just thought they were "Grandpa Shoes" but hey if they feel good on 95 year old feet they should work for 25 year old feet.  I'll go try a pair on.  Thanks!
[da2w6mm] (score 4, diepte 2) Yeah. Suggest some.
[da31u54] (score 4, diepte 0) [deleted]  
 ^^^^^^^^^^^^^^^^0.138618932)
[da3elm7] (score 4, diepte 4) The leather in the shoes needs time to re-stabilize its humidity level. Among other things, shoes tend to be water-resistant towards the outside so they "breathe" to the inside. The high humidity plus sweat/salt/oils lead to deterioration of leather, leading to mold etc. The same thing happens when people store leather in plastic tubs in the basement. That drying/stabilizing is one reason they recommend cedar shoe trees--the unsealed cedar is dryer than the leather, and cedar oil is an antimicrobial.

They test how fast shoe leathers allow humidity to pass through (the transpiration rate, or something) as part of the tanning/designing process for shoes. Or, at least, some do.

The 3 pairs of shoes vs 5 pairs ratio would be hard to quantify with so many variables, so you'd have to rely on anecdotal evidence.
[da3dj00] (score 4, diepte 0) Adidas Sambas. 

Still have a pair of beaters from 2010, they used to be my everyday, but after 2013 they turned into my gardening shoes. 

No holes, no tears, sole is still in almost top shape, with a lot of abuse biking, skate boarding, hiking, disc golf, on top of everyday wear and tear.

And I picked them up at the time for 45 USD from Kohls.
[da2tlgr] (score 3, diepte 1 OP) I really like those IR's.  They might be a bit too casual with khakis but I may keep my eyes peeled for days I wear jeans.

Thanks!!!
[da2tzao] (score 3, diepte 2) If you want a little more formal,  the Beckmans or merchants might work for you.
[da31h7r] (score 3, diepte 2) Don't underestimate IR's and Khakis. I wear that combo daily and it's a great look that fits well in to a casual, but professional, office environment. 

Even if they are well worn, it helps to keep them conditioned and buffed. If you are going to keep them conditioned, buy a shade lighter than you want since they will get darker with conditioning.
[da3nbff] (score 3, diepte 2) Great shoe. Make sure you get fitted. They run a little large.
[da2ziqe] (score 3, diepte 1) I think you mean the 1000 mile boot. They are about $350-400
[da33xr7] (score 3, diepte 2) I think it was assumed that after you walk 500 miles, you'd likely have to walk 500 more, you know... just to be the man...
[da36mbw] (score 3, diepte 2) I second this. My AE's don't get worn as much because they're a bit more dressy than I like in my current work environment
[da370bw] (score 3, diepte 2) You should be kinder to your fruit.
[da36ype] (score 3, diepte 1) Is there anything to back up that "rule of thumb" though?  Or is it just an old wives tale rather than a rule of thumb?
[da4qc6c] (score 3, diepte 8) "Made up nonsense?" "Almost all" common wisdom is wrong, eh? Okay.

Your big hole disappears once you put your foot back in it. Is overnight long enough to dry? I'll leave that to the experts... who have already studied this and drawn conclusions and shared them.

Military boots of the same style started falling apart during trench warfare and jungle environments, because of the increased moisture and conditions to which they were exposed... and because rotating to another pair of boots each day was not an option. The deterioration/falling apart of those boots led to redesigns in materials and methods... such as using textiles instead of leather in the sides of jungle boots.

You may refer to (some kinds) of leather as "very slightly absorbent", but that applies to a smaller group than you might think... and highly vs slightly is a semantics issue. As a class, leather is absorbent... and the less treated with finishes, and the more worn it is, the more absorbent it is. The inside of leather is, essentially, unbrushed suede. You can read up yourself about suede stains, cleaning, and care.

Or, you can decide that your one measurement of moisture levels of one person's shoes after one day of wear, and again three days later, is a better representative sample of all footwear by all people in all climates and use cases, than the combined experience of those who make, repair, and warrant shoes, as well as those have a great financial incentive to make leather footwear last longer, and the resources to actually study the conditions that would help leather (whether saddles, books, shoes, or anything else) to have a longer useful life.

A parallel line of reasoning could be about the lack of proof that exercise, long-term, has any physical life-extending benefits... because the only way to get a perfect study would be to prevent the control group from exercising until they died. However, you can draw some limited conclusions based on imperfect studies, and the combined experience of doctors, the aged, and coroners.

Look at what the human handling of virtually any leather does to it. People who maintain museum artifacts can tell you all about it.

Or, forget all the above, and find out for yourself. Buy three identical pairs of shoes. Wear one pair every day for a year. Then store them. The next two years, alternate days with pairs two and three. Then compare them.

It just might be that you find the second two pairs are in better shape after one year of use (ie two calendar years) than the first pair was. You don't have to take my word for it, and certainly don't have to believe my qualifications, experience, or the conclusions of my study... or those of anyone else. You can find out for yourself.
[da32im2] (score 3, diepte 0) Birkenstock London in brown. Replace the soles every few years. BIFL.
[da33mrx] (score 3, diepte 0) Made in England doc martens. They may not last for life but they will certainly last a few years minimum. I usually get 5 years per pair with daily use.  They make dress shoes too, just make sure you find ones that are made in the factory in england.
[da3k7tb] (score 2, diepte 1) I've been considering Iron Rangers as a general shoe for awhile, before I ever saw them endorsed here. I'm sold.
[da33k7l] (score 2, diepte 3) Thats good to hear on Ecco, I just bought a pair to replace a disappointingly short-lived shoe.
[da37jjj] (score 2, diepte 3) Agree. I bought a pair of AE McAllisters and they are a little too shmancy for me given the ambient scruffiness of my wardrobe. Look great when dressed up though. Guess it depends on one's own calibration of "business casual".
[da389r1] (score 2, diepte 1) The pair that I bought in April came apart within 4 months or sporadic wear. The sole separated from the upper under the ball of my right foot. I'm very particular in my care for the various pairs of boots I own- to the point of routine brushings, oilings and insertion of shoe trees when they're not being worn.

While they look nice, and I know a lot of people love the Desert Boot, but the build quality is in no way BIFL in my experience.
[da31lng] (score 2, diepte 0) It depends where you are too, for instance if you don't properly care for them salt used in the winter will destroy shoes. What kinda weather are you looking at?
[da31q70] (score 2, diepte 0) Ecco shoes will last a very long time.  More expensive but in this case you will get what you pay for.
[da44bz3] (score 2, diepte 6) Any reason to doubt the recommendations of the shoe manufacturers?  If I sold shoes I would make more money long-term by selling you, say, five pairs in a row than to sell, say, three pairs at one time.

If your liner has higher moisture, so does the interior of the leather.   The liner is not a sealed environment.  The interior (especially) of leather is highly absorbent.

The moisture leads to mold, yes, but also stinky shoes.  That's one reason for airing them out.  The shoe trees help dry out the liner's moisture, and also the leathers, because there is a moisture level delta between the wood and the shoe's interior.  The shoe trees additionally reduce creases/folds in the leather (which has an aesthetic benefit but also a longevity benefit because dust/dirt in those creases acts as an abrasive, physically damaging the leather fibers).

There's a lot of misinformation passed around as fact, I agree.  For further reading, look at the research done by and for the military on boot development (especially around WWI and trench warfare, then again in Vietnam with jungle warfare).  Or, ask a shoe cobbler the effects they see with people who wear the same shoes nearly always.  Or, read through leatherchemists.org's forums or write Waldo from the Leather Lab at the University of Cincinnati for a summary of his research/certification of leathers for particular applications.  Or, read through some of the studies that led to the development of British Museum Leather Dressing, or the study the Library of Congress did for leather-bound book preservation.  Or, ask shoe manufacturers about the challenges they face with neglect and warrranty issues when their recommendations have been ignored.

There are a lot of wives' tales out there, so I can't fault you for doubting any particular one.  However, there's no special reason to question this one.  If you want your shoes to last longer, brush them off when you remove them and don't wear the same pair every day.  You can believe me (a fellow internet stranger) or doubt me, but if you heed the suggestion you'll save yourself a lot of reading.
[da4ajeg] (score 2, diepte 7) >Any reason to doubt the recommendations of the shoe manufacturers?

Yes, there is a reason to doubt all "common wisdom".  Because it is often wrong.  They don't need to be trying to harm you to repeat a myth.

>If your liner has higher moisture, so does the interior of the leather.

No, it does not.  I already told you that.  Test it yourself instead of assuming.

>The interior (especially) of leather is highly absorbent.

No it is not.  It is very slightly absorbent.  The moisture leaves the big hole where your leg goes, it does not take the path of most resistance into the leather.

>The moisture leads to mold, yes, but also stinky shoes.

Yes, but we are not talking about smelly feet.  You can not support the claim that resting shoes for 3 days makes them last longer by saying it makes them less smelly.

> For further reading, look at the research done by and for the military on boot development (especially around WWI and trench warfare, then again in Vietnam with jungle warfare).

None of which supports the idea of rotating shoes.  It is all on construction.

>However, there's no special reason to question this one. 

There does not need to be a special reason.  The fact that almost all of this "common wisdom" is wrong is enough reason.

>but if you heed the suggestion you'll save yourself a lot of reading

I'm more interested in facts than believing made up nonsense.
[da39k7u] (score 2, diepte 2) Well it's been a long time, so I want to say I learned it on CompuServe.
[da34fee] (score 2, diepte 0) Expensive shoes doesn't mean your feet won't hurt.  Find a pair that fit right or get superfeet to match your arch.  Otherwise you have to get a custom orthotic.
(58 reacties met lagere score weggelaten)

