# Label-batch batch_0128

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
Schrijf het resultaat naar `batch_0128.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1aso473, tjzw3h, 1f5jtw9).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1aso473 ===
SUBREDDIT: r/Frugal
DATUM: 2024-02-17  SCORE: 154  REACTIES: 67
TITEL: People with small feet- buy from kids section
POST (source_id=post):
Not sure if this has been shared before or not but I was researching for a good pair of sports shoes and found comparable size in kids section for much cheaper. And they had better colors than regular women's shoes!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kqrogqe] (score 160, diepte 0) It works for a few brands but trust me, most aren’t as supportive and will hurt your feet . Maybe for an occasional use but don’t do it if you are on your feet all day
[kqrsa4b] (score 93, diepte 0) This is good advice if you want some fun, colorful shoes to wear in situations where you won’t be walking a lot, but I definitely second what others are saying about support, wear, etc.! 

I used to do museum talks/demonstrations and one time a little kid interrupted my presentation to point out that she and I were wearing the same shoes, which was adorable 😂
[kqrnlj7] (score 52, diepte 0) Sometimes it works well but sometimes the construction of the kids sizes is different. Was trying to do this with Ugg boots and the sole was much thinner and there was less shearling lining the boot.
[kqrpxxx] (score 52, diepte 0) Sometimes the clothes at the GapKids are just too flashy. So, I am forced to go to American Girl store and order clothes for large colonial dolls.
[kqrou27] (score 43, diepte 0) Don’t, though, if you weigh over 100lbs or thereabouts. They’re engineered for a child’s weight, so you will wear them out faster. Get your daily shoes in the adult section and the fun ones in the kids’ section.
[kqs185a] (score 22, diepte 1) Kids shoes are poorly made, this tip seems not truly frugal just cheap. Buy a shoe 3x more expensive that lasts a couple years,  and it is cheaper than buying new shoes every 6 months.
[kqrxf32] (score 19, diepte 0) Normal sized woman here. I am a woman’s tee shirt sized medium. I started buying stacks of plain black tee shirts in the boys section sized XL. Much much cheaper, and the neck hole is not overly large, which fits my frame better.
[kqrnkzc] (score 16, diepte 0) If you have a larger foot you can also buy from the mens section and get what is most likely a better quality shoe and you will probably take a size that a lot of men don't take which means you can get it on clearance for a cheaper price. A lot of the colors are very similar too. Most men I know don't wear a size 8-9 mens which is what most women with larger feet can wear, bonus points if you are a size 7 mens which never sells so you can probably find those on clearance easily.
[kqs5jsc] (score 16, diepte 1) It took me a long time to realize that weight has a lot to do with how quickly shoes wear out.
[kqrolg7] (score 15, diepte 1 OP) Ah, that'd good to know. I'm not on my feet all day. But had I known, I would have bought a regular one.
[kqsiu1h] (score 14, diepte 0) Please don't do this. I have a lot of tiny women in my family, blood related and by marriage. My cousin's wife was an immigrant & the smallest of us, only 4'9" and a US women's shoe size 3.5. 

There are no stores in the US that sell women's shoes below a 5. We tried to help her find wedding shoes here but she had to have a pair ordered from her home country instead and it was very expensive. 

She would buy shoes from the kids section and it caused damage to her feet. They aren't made for the weight of an adult, and are built more cheaply with the expectation to be quickly grown out of and discarded.
[kqrr38q] (score 11, diepte 1) I recommend shopping from the men's section for boots in particular. I struggled to find good boots in the women's section. Most were designed for style rather than longevity, waterproof-ness, etc. Finally bought a pair of men's boots on sale and finally got all the qualities I'd been looking for.
[kqs458t] (score 11, diepte 1) Omg 😂 Angela? Is that you?
[kqsgat5] (score 10, diepte 2) It can be frugal, but it’s just niche. 

I work in an office sitting at a desk all day and have a pair of boy’s dress shoes that I’ve had in my rotation for years. 

Yes, arguably a nice pair of adult dress shoes would last longer, but I know I’d never actually justify spending hundreds on a pair of shoes for just sitting at my desk all day and the boys shoes aren’t really more expensive than a thrift store pair
[kqsa4er] (score 9, diepte 3) Yes, I wear a women’s size 7.5 and bought a pair of size 6 UGG slippers in kids size
[kqu72z6] (score 8, diepte 1) Same, a lot of them have fun prints or messages too. I’d rather wear a shirt that says “NASA” than “namastay in bed all day” or “wine o’clock”
[kqsrjop] (score 7, diepte 1) Yeah I tried be frugal once with shoes and got Walmart shoes… i actually think the soles were cardboard I could feel everything
[kqrubb9] (score 6, diepte 1) I'm that size, and when I downsized my shoe collection on eBay a few years ago almost all of them sold to people with male names.
[kqrxy9c] (score 6, diepte 0) Shoes *and* clothes
[kqs23h6] (score 6, diepte 0) women with petit frames working the trades, try the target kids section.... cheaper and durable clothes lol
[kqs32dy] (score 5, diepte 2) For some reason women’s work boots are so damn ugly. But if I go to the men’s section they are so much better looking. I’ve been doing this for years now lol
[kqs87w7] (score 5, diepte 2) Is a women’s size 6 small enough?
[kqsp3yr] (score 5, diepte 1) For this you would probably have to have a pair of shoes custom made. There are places in the USA that do this, but it is expensive and can take 6 months to get a pair of shoes. I also don't think they could make something like wedding shoes.

I would suggest a unisex shoe like vans, comes in all sizes and its made the same throughout the product lines.

Nordstrom rack sometimes carries womens shoes in size 4 and 5, but I don't think they go to 3.5. Nordstrom rack is the best shoe store for odd sizes of all articles of clothing.
[kqtuu4q] (score 5, diepte 1) This unsolicited advice comes from working with kids who had to wear orthotic devices that ranged in height from not seen outside the shoe to braces that ran from their toes to their hips. I was constantly looking for shoes that could hold up to rambunctious play, could be easily put on over AFOs, had color options and were overall functional for at least 6 months. 

Since you have lots of small footed people in your family that likely still need shoes, check out Nike air Jordan’s and any of the classic styles of New Balance kids shoes! Think leather & suede vs. stretchy cloth. If you’re in store, look for a shoe sole that can’t be folded in half like a taco. The size and width range of new balance is the best I’ve every seen in kids shoes!
[kqrvfvk] (score 4, diepte 0) Hey if the shoe fits....
[kqsb059] (score 4, diepte 0) And at thrift stores, check all sections--for boots, flannels, sometimes dress shirts.

The employees are not paid enough to notice the difference, so they frequently sort quickly or incorrectly.  Note also: there are no unisex sections, so they pick one.
[kqsb8e0] (score 4, diepte 0) Agreed this works better if you are a lightweight! Works fine for Crocs, I can easily wear a kids 4-5
[kqsfd3w] (score 4, diepte 0) I do this for “office” shoes when they’re mostly just decoration while I’m sitting all day 

But for actual use you’ll get more mileage out of shoes made for adults. 

Kids shoes are made cheaply on purpose because kids grow out of them too quickly for most parents to be able to spend money on higher quality shoes multiple times a year. And they don’t need to hold up for as long if kids are growing out of them anyways
[kqrz7pq] (score 3, diepte 1) Yes. I just did this for my last pair of shoes - I scanned through the womens' shoes selection, didn't see much I liked, and went and found a pair in the discount rack in the mens' section - size 8 mens - same as a 9/10 womens. And, since I \*ALWAYS\* need a Wide in womens, a mens Medium will just (barely) fit me.
[kqrrmdj] (score 3, diepte 0) And this might sound strange but women with size W11 and 12 might want to ask their Trans friends for tips about where to buy affordable comfortable nut stylish shoes...and for really fun flashy heels ask any drag queen friends. Seriously. I have done both of these things.
[kqrw2go] (score 3, diepte 0) I look in all the sections when I shoe shop cause I fall in the overlap of the smallest men’s and women’s sizes and the largest kid sizes. Never know what I’ll find!
[kqrw3nv] (score 3, diepte 0) I'm 5ft 2 and 115lbs. I participate in Community Theater while looking for a costume piece the costumer brought me to the girls section.  It's cheaper and I don't have to hem anything. It wouldn't have ever occurred to me, it works great for pants and skirts but not always for shirts or dresses because of bust size.
[kqrygi7] (score 3, diepte 0) I’m a womens 8-9 and in “Big Kids” size 6, slippers are way cuter in the kids section
[kqs4bs7] (score 3, diepte 0) I buy Skechers in the kids sections sometimes. (Size 7.5 women’s) My favorite pair of cheetah sneakers 😆
[kqsdb5m] (score 3, diepte 0) I buy kids' vans and docs
[kqsge6e] (score 3, diepte 0) My 19 year old never graduated from the boys section because his genetic syndrome has left him very small.   I find plenty of adult style equivalents for him in the boys section so I haven't had many problems.   I mostly get his clothes from Target and Old Navy but occasionally if I need something better quality I will shop Macy's.

He has special fitting needs for shoes.  I gladly pay extra money for an attendant to fit his shoes personally to him at locally owned children's shoe store.   They are more expensive upfront but overall cheaper long term because using them saves me time and from wasting money on the wrong pair of shoes (again difficult to fit) plus they only sale premium shoes and a pair of shoes from there easily will last my son at least 2 years but often much longer.
[kqsvbyh] (score 3, diepte 0) I do that, but know that kids shoes aren’t built for adult weight or for longevity. I still kids shoes because my toes are short and fit better with my arches on the soles.
[kqszhqg] (score 3, diepte 0) Don't do it!! Unless you are talking a pair of rain boots you were twice a year or bath slippers you wear a couple minutes a day.

Health is the one thing to not cheap out on and foot support and proper shoes are soooo important!

I repeat: Please do NOT do this, at least not with shoes you were a lot. And PLEASE don't get them from Walmart or similar either. There is a time and place to save but something you will need forever (your feet) is not it
[kqt7ps1] (score 3, diepte 0) I have size 4 feet in women’s & before the internet I was often forced to buy kids shoes or just wear shoes that were a size too big (5 is generally the smallest you can find in stores & even that is rare). Kids shoes are not the same. They are showed differently, made out of cheaper materials b/c kids feet grow so fast, and have no support to them.
[kqsr0mz] (score 2, diepte 2) I've purchased Target Cat and Jack boots on clearance for $6-7. They lasted over 2 years. I wore them to work pretty much everyday and they were fairly comfy.  My job is fairly physically strenuous. I did buy cheap adult boots for $30 and they're very uncomfortable. I have Hokas and Brooks (that I don't wear to work) and they're definitely comfier than kid sneakers.
[kqrvwl5] (score 2, diepte 2) I have one Trans friend with the same size feet as me. She is a fashionista. Unfortunately her feet are a wide and mine are a narrow. Her tastes are way too chic for me anyway but a girl can dream.
[kqrut1x] (score 2, diepte 0) Cries in women's size 12 😢 😭
[kqspcbj] (score 2, diepte 1) The men's section is for you.
[kqs011d] (score 2, diepte 0) I wear an 8 in women's, and have bought adidas sports sandals in boy's 6 for years, so 15 instead is 30 dollars.
[kqsbuer] (score 2, diepte 1) Yea! I swear buy the kids scetcher
[kqsdm4u] (score 2, diepte 0) Same for T-shirts, for smaller frames, buy from 14 to 16 y/o section.
[kqu5p87] (score 2, diepte 0) This also applies to clothing, when applicable (and not obviously children’s clothing)! This fall I visited a Vermont flannel store and it was SO expensive to get a shirt. The children’s ones still looked nice, and I fit into a large, so I only spent $30 instead of $80+.
[kqutb4b] (score 2, diepte 0) This only works if you also don’t have wide feet. My flinstone feet and I unfortunately need to pray adult shoes come in a very small size…thanks dad.
[kqzhs9u] (score 2, diepte 0) Shopping through online thrift platforms like Poshmark and Vinted is great too - especially for brand new shoes. 

I recently purchased a pair of $110 leather pumps originally from Hobbs for $18, and a pair of leather riding boots by Rupert Sanderson (they retail for $800) for just $80. 
Both came brand new in their boxes still stuffed with tissue and shoe shapers. 

Even better, if you also sell your old belongings on the platform, you can choose to keep the funds in-app instead of drawing out as cash, so when you do make a purchase, it’s at no cost to your bank account.
[kqrn3qr] (score 1, diepte 0) Seems like a no brainer, but that’s actually great advice!
[kqspljd] (score 1, diepte 3) I actually prefer womens boots but I don't buy work boots. Men's winter boots are usually very stiff and heavy, and I have a size 12 foot so those women's boots don't come easily but I don't want my boots to be very stiff and heavy. I buy size 12 bearpaw boots for myself though and they are perfect.
[kqum4d3] (score 1, diepte 1) I wear a women's 8.5/9 and have flat, wide feet. It's hard to find wide sizes that are actually wide. I usually just stick to the unisex brands as my go-to shoes

Men's shoes in size 7 are super comfortable, and like you said, usually on sale/clearance. Especially work boots.
[kqubnct] (score 1, diepte 3) Yes. Try out the size 4 or 5 depending on brand.
[kriegvk] (score 1, diepte 1) Not OP.  I weigh about 130.  I wear UK 2-2 1/2.  I have shoes and boots, all used in their rotation, from before I retired which was 2015.  I walk a lot.  Maybe my shoes were just better made, as some years ago?
[kqs0g77] (score 1, diepte 0) I know!!! Right! 🌟  I have tiny feet, I drool in the ladies' section. I can go bonkers in the kids' department and save oodles of coinage!  I travel a lot, so I get awesome selections 👌
[kqs3h44] (score 1, diepte 0) I buy little boys shoes all the time.
[kqs5wma] (score 1, diepte 0) There's an old frugality saying that you shouldn't go cheap on anything that's between your body and the ground. In terms of health and safety you almost always fare better by shopping for quality in terms of tires, mattresses, and shoes.

"Shop in the boys' section" is a topic which comes up in this sub every couple of months. That's probably going to put an adult woman at risk for foot injuries unless your foot has a really unusual shape to the point where you physically can't wear women's shoes because the lasts are all wrong.

I happen to be one of those rare exceptions. Men's feet tend to be wider than women's and have wider arches. My feet are extra wide with high arches. For work shoes and dress shoes I'm limited to the Naturalizer brand which makes women's shoes in extra wide, but have never found athletic shoes made for women that were wide enough. Trying to wear women's sports shoes causes sharp pain even for a couple of minutes and would cause injury doing any type of sports. That forces me to wear boys' size 6 for playing sports. It's the only thing which fits. Ideally would shop in the men's section because adult shoes are made from more durable materials but the smallest adult men's shoe size is usually 7.
[kqsjvmh] (score 1, diepte 0) Same for clothes! I've learned that a children's XL shirt fits me almost exactly like a women's small, depending on the cut sometimes the shoulders can be a bit tight, have to try it on first and evaluate. Skirts and shorts too, children's XL fit me *just* the way I like at a fraction of the price!
[kqskmbb] (score 1, diepte 0) There are good quality kids shoes, I buy them all the time. I also like that I don't have to pay tax on kids items. I also get my gloves and socks this way.
[kqsl5a9] (score 1, diepte 0) I have small feetand have done this several times.
[kqso0ig] (score 1, diepte 0) I do. And it's a lot cheaper too.
[krihcb2] (score 1, diepte 1) Not OP.  I imagine all my shoes are kids (UK 2-2 1/2).  All from charity shops/car boot sales etc..  I have orthotics, so my feet are well supported.
[kqt2cb8] (score 1, diepte 0) Socks too if you have slim feet. The kids socks I got were cheaper but also much less stretchy and roomy.
[kqt2lvj] (score 1, diepte 0) Women’s 8 is a big kids size 6. I’ve saved money buying my timberlands at the kid store. Good tip!
[kqt3zxv] (score 1, diepte 0) I wear a womens 8.5 and occasionally shop in the men's department.  Men's sizes usually start at 6 or 7, which is equivalent to women's 8 or 9.  I've found some good deals on sneakers and loafers at Marshall's.  It's amazing how much more toe room they give dudes.
[kqtmfrg] (score 1, diepte 0) I wear a UK size 3 and it only occurred to me last year that I could buy kids socks to stop them flapping around. Game changer! Even though I have always bought kids shoes/trainers. I only buy adult shoes when I want heels/long boots.
[kqtr8wm] (score 1, diepte 0) I buy kids shoes (mainly sneakers) and find that they last the same as adult shoes. I do normally need to size up a half size, but for casual shoes I think it's fine.
[kqubkpd] (score 1, diepte 0) I have to do this for flats and heels and it honestly sucks. I just want adult-looking shoes that fit my feet 😭
[kqw293m] (score 1, diepte 0) I’ve done this. I wear a 5D width which puts me at a 7 ladies. I’ve bought boys wide athletic shoes that were half the cost of women’s.
[kqwxcqt] (score 1, diepte 0) I had been going to do this last time I went shopping for running shoes. Actually, it wasn't about the price, but I was having trouble finding my size cause I have wide feet, and someone recommended kids shoes as they apparently run wide. I didn't end up doing it though because I was later warned that the longevity of kids shoes isn't as great overall because kids grow out of shoes so fast that they aren't made to hold up as long. If they wear out right away you won't end up saving money unfortunately. That being said, if you're only wearing them at the gym for a couple hours a week, wear and tear probably won't be an issue.
[kqz7xej] (score 1, diepte 0) I’ve done this my whole life!
[kqzavb0] (score 1, diepte 0) Yes!! My friend used to do this and I would be so jealous of her prices haha
[kqznyvw] (score 1, diepte 0) Yep! I love Vans slip ons and the kids ones and adult ones are made the exact same. I’d rather pay the kid price!
[le8osoa] (score 1, diepte 0) My in laws are tiny. They do this. I don’t think my father in law could shop in mens. He’s 4’8 with a size 3 or 4 depending on the shoe.

=== THREAD tjzw3h ===
SUBREDDIT: r/ems
DATUM: 2022-03-22  SCORE: 72  REACTIES: 67
TITEL: Big toe shattered by a main O2 tank while on a clinical.
POST (source_id=post):
Hello EMS fam. So fun story for y’all followed by a question or two. So I’m at the end of paramedic school, and today was my first field internship shift. Sadly, I only made it halfway through the shift. The main O2 bottle in our truck ran out quickly after a gnarly trauma call. I was busy loosening the straps from the empty tank inside the truck, and my preceptor was getting a new tank. When she loaded the tank onto the dolly, I saw her put the chain on it to secure it. Anyways… while I was loosening the straps on the empty tank, she was rolling the new tank over to the truck. When she came to a stop and placed the dolly flat, the tank went forward and the chain became undone and the tank went flying… onto my foot. My preceptor felt so bad about it.. I tried to breath it off, and then I tried to walk it off… I quickly realized no walking was gonna happen. I hopped my way into the EMS quarters and very slowly took my boot off as I tried to hold back my tears of pain so I wouldn’t look like a wuss. When I took off my sock, my toe was already dark purple and swelling. My preceptor went and got me an ice pack and some Tylenol and helped me hop to the couch to elevate my foot… the swelling got way worse in a span of like 5 minutes. My clinical coordinator was contacted and informed of the situation at hand and informed me to do an incident report and for my preceptor to do an incident report per their company protocols and to send my clinical coordinator an email of what happened. I forgot to mention that this was my right foot that was injured… so I quickly realized there was no way I could drive, and there was no one that could come get me either. My preceptor finally convinced me to let them transport me to a stand alone ED.  Fentanyl is a fantastic drug. My x-ray showed that the distal end of my big toe is basically shattered and there is a straight fracture down the middle to my knuckle. I am now home with crutches and pain meds. So here is the question… my BF is dead set that there has to be some sort of compensation such as workers comp etc. I’m in Texas if that helps. I don’t believe there is though, but might as well ask anyways. My next question, anyone else have any fun clinical injury horror stories to make me feel better?

EDIT: PER MY PROGRAMS UNIFORM POLICY AND THE POLICY OF THE AGENCIES WE DO CLINICALS WITH, IT IS NOT REQUIRED TO WEAR STEEL TOE BOOTS.

IMPORTANT NOTE: I WAS NOT DOING ANY TYPE OF LIFTING OR MOVING OF O2 TANKS. I WAS REMOVING THE STRAP FROM THE EMPTY TANK SO THEY COULD TAKE THE EMPTY TANK OUT. THERE IS NO POLICY THAT STATES PARAMEDIC STUDENTS CANNOT LIFT STRERCHERS, PTS, O2 TANKS, ETC.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i1nn0ih] (score 154, diepte 0) Wait until 3am and call EMS for help. That’s the logical treatment for toe pain
[i1n87od] (score 76, diepte 0) So workers comp is an insurance to cover disability and lost wages. You are not an employee of the service and do no qualify for workmans comp doing a clinical if they’re not your employer. The school might have insurance for you for clinicals. You’d have to ask your program. I am not a lawyer. This is not legal advice.
[i1naib8] (score 31, diepte 0) And that's why we all should wear proper protective boots
[i1nh5x8] (score 26, diepte 3) They shouldn't have to suffer with the bills and recovery alone though. Yes ems is small, but what are they going to say "oh that's johnny, he got hurt on clinicals and asked for help, screw him?" I'm sure the fto broke some company policy when this incident occured.  Also, literally everyone is hurting for employees right now so I would risk it instead of being stuck with easily thousands of dollars in expenses.
[i1ngkbc] (score 24, diepte 0) I would contact the office of the dean over the department your ems program falls under. Every school I have dealt with (as student and teacher) has insurance for students on clinicals. You probably had a small fee in your tuition and fees that went towards it. At the end of the day, a workplace accident happened with a trained professional at fault and an untrained student was hurt.
[i1n8gr1] (score 20, diepte 1 OP) That’s what I was trying to explain to my BF. We were looking through all of my schools paperwork and found no information at all about injuries on clinicals, just protocols for exposures such as needle sticks etc. he’s just concerned and upset this happened so he’s trying to find any resource he can as I do not yet qualify for short term or long term disability at my job. I basically have no way of being able to take off and have an income. I literally cannot walk lol.. I hope they don’t expect me to “call off sick” every shift for the next 6 weeks.
[i1n8w3c] (score 20, diepte 2) You’ll have to ask your school what they can do. As far as getting compensation from the service where you were injured, I’d tread carefully as EMS is small and everyone talks
[i1oo4u8] (score 14, diepte 1 OP) Lol this comment wins
[i1novnl] (score 10, diepte 0) For all my clinicals we were told that if we were injured or exposed to a pathogen we are shit out of luck as far as being compensated or cared for by the entities we worked with. I imagine that’s true for you. I hope this isn’t too expensive, and if it is make a gofundme I’ll donate.
[i1n9xad] (score 8, diepte 0) Did you manage that with steel toe boots on?
[i1obxk4] (score 6, diepte 0) While you may not be entitled to workman’s comp you should be covered for any treatment you need for your injury. Rules were not being followed when you were injured. The oxygen tank should have been fully secured and I would guess that you shouldn’t have been involved with changing it out. We aren’t supposed to let students or interns load or unload cots from the ambulance for that reason. If your program balks at you receiving treatment or tries to blame you, it might be worth consulting an attorney.
[i1pbmwh] (score 6, diepte 2) Ok, so definitely contact an attorney, in my state there is no required coverage for students but a reasonable person would agree that that situation should not have happened if that is the case. So suing to cover the medical bills at minimum and lost wages/pain suffering MAY be required. Also remember, the company you were with DEFINITELY has insurance for things like this. The preceptor doesn't have to be personally liable, even if they're named or even blamed for the incident, so don't let that dissuade you. (maybe you heard about the aunt who sued her nephew for knocking her over? there was no bad blood but she was legally required to have the homeowners insurance cover the medical costs)

Either way, take care of yourself and finish those clinicals
[i1ng949] (score 5, diepte 1) Only applies if that's a requirement, many places no longer require them.
[i1p9wkk] (score 5, diepte 2) Then your school should be liable. That's f'n ridiculous NOT to require them.
[i1nf82a] (score 5, diepte 0) Insurance through the school?
[i1p50la] (score 5, diepte 0) This is why I only wear shoes with protective toes. I’ve had to many O2 tanks and stretchers dropped on my feet not to.
[i1qetwx] (score 5, diepte 4) I don't want to sound mean. I'm really sorry this happened to you. It's terrible. I can't imagine how you're feeling. And I hope you heal and recover quickly. I hope you're able to complete school as well. I'm going to say this out of love and not as a critique or sass.

>How was I supposed to know the giant O2 tank my preceptor was moving around was going to drop onto my foot when she set it flat? I watched her put the chain on it too.

Because this is EMS. We work in crazy environments with all sorts of crazy equipment. We don't work in an office. We work where regular people flee danger and carry things weightlifters wouldn't touch. This is a hard lesson to learn. I'm sorry you had to learn it this way. But the reason we are all so incredulous and confused is because steel toe boots are standard for the above (and unfortunately your) reasons. Things fall that shouldn't fall. We step on things that most people will never step on. We should protect ourselves.

Please take this experience as a harsh lesson and try to protect yourself. Ours is a business where we always have to assume the worse will occur. Not just with our patients but with our safety. The fact that they didn't tell you about these boots is extremely unfortunate and reckless. Sending good vibes your way.
[i1oo0s1] (score 4, diepte 1 OP) They are not required per our uniform policy.
[i1onwvd] (score 4, diepte 1 OP) There is no policy for the agencies we work with stating that a student is not allowed to load/unload stretchers or assist in changing out main o2 bottles etc. I believe the chain on the dolly wasn’t secured properly sadly.. my preceptor felt SO bad about it.
[i1p4j9y] (score 3, diepte 3) I've heard this too, but fuck em. They can talk all they want when no one wants to do this job for peanuts.
[i1npisx] (score 3, diepte 0) My program has insurance, and students can’t ride without it. My agency I work for, independent of that school, also requires schools to submit insurance to have students ride. I don’t know if this is a government mandate, but I would think most schools need some sort of insurance should a student gets hurt, I’d reach out to them.
[i1o7u9u] (score 3, diepte 0) When I was in Medic school we had to have proof of personal medical insurance in order to do clinical rides. If we didn't have insurance they referred you to an insurance agent, or advised you to secure insurance independently.  They suggested Liability insurance as well, but did not require it. So basically if you got hurt, you were covered, but there was no coverage provided or implied via the school or the clinical site.
[i1or3c3] (score 3, diepte 0) No pics? Wtf
[i1ov45c] (score 3, diepte 0) Can’t speak to Texas. In my state education centers who provide clinicals are required to have liability coverage for students in the event of any injury. I’d be shocked if other states do not have this requirement. 

You need to reach out to the organization providing your clinical’s ASAP. (You should have the second you were injured). Every education program I have worked for has a student injury policy. Going forward, if you are EVER injured as a student or whole employed, contact your supervisor ASAP, often times there are very specific requirements to be compensated through insurance. 

Call your school. Right now.
[i1pbr6e] (score 3, diepte 1 OP) My clinical coordinator was called by my preceptor. The clinical coordinator is who we’re instructed to call incase of emergencies like that. My preceptor also contacted her supervisor. I filled out an incident report for my program, and she emailed my clinical coordinator about what happened and she had to file an incident report with her agency as well. Who knows, maybe something will come out of it
[i1pcam0] (score 3, diepte 2) Wasnt blaming you at all!! I was just saying how i never understood why i couldnt do certain things. Your circumstance totally sucks, and i wish you the best.
[i1pbfe5] (score 3, diepte 2) Well, protective footwear. It's a requirement for most (if not all) services in Canada.
I use composite toes, myself.
[i1pcqs4] (score 3, diepte 3) My program definitely required steel or composite toe boots; my job didn't have a requirement but for my medic school it was a mandatory element.
[i1pwl26] (score 3, diepte 2) Well then, I guess this is your reminder of EMS lesson #1.

Scene Safety; situational awareness and work on those reflexes.
[i1qw7x9] (score 3, diepte 5) Indubitably, good sir!

There's no way I'm risking anything going through my boots from the bottom, just think of all the things that could be beneath the surface of a "ahem...collectors" dwelling, yard, or in the ditch! And I'd prefer if my piggies didn't go to the market, should anything go TIMBER!

And as a heavy equipment operator and horse/cattleman **NEVER** go with steelies! If the steel toes fail, then it's OFF WITH YOUR FOOT!(well... some of it)
[i1pfg5z] (score 3, diepte 0) Sounds super painful. Wishing u a speedy recovery
[i1qgqla] (score 3, diepte 0) Are you really posting this here? I know you’re just a student but I refuse to believe you don’t already know you need to call 911 around 0300 and cry to them.
[i1ot47c] (score 2, diepte 1) Because as a volunteer (assuming it's a municipal or county department), workman's comp policies consider you an employee, even though you aren't on the payroll.  That same caveat does not apply to students doing clinical rotations.  If anything, it would be the school's insurance that would cover because technically OP is a student completing requirements of their program, arguably with an agency that has an agreement with the school to provide for students to do clinical hours with them.
[i1ti0mv] (score 2, diepte 1) 2 weeks from now
[i1pbfiy] (score 2, diepte 1 OP) Lol I’ll see if I can add pics, fairly new to reddit but I’ll try!
[i1oxths] (score 2, diepte 0) And while i questioned it my whole ride time, now i see why i wasnt allowed to lift anything, or move anything. (Patients, stairchair, stretchers, do any extrication, etc.)
[i1p0zwe] (score 2, diepte 0) I’d check and see if your school has any coverage. If not, the agency you did clinical with might if you didn’t sign a waiver.
[i1qxc5q] (score 2, diepte 5) Well said,  colleague!
[i1qg46x] (score 2, diepte 0) I'll share my story. I hope it makes you feel better.

While a medic student, I got injured, but it ended up being the best thing that happened to me.

While in paramedic school, I was having trouble connecting the dots. I had a really hard time with my ambulance rotations. I just couldn't synthesize the clinical picture and figure out what I was supposed to do. I was a fumbling mess. Because of this, I always tried to overcompensate by carrying bags and making myself as useful as possible because I felt so useless.

One day, and honestly, I don't even remember how it happened. I lifted wrong and hurt my back. The mechanics of lifting our equipment and patients just aren't built for us to remain uninjured. Even if you use proper technique, the movements that we make are always awkward.

I told my skills coordinator that I was injured. he recommended that I take a few weeks off of field rotations to do hospital rotations.

This was the best experience of my entire education. Rather than shadow nurses, I shadowed the doctors. They asked me questions that I was able to answer. They included me in the patient's treatment and care. I realized that I knew a lot more than I thought I knew, and it was the confidence boost I needed to succeed in medic school. And it honestly made me the provider I am today.

So maybe, if this is an option for you, you may have the same experience. You might hobble around like Dr. House but maybe take some time away from the field to get better at other things. I'm really sorry this happened and you got injured. I hope you heal quickly.
[i1qs7sz] (score 2, diepte 1 OP) Oh wow I’m so sorry to hear that happened to you, but I’m glad you were able to recover and get that experience!!! I probably won’t be able to do anymore hospital rotations. I’ve done all of the ones required, and the hospital are very stingy about students.. also for me personally I’m not a huge fan of being in the hospital lol.. I definitely thrive on the box and out in the wild. Also the extent of my fracture(s) are pretty gnarly.. I have a strong feeling this recovery will be a while. I am now a couch potato lol.
[i1qr9pg] (score 2, diepte 1 OP) Lmao I went though so many emotions reading this at once 🤣🤣🤣 I love it
[i1qsgck] (score 2, diepte 2) I'm just teasing. You gotten a broken toe, no way around it. 

Roll up some small towels for the crutches so it don't hurt your arm pits so much.
[i1tct0q] (score 2, diepte 0) Speaking as someone who sees patients in the ED frequently for work related injuries...

The EMS agency's workman's compensation will not cover you if you are not their employee functioning as an employee at the time of injury. That being said, it sounds like the EMS agency is liable even though this was an accident.

If your school does not have insurance for something like this, the EMS agency will be liable and need to pay for your medical treatment. You will likely need to see an orthopaedic surgeon for follow-up in the clinic. Sometimes these kinds of injuries need surgery, sometimes they don't. You are potentially facing thousands of dollars worth of medical care, especially if surgery is recommended. The EMS agency will be responsible for paying for this. If you signed a waiver then this gets murky and you need to talk to a lawyer. NOT ALL WAIVERS hold up in court, and a lot of times they exist solely to scare people into dropping the issue because the assume the injured party assumes they can't sue. Not always true.

You may have to take them to court. What gets murky is when you use your personal insurance to pay for things and then you will have to ?sue the EMS agency to get your bills paid. Not fun.

You need to talk to a lawyer.
[i1pcnph] (score 1, diepte 2) No,the department is an independent corporation not a county entity,as far as the clinical side,if working on an ambulance service rig you MUST be covered by their comp unless you sign a waiver otherwise. Except for one small fact,that Texas doesn't even require employers to carry Comp!
[i1pfa8u] (score 1, diepte 3) But there is a loophole.  Doing clinical, you're not WORKING.  You're in a learning situation in a work environment.
[i1q4qo6] (score 1, diepte 4) But just like with an internship,if you are there, doing the job, you are technically an employee,that's how it was when we were doing our ER rotation.
[i1nfhzl] (score 1, diepte 0) Oof
[i2hpxqp] (score 1, diepte 2) No! A year from now would be the icing on the cake.
[i1ov2ib] (score 1, diepte 0) In our region, the college based programs require the students to get insurance prior to their ride alongs. Is this mandated at all in your program?
[i1pbzwu] (score 1, diepte 1 OP) I wasn’t lifting anything. My preceptor was. She was moving the O2 tank dolly and setting it next to me while I was removing the straps from the empty tank in the truck so they could remove it. When she went to lay the dolly flat, the chain came off and the tank went flying onto my foot. This was not my fault.
[i1p9r21] (score 1, diepte 0) Where were your steel-toe boots during all of this?
It's commonplace for us everywhere on the job, and failure to wear them (as with all necessary PPE) will make you liable for any injuries that could have been reasonably prevented by wearing them.
[i1pez66] (score 1, diepte 2) Mm. Wires calls
[i1pc9b7] (score 1, diepte 1 OP) It’s not required by my program or by the agency we do clinicals with.
[i1qqg9t] (score 1, diepte 1 OP) Thank you!
[i1ppgis] (score 1, diepte 0) You probably signed some kind of form releasing the place where you did rideouts from any liability. It usually is that way. The school should have something to do with compensation, though, since you were on the school's time doing schoolwork. Contact your coordinator first, and the company you did the rideout with second.
[i1q4djk] (score 1, diepte 0) Just started my clinicals as an EMT-B, im sure you can't because you aren't a paid worker, and I had to sign a waiver on case of injury and all that good stuff. I'm sure that you probably had to sign one too. So the liability won't fall on whatever agency or school you're with. Hope you feel better!
[i1qq229] (score 1, diepte 0) So you took an ambulance to the ED for a sore toe? /s
[i1qrele] (score 1, diepte 1 OP) I wanted to drive myself but there was no way I could 🤣 I felt like a major wuss.
(8 reacties met lagere score weggelaten)

=== THREAD 1f5jtw9 ===
SUBREDDIT: r/AmazonFC
DATUM: 2024-08-31  SCORE: 28  REACTIES: 67
TITEL: Excruciating foot pain from safety shoes
POST (source_id=post):
Just started my job and my FC is required to wear Zappos safety shoes. The first 6-7 hours are manageable but the last 3 hours are almost completely unbearable. The pain is so severe I need to go to the restroom just to sit down in the stall. It's the standing that's killing me. If I'm walking around it's not as bad. The work itself is easy and I don't mind it, but the foot pain is excruciating. I have to take all my breaks sitting down with my feet propped up in the air which, of course, brings stares. What can I do to help this? Will it get better over time?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lktaycc] (score 26, diepte 0) Please go to wellness! Report this! They will help you figure out what needs to happen. You might consider returning your shoes and grabbing a larger size.
[lktbf60] (score 21, diepte 0) If this continues to worsen I would speak with your doctor. Especially if your pain is located more towards your heel. My husband got diagnosed with plantar fasciitis not to long after started at Amazon. Apparently it’s a common diagnosis among fulfillment workers.
[lkthfkx] (score 17, diepte 0) I suggest going up a size and finding a shoe that comes in Wide sizes. It's a game changer.
[lktc9zl] (score 9, diepte 1) Ibuprofen every morning damn your liver must love that stuff
[lktbahq] (score 9, diepte 0) Your shoes are too small. The same thing happened to me when I first started at Amazon. You need to return these shoes and go up half a size or a full size. It will give your foot room to swell up some from all the physical activities.
[lktyp78] (score 9, diepte 1) Yes! This! ⬆️ It is incredibly common. I’m still dealing with it and I haven’t worked at Amazon for almost a year now. It came on when I started full time.. (it was a new building and short staffed, so we were all MET for MONTHS). It’s not going to get better, it will probably get worse, so go to wellness and report and get yourself to a dr. MET will probably start in Oct… so get on top of it now. There are a lot of threads to things you can do to help with the pain on here (again, because it’s so common)… lots of self care tips. No one cares you have your feet up btw… everyone goes through it!
[lktp62c] (score 8, diepte 2) Kidneys but yeah not great at all
[lkti2l9] (score 6, diepte 1) Amazon floors are very tough on feet for everyone starting out. Even with proper shoes and insoles there is just no give from the floor.  Get two pairs of shoes and rotate them every other day. Get insoles and thicker socks. That will all help. Heck I have a pair of boots that have two thin air soles in them. 

Once you have your feet taken care of any lower back pain should start to subside. Pain radiates upward.
[lkt9k0n] (score 6, diepte 0) I wear knee braces, compression socks, socks over that, dr scholls insoles, and eat ibuprofen every morning like it’s a multivitamin. I walk about 10 miles a day in RME and my body is dead afterwards. I’ve been doing it a month now and it hasn’t got much better. Use a heating pad on days off, eat as much protein as you can, and get as much sleep as you need. Good luck.
[lktob3n] (score 6, diepte 0) It's Mandatory that Amazon makes your work experience as horrible and destructive to your health as possible, it's for your safety.
[lktpvso] (score 5, diepte 1) This.  Went up half a size on my second pair and it was a game changer
[lkth6zl] (score 5, diepte 0) Buy shoes that are a half size bigger than what you normally get.
[lkt9c9q] (score 4, diepte 0) Insoles based on foot shape. If you have a high arch than you absolutely need an insole to support it. 

Even if you don't have high or flat arch you should get insoles. Box store one's to get by and order some real ones as soon as you get a chance. 

Pull the original insoles out of the safety shoes before adding new ones or you could run into the issue of the shoes messing with the top part of your feet.
[lktfiwe] (score 4, diepte 0) I brought my massage gun with me to use on my breaks. They even came out with a mini version that is cheaper and a lot easier to carry around. It’s by theragun. A lot of the cheap massage guns on Amazon are trash.
[lkto6ow] (score 4, diepte 0) I’ve been with Amazon for three years and my feet still hurt. The first three weeks are the worst when first starting. I think you just get use to the pain in the long run. I’ve tried many different safety shoes and have even worn my regular shoes. I just went to the pediatrist and they gave a cortisone shot that didn’t help in the slightest I have a fitting for custom orthotics in a few weeks so hopefully it will help. One thing that did help was a cushion that was provided that elevates my toes so I’m putting less pressure on my heals (which is where my pain mostly is) I have severely painful plantar fasciitis. 
 the drscholls gel inserts actually do help quite a bit if looking for a quick fix that’s a decent price.
[lkt9bd9] (score 3, diepte 1) I had that real bad a few weeks ago. It still hurts, mostly when coming off break and not moving. It probably will never heal long as they keep making me water spider.
[lktc452] (score 3, diepte 1) If you get an injury and they check to verify you get terminated
[lkthlf0] (score 3, diepte 1) You should never lie about your shoes, especially with how easily a heavy tote could fall onto your foot. If they’re bothering you, there’s a lot that can be done besides faking
[lkt9f7o] (score 3, diepte 1) Yeah they are banning the one shoe that literally feels like youre not wearing a shoe. Im glad I didn’t buy them yet they just said it today during stand up.
[lktic45] (score 3, diepte 0) At first, it was absolutely murderous. Being on concrete floors 10 hours is foot torture After a month, I started getting used to it, but my feet still really hurt. 

Pain meds and hydration help a lot. 

You need the right inserts for your feet.  I tried 2 different higher priced inserts with arch support that were OK, but my feet still hurt.  

Then I tried a pair of $12 Dr Scholl's gel inserts, which were marginally better than the pricier arch support inserts.  

Then I stacked a second pair of the Dr Scholl's, and I made it through a whole shift with no foot pain and no pain meds.  It took me 5 months to get to this point.

Looking back, I should have listened to my wife and had custom inserts made early on.
[lktlo67] (score 3, diepte 0) How long have you been there? It honestly didnt stop for me until week three or maybe four. Its touggh
[lkugece] (score 3, diepte 0) I suggest ordering shoes a size up and always go for wide width. I work 12hr shifts. I like to sit in my car on lunch break with my shoes off and feet up on the dash. That gives me at least 20 minutes of rest. I also wear compression socks and sometimes I'll change into a different pair of safety shoes on lunch break so I'm only wearing one pair for 6 hours at a time.
[lkt8f5w] (score 2, diepte 0) Make sure right size. Buy insoles. Wear double socks. Don’t wear safety shoes but shoes that look like safety shoes. I have plantar fasciitis because of the shoes and I only work about 6.5 hours a day because my feet can’t take it
[lkt8fun] (score 2, diepte 0) I’m wondering this too I start my 3rd week tomorrow and it starts hurting so bad like 3-4 hours before I’m off and my back and body start killing me it’s gotten easier since the first week but still bad I don’t think it will ever get better good thing I’m seasonal and have another job and I sit for 10hours a day😂 🙏
[lkvxemw] (score 2, diepte 2) I third this. I haven't made it to a doctor yet, but I know I am battling it also. Insoles won't fix it either. I had to pick up critical roles that management didn't closely monitor so I could sit down every so often. It's caused by overuse. I also suggested looking up stretches for your hamstrings and workouts to strengthen your feet. Compression socks also help some as they help support that tendon.
[lktnszv] (score 2, diepte 2) Zappos is not a brand. They are a retailer who sell many brands. Fun fact,  Amazon owns Zappos.
[lkvxlfu] (score 2, diepte 1) This is how I order all my shoes now. Also don't lace your shoes too tightly.
[lktvnfs] (score 2, diepte 0) You can also switch shoes tell Zappos the shoes are faulty and switch them. But the people talking about insoles are right. Worse case scenario you go to HR tell them you want an accomodation take the paperwork to the doctor and then you can wear those toe caps that go on the bottom of your shoes.
[lkuir6v] (score 2, diepte 0) Did you get the insoles they offer for free as well? They were a game changer for me.
[lkt6xv3] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[lku68va] (score 1, diepte 2) I highly recommend darn tough (padded) crew socks. They help me out a lot
[lkt8g7k] (score 1, diepte 0) I have the same issue. If I could wear a comfortable shoe, this job would be a breeze. It’s the “unsafety” shoe. I do more damage to my body using these shoes
[lkwx40r] (score 1, diepte 4) Yeah I really should alternate out. I think I used to take Aleve “muscle and back pain” stuff was legit. The worst thing is, when I get home, I take my last advil or ibuprofen with a few beers lol. The pain and aches have been so bad, today I put in 6.5 miles in on stairs and floors so I’m not in as much pain as the days I put in 9-11 mi. 

Last week I thought I had blown a disk in my lower back. With every step on the floor, I was gimping like an old blue collar worker. It was frightening to say the least. Pain doc said it’s likely “Myofascial pain” as when standing still I wasn’t in pain. Only when I was moving. Told me to relax the muscles and use a heating pad. That pain went away, but it was a wake up call. I doubt I can work at Amazon for more than 3 years. I fear of knee and hip replacements from all the walking on concrete and metal stairs. I use the knee braces everyday when I can, because there was days I came home and could barely squat or stand up from the couch. 

I have huge respect for stow and pick aa’s. I don’t know how you all can do it day in and day out. Get that career choice training in, save your money, and advance your skills & knowledge. I’ve seen young AA’s in their early twenties walking around like an elderly person pushing those blue carts full of packaged boxes and it’s a bit frightening to say the least. This is not a place to grow comfortable off the wage and not have a fallback plan if moving up the management food chain isn’t an option.
[lkwavqp] (score 1, diepte 2) Yup along with carpal tunnel, tendonitis, knee, shoulder, back, etc. There's a reason why Amazon has the highest injury rate among its workers. When I go to my doctor appointments I its not imcommon to see other FC associates with similar injuries.
[lktm5b1] (score 1, diepte 2) The Zappos brand
[lktqvu8] (score 1, diepte 3) Yeah I knew that Amazon owned it, brand is a misspeak but people get the gist
[lktnz84] (score 1, diepte 1) You most definitely are required to wear safety shoes, namely a composite shoe. They don't have to come from Zappos. They just need to meet a certain standard.
[lkwk6vh] (score 1, diepte 2) Literally what I said
[lkwwrvb] (score 1, diepte 1) Don’t do that I sized up two sizes and it’s the absolute worst
[lkurqq0] (score 1, diepte 1) I’m gonna try this. Thanks.
[lktiy3m] (score 1, diepte 0) Remember rice, rest ice and compression. After about a month you'll just go numb to the pain. If you want to speed things up you could ask to tote run or some sort of indirect role that makes you Walk 20 plus miles a day in those terrible shoes on that terrible floor
[lktk8v8] (score 1, diepte 0) Timberland Berkleys are fantastic, bro. I only wear vans outside of work, but the Tim's are comf
[lktqoae] (score 1, diepte 0) I had nasty foot pain, i thought it was the safety shoes turned out that i have a heel spur 😮‍💨
[lku4r9l] (score 1, diepte 0) Bunions are no joke...
[lku60ov] (score 1, diepte 0) This was me. I ordered the fururian steel toe shoes off amazon in a size bigger than i usually wear. Normally $50 but can be found cheaper on sale. Then I got valsole inserts for about $30 with good arch support since I am basically standing in place most of the day. I am like you, when i was walking I was totally fine but standing I thought I could not take another step sometimes. This combo of shoe and insert took a couple days to get used to but now I have no pain at all. Which is saying a lot because I am fairly overweight and I stow so mainly standing in place. Also compression socks! Almost forgot those. And then over those since the ones I have are thin, I wear darn tough cree socks since they provide extra padding and are super durable.
[lkulqod] (score 1, diepte 0) New balance comes in double wide (EEEE).  It's the only one that doesn't crush my toes and make them rub on the safety toe
[lkum34n] (score 1, diepte 0) I worked in podiatry for 5 years the shoes could be too heavy for your lower muscles of the calf. If it continues to worsen while you’re at rest, i would try arch supports and a night splint.
[lkum8eu] (score 1, diepte 0) You need wider shoes.
[lkunt6e] (score 1, diepte 0) I had knee pain, foot pain, foot fatigue, etc 

but when I got keen cincinnati (2EE - wide size) 8 inch boots, everything went away (for real)
[lkuymzh] (score 1, diepte 0) Get bigger shoes, I have to wear a 7.5 even though I normally wear a 7 and insoles have helped me so much I can go a whole shift without any discomfort. It also depends what job you’re doing
[lkv09eh] (score 1, diepte 0) Get a STIFF insole. Your automatic response is you want something soft and cushy on your feet but what you really want is support and structure.
[lkv7wlc] (score 1, diepte 0) Zappos shoes are terrible. You can buy any sneakers on Amazon as long as they have hard toes. 
Half my warehouse buys a sneaker you have to buy on Amazon. 

I remember my Zappos shoes were clunky clown sneakers that took out my calves. Now I have discreet little black shoes.
[lkve55o] (score 1, diepte 0) Takes a few weeks, but you’ll get used to it and you won’t even notice it
[lkvnwb6] (score 1, diepte 0) Go to the doctor and get an accommodation to not wear safety shoes, they have to honor that.
[lkvy988] (score 1, diepte 0) Try different safety shoes. I had a pair that didn't work for me, now I have the Reebok's and feel good all day.
[lkwiuqw] (score 1, diepte 0) Start the return process on your shoes and order Irish setter wedge sole boots on Zappos. Wedge sole boots are made for all day comfort on concrete floors
[lmq8p11] (score 1, diepte 0) I know the pain too. If it's not compulsory to wear only their brand, go for ladies shoes, a size up. Maybe they're lighter. Insoles help, take your shoes off and curl them to relax. I do that everytime I can sit down, I take them off and just curl my feet in any way. At home I put some gel for pain. Haven't tried compression socks, but there's a few stuff online you can order and try, so cushion pads for metatarsal part (the area below toes where if feels like you step on glass after 10h on those shoes lol). There's no other way to wear those boots, the sole is simply too hard.
[lkuvav9] (score 0, diepte 3) I heard to rotate between tyneol and advil .

Gives your kidneys/liver a break
[lkv8han] (score 0, diepte 1) Wellness gave me a lacrosse ball and told me I hadn't been at Amazon king enough for it to be an amazon caused issue 🤣 I'd been there 10 months.wellness sucks.
[lkvbfu0] (score 0, diepte 2) On break go back and ask for ice and or heat pad. Also ask them for a new credit for Zappos, if your shoes are a problem. I’ve seen people end up with stress fractures from certain styles
[lkvehoj] (score 0, diepte 3) Fuck Amazon. I don't work there any longer. All their safety bricks went into the trash.
[lkthnr2] (score 0, diepte 1) Yes you are required to wear them, did you not attend day 1?
[lkuqxoo] (score 0, diepte 0) Keep trying different shoe brands.  
  
I was in excruciating pain for 6 mos. before I got my Reebok's.  
  
They have never hurt at all.
[lktda6q] (score -1, diepte 0) Your not required to wear them they just sweat you getting them cause it’s free you can buy your own and be okay!! But next time but the Reebok zigzag composite toe !! They are very comfy and I stand up in a PIT ALL DAY also they have some type of memory foam gel for the insole
[lktdl8n] (score -1, diepte 0) It gets better over time, trust me. Those first couple days are brutal. 

That being said.... 

One COULD wear some wide toe boots, and I doubt anyone would actually question if they are safety toe....

Boots "look" the part so rarely does anyone ever question them....

So one could find a nice pair of comfy wide toe boots and bypass those toe crushing chinese foot bondage shoes they try and pass off on Zappos.....

