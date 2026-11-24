# Label-batch batch_0136

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
Schrijf het resultaat naar `batch_0136.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1kceppc, juq3bc, ku19rf, 1utaqvc).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1kceppc ===
SUBREDDIT: r/starbucks
DATUM: 2025-05-01  SCORE: 24  REACTIES: 64
TITEL: What shoes do you wear?
POST (source_id=post):
I’ve work vans, converse, air forces, on clouds, Uggs, literally every shoe I own to work and my feet, especially my heels, are always killing me. Do you guys have any good recommendations for shoes or insoles?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mq1zzgc] (score 27, diepte 0) doc martens, chelsea boots, they make them in nonslip and even a unisex version. they are leather, wipe off super easy, and are extremely comfortable once broken in, i put an insole in mine bc i have high arches.
[mq29tvd] (score 11, diepte 0) Crocs are technically approved if you get the kitchen ones 🤷‍♀️
[mq2i18z] (score 11, diepte 0) I wear shoes I found at Walmart on clearance 😂 but they’re a sketchers work shoe, unfortunately they’re starting to wear out 😭
[mq2ptbs] (score 10, diepte 1) Just a heads up -- nonslip shoes are NOT required by the dress code.  It's simply a recommendation.
[mq2ftbn] (score 10, diepte 0) I switched to crocs this year (called the bistro work clogs) and I’m so glad bc they not only feel like clouds but so easy to clean too so they’ll last forever
[mq202b8] (score 7, diepte 0) I wear sketchers from the at work line. I also have dr scholls insoles.
[mq21t19] (score 5, diepte 1) Same here! They saved my feet.
[mq3b7of] (score 5, diepte 0) I’ve been wearing blundstones boots since I started in 2019
[mq2brqc] (score 4, diepte 1) Doc martens all the way!!
[mq2uwr7] (score 4, diepte 0) Shoes For Crews slip-resistant and steel toe, it’s called the statesman or senator or something like that. Got used to it working in restaurants, I’m not jacking up any of my good shoes for this organization.
[mq4rg61] (score 4, diepte 0) Crocs 100%
[mq2n7bf] (score 3, diepte 2) They're the best. My regular docs took months to break in but my Chelsea's were just good out of the box.
[mq37xac] (score 3, diepte 3) Same here!! The Chelsea boots were my first ever pair of docs and I read horror stories about the break in period. I was shocked when they were comfortable right away
[mq20s5q] (score 3, diepte 0) depending on where you live if it rains a lot vessys are my saviours! they’re non slip and have awesome arch support!
[mq22oeb] (score 3, diepte 0) Our store makes us wear nonslip. I have stupid sketchers at the moment, probably gonna get the nonslip doc martens eventually.
[mq84dnv] (score 3, diepte 3) Starbucks corporate policy trumps whatever your dm and sm say.  They are not required.
[mq3bzzk] (score 3, diepte 0) I wear non slip clogs.
[mq3c7yq] (score 3, diepte 0) Air jordan 1s with those dr scholl’s inserts you get after stepping on that machine that tells you what number you are.
[mq3ejuw] (score 3, diepte 0) Hoka Clifton 9s changed my life. Signed, someone with chronic plantar fasciitis
[mq3fq8n] (score 3, diepte 0) I have Hokas. They have a whole work line of waterproof and slip resistant shoes meant for people working in the food industry. They are pretty expensive, about $175 BUT they are very comfy and I’ve noticed my feet hurt a lot less after shifts. When you walk it kinda feels like you’re walking on a little trampoline since they are so cushiony. I would highly recommend, they can’t get ruined.
[mq3vcd8] (score 3, diepte 0) I got the croc shoes from tik tok shop!! OMG what comfort!!!
[mq4dubb] (score 3, diepte 0) Crocs on the clock! The ones with the raised heel, splash-resistant, slip-resistant, and super comfy, were pretty uncomfortable to break in, but once broken in, they're fantastic.
[mq7m0ls] (score 2, diepte 1) Doc martens are comfortable once broken in, but the caveat it UNTIL they are broken in they can be high key torture if you already have foot pain.
[mq8ks5n] (score 2, diepte 4) Trust me, I know, but it won't stop them from bitching about it
[mqdhx65] (score 2, diepte 5) Yep and then finding other things to pick at. Constantly. :( I played that once (not at Starbucks ) and it was just too tiring. And honestly I don’t know very many people more stubborn than I am

TLDR: I feel you. It’s not worth it even if you are correct.
[mq22p48] (score 2, diepte 0) Try the Altra running brand. They have a black leather and it’s the most comfortable shoe I’ve worn to work!
[mq2ah1t] (score 2, diepte 0) A pair of Skechers boots. Steel toe because...? Idk. They're pretty comfortable and water resistant
[mq2dn0a] (score 2, diepte 0) Hoka
[mq2ek72] (score 2, diepte 0) Whitin high rise zero drop shoes in all black
[mq2kd1d] (score 2, diepte 0) I use cloud soles for shoe insoles. I've always bought shoes from shoes for crews but im trying out cariuma shoes because they're suede. The cloud soles are SAVING my feet either way!!! My feet don't hurt after an 8 hour shift
[mq2nsqn] (score 2, diepte 0) Oofos!
[mq2tcvg] (score 2, diepte 0) Sketchers, but look for their extra squishy line.
[mq2vv86] (score 2, diepte 0) I work at In N Out and my Docs are the most comfortable shoes I own. They were a total pain to break  in, I’m talking limping at work for a few months but now I can wear them standing and hustling around all day
[mq33jpu] (score 2, diepte 0) Reebok! Zero foot pain even during 8hr shifts!
[mq341pq] (score 2, diepte 0) i wear cloves. they are expensive, but worth it! [https://goclove.com/](https://goclove.com/)
[mq3bx6q] (score 2, diepte 1) when I first started customer service many moons before that, I used to almost cry with pain from being on my feet all day I couldn’t find a single pair of shoes that didn’t kill me - I almost gave up breaking them in but once they were good they were GOOD. I wore my first pair genuinely every single day from 2018-2024
[mvb81vj] (score 2, diepte 2) Before bc they were red but you can still wear jordans as long as they are the approved colors.
[mvc2g5h] (score 2, diepte 3) Thank you!
[mq3fkhy] (score 2, diepte 0) Keens
[mq3jc1h] (score 2, diepte 0) I used to wear non slip Skechers, but now I work at a store with slip-proof floors so I wear black leather platform converse.
[mq41h7v] (score 2, diepte 0) not dress code- but I LOVE my asics. I think they were 80 dollars max. The only shoes I’ve been comfortable wearing and I’m gonna be said giving them up when they enforce dress code :( they have a mesh top.
[mq4ll2q] (score 2, diepte 0) Danskos!!
[mq4wdje] (score 2, diepte 0) New Balance black nonslips!!! soooo comfy and unisex, I wore them to Disney and everyone in my group was in painnnnn in their shoes but my New Balances were amazing, great for standing/walking long periods of time 🫶
[mq54cq7] (score 2, diepte 0) i’m ngl… i wear the non-slip close-toed crocs. literally the best shoes ever for this job. i have worked a lot in food service and retail, always came home with my feet killin me. but ever since i got these crocs for work, it’s like heaven. i never have sore feet. i have no idea why it works, but it does. i cannot recommend them enough
[mq5fbiv] (score 2, diepte 0) Insoles from REI are the best! I forget the brand… or Timberland boots👌
[mq5pu7f] (score 2, diepte 0) Dr Scholl's
[mq5pvjs] (score 2, diepte 0) Vans with Dr Scholl's
[mq5qcvp] (score 2, diepte 0) Sketchers non-slip work shoes with Dr Scholl's in inserts! 💯
[mq6va6g] (score 2, diepte 0) I stand for 8-11 hours a day at my job at a grocery store and I love both Brooks and Hokas. Prefer Brooks but both are great!
[mq8w54a] (score 2, diepte 0) i literally just wear my plain white frat shoes from college they’re some kind of $30 reeboks i got on amazon but maybe i just don’t have sensitive feet LOL
[mq9wkyy] (score 1, diepte 2) I’ll ALWAYS recommend replacing the stock insole with a dr scholls or some other comfortable work friendly insole.
[mq7ek2l] (score 1, diepte 2) Yesh, but my DM and SM both want us to wear them. We still have the old floors with the mats.
[mq59u9i] (score 1, diepte 1) I got these and they told me it’s not dress code
[mq5gp09] (score 1, diepte 2) What? Why? I love mine!
[mq3b3rm] (score 1, diepte 1) I always buy the tread safe from Walmart. They been the only ones that I don’t slip in until I wear them out. Then I just get an insole after a while
[mv8qu9n] (score 1, diepte 1) Hi! Was this before dress code? Starting and I’m so unsure of what shoes to wear
[mq9vam6] (score 1, diepte 1) I have less back pain after switching to Hokas
[mq5gtbf] (score 1, diepte 1) Don’t leave them in the sun/heat!
[mq5aiej] (score 1, diepte 0) I wear crocs on the clock (the “full shoe” ones that look like Mickey Mouse shoes. But I put the insoles that I got from working in a warehouse inside them. Game changer. Protalus T100 Elite. They’re like $65
[mq9kw9v] (score 1, diepte 0) I wear Hoka bondi SR they are made for restaurant workers and nurses and are the mist comfortable shoes I've ever worn
[mq9vtfu] (score 1, diepte 0) Sounds like you’re on the edge of some plantar fasciitis. 

Shoes matters, but insoles and stretching matter more at this stage as you can improve an ok shoe. Chucks/vans/toms/dunks probably a no-go, especially at work, as they are very flat and encourage heel strikes when you walk instead of “heel-toe” walking. Look for something with a “rocker” that forces you to walk less on your heel. 

Are you flat footed? Do your arches fall? Are your calves and Achilles tendons tight? Look for shoes and insoles for those specific concerns. 

I’m a new balance or Dansko girly, but my flat-footed dad with plantar fasciitis swears by shoes from Orthofeet. My husband with arches and plantar fasciitis does Docs with insoles or oncloud cloudflyers— he hated all the other ones and he couldn’t get past how goofy Hokas look, though he thought they were comfy. I’d have a hard time spending $175+ on shoes to get ruined with milk and spills, but lots of partners do.
[mqadx3g] (score 1, diepte 0) Orthofeet and Superfeet green insoles.
[mqajwwh] (score 1, diepte 0) I always wore Dansko clogs. My feet never hurt.
[mqalska] (score 1, diepte 0) I wear the Walmart work shoes pretty much 99% of the time (35/hrs week). On occasion a pair of Doc Martins that were pretty expensive. Both of them are slip resistant and black but because of the new shoe material policy, I'm going to swtich over to the Docs . The Walmart brand ones have mesh, which isn't spill-safe. Unfortuntely my Docs make my feet hurt after about 5 hours and I'm afraid their slight heel will be a no-go.

I recommend getting a brand completely work safe and then adding some insoles if you need them. You shouldn't ever skimp out on work shoes.
[mqb96xd] (score 1, diepte 0) I went to the Skechers website and looked through the Work section for one that wasn't terrible. They were hell for a week but then were super comfortable
[mqd87b0] (score 1, diepte 0) They’re expensive and dorky looking but they’ll change your life- brooks glycerin max. I literally wear mine every day and it’s like walking on clouds.

=== THREAD juq3bc ===
SUBREDDIT: r/AmazonFC
DATUM: 2020-11-15  SCORE: 432  REACTIES: 64
TITEL: Six feet guys
POST (source_id=post):
[deleted]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gcf1v9x] (score 77, diepte 0) LMFAOOOO! What pisses me off the most though is the fact they get paid the same as me to just walk around the FC and be annoying.
[gcfswfh] (score 72, diepte 0) as a manager talks to me 10 inches from my face without a mask
[gcf3nbi] (score 48, diepte 1) And they tend to sit down if they’re monitoring the cafeteria, and if they’re not sitting then they’re making you uncomfortable by watching you eat. Fucking annoying with their goddamn clipboard
[gcf2j4c] (score 45, diepte 0) as they stand next to someone else too.
[gcfsxi7] (score 34, diepte 1) 10 inches is 25.4 cm
[gcf2sza] (score 30, diepte 0) yup as they pull their mask down to yell at you
[gcf8iu3] (score 23, diepte 1) lol one PIT driver hit em with the “6 feet guys” one day when they were walking by, they stared at each other than immediately looked at us down stacking and started saying “yea 6 feet”.. we just looked and laughed at them.. they were almost speechless someone hit them with their own annoyance
[gcfetjk] (score 22, diepte 0) One of the temp takers was sleeping in his chair last night.
[gcg03xe] (score 17, diepte 2) Thank you
[gcfy3b1] (score 17, diepte 0) In my place it’s the most useless, laziest, subhuman cretins who applied to be COVID marshalls. They’ve been affectionately renamed COVID cunts by almost everyone else.
[gcfdczw] (score 16, diepte 0) I Got put on "Social Distancing" and walk around quietly watching people work and wondering why I had to walk 32k steps that shift, my fc also likes rubber chickens and noodles for some reason.
[gcflf2k] (score 14, diepte 0) It's boring as fuck telling retards to pull their masks up and stay 2m apart all day NGL
[gch4jdy] (score 11, diepte 1) Sounds boring af honestly
[gcg5555] (score 8, diepte 2) I started calling them out a long time ago. Qlso was taking pictures of them when amazon was having thrm take photos of us. If I didn't start yelling back at them. I was going to loose it. I would like to keep the job for the benefits but jot sure how much longer I can take the mask and harassment.
[gcfxtcc] (score 8, diepte 1) It's almost like we're in a pandemic or something. You know?
[gcgue3j] (score 8, diepte 2) 10 > 6.. 25.4 > 6.. Big maths
[gcgh1q2] (score 8, diepte 0) The amount of hate this sub directs toward fellow employees for just doing their jobs is hilarious.
[gcgii6c] (score 6, diepte 3) It's probably because we've had record breaking cases in most states even ones that took the virus seriously. They aren't taking chances. A few weeks ago they were reducing the size of the sd team but now idk.
[gcfwl8s] (score 6, diepte 0) but have the mask up please. dont need grandma dead for amazon to make more money
[gcfy90y] (score 5, diepte 0) Lmaooo bruh I feel you so much
[gcgugk8] (score 5, diepte 0) And they are walking around in pairs, never 6 feet apart.
[gcguoz1] (score 4, diepte 2) How do you know they’re intellectually disabled? That sounds like cerebral palsy.
[gcgcxc2] (score 4, diepte 1) Lucky bastard.
[gche29k] (score 4, diepte 6) This.

It’s to cover themselves for the most part. If they didn’t have people constantly saying 6ft and whatnot and some got COVID, Amazon could be liable for not doing what they can.
[gcgsgu7] (score 4, diepte 1) Maybe he has people at home who are high risk? Some people have to take this seriously for their family members at home.
[gcgcue8] (score 4, diepte 0) Managers, assistants and the safety patrol are the main ones who break the 6 feet rule because no one will tell them not to.
[gceux04] (score 3, diepte 0) #Eyup.
[gchrln0] (score 3, diepte 2) Just wow. Ours give us an occasional reminder but they don't babysit us since they have other responsibilities to take care of too.
[gchdxbn] (score 3, diepte 1) I mean wouldn’t you do the same if you could? Get paid to just tell people 6 ft sounds like a sweet gig.
[gchkzs8] (score 3, diepte 2) No. If I have to be at a place for X amount of time I rather is go faster. Working is actually faster.
[gcgaalq] (score 3, diepte 2) Ha, I had 12 engineers with me at the FC looking at an issue and they were all within hugging distance, there was a safety guy walking in my direction when he noticed the vests he just walked away without saying anything.
[gcgvb3j] (score 3, diepte 5) It's not but you can't blame Amazon for covidiots. Their lawyers are trying to cover all bases.
[gchd4jx] (score 3, diepte 3) Not that easy when there’s so many unemployed rn and many businesses have gone bankrupt, shut down, cut back on employees, etc.
[gcfzatx] (score 2, diepte 2) For real, but I don’t see the need for so much policing. Maybe it’s my FC, or just the fact that I live in a state that rakes it fairly serious. Idk, I’ve just been keeping my space and avoiding the cafeteria and I feel safe.

But I see them escalating things. They’ve put time clocks in non high traffic areas, have put up partitions at the entrance.
[gcgutjm] (score 2, diepte 4) This would make sense if it was even possible to stay six feet from people, but it’s not.
[gcgcli1] (score 2, diepte 0) I got close to someone to ask for help with my scanner and the guy started yelling at me to keep my distance. Honestly it’s such an exaggeration having to keep our distance.
[gchfom9] (score 2, diepte 2) Well if they do theyre job shitty everyone suffers. So they have to make sure everything is being done so that goals are met at a certain time. Too many too few employees. Redirecting people, stopping errors early. Plus they're job is on the line in that they can manage the goal every night. So yeah they don't handle shit but good call there. Id say leadership isn't in you're future until you understand how shitty it is being in charge
[gcsct9l] (score 2, diepte 0) 🤣there not even safety atleast at my F.C there a whole social distance team they legit just walk around with a clip board all-day well one dude passes thru and chills in the small break room lazy fuck 💯🤷‍♂️
[gchsie6] (score 1, diepte 2) *Results may vary.
[gcis4su] (score 1, diepte 1) It’ll piss you off more that some are T3 roles and so they get paid more than you.
[gchxvh2] (score 1, diepte 4) Why? What would their body have to do with intelligence?
[gchg8bw] (score 1, diepte 2) Yeah but when I’m at my 10 x 10 cell, working.. I shouldn’t have to worry about my damn mask being over my nose when I’m hustling for rate. Soon as you do that there’s the covid cunts coming up (some yelling in foreign languages) telling me to put on my nose as I’m easily 10-20 feet away from the next human.
[gco8ruz] (score 1, diepte 2) Nope. I'm a 6FT SAVIOR
[gcht6s2] (score 1, diepte 1) space nazis
[gcguncx] (score 1, diepte 1) Part of the job is being able to assess a situation and make a call based on it versus what needs to be done.

Some of the hate comes from uppers not being able to make logically sound calls.  ┐( ˘_˘)┌
[gchy8x9] (score 1, diepte 3) It’s a choice to be in charge lol. Why would I feel bad for them for something they deliberately chose to do?
[gcguyzg] (score 1, diepte 1) The HR lady at my FC did that. I leaned in to talk to her and she gave me this face of absolute disgust. I hate HR.
[gchdvtm] (score 1, diepte 0) Has anyone actually had their badge scanned by these guys? Never seen it happen myself
[gchhxr5] (score 1, diepte 1) Definitely not! Lol
[gchl988] (score 1, diepte 0 OP) In 3 months I haven't had anyone tell me to step away from someone else or had anyone tell me to back off when I talk to them. It's loud as fuck where I am, though. If you don't yell directly into someone's ear you aren't gonna be heard, especially through a mask.
[gcib36z] (score 1, diepte 0) 🤣🤣
[gcihpmm] (score 1, diepte 0) LMAO!! ligit had to deal with the samething 2 days ago 😭😭😭💀💀💀
[gcjec8t] (score 1, diepte 0) They be saying that shit with their WHOLE chest lol
[gcl3uu6] (score 1, diepte 0) What pisses me off is that I try to keep distance. Other people who get close to me and I'm the one that gets asked to move. Hell no I was here first
[gcpzwgu] (score 1, diepte 0) Nope I only have two
[gnq3szb] (score 1, diepte 0) They usually walk in pairs holding hands 🙄
[gcgc07z] (score 0, diepte 1) 🤣
[gchy41c] (score 0, diepte 4) My point was it doesn’t make a whole lot of a difference what people do. The risk of getting covid in an FC is still too high.
[gcgrf0s] (score 0, diepte 0) I work in a delivery station and my shift assistant is hella annoying. Tried to hand her my badge to scan for vto and she would step away like i have some kind of disease. Maybe i should just boomerang it right in her face. I would avoid any kind of interaction with her and stay as far away from her as possible. Stupid retard. And she had ambassadors audit us why our pick rate is slow. Well bitch u told us to made sure 1 person per aisle, stay 6 feet away and had to wait for all delivery vans to come in b4 we can cross and stage the cart. Not to mention theres always cart shortage that we have to wait for drivers to empty the carts b4 we can continue to pick. Thats why it takes us awhile to finish picking a route, bitch.
[gcg6v9i] (score -1, diepte 0 OP) One time my manager manager asked if I wanted to do that and I said no
[gcgv12w] (score -3, diepte 2) If there is that much of a risk for them, they should probably get a different job.
[gchdyjr] (score -4, diepte 1) Did you fart his in mouth when he was sleeping?
[gcfvz7e] (score -4, diepte 0) I get a bullhorn and walk around the shop with it 6 FEET
[gcgurc4] (score -7, diepte 1) I don’t see them as fellow employees. They don’t have a real job.

=== THREAD ku19rf ===
SUBREDDIT: r/FASCAmazon
DATUM: 2021-01-09  SCORE: 76  REACTIES: 64
TITEL: 1st time doing any job other than stow. Tote runner. Got moved an hour into my shift. It was awful. Feet and legs are gone.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[giq50r4] (score 16, diepte 0) Tote running is a lifestyle not for me. Pick Dept.

Did it one day (untrained, thrown into the deep end) and just tried to keep everyone's ARSAWs  stocked as best I could. Then they moved a bunch of counters to Universals and I had to stock them too. Managers on my ass because they're like "you have to stock these now too". Oh okay thanks for letting me know it's only MY FIRST FUCKING DAY DOING THIS STUPID BULLSHIT WITH ZERO TRAINING. Ahem.

My feet were dead at the end of the day and I ran a large flatbed into my ankle bone near the end of the day because I was so done by that point and distracted.

TL;DR - This job is for jocks. I'm not a jock.
[giq9ry9] (score 10, diepte 0) I asked to Waterspider just to try it out the week before last week. Time moved by a hell of a lot quicker, but I only managed like an hour of it before I tapped out. Taking care of 20 stowers, with carts that only have five stacks of totes (so 25 boxes) each, was a nightmare. Dude training me gave himself like 10 stations, tops, while I was supplying an entire side of people basically. Would not recommend haha, I could not catch my breath!
[gipk556] (score 9, diepte 0) I stow at a DS. We also megacycle. Today I did 18.65 miles, yesterday was 23.29 miles and Thursday was 25.93 miles. 

While on my drive home, my muscles start tightening up in my legs.
[giq9yuz] (score 9, diepte 1) THE ZERO TRAINING PART, MOOD. My experience wasn't as bad, but getting thrown into the deep end and barely having a clue of what is happening is absolutely terrible 😭
[giqih5q] (score 8, diepte 0) 33K - 13 Miles
[gipespd] (score 7, diepte 0) I would take the job, it helps to lose some weight. Make sure you have a good set of comfortable shoes.
[giqdr69] (score 7, diepte 2) I would not advise you to put a camel on your back.  Those things are huge and besides, you can't bring pets into an Amazon warehouse I know that because I asked an HR person.
[giqiufn] (score 7, diepte 1) 20 Stowers???? That should be illegal. I refuse to try after 9. The Stations are too far from the downstacker for me to do that all myself.
[giq19tm] (score 6, diepte 0) Got moved from stow to ship dock to help out...loved it, and would recommend it over pick or pack
[giq3r2h] (score 5, diepte 1) I’ve lost over thirty pounds in two months. 

I’m a WHS specialist. 

What the floor employees have to do is above and beyond IMO, my last safety job was heavy construction and it wasn’t half as demanding on the workers as this is.
[gipoycz] (score 5, diepte 0) I consistently have hit 60,000 doing totes. I don't do it as much because there is no satisfaction from it. Snake chasing tail for 10 hours. Hell no.
[giq0pjp] (score 5, diepte 0) You'll get used to it. When I waterspider, I get 35k steps, haha
[gipslmk] (score 4, diepte 1) Yeah I do about 30 a day. Its more my hands or my hip that locks up though. Wish they didn't have masks and I'm seriously considering a camelback to stop the dehydration cus I always forget what aisle my waters on
[gipl274] (score 4, diepte 0) Lol me today, I usually stow but this whole week they made me work on the docks and today they had me water spider, steps way higher than usual. Legs are dead, got home and just slumped down. Haven’t walked this much since I went to New York a couple of years ago 😂
[gipwfik] (score 4, diepte 0) Try water spidering wraps and having to organize the sloppy stowers who rummage through all the totes and leave their workplace a mess
[gipkczc] (score 3, diepte 1 OP) But, so does stowing! Definitely need better shoes in general.
[gitp0rj] (score 3, diepte 3) Quarantine weight is a helluva thing. Glad to see it gone.
[gipplxd] (score 3, diepte 1) Same makes the day go by fast plus you get labor tracked
[gips4c6] (score 3, diepte 3) Labor tracking is used when you don’t have a trackable rate (like with a scanner)
[giqelsa] (score 3, diepte 5) Is that a legit option I can have lol. I'll take it. Till my wheels break and I'm fucked for the day.
[giqg7zd] (score 3, diepte 1) I hated spidering the wraps. My feet were dead by the end of the shift. One day I just said fuck it and moved at a comfortable pace, not giving a fuck if some people didn't have work. Now I'm permanent downstacker 😅
[girgt64] (score 3, diepte 2) I hated it - they would set me up with the carts of boxes, so when I finished a cart there would be another there and waiting. I couldn't sit and take a break at all it felt like, I was new to Waterspidering (haven't touched it since) so I was exhausted, walking back and forth across the side of the building. Still kind of mad at the person training me for that one lol
There are always quicker and slower stowers too, so I never could really get to the end with a cart because, by the time I did, I would have used all 5 stacks because someone had been running out.
[gipsjk0] (score 2, diepte 2) I wear these, originally got them for working doubles in restaurants, my feet don’t hurt super often and when they do it’s usually on the last day of the workweek. Downside is they don’t have a carbon toe so if you drop something on your foot it’s gonna hurt. 
https://smile.amazon.com/gp/aw/d/B012PW0R26?psc=1&ref=ppx_pop_mob_b_asin_title
[gipiqme] (score 2, diepte 0) Tote running is my favorite job!
[gipq1ug] (score 2, diepte 2) What’s labor tracked
[gipuojk] (score 2, diepte 2) I thought about using a camelback as well. I usually leave my water on floor at the end of the isle. That way I'm passing by it often.
[giqgme5] (score 2, diepte 2) I always cover the wraps and end up having to help the front catch up. My feet have some major calluses though
[giqkhsi] (score 2, diepte 1) I'm a picker/waterspider and I surprisingly prefer being a water spider. After my body adjusted to the physical activity, time flies. On the days that I pick on an order picker with cooling fans and less overall physical movement, time CRAWLS. I LOATHE Interacting with coworkers as a waterspider but the constant workout makes it tolerable. It's the main reason I haven't bothered to apply for positions like learning ambassadors and PA's. I need to MOVE lol.

Edit: spelling lol
[git2zrl] (score 2, diepte 1 OP) I have dr. Scholls insoles! They help lots!
[gityphx] (score 2, diepte 0) Screw amazon
[giue4nt] (score 2, diepte 0) It's all preference, stowing was always terrible for me. Constantly rotating from the pod to the screen and containers and not always using the ladder made my back constantly hurt. Being any type of runner like running for stow, tote running for pick, or waterspiding on the dock was always better to me. Your arms are on fire at first if you don't workout, but it goes away and you start building some toned arms and legs while getting trimmed overall from walking so much. Just need a good pair of shoes.
[girlkv5] (score 1, diepte 3) Get some Skechers memory foams and some insoles...walking on clouds
[gitsi5d] (score 1, diepte 4) I have some skechers picked out that I want, but they're not in the options group they let us choose our free shows from. The only ones they have avail, are heavy from what I see. What insoles are you using?
[giugwwr] (score 1, diepte 5) They have some available. I use dr scholles and some that my podiatrist gave me
[gitoxd1] (score 1, diepte 2) 30? Damn that’s a lot
[giu15b7] (score 1, diepte 4) Same here. Gained 30 during quarantine I’ve been with amazon for a month and I’m down 5 lbs
[giu162q] (score 1, diepte 5) 5 lbs is 2.27 kg
[giu1uqi] (score 1, diepte 5) The activity was one part of it, when I started working at amazon I started eating less since they had me starting at 4am. For whatever reason I’ve never been able to eat in the morning so that schedule jacked me up.
[i95hfbz] (score 1, diepte 1) The only upside to the job is if you’re fat or illegal. Otherwise. Look for better opportunities
[gipk3ma] (score 1, diepte 1 OP) Why??? I’m exhausted!
[gits49a] (score 1, diepte 1) Do you know if "Tote Running" is categorized under "Outbound-Sort-Batch" at Fulfillment Centers?
[gitzvl9] (score 1, diepte 2) I'm an outbound picker but I've been labor shared to run totes in multiple inbound and outbound departments. From what I know I don't think that tote running is something you can actually be hired for. They just pick a random person from the department to do it each day or they borrow people from other departments if they have people in stand up. 

I not 100% sure what sort-batch would be doing so don't know if they would even need tote runners
[gipwmbw] (score 1, diepte 3) All this walking is brutal on your sciatic nerve. I consistently get 20 to 35 miles a day depends on the job. If I'm doing autoslam it's 20 miles, tote team is 35 miles, water spider is 25 to 30 miles. The only time I can think I might hit 15 miles is I'm in Pack doing multis.
[gipwn9t] (score 1, diepte 4) 35 miles is 56.33 km
[giqdush] (score 1, diepte 4) Have you considered wearing roller skates?  They may help you out.
[gitruca] (score 1, diepte 6) Lmao....if only it were an option!
[gito58d] (score 1, diepte 5) If I saw an associate on roller skates I'd lose my shit! 

XD
[gisufmf] (score 1, diepte 1) Amen. I am a stower and I don't like clutter or mess.
[gqa2e1g] (score 1, diepte 2) Litteraly the best part is moving at an amazon job with a out rate, cuz being a robot and just standing in 1 place makes time go by hella slow
[gisre2b] (score 1, diepte 1) I noticed on the first line it says Pick Dept. at the end. Are you saying you're currently a picker and they moved you to tote running for a day, or that you did tote running for the pick dept that one day? 

Asking because I am currently a picker at an FC, and have been thinking about trying to xfer to Outbound/Sort/Batch which I believe is where tote running is categorized. I may be wrong though? I've tried asking but naturally I can't get straight answers. 

My reason for want to switch is because it feels like the time drags by sooooo slow at this FC when I'm picking, even when I'm only doing 5hr shifts (I'm flex, so I can do 5hr shift blocks, sometimes I go ahead and select to do 2 in a row to knock out 10hrs). I don't mind picking, I like staying busy and constantly moving. 

I don't know a single sole at the FC I am at now, so I really never talk to anyone, stay at a consistent pace, but I'm still not able to pick at the 90+ piece rate they expect! I could, if they didn't have everyone terrified to go in isles when someone else is in it and threaten to write you up if you get caught passing in isles. When it's not that, it's rude stowers that never offer to let you by to get your pick, so you have to go multiple isles down and around to try getting there, or getting sent 100+ isles between every 3rd pick. It just grinds my nerves to be made to feel like I'm failing when it's beyond my control.
[gitfkm1] (score 1, diepte 2) I mean I'm a picker and they had me tote running for the pick department one day. I work at an AR facility so don't have to do any walking in Pick. I couldn't imagine having to deal with other people's crap that much just to get my job done. As long as a tote runner is filling my ARSAW and the floor health is good, it's smooth sailing all day. I got put at the end of the line though today... kinda even more depressing that far down.
[gitrh0a] (score 1, diepte 3) Ahh..ok. Thanks! Yeah at our FCs here, pickers run all over the place.
[giugd56] (score 1, diepte 2) Tote running usually comes from pick department, but they can labor share anyone for it. Usually someone who uses a pallet jack in another department or a picker that gets trained in tote running. Try to transfer to ship dock since a lot of the jobs there are indirect roles that will have you just moving pallets, karts, and etc all shift with no rates. Either that or try getting into stow and becoming a runner since you'll have a better chance. Usually a lot more runners in stow vs tote runners in pick.
[giuena2] (score 1, diepte 1) It's definitely not, I've seen a 4'10 petite Asian girl be one of the best waterspiders on a shift. She pretty much can't move the really heavy pallet that are filled with heavy stuff, but can easily tote run and run your average pallets and keep every station filled with work. A lot of it just comes down to stamina to consistently work and being smart about it. Most of the top people in every role just do the job smarter, not harder.
[girla0y] (score 1, diepte 3) Don’t be so mad at him...they usually give the POC lower number of stowers or down stacking because they have to do wip counts every hour and have to fill in for people if they get pulled to the side
[girr5m6] (score 1, diepte 4) I'm not really that mad honestly. It's been a couple weeks, I've moved on from that. Just hold a grudge for being a waterspider now though I think! Stowing sucks, but at least I'm not trying to appease a bunch of stations. Not sure if he was the POC even though. He's been here as long as I have, which is not very long (this weekend marks week eight)
[gisoqke] (score 1, diepte 5) Usually has the radio in hand to report the wip count to the higher ups
[gisuew1] (score 1, diepte 6) Didn't see a radio on him but it's possible
[giueako] (score 1, diepte 1) Are you sure you guys weren't just understaffed with indirects? Also, were they exclusively waterspiding? If you had 20 and they had 10 you might have exclusively been just opening packages while they were also doing running.
[giqqdgw] (score 1, diepte 0) From receiving(decant) and tote running is a lot more fast pace for us but it’s not too bad
[girk04a] (score 1, diepte 0) At least you're not reverse logistics, AKA cret....
[git14y2] (score 1, diepte 0) Hey if you’re feet are hurting that bad I highly recommend buying soles to put in ur shoes. After a couple of days it’ll help your feet be used to walking about 12 or more miles at work. I’m a speed walker when it comes to picking all day and I’m never in feet pain ever since my wife got me a pair of soles!
[i95h71u] (score 1, diepte 0) I just don’t know who could do this job without being inspired for wanting more for themselves. The pay is decimal at best and you’ll have no personal time because you’re left bitching about how many steps you took that day.
[giqwb5s] (score 0, diepte 1) We have a tote runner who is elderly but does at least 45k steps a day. He's one of the fastest tote runners I've seen. So I wouldn't say its just for the jocks but it is a lifestyle.
[giqdd82] (score -14, diepte 0) I have never run totes but I did run some hoes in south Chicago for a few years.  Yo, those bitches be runnin' wild!

=== THREAD 1utaqvc ===
SUBREDDIT: r/Construction
DATUM: 2026-07-11  SCORE: 11  REACTIES: 64
TITEL: Comfiest Steel Toe Work Boots?
POST (source_id=post):
I've just started my apprenticeship 8 months ago coming from a labouring position. I've had New Balance work boots for a couple years now and I need a new pair. Don't wanna go NB again though. Just need some recommendations on steel toe boots that are comfy for long hours or even some insoles. Price is not an issue

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[owu9enf] (score 30, diepte 0) This may be unpopular opinion but I use the brand KEEN they make hiking shoes but also have a steel toe version. Very comfortable doesn’t even feel like you have boots on and I’m a size 15 wide I love them . The price is super reasonable too
[owu9jzm] (score 15, diepte 0) Thorogood
[owux34w] (score 7, diepte 1) KEEN's a solid choice for comfort, especially for wide feet. Just keep an eye on the durability if you're in a rough environment daily. They're comfy but might wear faster than some heavier-duty brands. How's the tread holding up for you?
[owvir8e] (score 5, diepte 0) Royers and blunstones
[owu9vzs] (score 4, diepte 0) Ive always had Blundstones, just like how they look at feel
[owuc6v3] (score 4, diepte 0) I've had really good luck with **Thorogood** boots. They are not cheap, but once they are broken in they are probably the most comfortable work boots I've owned for 10-12 hour days. If you are on concrete a lot, I'd also grab a pair of Super feet or Power step insoles they make a bigger difference than people think. Everyone's feet are different though, so if you can, try a few brands on before buying.
[owufbgt] (score 4, diepte 0) Thorogood. It was described to me as a boot you don’t rush/ can’t wait to get off. You could rock them as an everyday wear. Most comfortable boot I’ve ever worn and have continued to get them when worn out
[owvti9x] (score 3, diepte 1) Plantar fasciitis almost completely alleviated after switching to Keen. Love them.
[oww6l4a] (score 3, diepte 1) 100 upvotes for this.
[oww2zui] (score 3, diepte 1) They make steel toe??
[owwn825] (score 3, diepte 2) Not sure if theyre steel or composite but they've got the CSA stamp required for safety where I'm at. Been wearing them for about 5 years now, just started wearing my third pair 2 weeks ago
[owua3mp] (score 3, diepte 0) Most comfortable boots for me are redwings king toe with their moldable insert. They dont last long enough and they’re overpriced so I usually wouldn’t recommend.
[owuaokg] (score 3, diepte 0) Keen boots are comfortable. I dropped a 6x6 block on my toe today. I had no steel toe. Hurts. I was anti steel toe, now my toe hurts
[owuh22i] (score 3, diepte 0) I've had great luck with Timberland Boondocks. I throw the Dr. Scholls 440 insert in and I'm golden until they start to fall apart, which takes like two years for me. I'm not gentle with my boots.
[owvogll] (score 3, diepte 0) Do you need a wedge sole or defined heel? Either way, I wear and recommend Danner. Bull Run for wedge and Quarry for a heel
[owvpq0e] (score 3, diepte 1) We're in the minority, but I've been wearing Danner Bull Run wedges for almost 15 years. Great boot.
[owwdo8k] (score 2, diepte 2) What model of boot do you have? Even with custom orthotics my fasciitis is acting up.
[owxn85s] (score 2, diepte 3) See other comment.
[owxn6qu] (score 2, diepte 3) Synchro Waterproof Work Boot w/Carbon Toe  
Utility K-30 arch insole

These worked great for me, of course everyone’s feet are a bit different. But I went from walking on knives with red wings to rarely feeling anything. Also feel like my toes have more room.
[ox0x1e6] (score 2, diepte 1) I’ve worked thru thoros in 5 months. The best boot in the market is Irish setters. Put the arched in soles in them, and take them in to get fixed up for free every 6 months. Theres literally nothing better. It’s the best boot. Idk what to say
[ox0b8ja] (score 2, diepte 4) Each pair Ive had, before wearing them to the jobsites I wear them casually everyday to break them in and theyre not AS comfy as the non steel toed, theyre comfy enough to me for casual wearing before. Also have done jobs with pretty large footprints to the point of having 18-20k steps in a day in the blunds and  theyve been great to my feet
[owuca0z] (score 2, diepte 0) Keen ironworker boots; Ive tried a ton of the years but they’re the first boot I’ve bought 3 times in a row and don’t plan on changing
[owul81d] (score 2, diepte 0) Another vote for thorogood. I wore red wing and Irish setter for decades. They stopped making the model i liked and switched. My first pair lasted 3 years. I'm 2 years into my second. And am shopping for my 3rd before I kill these. They don't last forever. But as far as traditional leather boots and short of buying a pair of Whites. Thorogood is what I recommend
[owuutsm] (score 2, diepte 0) I like my Irish setters. They come in wide for my feet and that helps tremendously on break in. Since you know… wide feet.
[owv9u60] (score 2, diepte 0) Id go for composite toe, theyre lighter and dont freeze your toes in the winter
[owvyk74] (score 2, diepte 2) What’s the trick? Only buy the top tier American Danner? I had a pair of danner with the glued in sole and they didn’t last for very long. Also have a pair of danner hikers I was pretty disappointed by but got them at a pretty steep discount on clearance so no return. I wear them for general lawn mowing and doing anything light in the woods but they feel cheap.
[owvqqzt] (score 2, diepte 0) carolina sarge 8in steel toe. union made too
[owvu9g2] (score 2, diepte 0) Keen also, mid height at least.  They have waterproof ones too.  Last pretty well.  I treated the leather with “mink oil” paste when I get them new, helps keep the leather lasting longer.
[owvwdve] (score 2, diepte 0) Danner’s
[ox5xgos] (score 2, diepte 1) A lot of guys I worked with wore danners , they loved them
[owvzjf8] (score 2, diepte 0) Thorogood
[owxlbg1] (score 2, diepte 1) For real. Ive got a pair of Ariat ground breakers ive had for two years doing industrial demolition and they're just now starting to get wore out. Steel toe with met gaurd. I'm getting the Ariat workhog next
[owvf3lo] (score 1, diepte 2) Eh my keens are holding up as well as my carharts or timberland pros did
[owvsild] (score 1, diepte 3) I was surprised how well they held up to my timberland pros compared to half the price.
[owvr5et] (score 1, diepte 1) KEENs are comfy but watch out if you're in wet or rough environments; they can wear out quicker than others. For wide feet, though, they definitely hit the mark. Consider adding gel insoles for extra cushioning if you're on concrete all day.
[ox0wjf3] (score 1, diepte 3) Go get Irish setters, have them fit your foot for arches. Don’t fall for this marketing shit.
[owxisow] (score 1, diepte 2) I’m also interested in which boot you have to keep your plantar fasciitis at bay.   
I always end up jumping up a half size to accommodate some kind of orthotic. What do you guys recommend?
[oww153x] (score 1, diepte 1) Keen is good, but I found the inside of the boot where the heel is wore out way faster than it has any right to.
[owwgr2s] (score 1, diepte 1) I have some of their hiking shoes now. Very comfortable. Great for wide feet. Exceptional traction if you’re on hills. The only complaint I have is that they claim to be waterproof. They’re in no way waterproof.
[ox4doxc] (score 1, diepte 1) I just switched to Keens a few months ago. Absolutely love my San Jose’s for walking on concrete all day in the summer. They’re light and comfy
[ox34jox] (score 1, diepte 2) I have both. My current boots are Irish setters from a boot mobile that comes to my work every year. This current pair is two years old and going strong. The only reason they are my current boots is that when the truck showed up my first year there they didn’t have thorogoods. I have two pairs of those, one that’s four years old and still fits just right and one that’s brand new.
[ox05s9g] (score 1, diepte 3) I think they make both a steel and a composite version! Been eyeing them for myself! I have the regular ones for gardening at home and I was wondering if the safety ones were just as comfy
[ox6ylqb] (score 1, diepte 1) I've been interested in trying these for a while. I like to have two pairs, one comfortable pair and one heavier duty pair and have heard Blundstones are very comfortable. Problem is that not having protection over the toe leather is a 100% dealbreaker for me and they don't seem to offer that.
[ox77e3a] (score 1, diepte 2) You mean just like a toe cap? Theyve got boots with toe caps to protect the toe from being on your knees a lot
[ox7y8y2] (score 1, diepte 3) Hmm. Couldn't find them last I checked. Maybe they aren't on the composite toe ones.
[ox0xm13] (score 1, diepte 1) If you do redwing. You go Irish setters. 6 inch steel toe with the arched insoles and spray some tuff toe on em. simply the best boot on the market. I’ve ran a few into the ground. They last 3 years. This question pisses me off.
[ox49y4c] (score 1, diepte 2) My Irish setters fell apart in 6 months,  the the lace hooks ripped off.  The toes blew out in 2 months.  They were comfy and light but man they sucked
[owufcnw] (score 1, diepte 0) I Got my first pair of Redwings almost forty years ago. I was never able to find any other boots that were as well made and comfortable. I bought my first pair of Keen Detroit boots about 3 years ago. These are the most comfortable boots I have ever owned. They look like a hiking boot but have a steel toe. I'm walking on concrete, climbing ladders, and on roofs. I don't think you'll be disappointed in them.
[owuwvie] (score 1, diepte 0) Sketchers
[owv4cq4] (score 1, diepte 0) I’d suggest going composite toe firstly. Then if suggest shopping around and trying on different boots. Boot barn. Redwing store. There are so many brands. Hell even Walmart has one good boot and the rest are garbage. But if you’re at a complete loss. Redwing will measure you foot length, width, and arch and suggest everything down to the insole. They’ve paid thousands for that machine. It’s free to you to use
[owv8mp8] (score 1, diepte 0) Redback boots
[owvdbpu] (score 1, diepte 0) Double H
[owvf5ic] (score 1, diepte 0) Im a big Mr Miles fan. Since they arent a well known brand you dont pay a name premium
[owvkv6r] (score 1, diepte 0) Puma makes work boots and theyre very confortable when doing lots of walking.
[owvo3eq] (score 1, diepte 0) Keen are good. 

I got Skechers composite toe & they’re the best I’ve gotten for comfort, fit & durability
[ox66sku] (score 1, diepte 2) I rock a pair of synth toe Chelsea’s, and they broke in really good. Big fan.
[oww2v4y] (score 1, diepte 0) Bekina steplight rubber boots. 

I've tried many steel toe boots now and by far these are the comfiest if tried. 

Little to no break in time required!

I wear them as my everyday now for like 2-3 years and everything else just seems unfortunate in comparison. 

Pipelayer, 4 years
[owwe2bv] (score 1, diepte 0) Hit up a western store, find a pair of slip ons you like. Unless you’re doing backflips & shit on the job, slip ons are always the move
[owwlrmg] (score 1, diepte 0) It’s not necessarily about the brand, it’s about price points. Good brands will make very nice expensive shoes, and also budget friendly ones that aren’t as good. You may also find some mass produced shoe that works great as well.

I bought a new pair every year for years. Then once I spent more ($450 on Redwings). I’ve had the same pair for 8 years now. They are by far the most comfortable shoe I’ve ever worn. I even wear my work boots hiking.

The best advice I have is to make sure you can re-sole the shoe. This is typically a sign that it’s made to last.
[owwwdgj] (score 1, diepte 0) I haven’t had a pair myself, but everyone I talk to with Redbacks say it’s by far the comfiest work boot they’ve had. 

Basically Blundstones that are still made in Australia instead of Asia. Close to the same price and the quality seems way better from what I’ve heard. Getting some next pay cheque
[owxlidu] (score 1, diepte 0) Ariat groundbreakers or the workhog.
[owy99q4] (score 1, diepte 0) Red Wing 2412 8” goretex only boots I buy
[owzzb4t] (score 1, diepte 0) I recently switched from resi construction to cemetery maintenance and Keen is what i have been using. They are super comfortable, but already falling apart after 5 months at the cemetery. I didn’t wear them much doing resi, but only because I was a finish carpentry guy. Building decks, fencing, framing are the times I would wear a steel toe but other than that they got In the way much more than they helped
[ox0z17b] (score 1, diepte 0) Kenetrek hardscrabble ST
[ox1e5t9] (score 1, diepte 0) Thorogood hammerhead
[ox3is9r] (score 1, diepte 0) Costco once sold Dewalt boots. Noticeably the most durable/lightweight/comfortable combo I’ve owned. (Not the most in any one category). And they were like $100
[ox4ege7] (score 1, diepte 0) I stopped wearing steel toe boots years ago. They’re heavy, uncomfortable and frankly I don’t put my feet anywhere there’s a chance they could get crushed. Most of the guys I work with have gone to the more comfortable side and wear hiking boots. Much better especially in the heat, lightweight and better for your body when working long hours.
[ox4gcpd] (score 1, diepte 0) Blundstone 990
[ox5g0qu] (score 1, diepte 0) Timberland Titan Pro 6 inch, I’ve been wearing them for 20+ years probably had 30-40 pairs (I kick chocks for a living so they don’t last)  
I’ve tried every boot brand and always come back to them. Red wings were the worst and most expensive. Lacrosse used to make a quad comfort boot that was also good but they are discontinued
[ox5rzdw] (score 1, diepte 0) Wideload boots. Will never go under 6e again
[ox5wc5h] (score 1, diepte 0) Thorough good mock toe, made in the USA and you pay for them, but they out last any other boot and are comfortable right out of the box
[oxd8kdl] (score 1, diepte 0) I like my brunts
[oxdzh82] (score 1, diepte 0) I swear by thorogoods. I won’t buy another boot. Georgia boot is also another good one. I tried wolverines and ariat steel toes and I won’t get either again.
[p1jlrar] (score 1, diepte 0) The comfiest boot will be the one that matches your foot shape, so try a few on late in the day when your feet are a little larger. Make sure the safety cap isn’t touching your longest toe, the forefoot has enough width and the heel stays secure. If your site allows a certified composite toe, it can also reduce some weight without giving up the required protection. For an insole, check the arch from the inside and front to make sure the support actually extends underneath your foot. Don’t just pick whichever one feels softest for five minutes in the shop.
[owueo5z] (score 0, diepte 1) Hiker. Size 15.  
Have we found Bigfoot?
[owuiatn] (score 0, diepte 0) Go to a store. Try them on, run.

Theres so much difference in choice for whatever boots. I have 4 pairs of the wolverine ramparts, but it took 10 years to break each one in just wrong.

Seriously, go to a store and feel them. We all have funky feet and alpaca insoles only save some souls.

