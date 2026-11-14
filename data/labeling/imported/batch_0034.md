# Label-batch batch_0034

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
Schrijf het resultaat naar `batch_0034.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1tuora8, 1xes6ai, 2yc9mk, 1i1azlm).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1tuora8 ===
SUBREDDIT: r/WorkBoots
DATUM: 2026-06-02  SCORE: 24  REACTIES: 0
TITEL: Jim Green barefoot African ranger composite safety toe
POST (source_id=post):
Had these boots for about 6 months and here’s my opinion on them. First by far the most comfortable safety toe boots I’ve worn, Red Wing CRV (discontinued) were a little more comfortable but much hotter with the synthetic lining. These are double lasted full grain leather outside with a yellow calf skin lining inside, 360° double down stitched with a veg tan leather midsole. They do not have an insole which I need support (lifting copper all day) so I use Sole Wide insoles giving me a little arch support and they fit the wider toe box perfectly. 

The first set of pics are next to red wing #2446 Chelsea’s in 10.5 EE and the other is next to red wing #2216 logger max in 10 EE. These things are very well built and at a very reasonable price $240ish so if you need safety toe and tried of the toecap squishing your toes and/or want zero drop safety boots these are your answers. 

On the brannock device I’m a 10.5 EE-EEE I got size 11 (my foot measured just under 11” and size chart on jim green website said size 11 was for up to 11.02” feet) in the African they fit perfectly with my toes having just a little bit of wiggle room but not so much my forefoot slides around when exerting force! Just order their barefoot razorback hiking/outdoor boots can’t wait to try them out on my local trails.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):

=== THREAD 1xes6ai ===
SUBREDDIT: r/Frugal
DATUM: 2026-10-25  SCORE: 220  REACTIES: 429
TITEL: Ways to keep feet warm in winter for a diabetic?
POST (source_id=post):
Asking on behalf of my wife. She has diabetes and is well managed in that regard, but has incredible cold feet. Mentioned the diabetes as it may be related(?)

In the winter she enjoys wool socks, so I'm trying to help her stock up on those, but some times wool socks aren't enough. I've thought about getting her a pair of sheepskin boots like uggs as logistically that will keep her the warmest while being safe for diabetes, but she is very anti sheepskin, which is okay and I respect but it makes it a bit harder to find good shoes/foot coverings. 

She can not use anything that produces heat with a battery or what have you. Socks, of course, have to be washed after every wear and that can cause a lot of wear and tear if she's rotating a few pairs of super thick wool socks, and some times that isn't enough. 

I made her a pair of leg warmers out of a thrifted scarf, and they are fighter to her calves and ankles so she can put them under her pants legs. They are working well for fall weather, but I'm struggling to find any ideas for the winter. She does not like a lot of boot designs, and with being poor it's harder to find something high quality that also works for insulation.

Any advice? I'm thinking wool socks plus stirrup wool leg warmers,  and or a pair of thick fleece lined slippers or camp shoes for driving to work in the morning and wearing out of bed

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[19rm5559h08hx] (score 151, diepte 0) This seems like more a question for your doctor than the frugal forum.   You can find many specialized socks for persons with diabetes.  They are generally loose (don't restrict blood flow) and thick.   Perhaps more important is maintaining blood sugar control to avoid further damage.
[19rmomslr0phd] (score 139, diepte 0) I am not diabetic but also have very cold feet and the best thing for me has been reducing heat loss (if they're warm now and you put on a cold boot, you then have to expend extra energy). I know not being able to sense dangerous heat can prevent the use of direct heaters like hot water bottles, but is there any reason you can't pop a rice sock or other heated item into whatever pair of shoes she's going to wear a few minutes before leaving? On really cold days I start the morning with a hot drink anyways so throwing a couple microwaveable pads in for a minute and then leaving them in my shoes while I get dressed is cheaper and safer than a fancy shoe warmer. I'm also a big fan of tucking a heating pad under the blankets while I brush my teeth, then I can pull it out right before getting in and the feet area is pleasantly toasty. Just a thought. Also if some shoes just aren't warming up at all it may be worth considering a new lining or doubling up on socks, some thinner pairs don't insulate well...
[19rm5jmzlivb7] (score 103, diepte 0) You mentioned wear and tear on wool.  I wear wool socks year round because our office is always freezing cold even when it’s 100°F outside.  You will find that your wool socks will last much longer if you wash them in a wool safe detergent and hang them to dry.  My eldest does his own laundry (which I do appreciate) but he didn’t realize this and he was using tide.  His socks, same brand as mine, were wearing through quickly.  I told him to leave his socks to me, and now they’re lasting much longer.  Wool safe detergents cost more, but making wool last longer will save you money.

I wash wool and wool blend clothes on “cold” which is actually 30°C/85°F, gentle cycle, NO fabric softener.  I then hang dry.

Doubling up on the socks is an option, but to do that she would need to buy shoes about 1/2 to a full size up, which may or may not be worth it depending on how often she would wear them
[19rm5d68g4qo4] (score 85, diepte 1) I think that sometimes frugality has to take a back seat to health. I’d recommend going to a medical supplies and equipment to see what specialized products they sell for diabetic neuropathy.
[19rmtm8c987b5] (score 42, diepte 1) Oh!  They make boot dryers!  Like hair dryers for boots. That could be perfect!
[19rm5pwk969s5] (score 30, diepte 0) Socks AND slippers make a huge difference for me rather than socks alone. Would definitely recommend, helps even keeping the house pretty cold (55-65 degrees)
[19rm5r7s2ksn8] (score 29, diepte 2 OP) No I get that fully, she just had her 6 month Endo appt and of course it's always right at spring or the beginning of fall so we never remember. Just wanted to know if anyone had any advice
[19rmik2h43qbo] (score 27, diepte 0) You can also buy down booties (house shoes). She could wear them with her wool socks.
[19rmwu7r6iih0] (score 26, diepte 0) Is she primarily seated at work or standing? If seated I have a thought to share from something I have experienced myself.

At work the chairs we have are such that I notice my feet falling asleep/losing blood supply very easily depending on my seated position (sitting normal/straight up vs leaning to the side a bit or slouching - basically dependent on the way pressure is on my butt on the chair and the angle my knee is at that my legs come off the chair). If I change the pressure point on my butt or the angle my thighs come off the chair at my knees, fully blood flow is restored.

These are very fancy, cushioned office chairs too. But I have had to lower the chair height and get a cheapie folding Walmart footstool, in order to find the best angle for my lower body that I am not getting the restricted blood flow ‘tinglies’ multiple times per shift. So perhaps an ergonomic foam seat cushion and/or a $10 Walmart folding footstool to change the lower body pressure points or angles.

Might not be her specific problem but I thought I’d share because I hadn’t seen any comments addressing this avenue as a possible cause.
[19rmt0ckyilmr] (score 23, diepte 0) I used to work in our basement and it gets really cold down there in the winter. Even with a space heater, my feet were always cold. 

Until I found a brand of socks called Heat Holders. A pair on top of my regular socks keep my feet nice and warm. They are not inexpensive but they do last a long time so I consider them an investment. I wear a pair of loosish slippers on top because they will get holes if you walk around in them without something between them and the floor. 

For wool socks I prefer a brand called Smartwool. They can be thrown in the washing machine. They are nice and warm for normal environments. Paired with the Heat Holders your feet stay perfectly warm in even the basement. Again, they last a long time. I have pairs I’ve worn for years.
[19rm4v2nfe8zo] (score 22, diepte 0) I add hockey socks if it's cold. Despite the name, these are footless and actually work more like heavy duty leg warmers. I have seen heat reflective insoles but I haven't tried them yet
[19rm5eefe7kzl] (score 22, diepte 0) A stocking cap. If my head is toasty warm, my feet tend to stay warmer too.
[19rmjyrzm6nsx] (score 22, diepte 0) I have alpaca insoles in my shoes that add a layer & keep my feet toasty.
[19rnhhf0tf479] (score 21, diepte 0) I'm not sure how detailed of rules were given by the endo - but a family member who wasn't allowed to use devices that *continued* to generate heat was still allowed to use something like a warm rice pack. The reason was that once you take them out of the microwave, they aren't getting any hotter - so you can warm them up only so much that they are *warm - not hot! -* and check for safety with your hands, and then apply to the feet. They won't generate more heat and therefore won't hurt the feet.

Now my second suggestion is more... unconventional. I'm not diabetic, but my feet did get cold a lot at a previous office I worked in. I bought a cat cave. It's basically a cat bed that has a top cover. I can't link an example due to sub rules, but if you search for "cat cave," the one I had was round, one of the flatter ones (not the sort with a big tall dome) and it had a zipper opening that allowed me to have it very open (if I was moving around a lot that day and wanted it to be easier to move my feet in/out) or more zipped up (extra warmth!)

I basically tucked my feet into it while sitting at my desk for long periods. It's thicker than just a blanket would be, and retained heat very well. It was also just plain cushiony!
[19rm87c2w1ssi] (score 19, diepte 1) Also gotta say, OP’s wife may need to compromise on some things if cost is an issue. If this is just about making a frugal choice, whatever, but if there are serious cost limitations, frankly, OP’s lady is gonna have to be willing to compromise probably on aesthetics. Health solutions are not always fashionable. Dealing with complications is going to be significantly more expensive. I can appreciate the effort that he is putting into this, but I kind of think that they need to have a tough discussion about the options available if money is a concern.
[19rm67h1avj0j] (score 19, diepte 0) I keep a rotation of Snoozies in winter, for sleeping and walking around the house. About $12-18 USD per pair.

These are soft thick fabric slippers with grippy bottoms, plush interior and varied outer fabrics in lots of colors/patterns. The fit is a bit loose (which I prefer) but they don't fall off while walking. She could wear a thick sock and then these.

I throw them into the wash about once a week. They do tend to get holes due to the soft construction. Not sure I'd call them a frugal purchase but they are very warming.
[19rm6sz30wf0l] (score 18, diepte 0) There are plenty of slippers with outdoor soles that are still warm but aren’t made with genuine shearling. There are some Dearforms at Costco right now that are $17, for example. 

I also just want to mention that blankets work wonders if she has a desk job. Even just over her lap (obviously not around her feet) in the car will help keep her feet warm.
[19rm5jg9ncxkw] (score 17, diepte 0) If she works from home or spends time at a desk, she can put her feet on a folded blanket/towel, an old cat/dog bed, or something like that. Same principle as the homeless sleeping on top of cardboard

Not sure about the specifics of diabetes but repeatedly flexing the calves can help with blood flow in the legs as well
[19rmslbkazbph] (score 17, diepte 0) I have Raynauds and my hands and feet turn blue.  

Things I do:

Moving is important, anything you can do to improve circulation in the affected area will help.

You can get factory seconds from darn tough and smartwool wool sock makers.

I heat up my bed before I retire for the evening.

Keep your core warm, dress in layers.

L.L.Bean makes some very warm wool and shearling slippers.  Amazon has warm acrylic ones that can be washed in a machine.

Gentle foot massage will increase the blood flow in the feet. 

She can also talk with her endocrinologist about diabetic socks and compression socks.  

Wearing comfy warm socks to bed is also helpful.
[19rm5hocy4q9u] (score 15, diepte 2) If OP happens to be in the US, that is arguably far more frugal. Maybe regardless.
[19rm51sa5aq6d] (score 14, diepte 1) Bad idea for a diabetic.  The same underlying reasons for the colder foot temperature also lead to being less likely to judge temperature well, being more likely develop injuries from not well recognized temps,  being more likely to not notice those injuries when occurring, and being slow to heal.
[19rm5lzqe0emd] (score 14, diepte 2) It's possible to measure the temperature of the water with a thermometer before it goes into the hot water bottle. It won't get warmer on its own. The water will only cool down.
[19rnf74wsv0g5] (score 14, diepte 0) Diabetic here.. I use my electric heating pad to 'pre-heat' the foot of my bed at night. I turn it on under the blanket while I so my bedtime routine (15 minutes or so) and then pull it out and then it off when I get in to bed.
[19rm85b285j42] (score 13, diepte 0) You mentioned that things that generate heat by battery aren't an option, but is heat by warm water possible? I have Raynaud's and user a special warm water bottle design for under the desk. It is a hot water bottle with a thick cover that includes two pockets for the feet. This way, the hot water bottle sits on the floor (with stopper texture on this side), and you put your feet on top of it, into the pockets (as if you'd slip into a slipper, they are open at the back). If you're controlling the heat by putting in safe temperatures, could this be an option? 

I paid about 15 or 20€ for it, don't remember exactly, but it has paid off for me. 

I often use it in combination with a regular hot water bottle on my lap and a vest if my room is cold and this way my hand also stay mostly warm.
[19rm5jc1y0xl0] (score 12, diepte 2) It's possible to check the water temp before filling the hot water bottle. Once it's full of water the temperature only decreases. It won't get warmer on its own.
[19rm4zjsrbpc5] (score 12, diepte 1 OP) Nice!!! Hockey socks sound exactly like what I've been looking for
[19rm787smff2a] (score 12, diepte 2) Car heat set to blow on your feet can definitely help, it tends to be pretty directional. Work can be tricky, depends on what she's doing, but sometimes I will layer socks when I'm going out and it's cold, however many I can and still fit them in my shoes lol. If you guys do Costco, they sell packs of wool socks that stand up to constant wear
[19rm6r0vj53i8] (score 12, diepte 0) I have Reynaud’s syndrome, so I’ve spent a lot of time trying to figure this out. I don’t have an ideal method for keeping feet warm when I’m up and moving, but I’ve found the perfect thing when I’m stationary. I made rice warmers, fabric bags filled with rice that you heat in the microwave. They stay warm for an hour or two, and you can even make slippers with rice bag bottoms. They are one of the few things that work to warm up my feet once they’re chilled (the other is hot baths).
[19rmyvnzk0001] (score 12, diepte 0) Look at a pair of silk socks that go on before the wool.  They are thin and great insulators.  

Maybe a pair of silk long underwear could also work.

I wish you every success.
[19rmg8bnioi6c] (score 11, diepte 0) I have neuropathy and poor circulation as well as the diabetes so am in the same boat. I find thick woollen socks and ugg boots work well. My feet ache when they’re cold so I need the double layer. Being weird about sheep skin won’t help, Try explaining that it’s from a domesticated animal and that it’s a way of using the animal carcass from nose to tail so their life isn’t only to give meat or, for that matter, fleece, the whole animal is utilised.
[19rm4ys8yn2td] (score 10, diepte 1 OP) Sadly she isn't able to use those due to her diabetes. She has temperature regulation issues and could miss the queue to take it off when it's too hot and burn herself
[19rm5b7c6vnr6] (score 10, diepte 1) I heat a flax bag for my feet before bed. 

For someone with any type of sensory loss or neuropathy (such as is often seen in diabetes), you'd want to be careful of the temp, keeping it low warm and testing it on other body parts before use, but it doesn't run a risk of getting hotter.  

Another option, if one was especially concerned about burns with sensory loss would be to heat the foot of the bed or heat a warm towel with water bottle or flax bag, remove the bottle / bag, and put that slightly warmed material in the area of the feet, but not on the feet.
[19rm652vqgao5] (score 9, diepte 0) This is a bit random, but my feet are often cold when the rest of my body is perfectly comfortable. Does she shower every day? I find that my feet kind of “thaw out” in the shower in a way that I can’t get them to without it. If I’m tempted to skip a day (when just lazing around at home), I’ll still do a quick shower if my feet are cold.
[19rm6lc4xi2v8] (score 9, diepte 0) I actually got a gifted pair of *THICK* wool blend slipper-socks that are warm enough for walking on cold concrete cabin floors and camping in below freezing temps. But I agree they get dirty and then need to be washed. Ironically the best combo for cold feet at least while camping in cabins has been those socks plus slip on crocs - the rubber just blocks the cold floors. You can probably find thrifted crocs. 

Layering is also an option, thick wool socks with a thin liner you can wash.
[19rmbw7y7ooas] (score 9, diepte 1) Anything heated can be dangerous with neuropathy because they might not feel it burning them, and then if they get a wound it's slower and more complex to heal. I worked with a patient who sat with his cold feet in front of a radiator, got a severe burn and eventually had to get that part of his foot amputated. It's really common.
[19rmx6ag8w000] (score 9, diepte 1) I love a good rice pack.  I have a few.  We have cold packs in the freezer and hot packs to warm.  I do a hot pack when I am cold. We use a bigger sock for that and have smaller ones for other kinds of warming or cooling.
[19ro0qgd72qys] (score 9, diepte 1) I’m short and I keep a toddlers step stool under my desk to raise my feet so I can sit at the right height for the desk. And raising my feet even those 4 or 5 inches away from the cold floor really makes a difference warmth-wise. 

I also keep a small throw on my chair and put it over my legs when I get cold.
[19rm6t9fyznk4] (score 8, diepte 3) That’s literally what it’s called… diabetic neuropathy.
[19rm622cij1fk] (score 8, diepte 0) I like to match cotton socks with thick wool socks on top. Means also I can use the same wool socks longer and just wash the cotton pair, well, if I wear them at home. In shoes it is always just one time wearing. But at home the wool socks are like cozy house shoes. Also, you can mend them easily in the worn spots.
[19rm6tnc3nrwi] (score 8, diepte 1) Im so glad I read this comment.  

I LOVE Snoozies.  I wear them year round.  I wear the thin ones in summer and the fuzzy in side ones in winter.  But the holes!  I thought it was just me and that I was unnecessary hard on them.
[19rn4x6wdnpxd] (score 8, diepte 1) Unfortunately people with diabetes, neuropathy, circulation issues and other health concerns can't use heated items. It's terrible! I love my heated socks and heating pads, and am contemplating a heated foot pad at work, but if you have poor circulation you're more likely to burn yourself, and then those burns also take longer to heal. My mom is always chilly, broke her foot a few years ago and still had pain, and is T1 diabetic, so a heated foot pad would be so nice for her! But she can't use them.
[19rma41lrugw3] (score 8, diepte 0) Correct me if I'm wrong. This is a circulation issue. A perfusion issue. Would massaging her feet periodically help?
[19rnfsgi7turp] (score 8, diepte 0) Manitoban is a Canadian First Nations company that makes the warmest real fur lined slippers. I got some for my diabetic father and he loves them.
[19rm4t9ql4xl0] (score 7, diepte 0) Good old hot water bottle.
[19rm5zjv46uip] (score 7, diepte 1 OP) For diabetic people it can be more difficult to tell when a temperature is too intense and causing harm leading to burns or damage. It can be hard to ride the line of a temperature that is effective to fix cold feet, and one that is too hot and causing injury. And sometimes the temperature range overlaps
[19rm641xvrdhg] (score 7, diepte 0) Hey, Darn Tough Socks sells fully cushioned socks and fully cushioned snow boarding socks. One top of being warm the extra cushion between the floor might help. They also have a lifetime warranty so you can wear them and wash them as often as you want and if they get worn you can mail them in for a new pair. They aren’t the cheapest socks, about $30 a pair but you can literally have them “new” forever.
(364 reacties met lagere score weggelaten)

=== THREAD 2yc9mk ===
SUBREDDIT: r/Frugal
DATUM: 2015-03-08  SCORE: 867  REACTIES: 391
TITEL: Electric Bill is roughly 400.00/month for a less and 1000 sq foot apartment. Wtf?
POST (source_id=post):
I got my first bill from the first fifteen days at my new place and the amount absolutely blew me away. According to my power company (progress energy) I'm using an average of 113 kWh per day.

The house I'm in is cinderblock and was built in the 1950's and the only heating comes from three 10ft 2000 watt baseboard heaters. I know that's a horrid combination, but the house is less than a thousand sq feet and the only electricity that I'm using is for those three heaters and the fridge. I use natural lighting during the day and a single CFL lamp at night in whatever room I'm in. 

Ive got the heaters turned pretty far down, and I've cleaned them all to make sure that the airflow through the foils is unrestricted. I also replaced all the weather stripping around the exterior doors but the windows aren't really an option since they're kinda painted shut. Is there anything else I can do besides bite the bullet and nearly double my rent each month?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cp864ko] (score 525, diepte 0) Electric heat is expensive. But also get them to come out and take a new reading since you just moved in. They could still be estimating from the previous tenant.
[cp865q8] (score 336, diepte 1) that or other tenants could be wired into you, as is the case in my house....
[cp88x31] (score 314, diepte 3) And who knows who might have tapped into your lines? Figure out how to turn everything off and see if that dial keeps twirling. Do it all over again with a representative from the electric company there.
[cp86xb1] (score 212, diepte 0) Are you sure you don't have a neighbor secretly jacked into one of your outlets who's running a bitcoin mining operation or marijuana grow room?
[cp86hrp] (score 206, diepte 2 OP) I'm the only person in the house so I'm pretty sure there aren't other tenants. At least, I really hope there aren't...
[cp8dgbl] (score 194, diepte 4) I second this post.

One month, my gas bill seemed much higher than it should have been, so I turned everything gas-related off, went outside, and checked the meter. It was still spinning.

As it turned out, the neighbor's gas meter and mine had been switched.
[cp8ejmv] (score 123, diepte 5) I had an apartment in queens where my roommate, who was also paying the electric bill himself, moved out.  Shortly thereafter, I got a $450 bill from Con Ed for a refrigerator, a couple of lights, and a laptop.  It was spring time, so I didn't have an air conditioner plugged in yet.

After some going back and forth, it turned out that they had been reading the power for the office on the first floor of the building as my apartment.

The actual bill ended up being something like $38.
[cp89hd5] (score 97, diepte 3) The last time my electric company charged me $400 for one month was because it was "too cold for their meter guys to come out" so they just estimated it from the previous tenant, i.e. did not actually read the meter. Dirty bastards. Call them!
[cp86ikz] (score 96, diepte 0) 2000 watts * 3 * 24hrs = 144kWh per day. Sounds like your electric heaters are working near max capacity.

1. Electric heating is expensive. That's just the way it is.
2. I don't know how warm your apartment is or if you can adjust the output on those things. My apartment is ~60F and I wear PJs and a blanket wherever I go. If you have room to turn down the temperature, 70F -> 60F can make a *huge* difference in energy usage.
3. Make sure all your windows and doors are sealed nicely. Hold your hand ~3-4 inches from the window. If it feels cold or if you feel any draft, you should insulate the window more. You can buy plastic wrap for them, but it won't be cost effective this late in winter. It's essential a sheet of cheap plastic and some crappy tape, but they're remarkably expensive. That's more of an October thing. If your new place is a permanent home, consider investing in newer insulating windows. 

To cheaply and temporarily insulate windows and doors, you could just put packaging tape over any cracks in the windows that are drafty or hang curtains/bed sheets/any heavy sheet over the window to help block the draft.
[cp8abow] (score 77, diepte 2) Marijuana mining?
[cp8cirl] (score 65, diepte 5) But putting fake numbers to avoid the cold is fraud and theft.
[cp863za] (score 61, diepte 0) Yup electric heat. Not much you can do. Space heaters are expensive as well so I wouldn't go that route. Make sure there are no major air leaks I'm windows. I'd keep all your heaters at the same level, try to turn the temp down generally. Also go on budget billing at your utility. And make sure you're not paying for someone else's heat but if its an apartment youre probably not already.
[cp88iua] (score 53, diepte 3) Is it that your part of the house is the only part that is occupied or that you occupy the whole house? Because if you live in a multiunit house and the other units are wired into your unit, the landlord could be running the heaters to prevent pipe freezing in the empty units on your dime.
[cp89uyx] (score 53, diepte 1) Or both?
[cp8atkj] (score 53, diepte 3) Bitcoin growing.
[cp8dgvw] (score 47, diepte 8) "Just pay it and if it's wrong we'll apply it to your next bill." 

That's word for word what I was told once. I was speechless.
[cp86owv] (score 42, diepte 1 OP) If I'm reading this correctly, my house pretty much just hemorrhaging heat resulting in my heaters having to almost constantly work just to keep the temperature reasonable. 

I can adjust the output, but not the specific temperature, I'd also say I'm already around 60F in most rooms, though I'll sometimes close the bedroom door and let that room get a bit more warm.
[cp87im7] (score 37, diepte 2) http://www.energysvc.com/index.php/the-real-cost-of-heating

>So the moral of the story is “don’t heat with electric baseboard”

Basically all you can do is turn the heat down to as low as you're comfortable with (some apartments require something like 55F to prevent pipes from freezing) and insulate everything as best you can. This is one of those things that I'd nope out of when viewing an apartment, especially in a colder climate. 

I just saw in your post the windows are painted shut. That doesn't mean they're not drafty. I have the same thing in my apartment.
[cp8d37h] (score 35, diepte 7) So pay the 400 this time, and next time since we didn't do it right this time you get 200 credit? That's not right.
[cp8j6t7] (score 35, diepte 1) Not likely. For most installations, the meter and main are pretty close. Power is usually (or more easily) stolen from circuits. 

I'm an electrician, so I'd pop open the panel and use an ammeter on each wire to see what each circuit is pulling. A layman can flip each breaker and check it's effect on the meter. This would narrow down what the problem actually was.
[cp86qim] (score 33, diepte 2) It may be cheaper to move out over long run.
[cp8bqo2] (score 31, diepte 4) It's possible that the units are miswired.
[cp8frq6] (score 30, diepte 8) Where I live, we can call in and give a reading ourselves if they're using a bad estimate and they'll accept that until the next official reading.
[cp86tfn] (score 29, diepte 0) Get some plastic and seal those puppies up.   If they are painted shut they are probably pretty old and will be leaking out all kinds of heat.
[cp8g0wv] (score 27, diepte 2) I worked for a electric Utility and have done a bunch of "High Bill Appointments".

You can call your utility and they will send someone out and give you the best idea and they will give you tips and generally its free. Thats what part of my job duties.

There a ton of things that could be running but obviously as everyone posted its most likely the electric heaters. There are a lot of other things that it could be also. Does your water run too hot? If so your boiler may be not running properly, the device in it that regulates the heat has broken or is damaged and is running 24/7. This is actually pretty common for high bill tests. 

The best option is to either hire or electrician or buy/borrow a clamp on ammeter. Go to your brakers and start turning off everything and turn on each braker one at a time. If you see something on a braker that is running that high you can generally see exactly what is using all of your power. The higher then Amps the more you should check out what exactly is on that particular braker. 

Again like other ideas your usage could be estimated, especially with all the smart meter problems. Generally on your bill it would say that but every utility will differ.

Also another thing is go over to your meter at the same time every day (set an alarm) and take a picture/write down your reading. Some utilities you can check your usage online and see what you use down to the hour.
[cp8ow4h] (score 26, diepte 6) Woah. Lucky you looked into it. I was an idiot, got a $240 bill and paid it without even thinking. Lucky ConEd reimbursed me $120 after they realized their mistake.
[cp8rd3o] (score 26, diepte 5) Could also be an appliance with faulty wiring. I had this problem in one of my apartments. I turned everything off and the meter stopped spinning. Then I turned one thing on at a time. There was some problem with my microwave. I replaced it with one the same size/power and reduced my bill by $100.
[cp87f32] (score 26, diepte 2) What he says about the curtains is important. It would be cheaper to use curtains as an extra insulation over doorways and windows and LED bulbs compared to letting the heat escape through the windows.

Usually if you have at least a reasonable insulation on the windows then you need to check the ceiling. It can be easy and cheap to insulate better.

If you have 5 x 10W led bulbs you are using 0.8kWh/day during 16 hrs of lighting.
[cp873hk] (score 23, diepte 3 OP) It's only a six month lease and breaking it would be more trouble than it's worth at this point, especially since we're through the worst of the winter. If I was in a year long lease I'd absolutely be looking for other options though.
[cp8dcse] (score 23, diepte 6) I'll have one marijuana please.
[cp8ct5h] (score 22, diepte 6) It adjusts after the next actual... No fraud just an estimate until we can see the actual.
[cp86h2r] (score 20, diepte 1 OP) Heh, all the windows are painted shut so I'm not sure how much I can actually do in regards to resealing them. I'll be looking into budget billing though!
[cp87g15] (score 20, diepte 0) Get an electric blanket and heat yourself.  Get the apartment heat as close to 55 as you can deal with.
[cp88aej] (score 20, diepte 0) Just a suggestion:  Unplug all electric devices.  Go to your electric meter and see if it's still spinning/running.
[cp89crf] (score 19, diepte 5) The actual efficiency of these heaters is exactly the same. Converting electricty to heat is pretty easy. These make you feel warmer because they are closer to you, but they don't actually consume any less power per unit of heat.
[cp87qx6] (score 19, diepte 2) You could "seal" the windows  with plastic wrap.
[cp8drri] (score 19, diepte 6) You don't pay any less, you just pay at a steadier rate.  At the end of the year your total expenses are exactly the same.
[cp8nrkm] (score 19, diepte 5) They would never get me off of the phone until someone fixed that.
[cp8cpoe] (score 19, diepte 5) I knew I should've bought into weedcoin when it was at $2 a joint...er.. a bag? a seed? I don't know anyhting about marijuana.
[cp87k2g] (score 19, diepte 0) Your electric company may be estimating your usage. If the person before you cranked the heat, they will assume you are doing the same and basically over bill you for usage. Down the road your bill will start to level out and you may get free months, but if you are in a short lease it would be wise to plan ahead. Check the reading on the bill vs what the meter is reading, and also ask the supplier to NOT budget bill. 
I rented a small house (700sf) a few years back, the person before me had exotic birds and kept the house at 80+. My first bill was $500 (gas even) and after the first season I was paying $150-200/month. Needless to say I had close to $1500 in credits by the end of winter and didn't have to pay for most of the spring, summer, and fall.
[cp8iq22] (score 17, diepte 7) "I don't want to work in the cold...hey, why am I being replaced?"
[cp8833g] (score 17, diepte 1) You're taking those plastic sheets you "melt" (for lack of a better term) onto the window pane with a blow driver, right?
[cp86ser] (score 16, diepte 2) They won't make more heat for the same amount of electricity, but if you use them to only heat the air near you, and you keep the rest of your apartment cold, it could make a difference. Also, it's possible the heat from your floorboard heaters is escaping outside somehow.
[cp8v2ns] (score 16, diepte 6) How did that conversation with the neighbor go?

"How dare you stop me from stealing your electricity!"
[cp8biki] (score 16, diepte 4) Hey now reading meters in -10 degree weather is tough
Source: meter reader
[cp8fvt4] (score 16, diepte 8) It's not tragic if if the efficiencies are used to make the cost of electricity lower.

Do you also think that cars and internet are tragic and that we should still be using horses and telegrams?
[cp8dtao] (score 15, diepte 7) I know that the total was the same. but paying the same rate every month based on actual usage is far better than having a month or two spike because of estimates and having each month turn into a guessing game of how much the electric bill would be. either a cheaper month or more expensive month.
[cp88l83] (score 15, diepte 2) >"melt" (for lack of a better term)

pretty sure you mean "shrink" =D
[cp8desk] (score 15, diepte 1) As close to 55 as I can deal with?  So 70 it is.
[cp8amyj] (score 14, diepte 9) The point is, it's the same amount of energy.  If they stay warm longer after you turn them off, it's because they took longer to warm up when you turned them on.  There's no free lunch.
[cp8cge4] (score 14, diepte 5) That's why I was so glad I moved to an area with the remote read meters. I had been in an area where the reader would only come out every 2 or 3 months for an actual reading and the rest of the time the bill was estimated. Now they can just be in their car and fill out their numbers without having to get out so every month is an actual reading. I pay so much less.
[cp8c538] (score 14, diepte 2) Our house is 950sq and had all electric baseboards with the shitty dials that gave no real temp control. Our bills averaged 300 a month in the winter time.

We got blackout thermal curtains and switched to radiators and our bill dropped to 150-180 a month.
[cp893dg] (score 13, diepte 2) That's actually a safety violation that has killed scores of people.
[cp8tc2a] (score 13, diepte 5) I had a friend who moved into a place in a crappy part of town.  I was cleaning up his side yard a little when I noticed a partially buried extension cord.  I traced it back and it turns out his neighbor wired his cord through an exterior wall into a box in my friend's garage.  The guy came out in a huff once I had disconnected him.  My friend didn't even realize his neighbor had been stealing power from him. 

Edited for clarity.
[cp8c0x5] (score 13, diepte 1) They should make network-connected bitcoin miners that are glorified baseboard heaters.

EDIT: You could even receive a cut to offset your electricity usage. If someone runs with this idea, buy me a beer and make the dashboard overseeing your distributed mining system gloriously epic. I have a special place in my heart for distributed systems.
[cp8v3sz] (score 12, diepte 6) TIL what ConEd is. I have been confused by that Dylan lyric for years, as a southerner: "...but I didn't pay my ConEd bill, so the radio didn't work so well".
[cp8dg0a] (score 12, diepte 8) What? Do you want a smart grid that is connected to the internet? Next thing you will want citywide WiFi!
[cp8jo2j] (score 12, diepte 4) I tried this with my energy company. But we have digital meters so apparently they don't need someone to come read them, so when it seemed like they were over charging us when our bill shot up $60 and none of our electrical habits changed, they just kept saying the meter couldn't be wrong. I asked if they would come do an energy audit, and they said they didn't do them anymore.

So for a couple months we paid this ridiculous bill, until suddenly someone in our building moved out and our bill went back to the rate it had first been at before the jump. Since then our bill hasn't jumped again, but new tenants have taken up the vacancy that corresponded with our bill going back to a more reasonable amount.

Still not entirely sure what the hell was happening.
[cp8gblh] (score 12, diepte 1) Or flip the main breaker
[cp8c636] (score 11, diepte 4) Most of the meters in California can be read remotely. They either transmit through the wires themselves or wirelessly using GSM or proprietary equipment. 

I'm surprised this isn't more common in northern Europe

http://en.wikipedia.org/wiki/Automatic_meter_reading
[cp8ks06] (score 11, diepte 5) Here in the UK all gas and electric meters are required to be Smart meters by 2020. The rollout has already been going for some time.

edit: Source- Work for an energy company
[cp88mlw] (score 11, diepte 3) There we go! Damn, losing that hour of sleep is really kicking my ass today.
[cp8eqjn] (score 10, diepte 3) If its your first bill, it could include a deposit so that would have inflated your bill. Call them and ask if there is any kind of deposit in the bill
[cp8o4ww] (score 10, diepte 2) eli5 please?
[cp86qq9] (score 8, diepte 3) This is not true, all electric heat is 98 or 99% efficient, there is very little room for improvement. I would move because that combination sounds impossible.
[cp8vv87] (score 8, diepte 7) No, he looked around, saw me sitting there, and then visibly calmed down as he realized the situation but he still pretended it was nothing and asked me if I had seen any dogs fighting or digging (I don't remember, it was years ago) there.  I smiled at him and said nope, none that I had seen.  I didn't mention the cord, but I had coiled it up at the edge of his property.  The guy later came over to my buddies house and offered to pay him for power.  I have no idea if they worked anything out or not.  He moved a couple of years later, and this was probably 10ish years ago.  I guess I mean to say I'm old.
[cp8qbus] (score 8, diepte 5) One thing you may want to try is to turn off all of your breakers, then turn them on one at a time to identify what they power, and only leave the ones you use turned on.  Informing the neighbors/landlord optional, depending on how you think they would react.
[cp8dack] (score 8, diepte 2) This happened to us, with the extra electricity being used by our landlord's shed, where he used about twice as much electricity as we did.
[cp8h3dv] (score 8, diepte 1) This is the best advice. You should really go (if you haven't) to your local power company and see when was the last reading, have the previous payments been made, and deliver a new reading. And electric heating really is expensive. I had to do it this winter and being a poor bastard I rarely used it and still my bill skyrocketed.
[cp8raxc] (score 8, diepte 2) That wouldn't do any good if they're ripping off power after the breaker
[cp8bndo] (score 8, diepte 1) Not sure why your getting downvoted this happens a lot especially in towns with houses close togeather.
(310 reacties met lagere score weggelaten)

=== THREAD 1i1azlm ===
SUBREDDIT: r/Frugal
DATUM: 2025-01-14  SCORE: 226  REACTIES: 390
TITEL: How to keep my feet and hands warm when working from home?
POST (source_id=post):
It's winter (well my country winter is fairly mild but still) and my feet are always cold, I wear slippers with Merino wool socks (from a hike I did a few years back in the mountains) but still my feet are cold, warm showers only keep the cold away for the next 15-30 minutes.

My hands are cold as well but I do nothing special with them, just working on the computer most of the day, when in the mood I prepare some tea and keep my hands on the mug to keep warm but this too is a temporary solution.

What would you suggest I could do?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m74l0wo] (score 290, diepte 0) Toss a blanket over your legs or even just your feet.
[m74lc3h] (score 198, diepte 0) I sit under an electric blanket at home 90% of the time in winter. I am perpetually cold (not a health issue)
[m74q8bh] (score 148, diepte 1) And if it's really cold, get a heated one. Game changing. And cozy!
[m74l4cg] (score 86, diepte 0) electric heated socks. no joke. 

hand warmers - fingerless gloves so you can still type.

cozy up under an electric blanket.
[m74knga] (score 78, diepte 0) Easiest way to stay warmer is probably just to keep moving. Maybe some kind of peddling device under the desk? Or just stand up every 20 mins or so and do some jumping jacks or something
[m75bpj9] (score 76, diepte 1) My pro-tip is to sit on the heated blanket with a regular blanket on your lap! It’s so much warmer and the heat distributes more evenly!
[m74kfav] (score 68, diepte 0) Have your thyroid checked
[m74ofh6] (score 57, diepte 3) Every 30 min stand up and do some sort of physical exercise.
[m75iegb] (score 53, diepte 2) Add at cat, and it’s super life changing
[m74kmss] (score 52, diepte 0) Space heater?
[m74mikq] (score 37, diepte 1) My husband, dog and I hole up in the office with a space heater and dooe closed. Rugs, house slippers, fuzzy robes. At night, bedroom and feather duvet. Heat one room at a time if you can afford it.
[m74xchn] (score 30, diepte 1) If you've never worn them, fingerless gloves sound silly, but they do help.  My computer used to be in a much colder place and I would use them. They helped.  Didn't completely get rid of the cold, but made it a lot more bearable.
[m75ajlt] (score 30, diepte 1) Even a heating pad on your back or lap can help.  And might be a bit cheaper.
[m74sew3] (score 29, diepte 1) Heated socks are the answer.  Heated blankets are also great, but what about when you have to get up to go to the bathroom?   


I got mine from Amazon for like $50 and they've lasted 4 or 5 years now.   The batteries are rechargeable, I wear them almost every night in winter and then stick them on the charger on the morning.   I wear socks over them to help keep the heat in and to keep them clean from the dirty floors so I don't have to wash them as often.  
Every holiday season when I hear men complaining that they don't know what gift to get their partners I tell them- Heated socks.   Changed my life.
[m74khx7] (score 27, diepte 0) What are you wearing on the rest of your body? If you keep your core warm, that usually helps your extremities as well
[m74ptay] (score 27, diepte 2) Make sure your feet aren't sweaty in their coverings - damp feet stay cold. Try changing up your slippers and socks a few times a day
[m7514f7] (score 26, diepte 1) Exactly what I was going to suggest. I can be freezing my ass off under fleece blankets on the couch, but one I get up and do some chores or cooking, I’m peeling off layers of clothes.
[m74maw7] (score 26, diepte 0) I have hasimotos which means not only am I always freezing, my hands and feet are like blocks of ice. I get so cold that it feels like my bones have frozen over. For this I soak in hot water until they thaw out. 

I wear lots of layers of natural materials including wool. The most important item for me is a heated throw. It has been a life changer. I have it on on my lap right now. FYI: cats love them.

I don't want to hear about my health nor am I going to explain why I am this way despite being under an excellent doctor's care.
[m76wmju] (score 22, diepte 2) I have a heated mattress pad. It's so awesome to crawl into a warm bed st night.
[m74kojs] (score 21, diepte 1) I was also going to suggest get your health checked out.  What is temp of your place?
[m7698js] (score 21, diepte 3) But know that the cat actually hates you and is just there for the blanket...oh and feed me bitch.
[m75cnju] (score 16, diepte 3) Cold hands and feet can be indicative of Iron and or Iodine "deficiency." Deficiency does not necessarily mean so low a doctors visit would catch it.  If you are female, taking an iron supplement is very unlikely to hurt you, and may help.  Some men can have too much iron, so maybe consider more carefully.  Similarly, it is unlikely adding a supplement would be too much iodine.  Both are pretty low cost supplements.
[m74lf78] (score 16, diepte 1) This solved it for me. The tower type that blows hot air directly at me.
[m78oc6i] (score 16, diepte 1) Hot water bottle lasts hours and does the trick for me.
[m74n38x] (score 16, diepte 0) My hands are cold as I'm typing this... I feel this post in my soul. I literally am just about to set up a new foot rest I got - for ergonomic issues - but I sprung for one that says it's also heated, so fingers crossed it!
[m74yen7] (score 14, diepte 3) This. I have Reynauds and at home wear thick socks with high quality foam based sandals or flip-flops that are a few sizes too big. Feet stay warmer than they used to in thick socks n slippers. And get some fingerless gloves on.
[m74mm9i] (score 14, diepte 0) Cover your head, lots of heat escapes up top, a warm head will help regulate. Also get some gloves and cut the tips off the fingers so your hands can be covered while you type
[m74nu4w] (score 13, diepte 2 OP) it's not that cold, but rather relatively cold to regular temps, my room sits between 18-22C and has no direct sun access (I mean there's a window but it's always shadowed).
[m76z5h6] (score 11, diepte 1) Yes. I had no idea hypothyroidism was causing me to feel so cold all the time.
[m74r4xx] (score 10, diepte 0) Apply a moisturizer to your feet and hands. It’s surprising how it warms the limbs.
[m74yvk7] (score 9, diepte 4) Oh yes let's try and diagnose someone based on one small thing

Classic reddit
[m74nfsa] (score 9, diepte 1 OP) that's the odd part, the rest of the body is warmed and covered enough, I wear a base shirt with a hoodie on top, and warm jogging pants.
[m752gnh] (score 9, diepte 2) I crocheted myself some wool/alpaca fingerless gloves, but you could buy them. Helps a lot , I keep them all around the house for
[m74qs48] (score 9, diepte 1) I waa going to say the same thing about covering the head. The brain gets priority for staying warm vs appendages, so you have to do what you can to keep your head warm.
[m769k5m] (score 8, diepte 4) Ouch, this is true, she does really really REALLY like the texture of the blanket
[m74l4x2] (score 8, diepte 0) It sounds like you don't have a strong Hunter's Reaction - the thing where your blood vessels in fingers and toes adjust to the cold. You can buy rechargeable heated socks and fingerless gloves.
[m74osac] (score 8, diepte 1) I was gonna suggest this. An electric blanket and a oversized cozy fleece sweater
[m76tm08] (score 8, diepte 0) It sounds like you might have some minor circulation issues or even some anemia.  Consult with your doctor.

You could also have a heating pad on the floor and put your feet on it.  Holding a cup of hot tea is also good, and you're already doing it.

Perhaps get up and move more frequently to get the blood flowing.  It doesn't even need to be much, walking to the kitchen to get another cup of hot tea should help.
[m750leh] (score 7, diepte 4) I have POTS and this makes no sense
[m74oth6] (score 7, diepte 0) Feet- merino wool socks and sheepskin slippers

Hands- what you're already doing- hot tea:)

Body- wool/cashmere scarf, wool/layers of clothing, hoodie

Exercise breaks- walking treadmill, jumping jacks, squats etc to move your body and generate body heat.

Kotatsu table- heater under table over sheepskin rug- so dang toasty!!!
[m74q9lm] (score 7, diepte 0) You can get fingerless gloves. 

Also, make sure you're getting up an moving regularly to promote circulation.
[m758t4z] (score 6, diepte 2) My feet are always cold, too. My floors are all wood and tile. I keep a small thick rug under my feet at my desk. It helps. When it's really cold, I put a heating pad between two layers of rug under there. It's heaven.
[m750hoq] (score 6, diepte 1) There are rechargeable hand warmers now too!
[m773kdr] (score 6, diepte 2) My electric blankets come with warnings that no blankets should be placed on top of them.
[m74qmh8] (score 6, diepte 0) Layers

L.a.y.e.r.s.


You put on shirts underneath your shirt, maybe even thermal underwear beneath your pants, and these things keep you warm. If it gets too hot you can take off a layer quickly. This is how I have been doing it and it has been a wonderful, no cost way to go while still staying warm so that you don't get sick

But sometimes if you just need the place to be warmer then you need it to be warmer.
[m75ojv9] (score 5, diepte 6) Circulation issues happen for tons of reasons including several that are more common than POTS, plus we aren’t doctors and don’t have their medical history, and POTS couldn’t be diagnosed on this basis either way
[m75kqay] (score 5, diepte 2) I agree with u/Responsible_Use_2182 in that keeping one's core super warm may be the key -- I have EXACTLY the same problem as you: I work from home and in the winter my hands and feet seem permanently frozen, and it's so uncomfortable and goddamn annoying no matter what I do. Except: the one thing that seems to work for me is wearing a thick sweater, on top of a thin alpaca hoodie, on top of a standard t-shirt. When your core is super-heated beyond what you think is OK, the warmth will eventually spread to your hands and feet. Good luck!!
[m77cikw] (score 5, diepte 5) I've got one of those super slick down filled camping blankets that looks like a down coat. My younger cat loves this blanket with the intensity of a thousand suns. He just can't quit snuggling with it.
[m74otca] (score 5, diepte 1 OP) i think Hunter's reaction is something from the north there was no use for it for my ancestors, they always lived in deserts and arid environments.
[m76bkuh] (score 5, diepte 2) Can also damage the wires in the electric blanket, be careful and double check the papers that came with it.
[m75d7v9] (score 5, diepte 1) Yes! I often just curl one around my feet while at my desk

Then when I’m relaxing on the couch I usually put a normal blanket over the heated blanket to stay extra cozy
[m755g80] (score 5, diepte 1) Came here to say this. My feet are so cold at times it hurts. 

Get a full thyroid panel from your doctor!
[m75i41q] (score 5, diepte 1) I feel you. I had a radical thyroidectomy (cancer - that luckily didn’t metastasize to my lungs), and my metabolism relies entirely on synthetic thyroxine. 

I’ve found that layering that core REALLY helps. I wear thermal longjohns under sweats or jeans, and I always have a hoodie and/or vest and cap. Keeping your core warm allows your body the luxury of sending a more reasonable warm flow of blood to your extremities, which in turn allows your hands a feet to feel a bit warmer. 

When it gets bitter, I don and fire up the electric socks, and maybe bust open a heat pack for my hands inside my hoodie pouch.
[m7784eq] (score 5, diepte 1) I have Graves and Reynauds. Came here to say this about wool. Winters were torture until I discovered Ugg boots. Now the only thing I'll wear in the winter is real wool fleece boots and slippers. It's been a game changer for me. Bearpaw is an economical brand and you can find good deals on it, especially at Costco and TJ Maxx.
[m74nnhu] (score 5, diepte 0) Two pair of thinner socks seem warmer than one pair of thick. In the house, I wear a sock cap and a zippered hoodie as easy items to add or take off as needed.  When stationary in my recliner, lap blanket and quilt work great.  

Summer is my season, 80°-85° seems perfect to me.
[m74ntv6] (score 5, diepte 0) Do 25 jumping jacks every hour to get your circulation going.
[m74rw8g] (score 5, diepte 0) Amazon has electric heat pads you can place under the keyboard. They also have a folding heating “wall” you unfold and surround your legs.
[m752teg] (score 5, diepte 0) Lap blanket, fuzzy slippers/socks, fingerless gloves, and a long, thick bathrobe. It's my standard wfh setup.
[m74n2c0] (score 4, diepte 1) I sometimes do this, but I also wrap myself in a heated blanket. My hands get so cold when playing games.
[m75cytu] (score 4, diepte 1) I love a small space heater. I am always hot, but my feet always run cold. Game-changer.
[m74pb18] (score 4, diepte 1 OP) yeah, I am! i think it just comes down to different building and insulation standards, since for them it used to mean death and for us it just meant a bit colder than usual haha
[m753p8c] (score 3, diepte 5) But they saved that guy from CO poisoning that one time!
[m7bo4xe] (score 3, diepte 1) And iron level.
[m74o8kn] (score 3, diepte 1 OP) im trying to find a solution that isn't related to a heater as the problem is only for my hands and feet, the heater is for the really cold days and to keep the moisture out
[m75jxf5] (score 3, diepte 2) your people are here with tips [https://www.reddit.com/r/Raynauds/](https://www.reddit.com/r/Raynauds/)
[m79gc7o] (score 3, diepte 2) I got a heated floor mat for my desk at work.  It was rather industrial (it was for people who work in a shop with cold concrete floors), but it kept my feet very comfortable in a way space heaters could not.  I also got USB heated gloves.  But once my feet were warm, my hands usually were too. 

I tried every combination of shoes, socks, blankets, etc.  But what I needed was heat in the one specific place.  It also uses a lot less electricity than a space heater.
[m79f349] (score 3, diepte 2) Depends on your situation. I would rather pay about 30 cents in electricity to heat up my home office vs paying 2 dollars worth of natural gas to do the same via the central HVAC (running it on higher temp than needed). The rates are per day. Two bucks a day for the whole month would add up quickly to the electric/gas bill in the winter.

My home office is on the first level of my townhouse, I just divert most of the heat to the 2nd (living room + kitchen) and 3rd level (all the bedrooms).

When it comes to heat, you still need some kind of external source. It's just physics. There aren't many frugal options if your body is not generating enough to keep itself warm.
[m75bjbj] (score 3, diepte 2) Can I please ask what brand your heated socks are?
[m76bh9g] (score 3, diepte 3) I just looked in my past orders and the ones I have aren't being sold anymore,  but it looks like there's lots of similar ones.   Mine are a rechargeable battery pack but the ones that take AAs are cheaper- if you buy rechargeable AAs it might be the same thing just with an extra step.
[m75rflk] (score 3, diepte 2) Winter is not particularly cold where I live in Australia, BUT I’m a stickler for fresh air so I can have windows open when working from home. Fingerless gloves all the way. Last winter I also got a fleecy oodie (knock off brand) and it was a game changer for me
[m74m7nx] (score 3, diepte 0) Wear a winter hat and a scarf or neck gator.  
Source: enjoyed living in the rocky mountains for 20 years.
[m767l8r] (score 3, diepte 2) Purchase what is available and what you can afford. 

I bought mine on sale at Costco.
[m74ob7w] (score 3, diepte 0) Had this problem too! I got an electrical blanket from Costco that I drape over the back of my seat and shoulders like a cape. I cross my legs and it feels like I’m sitting in a cozy cave / volcano.
[m74rgu1] (score 3, diepte 0) Get checked for Reynauds.
[m75267q] (score 3, diepte 0) I do a couple things:

Use a treadmill desk intermittently 

I have an electric warmng coffee cup.  After I finish coffee, i will use it for herbal tea or even just hot water, to hold as needed

Shearling lined (real wool, not synthetic) lined slippers or boots
[m758i9j] (score 3, diepte 0) Two pair of socks. Cherry stone pillow.
[m76y9fl] (score 3, diepte 0) Get yourself a mini stepper and step on it for a few minutes every hour. The harder you go, the warmer you get. Hands and feet included.
[m772sq1] (score 3, diepte 0) I wear Ugg slippers I’ve had since before Covid was a thing and use a heated throw purchased on a prime day several years ago. I know Uggs are pricey but since I only wear them in the house, they are still in great shape and super warm. 

Husband bought me a rechargeable hand warmer which is awesome. I have RA and heat tends to soothe them. Great for cold too though.
[m7db98a] (score 3, diepte 0) Put a hat on.  
We lose most of our heat through our heads. 🧢
[m766uy2] (score 2, diepte 4) This after I eat breakfast I stand in place & walk for about 10 mins. Throughout day, I will stand stretch, heck I even started doing squats while waiting. I have the walking pad, my coordination is not there yet to stand walk that & work lol. I will jump on it during lunch.  I have found that moving gets my blood flowing warming me up.
(320 reacties met lagere score weggelaten)

