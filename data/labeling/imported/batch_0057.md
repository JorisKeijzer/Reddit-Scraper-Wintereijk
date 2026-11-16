# Label-batch batch_0057

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
Schrijf het resultaat naar `batch_0057.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 13qjwes, o8japa, 1xc7vtu).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 13qjwes ===
SUBREDDIT: r/bartenders
DATUM: 2023-05-24  SCORE: 52  REACTIES: 123
TITEL: Comfortable shoes to combat 14 hour shifts
POST (source_id=post):
Pretty boring one, but we’ve got some staff shortages just now which has led to me taking up more hours and my legs and feet are in a lot of pain. 

Was wearing a pair of adidas trainers around work but they’re just not giving me any support

We wear pretty casual clothes in work but probably looking for a decent, affordable, comfy trainers if anyone can recommend a brand?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jlf6s6v] (score 65, diepte 0) Have you tried compression socks? They've been a god send for my old legs.
[jlfh3wt] (score 42, diepte 0) I will always be a huge proponent for Doc Marten Chelsea non-slips. Yes, the first week to two weeks isn't fun as the shoe breaks in. Yes, they're a little heavier. But once you've gotten past that initial break in and adjustment, I haven't thought about tired or cramped feet in forever. 

It's like walking on air.
[jlf3671] (score 36, diepte 0) Superfeet inserts helped me a lot. Find the one that suits your arch type
[jlf7ahk] (score 27, diepte 0) Shoes are one thing. Make sure your socks are on point. No thin material.
[jlf43r3] (score 17, diepte 0) I have Skechers nonslip sole work shoes- comfortable, slip-on, and supportive. Look just like sneakers.
[jlfhtfy] (score 11, diepte 0) Try Hoka brand- expensive but they’re saving my feet on a cement floor I wish I knew about them sooner
[jlfaukp] (score 10, diepte 0) Crocs with some higher-end insoles are where it’s at. Let them feets breathe.
[jlf64rj] (score 8, diepte 0) I joined the ranks of the Dansko clan. Worth the money. Will last ages.
[jlfkad5] (score 8, diepte 1) Yes! My pair of Doc Martens combs just came in! I’m excited to get them broken in after reading this comment.
[jlfpjol] (score 8, diepte 1 OP) Was thinking of getting a pair of docs, is there any good way to break them in or is it just a case of bearing with it until they feel comfortable?
[jlf3cmf] (score 7, diepte 0) I've had some success with just going to a local surplus shop and getting combat / "tactical" boots - second hand ones work just fine too, as long as they're not already too worn out. They're designed for being worn for entire days at a time, to not rub your feet and cause blisters, to be highly durable, and to prevent slipping as much as possible.

Plus, if they're already kind of ugly, you don't need to worry about them getting dirty or scuffed.
[jlf9nek] (score 7, diepte 0) Legit the adidas non slip work shoes are a dream. I work doubles 3x a week sometimes and my feet are never crunched and I’m 350lbs.!!!
[jlfotx4] (score 7, diepte 1) Totally agree. I love all my Doc Martens, but my favourite purchase was the Chelsea non-slips I bought for work. Long, long hours on a concrete floor and you wouldn't know it at the end of the day.
[jlftms7] (score 7, diepte 2) 2nd docs. To break in I double sock or some real think socks and hit with a blow dryer to stretch out the leather. Walk around the house 10 - 20 minutes and do it again. Test it out on a day out the house before you work your first shift and bring a 2nd pair just in case they're not ready yet.
[jlfszvu] (score 6, diepte 1) These are the best ones. I second skechers as a full trade but this model is the best for your feet health.
[jlfpcj7] (score 6, diepte 2) Same. Best part is you can take the insoles out and run ‘em through dish when they get dirty.
[jlfnw1v] (score 6, diepte 2) They make a pair specifically for service workers/nurses that are nonslip!
[jlfy9sv] (score 5, diepte 1) Superfeet in some basic shoes, or better yet, whites boots with “arch ease”  albeit they cost 10x more, but work about 10x better than super feet.
[jlfiqhe] (score 5, diepte 1) Non-slip bistro crocs have been a god send for me
[jlgx50y] (score 5, diepte 1) Bar manager here. I keep trying to tell my staff that HOKAS WILL FUCKING CHANGE YOUR LIFE. I should be a brand ambassador at this point. They are very expensive for work shoes but you can work 14 hour days without foot pain. 

My first pair lasted a year. They're in rough shape but they made it. I'm about to get my second pair. I didn't know cobblers were still a thing since the 1800s but turns out there's 2 shoe repair shops in walking distance of my apartment. I'm gonna try to keep them maintained and see if I can't get more time out of them.
[jlg2tf0] (score 5, diepte 0) My move for the *really* long days in bars, is to start the day with some really supportive boots, and then when I inevitably take a break of some sort once I start getting tired (usually hour 9-10), I’ll run to my car and put on some lighter non slips. Switching shoes from heavy to light always makes me feel like I’m walking a little lighter despite my legs being a bit tired from working my ass off all day, and a bonus, the fresh pair of shoes is going to be a lot cooler on my feet.
[jlhtyry] (score 4, diepte 3 OP) Should have clarified that I’m in the UK. Never heard of this Ollie chap but I’m sure he’s lovely
[jlfw3mc] (score 3, diepte 2) Yes...these skechers...I have lupus, RA and Fibromyalgia, standing on my feet kills me...but between these...and extra Doctor Sholes insert and ankle braces (I have a bad ankle too) I can rock it all day. Now id like to go to the Good feet store. But I don't have the money ATM.
[jlfbym3] (score 3, diepte 0) I use “Fila Memory Workshift Slip Resistant” on Amazon. 

Also Dr. Scholl’s inserts. The ones I use are specifically for plantar fasciitis. The inserts have been a game changer.
[jlg00t4] (score 3, diepte 1) yep this is what I have and they're so good
[jlfxeoy] (score 3, diepte 1) Seconding Hoka! The non-slip are $175 but they’re the ones my physical therapist recommended as well
[jlpnwyy] (score 3, diepte 3) This is the way. Every other shoe is just a shoe now. You walk on clouds.
[jlfp8fv] (score 3, diepte 1) Try a pair of thick wool socks.
[jlfkw8c] (score 3, diepte 0) I usually just go to any sport/gym-shop and buy a comfortable pair of "walking-shoes".

If there is a shoe-shop with highly educated staff you can just tell them your needs and situation.

You do not want anything flat or running shoes, as flat shoes dont give good support and running shoes gives too much
[jlfkzsq] (score 3, diepte 0) If you like boots checkout redwings
[jlfpgjb] (score 3, diepte 0) They are pricey but you can find Adidas boosts or ultra boosts on GOAT or StockX for about 85 dollars sometimes and they have absolutely changed my life when it comes to body pain.
[jlfqmgb] (score 3, diepte 0) I'm a big fan of the New Balance x Shoes for crews collabs
[jlfrkjg] (score 3, diepte 0) I feel an unbelievable difference wearing my “hiking” socks. Ones marketed for long distance hiking, I like Marino wool. Seem thick but they keep my feet cool and dry and prevent rubbing and provide good cushion.
[jlgkyik] (score 3, diepte 0) What's the floor mat situation? A nice, cushy industrial foam mat under your feet really helps.
[jlgibut] (score 2, diepte 1) I agree with Skechers work shoes. I put on 40 miles/60 hours a week as a postal carrier in these. Be wary of shoes with foam soles, they are comfortable at first, but in my experience collapse within a month. You are in a break-in period right now, the pain will subside, so don’t freak out.
[jlf6p1u] (score 2, diepte 0) Altras. They are zero drop meaning theres no heel. They have a wide toe box that actually is shaped like a foot unlike 99% of shoes. They help you build strength in the feet without the normal strain caused by shoes with heels
[jlgwq7b] (score 2, diepte 2) they do their own brand of socks called doc socks, they have a lining which slips against the outer sock so you don’t get blisters. i bought a few pairs and wore those religiously and they worked a treat
[jlgb6wb] (score 2, diepte 1) I had these for a while but I have wide feet so they really cramped my toes and I had to switch to something else.
[jlfkmz3] (score 2, diepte 1) Do they have non slip tho?
[jlggolk] (score 2, diepte 1) HOKA for sure for sure! They're a little weird looking but my comfort for 13 hours on my feet trumps that

Bondi are slip resistant: [https://www.hoka.com/en/us/womens-walking/bondi-sr/192410928880.html](https://www.hoka.com/en/us/womens-walking/bondi-sr/192410928880.html)

And joining the compression sock train to say they're an absolute MUST
[jlos4v3] (score 2, diepte 2 OP) Bought a pair of Hokas yesterday. Only wore them for one shift so far but can feel the difference already, especially the support in my arch. Expensive but I’m sure they’ll be worth it. Thanks for the tip!
[jlfjloh] (score 2, diepte 0) Doesn’t matter how comfy my shoes are, I always get really sore toes, specifically by big toes. I’ve found wrapping them (just my big toes) in bandage tape works absolute wonders, coupled with some compression socks. Really makes a difference!
[jlfnl0o] (score 2, diepte 1) Hoka Bondi or Hoka Cliftons have done wonders for my feet
[jlfkc0e] (score 2, diepte 0) Skechers with good insoles like dr.scholls for work specifically
[jlfp231] (score 2, diepte 0) Compression socks and Brooks
[jlfq4x8] (score 2, diepte 0) Recently I started buying shoes, boots a 1/2 size bigger. What a relief. So when my feet get swollen it just helps them relax a bit more.
[jlggen6] (score 2, diepte 1) Saved my life while I was in the kitchen. Recently switched to FOH they’re still a dream.
[jlfrf66] (score 2, diepte 0) all about the insoles. dr scholl's work gel insoles are wonderful.
[jlfzz85] (score 2, diepte 0) Friday and saturday i always work a minimum of 12 hours and my workshoes have never failed me. Redbricks, these are amazing. They don’t look that pretty but are nice enough to pass as sneakers. They have a composite nose and special soles which don’t get penetrated. Which is a huge plus! If it is busy and glass falls i dont have to clean it that instance cause my shoes make me walk over glass. Besides that i never have sore foods nor a sore back, which i had with my previous work sneakers
[jlg2bob] (score 2, diepte 0) High quality combat boots with good inserts. Combat boots aren't made for kicking ass as much as they are for standing and marching in formation for hours
[jlgi5mk] (score 2, diepte 0) I love my pumas
[jlgo52t] (score 2, diepte 1 OP) I’m the bar manager and we’ve recently refurbished the beer garden and have became really busy. Since we’ve taken on a lot of new staff I’ve been putting myself down to work all day at the weekends so I can make sure they’re trained up in time for me to go on holiday in the summer. So it’s self inflicted me doing all these hours but it’s worth it.
[jlgsm07] (score 2, diepte 0) Not a shoe but make sure that you are stretching post shift, and I mean like a proper 5-10 minutes of (mostly leg) stretches.

I personally love calf and shin stretches after work as I feel we put a lot of pressure on those working.

One of the best purchases I've made was a Theragun for giving myself small massages after long shifts. It was an expensive upfront cost but it's most definitely been paying itself off in terms of pain relief. 

We work in an industry where many people overlook self-care (physical but also mental lol ): ) and it's unfortunate because it's an industry that also takes a big toll on your body.
[jlhyxbz] (score 2, diepte 0) Merrells. Ugly as all get out but exceedingly comfy
[jljaupt] (score 1, diepte 1) THIS. Any shoe you get is mediocre until you add an insole. I’ve been using super feet insoles for years and it’s made a HUGE difference. They last maybe a year in our industry (I push it to two) which makes the price tag worth it considering other cheap insoles last a month.
[jlh051j] (score 1, diepte 1) I'm wearing a pair right now. Can confirm these shoes are top tier.
[jmrgzdz] (score 1, diepte 1) I was recommended to get Dansko clogs by a chef I use to know. They felt like I was wearing high heels. I kept falling over. Ended up getting birkenstock clogs.
[jmu00ry] (score 1, diepte 2) Birkenstocks are also premiere comfort
[jmthruk] (score 1, diepte 1) Any specific brand?
[jlgcuv9] (score 1, diepte 2) I've seriously considered switching to the bistro pro from shoes for crews.
[jlgswaa] (score 1, diepte 1) The crocs put deep bruises on my ankles for over a week. I legit looked like I was held captive!
[jlfcdf4] (score 1, diepte 0) I found shoes on Amazon about a month ago, so I can't take about longevity as of now, but they are so comfortable and lightweight. They are also water resistant. Only paid $60 for them. Look up shoes for crews.
[jlfdeq0] (score 1, diepte 0) I do anywhere from 10-16 hour shifts. It's all about the crocs. Depending on your places rules you can get different styles and they even do a trainer type one. I wear the ballet pumps ones personally when behind bar (have steel toe boots for cellar maintenance)
[jlh31w2] (score 1, diepte 2) Looks like some folks have good suggestions. I always just suffered for it.
[jllegvl] (score 1, diepte 2) For my last pair, I stuffed newspaper into them between wears for a week or so. Plus thick socks. They broke in fairly quickly.
[jlh7d1r] (score 1, diepte 1) Just make sure to take care of the leather. Didn’t really understand and they are cracking/ripped in less the 6months.
[jlj1wb9] (score 1, diepte 2) Yeah definitely wipe them down after shift and then apply the leather conditioner they sell from time to time. Works great.
[kge7e65] (score 1, diepte 2) I'm Sold!! 

I want them for my 14 hours shifts !!!!
[jlitrt2] (score 1, diepte 1) Seconding Hoka. Designed by and for marathon runners they will save your feet.
[jliyy1o] (score 1, diepte 1) I am on the Hoka train and have been for years. If you happen to have a Nordstrom rack nearby, they have last years styles and colors right now for about 47% off their normal price. But at $80 a pair, it is such an incredible deal!
[jlfrril] (score 1, diepte 1) i gotta wrap my fourth toe on each foot to keep them from getting worn to nubs.
[jlfk30v] (score 1, diepte 0) orthodic insoles in almost any shoes will have a big impact.

If you want cheap and durable just get Crocs clogs.

If you want trainers Hoka makes great cushy shoes

I personally prefer a work boot like Doc Martens or Redwing.    They offer support for foot and ankle but if your feet get stuff you might not like them because they don't allow for much movement.
[jlfk3ht] (score 1, diepte 0) https://www.newbalance.ca/en_ca/pd/leather-928v3/MW928BK3-4E-14.html?Ecid=ps_MW928BK3_Google_PLA&ncr=true&gclid=CjwKCAjw67ajBhAVEiwA2g_jEOK-oS7LwnVf0jRRTlhbow4lQgQPVnq12YgOML-xVfif5fGSj0cyrRoC00oQAvD_BwE&gclsrc=aw.ds#dwvar_MW928V3-19761_size=14&dwvar_MW928V3-19761_style=MW928BK3&dwvar_MW928V3-19761_width=4E&pid=MW928V3-19761&quantity=1
[jlfl51z] (score 1, diepte 0) Snibbs.
[jlfrkkb] (score 1, diepte 0) Thorogood moc toe boots. Made in America with Union labor. Just got my 4 year old pair re-soled and are good as new. I work on concrete all day at my brewery job.
[jlfrl8y] (score 1, diepte 0) Thorogood moc toe boots. Made in America with Union labor. Just got my 4 year old pair re-soled and are good as new. I work on concrete all day at my brewery job.
[jlfu1mp] (score 1, diepte 0) I use dr martens and wool socks. 
Reeder Oxford*
[jlfvq2f] (score 1, diepte 0) I use Hoka shoes with super feet inserts, even after 13 hours I don’t feel anything and I have flat feet they normally kill me. They also have slip resistant Hokas which is nice
[jlfwyhz] (score 1, diepte 0) HOKA work shoe is the only answer you need.
[jlfzs6l] (score 1, diepte 0) FP insoles makes insoles for high impact activities and started out making insoles for skateboarders. I got a set of their insoles that go in the oven at low heat for 8 mins then mold to your foot when you wear them and my feet and back have never been better. I use them in Fila high top work shoes.
(47 reacties met lagere score weggelaten)

=== THREAD o8japa ===
SUBREDDIT: r/Chefit
DATUM: 2021-06-26  SCORE: 53  REACTIES: 122
TITEL: Shoes in the kitchen
POST (source_id=post):
Help!! 
What is the best shoe to wear to work that will provide support for long shifts? Crocs are not cutting it anymore and I’m standing 12+ hours with the only sitting time aloud is when your going to the bathroom my feet are killing me! I’ve tried inserts for my crocs but little to no effect.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h35k0f6] (score 79, diepte 0) I switched from crocs to birkenstocks and they suited me.

I also used to take a change of socks, (and clean underwear and usually a clean jacket) and put them on about five o clock so I was fresh for the evening. Made a big difference mentally and felt good too.
[h35a9lr] (score 41, diepte 0) You should find a new job.

12 hours and you’re only allowed to sit to take a shit?

Fuck. That.
[h35j2an] (score 41, diepte 2) What's the point of that resume experience if youre already working at a top tier restaurant? 


You're expecting to work 12 hour days if you work as a prep cook at shitty dinner, because you have to "earn your way in this industry". Sometimes that becomes a 14 hour shift because the dish guy didn't show up and you are expecting to finish up the pit before leaving.


Then you go to a mid tier restaurant and they expect you to work 12 hours, 7 days a week, and stay late to reorganize the walk-in because the health department is coming tomorrow and you are "just such a good worker."


Then you finally get the call, you have the interview you've been waiting for at the Michelin star restaurant. And you get the job! Now you work 12 hours shifts tweezing shit on to plates for people that made more $ on the interest from their savings account then you'll make in a year, of those wonderful 12 hour shifts. But hey we are family and we love our fucked up jobs..... right?


Where does it stop? When you finally save enough to start your own restaurant. And like most owners you end up practically living at the restaurant between making menus, doing schedules and ordering and paperwork and taxes and anything else that comes up daily in a restaurant. And you get to hire some young cooks and make then work 12 hour shifts so the cycle continues?


We need to unionize already if we actually want anything to change.
[h35pqll] (score 28, diepte 1 OP) That’s a great idea about changing half way!! I feel disgusting after working grill all day
[h35fzit] (score 23, diepte 0) It is not necessarily the shoes, it’s more important to have good insoles. Get your feet checked professionally to see if you need arch support. Do not rely on a machine in a drug store that is conveniently situated next to a rack of insoles do it properly. Yes it costs money but without your feet you are out of a job.
[h35x3wq] (score 19, diepte 0) Compression socks will change your life.
[h35k2k8] (score 13, diepte 3) It sounds like you have more of a problem with the structure of the hospitality industry than anything else. I work 44 hour weeks, I get paid for my time, then I go home. I'm not ragged, I get 3 days off to pursue my hobbies and other job. If I make it to Michelin, I dont care about the wealth disparity of me vs. The guest. I'm happy someone wants to pay 300$ for a 15 course I get to work on. It's challenging and rewarding to work at the top of any industry, and im cool with that. No shade on your criticisms of the industry but im not trying to reinvent the world, I admire your optimism though.
[h361gu1] (score 13, diepte 1) Birki clogs. Yeah, they cost $100 but they last me almost two years of 65+ hour weeks. Cheaper non slips I'd be lucky to get six months out of. I had the worst pain, not just in my feet, but also in my legs and back before I switched.
[h35jbxg] (score 12, diepte 4) Friendly advice: You sound like a tool, man. 

Running yourself ragged isn’t a flex, it’s sad. 

You’re being taken advantage of.
[h36huyt] (score 9, diepte 0) I was a birkies guy for years, but switched to the sketchers work shoes. Once I got used to having a shoe instead of a clog I love them.
[h35c5yh] (score 8, diepte 2) Ya ok but you’re aware there are like labor laws? And I get it I’ve done it plenty. But you can find places to work with both good cuisine AND respect for their workers.
[h35uovr] (score 8, diepte 4) I'm happy my pessimism comes off ass optimism haha. All fair points you make.
[h36re9y] (score 7, diepte 2) Birki’s clogs changed my life. Also, after working in kitchens and then transitioning to outdoor work with 80+hour weeks on rough terrain I highly recommend [Superfeet Inserts](https://www.superfeet.com/en-us/). Superfeet are a bit expensive upfront($50USD approximately) but your feet and back are invaluable. My superfeet Birki’s combo helped with having high arches(they have all types for different feet) and tremendous lower back issues. I’ve now been able to save and put a pair of proper insoles in all my shoes. Don’t trust those silly pressure machines at the local drug store like others have mentioned.
[h35ndyb] (score 6, diepte 0) Super birkis with the cork inserts are the best for me.
[h35l2w1] (score 4, diepte 5) Sorry you feel that way, but I've been at it for almost a year. I'm really not ragged. I still live an active lifestyle, see my family/friends, I even get Fridays or Saturdays off on rotation. I'm happy to be where I'm at as opposed to boring cakewalk gigs that turn 800 covers a night slinging bullshit.
[h35mjti] (score 4, diepte 6) Rotating weekends off?! That’s life changing
[h35i0pn] (score 4, diepte 1) I 100% agree. The Good Feet stores offer the best arch supports for even low arches like mine. Absolutely zero feet problems after I got them.
[h35z2ix] (score 4, diepte 1) I too recommend Birkencrocs.  Life changing.
[h35oebn] (score 3, diepte 7) A year here, yeah. 9+ years industry in total. I've gotten burnt out faster working jobs that are absent of passion, im sorry I'm not as miserable as either you are, or you want me to be 🤷‍♂️
[h35nrbm] (score 3, diepte 7) It's one day throughout the week but a Friday or a Saturday off regularly in this industry is crazy. So I'd work weds thurs, and sat sun or some other variation on that.
[h37sgxa] (score 3, diepte 4) Fyi, you're not as good a cook as you you think you are.  Taking a break and resetting your brain and body are essential to being great.  Your attitude is wrong, broken, and sad.
[h37ufjl] (score 3, diepte 4) I have all of those things plus I get matching 401(k), and I get a paid lunch break every day. Like you said yourself your restaurant just needs to staff better. No reason to not be able to go take a break midway through a shift. I’m sorry but your sucker if you think that’s acceptable.
[h35g29c] (score 3, diepte 2) If youre in fine dining, it's pretty normal. Try not to let it bog ya down, and honestly I'd flip the scenario and look at it as a great way to quit all together. The industry is already unhealthy enough to work in lol. Id definitely try out Berkenstocks if you can afford them, theyre one of the most durable kitchen shoes available and they get really comfortable after you break them in.
[h36nvmi] (score 3, diepte 1) This, plus Birki's
[h3610vt] (score 3, diepte 0) I'm a blundstone man
[h3712dl] (score 3, diepte 0) Dansco or Sanita brand shoes saved my spine.
[h371drw] (score 3, diepte 0) I'm probably an outlier but I wear Timberland pros boots. I still feel fresh after 10 hours but you'll want to replace the insole after about a year or so.
[h37n79f] (score 2, diepte 8) “I’m sorry I’m not as miserable as you are”

No one said I was miserable. Also, reread YOUR OWN comments. You don’t sound like a happy dude.
[h35uvny] (score 2, diepte 7) You’re kinda the one that sounds like a tool dude.
[h38043p] (score 2, diepte 9) I hope you're not actually being literal about that first statement because your lack of a world based perspective is showing in full colors if so. Shit conditions means different things to different people, a long day with no breaks isn't equitable to working in a third world country buddy.
[h3818z7] (score 2, diepte 6) You’re a sucker. You also seem like a pretentious douche.

Stop trying to pretend like you know what I serve in my restaurant.
[h35fibm] (score 2, diepte 0) Try out Berks, I like crocs but I have narrow feet. Berks are supposedly better for wider feet. Also helps to not lock your knees all night long, and if it helps at all I got used to the longer shifts after about a month. Not sure if you're green to that type of long day.
[h35fsiv] (score 2, diepte 1 OP) I’m used to the long shifts not used to the no break thing new job I’ve never worked in a restaurant that didn’t offer a smoke break but I guess I found the one place that doesn’t let you go sit and smoke a butt
[h35ggjb] (score 2, diepte 3 OP) Lol how did you know it’s my first real high end gig lol and you are very right about quitting but it was the only thing that let me get a break at my last job lol first step is better shoes at my new place we have these weird floors in the kitchen I’ve never seen before I’m used to the tile floors in kitchens idk if it can relate to my new foot problem. I’ll deff look into berks
[h35h5tc] (score 2, diepte 4) I've never seen a boring family style or burger bar that didn't offer at least 3 smoke breaks per shift. High end dining means 1 cook can't work 2 stations so you get no breaks. Take notes, soak in all the dish composition and ingredient choices you can. You've just started your journey to being the absolute best chef you can be, good luck man!
[h35i5qv] (score 2, diepte 2) Me too but I don’t like to recommend them directly because they are very expensive
[h366sx4] (score 2, diepte 1) Love my birkies.  But everyones different so u just gotta try until u find something that feels right
[h37ua9r] (score 2, diepte 1) The Alpro model Birkenstock is the best for the kitchen IMO
[h35yzef] (score 2, diepte 0) I’m generally a Crocs wearer but I do have a pair of non-slip boots that I’m looking to replace and one of my kitchen managers recommended her Dr. Martens. I haven’t but the bullet yet so let me know if they work for you :).
[h360rm2] (score 2, diepte 0) I’ve always been a big fan of Birkenstock, the rubber ones are really nice because you can remove the insoles and pop them through the dishwasher when they get gross - you can also get high arch insoles for them off Amazon and they’re a total game changer, they last a lot longer than the cork soles too. I had those insoles for a couple years and the shell wore out before they did, I highly recommend. 

I recently splurged on the nonslip Boston model from Birkenstock and I’m really enjoying them. It takes a couple weeks for the cork to break in but they’re getting to be super comfy now.
[h3655c4] (score 2, diepte 1) Are they the regular blundstones with the elastic side that goes up your ankle? That's a serious flex
[h367e3y] (score 2, diepte 1 OP) I’ve been looking into snibbs!!! How long did it take for the shopping process? I also like how they don’t look like chef shoes
[h3696ez] (score 2, diepte 0) I've used Shoes for Crews my whole career and have always found them comfortable, also keep a pair of regular comfortable shoes and change shoes as soon as your shift is over, this feels so good.
[h3698tr] (score 2, diepte 0) My crocs work but also recommend some compression socks.  Not sexy, but it helps with circulation tremendously
[h36qple] (score 2, diepte 0) Something I’ve learned is that socks are just as important as the shoes. Get some nice comfortable cushioned ones, not those 2 year old Hanes.
[h36x2d3] (score 2, diepte 0) I had a pair of Van's, they cost me a 100 bucks but man they're comfy. They got different styles and two different fabrics. One is pleather and other is fabric.
[h371lu7] (score 2, diepte 0) I use sketchers. Their work shoes are surprisingly good
[h38hyhy] (score 1, diepte 9) I hear a motivated, passionate person. A person who gets weekend days off and gets to spend time with the people he loves. A person who feels that their work is fulfilling. Where's the unhappiness?
[h35ljab] (score 1, diepte 5) They definitely are, but it's about opportunity for career advancement. It's a 44 hour work week with rotating weekend days off, its honestly great.
[h37tcbb] (score 1, diepte 5) Interesting assumption, but thanks. I get a couple weeks off paid, those make for some good time to mentally reset lol. I'm not sure where everyone assumed I'm working 70 hour weeks but the concern is appreciated.
[h37wm89] (score 1, diepte 6) A couple weeks off a year is pathetic, you're being abused and fooling yourself into thinking this is ok.
[h37x80j] (score 1, diepte 7) Tone back the melodrama there buddy lmao, 2-4 weeks PTO is standard across most jobs that even offer PTO, at least Stateside. Not sure where you're from.
[h380oac] (score 1, diepte 10) [Just because you're ignorant of the rest of the world doesn't mean I'm wrong](https://en.wikipedia.org/wiki/List_of_minimum_annual_leave_by_country)
[h381ebp] (score 1, diepte 11) Thanks for the link, im gonna pack my bags so I can get an extra week off in Brazil even though social mobility is non existent and crime is 40% higher. Totally better /s
[h383wm1] (score 1, diepte 12) Make whatever excuses you need to justify not taking a fucking break during a shift because you're sooo awesome and special.
[h3820b9] (score 1, diepte 7) Sheesh, sorry man. Didn't mean to offend ya, just going off my personal experiences. I'd be surprised to see a golf course serving food that keeps up with high end restaurants, so if thats the case hat's off to you.
[h38nfka] (score 1, diepte 5) Personal heaven is a bit of an overstatement lol, but at the end of the day I sleep well knowing I'm putting out food I'm very proud to make.
[h36yyf7] (score 1, diepte 2) > I mean I go through the same thing.

Why are you trying to justify an obviously garbage situation?
[h38ba1d] (score 1, diepte 4) Lol, what a brain dead response
[h35idnw] (score 1, diepte 5 OP) Thank you! It’s a game changer for my career that’s for sure! Killing it so far :)
[h35ies3] (score 1, diepte 1) When your on your feet constantly it’s worth it. They pay for themselves. Consider them an investment
[h39cro4] (score 1, diepte 1) To piggyback on top comment: Superfeet insoles last way longer than any pair of shoes I've ever had. I'm on my third pair of shoes for crews Mozo Fozas in maybe 5 years with the same green insoles I got at a running store. Also, good running shoe shops are solid places to get shoe advice whether you're a runner or not.
[h35h6oj] (score 1, diepte 0) I totally depends on how much you want to spend on your footwear. I've had dansko, birkenstocks, shoes for crews, naot. If I had extra cash to buy them again I would probably go with the naot, but if you're on a budget, shoes for crews. But if you do get shoes screws, get another pair of work insoles because the standard footbeds do not hold up very well
[h35ihqg] (score 1, diepte 1 OP) Thank you! I’ve been looking into the brand snibbs but I need to do more research they are a little pricey
[h35kcao] (score 1, diepte 2) If you have the ability to invest at least a hundred bucks in your shoes and take care of them. It will pay off at the end of the day and will you get fairly good life from them.
[h366hv4] (score 1, diepte 2) 10 out of 10 recommend
[h379fap] (score 1, diepte 1) This makes a huge huge difference.
[h38dfj5] (score 1, diepte 2) As long as they have cork, I'm 100% about the Birk. I have had back problems since middle school, and standing in those shoes for 10hrs a day has been a lifesaver. I've moved to the front of the house and I'm considering getting some of their nicer-looking shoes.
[h3604u3] (score 1, diepte 0) What's your budget? Do they have to be certified nonslip? I wear danskos but the height on the heel isn't for everyone. They also hurt my feet but they're the only shoe I've found with the support I need. I've also tried blundstones (all my coworkers wear them) and naot slipons. Both are good but don't have enough arch support for my needs.
[h366lij] (score 1, diepte 1 OP) I’m hoping to spend 100-200 max. I wouldn’t mind the extra height considering I’m only 4”11 and everyone knows kitchen are NOT short people friendly lol
[h365kq2] (score 1, diepte 2) https://www.blundstone.ca/products/blundstone-1901-dress-ankle-black?variant=32533711519823

Yeah, it's a splurge, but they are my favorites I wear them outside the kitchen also
[h365mmo] (score 1, diepte 3) Also they didn't used to be this expensive (more like $200)
[h365r7k] (score 1, diepte 3) The only shoe that's equally good with shorts or a tux. You're a chef with taste
[h368w6r] (score 1, diepte 1) If it’s good enough for Fäviken, it’s good enough for my feet.
[h387zll] (score 1, diepte 1) I was a blundstone lady for several years working regular long ass kitchen shifts, but this past year, they started to fit my feet differently and felt way too constricting! Has this ever happened to you? It was my second pair and I broke em in just fine but felt sooo betrayed after about a year of wearing
[h38m6pt] (score 1, diepte 2) My feet suffered pretty noticable swelling and daily discomfort in general, (unrelated to the shoes) but strongly related to 12-16hr days and drinking too much.  Never enough to change shoe size though

Foot pain went away with less alcohol and less standing time, still love the boots
[h363pzr] (score 1, diepte 0) I swear by my Birkenstock’s.
[h366a31] (score 1, diepte 1 OP) Vans was my number one choice but they don’t have my size in stock unfortunately I wear vans outside of work and they are the best shoes I own
[h367vbe] (score 1, diepte 2) Docs have some nonslip shoes that looked good but werent in my size at the time. I know the universal rec is birks but I wear a womens 38 in their normal clogs but the 38s were enormous,
the 37s a little too big, and 36 was wayy too small and caused me a lot of pain! Much prefer kitchen shoes with a back heel
[h3692ch] (score 1, diepte 0) Berks or non-slip Merrells for myself, but individual foot structures are also all different so this may not help much.
(42 reacties met lagere score weggelaten)

=== THREAD 1xc7vtu ===
SUBREDDIT: r/Chefit
DATUM: 2026-10-22  SCORE: 8  REACTIES: 115
TITEL: the ultimate chef question: what shoes do you prefer?
POST (source_id=post):
title says most of it. details are that i’m a prep cook working 9+ hour days and my current shoes are okay. i wear crocs, but it seems they’ve changed some designs from my first pair several years ago. the ventilation is nonexistent so my feet are getting sweaty quickly and staying wet all day (effing gross). the soles are fine and i appreciate that i can wash them out.   
here are my musts: must be able to handle 9+ hour days (8 is what i’m scheduled, 9-10 is normal obvi), and must be able to be washed. idc if insoles come out or not but i love the privilege of spraying out my shoes and letting them sit for my days off. 

bonus points for color.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[19rgrg3jyu9uq] (score 14, diepte 0) Fuck me pumps. Gets me ready for my paycheck.
[19rgx1cvdy2qr] (score 12, diepte 0) Birkenstock Tokio Supergrips - the only shoes I'll wear in kitchens
[19rhbpgzzzz39] (score 11, diepte 1) It might just be me, but I've noticed a pretty big quality difference in the birks I've bought recently versus the birks I had in the past. I've heard about them being sold to private equity and that might be a part of it. I know the old ones are basically BIFL if you get them resoled, but the newer ones seem kind of cheaply made.
[19rgsm4ebq7hf] (score 10, diepte 0) Vans Made for the Makers are-for me-the best work shoes I’ve ever had. It’s actually kinda nuts.
[19rgvjbtmagde] (score 7, diepte 0) I wear oil, slip and skid resistant, waterproof steel-toed leather work boots. 
I do not apologize.
[19rgrghyr936t] (score 6, diepte 0) Birkenstok Profi birki
[19rgw1nirwfvk] (score 6, diepte 0) Blundtstone
[19rhet5ckyd7p] (score 6, diepte 2) Not just you. The company was bought by PE in the last few years and while they have kept the same prices, they have changed manufacturing processes and no longer produce the quality they used to. 

Fuck PE companies, man. They ruin absolutely everything
[19rhcojn9rotf] (score 6, diepte 2) Think about what you're investing in. Can you put a price on foot, ankle, knee, hip, and back health? $200 is cheap, friend
[19rgrl7p1mf6r] (score 5, diepte 0) I’ve tried quite a few and the best overall isn’t the expensive ones. 

Sketchers slip ons with superfeet orange insoles. Total around $100. Last at least a year on 45 hours per week
[19rgsfu1zpb36] (score 5, diepte 0) Just got the HOKA’s, love them!
[19rgz9pxht085] (score 5, diepte 0) Danskos the last 17 years
[19rhh4hylo7z7] (score 4, diepte 3) I’m having ankle/foot/Achilles issues in no doubt to me wearing busted work shoes the last two years. It is most definitely worth it to buy proper footwear
[19rgrk5sh3azl] (score 3, diepte 1) birkenstock super birkis are the move imo, the ones with the removable cork insole. you can hose them down like crocs but they actually breathe a little better, plus the footbed molds to your feet after a week or two. only downside is they’re kinda ugly but at least they come in some colors
[19rguj3u79gmc] (score 3, diepte 1) I just started wearing these along with some Superfeet anti fatigue insoles and it’s literally the best kitchen shoe I’ve ever worn.
[19rhh27yweogy] (score 3, diepte 3) God fucking dammit dude
[19rhbmznqhl5t] (score 3, diepte 0) I personally wear keens, the slip-ons. Been rocking the same pair for about 2 years, just replacing insoles. They're still holding strong. Last 4 pairs of kitchen shoes, keens all day.
[19rhgr9u3fa04] (score 3, diepte 0) I have switched to zero drop shoes, making it very hard to find a non slip. But I have recently gone to a "barefoot" zero drop kiking shoe. They are comfy and fine on the greasy or wet floors. However, they are pricey and the kitchen floor destroys them. Worth it for the knees and back though.
[19ri28xfrq6oy] (score 3, diepte 0) Birkenstock clogs are the only shoes I’ve had that I can work 16hrs and my feet don’t hurt it’s crazy.
[19rgrau6vg9k3] (score 2, diepte 0) Sandals when I'm alone in the resturaunt.
[19rgrtph3ngpt] (score 2, diepte 2) My friend was recommending clogs, they can't be as ugly as those !
[19rhkrkvcmbfm] (score 2, diepte 2) Great... they are open back
[19rgrslqqjmn7] (score 2, diepte 0) I used to wear new balance 626 religiously, but they have since stopped making them so I am trying out different shoes. I used superbirkis for a while but my feet just don't like them anymore. I need something I can put orthotic inserts in.
[19rgshls1797n] (score 2, diepte 0) Kingston McKnight, Birkenstock, Blundstone
[19rhh5p1nvfj6] (score 2, diepte 2) Their slip resist is awful fyi
[19rhbwfi461y8] (score 2, diepte 1 OP) i couldn’t find them last time i looked :(
[19rgszgule7ol] (score 2, diepte 0) The original Sticco clogs were incredible. The tread lasted forever and you could stop on a dime. Extra wide toe box, flexible material. Those things were great.

Then they went through four different versions and have discontinued since.

Now I wear Hoka Bondi SR. They're big, ugly and expensive but my feet don't hurt at the end of the day.
[19rgv4kc6swv5] (score 2, diepte 0) I wear safety shoes I have lost all feeling in my right big toe. I think they call it hiker's foot?
[19rhur1g9na01] (score 2, diepte 2) I like Wolverine and Redwing, but Herman is not bad for the lower price. The Hermans need secondary waterproofing which is easy enough.
[19rqmpiy6k6e8] (score 2, diepte 2) I use Bates, which are used by u.s. military. Get one of their durashock lines. I like ones with side zipper for ease of on/off purposes.
[19ri84ki3ncro] (score 2, diepte 1) Same but not steel toe, red backs or thorogood
[19rjrm3m6ox28] (score 2, diepte 3) Genuinely distressing news
[19rhehq5korxd] (score 2, diepte 2) Can you justify being in pain, possible injury and not being able to work? 

It can take less than a year for severe problems to develop.
[19rgxzppkheg0] (score 2, diepte 0) Currently blundstones. Thinking about redwings
[19rgzg0363nfm] (score 2, diepte 0) I wore crocs in the kitchen for years and eventually got plantar fasciitis working FOH as a server on uneven concrete floors. I bought a pair of KURU combined with inserts and my plantar fasciitis eventually went away. They were a little pricey but I’m happy with them
[19rhdz1nmb42s] (score 2, diepte 0) Vans for Makers. Ultrarange model.   
Pricey but amazing.   
I actually bought a second pair for the gym because they are really grippy on the lifting platform.
[19rhfaksoreqt] (score 2, diepte 0) Keen slip on kitchen shoes with Sole inserts. I made the switch to this combo about t years ago and haven’t looked back.
[19rkkuadx759g] (score 2, diepte 2) Yess, and then just get them resoled and they’ll do another 2 :)
[19rh9gmft03ms] (score 1, diepte 2 OP) i thought they looked really cool but they look like they have 0 ventilation. i don’t want to spend $80 and be in the same boat i’m in now
[19rhbw3w0ewdd] (score 1, diepte 1 OP) how’s the ventilation?
[19rn57s2mm0rp] (score 1, diepte 1) These are the best, been using them for 15 years or so. I use the closed back style though.
[19rgusnflpc9t] (score 1, diepte 1) Mine didn't last, but I'm hard on shoes. They were comfortable though
[19rk4tg6l9tnm] (score 1, diepte 1) I used to run my Vans makers slip ons through the dishwasher once every couple of weeks. To this day I have no idea how canvas shoes could withstand that. Not recommending it, for the record.
[19rgzahvzw40w] (score 1, diepte 1) I wore hoka Bondi SR's for 2 weeks and had unimaginable hip and back pain. may just be my own problem but I wince whenever I hear about them
[19rqbu4z89ylf] (score 1, diepte 1) The Bondi helped tremendously with my lower back problems, but they are big, ugly, and expensive.
[19rgt72l5t8wz] (score 1, diepte 0) Crocs, idc if my feet hurt, I love my crocs
[19rgtzz8jy3xg] (score 1, diepte 0) Wolverine Floorhand waterproof soft toe boots
[19rh47il280o5] (score 1, diepte 1) What brand? My old work docs went to shit a year ago
[19rk4vo3v2a90] (score 1, diepte 1) Wearing blundstone knockoffs right now. Concerned that they aren't breathable, but they are extremely functional.
[19rgz2wcap10h] (score 1, diepte 1) Why are they so hard to find these days? Had. Pair of Boston super grips since 2017 maybe 2018. Took a small break from the industry in that time but I need a new pair desperately. Can't find the Boston anymore so.j sent looking for the Tokiyo but can't find a pair in my size (9.5-10 US) anywhere. 

Birkenstock saved my career. I couldn't deal with the back pain anymore and they took it all away. Really bummed I can't find any super grips in my size.
[19rhp6r0tqi5f] (score 1, diepte 2) Official website has me on a waiting list for my size. I went on amazon and found a pair in my size sold by Birkenstock. Super weird but you might be able to find a pair in your size.
[19rhbvmjc21d0] (score 1, diepte 1 OP) i was looking at those last night but idk if i can justify that price rn
[19rhhxgd98i90] (score 1, diepte 4) Without question
[19rhg73ceb1pf] (score 1, diepte 1) I 2nd this. They are the best.  26 years in the kitchen and I landed on these as my favorite.
[19rgycfnzkiua] (score 1, diepte 0) 3/4 boots with composite toes, waterproof, non slip and Dr Scholls inserts.
[19rgyol9soqcj] (score 1, diepte 0) Switched to snibbs and never looked back
[19rhyd349ue00] (score 1, diepte 1) Lowkey I got these for free bc the owner was a regular at the restaurant I was working at. They were fucking terrible 😅
[19rgyuzvqpu8w] (score 1, diepte 0) Bragard
[19rgzozbnc2n7] (score 1, diepte 0) Timbs.
[19rh2ahjia63p] (score 1, diepte 0) machine washable skechers
[19rh3pwgpfjvm] (score 1, diepte 0) I really like Merrill’s. Just buy yourself an insole
[19rh5g4eusdwg] (score 1, diepte 0) Merrell Men’s World Legend 2 Moc Remat Wide Width
[19rh911i1m82s] (score 1, diepte 0) Contrary to a lot of folks , I very much like my pair of mise .
[19rh9f10p12ed] (score 1, diepte 0) Thoroughgoods
[19rhbtv355obp] (score 1, diepte 1 OP) what’s the price point of these? are you able to wash them/scrape the bottoms easily?
[19rhgll203fxc] (score 1, diepte 0) I’ve had some expensive shoes, but I honestly think my cheap, black Skechers are my favorites.
[19rhjjflttdnn] (score 1, diepte 0) Keen's PTC Oxford. Ive owned 2 pair on 5 years, the first lasted me 3 years. They are comfortable and durable.
[19rhjlxhb1nc3] (score 1, diepte 0) Big fan of redbacks, my kitchen is about 50/50 blundstone/redbacks and I'm converting them slowly
[19rhlncx4xwmb] (score 1, diepte 0) Blundstones. Comfortable, stylish and last a good while. Been my go to for the last decade. Strongly recommend
[19rhm644sllcz] (score 1, diepte 0) Not your broken flat tires.... lol
[19rhq73ownof4] (score 1, diepte 0) I do birkenstock A630s. They're great and I have almost no foot or back pain in them, but I do crave a little more cushion sometimes. Off to do another 12 hour shift in them today.
[19rhqit9jzhpg] (score 1, diepte 0) My last 2 pairs have been snibbs and I was working 10hrs 6 days a week average and they both lasted about 2 years. The first pair was a gift I tried going back to a cheaper standard pair and it was so bad I went and got myself another pair of snibbs
[19rhrvkjnuf6s] (score 1, diepte 0) HOKA has a really good pair of slippers resistant work shoes. Theyre pricey at $200, but they've lasted me close to 2 years and my knees and feet no longer hurt every single day after work.
[19rht20rbho4l] (score 1, diepte 0) I’ve tried literally every brand and cut of shoe under $150, and nothing has beat Sketchers for me, Hoka is a close second. 

For reference I’m 350+ lbs and wear through shoes pretty quick working 8-10 hrs a day on my feet. 

Currently wearing cessnock sketchers and their a 10/10 for me
[19rhtxeijq92b] (score 1, diepte 0) Blundstone boots, hands down.
[19rhujk6u6fs3] (score 1, diepte 0) Brooks running shoes, hands down.
[19rhyad24lbvp] (score 1, diepte 0) Mise, but with added insoles. My first pair lasted about 3 years and I like that it’s easy to clean. Trying out their Chelsea boots next.
[19rhyf52c4s4k] (score 1, diepte 0) Black steel toe blundstones with a set of insoles in them, my feet have been quiet since I switched from crocs/kitchen shoes
[19ri2n1q2eued] (score 1, diepte 1) That, and they last. I had a pair last me 4 years of 50+ hour work weeks.
[19ri2vc5f78tg] (score 1, diepte 1 OP) what’s the ventilation like? do your feet feel soggy af at the end of the day?
(35 reacties met lagere score weggelaten)

