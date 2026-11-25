# Label-batch batch_0146

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
Schrijf het resultaat naar `batch_0146.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1j0twwm, 1tpg6kb, ihutrp).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1j0twwm ===
SUBREDDIT: r/AmazonFC
DATUM: 2025-03-01  SCORE: 16  REACTIES: 62
TITEL: Theres too many options which safety shoes ended up hurting your feet
POST (source_id=post):
I'm trying to  pick new shoes but I got like 20 options I like don't know which to pick
So I want to know which brands yall have ended up regretting

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mfeb98j] (score 24, diepte 0) go reebok or keen. and go wide
[mfebz9x] (score 8, diepte 1) Ironically both of these killed my feet and dug blisters into the heels. Skechers and surprisingly a volcom pair have been my favorite
[mfec4fg] (score 6, diepte 0) I'm a big fan of Red Wings, but they don't have them on Zappos
[mfeel4w] (score 5, diepte 2) Seconding Volcom, every pair I tried killed my feet up until these
[mfec4p4] (score 5, diepte 0) Also, go a half size or a full size up. The toe box is generally smaller on steel/composite toe so you don't want your feet crammed.
[mfec6ty] (score 5, diepte 0) I tried 10 different brands over the years and the only brand that doesn't have me in pain is Airwalk. I get the mid top version for good ankle support.
[mfedsag] (score 5, diepte 0) Reebok safety shoes are Hella comfortable.
[mfef2g7] (score 5, diepte 0) Timberland Pro is the only correct answer
[mfejrxt] (score 4, diepte 2) sketchers are comfortable but do not last for very long.   did you get wide?  reebok and keen have been great for me and i have big foot probs and i'm over 300lbs and i don't move like it.
[mff8sj5] (score 4, diepte 1) Those killed my feet, I tried 2 different ones and they both did the same thing
[mfensc6] (score 4, diepte 0) Depends on the person's feet. What some people find comfortable are horrible in my experience.  I have a high arch and can't wear the normal shoe size I would wear. Safety shoes, in my opinion, cause more foot problems.
[mfejy3o] (score 3, diepte 2) https://preview.redd.it/cthrxu26k1me1.png?width=1834&format=png&auto=webp&s=e368c2ab1e48a1e708189e1c98d41c7ac948be7e



i have wide feet and i have several pairs of reebok.    
also i have a torn  meniscus and  fucked up feet.  i can stand for 12 hrs in reebok
[mfeqcnp] (score 3, diepte 1) Totally second the Keens and going wide. I’ve had probably 6 pairs of safety shoes in 3 years. Most were horrible. I switched to the Keens, go up half a size and get a wide. I add a thin insole. I NEVER have pain in my feet.
[mfexmxu] (score 3, diepte 1) I second Red Wings. I ended up getting a hiking boot style and a set of memory foam inserts. Amazing feeling and they always have great deals in their clearance section at a brick and mortar store.
[mfee4jx] (score 3, diepte 0) i got some rebok ones last year tht fckn sucked idk whay they were called so avoid em all
[mfeibyd] (score 3, diepte 0) GET TIMBERLAND PRO. THEY ARE ALL COMFORTABLE.
[mfeux3f] (score 3, diepte 0) I have yet to find one I actually find comfortable.
[mfezxe0] (score 3, diepte 0) Obviously I can only speak for myself but even getting the size Wide or extra wide the cap of the shoe is way too tight around my toes. I recently went with the Timberland Sawhorses. And although you still end up paying like $7 out of pocket, they have been the most comfortable out of the other 4 pairs I got. The New balance were terrible and the Thorogoods were even worse for me. I went wide in all selections. The Timberlands are manageable but still tight. 

Pro Tip for others with wider feet and the same issues-

Take a baseball or something of the sort and jam it into the shoe smacking it in with a hammer. Be careful not to stretch too far, use your common sense, but letting the ball or whatever sit inside of the toe cap for a day or two can make a world of difference for comfort. You have to make sure you are smacking it in with a hammer or something though to make sure it's even working.
[mfhbwvb] (score 2, diepte 3) Thirding Volcom. On my second pair and love em.
[mfeifry] (score 2, diepte 1) Facts! I have the black and purple pair this year, the fusion flexweave. I also ordered the black and green insoles for when the standard ones wear down (that part does wear fast on the reebok shoes I've noticed)
[mfef0iq] (score 2, diepte 0) Nautilus have been the best ones, I tried timberland, sketchers,  rebook they all hurt my feet, until I found this ones, Zappos and employees credit should be enough 109$ trust me you'll feel will appreciate it.
[mfftz9b] (score 2, diepte 2) Yeah as long as you buy them yourself.  Safety tried to hassle me at first. But I showed them rule doesn't say they're not allowed after 2 weeks just that Amazon won't supply them after 2 weeks.  They expect you to have your own Safety shoes by then. But definitely get a size bigger.
[mfgftav] (score 2, diepte 3) My HR told me I had to have a doctors order accommodation in place to use the OSHA toes and I was like wtf?! She’s like…ya you can’t even get them outta the machine. I was like…watch me….walked over, scanned my badge and a pair dropped down for me. Like…for real…know 100% ur job before runnin’ ur mouth 🙄
[mfgpiyp] (score 2, diepte 6) No you don't need accommodations. They are OSHA approved footwear. They can't deny you from wearing them.
[mfeau8l] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[mfexqh1] (score 1, diepte 2) Can find any brand besides keen that has size 15 wide or double wide
[mffc83a] (score 1, diepte 3) New balance has extra wide widths. My husband wears them. I haven't seen the Keens in an extra wide myself.
[mfgltz1] (score 1, diepte 2) I have heel issues with most shoes, including Amazon safety shoes. My fix was getting thick ankle socks. Reebok wides are my go to now
[mg2gxn7] (score 1, diepte 2) Skechers worked for me Reebok was the worse
[mfec55r] (score 1, diepte 0) I hated my carhartt tennis shoe looking ones
[mfeijc9] (score 1, diepte 1) You can see your order history on zappos! Glad because I almost ordered the same boots I returned last year.
[mfeiovb] (score 1, diepte 1) The nautilus Tempest shoes were the worst I ever ordered. At least a size too large at my normal size, and they felt so heavy. I like my reebok once I change the insoles.
[mfeicyz] (score 1, diepte 1) 100%
[mfg0gpd] (score 1, diepte 1) I used them but considering switching since they are bothering my feet now.  Going to try Keen.
[mfeiyqk] (score 1, diepte 0) Timberland and the sketches was a big no switched to keen utility my feet do not hurt
[mfek3s1] (score 1, diepte 0) I got the Stratus ct wide those have worked wonders so far
[mfel2x8] (score 1, diepte 0) Go with the wide fitting
[mfelyjn] (score 1, diepte 0) I needed light weight, so I go by the weight - my Reeboks were the lightest weight. They're comfy, no problems.
[mfelzwc] (score 1, diepte 0) Timberland Pro was my worst choice my first 60 days once January '24 came I got a different pair (Avenger Boots) and I've been fine since. Just got my 2nd pair of Avenger boots this year and no regrets
[mfemq23] (score 1, diepte 0) Try Skechers, are really comfy
[mfemx3o] (score 1, diepte 0) I hated the lack of toe space and had heel pain. The trick for me is getting wides and slapping in a heel gel insole ontop of the insole supplied. Glued it on.
[mfeqsbp] (score 1, diepte 0) Best thing to do is buy your own OHSHA Toes and put them over your most comfortable sneakers
[mffbio6] (score 1, diepte 1) is this allowed?
[mfgimw3] (score 1, diepte 4) Right, I had to take safety to HR and explain to them both that OSHA toes has to meet all safety standards or Amazon would never pass them out.  They would be liable for any injury if they weren't approved.
[mfgjrz7] (score 1, diepte 5) So it’s true then? You have to have an accommodation to use the OSHA toes?! If that’s true, why can you get them out of the machine?
[mfesnop] (score 1, diepte 0) Go PUMA
[mfrhjab] (score 1, diepte 1) There alright I think the sketchers r still a bit better but the pumas look nice xD
[mfevdsx] (score 1, diepte 0) I didnt regret it but i only use the reeboks and have been happy
[mfevevs] (score 1, diepte 0) Rebook and love them
[mfo3564] (score 1, diepte 1) I just got the wide ones to help with my Plantar Fasciitis. And I kinda of like the feeling of these new ones that I got since it didn’t hurt my feet as much as the ones,  I kept buying….
[mff1500] (score 1, diepte 0) The problem is it depends on the shape of your feet and the shape of the shoes.

Use the return policy.
[mff349n] (score 1, diepte 0) Order ½ or 1 size up. Always, regardless of what you pick.
[mff3en5] (score 1, diepte 0) Airwalk or Reebok
[mff7h8t] (score 1, diepte 0) God, I wish there was somewhere you could physically go to try on Amazon approved shoes. Hell, even someone to measure my foot would be fine. And yeah, I know I can go to a regular shoe store to get measured but the toe caps are what are killing my feet. The first pair I got really butchered my pinky toe nails. Perfect size, got wide width and still my pinky toe nails would hit the edge of the top cap until I lost one nail, and the other managed to hang on but it’s just purple. Thankfully they’re both growing out, slowly though. Got a second pair at a Walmart, 2 sizes bigger just in case and still butchered my nails. Got a pair of Volcom boots that have been my go to and got another pair from Amazon but I can only wear those for a day before my feet start hurting. The volcom aren’t too bad but I have to wrap my pinky toes in moleskin or else the boots rub my toes while ALSO putting a strip of mole foam padding that sticks to the inside of my shoe where the toe cap ends for extra protection. I think I need like a triple wide shoe. My foot is almost 4” in width across my toes and I wear I think it gets wider at the end of the work day. I’d really like the job if I didn’t have to deal with all the foot pain.
[mff7xaw] (score 1, diepte 0) I always get Keen, they only make work shoes. I get wide and a half a size up.
[mff90ia] (score 1, diepte 0) The answer is you get whatever shoes you want for everyone that's going to be different the only thing that really matters is the insult and you can't know that so you buy different insoles until you find one that you like.
[mff9bom] (score 1, diepte 0) There are my pick after 3 different brands , no callous no feet pain and they have lasted so far 6 months with them in perfect condition 
*
[mffoth1] (score 1, diepte 0) Skechers gave me the worst blisters. I’ve had Reeboks for 4 years now and they’re comfy. YMMV.
[mffv9nk] (score 1, diepte 0) They’re more expensive but the Brunt Marin boots are amazing! I’ve had two different pairs for two years and they’re still amazingly comfortable!
[mfgqsx5] (score 1, diepte 0) The airwalks are nice.
[mfhbw4h] (score 1, diepte 0) You may have to try a few. Get socks that are designed for the steel toes.
[mfja3gu] (score 1, diepte 0) Reebok were "ok"
[mfmilct] (score 1, diepte 0) I go with Columbia and stay the f away from timberland they are ass
[mfo2bj2] (score 1, diepte 0) I got Reebox just recently and they seem really comfortable and composite shoes. [These are](https://a.co/d/h6MSGdS) the ones that I got and they seem pretty comfortable…
[mfocoe7] (score 1, diepte 0) I've tried a lot and the most comfortable have been wide air walk shoes.
[mfrhbyw] (score 1, diepte 0) Puma ain’t hurt my feet but has to switch back to the Sketchers bc the other ones were too “heavy” and were physically loud and annoying when I walked 
Next ones will probably be the work boots I mean those can’t be that bad right?
[mg2h1yy] (score 1, diepte 0) I got brunt work boots paid less the. 20 out of pocket they come double insoles
[mfec6j9] (score -1, diepte 1) The one Reebok I had was fucking horrible. Wasn't on Zappos but still. If you have wide feet don't do Reebok

=== THREAD 1tpg6kb ===
SUBREDDIT: r/Construction
DATUM: 2026-05-27  SCORE: 10  REACTIES: 62
TITEL: My heels always hurt
POST (source_id=post):
I figured I’d come here and get real responses from real people instead of AI  
But I weld in a boat factory for 10 hours and my heels hurt so bad that I can’t even stand on them, I have to like roll my ankle and kinda stand like that if that makes sense. I’m a bigger guy, I have flat and wide feet. I’ve tried soles for the shoes but those don’t work.   
Everyone tells me to get good work boots and I did… I bought some brunt work boots and tbh my heels still hurt. It’s not my whole foot just my heels

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oo8n0we] (score 40, diepte 0) Assuming when you say “bigger guy” you mean a bit overweight, you need to lose weight in a steady, healthy way. 500 calorie deficit daily, 0.8-1 gram of protein per pound of body weight every day. 

It’s not easy but if better boots and inserts isn’t working, you don’t have a lot of other options. Getting your weight down to a healthy body fat percentage is guaranteed to put less stress on your joints on top of all the other health benefits. I don’t know how it translates to your heels, but losing 10 lbs of body fat equals 40-50 lbs less pressure on your knees when you walk.
[oo8lvzz] (score 18, diepte 0) Plantar fasciitis….my feet /heels were always killing me no matter what boots I wore…Finnally so a podiatrist and yup ,sure enough I have plantar fasciitis..!!
[oo8w202] (score 16, diepte 1) Don't be afraid of the GLP-1s, either. A huge help to anyone.
[oo8rd03] (score 12, diepte 1) I agree, same thing happened to me. Doctor told me
1. Get the boot you sleep in that stretches the tendon
2. Good shoe inserts
3. Don’t go barefoot or in flip flops, even open toed shoes need to offer support

Mine resolved pretty quick and hast been back
[oo9r347] (score 11, diepte 1) Just to as definitely have a digital foot scan done instead of just spending money on random insoles alsom
[oo8oxib] (score 11, diepte 0) Brunts are trash boots. But seriously, make an appointment with a podiatrist.
[oo9ce1t] (score 10, diepte 2) I had major plantar fascitis at 270lbs which went away at 240. Good boots also helped, OP might want to go the custom orthotics route.
[oo8p51q] (score 9, diepte 0) Sounds like plantar fasciitis, I recommend yoga and make sure you aren’t locking out your knees when standing
[oo8lz9k] (score 5, diepte 0) Try massaging the backs of you legs below the calf muscle. I have a massage gun and if I use it on those smaller muscles below the calf muscle it really helps with foot pain. Might help, hope it does!
[ooarmv8] (score 5, diepte 2) I've watched them completely change a couple friends' lives in the best way and seen how the pride of losing the weight led them to getting into fitness generally to the extent that when they come visit me in colorado they ask me to take them hiking which would have been inconceivable 5 years ago.

Our lives follow Newton's first law as well. If there's a tool out there that can help get the ball rolling, you can continue it on your own. I couldn't give half a fuck less about anyone that says negative shit about GLP1s, they have given people I love the boost they needed to live happier, healthier lives
[oo9kv5v] (score 5, diepte 1) I recently lost 30lbs (quit drinking) and have noticed my very sore knees are not bothering me as much. There’s other issues with my knees that I need to do PT for that will further help. All I need to do now is get new boots as they are worn thin and no longer have much cushion.
[oo8rqzz] (score 5, diepte 1) Agreed. Every time my feet start acting up it’s because I’ve fallen off on my stretching routine. Oddly enough, stretching my legs helps the most with my foot pain.

If I stop stretching for long enough, I can barely walk and hobble around like a 90 year old.
[oo8tlb8] (score 5, diepte 0) Other have given great advice but id add that posture can help a lot. Weight equally on the balls of your feet and your heels. Knees slightly bent. Knees over feet. Back straight and shoulders over knees/feet.
[ooa21kv] (score 4, diepte 2) Changed my fucking life.

Been struggling with weight since I was a kid. It's like someone just turned on easy mode.
[oo99sa2] (score 4, diepte 2) Eh there are tipping points. For me it was really hard to jog when I was over 300 lbs and chairs kept snapping on me, I’ve never broken a chair while under 300 lbs. I could see losing 50 lbs really making life easier for OP.
[oo8l9gu] (score 3, diepte 0) Have you tried any different lacing techniques like heel lock lacing? I don’t work in construction or do anything of the sort but it really helped me in all manner of boots/shoes.
[oobhel5] (score 3, diepte 3) Yeah this guy gets it. Just tie 30lb dumbells  to your bootstraps and pull yourself up after youre 10hr shift
[oo8pieh] (score 3, diepte 0) Used to take me 20 minutes to get my heel warmed up enough to walk normal. Went and got custom orthotics made and I’ve never had heel pain since. I will say the orthotics were like 600 bucks 7 years ago
[oo8v29q] (score 3, diepte 0) Lose weight, good insoles and if your standing in the same spots ask for anti fatigue mats they should buy them for you from u line they did when I was a cmc machinist and was getting the same shit from standing on concrete all day
[oo9x8om] (score 2, diepte 1) Might be that, could also be spurs.


I don't have spurs on the bottom that some people get, I have what's called "pump bumps", spurs on the backs of my heels. If I'm doing a lot of standing still, especially on ladders with my achilles strained, it gets bad.


It doesn't hit you in the moment, it hits you later on after you've sat down for the first time. Really hobbles you.


The fix is they open up the back of your heels abs grind them down. you're off your feet for nearly 2 months.
[ooaa7fl] (score 2, diepte 2) My heel spurs were cured with platelet rich plasma (PRP) injections, administered by my orthopedic specialist. Two injections and the pain is gone for more than 5 years now. Previously, I couldn't walk  She recommended the PRP to prevent surgery on my achilles, which sounded dreadful. Each shot was $500 cash, it's not covered by insurance for this condition.
[oo8m71c] (score 2, diepte 0) Do you rest on your heels. Like when you stand is all of your weight on your heels?  I have noticed that I do that sometimes so I try to be aware a d plant my feet where my weight is distributed throughout my foot.
[ooa8yo9] (score 2, diepte 1) True….im 6.3 and at 225 I could feel it on my knees and feet…I dropped 10 lbs makes a big difference
[oo8nu48] (score 2, diepte 0) You need orthopedic work shoes.

They are expensive, but they are really comfortable.

The only problem I had was that they were heavy,  but felt like walking on air, with some weights on my wings.
[oo8okh0] (score 2, diepte 0) So couple years ago I discovered custom orthotics. I was just being crippled by walking. 

What I didn’t realize is I was basically walking on the insides of my feet. They made orthotics to roll them out. 

My foot pain, occasional knee swelling and lower back pain basically dissapeared. 

The other thing they mentioned was that we all wear boots until they are falling apart. She recommended no more than a year with good boots and 6 months with cheaper ones. Thing is your walking wears the soles out to how you walk and then it builds on itself. It’s like tire wear and alignments. 

But some new boots, custom orthotics and some foot care fixed me right up. Had calluses from a those hot spots from my walking and worked on those. If it’s bad they had a nurse who did foot care to help sort out.  

Did have a coworker once with what I believe are called spurrs. It’s like a calcium deposit that builds on your heel. Believe they did some sort of laser thing on him to break it down. 

But I’d honestly start with an orthopedics place. They’d know where to start.
[oo9tqkb] (score 2, diepte 2) Yeah, my calves lock up and pull on the tendons in my foot
[oo901jc] (score 2, diepte 0) Bigger guy here. Construction beats you up. Did an enlistment in the Corps, got out and got back to drywall, when you’re young, you’re invincible, but it catches up. I’ve since lost some weight, got good inserts, invested in a second pair of boots that I rotate in, and became a super. Fuck all that haha You must take care of your body or it will be short lived like a neglected sports car. We clown on the hippies “my body my temple, but they’re on to something” catching rays and mediating, they are the ones who have it figured out really.
[oo99efr] (score 2, diepte 0) I got once a month with my adult daughter for a pedicure. The one we use is a couple little old Asian gals. They give zero fucks about us having a couple beers and kind of just yell at me in terrible English about how I need take better feet care lol. It's become a thing it feels good and I have come to enjoy it and it really helps. There's a tool called a foot rasp and it took several visits to get the gnarly cracks out of my heel calluses and that helped so much I ordered one of my own.
[oo9fo36] (score 2, diepte 0) You’re going to need inserts. A podiatrist can make you something custom that will actually correct the issue.
[oo9hgid] (score 2, diepte 0) Do the foot stretches for plantar fasciitis
[oo9zh8c] (score 2, diepte 0) Sounds like plantar fasciitis. Foot wear helps but you'll need ice and stretching to get rid of it.

In the mean time, anti-fatgue mat or wheeled stool to sit on if your work makes either of those practical.
[oo8lg8j] (score 1, diepte 0) Easy feet soles
[oo9gn3c] (score 1, diepte 2) This. I also recommend weight lifting at the gym — just have an upper/lower split, get AI to plan you a workout, and focus on ergonomics / posture muscles. It will take a year or two, and you will be sore a lot, but it will change your fuckin life.
[oo8nl26] (score 1, diepte 0) I have some extra wide Tony Lamas, square composite toe. They're pretty darn comfortable. 

My only complaint is they don't breathe that great and I have hot feet in general.  

Also recommend the PowerStep insoles for flat feet.
[oocxtz0] (score 1, diepte 1) Yeah brunt are walmart quality. Redwing, throgood, danner, georgia are brands to look at. Not sure what offers the best for heavier.
[oo91huv] (score 1, diepte 0) Get an exo-skeleton brace that takes pressure from the soles of your feet when squaring multiple times.
[oo91lav] (score 1, diepte 0) Inm seriosu about this, watch vanover customs and see what he has put on his boots to give him some relief to get more cushioing on the soles of his feet.

I got a larger boot size, got the best gel insoles and some good socks and that helped, tight boots caused a lot of problems
[oocxcd8] (score 1, diepte 1) I'm imagining Lloyd and Harry from Dumb and Dumber when they use an angle grinder on his toe nails 😂
[oo9bvml] (score 1, diepte 0) I had the same issue, and tried several things h til I found what worked. A physiotherapist had me doing simple calf raises on my bottom stair at home. Stand with you toes on the step, flat ground is ok too, and stand up on you tip toes and back down again. 10-15 times a couple times a day. It felt better in about 3 days and has stayed better for years now. I had the heel pain for a decade before that.
[oo9hw9m] (score 1, diepte 0) Get actual, custom, orthopedic insoles from a reputable medical professional, not Dr. Schols
[oo9psg0] (score 1, diepte 0) As a 2xx+# old man. Wedge heal like the redwing traction or Irish setter wingshooters and insoles have helped me a great deal on concrete floors. Another thing to add to the resting night splint already mentioned was rolling my foot on a tennis or lacrosse ball in the evenings. And no bare feet at the bar is also helpful with the figure.
[oo9qw73] (score 1, diepte 0) Goto a reputable boot store and have them do a digital foot scan. It can tell you exactly what your feet are doing. I never knew I had high arches and got some insoles to correct them when I got my newest boots. Feet feel great now.
[ooa8vvc] (score 1, diepte 0) Bursitis? Heel spur?

In either case, go see a podiatrist or orthopedic specialist. 

I had heel spurs and my orthopedic surgeon from another injury administered two treatments of Platelet Rich Plasma (PRP) into the spurs for a complete healing.  Each injection was about $500 and worth every penny
[ooacqey] (score 1, diepte 0) Have you tried a fatigue mat?
[ooafbxn] (score 1, diepte 0) Are your boots worn out? Even if they look good, they can lose their ability to absorb shock.

Are they tied properly? If they’re “flip flopping” even a little bit, you’ll notice it after a while.

Consider insoles. Whenever my boots are getting to the end of their life, I a use generic supermarket insoles that have a ridged arch and wide cup for the heel. They’re like $20 and the difference is night and day. Prescription insoles are apparently awesome too and they last years (so I’ve heard).
[ooafonc] (score 1, diepte 0) You need a fatigue mat in your workstation.
[ooag3we] (score 1, diepte 0) I have good insoles from a podiatrist, but she also pointed out that as a 55-year-old man, my feet have changed enough that they *require* strong shock absorption.  The extremely-squishy Timberland work shoes just...handle it...with no added fuss.  When I was younger, plantar fasciitis was a thing.  So, at least give thought to some of the ridiculously puffy shoes, which can come in hard toe.
[ooaiud5] (score 1, diepte 0) Or are you climbing a lot of steps
[ooaiv54] (score 1, diepte 0) Find a franchise like the good feet store or foot works. Whatever is local. They did me better than my string of podiatrists.
[ooajt70] (score 1, diepte 0) Check out Barefoot Science, their insoles saved me and now i wear reebok alloy toe shoes all day and dont have pain, i wear brooks when not at work
[ooajuup] (score 1, diepte 0) Plantar fasciitis sucks! After a couple shots and a few rounds of therapy it might get tolerable.
[ooak4dl] (score 1, diepte 0) I wear industrial doc martens steel toe with ankle support pull on boots.

I used to drill water wells, which meant being on my feet 12-16hrs a day, and working with water and mud around me.

My feet never hurt, or felt sore once.

They’re not crazy expensive either 

This is for reference:

https://a.co/d/05TUNzpH
[oobcblt] (score 1, diepte 0) Clean and dry your feet daily. Message them. The less you weigh the better for foot injuries. So eat less. See doctor as well. Maybe take shoes off at lunch. It can be shoes.
[oobhd0l] (score 1, diepte 0) Try heel cups.
[oobkjwl] (score 1, diepte 0) Brunts really are kinda terrible boots. They are basically Walmart workboots with more expensive marketing. I think you should get something with a little more heal on it so it will put your weight more onto the balls of your feet and take some off the ankle. Idk if that makes sense. An engineer boot would be good, especially for a welder. Unfortunately they are either cheap fashion biker boots or very expensive handmade boots. Most of the reguler working man boot brands (red wing, chippewa, etc) dont make engineer boots anymore
[oobtat9] (score 1, diepte 0) Try the good feet store
[ooc0yxp] (score 1, diepte 0) Dealt with foot pain in my arch for years. Finally went to the podiatrist and he diagnosed me with plantar fasciitis. Sent me to physical therapy.

At PT the guy wiggled me around a bit and says: you don’t have PF, you have super tight hamstrings. So he proceeds to stretch my hamstrings out to the point where I thought they were going to tare or something.

It’s now been 8 years without any pain whatsoever in my feet.
[ooc372j] (score 1, diepte 0) As a Personal Trainer...   Its really complicated.   

1) Fitness level, daily activity, past activity.
2) whats 'bigger' mean (BMI)
3) (fat percentage x height) x (tibia:femur:torso ratio).   Basically are you all leg and pudgy?  This will affect how you centre your balancw doing simple things like reaching for things.  That swaying on the heel.pad is very over looked.
4)  What does work look like.   Standing at a table all day or moving crouching shifting laying down.  Do you get pain outside of work.  If youre walking (with or without boots) does it get worse, same, better?


5) Most important.  Youre foot bones are the same as your hand bones and the heel.pad the same as your palm.   The calcaneus is made way more like a lever than a hammer.  so we arent like horses able to plod around.   We SHOULD 100% be walking around on the balls of our feet with our heels elevated and the muscles of our feet engaged in managing how our foot recieves the surface its placed on.   If safety mocassins were possible alot of dudes I know would have no back issues.   

Find insoles that elevate your heels and put your ball of foot and toes in a position they can meet the ground.  Even a 1/4 in is pretty impactful.

Weirdly the way people walk has massively changed in 200-300yrs.   Also wierdly Clogs are apparently super effective at resolving this.

Shims under the heel like a Oly lifting shoe. Custom insoles/ whittle them and glue some foam and roung rhe middle out with a flap pad. Tuck them under a Dr Scholes

Brunts are new, find a brand with legacy and who gives a shit how feet work (I love keens)Stsrt doing some ido portal mobilization.  Stay away from kelly starret. and improve your core stability and mobility.
[oocys77] (score 1, diepte 0) I’ve tried brunt. It’s not a good boot at all bro. Get a pair of red wings. thats the only boot that have gotten rid of the heel aches towards the end of work days for me.
[ooeei8l] (score 1, diepte 0) Get orthotics for plantar fasciitis, sounds like that's what you've got, it places more load on your arch than your heel.
[oorrj9b] (score 1, diepte 0) Go to orthofeet.Com. They make orthopedic work boots
[oowz1jk] (score 1, diepte 0) Gotta get to a foot doctor
[oo93kss] (score 0, diepte 1) they’d have to be a really big guy for weight to be the overarching factor
[ooav8l7] (score -1, diepte 2) No. They aren't. Build your willpower. Do it the hard way.

=== THREAD ihutrp ===
SUBREDDIT: r/army
DATUM: 2020-08-27  SCORE: 21  REACTIES: 62
TITEL: Does ruck marching suck really bad or is it just me?
POST (source_id=post):
I graduated basic training at Fort Benning almost a year ago and now I am thinking back to my experiences. Everything that I did during basic wasnt really that hard and the only thing I find insanely difficult was the ruck marches. It was literally hell for me. I remember wishing to die and hoping that I trip over a rock and pass out to the afterlife from dragging my feet on the ground. Did anyone felt this way? Some people were really sucking (mainly overweight people) but I was dying. I felt like if I was on my 4th hour of walking through a desert. Just want to know if you guy were feeling the same way or not. I did fairly well though on PT test scored about a 246 with max on run but I was struggling worse than the people failing the PT test.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[g32lxki] (score 92, diepte 0) I’d rather ruck than run. Might just be you boss.
[g32xddc] (score 68, diepte 2) You know what is neither ? My dental appointment at 0700 tomorrow
[g32lmtq] (score 59, diepte 0) It’s you.
[g32x7tv] (score 55, diepte 1) Running is just a short suck fest 

Rucking is a long borefest 

Pick your fighter
[g32mw2q] (score 36, diepte 0) A buddy of mine tried to break his own ankle to get out of one in the middle. When that failed he shit his pants and got a ride back.
[g32saxd] (score 34, diepte 0) I'd rather ruck than run any length of distance.
[g32rxgz] (score 29, diepte 0) I am better at rucking than I am running.

I have thicc syndrome so I'm basically built like a mule.
[g32xm02] (score 28, diepte 3) You need to make it 0800 so you have to skip PT but they need to expect you to be late to work call
[g32r6pl] (score 25, diepte 0) I'm a regular backpacker and I fucking hate rucks. I'm a pretty good rucker but it's the exact opposite of fun.

Make sure you're getting good hydration/nutrition the night before. Take LOTS of advil and do a bunch of squats
[g33urvt] (score 24, diepte 2) “We were a little slow that last mile guys, my Garmin has us at 14:20; let’s stretch it out on the flat and jog the downhills!”

“Wow, great idea sir; you’re literally the first person to ever come up with that strategy.”
[g32m8f7] (score 21, diepte 2) Neither of those indicate if you have short legs. If you also struggle with sit-ups, it's probably because of a long torso and short legs.
[g32na3y] (score 20, diepte 0) Just be an athlete
[g330wvb] (score 18, diepte 1) This got me laughing so damn hard, not even kidding. Just picturing a dude falling, getting called on bs, just dead eyeing a guy while he did it. Thank ya man
[g32lqu9] (score 14, diepte 1) /thread
[g32y6hb] (score 14, diepte 5) Once you get your slip, cancel the appointment
[g32r6ik] (score 14, diepte 0) A lot of that is having to ruck in formation versus doing it on your own. Me for instance, rucking always sucked ass the first mile or two cause my calves would cramp like crazy til I got that point where my blood flow would open up and bam I was good to go. I was prepping for SFAS before I went to drill school and a guy told me to try picking up a jog pace I can keep up for a long time to help beat the cramps, and it made a world of difference. I used to do 2 rucks a week, just throw a t shirt and some fucked up uniform pants on, put the headphones in and just go
[g32xprp] (score 13, diepte 4) Excellent work. Let me update my psg
[g33u68t] (score 13, diepte 1) Or that Lieutenant who wont shut the fuck up during a ruck.
[g33i1t4] (score 12, diepte 0) That one dude in your platoon that brings his Bluetooth speaker and blasts inappropriate trap music once you’re out of earshot of anyone with more than 2 rockers makes it much better.
[g33cy4m] (score 11, diepte 1) Seriously. Could never run for shit (I think I just hated running in formation because I'm 36 and run faster avg over 5 miles now than I did my 2-mile at 22), but I used to show up for formation shitfaced for ruck day every Thursday and I'd be cruising along like I was carrying a pillow on my back. But running I'd fall out of 75% of the runs we did. Even sober.
[g34t9o8] (score 10, diepte 2) Rucking: Nice, manageable walk. Enjoy the morning. Think to myself.

Running: Think about how much I want to die at this moment.
[g33iwiy] (score 10, diepte 1) > Me for instance, rucking always sucked ass the first mile or two cause my calves would cramp like crazy

This is the same for me. First 2 miles it'd always feel like the meat on my shins is gonna tear off. Then it just goes numb and I stare at the ground for the remaining 10 miles.
[g33oc88] (score 10, diepte 2) I am DOD Per-diem air compressor that collects free money pretending to be in the military.

That's what it means.
[g336kpn] (score 9, diepte 0) It's not just you. I despise rucking. If I run, my legs and my lungs hurt. If I lift, that specific muscle group feels the strain. If I ruck, I can feel every cell in my body beg for mercy. 

Some people can sustain a fast walk for 12 miles and finish in 2.5 hours, without even jogging. Fuck those people.
[g33hr6s] (score 8, diepte 6) *the mafia would like to know your location*
[g32v8mz] (score 8, diepte 0) Squats and Deads my guy
[g32pw7o] (score 7, diepte 0) It sucks. Different things suck for different people.
[g337ms8] (score 7, diepte 0) Fuck rucks. I am thick boy and prefer to run any day.
[g33uvs3] (score 7, diepte 2) Not making fun. Thats a bit short.

You"re stride will cover less. You need more steps to cover the distance.

Had a 5'7 commander that ran sub 12s.

On road march days in a row of people over 5'10 he struggled terribly.
[g33hy7l] (score 6, diepte 7) I was part of the mafia for so long that I got promoted to WO for my shamming instead
[g34ug88] (score 6, diepte 3) This is me when I pass the shoppette on Ardennes
[g32pszm] (score 6, diepte 0) Mind numbingly boring.
[g32mkj7] (score 5, diepte 3 OP) This might be it. I do struggle with situps.
[g33sv2f] (score 5, diepte 2) Try foam rolling or lacrosse ball to your calves before and after for a few reps and see if it helps, I’ll admit a solid stretch sesh before definitely makes a difference for me, since I’m doing so much up and down flex in rigid boots my calves and stuff tend to be pretty unforgiving.
[g33366i] (score 5, diepte 0) If you suck at it or aren’t in shape it makes it exponentially worse. So I would practice, start light and just get out there for a couple miles a week.

However even when I was in shape and hitting 2:15-2:30 time frame it was still almost solely out of pure anger at the fact that I was still walking. I hate rucking. So yes, I think it does just suck on a basic level.

Make sure you’re bringing something to eat too, maybe also a bottle of your liquid electrolytes of choice. If you’re pushing consistently for 2-3 hours it’ll drain you. Gotta replenish.
[g32lxbt] (score 4, diepte 1 OP) No im 5’8 150 lbs
[g34jj9v] (score 3, diepte 2) That’s short. Most rucking Chads I know are 5’11-6+
[g35pcb2] (score 3, diepte 1) Warrior*
[g32q4jc] (score 3, diepte 0) I don’t mind it.
[g34pubb] (score 3, diepte 1) Yep, the first 2 miles of a ruck always suck for me. After that I’m warmed up and it’s just autopilot.
[g33o85i] (score 3, diepte 1) Unrelated, but what does your flair mean? Are you a DOD civilian or something?
[g3317bv] (score 3, diepte 0) We had to do ruck runs. Fuck that shit!
[g33b5ev] (score 3, diepte 0) Here's my thing...

I can ruck at a decent pace if I'm in the front. But then last time we rucked as a group in formation i was told i was too fast. I went to the middle... the tall guys and i kept hitting feet while walking. Went to the back and i couldn't keep up for some reason. I'm short so let me fucking ruck and if you can't keep up with the short guy then tough shit...

No one tells you to slow down for the slow guys when running. Everyone suddenly on their own when it's a run.

But when we're rucking suddenly it's "slow down, you're messing up our pace" "third platoon can't catch up".

Tl;dr: idk just do your own thing. Fuck running.
[g350z4p] (score 2, diepte 6) >Once you get your slip, cancel the appointment

You out of your fucking mind?  Not only do you risk UCMJ for this potentially very costly endeavor, but you risk *not* be able to flirt with whatever potentially attractive woman is helping the dentist that morning
[g355z93] (score 2, diepte 4) I spent three weeks there. In my dreams, I can still hear an NCO yelling "THERE'S NO WALKING ON ARDENNES".
[g33ohk9] (score 2, diepte 3) Nice
[g33ooe2] (score 2, diepte 4) Yes, Readiness^(TM) is nice.
[g33e41x] (score 2, diepte 0) Rucking is so boring. At least when I run the scenery changes quickly.
[g33q2uv] (score 2, diepte 0) Are you short? I've noticed shorter people have a rough time.
[g347rbp] (score 2, diepte 0) You were more tired and hungry than your body was probably used to being, and doing something your body was not yet conditioned for.
Basic rucks weren’t too bad for me but I used to do long, high elevation hiking and stuff like that (walked about 20 miles with some snacks and a case of water in a backpack just weeks before basic). If you didn’t have that conditioning, it probably wasn’t fun. I still didn’t have fun on that last 15 mile ruck. We had full kit, full rucks, and hit the stairway at Benning on our way back from FTX. The last few miles there definitely sucked.

Personally rucking is a nice pleasant relaxing activity, even when I’m pushing for time. Wish I could replace running with rucking for all of eternity.
[g7ogh09] (score 1, diepte 3) Now I know why I'm cheeks at both lol
[g33id28] (score 1, diepte 8) And now you’re just giving away all the secrets....
[g33ztzf] (score 1, diepte 3) Yeah my last 12-miler I'll admit I kinda dogged it leading up to it. Granted, we were only given like 2-days notice of it, but that's still plenty of time for me to hydrate like fuck and stretch out for at least a day before the ruck.

I didn't prepare as well as I should have and I definitely felt the effects of it. Next time for sure, I'll be drinking water like a camel and rolling/stretching the living hell outta my calves!
[g34y9jy] (score 1, diepte 2) Y’all gotta go off road, it can be fun
[g33f5fr] (score 1, diepte 0) are you saying you rucked and didn't get fucked up and ambushed *THE ENTIRE TIME by holdovers??*
[g33tr35] (score 1, diepte 1 OP) No, im 5’8
[g34y1ia] (score 1, diepte 0) Idk man I ruck for fun (trails are more entertaining than the road in the dark). Your posterior chain is probably weak, you’ll get there mate. 

Deadlifts, front squats, running, and not being a bitch are key imo.
[g350hbn] (score 1, diepte 0) Lol rucking was my favorite part of basic. You got to shut out most of the BS and just take a nice long walk. I think I have pack mule genes, I’m no PT stud but I’ve always taken to walking/hiking long distances.
[g351si6] (score 1, diepte 0) Oh boy.  I’m one of those people who could barely pass pushups/sit-ups but could max their run and found the 12miles/3 hours target for the ruck wasn’t very difficult.   

We just aren’t all built the same way.
[g358znd] (score 1, diepte 0) Just suck it up and power through.   I usually run/jog for a minute, then walk for a minute and repeat until done.  Wear well padded socks and use foot powder.  I like compression shorts to avoid chafing. Stretch your legs well before, focus on calfs.    Drink a lot of water before and sip during, take ibproufen right before, and I like a small snack halfway if I can.  Usually something like a fun-size snickers or one of those honey waffles perks me right up through the rest.  I usually do my 12 mile in about 1:50.
[g37qdxj] (score 1, diepte 0) I've been out for 5 years and still ruck(hike with a moderately heavy pack). It was what I was physically best at in the Army...couldn't run fast for shit. I don't remember enjoying it in basic but the more I did it, the better I got at it, and the more I enjoyed it.
[g33tw2v] (score 0, diepte 0) Well I like rucking but I HATE rucking in formations. I ruck on my own with an Iotv with 2 sets of plates and a 15lb dumbbell. Don’t recommend being so heavy for pt because mfkers will pack light and you’ll hate life and probably get yelled at for not “closing that gap” or whatever some grumpy fuck says during a ruck.

