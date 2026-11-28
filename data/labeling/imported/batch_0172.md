# Label-batch batch_0172

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
Schrijf het resultaat naar `batch_0172.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: pfnjcd, 1mzbftg).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD pfnjcd ===
SUBREDDIT: r/BarefootRunning
DATUM: 2021-09-01  SCORE: 14  REACTIES: 57
TITEL: Has anyone gone back to cushioned shoes after wearing barefoot shoes for a while???
POST (source_id=post):
So I’ve been wearing barefoot shoes, vans with the insoles ripped out, and Shamma Sandals for the better half of 2 years. This Sunday, I went somewhere and thought “I should wear my running shoes, since I’m going to walk a lot” HUGE MISTAKE. My feet and knees were killing me, why is this? Is it because my feet have become so accustomed to barefoot shoes that the cushioned sole actually hurt my feet? Has anyone else experienced something like this??

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[hb5q2zp] (score 23, diepte 0) I’ve been wearing minimal shoes and huaraches for most this pandemic and my legs and feet have felt great. First work convention back I decide to wear some casual sneakers that have a larger heel-toe offset (just cause they look cool) and just stood in them for 8 hours behind a booth. My heals went numb near the end of the day and my leg muscles kept seizing up. I took them off and all the pain and numbness went away. I’m never going back.
[hb6694r] (score 10, diepte 0) I can't wear "sensible" shoes anymore more. I feel like the heel is pitching me forwards and I feel so off-balance now it's just not funny.
[hb5tyjj] (score 9, diepte 0) I have been wearing barefoot shoes for the past 3 years. I wore my old pair of running shoes from three years ago to see what it felt. It was a uncomfortable experience as my feet have gotten wider and I’m not used to walking with a elavated heel. My body found the it hard to balance on tight shoes. It felt like I lost stability. I don’t think I will ever go back. My feet used to be flat, but now have arches after wearing barefoot shoes +  doing foot exercises.
[hb5qs9l] (score 8, diepte 1 OP) Wow I’m glad to see I’m not the only one. I’ve tried wearing my Doc Martins and they feel uncomfortable now :/
[hb6x7g8] (score 6, diepte 2) I’m pretty sure it’s the heal-toe offset more than anything. The next day I wore Toms, which have kinda narrow toes but relatively flat soles and I had zero problems. I’ll never understand why there are so many “performance” shoes with so much rise.
[hb76agg] (score 6, diepte 4) We’re shocked when we’re told of ancient foot binding practices but we really haven’t changed.
[hb5m4cu] (score 3, diepte 0) I got some nagging sesamoid inflammation, so I have to wear padded shoes when that’s really bothering me.  It definitely makes my feet sore at the end of the day, though, even just from work.
[hb5o1a7] (score 3, diepte 1 OP) Nice I tried a pair of Birkenstock’s and thought “these things are super stiff” and the arch support bothered me lol too bad I really like how they look
[hb5wy6f] (score 3, diepte 0) I think maximal shoes tend to constrain the foots freedom of movement
[hb62lf4] (score 3, diepte 0) Now and then in social situations. Looks, conformity and presentation are very important where I live/work, but if I’m alone or just staying comfortable I’m barefoot/minimal! :) it’s all about adaptability for me
[hb9o3uc] (score 3, diepte 1) Check out the birkenstock qs 700 steel toe boot. 
There aren't many zero drop/minimalist workboots out there.
The birkenstocks and the Belleville mini-mills are the only workboots I'd recommend.
[hb5noji] (score 2, diepte 0) I've been wearing minimal footwear long enough that I don't really need to. But I still keep around a pair of Birkenstocks as I like them for driving/traveling (although I'm still breaking them in and my feet swelled like crazy after getting blistered). I also still have a pair of "dress" shoes and some Converse All-Stars. Though I haven't worn either in years.
[hb5ov2c] (score 2, diepte 0) I have a few pair, but most casual shoes are minimal/barefoot. I still run in my Altra Superiors, but I think I might be strong enough to switch to barefoot running shoes in a few months. A little bit of cushion under your feet is quite nice from time to time.
[hb6y4up] (score 2, diepte 3) Height is desirable in this culture.
[hb5tivr] (score 2, diepte 0) Gotta say I still find regular shoes more comfortable, but I haven't tried adapting to fulltime minimal either. Only for runs and workouts.
[hban3w8] (score 2, diepte 2) YouTube has a lot of good resources. Just be a little discerning.  I don't have flat feet myself so can't advice anything specific, sorry. /R/FootFunction has advice as well.
[hb6xv9g] (score 2, diepte 0) Does anyone recommend any shoes for when a job requires work boots?
[hb88cvt] (score 2, diepte 1) It depends on why you’re wearing work boots to be honest, and what you need to gain. Does it need to look like everyone else or do they need to actually protect you with a steel toe kind of thing?
[hb9hc0c] (score 2, diepte 3) Depending on the size of the nails, the sole of the tactical research mini-mil might get the job done. Please do your own research on the boot properties, I’m absolutely not an expert on shoe materials.
[hb5sex4] (score 1, diepte 2) Well it's cork so it's quite stiff and the footbed is comfortable once broken in. But it's very different from minimal footwear and my swollen feet seem to have confirmed that. But I am keeping them as I do like the look of them. I've found some other minimal sandals that have Z-straps or other straps that go over the foot rather than have toe posts, so that's a plus.
[hban247] (score 1, diepte 5) Eh foot binding is a thousand times worse. They literally broke the bones then forced young children to walk on the broken bones to further damage the feet. 

What we do now is more like stretching earlobes for gauges or using rings to stretch the neck. Which, admittedly, plenty of people are repulsed by - failing to notice the hypocrisy on their feet.
[hbagfmq] (score 1, diepte 4) Isn't that weird? How do we actually get that idea in our heads growing up? 

Getting few more centimeters (Total height :D ) was a serious issue for 18yo me.
[hbaml4c] (score 1, diepte 5) Height makes sense - because there is a relationship between resources and height. Not the only thing, but to be tall you have to have good food and a reasonably healthy upbringing. 

What I don't get is when we start fetishizing people who are dangerously unhealthy. Like it used to be fashionable to look like a heroin addict. Wtf?
[hbmq6uk] (score 1, diepte 3) Shoe manufacturer marketing convinced runners they needed to cushion their heels or they'd get injured in about the late 70's or early 80's.
[hb8yb0f] (score 1, diepte 1) Where did you find foot exercises to get arches? I’m flat footed
[hbzy9el] (score 1, diepte 2) Sorry for the late reply, r/footfunction
And this is the direct link to the video recommended by footfunction. https://youtu.be/2OOJ9AQ1AEg.  I did the toe splay and arch cramping exercise. I was also flat footed as told by my podiatrist and had custom insoles as well. I hope this helps!
[hbzyalr] (score 1, diepte 3) Here's a sneak peek of /r/FootFunction using the [top posts](https://np.reddit.com/r/FootFunction/top/?sort=top&t=all) of all time!

\#1: [Happy New Year! Is 2021 the year to begin improving your feet? It takes time to create change, but the results can be very rewarding. It's always AMA around here, but maybe this comparison will get you thinking about something new.](https://i.imgur.com/xOJfBXI.jpg) | [48 comments](https://np.reddit.com/r/FootFunction/comments/kogf6n/happy_new_year_is_2021_the_year_to_begin/)  
\#2: [Anyone else going loincloth with their minimalist foot function-focused setup?](https://i.redd.it/hh1xthbn45x61.png) | [8 comments](https://np.reddit.com/r/FootFunction/comments/n4ykow/anyone_else_going_loincloth_with_their_minimalist/)  
\#3: [Knights... Zero drop and flexible, who knew?](https://i.redd.it/pixsd05xefj61.gif) | [5 comments](https://np.reddit.com/r/FootFunction/comments/lripe4/knights_zero_drop_and_flexible_who_knew/)

----
^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| [^^Contact ^^me](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| [^^Info](https://np.reddit.com/r/sneakpeekbot/) ^^| [^^Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/o8wk1r/blacklist_ix/)
[hb67jy2] (score 1, diepte 1) I get all sorts of weird foot pains in cushioney shoes, even before I started buying/using minimal/barefoot ones. My feet are shaped like a duck's flipper (not webbed though!) so it's always that skinny, toebox that gets me. Not to mention all the weird arch support and other such shapes they tend to have, causes my foot to feel squished and weird by the end of the day!
[hb687z0] (score 1, diepte 2) The problem is maximal shoes are very constrictive. I personally wear some sandals these days. They still have a thick rubber sole, but they allow the top of my foot to have some breathing room, and my toes. I hate the feeling of sticking my foot in a maximal shoe and it feels like I've just lodged it in a thick pool of mud, cant get it out.
[hb6ad5j] (score 1, diepte 1) I wear Softstar shoes. I bought some in black and dark brown for business trips. But I need to get my business slacks hemmed as they’re too long in the leg.
[hb6amr9] (score 1, diepte 0) I am wearing my old nikes for "dirty work" bc I dont have "old" barefoot shoes yet (just went completely minimal 2 years ago) but I try and not walk too much in them bc I get hurting knees and toes from wearing them long amounts of time.
[hb6ao7m] (score 1, diepte 0) I attempted it a few times and the struggle was similar. The main thing for me was that my posture felt off from the elevated heels.

Similarly, my feet would feel fine at first but would start to ache after maybe 30 minutes or so of standing. By the end of the day I was eager to throw the shoes off. I had forgotten about that feeling!
[hb6b5b9] (score 1, diepte 0) It probably is due to changing your gait. I’ve noticed that even between vapor gloves and lems my gait changes slightly. 

I wear more standard footwear for different things and it’s always the pinky toe not having space that bothers me but I generally don’t have issues with my knees/hips
[hb6h0q6] (score 1, diepte 0) A few months back I found an unused pair of Altra and since I had to run roads because of the weather anyway (too dangerous on trails) I decided I might as well wear them up. (Maybe surprisingly) wasn't an issue at all, but then they had zero heel drop. I had originally got them because of an article on Zach Bitter's blog about his "shoe quiver" - he tends to mix barefoot, low cushion and with-cushion training.
[hb6idof] (score 1, diepte 0) A few years ago I wore some very cute “flats” (minimal heel drop but still a drop) with a narrow toe box on a date with my husband and ended up taking them off halfway through walking around downtown because my hips started to hurt. It’s misery! I used to have a LOT of realllly $$$ shoes and ended up consigning them all and now just wear my minimalist shoes (and soft bed Birkenstock’s which don’t bug my feet/hips).
[hb6ixpw] (score 1, diepte 0) I live on a rocky road. I normally run in vapor gloves but also have altra lone peak 5's. 

It's more worth while to get some small stone induced foot pain than it is to deal with how my feet and  legs feel after running in the smooshy shoes. 

So I'm going to look into Xero's for my more protective shoes.
[hb6wd0y] (score 1, diepte 1) I'm on my second day of wearing my lone peak 5 and I am a little bit taken aback by how high the arch support is. It's not bad but it's quite a difference from my Lems.

I guess I'll get used to it in a few weeks
[hb7573l] (score 1, diepte 2) Honestly I just wear them when my feet are too beat up. 

Xero has some shoes that look like the old Merrell trail gloves before they started trying to get in on the Nike market. 

The Altras are so much cushion I get blisters for I'm not sure why.
[hb6jcaw] (score 1, diepte 0) So I spent about a year, year and half transitioning and then fully committing to running in Luna sandals. I would wear normal but minimal support shoes after that.

After about a year of fully running with them I started upping my mileage and had noticed some pretty intense fatigue with my sandals past 12-14 miles. So I slowly and ultimately switched back to normal shoes. 

Tbh I have no issues. I love running in normal shoes now because I feel I have much better form etc. I still run some runs in sandals. Just my experience but never had an issue.
[hb6n1vv] (score 1, diepte 0) I unfortunately have had to. At least for the time being. Every pair of shoes i had was minimalist, out at least zero drop (one pair of altras). Then i got an Achilles overuse injury and the doctor basically told me it wouldn't heal if I didn't get some shoes with heel lift. So now I'm in some topo athletics for the next few months. I hate them - even though they're wide and my foot has room, I'll sneak a little walk with some Vffs and everything feels better until two hours later. Such is my life
[hbaqpyo] (score 1, diepte 1) Did your doctor give you any reasoning behind his diagnosis and instruction? Why would heel lift cure the problem?
[hbaui85] (score 1, diepte 2) Less strain on the Achilles’ tendon due to less stretch in the area.
[hbavcxq] (score 1, diepte 3) Exactly. Basically i need to use it less, lifting it will require less work from it with each step.
[hb6plxq] (score 1, diepte 0) I only recently started wearing barefoot shoes or walk unshod. I've got my calves overloaded and some pain throughout my feet. So I put my cushioned running shoes for a short walk for groceries. In ten minutes I've got awful crams in calves and limped back home. One of my knees started aching too. I suppose it is due to high heel-to-toe drop making calves permanently fixed in a shortened state. I changed  these shoes to a soft but zero drop (or something close, I'm not sure exactly) ones (casual Crocs loafers). These were both comfy to my feet and easy to my calves.

I like to use these shoes to give my legs rest. So maybe it was some specific property of your running shoes giving you knee and feet pain: heel drop, narrow toe box, arch support, pronation correction inserts (these can be very awful if chosen wrong even if you never walked in barefoot shoes).
[hb6rud4] (score 1, diepte 0) I wear chuck Taylors to work when I have to go into the office. Not exactly typical cushioned shoes, but something of a compromise.
[hb6sy4g] (score 1, diepte 0) I have switched over to using Altras for trail running. Previously used Xero shoes and still do for everything not on trails. While running on trails I would always need to slow way down in rockier/technical terrain. So I had wanted to move to something that would provide a bit more protection without having to worry as much. So far I'm very happy with my decision.
[hb8w9y8] (score 1, diepte 2) Well I’m thinking it has to look like I’m wearing boots for sure. But also have some sort of protection for stepping on nails, etc... I’ve been looking and I’m not sure there is a minimal, wide toe box boot that has protection from nails.
[hb9saqj] (score 1, diepte 2) Much appreciated!
[hb6y2hy] (score 1, diepte 0) Try walking with crutches.  It's uncomfortable and awkward as hell.

Mainstream shoes are like crutches -  they're designed to fix a problem. Grow up using crutches and it'll seem normal. All you know.

Learn how to walk without crutches, though, and going back is painful and awkward as hell.
[hb71c3d] (score 1, diepte 0) I did buy a pair of runners with some stack, but also neutral and with wide toe box (altra escalante 2.5) 

they don't hurt me but i don't use them all the time. I figure it works different parts of my foot
[hb7931n] (score 1, diepte 0) I’ve been running in minimalistic shoes for a decade but would normally wear sandals and regular type boots until recently discovering vivos boots and wore those until they fell apart. But I have always kinda preferred some kind of cushion if I was going to be walking on a hard surface all day. Currently I’ll wear Altra Escalante 2.5 and every once in a while I’ll run in them too just for something different. Walking on hard surfaces for an extended time has always hurt my heels.
[hb79r1p] (score 1, diepte 0) I tried wearing a regular dress shoe again on a whim while visiting my in-laws. Never again, I wasn't even on my feet much and had ankle pain. Plus after wearing my xero cloud sandals for so long even socks feel like foot prisons.
[hb7dnl2] (score 1, diepte 0) I still wear regular dress shoes for work, and semi-cushioned shoes from Decathlon when traveling.  But for running and gym work it's barefoot always
[hb7g0ll] (score 1, diepte 0) I can wear well made dress shoes (if they’re wide enough) with welted leather soles no problem, but anything with cushion feels terrible.
[hb7tlee] (score 1, diepte 0) I switched my 3mm? Vivo Ra2 shoes for 10mm (I think?) Lems 9to5s.  I walk up to 30miles per week on a carpet and concrete so the extra sole has been helpful.  Still zero drop and wide toe box however.  

Edit: also pick up some Topo ST-3s for road running (16mm?) and that has been a nice mental break from my vapor gloves.  

General life shoes are still vapor gloves for me.
[hbhd2uf] (score 1, diepte 0) The padding in a zero-drop shoe (eg altras) doesn't bother me much but anything with a heel-toe drop is instant pain for me. Metatarsal pain, heel pain, calf pain, hip pain. Lawd do I ever hate a heel-toe drop.
[hb6qz6e] (score 0, diepte 0) Same. I know a guy who went minimalist and then went back to cushioned shoes and he complains about injuries now. He somehow still thinks he doesn't need to go back to minimlaist, though and he talks about how he got what he needed out of minimalist which "fixed my form."

He's falling for the fallacy that form is a destination; like it's something you can just focus on for a short period of time, fix it and then you're good! I've found it should be a daily practice and you can absolutely get rusty and let bad, old habits creep back in.

=== THREAD 1mzbftg ===
SUBREDDIT: r/Frugal
DATUM: 2025-08-24  SCORE: 8  REACTIES: 57
TITEL: Running shoes that won’t break the bank?
POST (source_id=post):
I run a couple of times a week and do a long run on Saturdays. I currently wear Brooks and have had Hooka in the past. The Brooks were the better of the two and I think they lasted longer too. I’m just looking for something’s that isn’t $150. I have a pair of Brooks that I wear to work and I absolutely love them but they are pricey to say the least. Are there any decent running shoes that won’t make my knees hurt and not cost an arm and a leg? I know everyone’s experiences will be different. I’m just looking for suggestions.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nai2pro] (score 41, diepte 0) Last years model.  If the 12 is current, get the 11 (or even 10) on clearance for 40% to 60% off.

The shoes usually get marked down when the new versions comenout and stay on sale till they're gone so you have to pay attention.
[nai0pgq] (score 39, diepte 0) Asics are my go to. Can usually find a nice pair on sale for under $100.

A lot of times you can find last year's model for a whole lot cheaper (any brand). Ymmv, just keep your eyes peeled. 

Whatever you do, just remember - frugal is good, cheap might not be - buying cheap shoes can end up costing a ton in knee repair later on in life.
[nastxrp] (score 11, diepte 0) These days, it seems like a cheap running shoe is anything not over $100 lol. I usually go for an older model of Hoka Cliftons from amazon, sometimes they put the less popular colors on sale
[nai4rmm] (score 8, diepte 1) NOT AT ALL
[nai74a3] (score 7, diepte 1) I love Asics as well and have used them exclusively for decades.  Agree that it easy to find pairs on sale, especially older models. Important to know your pronation for best results, there are online tools, evidence in the wear on your current shoes, etc.

p.s. bonus IMHO is that "Asics" is an acronym for Anima sana in corpore sano", Latin for "a sound mind in a sound body."  I've found running does wonders for both body and mind.
[naie9z4] (score 7, diepte 1) Can be tough if you have a common shoe size (ithink most common is US 10 for men,  US 8 for women)

Relay Goods is good alternative if you can't find previous years shoes... it's a website that sells running shoes that were returned (but barely run in,  if at all). I think most were returns due to wrong size and have 0 miles on them.
[nai3z5h] (score 7, diepte 0) Looks for older versions of brooks, they will be cheaper than the newest models
[nai15r8] (score 6, diepte 0) Joe's New Balance (this is the outlet for new balance), they are the best in my opinion.
[naigodw] (score 6, diepte 3) I've ordered several pairs and they look and feel brand new. Fine to run in.  (Former running store employee who runs 60 mpw)
[nai81u3] (score 6, diepte 0) Brooks typically go half off in the 4Q when the new year’s model rolls out. Much like iPhone, I stay back a few generations. 🤣
[naiecxd] (score 5, diepte 1) Big no
[naie8u1] (score 3, diepte 1) I I agree with ASICS. Personally, I wear gel-Nimbus, which is in the 150 range but I’ve also had gel-contend which is in the $60 range. I have old problematic feet and I can’t wear those anymore but they’re nice shoes.
[nai2pmv] (score 3, diepte 0) Nordstrom Rack has very good deals on running shoes.  I like On Clouds a lot
[nail9io] (score 2, diepte 1) Happy to join in the Asics train. The MSRP is a bit high, but there's a deal to be had once in a while, just keep an eye on it. I am on my I don't even know...5th or 6th Nimbus. Did detour to the GT2000 model once, didn't like it. Currently on Nimbus 26, although still have my old Nimbus 17 they are still in OK shape... I believe they went rocker (similar to Hoka) for 24 but it wasn't great...25 made it good, 26 was minor improvements. There are some things I still prefer my non-rocker 17s for, but strictly for running can't beat the rockers - they are great for that running stride motion, although they get a little wobbly laterally so I would not recommend them for trail running or if you have wobbly ankles. 

The wife is on one of the cheaper models... Cumulus maybe, generally likes it. Not a runner though, mostly just for walking and everyday life.
[nakleev] (score 2, diepte 2) Nimbus is a max cushion neutral shoes while GT2000 is a lightweight stability shoe (for people who pronate while running). These shoes are polar opposites...that's probably why you didn't like it. 

Recommending a specific model (or even brand) is not super helpful without additional info from OP.
[najjl53] (score 2, diepte 2) Not really how running shoes work. More expensive running shoes a lot of times means more delicate sole to dampen the pounding and it makes them less durable.

But thinking about more expensive running shoes = less pounding on your body then it is worth it.
[narw0tr] (score 2, diepte 1) I love Asics for the ankle/Achilles tendon support. I get the oldest new pairs I can find, either online or somewhere like Shoe Carnival, for like $50/pair.
[nai27a5] (score 2, diepte 0) Brooks. Sale or used ebay/fbmp mercari
[naihxsc] (score 2, diepte 4) Good to know. Your feet chew up and spit out shoes LOL.

Timing is pretty key so deals can be had for the new ones.  100 bucks for a 140 pair of shoes is a deal in my book.  For those people with uncommon foot sizes you will see the steepest discounts usually at the end of the inventory.
[nai89kp] (score 2, diepte 1) I got a pair of those fancy Australian Chelsea boots on Sierra for like $60 two years ago! 🙌🏻
[nav7ges] (score 2, diepte 1 OP) After reading the suggestions and researching customer reviews and pricing. I decided to listen to my knees and just ordered another pair of Brooks. They are more expensive but not being in pain is priceless.
[naiq7eq] (score 1, diepte 1) Or just more shoes.

In general, you get what you pay for.

Sometimes “being frugal” means an upfront cost, so that your boots, shoes, tires, etc…. Last longer than something cheap and “disposable”.

Buy 4 pair of $50 cheap shoes over two years or buy one $160 decent pair over two years.

Only you know what you’ll do.

I spent $450 on a pair of hiking boots.

People thought I was insane!!!! 

Real nice Italian leather.

I had them resoled once at $220.

That’s $670 over the span of… get this… 11 years! And I have no idea about km’s but several hundreds into the thousands.


That’s less than a fricken Netflix subscription!

Think about it!
[nai10by] (score 1, diepte 0) I use Mercari for mine. A lot of times I will go with a “tried once, but didn’t like” pair that somebody just wants to get rid of
[nas5ult] (score 1, diepte 1) I like mine a lot. I'm a slow runner and go 2x a week, I like the max cushion since they allow me to have pain free runs.
[nai266u] (score 1, diepte 0) Woot! (Amazon discount outlet site) regularly has the good running shoes (Brooks, ON, Hoka, Asics, etc) for $60-$100. Got some Ghosts off there for $80 a few months ago, but tariffs are affecting them now as well.
[natruw4] (score 1, diepte 1) Argh. The first comment was going to be my comment. My running shop stopped having a clearance rack which was where I always shopped. I was disappointed.... but the sales person told me if I knew what I wanted they could just look up the brand and model and find what I wanted of the 'old ones' and have them shipped directly to me at the clearance price. I was pretty impressed they gave me that information. That reminds me. I need new shoes.
[nai3hlf] (score 1, diepte 0) Sierra has great deals on running shoes.
[naic61o] (score 1, diepte 0) I always get older models!
[naiesgq] (score 1, diepte 0) I just got a pair of brooks for about $80. They were just on clearance on their site.
[naigzqn] (score 1, diepte 0) Costco has hokas some times.  Usually under $100.
[naihhn2] (score 1, diepte 0) You can get brooks on Amazon for 99 dollars . Also try eBay . Sometimes people get stuck with them and sell cheaper . Brand new .
[naikygh] (score 1, diepte 0) ASICS on sale
[nailocm] (score 1, diepte 0) I look around Xmas time.  If it’s a good deal I’ll buy 2 pairs
[naimr12] (score 1, diepte 0) I got a pair of Asics on sale for like $40.  And Im still running in them 3 years later with no issues (for reference I run about 4x a week ymmv)
[naiu5np] (score 1, diepte 1) Hi, grazzhoppa50. Thanks for contributing. However, your [comment](https://www.reddit.com/r/Frugal/comments/1mzbftg/-/naip1pi/) was removed from /r/Frugal.

We are removing your post/comment because of commercial/ad-like content or it is a shopping request. This includes:

- Linking to commercial sites, defined as a site which sells products/services through a cart, subscription, or booking appointments/trips. Talking about a site or product is fine, just don't link to it.
- Requesting product suggestions such as the "cheapest" product, "best" product, or simply the best place to purchase something. Posts which generate meaningful discussion are fine but "fly-by" shopping requests will be removed.

Please see the full rules for the specifics. https://www.reddit.com/r/Frugal/about/rules/

Our sister subreddit /r/FrugalShopping does allow commercial posts if you would like to post there.

If you would like to appeal this decision, please [message the moderators by clicking this link](http://www.reddit.com/message/compose?to=%2Fr%2FFrugal&subject=Removal%20Appeal&message=Author%20would%20like%20to%20appeal%20the%20removal%20of%20their%20post%20because) within one week of this notice being posted.
[naipwnx] (score 1, diepte 0) Look at runners warehouse and eBay for the model you like and get them less expensive there. Honestly, not what you’re asking for, but for the mileage you’re doing, quality shoes are cheaper than injury and PT.  Just my opinion, of course.
[nairh10] (score 1, diepte 0) A lot of shoe brands and running stores sell shoes that have been returned at very discounted prices. Also buying the older models is good.
[naiwfm4] (score 1, diepte 0) I check the runrepeat deals page and sort by rating then scroll until I find a price I'm ok with. 

If you know what you like you can filter by toe drop, width, stack, etc. too
[najcoog] (score 1, diepte 0) I've had good luck with puma running shoes. Not as expensive as Nike and under armor but just as good quality.
[najhorv] (score 1, diepte 0) I'm a long time Brooks Ghost wearer - the fit & support is worth paying the extra for imo.
[najjoy3] (score 1, diepte 0) Saucony has good but affordable running shoes and they come in wide widths!
[nalklt0] (score 1, diepte 1) Hi, Alternative_Pay4884. Thanks for contributing. However, your [comment](https://www.reddit.com/r/Frugal/comments/1mzbftg/-/najunrp/) was removed from /r/Frugal.

We are removing your post/comment because of commercial/ad-like content or it is a shopping request. This includes:

- Linking to commercial sites, defined as a site which sells products/services through a cart, subscription, or booking appointments/trips. Talking about a site or product is fine, just don't link to it.
- Requesting product suggestions such as the "cheapest" product, "best" product, or simply the best place to purchase something. Posts which generate meaningful discussion are fine but "fly-by" shopping requests will be removed.

Please see the full rules for the specifics. https://www.reddit.com/r/Frugal/about/rules/

Our sister subreddit /r/FrugalShopping does allow commercial posts if you would like to post there.

If you would like to appeal this decision, please [message the moderators by clicking this link](http://www.reddit.com/message/compose?to=%2Fr%2FFrugal&subject=Removal%20Appeal&message=Author%20would%20like%20to%20appeal%20the%20removal%20of%20their%20post%20because) within one week of this notice being posted.
[nak733l] (score 1, diepte 0) I love Brookes as well and if you don't mind second hand, check out services like Vinted (if they have that in the US). I got a pair for £20 and basically brand new
[nak9ftt] (score 1, diepte 0) I've had good luck with Asics. They usually go on sale for under $100 and still give decent support for regular runs
[nakgtwc] (score 1, diepte 0) As someone who runs 5 days a week, I just figure I'm going to be spending $250-350/year on shoes. 

I buy the brands I like when they're on sale. $100 for a pair of shoes is a good price these days, sometimes I luck out and find some unpopular color in my size for \~$75. If you want a deal, you can't be picky on color.

REI garage (gently used) often has good brands for quite cheap, but it's very hit or miss. If you know exactly what size and style you want, you can sometimes find deals on Amazon.

Running shoe stores can often be another good place to find deals, if you have any local. It feels like every time I stop in at my store there's a stack of discontinued shoes somewhere in the store that have been marked down. If not, you can ask - they might say no and tell you when their next sale will be, or they may disappear into the back and come back with a discontinued color at a discount. 

About half of my running shoes were picked up from local running stores at a 30+% discount. The other half have come from Amazon, REI, Zappos, and 6pm. imo stay away from running shoes at most department stores and DSW, those are fashion shoes more than actual running shoes.
[nakkzub] (score 1, diepte 0) I get Brooks Ghost last year’s model. Each year I buy 2 pairs. Usually between $89-109 depending on color. I couldn’t care less about the color, so this helps.
[nal5ao4] (score 1, diepte 0) Just got my brooks for a great deal $109 for ghost max 2 and $99 for ghost since the new models came out. The site has 90 day free returns so it’s low risk if they don’t work for you.
[nalo601] (score 1, diepte 0) I love Brooks but agree they are too expensive, I go to Marshall’s and Ross and I can usually find them for $60-$80
[nalz1he] (score 1, diepte 0) Amazon has a sale on Brooks Ghost right now. I got a pair for a little over $90, but I don't know if that's a great deal.
[nalzizg] (score 1, diepte 0) bought MANY pairs of high level running/trail/hiking shoes over the years on ebay too!

most open box returns, the balance very gently used (peruse listing's pics and use your judgement....sole wear is most telling).

over 25 purchases only one seemed counterfeit....ebay refunded fully and seller let me keep the shoes.

REI co-op stores have a return resale section offering quality shoes at substantial savings.
[nasdjpn] (score 1, diepte 1) What do you mean running shoes are total bullshit? Sauconys shoes are running shoes. Would you buy noname Walmart brand running shoes for $15 then?
[nanj4e3] (score 1, diepte 0) If you know the exact sizes and models of running shoes that you like, search Ebay and secondhand clothing retailers for them. You may be able to get the high-end shoes for much lower prices if someone else bought them for a new years resolution then gave up.
[nanw4a9] (score 1, diepte 0) Buy Brooks “new in box“ from eBay. Save at least $50.

If you are going to run in them then do invest in not getting foot injuries.
[naotuz0] (score 1, diepte 0) For Brooks specifically, I always get them at Brooks Restart.  
  
IIRC when they get returns from their main brooks website, they inspect them and if they are perfectly fine but returned for wrong size etc, they'll put them on the re-sale website for a lot less. It's how I always get the Adrenelines for less than 100 bucks.  
  
The downsides are of course for your size (I wear a common size myself but if you're say a 14 wide good luck) and color (more limited to what they got in stock), but they're always so much cheaper than brand new.
[nap87z8] (score 1, diepte 0) I got some Hookas on Facebook market place for $38. They were basically brand new.
[napxcg7] (score 1, diepte 0) Are the Skechers Max Cushioning (Hoka clone) good? They're not crazy cheap so maybe they're very high quality.
[nas9qks] (score 1, diepte 0) The problem with shoe recommendations is that every foot is different so what's good for other people most likely won't be great for you. The only way to know is to try shoes first at a store, then look online for the same model. Even if 100% of people here recommend the same shoe, there's zero guarantees it will fit your foot and be good for you. Shoes are probably the one thing not to be frugal about because it can lead to discomfort and injuries that will have a cascading effect on your health and life if you don't choose carefully.
[nauhmqf] (score 1, diepte 0) Stay with Brooks, take care of your feet
[naxexxu] (score 1, diepte 0) I always check Ross first for shoes.
[nb65g4q] (score 1, diepte 0) I found a pair of Brooks for around $40 at Nordstrom Rack. If you live near one, it may be worth taking a look. If not, there is a website.
[nc3su4c] (score 1, diepte 0) See if your work place covers fitness stuff. I got my pair of $180 adidas running shoes for free.
[nai7sm0] (score 0, diepte 2) That is incredible and I will now be plastering that shit all over my desk lol
[nai1637] (score 0, diepte 0) Are sketchers running shoes any good?
[naifn5x] (score 0, diepte 2) I wouldn't do this for running shoes but would absolutely would do this for casual shoes.  Great tip - thanks!
[naia0ba] (score 0, diepte 0) Good shoes are worth it because your body is worth it. I love ASICS. Hoka wore out too quickly for me. Have heard nothing but good things from people wearing Brooks.

I try to buy new while trying to find last year's models on clearance.

If your local athletics shoe store has a frequent buyer program, it might be worth it between rebates and discounts.

At my peak, I was running quite a bit (120-200 miles a month) and buying new shoes every month.
[naicv0f] (score 0, diepte 0) Brooks are the best. They're worth the price for high quality, long lasting shoes. Beats buying shoes that are cheap and may break down faster.

That said, I found my pair of Brooks in a thrift store for $5. They looked new, maybe worn just a couple of times. Cleaned them up. But, if they fell apart,  I'd happily pay $150 for a brand new pair...I have a bad back  and knees, and these shoes are the most comfortable I've ever worn...less pain.

Skechers are also a great brand. Almost as comfortable as Brooks.. Cheaper too...can get them from Costco. Had a pair last 2 years, got another pair, and still wear them almost daily (for walking the dog, and quick trips out) since 2020.  The Brooks are for day trips and knowing I'll be on my feet longer.
[nam8nm1] (score -2, diepte 0) Running shoes are total bullshit … I’ve ran for 35 years … short runs - long runs - really long runs - ultras …

I exclusively use the Sauconys that are a year out of production and hover around $45

Anyone who says anything about them I’m happy to show my mileage versus theirs because I always win … always

