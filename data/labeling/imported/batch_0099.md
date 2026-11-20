# Label-batch batch_0099

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
Schrijf het resultaat naar `batch_0099.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: yr3oc2, 1rjaij4, 17fdc2b).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD yr3oc2 ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-11-10  SCORE: 32  REACTIES: 75
TITEL: bro how do ya keep ya feet from not feeling like it's breaking
POST (source_id=post):
I'm four hours in and my feet feel like they're gunna fall off. Any tips on how to lessen the pain??

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ivruv4k] (score 25, diepte 0) Dont wear Zappos shoes. Those pieces of crap hurt my feet so bad they were going numb. Everyone told me it would go away in time

NOPE. i ordered a $50 pair of Sketchers and they were night and day better. My feet still get sore after a busy day but its nothing like those shitty ones I had. Decent shoes make all the difference
[ivrs1wb] (score 16, diepte 0) It's inevitable 🤷🏼‍♀️ go get a pedicure, your feet will appreciate it.
[ivsstos] (score 14, diepte 1) I don’t understand why people keep talking about Zappos like they are a brand of shoes? They are just a distributor. There’s a ton of different types/ brands of shoes on there and a lot of them are fine and comfortable.
[ivrs716] (score 10, diepte 0) Get those blue shoe inserts from the supermarket or drug store.  They help a lot for about a month.

Also, make sure your shoes are big enough and wide enough.  Your shoe size changes.
[ivs1fw6] (score 9, diepte 1 OP) Damn bro im in the freezer wearing Adidas right now AND I got asthma 😭😭😭 this is a nightmare.
[ivsbynv] (score 9, diepte 0) I use well  fitting new balance safety shoes (I got fitted for my size at a running store) and superfeet orange insoles along with arch support/padded socks. 

Really helped me out. Also, Keep your nails trimmed.
[ivsssly] (score 8, diepte 1) Rip liver
[ivs8xvk] (score 6, diepte 0) On my lunch break I go to my car and take off my shoes for 25 mins and put them back on when its time to go back.
[ivv2dzo] (score 5, diepte 1) categorizing zappos shoes as a whole is honestly wrong. there’s good shoes and bad shoes, just like anything else in life. Don’t judge anything based on a whole group.
[ivs1o8m] (score 5, diepte 0) OMR here, I would first make sure that the shoes fit properly. Get some good insoles, good does not equal expensive either. Make sure that you have some good thick socks to help cusion your feet from stiff parts of the shoe, especially as you are breaking them in. Make sure to not wear brand new shoes for an entire shift if you can help it. Ease into them. Make sure you bring other shoes to change into while you are breaking the new shoes in, and change into them at the first sign of pain each night. You can slowly wear them longer and longer, as they get broken in.
[ivrsgh1] (score 4, diepte 1 OP) Lmao that actually sounds great tbh
[ivsjrp7] (score 4, diepte 2) Yeah they are steel toe
[ivs1xsv] (score 4, diepte 0) Hand stands.
[ivs21tc] (score 4, diepte 0) Insoles help but the pain won’t go away regardless of what you do. You’ll just become more resistant to the pain after a while 🤷🏻‍♂️
[ivs3s9t] (score 4, diepte 0) If you move more and not stay just standing in one position your feet hurt less.  I’m occasionally a water spider and since I move a lot my feet hurt less than when I am on sbc or dam dispatch
[ivs5qbi] (score 4, diepte 1 OP) LMFAOOOOO damn bro have you seen doctors at least?
[ivssvt6] (score 4, diepte 0) Epsom salt foot baths.
[ivrukws] (score 3, diepte 0) Some people wear 2 socks on each foot to help with pain, other wears insoles go help, or you could do both, massage your feet before or after work or during etc
[ivs2zip] (score 3, diepte 0) 4 hours in you shouldnt really feel that way unless you are truly never on your feet. You might have plantar fascitis. Had the same problem and it was solved after a day or 2 wearing the PF insules. If you tend to walk around barefoot a lot it happens
[ivs97r8] (score 3, diepte 0) 2 pairs of socks, plantar fascitis sleeve on both feet, and insoles
[ivsk6mn] (score 3, diepte 1) what's the name of the nb safety shoes?
[ivsfsfg] (score 3, diepte 0) One time I sprained my ankle very badly on the ship dock, I should’ve probably explained it to the PAs, instead I spent the next 9 hours limping on it, it was hell 

I recommend getting insoles, make sure your shoes are tied tightly, and do some stretches before going into work, I also would maybe take a painkiller
[ivvj36p] (score 2, diepte 2) I guess that's fair, i had talked to about 4 others that hated their shoes and were either actively in pain or had already replaced them so I assumed their entire brand was garbage

But i guess they might have some good ones
[ivs3v33] (score 2, diepte 1 OP) Nah yeah I realized that today but it's hard to move in this giant freezer suit so I end up walking slower
[ivs5yno] (score 2, diepte 0) Ibuprofen is goated for this. I take some IR 500mg ibuprofen 5 minutes before every break, then during break I take an extra chair to rest my feet on. I’m a big dude too and I wear those shitty Zappa shoes. End of the night my feet might be a little sore but nothing like before I started doing those 2 things
[ivsds9r] (score 2, diepte 0) Orthopedic show inserts, feet and lef stretches, aleve and get home… take hot  epsom salt bath. Your feet will adjust after a few weeks.
[ivsm7wz] (score 2, diepte 1 OP) I was thinking about pain killers but I don't want that to be something I overly rely on ya know
[ivsh4fo] (score 2, diepte 0) Take your entire arse to the Good Feet Store.
[ivshyb3] (score 2, diepte 0) Ibuprofen
[ivsnv2c] (score 2, diepte 0) Red bull
[ivvhwcq] (score 2, diepte 1) Yeezy shoes works too
[ivtwtlq] (score 2, diepte 0) Nice shoes, they definitely make the difference. I have reebok composite toe and I haven't had any feet issues
[ivrrp8f] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[ivtveoj] (score 1, diepte 4) Naw won't fire you at all. Also amazon does not decide who gets workers comp they use a third party Company they legally can't be the one that makes the choice. Now sedgwick might deny you for that reason or they might not who knows I have seen them deny claimes that where legit and should have been approved and I had the AA file a dispute and they ended up winning and I have seen them approve shit that was clearly BS luck of the draw like with any WC company
[ivtwsx3] (score 1, diepte 6) If your drunk or high your fired and federal law says your not entitled to anything lol but yeah naw long as your not clearly faking it they are not going to challenge your already a LTI and recordable the rest really does not matter. I do the investigations and they legit never even ask for anything for a denial unless you just softly lay down and say you fell or some dumb shit (that actually happens btw lol) even if your breaking the rules unless it's absolutely insane like riding a pallet jack by all the stations we legit can not discipline you for it. I just talk to them and tell them not to do dumbshit anymore and move on. Workers comp is a very strange world and sedgwick legit holds almost all the cards I have never seen amazon fight a workers comp case unless like I said it was clearly fake then you will more then likley get fired and depending on the state potentially arrested
[ivw1qpu] (score 1, diepte 2) Yeah my first two pairs were sized wrong and were bigger than they should be, and they gave awful blisters. I didn't return the second ones since they had actual blood on them and I didn't think they'd accept them. On my third try though, and I love my Nautilus
[ivw385w] (score 1, diepte 3) Yea it just depends on what brand you get. Some brands of shoes suck. Some are better. Doesn’t really have much to do with Zappos lol.

People at my fc are always blaming Zappos I don’t get it
[ivvrp4q] (score 1, diepte 3) well they sell all sorts of different brands of shoes. i got some reebok’s through them and i’ve been wearing them for 6 months i just changed out the insoles and still rocking them 😂😂
[ivw0z37] (score 1, diepte 1) Pleassssse take less ibuprofen! It’s so bad for you long term! Especially the amount you’re describing! My whole body hurt when I first started at Amazon and now I take collagen powder throughout my day and I haven’t needed any pain medicine for over 6 months. No muscle aches, nothing. Pllllease look for alternatives, you’re going to kill your body  💔
[iw4tigb] (score 1, diepte 1) Make sure you switch between acetaminophen and ibuprofen. Itll be a little easier on your body long term. I don’t recommend taking that much but I ain’t preaching I’ve done it.
[ivw0kva] (score 1, diepte 1) I read this in a Scottish accent
[ivsjnf7] (score 1, diepte 0) Furuian shoes will change your life. I bet mine on it. 

Furuian Steel Toe Shoes for Men Lightweight Indestructible Work Sneakers for Women Puncture Proof Comfortable Slip On Safety Shoes for Industrial,Coustruction https://a.co/d/0MnfVJp
[ivslr77] (score 1, diepte 0) The shoes matter and it doesn't even have to be a 100$ pair a Walmart pair felt better than the 150$ timberland work boots I bought I'm Dead ass,l.
[ivso4zy] (score 1, diepte 1 OP) We ran out bro smh
[ivso6he] (score 1, diepte 2) Did you look at all break rooms
[ivso88v] (score 1, diepte 3 OP) Oh shit you're right I didn't I always ignore the one on the first floor for some reason smh
[ivso6tc] (score 1, diepte 0 OP) Thanks everyone for all the advice. I'm definitely going to take these into consideration and try them. I'm done with my shift it's 4 am God damn I'm my days off are here lmao
[ivt0dxd] (score 1, diepte 0) Invest in some good safety shoes (I recommend CAT boots), wear compression socks and if also necessary get some Dr scholls insoles. Ibuprofen doesn't really work for me, I use Diclofenac instead. Put your feet and hands in warm water, that helps as well.
[ivt0uks] (score 1, diepte 0) expensive running shoes dawg
[ivt3al6] (score 1, diepte 0) foot massage
[ivv0atf] (score 1, diepte 0) Are u a fresh associate? If so do u need steel toe? My last site didnt enforce that crap if not wear the most comfortable shoes u can find i used to use adidas with memory foam.... Good luck
[ivv4tuy] (score 1, diepte 1 OP) They did at firsy but no one wore em so they just gave up. I wear Adidas but I'm thinking of maybe getting foam deposits.
[ivv52wk] (score 1, diepte 2) Yeah im at a DS site now and have to wear steel toes.... Found the most comfortable ones ppl mentioned on here and added memory foam inserts and mole skin in the hotspots.
[ivvbnhi] (score 1, diepte 0) Honestly I suffered for month. Until I decided to switch them and ordered 2 sizes up. They still hurt but it’s bearable for the 10 hr shift. Steel toe suck if you’re not use to them. I got the timberlands pro.
[ivvgjrg] (score 1, diepte 0) Chop your feet off to do the lord Bezos’ work
[ivvipe6] (score 1, diepte 0) Take shoes off on breaks if you can. I sit in my car so on my lunch I take my shoes off soons I hop in
[ivvpr3p] (score 1, diepte 0) I got the $80 sketches with the zappos and an insole.  Working stow with that ladder (I'm on the heavier side) and so far the shoes have been great.  Was using the pumas before that and it was a nightmare.
[ivw02n4] (score 1, diepte 0) I had this same problem and not wearing the right shoes caused me to get a stress fracture in my foot.. literally just from all of the walking. Didn’t drop anything on it or something crazy, just a tiny break from the constant walking and in bad shoes.

Since then I’ve gone through several shoes, but what I found that worked was going up a half size and getting them in wide. This helped bc it compensates for the inevitable swelling that’s going to occur from walking 25k steps on concrete. 

I also invested in good inserts and metatarsal pads, bc inserts aren’t very thick near the top of the foot and didn’t provide enough cushion for me.

As someone else said, compression knee highs are great. I thought they were just for old ppl or ppl with medical problems, but when I broke my foot last year my podiatrist advised them and they made a world of difference!

I saw someone suggested taking ibuprofen for pain… I’m also a pharmacy tech and it’s not good to rely on NSAIDs (naproxen, ibuprofen) bc it’s bad for you long term. It shouldn’t be something you’re taking every day. I take collagen powder either in my food or coffee multiple times a day and it has completely alleviated the need for pain meds while working at amazon (takes about two weeks for full effect, and I take 4 times the recommended dose)

Some ppl think the stretching is stupid, but you should do it, and stretch your feet ankles and toes as well, it makes a difference. 

If you’d like a link to the collagen powder i use just let me know, it was such a life saver I suggest it to anyone I find out is taking too many pain meds! I found a huge jug on Amazon, and it is completely tasteless and dissolves easily in food or liquid. I love it bc I use so much of it and the normal containers at regular stores would only last me a week or two and were too pricey. 

Good luck!!
[ivw0joi] (score 1, diepte 0) I bought the shoes that everyone was talking about in here. "Furuian Steel Toe Shoes" pretty comfortable and do not burn like the ones from Zappos
[ivwfxfm] (score 1, diepte 0) You could always go to the bathroom and take your shoes off and give them a quick massage. I also used to go to my car during break and take my shoes off to let my feet breathe (mine were too tight)
[ivwgeia] (score 1, diepte 1 OP) I can't that's tot
[ivwhs9j] (score 1, diepte 2) Mmm no it’s not. I mean it is, but 5 minutes tot isn’t anything at the end of your shift. What department do you work? For sure if it’s stow, don’t be to hard on yourself and go to the bathroom 😂 

STU- seek to understand, managers will come by when your TOT is too high to “understand” where you were/what was going on. I think this doesn’t begin until at least 30 mins though, someone correct me if I’m wrong
[ivwkh80] (score 1, diepte 3 OP) They take off one hour for one minute let alone five I'm fired at that point lmao
[ivwnld7] (score 1, diepte 4) Damn that’s crazy! I defo would’ve been fired already if i worked at the same place 😹
[ivwkig4] (score 1, diepte 3 OP) And I work at fresh
[ivwr8bm] (score 1, diepte 0) Insoles, compression socks, and no pto or vto lol. You gotta work consistently for a few months or you'll never get used to it
[ivwrmyx] (score 1, diepte 0) compression socks, and epson salt soaks for 10-20 mins in hot water. I have restless legs and it really helped me go to sleep and heal. buying some soles with arch support for my shoes made a lot of difference too.
[ivws7mo] (score 1, diepte 0) Get plantar fasciitis insoles they make the world of difference
[ivwtv6x] (score 1, diepte 0) Compression socks and hard toed sneakers will be a blessing. The shoes Zappos provides suck. Maybe also get insoles if your feet still hurt afterwards.
[ivwujjs] (score 1, diepte 0) If this helps, I got Zappos, and honestly they’re a godsend. They’re rebook and I’ve never seen anyone else with it and I’m constantly getting stopped and asked if my shoes are steel toed, I’ve worked 12 hour shifts and felt nothing! They were maroon colored, I’ve been there since June and i have zero complaints
[ivx0y5o] (score 1, diepte 0) Bro get a pair of Timberland Pros, they’re comfortable asf and I work in one of the old school FCs that have you walking around so much. My feet feel great still at the end of the day
[ivuvoaq] (score 0, diepte 0) You get used to it after two weeks, and if you don't... get better shoes.
[ivs92mz] (score -5, diepte 2) They will not fire you, they will send you home if you dont have safety shoes or if you refuse to wear the safety covers.

=== THREAD 1rjaij4 ===
SUBREDDIT: r/AmazonFC
DATUM: 2026-03-03  SCORE: 30  REACTIES: 75
TITEL: My feet smell like PUKE after my shift
POST (source_id=post):
Sorry to be so gross, but I need help.

I'm a very clean person and bathe before work. I'm in indirect role where I'm waterspidering all day so constantly moving. 

When I get home and take my boots off, the stench is embarssingly bad, just the with feet. How do I deal with this? Obviously showering after (which I do), but god forbid the few times I can't right away and have to deal with it. I've got new boots and that didn't change anything.

Anyone deal with? It's not a normal type of odor, it's disgusttttting

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[o8bt1z5] (score 38, diepte 0) Maybe foot powder in your socks I like to do that help everything stay dry
[o8bwx47] (score 32, diepte 0) It’s the shoes man. None of them let your feet breathe .
[o8bv5ij] (score 21, diepte 0) Glycolic acid right after the shower on your feet when they are still damp. Dermatologists recommend it for B.O. on any body part. Also, it can make your feet/rough spots on your body softer with consistent use.
[o8bupya] (score 11, diepte 0) You need cotton socks.
[o8cqi9b] (score 11, diepte 1) Shhh... don't tell.  If they're more or less unwearable you can have safety put in a ticket for a new pair.
[o8cy82v] (score 9, diepte 1) Spray powder too before work
[o8bxy6b] (score 9, diepte 0) It sounds like you have athlete's foot. You need to buy antifungal cream (such as terbinafine or clotrimazole) and apply the cream for at least a week, morning and night. 

New shoes once the treatment is done. And antifungal powder afterward.
[o8btkn2] (score 7, diepte 1) And change your insoles every few months.
[o8bz6dt] (score 7, diepte 0) Worked EMS prior to here, wearing leather boots for 48+ hours at a time.

-Talc Free Powder
-Cotton Socks
-New insoles every 6 months or so
-Boot/shoe drier
-shoe disenfentant/deodorizer spray (they sell it in the shoe section at like Walmart. Kill the bacteria, kill the smell)

If you do all those it SHOULD be manageable. But most safety shoes are not breathable at all and the smell/sweat problem will always exist to some extent
[o8c3jm7] (score 7, diepte 0) It's not solely your feet and you aren't gross. You're walking around for 10 hours a day. Copper socks. Yes, socks lined with copper. Put scented baking soda in your shoes. Wash feet thoroughly. Yeah that's pretty much it. Copper lined socks are a game changer. They actively kill and prevent smell producing bacteria. Combined with other suggestions and you're good to go.
[o8btfts] (score 5, diepte 0) Get a shoe drier
[o8cka8f] (score 5, diepte 1) If you have also toenail fungus (can't believe I'm admitting this LOL, some ppl know my username here haha- but we're ALL human and it HAPPENS!!!!), Vic's vapo rub can be your best friend- just apply to the area after showering daily, and it is a long game (needs to grow out).  I also did a weekly toe dip in peroxide, not sure if it helped though).  I just finished using it for like 6 months and my big toenail is healthy again, and ready for sandals!!!  No toxic drugs, just camphor and eucalyptus doing its magic ;)
[o8c5070] (score 5, diepte 0) I use the Secret whole body spray on my feet (it’s meant for sensitive spots too!) with foot powder in my socks lightly rub it on your feet if you can’t pour it into your sock. I also apply a little bit in my shoes. It definitely helps out a lot! I also use the dial antibacterial soap on my sweaty areas and go back with whatever body wash I usually use in the shower. After a shower lotion, an apply clean socks. My socks/underwear and usual clothing I wear to work I wash with the Lysol sanitizer solution and normal laundry pods, no fabric softener or scent beads. Fabric softener if used too much can thin the fabric of your clothing causing issues later like not absorbing sweat if cotton.
[o8bwgaf] (score 4, diepte 1) Like the shoe drier was a life saver, STG everytime I take my shoes off I wanna cut my feet off and trash them as well. And it’s only at Amazon, mind you I wear slides and flip flops exclusively because I like to spread my toes lol
[o8bwv4v] (score 4, diepte 0) Get 2 pairs of boots wear and change them through out the week and use dickies socks
[o8cjn0w] (score 4, diepte 1) If you haven't used your shoe allowance yet, go for pairs that are on clearance- I got a pair of Keen and Wolverine this year, fully covered, and they are SUPER comfy (at least for composite toe lol).
[o8c39xx] (score 4, diepte 0) Uncle Todd's enzyme shoe spray for your shoes.  Works pretty good. Get some foot spray from the dollar store.  If you want to go whole ham get to tea tree wipes and wipe your feet down in the stall on break.   Another upgrade is to get yourself some good smartwool socks that actually keep your feet dry.
[o8fe1wd] (score 3, diepte 1) This plus a boot dryer and a spray of Clorox into them before you put em on the dryers. 

Believe me it helps. And make sure you're only wearing socks for a single shift. The Clorox spray kills all the stinky bacteria and the dryer makes sure that anything left is cooked to death. The feet however will likely smell bad no matter what you do at the end of the shift. All you can do is mitigate it.
[o8bxt6a] (score 3, diepte 0) Scrub the dead skin off your feet in the shower at the end. Blow dry your feet. Wear socks designed for people with sweaty feet. Use an anti perspirant spray on your feet.
[o8c2xno] (score 3, diepte 1) This, also clean thoroughly under your toenails and scrape w plenty of soap nightly.
[o8by9kb] (score 3, diepte 0) Tarantino would STILL suck on them hoes
[o8ctjfe] (score 3, diepte 0) Leave your shoes out in the sun to dry regularly. You want your feet to be dry when wearing your shoes to avoid smelly feet, but the issue with that in my case is the calluses that develop after a while. The solution that I found works for me is to dry my feet, apply lotion and after that apply Vaseline to lock in the moisture from the lotion. The results are great smelling and looking feet and no calluses.
[o8dg7kh] (score 3, diepte 0) Clean you feet with Lume.   

Do NOT wear Cotton socks.   Your feet are sweating and Cotten absorbs it and traps sweat and bacteria.   They do not wick the wet away from your skin.  Instead, cotton holds the sweat and bacteria next to your skin… and makes it stink.      Wool is your friend.   It is a game changer.   It wicks sweat and is antimicrobial.     Buy a bunch of wool socks and rotate them.
[o8c6iik] (score 2, diepte 1) Good advice, and socks should be 100% cotton, no synthetics.
[o8c679c] (score 2, diepte 0) I had the same issue.

I bought new insoles for my shoes, put on latex gloves and soaked a clean little dish rag with rubbing alcohol and aggressively scrubbed the insides of both shoes, let them dry and put new insoles inside.

It should be common sense but get enough socks so that you never wear a same pair twice before you wash them all.

I haven't had the problem since and it's been close to a year.
[o8cara5] (score 2, diepte 0) I bought some foot powder & spray after smelling someone else’s stinky feet and knowing mine sweat a lot. Anyway, the spray has helped with not sweating as much and sprinkling the powder in my shoes absorbs any moisture so they won’t start to smell.
[o8cns8x] (score 2, diepte 0) cotton socks make a big difference. You can also try benzol peroxide face wash for your feet. Helps kill bacteria which is what causes bad odor.
[o8cx9wu] (score 2, diepte 0) Try a chlorophyll supplement. You’d be amazed at how well it works with any type of body odor.  I started taking it and foot odor is absolutely gone.
[o8dn86p] (score 2, diepte 1) This. Which brand do you use if I may ask?
[o8dlt9f] (score 2, diepte 0) Air. Maybe a canvas shoe? Wool socks and give those puppies some air somehow. Basketball shoes often have holes worked into the design because of this problem. If you're wearing leather boots then listen to the guy that was telling you about wool socks.
[o8e9n42] (score 2, diepte 0) 2,  if not 3 change of shoes a week. Don't wear the same shoes everyday. That's important. 

Bring a extra pair of socks to switch out mid shift.

Invest in new socks. Gold toes are cushy.

Soak your feet in Epsom salt after work.
[o8bsjop] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[o8cprcv] (score 1, diepte 2) Also dryer sheets in the shoe before you throw em on the dryer if the shoes are especially bad
[o8dws0d] (score 1, diepte 1) Most useless comment of the thread. You can't bring a shoe dryer into work and by the time you put them back on for work the next day they'll already be dry.
[o8btswg] (score 1, diepte 0) Yes powders and change your insoles.
[o8qx4gc] (score 1, diepte 2) They tell you this in training.
[o8e5ad0] (score 1, diepte 1) Yes! They used to always preach to rotate your shoes out so they don’t get worn down but it def makes it a lot harder when you get one credit per year. It’s like June or July when it renews. At my site having a ticket put in will take 10years jut to find someone willing to care enough lol.
[o8f1r55] (score 1, diepte 1) Orthofeet shoes are breathable imo. Also a lot more comfortable than any of the other ones I’ve tried from Zappos
[o8c0wyl] (score 1, diepte 0) Welcome to amazon man lol, get anti odor shoe spray, can't remember the name of the brand I have
[o8d4dw7] (score 1, diepte 1) I agree with investing in moisture wicking wool/cotton socks and no to foot powders. For me, the powder didn't help it actually just made my feet slip on the insole and get blisters.
[o8ej81o] (score 1, diepte 1) This is the way ☝🏽
[o8c3rwf] (score 1, diepte 0) These safety shoes are terrible bro, they made them Mando at our site now and my feet sweat like a mofo and its 30 degrees on the east coast.  Not even summer yet,smh.  Ima start going to amcare everyday, last time they tried this too many people were going to amcare and they shut it down
[o8cc2ve] (score 1, diepte 2) Lysol spry the crap out of your shoes after work
[o8cct29] (score 1, diepte 2) Thank you! My SO has very sweaty feet an we got most of these tips from his Dr an we all live by it now.
[o8cdr1r] (score 1, diepte 0) Different socks can help
[o8cfzgt] (score 1, diepte 0) On Amazon ,Get Lume Deodorant, the cream in a tube, they have an unscented one . It works better for me than any powders or anything. Put it all over the foot and toes especially. Just a small amount tho so it can absorb . make sure you let it dry a minute before u walk or put on sock.
[o8ck2o5] (score 1, diepte 0) Foot power before and after use. Also what do you mean you can’t shower? If my foot stank bad enough that I couldn’t withstand it then showering is a must once I get through that door.
[o8cnoy3] (score 1, diepte 0) go to the doctor
[o8cqlcx] (score 1, diepte 0) Gold Bond.  Really.  It helps.
[o8cti0j] (score 1, diepte 0) Wash inside and insoles with soap and Lysol rinse and spray with Lysol and let them air dry
[o8cvzz8] (score 1, diepte 0) Like others have said it's probably your shoes/boots that aren't allowing your feet to breathe. You can try different shoes/boots and or foot powder. If the issue continues even after you tried alternate solutions then I would make an appointment with the doctor. It seems silly but trust me this issue happens to a lot of people more than you think. My brother has this problem and good Lord does his feet stink 😂
[o8epqav] (score 1, diepte 2) I use Natures Craft. It’s a chlorophyll complex. It also has a bit of peppermint and parsley in it. I started noticing a difference within two weeks. Stay hydrated of course.
[o8d00gp] (score 1, diepte 0) Order composite off Amazon.
[o8d09og] (score 1, diepte 0) Barhe after work instead YESSIR
[o8d3ejg] (score 1, diepte 0) Those steel toed shoes are terrible.
It’s normal, the best you could do to mitigate this problem is making sure to powder your feet with like goldbond or something and check between your toes to see if you have athletes foot, of course wear clean socks everyday and make sure the material is moisture wicking and breathable !
Like bamboo fabric socks.
Just keep your feet dry and clean.
It won’t rid you of this problem completely but the smell will be much less noticeable
[o8d88th] (score 1, diepte 0) Was your feet in hiblcens once a week let it sit on them for 5min and kill that bacteria causing the smell and powder in your shoes and wash the insoles weekly
[o8daqbd] (score 1, diepte 0) during the summer when I first started it was hot af it felt like my skin was coming off on my feet (it wasn't but definitely uncomfortable as hell) and ever since then before i put on my boots I put antiperspirant (not no weird shit, give me all the aluminum) so it helps with the smell/sweat. not sure if you have something more going on with athletes foot or something else but that was my solution. 

Also replaced my shoes when they got worn out, shower everyday, use socks and slippers around the house so your feet go in clean into the shoes. the usual.
[o8djhfu] (score 1, diepte 0) Swap your shoes out. I have two sets, I alternate. Also, Foot powder, and lastly Cedar balls inside your shoes when you're not wearing them.
[o8djn4c] (score 1, diepte 0) Bring several changes of socks to work and change maybe every few hours. How many pairs of work shoes do you own? Buy one more pair and alternate. Switch out every six months. Don't wait until the $110 coupon yearly
[o8dq3e4] (score 1, diepte 0) Carry clean socks and change into them in the middle of your shift. After your shift, spray inside your shoes with an antibacterial shoe spray. Make sure it's able to be "aired out" and dry.
[o8dwdqk] (score 1, diepte 0) Get an anti fungal soap and foot powder.
[o8ejyh4] (score 1, diepte 0) Mmm sounds yummy🤤
[o8ey3m7] (score 1, diepte 0) As someone with sweaty feet I just went to podiatrist. PODIATRIST RECOMMENDED. Wear wool socks, switch socks halfway through your shift. before your shift put foot powder and after every shift spray Lysol in your shoes, it’ll kill all the bacteria that’s most likely causing the smell. If you can I would recommend getting new shoes if you feel like you can’t wash the stench out.
[o8eykz9] (score 1, diepte 1) Also when you get off work take a shower, or at least fully wash your feet. This help me a lot, ig you try this after a week and don’t notice a difference go see a podiatrist, it’s worth it in the long run!
[o8ezdce] (score 1, diepte 0) My brother has terrible feet odor. I bought this, spray on his shoes and it's gone! This is a god sent! Haha

https://preview.redd.it/2xim4qehcumg1.jpeg?width=1170&format=pjpg&auto=webp&s=ac4700a0c5e9920cf645de2def77b664fc746f9a
[o8fag82] (score 1, diepte 0) Try to always keep your feet dry, are you putting shoes on right after a shower, always air them out. It’s ok to go get looked at for it, could have issues that require more. 
But for now, it may be a pain in to do, switch shoes out on one of your breaks. Air them dogs out in your car and put on clean dry socks and different shoes.
[o8fjhgd] (score 1, diepte 0) I had the same issue and bought desenex. Put a little of the powder in my socks before work and it was like a miracle
[o8fmhpk] (score 1, diepte 0) So I had this issue for a while while I worked construction and it turns out it was a mixture of boots that got wet, and shitty socks. Changing socks to an all cotton blend was a game changer
[o8fxpnd] (score 1, diepte 0) Odor-Eaters foot powder works well. You may also want to change out your insoles every month or two
[o8fz6ii] (score 1, diepte 0) Piss on your feet in the shower old folklore it works
[o8g00m2] (score 1, diepte 0) Vinegar water epson salt cornstarch and tea Tree oil make a mix thank me later
[o8gk811] (score 1, diepte 0) Gold bond.  
Blue or green bottle depending on your needs.
[o8go8be] (score 1, diepte 0) Use an anti fungal and deodorizing foot spray or powder before and after work and buy moisture wicking socks they will keep your feet drier
[o8jrbfy] (score 1, diepte 0) Get odor eater insoles. And wash your feet. Once dry, powder with gold bond medicated foot powder
[o8m6k9z] (score 1, diepte 0) You probably have trench foot it's common with the work shoes. Get some foot powder change your socks asap when you get home
[o8pld9h] (score 1, diepte 0) Idk if anyone has mentioned yet, but I’ve noticed my son’s feet REEK if he wears cheap socks/socks with any polyester. 100% cotton is the way! The material of the socks you’re sweating in all day makes a world of difference - if you’re confident that you’re cleaning properly, that/the shoes not being breathable could be the culprit
[o97hosz] (score 1, diepte 0) I definitely think it’s cause u wear boots maybe switch to the sneaker steel toe and see how that works cause I can’t imagine having ur feet in boots all day 😭😭
[o8cw9in] (score 0, diepte 1) 😂
[o8cfphp] (score 0, diepte 0) U might have a infection or foot fungus. Or ur socks or boots material just stinks when it’s hot and damp and it seeps into ur feet. Try wool socks my feet don’t stink at all when I wear darn tough steely toe socks, but they reek after a 10-15 mile day in some dickies or Nike socks

=== THREAD 17fdc2b ===
SUBREDDIT: r/electricians
DATUM: 2023-10-24  SCORE: 176  REACTIES: 75
TITEL: Insulator hate thread: I left my ladder on a jobsite. Insulators used it while I wasn’t there, got the foam stuff on one of the feet, and didn’t clean it off. Now the ladder is unstable, and wobbles. Taking the first hour of the day to clean the stuff out with wire cutters.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k68zkog] (score 89, diepte 0 OP) I’ll be the first to blame myself, I usually lock up ladders when I leave, but forgot to this time. But fuck man, if you get your stupid foam shit on my tools, at least try to clean it off.
[k69dlgu] (score 82, diepte 0) Tapers once "borrowed" my ladder - I come back to it totally covered in mud, meanwhile GC had 3 sitting on-site unused and spotless. And then he had 2.
[k69e56w] (score 71, diepte 1) I did the same thing. Came in one day and my extension cords were strung everywhere and my ladders all over site. I was supper pissed at first. Took everything with me at the end of the day. Got a call a few days later from the site sup asking where all the cords and ladders went. I just told him rough-in is done and they are at another job.
[k69mrpa] (score 45, diepte 0) I once unlocked all the ladders (10',12') and promptly took a shit outside in the john. All I heard was a chain being undone, esponel, clanking, and a truck drive away. A new 12' ladder was gone.

     2 weeks later, painters truck comes back, with all aluminum ladders. Except 1 bright 12 footer with the " company electric" on it. I stole my ladder back. Took pictures, sent to the p.m. another p.m. the GC, and  the painter owner. And literally no one cared.
[k69tn7b] (score 44, diepte 2) Lol wtf does the super think your shit is for everyone?
[k69tfnb] (score 40, diepte 2 OP) I’m on hour three, still no progress. Lunch time though
[k69j4qo] (score 35, diepte 1) Maybe 2, depending on how the day goes.
[k69lmlh] (score 31, diepte 1) >And then he had 2.

:)
[k6976ll] (score 26, diepte 0) It's going to take you an hour to clean that?
[k6a57fg] (score 24, diepte 1) Next time shit on the ladder, nobody will take it.
[k6a7c2k] (score 23, diepte 3) Yeah right? They didnt say shit when i told them its gone to the next site. But maybe, just maybe, he was concerned it my shit got legs and walked away
[k6923u5] (score 23, diepte 0) Everytime I take a week off I come back to a wobbly ladder, the idiots walk the ladder instead of getting down and moving it.
[k69nt1v] (score 18, diepte 1) And 1 was covered in mud!
[k69tpsu] (score 12, diepte 0) I was always a little amused at how lifts and ladders were just community property on big jobs. Oh the tinners aren’t  here today. You can just use their lift. 
Or you come back after not being on a site or a floor for a day and your lift isn’t there anymore and someplace else, dead. Or your ladders are all moved
[k68zz4h] (score 11, diepte 1 OP) *unmortars the brick*
[k69li1d] (score 10, diepte 1) And it's always the guys that talk big game but actually fuckin suck and you kinda just let ramble until they eventually get fired for fucking enough stuff up
[k6bc0zn] (score 8, diepte 1 OP) Lift is always dead, and the extension cords are now being used for the overhead chain lights.
[k6bmx1w] (score 7, diepte 1) When I insulated we'd not get the gear dirty first off, but if a new guy did it literally took 5 minutes to clean that foam off (after it dries) with a knife or screw driver. An hour though? Someone is really milking that job out.
[k69kcn5] (score 6, diepte 1) Safety first bubba
[k69qy87] (score 6, diepte 1) Take me till lunch
[k69veew] (score 6, diepte 4) Vaseline takes it off. I leaned on a wall covered in it from my ass to shoulders. No shirt on .  Hot as balls I drove home wrapped in poly.  Old guy was like vase takes it off. I wasn't sure if he was fucking with me . But it worked
[k6a6zun] (score 6, diepte 2) I know I should have. Poor judgement on my part. Flooring wasn't even down yet
[k69ymvl] (score 5, diepte 3) Try a flap disc on an angle grinder
[k6bg0ac] (score 5, diepte 3) Acetone will take spray foam off in seconds. I’d still charge the insulators 5 hours though.
[k69e42b] (score 5, diepte 0) Thanks for sharing
[k68zudd] (score 4, diepte 0) I’ve had masons fill the round “hole” with mortar on a brand new ladder just because they wanted to be dicks.
[k69rbao] (score 4, diepte 1) Hydrochloric acid, I always have a jug of it in my van just for this purpose
[k6a5k29] (score 3, diepte 1) Not to start a war (ok maybe) but use some of the orange marking paint and spray their fresh mortar joints. Maybe next time they will think about fucking with you.
[k6bsezg] (score 3, diepte 2) I was just trying to make it through the job. I was sent there to put boxes in their block no I was still an apprentice. Was so fixated on all of the boxes that I missed that one of the panels was supposed to be recessed as well. 

Ended up having to cut many boxes in as well because they would say “we’re doing Wall ‘G’ next Thursday and I’d show up on Thursday and it would be complete.”

In fact, they did that in one particular wall so I grabbed our hammer drill and started drilling down to run my conduit down. The bit got caught on their rebar, yanked the hammer drill out of my hands, and tore the top course off of the wall, 4-5 blocks long. They then showed up and “What the FUCK, Sparky?”

You dumb asses have this wall done 2 days before you told me you were going to do it and never relayed any information telling me plans had changed. “Well, we’re going to have to backcharge you to fix it.”  “Talk to my boss about it, idiot”
[k69lxmm] (score 3, diepte 1) I guess if it was black caulk, I could see getting worked up.
[k69pzmp] (score 3, diepte 2) That shit gets on everything
[k69q27a] (score 3, diepte 0) Isn't there something that dissolves that shit?
[k6ae4vv] (score 3, diepte 3) I would have thought definitely don’t expose a fiber glass ladder to HCl but evidently it is ok within concentration and temperature limits.

https://www.wernerco.com/docs/default-source/literature/gm6070-fg-techmanual.pdf?sfvrsn=dda06ff2_2
[k6ajeau] (score 3, diepte 0) Lock up your ladders
[k6b0qvl] (score 3, diepte 0) This is why my ladders have a nice leash that connects them to my jobox when not in use.
[k69sz2j] (score 2, diepte 3) I always tell new apprentices “DO NOT! Touch the black stuff, it gets everywhere and is a nightmare to get off”
[k69vlp9] (score 2, diepte 5) Awesome, good to know. Thank you
[k69m5i2] (score 2, diepte 0) Learn to lock your ladders up.
[k6dvjb3] (score 2, diepte 1) Sounds like a tire screwing is in order.
[k69t5m4] (score 2, diepte 2 OP) Thank you!
[k6a0c2t] (score 2, diepte 2) I was thinking a solvent like acetone.
[k6a0k1g] (score 2, diepte 2) Is that for real?  It sounds a little like a joke, but if it's for real I'm getting some.
[k6bg3aj] (score 2, diepte 2) You can still use acetone on cured foam.
[k6at5fw] (score 2, diepte 1) Acetone. It will dissolve the rubber too.
[k6ayy4n] (score 2, diepte 0) Ladders are the most dangerous tool because of this kinda ass hattery.
[k6bqque] (score 2, diepte 0) Tip: when on messy jobs put booties or plastic bags on the feet of the ladders and tape them on. If stuff gets stuck to the bottom and makes it unstable, rip the bag off and replace.
[k6c3v6y] (score 2, diepte 0) Bullshit, buy your own to destroy
[k6dfa3l] (score 2, diepte 0) Those spray foam guys are almost a different life form entirely. I think it’s because they breathe that stuff in every day.
[k68z6pr] (score 1, diepte 0) **ATTENTION! READ THIS NOW!**

**1. IF YOU ARE NOT A PROFESSIONAL ELECTRICIAN OR LOOKING TO BECOME ONE(for career questions only):**

**- DELETE** THIS POST OR YOU WILL BE **BANNED**.

**2. IF YOU COMMENT ON A POST THAT IS POSTED BY SOMEONE WHO IS NOT A PROFESSIONAL ELECTRICIAN:**

-YOU WILL BE **BANNED**. JUST **REPORT** THE POST.


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/electricians) if you have any questions or concerns.*
[k68zbrz] (score 1, diepte 1 OP) I’ll be the first to blame myself, I usually lock up ladders when I leave, but forgot to this time. But fuck man, if you get your stupid foam shit on my tools, at least try to clean it off.
[k6edlnm] (score 1, diepte 1) Yep, lock it up or take it with you or expect stuff like this to happen. People don't care about other people's stuff.
[k69dofr] (score 1, diepte 0) Thats shitty.
[k69inip] (score 1, diepte 0) Back charge the insulation Corp for the loss of time.
[k6ehg4g] (score 1, diepte 2) It was like 3 years ago. Every building that company did lost like 10 6 foot ladders. That were new at the beginning of the job
[k6bhanx] (score 1, diepte 3) According to the multiple source ive read online it will not disolve it. Sure you can use it but wont do anything.
[k6bmobt] (score 1, diepte 4) Don’t believe everything you read. In my experience it works. It might not work on all foams but it worked on the ones I tried it on.
[k6auj28] (score 1, diepte 2) Should be OK if you hose it off.
[k69wvee] (score 1, diepte 0) Get a metal brush from dollartree
[k6b7wfb] (score 1, diepte 0) I set up a ladder to gain access to a roof via a hatch. Not five minutes of me being up there and my ladder walks.
[k6dfu3a] (score 1, diepte 1) I was using one one time and this temp guy working with us walks off with it. I come and take it back. Our ladders are numbered so I know it’s the one I had. He gets all riled up and shouts at me “hey man now I only have one ladder left and gonna have to keep moving this one!” What.
[k6bj3dl] (score 1, diepte 0) If I’m leaving mine unattended for a short while during the work day, I like to collapse it and tie a length of scrap 14/2 I usually have on me or nearby to use as a tie wrap. I wrap it around so it’s hard to open and use…hopefully deter most from using it.
[k6bsuxy] (score 1, diepte 0) We lock everything up anymore, even take the keys out of our lifts
[k6bt92q] (score 1, diepte 0) THIS is why there are Back Charges… Let the GC get the money from them.
[k6c84wg] (score 1, diepte 1) Money for what tho ?? U gonna send an invoice to insulation guys/drywallers for what amount ??? Just take the L, clean the shit out and move on
[k6c7xps] (score 1, diepte 1) Sorry bud but the mods are gonna ban u for that comment ..
[k6gi2le] (score 1, diepte 2) Let ‘em ;)
[k6hd2ti] (score 1, diepte 3) Hahah I share the sentiment brotha ..
[k6qmr0b] (score 1, diepte 4) Well, at least there’s 2 of us!
[k6cbmah] (score 1, diepte 0) Burn it off?  I suppose this is highly flammable, right?
[k6dd4fd] (score 1, diepte 0) Try baby oil or light sovent I chain my stuff up
[k691muj] (score 0, diepte 0) Tsk, geez
[k69c7xc] (score 0, diepte 0) Lock your ladders
[k6ax4zd] (score 0, diepte 0) Maybe put your own tools away
[k6dkjpj] (score 0, diepte 0) Karen
[k69yqsj] (score -2, diepte 3) Try a flap disc on an angle grinder for the flat portion
[k6c3lkz] (score -2, diepte 0) You sound like a pussy

