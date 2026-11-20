# Label-batch batch_0096

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
Schrijf het resultaat naar `batch_0096.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: l2u6t6, 169zf85, z2c6uw).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD l2u6t6 ===
SUBREDDIT: r/Frugal
DATUM: 2021-01-22  SCORE: 3022  REACTIES: 77
TITEL: The size 15 insoles were $9/pair. For some weird reason, the size 13s were $16/pair. According to the manufacturer, they can just be trimmed if they're too large, so I got the larger ones and trimmed them down
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gk86wok] (score 548, diepte 0) Good idea as long as the arch support isn’t much different. I can see the size 15 arches being longer/wider/taller than the smaller size and not good for your feet. I’m all about being frugal but you only get 2 feet and as someone who has arthritis and other foot injuries from running.... take care of them.
[gk89tqu] (score 179, diepte 1) This is the correct comment. Most insoles are better sized by arch location rather than foot size. You need to have the arch support in the right place. You can actually end up with a lot of chronic foot, knee, and hip issues entirely from wearing improper footwear. One of the most common ones is plantar fasciitis. I worked in a specialty running store and nearly every day had customers coming in with orders or prescriptions from doctors seeking out specific shoes or specific support, largely because they had previously been wearing inadequate or improper footwear. They end up spending WAY more than the extra $7 you saved by potentially buying the wrong insoles. Especially if you spend a lot of time with your feet, it pays in the long run to pay a little more and spend some time researching or finding the right footwear. However, if you stand in the heel cup and they feel like the perfectly support your arch, then great find. But, my suspicion is that arch will be too far forward and possibly too wide.

[https://www.mayoclinic.org/diseases-conditions/plantar-fasciitis/symptoms-causes/syc-20354846](https://www.mayoclinic.org/diseases-conditions/plantar-fasciitis/symptoms-causes/syc-20354846)
[gk88d8j] (score 163, diepte 0) The arch still has to actually rest in the right place and support your arch. Unlikely (but not impossible, I suppose?) this applies with a pretty big sizing difference.

I don’t think insoles are the right place to try to save $7... such small savings for something that could have big consequences.

You are in “cheap” territory here. Not frugal. Possibly to the detriment of your health and a correct purchase later down the line, with maybe more doctors visits to boot.
[gk87v9j] (score 67, diepte 0) But the arches are different....
[gk8g02b] (score 37, diepte 0) Never cheap out on things that touch the ground: Shoes, Tires, and your Bed. It sounds like this is something that may seem like it works but likely will go bad quickly if the arch support isn't in the right place.
[gk8f8w9] (score 35, diepte 0) Please please please make sure the arch support is in the right spot
[gk9g3s5] (score 26, diepte 2) Do you have any link to information on how a shoe SHOULD feel? I've come up short and go nuts finding new shoes. 

Size 13 so options are limited as is. 

But should I feel all my weight on the arch? Should it be there but just barely touching? Merrells for instance always feel like my heel is touching and my balls of my feet are on a piece of pipe, I'm just assuming that's a bad thing but they're a respected company.
[gk8kvu6] (score 26, diepte 0) $7 is money well spent to make sure you have the right insoles for your feet and as other comments have pointed out you may not be supporting your foot properly. This isn’t a frugal but it’s a “penny wise pound foolish” buy with potential foot pain being the pound foolish implication
[gk86me3] (score 22, diepte 0) Do they not do multi-size insoles? The only non-medical insoles I've ever bought just come in all sizes and you cut them at home.
[gk8d7fu] (score 20, diepte 0) I save even more money by not wearing shoes at all.
[gk99ps0] (score 19, diepte 3) Not OP but I like SuperFeet. Their original green line were made for Appalachian Trail hikers (and so I have those in my walking shoes) but they have a wide variety of shapes, levels of arch support, and sizes. They make some great 3/4 length ones that are designed to be slipped in and out of different shoes without needing to size them. I love those.
[gk8ehir] (score 18, diepte 0) Its also not weird that the more common size was more money. It's called supply and demand. Same thing happens with shoes all the time, I wear a 14 EE, and when I find them at regular stores, they are cheaper, because they need to get them off the shelves since they sell slower. But lots of stores don't even stock above a size 13, and require me to special order my shoes.
[gk86udb] (score 17, diepte 1) Yeah! I'm used to cutting down insoles for shoes when I worked retail and needed to replace them every few months:')
[gk8kd8c] (score 17, diepte 2) I don’t think those are supposed to touch the ground
[gk8jckh] (score 16, diepte 1) Condoms too
[gk92sd3] (score 15, diepte 2) Perfect comment. 

Question: If you were going to throw better insoles into sneakers, like Vans / Chucks do you have a recommendation for something that is both low and good? 

Do you have a favorite overall brand of insole?
[gk8lihm] (score 10, diepte 0) Invest in quality footwear, not in aides to make shitty footwear.... More shitty?

This isn't a frugal hack, it's asking for a problem down the road.

Poor man's boots theory and all that stuff too.
[gka0l2z] (score 9, diepte 2) I have moderate plantar fasciitis and using store bought insoles only worked for a short period of time. I ended up getting custom insoles at two different places and they're covered under my benefits. I can't stress enough that custom insoles are worth every penny. Yes it's nice to save money, but having chronic foot issues is no joke. Save your money in other areas. I also have dedicated work shoes (clogs) and they have helped me so much and I rarely get any foot pain now. They're also great because I can wipe them down after taking care of covid patients.
[gk902g9] (score 9, diepte 2) Congrats to you, and condolences/congrats to the lucky/unlucky lady.
[gk8a9iy] (score 7, diepte 2) Looking again i think these are arch support insoles so I'm a bit wrong lol.  I just like buying nice warm fluffy insoles to keep my toes cosy
[gk8i1uk] (score 6, diepte 1) In summer I only wear one pair of certain sandals to go shopping or if I’m driving. All other times, *fuck shoes.* I’ll bring some with me if I’m gonna go inside someplace but barefoot allll the way. I got an extra bone in each foot and I dread buying new shoes. 

So, I save money by having weird feet and wearing my shoes to the bitter end when I wear them at all.
[gk9ut0a] (score 6, diepte 1) Unless it takes away from my working hours, my free time is free. (To some degree at least)

There are some problems with this post but this isn't one.
[gk8p927] (score 6, diepte 0) No weird reason.. demand drives the price.
[gkaenk3] (score 5, diepte 2) I went to a local Fleet Feet franchise and got fitted and it was one of the best things I ever have done for myself in my life. Now I know I need a stability control sneaker, and my favorite has been Brooks Adrenaline GTS. Always telling people to just go get properly fitted and stop complaining about poor fitting shoes.  


They also fitted me for the right style of SuperFeet insoles for other footwear that is close but needs more of an arch.
[gk9z56t] (score 5, diepte 2) Its not crazy to trim off a little foam.  Some of these comments are the end of the world is coming.
[gk8ztqm] (score 4, diepte 1 OP) I've seen it both ways. These ways for whatever reason come in each size
[gk8aos9] (score 4, diepte 1) Absolutely! And I know these I soles are commonly recommended for arch pain.
[gkaede8] (score 4, diepte 3) The ground is cleaner than most places I've put condoms.
[gk8gx79] (score 4, diepte 0) If this took you 20 min, it’s equivalent to $21/hour. At 30 min it’s only $14. Be cautious of being frugal with you money and spending your time
[gk9nu0a] (score 4, diepte 0) Save dollars now destroy your feet for years lol. Your typical frugal poster.
[gk9x3mv] (score 4, diepte 0) for flat feet ladies who work long hours on ur feet. 11$ walgreens insoles memory form top and gell on the bottom...best eva
[gkad9zl] (score 4, diepte 0) This is stupid. The arch support isn’t going to be correct. What a waste of money.
[gkezw5u] (score 3, diepte 4) I completely agree with Superfeet. Unlike other insoles, they focus on support, rather than the soft cushion that most other insole manufacturers do. Soft cushy shoes might feel nice, but are not necessarily good for your feet.
[gk9o1jf] (score 3, diepte 1) yep, the trimming thing should really specify that it's intended to get the insole to fit in the shoe if its the right size but just barely doesnt fit in the shoe
[gk8hrxl] (score 3, diepte 1) Maybe r/MaliciousCompliance ?
[gkaosq3] (score 3, diepte 1) Chairs also fall into this category.
[gk90qon] (score 3, diepte 1 OP) It took about 3 minutes
[gk9gb8u] (score 3, diepte 0) There's a difference between being cheap and being frugal...
[gk8aj06] (score 2, diepte 3) Ah haha:) I have some of these same ones OP has, I usually have to cut them to fit the specific shoe anyway!
[gka053h] (score 2, diepte 3) I have very bad feet. Crushed my right heel, pins and screws, luckyish to still have foot. I have tried all of the popular insoles on Amazon after being unhappy with custom orthotics. My favorite are EASYFEET on Amazon.
[gk8bf0e] (score 2, diepte 0) I believe there's a subreddit called passive disobedience or something. This was gut-bustingly hilarious to me.
[gk8mjp8] (score 2, diepte 1) Also very common with queen sized mattresses and sheets, they are cheaper often than full/twin sized.
[gk8w2ak] (score 2, diepte 0) Seven dollars!
[gk9ifs7] (score 2, diepte 0) We're did you find this deal, because I wear a size 15.
[gkay2r4] (score 2, diepte 1 OP) I'm finding them very comfortable and supportive. I've been having problems with plantar fasciitis and tendinitis in my feet and they're making a big difference
[gkb77rc] (score 2, diepte 0) And those of us who need those freakishly large sizes aren’t sure whether to be happy that you’re increasing the apparent market size of large shoes or mad that you’re buying up the very hard to find sides.
[gk8k0oo] (score 1, diepte 2) Haha the hero! On second thought it doesn' really apply but thankyou! That was it!
[gkeopd7] (score 1, diepte 4) Then you clearly missed the whole point of the argument, which is that the more common stuff is more expensive, not the other way around. That's why the size 13 insoles was more expensive than the size 15.
[gkav97c] (score 1, diepte 4) dont put OPs mum down like that man
[gk8hwsu] (score 1, diepte 0) Dr.sholl’s was the move
[gk8ka4h] (score 1, diepte 0) Unless you’re like me and accidentally cut an insole for my work shoes a little too short. For a year my big toe was not supported.
[gk8n3i6] (score 1, diepte 0) Have you tried growing larger feet?
[gk8z319] (score 1, diepte 0) My mom just buys these insoles that have guidelines for cutting in the size you want, pretty neat.

They're cheap though, so not really super comfortable, but they work.
[gk984qf] (score 1, diepte 1) If you have a shoe with a removable insole, take it out and trace it onto the new insole- perfect size and shape. shoes of the same size aren't all the same shape
[gk9bkhn] (score 1, diepte 0) Good clear thinking!  Do these help add cushioning without creating other problems?  Looking for solutions.
[gka2x6c] (score 1, diepte 0) you should look into Japanese dollar stores.
[gkaao8o] (score 1, diepte 0) How many pairs of shoes do you own?
[gkaum7y] (score 1, diepte 2) Well, how many are you buying insoles for?
[gkarmj7] (score 1, diepte 0) Did the arch still end up in the right spot?
[gkawzc4] (score 1, diepte 1 OP) yep. Feels great
[gkaxh9v] (score 1, diepte 0) Just bought these. How are they?
[gke0cfp] (score 0, diepte 3) That's exactly what I said. Queen stuff is cheaper because it's more common.
[gkeu054] (score 0, diepte 5) It's not universally true though, sometimes common stuff is less expensive because its made in larger amounts, so there's economy of scale, and the less common stuff can be more expensive because not as much of it is made.  Just as an easy example that's right in front of me, QWERTY keyboards cost as little as $10, whereas a Dvorak keyboard typically costs more like $100 if you can even find one, because the former is cranked out by the tens of millions, and the latter has almost no market share at all.
[gk9twrr] (score 0, diepte 1 OP) Amazon
[gkaczdf] (score 0, diepte 1 OP) 3.	Why?
[gkax2ac] (score 0, diepte 3 OP) 3 pairs for now
[gkaywqu] (score 0, diepte 4) If I had three pairs of shoes, and I knew one of them I would want to keep, I would want insoles specifically designed for that size of shoe, rather than telling a random person to take an insole not designed for my foot size to cut it for me to make it work.

Invest in your shoes. More than a coat. Come any season, you have to walk. That 5 bucks you are saving now can be a back surgery in 10 years

edit: invest sensibly. But seriously: save 15 bucks on all your footwear to wear down your feet and back and ruin your foundation, in turn causing major health problems?
[gkanaqd] (score 0, diepte 0) They’re priced higher cuz there’s more size 13 than size 15 people.
[gk9lvbo] (score -1, diepte 3) Dr scholl Wal mart gel knockoffs are great
[gkb8vog] (score -1, diepte 2) You gotta be kidding. Queen is by far the most common size for a bed.
[gk7xs3m] (score -4, diepte 0) Hey gianthooverpig, thank you for your image contribution! We like to have discussions here on r/frugal. To avoid your post being removed; 

**If you're posting something you made**, please leave a top-level comment under your post explaining how or why you went about it, how much it cost, how much time it took, etc., and share the recipe or materials needed. 

**If you're posting a general image**, please leave a comment explaining how it relates to frugality and any other details you'd like to share! Thank you for participating in r/frugal!

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Frugal) if you have any questions or concerns.*
[gk7zdnu] (score -4, diepte 0) Well done!
[gk85fdg] (score -5, diepte 0) Yeah, that’s the spirit!
[gk8r1xl] (score -8, diepte 0) I was looking at a premium yoga mat (27.00$) that had a clearance price of 7.  I thought hmm, I could cut this up into insoles.  It looked nice, foamy and thick.  Anyone use their own "homemade" insoles?
[gk8gr1m] (score -10, diepte 0) A flawless frugal post. Kudos to you.

=== THREAD 169zf85 ===
SUBREDDIT: r/BarefootRunning
DATUM: 2023-09-04  SCORE: 0  REACTIES: 76
TITEL: Zero drop shoes fucked up my foot. Be very, very careful when transitioning into any type of zero-drop or barefoot running shoe. Learn from my foot pain. This has cost me big.
POST (source_id=post):
About two months ago I developed Plantar Fasciitis from ONE, 3km run in my, at the time, new Altra Escalantes:  [https://www.reddit.com/r/BarefootRunning/comments/154seda/foot\_pain\_after\_first\_run\_in\_altra\_escalante\_3s/](https://www.reddit.com/r/BarefootRunning/comments/154seda/foot_pain_after_first_run_in_altra_escalante_3s/)  
And it STILL hasn't healed.   


I had worn barefoot shoes before; these weren't even barefoot but zero-drop with foam cushioning; I'd done a fair bit of reading about barefoot running before, and at no point came across anything advising to take it any slower than I did; searching Altra Escalante and Plantar Fasciitis for me, only provides results suggesting that these shoes PREVENT or CURE plantar fasciitis, not that they CAUSE it; my average run is 5km; I already walk around the house barefoot all the time, and do all of my other exercises (strength and flexibility) barefoot; I didn't push very hard, or run very fast, but I noticed some mild discomfort developing throughout the run at about 3km, and so stopped and walked the rest of the way.   


Before that I was breaking my 5km records, and generally appreciating the fuck out of having running as a stress management tool, as I'm currently going through something really horrible.   


It was my main coping resource, and I've been without it for 2 months when I need it the most.   


I feel like zero-drop/barefoot shoes hoes should have a literal warning on the box, because this has seriously cost me, and I don't want others to needlessly suffer.   


Feel free to tell me what I did wrong so others can learn too, but as it stands, if I was selling these things, I'd put as many warnings about the place as possible to prevent needless injury.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jz4oegp] (score 42, diepte 0) Basically all advice for transitioning to barefoot is "take it slow".  It doesn't sound like you did that.  Your post sounds like you bought some minimalist shoes and ran 3k.  Yeah that's gonna hurt.  So get some water bottles, freeze them and start rolling your planter fascia.
[jz58sd5] (score 14, diepte 2) Sounds like you brutally misunderstood what "take it slow" means.
[jz5eqla] (score 14, diepte 2) Dude what?  You were like "I ran 2 miles and now my feet hurt", as though that was advice anyone gives. I know you are now saying you "took it slow", but nothing in this post or the other post you linked says that.  Give me a break.
[jz4v10e] (score 11, diepte 0) Shoes do not cause or cure PF. They are one piece of a puzzle. PF is caused by weakness and or imbalance of foot muscles, which can be caused by time spent in more traditional shoes, or be a downstream effect of imbalance farther up in the system. Please find a physical therapist who is confident in treating PF and does not feel that shoes are the only thing that matters.
[jz5h201] (score 11, diepte 0) So you say it’s the zero drop shoes, but realistically it’s all the heeled shoes you’ve been wearing your whole life, and possibly some bad luck, that are the culprit. 

Barefoot shoes should have a warning? Traditional shoes should have the warning. They’re the shoes that immobilize our feet and cause our bodies to compensate in painful ways. If a kid gets minimalist shoes, the chances of them developing A LOT of ailments goes down compared to a kid you live in trad shoes and never transitions. 

You say that people can feel free to tell you what you did wrong, but then you’re not taking it well. 

You made a mistake, got injured, and it fucking sucks. I feel for you.
[jz4n7yd] (score 10, diepte 0) I think the transition can be much faster if you have a lot of daily steps, i do up to 20k steps per workday and never had any issue switching cold turkey form one day to next (just some sore muscles). Also multiple other coworkers did the same, no issues from anyone. Did you ever had any problem before? I also suspect that everyone who already ran before (with "normal" shoes" might have more trouble then someone who never ran. source: me, i never ran in my life till recently, first run ever (about 1 year ago) was 16k - one week sore muscles of hell, but nothing else, recently first time 60k, nothing bad from this even though i didnt really train lol
[jz6kf6h] (score 10, diepte 2) ...You replied to someone with just the rule that says not to reply to someone with just a rule.
[jz5ir4p] (score 7, diepte 0) Huge difference between barefoot running and the zero drop shoes you wore. You had enough cushioning to run much further  and with poorer form than you should've, if you were properly barefoot you would've felt the warning signs prior to getting injured.

Also if one run caused such an injury you were already right on the edge of developing one.
[jz71f35] (score 6, diepte 3) Guess he didn't spot the contradiction.
[jz8ahw0] (score 6, diepte 0) I ran in Altra for about a year. Developed serious IT band issues in both legs for about the last 3 months of that year. Switched exclusively to Vivobarefoot roughly 8 months ago without any sort of transition and have had virtually no lower body injuries. My calves were brutally sore the first month and are now significantly larger than when I started. I ran a 4:04 marathon two days ago. YMMV.
[jz9cleq] (score 6, diepte 0) Funny, I had the same experience following my purchase of the altra escalantes as well. First zero drop shoe and it completey sidelined me for a year.

I lacked the tib post & hip abduction/lateral rotation strength to check the over pronation that was now happening with the new shoes.
I ultimately had to shelve the shoes for now and find something more stable while I dedicate time to strengthening.
When you revisit minimalist footwear down the road, I'd suggest going truly minimalist (xero, vivo, etc) and start out with a few hours a week just walking/running errands in them.
[jz4piqk] (score 5, diepte 0) In my pre-minimalist (unelightened) days, I had a pair of Hoka trail shoes that bothered me. Went and got a pair of superfeet insoles and took for a 5 mile run. Instant IT band issue that persisted for months until the minimalist/zero-drop change resolved it. 

Your experience definitely sucks OP, but I guess I am sharing to illustrate that any transition may have issues. Hopefully you get better soon!
[jz8fbcr] (score 4, diepte 4) I hope you feel better soon.
[jz9bwpp] (score 4, diepte 2) take it slow, means start with walking, so that you strengthen the weak parts of your feet, ankles, knees, hips, and work on mobility as well. this should be done before whole hogging it for everything. that length of time varies for everyone since we all live in different bodies with different mechanics. it should not be a warning to never use a certain tool. it didn’t work for you, or your methods, but please don’t condemn what has helped many, many people. kindly. and hopefully you’ll be back in your new balance soon.
[jz4t26a] (score 4, diepte 0) I hope you can heal quickly. Plantar fasciitis is a tough one. I sympathize with you loving running and being unable to do it right now.

My first instinct is to criticize something you did, because this is the internet. But I don't think that is very helpful. 

The Altras are big and squishy though so I don't think it's fair to call it a barefoot shoe. You probably would have been better off in a barefoot shoe or sandal because you would have received a lot more feedback from your body about anything going wrong.

To really have an idea what went wrong we would need a lot more information about you and your training, but it's not important. Your feet weren't strong enough for what you asked from them. 

Now just focus on recovery. When it's time to start again maybe volume walking in barefoot sandals can help to strengthen your feet and prepare them. Actual barefoot running is great too, just a few laps of a running track every day can really help your form.
[jzeegig] (score 3, diepte 1) same here: 20k steps daily goal keeps my feet strong/conditioned between big runs
[jz4sou4] (score 3, diepte 2) I did zero research on barefoot running about ten years ago and just started running on pavement in vibrant 5 fingers. Cost me big time. My feet were absolute junk for months.
[jz4txfu] (score 3, diepte 3 OP) That's what's frustrated me a bit, is that, as far as I'm aware, I did more research than the average person, followed the advice and still got an injury.
[jz4uxq3] (score 3, diepte 4) I swear that the varied terrain that trails and hills provided definitely helped me acclimate. Definitely frustrating.
[jz4u3v9] (score 3, diepte 0) I mean, how were you running?

Most people run heel to toe rather than with a midfoot strike, if you were doing that I could see it possibly causing pain

How strong are your feet in general? 

Lots of variables at play, imo it's not as straight forward as it might seem
[jz5cejc] (score 3, diepte 2) It's too much toe strike the does it. I had been running with barefoot shoes for over ten years perfectly happy with mid foot landing. Somehow I got convinced that I need to be a lot more pronounced on toe first then did a half marathon - planta fasciitis for about 18 months!!! I feel your pain.

The only thing that helped was smaller cadence and exercises posted on Instagram by @thephysiofix (Dr Stacie Barber) . That was after two different physio therapists including shockwave therapy.

But essentially the cause was me changing from a mid strike to very high toe strike. 

Fix was - keep load and keep barefoot shoes, lower cadence and exercises by physio fix on Instagram. Once I combined those recovery was fairly sudden. On physio fix look through all the posts looking for plantar specific.
[jz9epmu] (score 3, diepte 0) Any change in shoe style can cause injury. 

As far as facitis, there's info all across the board out there. Some say go minimalist, some say go ultra padded with orthotics, arch support and heels. So maybe be more thorough in your research. All shoes have their magic pill schpeal, and theres usually some truth and some exaggeration involved. No shoe is magical, and any shoe can exascerbate injury. 

By your logic ALL shoes should have a warning list of the potential injuries people get while running. I got a bunion from ASICS, and knee problems from keens; I still don't think they need a warning. It was my bad for overdoing it in a shoe that didn't work for me. They probs work just fine for someone else. 

Live and learn.
[jz4qh2f] (score 2, diepte 0) I had a real difficult time transitioning.  The thing that worked for me was trail running and hiking. At first I would hike briskly and only run the hills. Now 4 to five mile runs. Feet have never felt better.
[jz4xsmk] (score 2, diepte 0) I gradually switched to barefoot (BF) running over several years, taking it very slowly. Although I would have liked to progress faster, my calf muscles needed extensive conditioning and suffered a few tears because I didn't listen to them initially. Fast forward a few years, and I can now comfortably run 20 to 30 miles with only fatigue as an issue. Despite the challenges, it has been immensely rewarding since I used to experience shin splints and sore knees when running in traditional shoes.
[jz7zyek] (score 2, diepte 1 OP) That's what I'm hoping to get to. The only pain I occasionally experience with normal shoes was when I was increasing frequency of running a lot, and getting some mild knee pain; this was the motivation to get into minimalist running shoes.
[jz52z57] (score 2, diepte 0) So wait…you were injured and then tried to cure yourself with barefoot shoes?

Lmao. Bro. Common sense.
[jz55249] (score 2, diepte 0) I dealt with a stretch of PF when I transitioned. It was mostly about my calves being disproportionately stronger than my feet. As my feet strengthened it stopped being a problem. Overdoing it is absolutely the enemy.
[jz5jzqs] (score 2, diepte 0) Since you're mentioning stress, it could also be TMS :

https://www.tmswiki.org/ppd/Plantar_Fasciitis
[jz6bjdu] (score 2, diepte 0) Quit being a baby
[jz7yuc8] (score 2, diepte 1 OP) Yeah. People don't seem to be acknowledging that part of the post. I spend most of my time fully barefoot at home, and have worn barefoot shoes on and off over the years.   


No heel striking, slow running/jogging, stopped at the first sign of pain, following the advice given, but still got injured. Seemingly pissing a lot of people off who are either ideologically attached to barefoot running, or just like condemning people.
[jz8qlwh] (score 2, diepte 0) They probably weren’t wide enough to allow full toe splay. This happened to me while wearing Vivo’s and Xero’s. Once I found some that didn’t hold my big toe in (I still haven’t found any that are perfect, yes I’ve tried Softstar) I was able to engage my foot arch and glutes for the first time in my life. My PF then went away. This literally took me 3 years and many barefoot shoes to figure out. Actually 20 years since I wore stability shoes use for most of them, even when taking a piss in the middle of the night. This fit issue is never talked about and I agree can be dangerous. Barefooters think it’s all about the thin sole and also think because their heavily marketed barefoot shoe brand is wider then their old Nikes it must fit right even though it’s still too narrow or not shaped right. Everyone’s foot shape is unique. But you don’t even understand why you got PF and I don’t blame you as most the info out there sucks. I suggest getting sandals first and go from there since you won’t have anything holding your toes together. Do calf raises barefoot and one legged strength training.
[jz9wkax] (score 2, diepte 0) "I was a dumbass and didn't follow the transition slowly advice, it's definitely the shoes fault"
[jz4n5jb] (score 1, diepte 0) Get better running from and ride a bike until it heals.
[jz4qgzz] (score 1, diepte 1 OP) Thank you. I went slow, but not slow enough. Attempting to help others prevent similar issues.
[jz4sdhu] (score 1, diepte 1 OP) Noted. I don't intend to write off minimalist running, so will ponder this in how I approach it post recovery.
[jz800ym] (score 1, diepte 5 OP) Will add walking trails to my list of things to test out. Thank you.
[jz4t3ya] (score 1, diepte 0) https://www.reddit.com/r/BarefootRunning/comments/cw6fhd/what_shoes_are_best_to_start_transitioning_none/
[jz4v1uw] (score 1, diepte 1 OP) >I mean, how were you running?  
>  
>Most people run heel to toe rather than with a midfoot strike, if you were doing that I could see it possibly causing pain

&#x200B;

I've been specifically consciously running with my normal running shoes, training mid/toe striking for a few years prior to this, so definitely not heel striking. 

&#x200B;

>How strong are your feet in general?

&#x200B;

As above, I've worn full on barefoot shoes whilst walking, and dancing for hours with no issue. I never wear shoes/slippers in the house, and being an introvert who only goes outside to read in the park or run, I spend a lot of the time walking barefoot. So, I'd imagine better than average (again, that's what's frustrating about this). 

&#x200B;

>Lots of variables at play, imo it's not as straight forward as it might seem
[jz7zqp7] (score 1, diepte 3 OP) A few bits of advice have recommended to keep up with barefoot shoes, but I'm understandably anxious about wearing them, and also super put off from this community re: the current top voted responses to this post.
[jz89kpt] (score 1, diepte 4) I totally get it - plantar is a bitch. I wanted to do anything to get over it. Have a look at that Instagram account though (they don't preach shoes , it's all physiotherapy). Also, the best footwear for pain relief while walking was the Birkenstock beach shoes type (Arizona EVA or something like that). I know it's not long term but it is nice to have some pain relief while walking. 

Obviously everyone is different though, if barefoot doesn't work for you then they simply don't. I feel I can't go back to other shoes as I tried barefoot shoes because of back and hip pain. Been in this style of shoe for 14 years now. Plantar after 10 years was my only issue, and I don't think it was the shoe - it was more to do with the change in action too rapidly (I think). For me working out to get back to pain free walking it wasn't worth going back to - back and hip pain. But if that isn't an issue for you then do whatever works.

Good luck.
[jz9igub] (score 1, diepte 5 OP) Thank you.
[jzi5a2l] (score 1, diepte 1) I got it from skating in new trail running shoes on hard ground. I'm used to skate 100km without a break and without any issues. So wrong balance can't be the problem. The shoes felt like they shifted my foot contact area to the inner side after several km
[jz50os4] (score 1, diepte 0) Sorry to hear of your injury. Definitely ease into the shoes by doing a few long walks first, and then running at a really easy pace for a really short distance first. I've had some Achilles issues from running, but that's usually been because I've pushed too hard after a long layoff.

I didn't start running until a few years after I got my first pair of Vibrams, so I guess I'm lucky that I didn't have to make a big adjustment to my running form. I just did what felt natural in the VFFs.
[jz7zfud] (score 1, diepte 1 OP) Thank you.
[jz563cu] (score 1, diepte 1 OP) >So wait…you were injured and then tried to cure yourself with rapidly “transitioning” to barefoot shoes?  
>  
>Lmao. Bro. Common sense. Zero drop didn’t fucked up your feet, you did.

  
No. Please read posts before commenting on them. The reason I bought the zero drop shoes was to PREVENT injury. Having read about knee injury issues, etc. I thought it'd make sense to start transitioning to barefoot/minimalist/zero drop shoes.   


I had no injury whatsoever at all.   


"Before that I was breaking my 5km records, and generally appreciating the fuck out of having running as a stress management tool, as I'm currently going through something really horrible."  


I followed the advice. I took it slow. I ran a shorter distance that usual. I didn't heel strike. I watched out for discomfort. I'd worn barefoot shoes for years prior. At 3km, I experienced some mild discomfort and stopped, and that mild discomfort quickly turned into enduring Plantar Fasciitis that has lasted 2 months.
[jz54if5] (score 1, diepte 0) I’m a fan of Altras generally, but imo Escalantes suck. WAY too squishy. Squishy is bad. Squishy = unstable. Squishy causes you to naturally push down with greater force, searching for the stability.

Fine for walking, terrible for running.
[jz567pd] (score 1, diepte 1 OP) Yeah. Currently doing calf/heel raises to strengthen my foot and calves.
[jz5c5me] (score 1, diepte 0 OP) Thank you to all the nice commenters!
[jz8093q] (score 1, diepte 1 OP) >You say that people can feel free to tell you what you did wrong, but then you’re not taking it well.

I guess I was naïve to expect that it'd be done in a non-judgemental, kind way.
[jz5w9m5] (score 1, diepte 0) Sorry for all the downvotes.. you’re just warning people to take it slower. For me it took years before I could run without calf pain or shin pain. Occasionally I still will get knee or top of foot pain but I stop once I feel that. I was never a runner before so it was easy for me to transition because I didn’t have an urge to go out and run even a 5k, running a mile at first barefoot was good for me. Now I can do up to about 4 miles at a time, but like I said, this was over the course of 3 years.
[jz7zdnc] (score 1, diepte 1 OP) Thank you.
(33 reacties met lagere score weggelaten)

=== THREAD z2c6uw ===
SUBREDDIT: r/pharmacy
DATUM: 2022-11-23  SCORE: 33  REACTIES: 76
TITEL: Shoe recommendations for retail pharmacists
POST (source_id=post):
I am a new grad in the retail pharmacy setting. I am now on my feet for 12-13 hours a day….While I have worked in the retail world for the last 6 years (started as a tech, then an intern during pharmacy school) my hours were never as long as they are now that I am a pharmacist. Even then, I felt like no matter what sneakers or shoes I tried, my feet would still ache by the end of the day. 

For the last year I’ve worn crocs and I love them — my feet don’t hurt anymore BUT I have found that my hips are starting to hurt a lot more and I am thinking it’s because, while the crocs are comfortable on the feet, they aren’t offering enough support for my hips & back….

Looking for recommendations for shoes that have good support while also still avoiding the aching feet at the end of the day

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ixfqxea] (score 49, diepte 0) Hokas plus compression socks!
[ixfrfyi] (score 28, diepte 0) Hi. Not a pharmacist, but a nurse (don’t hate me lol I’m not one of the dumb ones I swear). 
I wore crocs exclusively for a long time until I realized one day that my feet hurt when I WASN’T wearing them. Like even barefoot my feet hurt bad until I put the crocs back on. That can’t be healthy so I stopped wearing them. It took a while for my feet to feel better. Like weeks or more. I got fitted for shoes at a running store- I don’t run but they analyze your gait and recommend a shoe based on how your body moves and the way your feet move when you walk. They recommended a pair of Brooks for me and they’re suuuuuper comfy. But everyone’s feet are different so your (literal and figurative!) mileage may vary with any specific shoe.
[ixfvzht] (score 15, diepte 0) Hoka bondi, but get two pairs of shoes so one can rest and decompress while you wear the other
[ixg32rt] (score 15, diepte 0) Dansko clogs
[ixfx9yp] (score 11, diepte 0) I switch every day. I have two pairs of Hokas, a pit of Reebok nanos, and Nikes. Switching every day is key.
[ixgj3p8] (score 11, diepte 0) Real pharmacist answer is that Voltaren goes unmatched as the best footwear
[ixfws17] (score 9, diepte 0) Im ultraboost pilled
[ixfw1se] (score 8, diepte 0) For business casual, I generally wore Clark’s when I worked retail. I teach now and sometimes spend about six hours on my feet walking back and forth while lecturing and on those days, I wear Allbirds Treerunners or Ecco’s. The Ecco’s are great especially if you have wider feet. Would also look into Mephistos if looking for something a little more dressy.
[ixfrppc] (score 6, diepte 0) Shoes that worked for me: cloves and ultraboosts
[ixfrppo] (score 6, diepte 0) Hokas
[ixg23b5] (score 5, diepte 1) Do you have a particular style of Hoka you can recommend?  When I search "orthopedic" on their website, I get 77 results!
[ixg57lb] (score 5, diepte 0) Brooks + compression socks! I will NEVER work without compression socks now - makes such a difference!
[ixgb244] (score 4, diepte 2) I like the Bondi
[ixh8xme] (score 4, diepte 2) I wear the Bondi style, but I think it depends on if you have low or high arches. A lot of time track shoe stores will assess how you stand and walk and can make a recommendation for you about the style. I would just buy their recommendation online because they are usually cheaper!
[ixgxm20] (score 4, diepte 1) I wear the Bondi SR, leather outer, all black.
[ixhkmsv] (score 4, diepte 1) Hey I have mad respect for kind nurses! Thanks for all you do! :)
[ixmmw8g] (score 4, diepte 1) I used to argue with nurses at work, then I married one. Now I argue with nurses at home too. ❤️
[ixg6kb2] (score 4, diepte 1) My converse are fucking up my feet real bad. If they work for you, you're probably the rare exception
[ixgj1qu] (score 4, diepte 1) Same. 6'4 220, my ultra boosts hold up best. I've tried new balance, which are great too, but ub's last longer.
[ixhk05x] (score 3, diepte 1) The compression socks make a big difference. Btw, Pro Compression is running a sale currently. They’re a little high, but the best I’ve found so far.
[ixhoflb] (score 3, diepte 2) Thank you!! I have similar love for my pharmacy peeps. I love lurking here, I learn so much! 
Also I’m way better about picking up my prescriptions on time now 😂😂😂
[ixg6su7] (score 3, diepte 2) Like I said it's probably an unpopular opinion and I'm already getting downvoted for it hahaha but it really does work for me. Just putting it out there for others to maybe try
[ixge8se] (score 3, diepte 3) I find Chucks to be great for my feet with a pair of basic flat insoles (store brand equivalent to Dr. Scholl’s original Air-Pillow insoles). Spouse, OTOH, can’t wear Chucks at all. It all depends on your feet. Your comment doesn’t deserve to be downvoted.
[ixg6yuf] (score 3, diepte 1) These are one of the few shoes I can stand in all day. My new balance are ok especially if I’m moving more but if I’m at a busy store and I’m one spot verifying for long times danskos are better
[ixg3gcz] (score 3, diepte 0) Vionic. I can’t sing their praises enough. Do yourself a favor, and wear compression stockings too!
[ixgvggt] (score 3, diepte 1) This. I prefer Firm compression level but it’s one of those things you don’t realize the benefit from since it’s preventative.

Compression socks everyday for me!
[ixh1irv] (score 3, diepte 0) Danskos
[ixh5269] (score 3, diepte 0) I have spent thousands on shoes for my husband.. the only shoea after 10 years that helped with his standing all day were Cloudnovas from on cloud. They are about 160$ but he is still using the same pair after 2 years and foot pain is gone. We also have active pairs that are amazing but the cloud nova for standing.
[ixhtv0r] (score 2, diepte 3) That's a good call; I really should visit one of those stores first.  Thanks for your recommendation!
[ixh4nz4] (score 2, diepte 1) Is this some well kept pharmacist secret? I have never heard of Hokas…..did I miss the day they handed them out? What makes them so special? (Cuz an overwhelming amount of people have said Hokas!)
[ixg4qxz] (score 2, diepte 1) I love my Cloves
[ixfu0tz] (score 2, diepte 0) Burkies by Birkenstock
[ixgkydm] (score 2, diepte 1) My aunt who is an OR nurse gifted me a pair of Dansko clogs when I started pharm school. Since I started working I love The XP clogs & compression socks. They look fine with scrubs 🤪.
[ixhfsqd] (score 2, diepte 1) I second this. Been a pharmacist since ‘97, in retail from 97-19 and wore Danskos. I also wear them in civilian time as well AND visited a podiatrist for inserts. Take care of your back and legs.
[ixi8300] (score 2, diepte 2) Well that’s a bummer. I’ll admit, almost rolled my ankle when I first got them. Had to get used to walking in them. Definitely can’t go faster than a brisk walk.
[ixgvck0] (score 2, diepte 2) Sockwell are my favorite
[ixg7qwj] (score 2, diepte 0) I’ve used Vionic and Brooks and both have provided support for my feet legs and lower back!
[ixgh8tp] (score 2, diepte 0) I wear just regular Nikes, with a Dr Scholls foot insert for arch support.  Until I started adding the arch support, 12 hour days would leave my feet aching.  These days, if my foot starts hurting I know it's time to replace the insert - every 4-6 months or so.
[ixgv8dp] (score 2, diepte 0) Hoka Bondi seem to be pretty popular these days but not my type of shoe. Any shoe that has a large surface area will be better at distributing weight. New Balance alternative would be the V3 More. New Balance alternative for Ultraboost would be 1080v12. 

Personally I like to wear New Balance 2002R (all around standing and moving) and 9060 (standing, has larger surface area on sole). I wear these depending on where I’m working (inpatient or retail) and rotate shoes everyday. 

Compression socks - Sockwell merino wool socks. I wore ProCompression prior to this but Sockwell is much more comfortable and lasts longer. Firm for me keeps the aches and pain away, something you don’t feel any benefit from wearing but definitely feel the repercussions from not wearing them. 

Insoles - whichever fits your needs. You do not need expensive orthotics. Change them out occasionally. I use Dr. Scholl’s Heel Pain Support due to insertional Achilles tendinitis. Works great for me.
[ixhmf3s] (score 2, diepte 0) Rockports.

Also highly recommend a new pair at least every 6 months.

I do 3-4 months.
[ixh95jd] (score 1, diepte 2) Honestly, almost all of the techs at my hospital wear them. I finally tried them, and it was like night and day. Would highly recommend if you are in the market for new sneaks
[iximhd1] (score 1, diepte 2) I'm not trying to force it on anyone. I'm not saying "hey do this because it's 100% effective". I'm simply putting it out there because the post asks for suggestions and I'm just stating what worked for me.
[ixgir68] (score 1, diepte 1) I came to say Clark’s! They have some cute styles. I really like the ankle boots, but wear Wallabees sometimes. They can get heavy for a whole day, so wear those more when I’m off.
[ixg05b8] (score 1, diepte 0) Altra Paradigm or Via Olympus
[ixhmajn] (score 1, diepte 1) Never wearing Dansko again, they gave me plantar fasciitis (so bad I had to go to an podiatrist thinking I had a bone spur) and I’ve know several peers who have either rolled ankles or broken ankles due to the instability in these shoes.
[ixivslf] (score 1, diepte 3) Super bummer. I’m not retail (I’m hospital) and go to rapid response and code blue calls though so running is a daily requirement.
[ixgb7my] (score 1, diepte 1) Brooks Walk Addiction are my current favorite
[ixgi5gq] (score 1, diepte 1) Do you use different compression socks in the summer? I tend to get too hot with them on in the summer.
[ixggumb] (score 1, diepte 0) I live and die for my hoka shoes. Alot of the pharmacists I worked as a tech in training swears by them
[ixgvjvk] (score 1, diepte 1) Insoles are just as important and many don’t realize this. You do not need fancy orthotics from the podiatrist.
[ixghsgv] (score 1, diepte 0) I heartily recommend against crocs to anyone even if they "feel" comfortable at first. Think of a a couch that's *super* comfy but you hurt like hell if you sit down on it too long. There are some things I like but for a pharmacy setting instead of recommending a particular brand, find a shoe store that caters to runners etc (not Foot locker in the mall). Tell them the situation and what you likely want to look for is a walking type shoe that leans towards comfort.
[ixhdxag] (score 1, diepte 0) Definitely HOKA!!!!!
[ixheo3t] (score 1, diepte 0) I bought like a slip on shoe of any kind. Some of the techs do wear Vans, crocs
[ixhjjen] (score 1, diepte 0) Skechers with memory foam or Brooks Ghost or Glycerin.
[ixhkt01] (score 1, diepte 0) OP: In the last 3 months I’ve don’t extensive research in this very topic . I’ve bought and worn 4 pairs of shoes and tested each thru at least 100 hours during my 12 hour shifts. Here are my results :
Hands down best pair - Nike ZoomX infinity run. Eastbay had a 50% sale (might still be going on) I copped a pair for $90. Worth it at $180 msrp. Most cushioned, comfortable sneaker, bouncy, my legs don’t hurt 1/20th as much after a 12 hour shift. Get these.

Notable mentions: New Balance 1080 v11 (8/10) , Brooks Glycerin 20 (8.9/10) , On Cloudmonster (7.5/10)
[ixhq15s] (score 1, diepte 0) My two-cents are OOFOS, they have a very deep cushion and high arch support. Of course, the support does eventually wear out and isn't replaceable like an insert would be. But they are very light-weight and breathable. I had previously been wearing Nikes with an insert, but started having major trouble with plantar fasciitis. Lots of arch and heel pain and tightness in my Achilles tendon when I get up.

The OOFOS have basically chased that away. I also own their open sandals at home or out and about in the summertime. Very squishy.
[ixhsto9] (score 1, diepte 0) Sketchers with Dr. Scholls insoles, adidas ultraboost, brooks are all shoes that have worked for me
[ixhuheq] (score 1, diepte 0) I vouch for my pair of white Vans Sk8 Hi-Tops.
[ixi1h17] (score 1, diepte 0) Brooks sneakers
[ixifwul] (score 1, diepte 0) For me it's it the shoe, but the insole.  Getting custom orthotics made was a lifesaver for me.
[ixo4m8b] (score 1, diepte 1) Same here. Years ago I had gotten a case bursitis and went to a podiatrist and got fitted for orthotics. 
My insurance paid for them and after a few weeks I got used to them and I haven’t looked back. No hurting feet or back issues since ( that was over 20 years ago). I will add to that good quality cushioning socks. I wear Addidas campus shoes and have no foot problems. The orthotics can be put into my other shoes ie. Hiking boots, sneakers, dress shoes, or whatever. Same comfort and support.
[ixihc1z] (score 1, diepte 0) Just got a couple of pairs of Dr. Scholls shoes that have been great and not at all expensive ($64.99 a pair at DSW). Black and brown and they can look casual or dressy. I like comfort but I’m old school enough to still like the shoes to look professional. It’s mainly the male pharmacists I’ve seen that’ll have a nice dress shirt and slacks and then a pair of clunky looking Nikes that don’t even match.
[ixisqr7] (score 1, diepte 0) birkenstock londons and addidas ultraboosts
[ixixn5u] (score 1, diepte 0) Cloves!!! Will not wear anything but them at work
[ixj7qly] (score 1, diepte 0) I've been on a journey with my work shoes 😂
When I got my first job in pharmacy as a tech I bought some dansko type clogs cos thats what all the nurses I knew wore. I was constantly rolling my ankles and one day, while walking to class in them before work, I took a step and the entire sole of the shoe fell off 😱
I ended up going to a shoe store on the way to work and grabbing the first pair of solid black shoes I could find. They were some off brand mr Roger type tennis shoes with no support and they were one of the best shoes I ever had.
When I passed my exams as a pharmacist, I bought myself the most expensive shoes I ever had til that point and got Nike running shoes. They were ok but gave out after about a year as the fabric had worn through. I tried Hokas but they compounded my lower back problems and I returned them after a week. I'm now using hightop converse sneakers (again, shoes with little to no support in the sole) and so far its been great.
A lot of the suggestions you'll find here are great, but really it depends on the person, everyone's feet are different, and everyone has a different thing they look for in footwear. For me, as close to barefoot as possible was what my back needed, for a lot of others a soft cushion or strong arch support is what's needed.
[ixjxqxn] (score 1, diepte 0) Hoka Bondi 7
plus “Power Step” orthotics 

this was recommended by several podiatrists for ppl that stand for loooooooong periods ,
waitresses, nurses, retail personnel
[ixk3qaz] (score 1, diepte 0) Merrell, compression stockings .
[ixk8jlj] (score 1, diepte 0) Dansko shoes are the best.
[ixftckl] (score 0, diepte 0) Maybe an unpopular opinion but Converse chucks really worked for me. My theory is that due to it being flat, my back doesn't have to conform to the cushion of whatever shoe I was wearing, if that makes sense. Used to wear running shoes by Nike and Adidas before that. But to each their own.

PS. New Balance Figs worked for me for a while but my feet started to hurt after a couple of months wearing it.
[ixgyogi] (score 0, diepte 1) I think you’d have to search pretty far to find a podiatrist or physical therapist that signs off on this theory.
[ixgyrcw] (score 0, diepte 1) Mitch Hedberg preferred Mr. Scholl’s.
[ixh5ui5] (score 0, diepte 0) Adidas is having stupid sales on eBay on ultraboosts, picked up 2 pair for 117
[ixha91i] (score 0, diepte 0) Ditch the crocs, you are correct they have too little support.  But compression stockings.  Knee height, athletic stockings are fine.  Don’t necessarily need medical grade.  Trust us old guys ;)

