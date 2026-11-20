# Label-batch batch_0098

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
Schrijf het resultaat naar `batch_0098.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1noyqd1, 4h19ts, 17ay4yk).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1noyqd1 ===
SUBREDDIT: r/Construction
DATUM: 2025-09-24  SCORE: 34  REACTIES: 76
TITEL: Bigger guys in construction, how do you deal with foot pain and aches while working long weeks?
POST (source_id=post):
6’5 280lbs, broke my foot when I was 315 (jones fracture) and been losing weight ever since. Job I’m on has longer hours coming up and gonna admit it makes me nervous whenever my foot ache despite it healing since. Any tips you guys have to get through the day? I usually wear socks with cushion and have doubled up on socks for extra cushion for some extra support. Already have orthotics and good boots, any advice boys.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nfvbxza] (score 70, diepte 0) I lost weight brother. 6’2 pushing 300 pounds was killing me.
[nfvbk8u] (score 37, diepte 0) I do have a massive dick, but I only have to worry about that in the portajohns. 

Apologies - it’s been a terrible fucking day.
[nfvgltx] (score 34, diepte 2) It’s literally all in what you eat bro, track every single calorie. I mean it.
[nfve5yj] (score 15, diepte 1 OP) What kinda changes did you make to lose the weight? Been steadily going to the gym a year now and eating better, upping the cardio lately
[nfvcf7w] (score 12, diepte 0) Beer and weed and good boots
[nfvdjc2] (score 9, diepte 0) I would suggest getting the Dr. Scholl's boot inserts for big and tall men and also buying diabetic socks even if you are not a diabetic; they dry fast, stretch, and are comfortable.
[nfvkdof] (score 9, diepte 0) I was 305 lbs last fall and at 5’9” that made me a fat fuck.  I ate like shit and drank to many IPAs every day.  I gave up alcohol completely and tracked my calories.  I did a steep deficit with lots of cardio and I am proud to say I am 178 today.  The difference in how I feel is amazing.  My back doesn’t hurt anymore, no more sleep apnea, I can move around at work, I have energy for things after work and on the weekend.  Sex is better.  I am in the irrigation industry so I am outside all summer in the heat and having lost 125 lbs has made tolerating the heat much easier too.  

Get some good shoes but really try to lose the weight you won’t regret it.
[nfwh4k2] (score 8, diepte 4) Switch to whiskey. Seriously. You won’t have 10 drinks and you won’t consume 1500 more calories. Drink it neat or on ice, no mixed drinks.
[nfvdcw4] (score 7, diepte 0) I roll my feet each night and morning with a small ball to massage them and get blood flowing
[nfvbp5w] (score 5, diepte 1) have you tried using a wheelbarrow
[nfvg2e5] (score 5, diepte 2) Gym is great, eating better is great. Biggest difference maker for me was IF and drinking a shit ton more water.
[nfvr1jq] (score 5, diepte 2) I went from 325lbs to 165 lbs, 5'11". When I was much younger. 

I started by rowing with a shitty old duck boat with oak locks along with riding road bike. I rode to work, to the grocery stores, etc. Eventually I was riding around 20 to 30 miles a day, and I could happily push 25mph constant for over an hour.

When I started rowing I'd row down the lake, with the wind, until I had nothing left. Then I'd still have to row back to my lot with my truck, just dead tired. Just pushed when it was easy until I had nothing left, only to be left with getting back home.

 When I first started riding road bike for distance/endurance I'd listen to angry music(like Immortal Techinque) and I'd just push. I'd push until all the muscles in my legs felt like they were on fire. I'd push as far as I could, again, only to have to ride back home. 

In general, I embraced the suck. I'd probably die of a heart attack if I ever tried that again. But even today I can grab my road bike and do a 20 mile ride in a hour. I'll sweat doing it but it'll be easy, and god damn it feels good. And eh, I'm kinda fat these days, 190 lbs. 

Regardless, just dieting isn't going to do it. Some light cardio isn't going to do it.  You need to get motivated and push yourself.
[nfvyh68] (score 5, diepte 1) Hey man-don’t know you but that’s a great thing that you have done for yourself and your family. Super proud of you and you should be too.
[nfvm2w0] (score 5, diepte 0) Good boots paired with custom orthotics. Pain is gone. Use to be sore every night. Never sore now, worth every penny.
[nfvcoo3] (score 4, diepte 1) This and good boots. Some of us are better off biting the bullet and buying a more expensive boot. The feet can fuck everything up. And bring taller and bigger does not help
[nfwfkug] (score 4, diepte 3) But what’s the point if I eat smart for 5 days but then sit down and drink 14 beers on Friday night ??
[nfwmsl7] (score 4, diepte 5) My brother did whiskey and water then switched to just water with the occasional vodka shot. He lost his "beer weight" pretty fast.
[nfvf27q] (score 4, diepte 0) Keen makes some comfortable boots and the timberland boondocks are pretty comfortable as well
[nfvse08] (score 3, diepte 4) Good shit. Don’t forget to throw in a rest day. Atleast one if your gonna go hard like that. I’m hitting 4-5 days a week, with a few rest days. And just recently got into doing squats. Holy shit that was a big game changer. After 36 years I’m finally able to do chin ups. And I thank the squats for that.
[nfvdfh5] (score 3, diepte 0) Gotta keep losing weight man. I’m in the same boat.
[nfvnpwx] (score 2, diepte 3 OP) Nice man, been going protein heavy myself too. My gym time’s decent I’m back in my habit of going 6-7 times a week, hour long workout each time usually. Gotta get more veggies in my diet
[nfvntit] (score 2, diepte 3 OP) Stopped drinking alcohol a while ago and no energy drinks
[nfvjikg] (score 2, diepte 0) see foot doctor.  wear super lite boots. danner,  hush puppies. and carpenter boots.  these are white bottom superlite. I wear therogoods  carbone toe no insulation.  good luck
[nfx7ekl] (score 2, diepte 2) Thank you!
[nfxwhz2] (score 2, diepte 0) I have foot problems as well and what helped me most was losing weight. I lost weight pretty easily by cutting out fast food, chips and soda. I drink water, snack on carrots and prepare my own meals. Now my feet and back feel much better and my tool belt is more comfortable.
[nfyktwz] (score 2, diepte 0) It’s ok to indulge in binge drinking every once in a while but I think we were talking about drinking 10 beers on a regular Friday night
[nfvbyei] (score 1, diepte 2) Yeah. But then her arms get tired.
[nfvmapf] (score 1, diepte 2) Randy! Your balls!
[nfvhpyj] (score 1, diepte 2) I’ve been wearing Wolverine’s for years now, I know there’s better boots but just throwing it out there what dropping some pounds can do.
[nfvxtnn] (score 1, diepte 2) Get some hikers with safety toes and prepare for it to change your life.

My boots get pulled out a few times a year for heavy shit days.  Besides that, I’d rather not hurt myself 999/1000 days with the chance of maybe breaking a toe that 1000th day, than hurt myself every day for 1000 days just so my toe gets *slightly* less broken
[nfy7fqb] (score 1, diepte 6) I started doing this with gin and tonic. I don't really like heavy Juniper but I found there a lot of citrus forward gins. Anyway, a little bit of gin and a lot of zero calorie tonic tastes like I'm throwing them down, but in reality I'm at a couple hundred calories tops by the end of the night. I'm also super hydrated
[nfyawk3] (score 1, diepte 5) Cheat code to the mixed drinks is just mix it with zero calorie soda. Vodka zero calorie sprite taste delicious
[nfyhlff] (score 1, diepte 6) Don’t do mixed drinks. Way too easy to drink too much alcohol
[nfyim9m] (score 1, diepte 7) Way too much alcohol = way too much fun!
[nfvhkrm] (score 1, diepte 2) Been dieting/ going to the gym since this past November,  I went super strict in the beginning. I have a big sweet tooth, so I cut out carbs and dairy. Literally ate mountains of almonds and fruit. For the first 3 months. And protein. I went heavy on the protein. Eggs, steaks, ground beef/ turkey, chicken. I still eat like that today, heavy protein, fruit or broccoli, it’s just alittle more balanced now. How’s your gym time?
[nfvmxia] (score 1, diepte 2) Calories in, calories out. If you're on your feet a lot your intake must be huge. Judging by others in this field you might be drinking a lot of your calories with energy drinks or alcohol.
[nfvnyl0] (score 1, diepte 2) It’s all about diet.  If you are working out lots you’re gonna be more hungry just gotta have some good metal strength to control the treats
[nfw0uom] (score 1, diepte 3) Shout out to immortal technique!  Been on an angry 90s tip lately, and been rocking Jedi Mind Tricks a bunch.
[nfvunqp] (score 1, diepte 2) Tirzepatide kicks ass if you can afford $500 monthly
[nfvym2p] (score 1, diepte 2) Caloric deficit brother. Keep swinging that hammer, hydrate religiously and you'll start getting some muscle mass that will give you a higher resting metabolic rate. You have to eat CLEAN though. Do as much education as you can on what is good for you and what is necessary for your macro nutrient intake.
[nfw1b6b] (score 1, diepte 2) No, bread, no sugar, and buy a good pair of wedge thuroogooods.
[nfvclqe] (score 1, diepte 0) Keen Braddock boots are so comfortable.  That and maybe taking them off at break time if your having a tough day. 

6'5" 220 here.
[o9fewhp] (score 1, diepte 1) This is the one thing that made the biggest difference for me outside of what i put in my boots. frozen water bottle works well too if you've got inflammation going on, gets the massage and the ice at the same time. i do it for about 5 minutes each foot before bed and my mornings are completely different now. used to hobble around like an old man for the first hour, now i'm good to go straight away. tight calves feed into it too so rolling those out with a foam roller at night is worth adding if you're not already.
[nfveptv] (score 1, diepte 0) 225 and 6’2” here, I wear wool socks and that’s about it. I averaged 26,000 steps a day last year and I’m often on my feet all day everyday but I’m only 44 so maybe it’ll get harder in the future, I think don’t get foot pain yet.
[nfvkupy] (score 1, diepte 1) I have the keen vista energy mid with the carbon toe. It's the lightest and most comfortable boot I've ever owned. They feel like basketball shoes.
[nfvfan9] (score 1, diepte 0) I dealt with it by leaving construction
[nfvg7r3] (score 1, diepte 0) The foam wedge style boots are very helpful. Usually have white bottoms. Most cushion I’ve ever had in a shoe. Losing weight makes the biggest difference.
[nfvg859] (score 1, diepte 0) There's tons of different types of safety toe shoes that aren't boots. Continue doing what you are doing, but look into some of those other types of shoes. I typically wear thorogood boots, but I also wear combat boots, sneakers, and even boat shoes like hey dudes all with osha compliant safety toe. Depending on what im doing that day, I'll choose accordingly.
[nfvge8c] (score 1, diepte 0) GET SOME CUSTOM MADE ORTHOTICS. Changed my life man I can stand and walk for 12 hours + instead of suffering after 6 hours. They'll run ya 600$ but you will thank me
[nfvo31k] (score 1, diepte 1 OP) I got custom made orthotics they were great at first but haven’t felt the same even though I’ve lost weight since
[nfvgeoz] (score 1, diepte 0) I don’t how guys with the big guts do what they do. They’re also pretty good and what they do. I always figured the got in young and learned the trade and then got progressively bigger over time.
[nfvhqrh] (score 1, diepte 0) 6'1" 220. You have to do stretches and exercises that elongate your achilles and strengthen your lower back. There are no muscles in your foot, everything is in your calf, so if your achilles is too tight, foot pain will crush you. And they're actually really simple. I do two main ones, before getting out of bed I do some knee-chests, and then some whatever it's called keeping your shoulders flat and leg over leg, just stretching out the lower back. For achille's they'll tell you all kinds of bullshit but here's all you have to do, get like a sturdy table leg or a column than won't move and inch down, but keeping your heels on the floor. Some call it the "asian squat" or the "weightlifters squat" either way keep doing that until you can squat with your heels on the floor, knees up to chest and can even lean forward a bit without touching the column. Takes a few months, but you'll never have foot pain again.
[nfvi6u3] (score 1, diepte 0) Change shoes and socks halfway through the day and get fitted for proper insoles.
[nfvi7of] (score 1, diepte 0) Danner boots and drink a ton of water
[nfvj8co] (score 1, diepte 0) Diet. Lose weight.
[nfvk6yf] (score 1, diepte 0) Some good solid boots with good ankle support and then a good insole with arch support. You keep them laced up snug and retie them through the day as they get loose. Everyone is saying lose weight. That's gonna happen no matter what working so start with creating an excellent foundation for your feet and ankles. They gonna be carrying you all day so help em out.
[nfvlkyv] (score 1, diepte 0) Orthotics.  Massages.  Weight lost.  Eating HEALTHY and drinking WATER.
[nfvmja1] (score 1, diepte 0) Go find your nearest good feet store and buy the expensive in soles. The best thing you can do for your body is treat your feet.
[nfvo0c7] (score 1, diepte 0) I stopped wearing boots on the job like 10 years ago and I will never go back. Get a pair of these it'll change your world. Actual foot shaped with more cushion you'll ever find in a boot. You'll thank me later. 

https://www.altrarunning.com/en-us/trail/mens-olympus-6/AL0A85NJ.html?dwvar_AL0A85NJ_color=001
[nfvoer5] (score 1, diepte 1 OP) I work on sites with steel toe / 6” heel requirement
[nfvq8al] (score 1, diepte 2) That sucks, but a heel requirement? Why would they want you wearing high heels?
[nfvq3iz] (score 1, diepte 0) Keep losing weight.  Weight is your worst enemy because your foot is your base. I think you'll feel a whole world of difference at 250.  I'd recommend Whey. When you're feeling hungry but you really shouldn't continue eating, a glass of protein and water will fill your stomach for the night.  You can even blend berries, bananas, avocados, or whatever to make it tastier and fill your stomach.
[nfvqdpd] (score 1, diepte 0) It's all about the right match of shoes, and it took me a while to not lace up so tight.  I  also figured out that the most work I do all day is dragging my carcass (which includes a deep love of beer and ribs) around.  Since then, I try to work very efficiently, knowing that skinny little 20 something dudes can afford to run back and forth to the truck 8 times, but it's better if I load up and make 2 trips.
[nfvsmfo] (score 1, diepte 0) Easy its best to spend $300plus on good boots every 2-3 months replace
[nfvsodp] (score 1, diepte 0) Barefoot shoes when not at work. On your feet all day but the muscles get no exercise
[nfvsydw] (score 1, diepte 0) What boots are you rockin?  What trade?
[nfvv7h0] (score 1, diepte 0) Where I live there are a couple of places (maybe chains) called the foot works and another called the good feet store. They are probably similar. They seemed like they knew more and cared more than any podiatrist I ever went to. They take like an hour with you to get you custom insoles and proper shoes. The insoles were really better and cheaper than what the podiatrist sells you on your first visit. (Whether you need them or not). Find a place like this.
[nfvwhdx] (score 1, diepte 0) You can't outrun a bad diet. Have 2 pairs of work shoes to rotate through. Ditch the belt and get suspender
[nfvwsjc] (score 1, diepte 0) If you can get orthotics, do!
Other advice would be to get a foot massager, like the electric one, preferably one that heats.

Like you I broke my fifth metatarsal, not exactly a jones but really close. I was off my foot for 3 months, and it was super rough getting back into it.
[nfvxjqv] (score 1, diepte 0) Loose weight. Fasting (believe me it works, you’ll feel better throughout the day). Orthotics from a fitter or see a podiatrist. Eating clean. Supplements.
[nfw0az4] (score 1, diepte 0) Keep on working on the weight. 

I’d also start working on your foot/leg strength.

Your foot has an arch, guess why it’s called that, because it’s literally an arch. The more you push down on an arch the stronger it gets, the more you push up on an arch (arch support/padding) the weaker it gets. 

Just basic physics here, also your foot’s muscle and tendon support structure atrophies. 

You won’t be able to do a full switch right away by anyone and but start doing more and more things barefoot. Go run around in some grass, don’t wear shoes or socks outside of work whenever possible.

Maybe get some wide toe box zero drop shoes and start wearing them when you don’t need hard toes.
[nfw17p6] (score 1, diepte 0) Yup.
I'm 6'2" and 235lbs and it is taxing to pull long days.
[nfw24yx] (score 1, diepte 0) Im about 305lbs right now, and i know you guys talk crap on them but the timberland pros are so comfy and make my back feel bigger. Most other boots i have to add insoles.
[nfw58rm] (score 1, diepte 0) Stop eating at the gas station. Do cardio and eat lots of fruits and vegetables
[nfwe7ek] (score 1, diepte 0) Gotta invest in some good comfortable boots and try to keep your tool bags as light as possible. Look into getting some CDB oil with THC in it. When you’re off work, don’t wear shoes. Only slides and stay off your feet as much as possible. Also don’t sleep on those massage parlors. You can get a nice 30 minute foot massage for like $50
[nfwnql4] (score 1, diepte 0) At 47 I was 225 and 5'9. Cut back on sugar, salt and portion control. Soon to be 50 and at 170. Spend more $ on great shoes or boots with custom orthotics. 
When your feet hurt, you become a couch potato in the evening. 
Stay healthy and active.
Good luck!
[nfx3cus] (score 1, diepte 0) There’s this wonder drug taking over the world. I’ve lost 40 on it so gar. It takes the noise of being hungry out of your head giving you the choice of how you eat. Mounjaro for the win
[ngjgxv7] (score 1, diepte 0) Buy  good boots and i always preferred the wedge soles seemed like it was easier on me then a boot with heels
[o9fdo2e] (score 1, diepte 0) Mate i feel this one. carried a lot of weight through my 40s and the feet cop the worst of it when you're a bigger bloke standing all day. that jones fracture would have weakened the whole structure on that side too so it makes sense the pain keeps coming back under load.

Doubling up on socks might actually be working against you. feels like more cushion but it restricts blood flow and makes your feet swell faster on longer shifts. your toes need room to spread and grip naturally or the pressure just concentrates in the wrong spots.

The orthotics could be part of it too depending on what type. a lot of the rigid ones are built for a neutral foot and if your mechanics changed after the fracture they could be pushing force into areas that can't handle it. you want something with actual shock return not just a hard shell holding your arch in place.

i ended up trying some insoles a bloke on site recommended, i think they were called WorkFit insoles, and on concrete the difference was noticeable within the first week. by hour 8 they still felt like they had something left in them which is what sold me.

the weight thing everyone's saying is legit too. every kilo you drop takes about 4 kilos of force off your feet per step. you're already heading the right way with that so keep at it.
[nfvjgc5] (score 0, diepte 1) have an apprentice hold it

=== THREAD 4h19ts ===
SUBREDDIT: r/electricians
DATUM: 2016-04-29  SCORE: 119  REACTIES: 76
TITEL: The fishtape is now a few feet shorter
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[d2ms1ou] (score 49, diepte 0) I've done it.  My friends have done it.  We've probably *all* done it.

But you see accidents like this and realize just how *genuinely fucking stupid* a lot of the hot work we do is. 

There needs to be a serious culture change in this industry.  If you told a layman "I'm gonna feed this long steel spring into a piece of energized electrical equipment!" they'd look at you like you were retarded, and they'd be right to.
[d2mlfoc] (score 31, diepte 0) They make fiberglass snakes (fish tape) on a roll.
[d2mlu1g] (score 27, diepte 1 OP) That's what I would have used. They violated company rules by even pulling wire into the live cabinet. Now I have to undergo lockout /tag out training again even though I only do signal wiring.
[d2mupyo] (score 26, diepte 0) This is the type of stuff that should be on /r/osha not receptacles without cover plates or someone standing on top of a ladder.
[d2mqstp] (score 22, diepte 1) There's nothing worse than hearing the bang through the pipe, and having to run down the hall to see how the other guy is...
[d2mxhjy] (score 22, diepte 2) And the problem with "We can't afford to shut down!" is that if your business can't afford a planned outage, then it sure as hell can't tolerate an *unplanned* outage.

We do a lot of failure repair work:  I've been involved in way too many post-mortems to believe that all accidents can be avoided.  It's not if, but when something goes wrong, I'd damn sure prefer it to happen in deenergized gear instead of having guys on the business end of 50,000 amps at 480V.
[d2mq0ua] (score 20, diepte 0) Jesus.

I was feeding fish tape to a guy years back where he was on top of some 480 switchgear. It was a data facility so there was no downtime for the setup work leading up to connections being made. 

I was feeding and when the tape came out he couldn't keep up with my feed and I couldn't hear him (rooms away) saying stop. It looped into the gear. 

He was fine, nothing blew up. A breaker tripped and the fish tape vaporized...but I can still remember feeling my brain shut down trying to process that this guy had almost died. 

To say I've been more mindful since is an understatement. Thankfully this lesson (or mine, for that matter) wasn't more costly.
[d2mwu37] (score 19, diepte 1) I used to do it all the time just like everyone else. Then something clicked over the many safety classes I've had to take. So I decided I'd try to do all panel work by the book (our book anyway) and realized that it really isn't that much effort to shut down a panel. Maybe you put it off a couple more days or come in a couple hours early. 

Other foreman give me crap for it when I help out on their jobs (and tell them no one is working in a live panel unless absolutely necessary and with a hot suit) but at least my guys know there is no way I'm letting them do it.
[d2mynzg] (score 19, diepte 1) I'm a new apprentice, young guy, and I absolutely refuse to do any live work.  It gets turned off, and I have already gotten into arguments with people regarding this.  It's also illegal.

My take away is, I have three young kids and all it takes is for me, or some other fucking moron, to have a bad day, or cough, or have a hangover, or be drunk, etc at the wrong time and I get my dick blown off. 

We were working at this large commercial job, a warehouse with three automotive shops and the guy there said "I'd love to work on this live, it teaches you respect for electricity."  I had to call him out and it started a big argument about how I'm the pussy. I don't understand how people can be so flippant with regards to this.  Electricity is safe, but she is an unforgiving cunt.  It's fucking terrifying.

I implore other people to stand up for yourselves and not to do anything that is unsafe, no matter how fucking safe some dick tells you it is, you the only way it becomes safe is if you turn the fucking thing off.  You cannot be fired, at least where I am, for refusing to do work that is unsafe.  Actually, if it comes down to it you can call the ministry of labour on their ass and see if they like fines. I'm sure they love fines. Have zero loyalty to anyone who does not respect your safety.
[d2mkt79] (score 18, diepte 1 OP) Thanks for asking. Thankfully, nobody was injured. I was not involved. They tried to pull new wires into a live panel. The fish tape made contact with 480 and ground.
[d2n1c11] (score 16, diepte 1) that sub is a weird blend of pedantry and circlejerk
[d2mzcl9] (score 14, diepte 2) The problem with the "respect for electricity" argument is that it's based on a completely bullshit notion that if you're just awesome enough, you'll never get hurt.

1) I have made many mistakes in my time and I have seen guys way more talented than me fuck up just as bad:  Everyone screws up eventually, the only thing that will save you is what steps you took ahead of time to safeguard against that.

2)  Even if you're perfect, the tools and equipment are not.  I have worked a ton of blowups where nobody was even nearby, but an insulator finally failed, or a contact got stuck, or a lug came loose.  Totally unpredictable events that no amount of Being Awesome would've stopped from happening if some poor bastard had been unlucky enough to have his face in there when it blew up.
[d2my3g5] (score 13, diepte 4) I get a lot of shit for saying it but look at the difference between the average sparky and the average lineman.  I went through the liney safety training when I worked for the utility and they practice it like a religion:  Guys wouldn't dream of not using gloves and cover-up, even on LV.

Then you got electricians where maybe 1 in 5 even own insulated gloves?  Or we just wrap beat up old tools in electrical tape?  Is it because so many of us have gotten buzzed and survived that we just shrug off the risk?  It never kills you until the day it does.
[d2mofr4] (score 12, diepte 1) Seems like your company isn't run by electricians ...
[d2miomi] (score 11, diepte 0) holy fuck. are you alright?
[d2mmlw7] (score 11, diepte 0) I guess this is why my company banned metal fish tapes. It really makes it a bitch to fish a wall. Good thing they didn't ban suspended ceiling tie wire.
[d2mxs7h] (score 9, diepte 3) Too many people get it in their head that "sometimes you have to do what you have to do" then they just use it to justify their actions. I hate the excessive use of cliches but safety really is a culture. People have to default to the safest options automatically and not just come up with an excuse when they haven't planned something properly
[d2mks2c] (score 7, diepte 2 OP) Thankfully, nobody was injured. I was not involved. They tried to pull new wires into a live panel. The fish tape made contact with 480 and ground.
[d2mvuef] (score 7, diepte 3) > They tried to pull new wires into a live panel. 

With a metal tape? Yeah, how could that go wrong?
[d2nh56s] (score 7, diepte 3 OP) I wasn't involved in the incident, but the company is making everyone in engineering undergo retraining. I never even work on AC power, just low voltage DC and signals. I'm not complaining, but it is a waste of my time. They write the checks, so I do what they want.
[d2og72v] (score 7, diepte 3) Vac goes on one end of conduit, helper with bag tied to end of string feeds bag into other end of conduit.  Vac pulls bag and string through, use string to pull your wire or a stronger pull rope into conduit.
[d2mw32v] (score 7, diepte 1) Fiberglass rods are the superior wall fishing impliment anyways. The fiberglass/nylon tapes suck though.
[d2mmtdd] (score 6, diepte 1) Yup! On certain jobs(hospitals) we have to use fiberglass fsh tapes for that very reason.
[d2myo5p] (score 6, diepte 2) Nightmares man.
[d2nf6br] (score 5, diepte 2) Re-training is a pretty light punishment. At my company someone directly involved in a lock out tag out violation is suspended for 2 weeks without pay and has to write an essay explaining how they'll ensure that they're never be involved in a LOTO incident again in order to return to work.
[d2ne4dz] (score 5, diepte 4) I always just yell down the conduit to my journeyman "Hey fuck head, I got the fish tape"
[d2n9taz] (score 5, diepte 1) That sub should also require posters to cite OSHA.
[d2ng0yr] (score 5, diepte 2) To be fair, it was kind of dual purpose for parodying safety vids as well as safety code violations. But yeah, 90% of it is people posting pictures of telephone wiring or someone on a ladder or some retard driving down the highway with an unsecured load.
[d2mjw9w] (score 4, diepte 0) The kind of picture that puts a nasty shiver down your spine...
[d2nd0gj] (score 4, diepte 1) That or a large wet/dry vac, a bucket of string, and a plastic bag. Nothing metallic to be energized, you know damn sure what pipe the wires are going into/ out of, and sometimes much easier to get around bends.
[d2n9lok] (score 4, diepte 3) A couple other methods to signal to the feeder that you've got the fish tape when the other person isn't within earshot:

- bang in the pipe with your pliers a few times - the sound should travel through the pipe back to the person feeding the 

- give the fishtape a quick yank. Or push and pull it backwards and forwards a few times. The person feeding it on the other end will know that something is up, and should stop to investigate.
[d2mvrst] (score 4, diepte 1 OP) I don't know, it was sent to me with a notice of mandatory retraining in lockout/tagout procedures.
[d2mjnli] (score 3, diepte 1) Does OP still have pants to poop? What level of Arc Flash Protection was everyone wearing?
[d2mpkhc] (score 3, diepte 0) And someone's pants are a few pounds heavier.
[d2o5nr5] (score 3, diepte 5) sounds like the company I work for
[d2n61qo] (score 3, diepte 1) Guy here who knows almost nothing about electricity, and I'm indeed wondering why the fuck electricians like to play with death working with live equipment.
[d2n0oad] (score 3, diepte 1) Hey, don't knock it 'til you try it. ;)
[d2nh3tt] (score 3, diepte 3) I think they're so afraid of heights related regulations that they refuse to upvote anything either. It's an all day downvote fest in the comment sections.
[d2my4da] (score 3, diepte 0) As a first year apprentice, I enjoy seeing pictures like this to remind me just how dangerous this job can be. I hope I find myself thinking ahead, and being aware of dangers like this in my (hopefully) long career. Thanks!
[d2n0nem] (score 3, diepte 0) Why didn't you use a fiberglass fish tape? They are great things sometimes.
[d2mjbq6] (score 2, diepte 0) Did you poop your pants a little ?
[d2o5iog] (score 2, diepte 2) please enlighten me more on this shop vac, bucket o' string and plastic bag technique
[d2ogomp] (score 2, diepte 4) This is awesome.  LPT
[d2p38ck] (score 2, diepte 5) It has been my preferred way of pulling for a while now. Particularly if I have a lot of conduct and wires to feed from one area. Let's say I'm at a panel, and there are 20 runs coming off it going to various areas in a building. Well, all I have to do is set up the vac in the panel room, and send the helper around with a pocket full of plastics bags and a bucket of pull string. I'll put the vacuum on the pipe, he'll put the rat( chunk of plastic bag) on and send it. I cut the rat off, tie on the wires to be pulled, and he can pull away. The wire reels and vacuum stay in one central location, and the only thing to be moved is a bucket of string. Very cost effective and labor saving. No trying to push a fishtape through, then pull it back. Plus, if there's and mud, water, or rocks in the pipes because the concrete guys were shit heads, the vac will remove most of it.
[d2oxx42] (score 2, diepte 5) Only if you are Australian.
[d2ng7wv] (score 2, diepte 3) Unfortunately most safety guys are just desk jockeys and university graduates. Like the people at the ministry of labour in Ontario who have outlawed working off of ladders. Even if it's a 4' A frame ladder, if you are doing anything that causes you to not have 3 points of contact (only hands and feet count) and your stomach is above the top of the ladder, you're in violation and could get levied a fine. Using only one hand it would literally take a half dozen electricians to hang a light... Extension ladders are only acceptable for access and egress now, but need to be secured at both ends.

The only legal ladders for working off of now are those stupid platform ladders (but only if you have the chain on it to keep you from falling off!). Because someone at the ministry of labour seems to think that electrical devices and conduit ALWAYS goes in the dead center middle of a room that has scissor lift access...
[d2npk57] (score 2, diepte 3) >  The problem with the "respect for electricity" argument is that it's 
> based on

There's the argument that you should learn to work on live things, so you can conduct all the proper practices for working on live things appropriately.

Then in the field, once you've learned how to work on live things.... you **always** de-energize first,  but work on the de-energized circuits  observing the precautions **as if they were live**.

See turning things off is not a 100% guarantee;  it's a 99% guarantee in most cases,  but   uou might find situations in which strange things happen  as a result of errors or faults elsewhere in an electrical system.
[d2nptdl] (score 2, diepte 4) It's why in another comment I made the comparison to how linemen do hotwork:

I honestly believe that a lot of hot work can be done with reasonable level of safety.

I also believe very few electricians are equipped or trained to actually do that.  Which is why I don't give any credence to most people's argument about how they should be allowed to work hot.  The OP is a good example of this.
[d2o5rs7] (score 2, diepte 2) Sometimes it needs to be on for us to find the problem.  and we have to open it to test it, and test it while it is on.  but most cases, it is pride, honestly.  Too many, including my boss, put safety in second place to getting the job to work.  In residential and commercial, the customers do not want power shut down, they have stuff to do while you work.   by no means an excuse, just trying to answer your question
[d2ms5ox] (score 2, diepte 0) Aw hell naw.
[d2mu68b] (score 2, diepte 0) Should have put some cardboard covers over the bus.  /s
[d2nh1h6] (score 2, diepte 3) That's a good point. I guess not all sparkys are windowlickers.
[d2mvklb] (score 2, diepte 0) What was the justification for working this hot? What sort of PPE was being used, if any? Nobody's life is worth a few hours of downtime.
[d2n4yor] (score 2, diepte 0) Similar thing happened to a guy at my last company except he wasn't pulling into a cabinet, he was pulling into a 4x4 on the other side of the room and got careless with the fishtape, which did its thing and found its way into the worst place it could, between a buss bar and its cabinet's frame. This was at an airport in the middle of the day no less, so once the place dropped to generator power they had about 20 airport guys down their necks. Must have been fun explaining that one.

The guy who did it, after a few more years of fucking shit up, has been promoted (demoted?) to junior estimator where he can do less damage. Did I mention he's the owner's nephew? Funny how that works ;)
[d2n874a] (score 2, diepte 0) This is why we can't have nice things!
[d2ncjc7] (score 2, diepte 0) This is one of the scariest pics we've seen here in a while.  Glad nobody got hurt or killed.  Hope you use it as a learning experience.  Stay safe.
[d2nz8gd] (score 1, diepte 2) **Much** easier. Had to do some low voltage audio networking runs as a sub for the main electrical contractor. They put us in conduit... with at least 9x 90 degree bends and no pull string on a 200-ish foot run. The walls had already gone up when we found out - not that it would matter they didn't put in pull boxes for us. Low tech shop-vac method to the rescue.
[d2oxaes] (score 1, diepte 4) Can one substitute snakes in place of string if one is out of string?
[d2mw2qc] (score 1, diepte 1) Thinking outloud, but can't Klein's stop the feed? Use the bite under the pivot to grab the tape right at the pipe. We all use that bite to pinch and pull fish tape, I guess it could be used to pinch and stop fish tape as well.
[d2mwz91] (score 1, diepte 2) You could probably just grab it with your hand. Hate to drag a victim through the mud but I'd guess he probably wasn't paying attention
[d2o5lcz] (score 1, diepte 2) I stopped doing this because I chipped my two front teeth using the pliers bite to pull fish tape.  It just slipped right off and my Kleins smacked me right in the puss.
[d2ns7br] (score 1, diepte 3) Well played.
[d2nk3mk] (score 1, diepte 1) Your best bet for thinking ahead is to question. If you, or your JW is asked to work it hot, ask why. That goes for everything, from a 120V receptacle changeout, to opening up a 480V gear/panel. If they somehow justify putting your lives in danger, ask if an arc flash study has been completed and make sure they provide you with the properly rated PPE; faceshields, gloves, 8, 10, 20, or 40 cal suits w/hoods.
[d2q9zrx] (score 1, diepte 2) We use 10 calorie in our plant. That wouldn't have saved you from that arc flash on that cabinet. I can't imagine using a metal fish tape going into a live cabinet.
[d2n09wn] (score 1, diepte 0) Whoever did this should be fired. There is no excuse for this level of dumbfuckery. It looks to me from the picture that fishtape came up through the floor and hit the main buss. The bottom cover is still in place and obviously no one was watching for it. Depending on the damage to the gear which I'm guessing is extensive,  they'll probably have to replace the whole cabinet. Not cheap. At least they lived to look for another job or maybe another career.
[d2n1k23] (score 1, diepte 0) It's crazy stupid shit like this that reminds me that as an electrician I am almost the lowest paid guy on site and I could be poof in a second. Similar thing happened to us on our site. Fellow was hooking up a 480 volt crane. Didn't realize cable was live, went to put connector onto cable and now his hand is melted cheese. Had to go thru lock out training all over again.
[d2ne7yi] (score 1, diepte 1) Lowest paid guy? Journeyman electricians where I'm from make 10 more an hour than the labourers and like 4 more than the carpenters
[d2nplb1] (score 1, diepte 2) Those are like the only few that are paid less then us. Although neither of those types of work require school. My second year roommate tin basher apprentice makes the same amount I do as a 4th apprentice sparky.
[d2nrn1w] (score 1, diepte 3) In cali electricians and yin beaters are paid the most
[d2nzt0c] (score 1, diepte 4) JMan wage for us is like 27-30ish depending on your capability in the eyes of the owner. JMan wage for Tin Bashers is 40/hour. I'm like. Wow. Whoever told me electricians made money lied. I make $23 as a 4th year.
[d2o1qoj] (score 1, diepte 5) I make 20 an hour as a first year in California
[d2ojfuu] (score 1, diepte 6) Our first year green rate is 13.50
[d2npjaf] (score 1, diepte 2) No. You need to. Plumbers make $3-5 more an hour then us. Tin Bashers make $8-12 more then us. Industrial painters make $1-3 more then us. Carpenters get shafted where I'm from and make like peanuts. Brickies make $1-4 more an hour. Steel stud guys don't come to work for more then $40 an hour. Which is insane. Even drywallers get paid on par or better. Only labourers, carpenters and concrete finishers make less then us.
(3 reacties met lagere score weggelaten)

=== THREAD 17ay4yk ===
SUBREDDIT: r/pharmacy
DATUM: 2023-10-18  SCORE: 24  REACTIES: 75
TITEL: Shoe recs
POST (source_id=post):
Retail pharmacists or any pharmacists that spend majority of their days on their feet - what shoes or inserts have you found to be the best for comfort and not feeling like your back and knees are on fire after your shift?

Appreciate any recs thank you!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k5fw6jn] (score 19, diepte 0) I like Hoka One One Bondis. I used to wear adidas ultra boosts but find the bondis more comfy. I want to try the brooks ghost next. I’m always on the hunt for the next best thing. Tempted to try Cloves but they’re so ugly.
[k5fz6ju] (score 13, diepte 1) The [Hoka shoes](https://amzn.to/3M5wUNA) are ugly AF honestly, but they are so comfy.
[k5g8id8] (score 10, diepte 0) I like Brooks , they make one for walking on roadway and it has a really open toe and soft feel
[k5glm3z] (score 8, diepte 0) I very much follow this philosophy as to why these work, I have flat feet (a long with my bone actually pushing down further to make them flatter than normal) have done every medical grade insert and shoe gimmick. Barefoot shoes are hands down the only thing that have worked after 18 years, 8 of which have been in pharmacy. 2 of the last 8 years with barefoot have been a game changer, it took 2 months to adjust. But was worth it. https://youtu.be/KbsH6mpATUY?si=6pZKqibFopZNQAty
[k5fzp3t] (score 6, diepte 0) [Adidas Ultraboost](https://amzn.to/3rTSyO1) are probably the best. Also, your sock choice matters a lot!
[k5gl2io] (score 6, diepte 1) Yes, I have them and love them for retail. I used to wear New Balances for years and switched to Clove about a year ago. I got some for my boyfriend who works retail (not pharmacy), and he also has told me that it helps with his back pain.

But all of these “what shoes should I wear?” threads aren’t asking the right question. Properly fitted **compression socks** are what actually make the biggest difference for me in terms of how tired I am at the end of my shift.

I have some cute Figs compression socks that have cute amber vials on them and say “bottle service” on the bottom. There are other vaccine-themed socks that say “hit me with your best shot” and “shots fired” on them.
[k5i8a3i] (score 6, diepte 0) I just take Percocets
[k5g0ezy] (score 5, diepte 0) I have a few pairs of Brooks Ghost that I alternate every day. haven't tried Hoka but hear a lot of people recommend them. I think a good thing to do is have multiple pairs and alternate. Was able to snag mine for cheap on goodwill online, basically new.
[k5h9lql] (score 4, diepte 1) Bare foot shoes with a good pair of compression socks has been my winning combo for the last 2 years!
[k5fzvd9] (score 3, diepte 2) Yeah super ugly but recently got a light baby pink pair that doesn’t look as bad as my black ones.
[k5g6qpt] (score 3, diepte 1) Just switched from Brooks Adrenaline to Hoka Bondis and the Bondis are much more comfortable in my opinion.
[k5h0q4e] (score 3, diepte 1) Hoka ftw
[k5g0hjc] (score 3, diepte 1) Asics gel kayano and quarter length compression socks recently bought is really making a difference when standing a lot
[k5g9l9k] (score 3, diepte 0) I rotate between a few. I find rotating is the best way to maximize the life of the shoes, and keep your feet from getting super sore by the end of the week. 

[Hoka Bondi SR](https://www.hoka.com/en/us/womens-walking/bondi-sr/1110521.html?dwvar_1110521_color=WHT). A bit heavy but very comfortable for long days standing.

[Allbirds Mizzles](https://www.allbirds.com/products/mens-wool-runner-mizzles-hazy-indigo?price-tiers=msrp%2Ctier-1%2Ctier-2%2Ctier-3%2Ctier-4). Nice for the winter because they are slightly water resistant and warmer than synthetic shoes

[Kizik Roamer](https://kizik.com/products/mens-roamer-blackout). My current favorites because they slip right in and out which nice. Very light and comfy.
[k5gf75c] (score 3, diepte 0) Hoka Clifton
[k5hen58] (score 3, diepte 0) Just sit man, we got a chair in the pharmacy and whoever is in the main chair sits when they can
[k5hry5s] (score 3, diepte 1) Well lucky you.
[k5icvgg] (score 3, diepte 1 OP) That’s not really an option at walgreens lol
[k5ir5cr] (score 3, diepte 2) Sure it is. Find / bring in a chair and sit in it.
[k5ihqvi] (score 3, diepte 0) Anyone have recommendations for people with bunions?
[k5g8ar2] (score 2, diepte 1) I have the Bondis too. They’re so ugly there cool
[k5kixpg] (score 2, diepte 1) I bought cloves and I was underwhelmed!
[k5g921g] (score 2, diepte 0) The only ones that alleviated my plantar fasciitis were Vionic and Danskos
[k5hygy6] (score 2, diepte 1) Vionic is the only thing I wear anymore. And they are SO CUTE for orthopedic shoes! I get compliments all the time!
[k5gcgpc] (score 2, diepte 1) I’m curious about them too, but I’m worried that they might not be wide feet friendly.
[k5gvhux] (score 2, diepte 2) I read some reviews and they do not carry wide sizes ☹️ so I did not consider them anymore
[k5h61cr] (score 2, diepte 3) Ah, thank you for that feedback! I need wide feet friendly shoes.
[k5jhw9v] (score 2, diepte 4) Np! Same here. I have a pair of Asics I forget the model but they are wide sized and the fit is very comfortable, but my feet still get tired at the end of the day so I'm looking for other options
[k5ge3r8] (score 2, diepte 1) A tech I work with has them. She says they aren't that comfortable but they do clean up really easily.
[k5gcd5l] (score 2, diepte 0) Altra Paradigm
[k5htzfx] (score 2, diepte 1) I am flat footed and found this to work for me as well!
[k5h1ggq] (score 2, diepte 1) Really? I know vans would destroy my feet for sure
[k5hqdpp] (score 2, diepte 0) Brooks and Saucony
[k5hsy4c] (score 2, diepte 1) I love Brooks.
[k5i2sxq] (score 2, diepte 0) I like my New Balance 928s. I walked into the shoe store and said I need shoes, and the fantastic sales person brought me a bunch to try and they felt the best for my foot. They've lasted at least 2 years too, though they have lost their squish. I'm going to try to get new inserts and see if that works to renew them, otherwise I'll get another pair.

For a good shoe expect to pay $150-200. It feels steep, but it's so worth it to not have your feet (and ankles, and knees, and back...) hurt at the end of the day.
[k5id4e9] (score 2, diepte 0) I’ve been a Dansko girlie for 15 years.
[k5k4hcb] (score 2, diepte 0) I started with rockports in the early days, have seen podiatrists 2 to 3 times for stress fractures and plantar fasciitis, that involved injections and tapering feet . The taping  helped a lot. My podiatrist asked what size shoe I wear, I replied men’s 12 , to my surprise he said I should be in a 13.5 to 14 wide.  I think my foot flattened out over the years. New balance 995 have be my go to for years. When the company installed carpet tiles , the floor was to soft and I felt off balance a lot, the ankles and knees started to bother me.  I should have tried high top 995’s , but I retired instead . I miss working, but I don’t miss the constant struggle to keep up with all the bs ( you know insurance stuff ) that we are required to complete. Ps the rotation of shoes does work well…
[k5hnj1q] (score 1, diepte 2) So, crocs.
[k5g8zld] (score 1, diepte 0) Brooks Ghost are the best I’ve tried.
[k5gbsw8] (score 1, diepte 0) Anyone try those clove shoes?
[k5kk35d] (score 1, diepte 2) I actually find cloves to be too wide and I don’t have particularly narrow feet.
[k5klyeo] (score 1, diepte 3) Ooh that’s interesting. I wish they had them in a store so I could test them out. Their return policy isn’t great from what I remember.
[k5gihbs] (score 1, diepte 1) I have them and they’re amazing
[k5ge6px] (score 1, diepte 0) I bought some ASICS Nimbus 25 or something. I think they’re a bit comfier than my ultraboosts
[k5giem2] (score 1, diepte 0) Clove!! They’re made for nurses and are super comfy
[k5gjjzb] (score 1, diepte 0) Hoka Clifton 9’s are my favorite at the moment
[k5guplc] (score 1, diepte 1) the bottom of cloudmasters felt so flat for me ☹️
[k5k27ls] (score 1, diepte 1) I have some Xero shoes.  Not sure how standing in them in one spot all day would be, as I do a lot of walking in the hospital along with stand up sit down all the time, but they are virtually weightless and are very comfortable to move around in.
[k5k3r6j] (score 1, diepte 2) https://preview.redd.it/ug2o678gi6vb1.png?width=3024&format=png&auto=webp&s=66fb16b39cce1f86667dfd988a4bc312eb056ca2
[k5gmzxu] (score 1, diepte 0) I have weird feet and standing in tennis shoes all day ends up killing my back. So I wear Converse or Vans.

However I know Hoka's are really nice for a lot of people.
[k5gt0mf] (score 1, diepte 0) Hoka’s
[k5gwknp] (score 1, diepte 0) I had some Sauconys don't remember the exact style but they where the best shoes I ever had, feet never hurt even working straight 12s. I have some cloud tecs now and they aren't anywhere near as good
[k5h2cpo] (score 1, diepte 0) Hoka bondi 8+ compression socks+ shoe inserts for my flat feet
[k5ha82l] (score 1, diepte 0) Merrill's.
[k5hacr2] (score 1, diepte 0) Dansko

They are known for their clogs but they make actual shoes as well.
[k5hd5jr] (score 1, diepte 0) Proper Goodyear welted with Podiatrist prescribed orthotics. Yea, it can be $6-800 dollars/pair initially, but they can be resoled.
[k5hkqqo] (score 1, diepte 0) OrthoComfoot Comfortable Orthopedic Mens Slip On Loafers, Arch Support Boat Shoes for Extra Cushioning and Pain Relief, Canvas Breathable Plantar Fasciitis Walking Shoes https://a.co/d/50HEvue

Bought a pair earlier in the week and just bought two more. Real comfortable
[k5hqwvo] (score 1, diepte 0) Taos tennis shoes
[k5hsbui] (score 1, diepte 0) Z coil
[k5i21xt] (score 1, diepte 0) 40 years ago, I saw many RPh wear Rockport, I have been wearing them since.
[k5ie6j5] (score 1, diepte 1) I have 3 pairs of new balance 626 that I rotate through
[k5i6868] (score 1, diepte 0) I went to Fleet Feet, where they put you on a machine that maps your foot. From there I found out I have a very high instep (I had no idea) and Brooks would be a good shoe for me. They were right!  I recommend them highly.
[k5iclfa] (score 1, diepte 0) Anything from OrthoFeet. I bought a pair about 2 months ago and have had zero leg or foot issues since
[k5u1d8n] (score 1, diepte 1) I have bunions and wear Brooks Adrenaline in a wide size.  There's not many color options which stinks, but they are roomy enough
[k5ii1y0] (score 1, diepte 0) So I used to be a die hard ASICS gal. Up until I was starting to realize my feet ached so bad after my constant 12 hour shift… and my shoes couldn’t handle those shifts lmao..
So I switched over to hoka Clifton’s..honestly I find the Clifton’s more comfy vs the bondi
[k5iwpqw] (score 1, diepte 0) White Crocs
[k5j1sdc] (score 1, diepte 0) On cloud! 100% worth it
[k5j98tp] (score 1, diepte 0) Not shoes, but make sure you’re also wearing compression socks
[k5jf271] (score 1, diepte 0) [Gravity Defyer's Mighty Walk](https://www.gravitydefyer.com/tb9024fwp-womens-mightywalk-athletic-shoes-white-purple) were my go to along with compressions socks.
[k5jqac1] (score 1, diepte 0) Doc Marten's are my go-to. They last forever and my feet never have any pain when I work in them.
 They have so many styles to look dressy, funky,  punk/ grunge, and everywhere in between. Even have non-slip options. Plus, you can never go wrong with a good pair of leather shoes!
[k5pr6wn] (score 1, diepte 1) Agree rotating is a must I also rotate my ASICS with low cut boots 🥾 helps with fatigue 
Curious as to how you went about retiring did you cut hours or just walked away?
[k5kgwyo] (score 1, diepte 0) Regarding the back on fire , I used to place the a old ice pack that shipped with the vaccines, behind ; my belt at center of my back  at work ,  that would relieve the discomfort. we would keep the packs frozen in freezer.
[k5mgid9] (score 1, diepte 0) I am rotating between ASICS and cole haan right now. Rotating shoes seems to help
[k5gke8k] (score 0, diepte 0) ON Cloudmonster

