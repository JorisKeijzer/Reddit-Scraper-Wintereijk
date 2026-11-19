# Label-batch batch_0087

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
Schrijf het resultaat naar `batch_0087.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: mmmqee, 15340ts, 1ft5h3s).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD mmmqee ===
SUBREDDIT: r/FASCAmazon
DATUM: 2021-04-08  SCORE: 42  REACTIES: 81
TITEL: Aching Feet
POST (source_id=post):
Greetings fellow amazonians. Anyone have any thoughts about keeping your feet happy? I have tracked myself walking over 13 miles on certain days and those concrete floors are not forgiving. Thanks...

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gtsvc5e] (score 24, diepte 0) I be giving foot massages in the break room for swag bucks. Throw in a Peccy pin and I’ll suck the big toe lol
[gtskqwt] (score 17, diepte 0) 1. Compression socks 

2. Ice baths for feet

3. Massage

4. Adidas ultraboost
[gtsf1r3] (score 11, diepte 0) Adidas ultraboost.
[gtsbb1s] (score 7, diepte 0) I went through 9 pairs of shoes before I found ones that made my feet feel a million times better at work. I’ve had days when I’ve logged 25 miles on my fitness tracker in a shift so these shoes saved me. I rotate my shoes between two pairs of adidas ultra boosts (solar boost and Ultraboost 20) and a pair of Hoka Bondi 7’s. All three feel like walking on clouds but if you wear them three days straight the cushion gets compressed so I rotate them to give the cushion time to bounce back. Then I powder my feet with baby powder before putting on some compression socks and stretch my legs about every 30 minutes throughout my shift. Sell the free shoes Amazon gives you from Zappos and use the money to get the good shoes. Also taking a aspirin will help improve blood flow to your extremities and keep your feet from swelling.
[gtsugz1] (score 7, diepte 1) Alsp recommending compression socks. When trying out different ways to alleviate my foot pain, compression socks gave me the most notable improvement.
[gttvh1f] (score 7, diepte 0) Get yourself a pair of Hokas or Brooks or Ultraboost - something made for walking. They’re pricey but a lesson I learned is never skimp out on great shoes because of the price. I’ve tried Skechers but it doesn’t work out for. Hope this helps. 
Source: my happy feet
[gttzd32] (score 7, diepte 0) 13miles aint nothing compared to walking 25miles a night in my FC, so take my recommendation , First insoles. can use brands like Z Liner ( best with adidas boost shoes ) , if you use boots ( i use composite toe boots once im unloading trucks ) ill recommend Powerstep Insoles, Second ill recommend buying a feet powder to keep feet dry if your feet sweat a lot like mine, and third and this is gonna sound weird, BUY WOOL SOCKS. yes, someone recommended me that and i was like what? i bought a 4pack for 20 bucks and i can say my feet dont hurt no more after 20-25 miles a night when i tote run.
[gtug5ut] (score 7, diepte 0) What about for an aching soul? Get it... nah really tho. I’m drained.
[gtsn00c] (score 6, diepte 1) Compression socks are absolutely necessary, and there are plenty of patterned options
[gtumn8l] (score 6, diepte 1) I took that free shoe through Zappos , chose Reebok’s but they are so heavy . Such a waste .
[gttvvvf] (score 6, diepte 1) Memory foam goes flat after a while because youre always on your feet. At least that’s my experience wait it
[gttp6nm] (score 6, diepte 0) Compression socks!
[gtt94f1] (score 5, diepte 2) I bought the ultraboost 21 shoes and wear them to work everyday. Never had foot pain again.
[gttvyrc] (score 5, diepte 1) Really you should never skimp on anything between you and the ground. Be it shoes, tires, or mattresses, these things are factors that contribute to how your day will be.
[gtu5iv2] (score 5, diepte 1) I am here to tell you that Hokas are a mainstay of nurses, or at least, those that know of it. Listen to this person. Then thank him later.
[gtsgqck] (score 4, diepte 0) 1. Comfy ass shoes.

2. #BUY A MOTHERFUCKING MASSAGE MACHINE OR PAD OR SOMETHING ELSE OF THE SORT TO PUT UNDER YOUR FEET WHEN YOU GET HOME.

Trust me, shit does wonders.
[gttbcqs] (score 4, diepte 1) Omg such a brilliant idea for business lol 😂!!!
[gtu61j3] (score 4, diepte 1) Buy some credit card operated massage chairs and place them in the break room. Roll in dough after a few weeks. I can't believe Amazon hasn't done that yet. Do they not want more money?!
[gtsx7tx] (score 4, diepte 0) I know an AM who swears by bringing two pairs of shoes and changing midway through shift. for me, just switching socks on lunch break does wonders. Also, seconding what everyone else is saying - it can take some shoe trial and error. My first pair of work shoes were some stupid comfortable reeboks that were great, up until about 4 hours into shift, when suddenly they got very, very, very uncomfortable for reasons I’m still not sure about. Got a solid pair of tactical boots for half the price on recommendation from some correctional officers i know (turns out you end up walking more than a few miles a day in a prison too, lol), and once i broke them in, they were golden.
[gttqvxh] (score 4, diepte 0) lose weight, wear comfortable shoes, sit when you take your breaks, wear a thick sock. i have flat feet, which makes it extra hard, but its part of the job, i just deal with it.
[gtu2ehs] (score 4, diepte 1) Socks are major key! I log 6-12 miles a night in my DS.
[gtta4li] (score 3, diepte 2) Only the yeezys are but you can get boosts made just by adidas
[gtskocu] (score 3, diepte 1) goddamn right
[gtw08dt] (score 3, diepte 2) And go work where?
[gttt4bk] (score 3, diepte 1) That's what I do! I change my shoes out on my lunch break
[gtt3sju] (score 3, diepte 0) I definitely recommend getting some good insoles and doing some research/ shopping around for shoes that fit your needs. Take a few hours at least. You’ll be living in those shoes so it pays to do the research and test them before you commit. 
Most of the shoes I’ve tried from the Zappos at work program were crap. The hard toe bites your feet with every step. Most people who work on the ship dock walk so much they don’t even wear the Zappos shoes. The keens bit into my big toe a little. After my toes got calluses they turned out to be very comfortable. I blew them out in less than a year though

Look for something lightweight AND add good insoles (I like the footprint insole technology insoles. They’re expensive but worth the cost).
[gttewrg] (score 3, diepte 0) I swear by Hoka’s. I wear the Arahi’s for stability and love them!
[gttgge8] (score 3, diepte 0) Compression socks and memory foam Skechers.
[gttkx2m] (score 3, diepte 0) When I was a CNA we used to freeze water bottles and roll them under our feet when we got home. I still do it to this day now that I’m at Amazon but I add whatever pain killers I can find
[gttn0fl] (score 3, diepte 0) I use filas I got them at jcp for 40$ and they're rhe most comfy shoes. I used to use adidas ultra boost but after a week I could barely walk. I also get pedicures every once in awhile and get extra massage and I use menthol foot creams on my calves and feet.
[gtu5rvf] (score 3, diepte 0) The sketches in got from zapper ducked. I went back to my favorite brand of shoes/boots/sneaks, Merrell, from day one they never hurt me. They can be a bit expensive,  but I look for sales & use coupons, plus I have multiple pairs so I can switch them out depending on the weather.
[gtvj7bm] (score 3, diepte 1) You could've bought $110 worth of in soles from Zappos on their dime
[gtvp6q9] (score 3, diepte 1) Zappos is hit/miss. I always pay the premium on top of the discount to get a half decent pair of boots. That and copperfit work soles. Like $12-16 at walmart. Worth it for me personally.
[gtumzel] (score 3, diepte 1) 😂😂
[gtugyjc] (score 3, diepte 0) Hoka one one they are the cushiest shoes on the market. Clifton, arahi, or bondi.
[gtunv3b] (score 3, diepte 0) I’m here for the comments my first month at Amazon I literally cried walking up the steps to my apartment every morning . 🤦🏻‍♀️
[gtvp17j] (score 3, diepte 0) I was taught by an older colleague when I was with nestle to not think about it. The moment you do it gets 100x worse. Get solid good solid insoles. Copperfit work soles are great. A little higher on the price but I mean they last about 6 months for me. Also if you're in an indirect role. Good stable boots. If you're in a direct role, good supporting shoes. 

The boots are a preference. Have worn them for most of my life and shoes do not entice the same level of comfort for me. Everyone varies there.
[gw9et04] (score 3, diepte 0) I recommend compression socks or socks that offer compression properties.  Steigens are the best option that I've found so far.
[gtsyeru] (score 2, diepte 2) HA! NERD! 😂
[gtsuran] (score 2, diepte 2) Mediocre bot
[gtshzug] (score 2, diepte 0) Double socks! Just remember to loosen the laces too.
[gtufj85] (score 2, diepte 1) Leave that crappy job. That’s the best advice I can give you for your feet
[gtspcb6] (score 2, diepte 0) Rotate your footwear. Daily.
[gtumo7t] (score 2, diepte 1) 😂😂😂😂
[gtszepx] (score 2, diepte 0) For me. I brought some Metatarsal Pads that you can wear on your feet. It works like heaven for me. Little bit of a warning though, at first can be a little uncomfortable to wear on bare feet because fabric can feel a little tight, if this happens you can try to wear them on top of socks until it get use to your feet. Hope it helps. Stay safe.
[gtu8zkj] (score 2, diepte 2) I had them for years before I worked at anaxon and used them to run but got injured so I just had them. And thought they would be fine but nope, I was limping to my car. Even the zappos shoes are uncomfortable I returned them.
[gttw2jy] (score 2, diepte 0) I raise my feet when I sleep
[gtty2cv] (score 2, diepte 0) ngl,,, when i have small items like books that can fit at the buttom shelf i kneel down to stow them just to get off my feet for a second
[gtu2j89] (score 2, diepte 2) Wool socks are magical, plus the feet powder makes sure your feet don’t sweat like crazy , even when I’m in the truck sweating like a Bull my feet stay dry all night
[gtu2ems] (score 2, diepte 0) I got inserts that were actually for planter fasciitis, and they were great. They hurt for the first few days & I had to take them out after 1/2 the day (6hrs) but the next week they were a God send. & I’m still wasting them 6months later.
They were the off brand from Dr. schouls.
[gtu7a56] (score 2, diepte 0) I don't use the zappos bc they hurt everyone, me included. Apparently the composite toe messes up the sole. I switched to my old shoes and on top of my insoles I bought at walmart, I did the dr scholl's measurement and put in another insole. It was $50 I think for my Dr scholl's custom. I also take 50 mg of diclofenac. And I think my feet are used to it now, because sometimes I miss a day of medicine but I'm still scared to stop using the prescription ibuprofen. It was really painful before.
[gtuekqc] (score 2, diepte 0) I just got hired from amazon. and my wife recommended me to buy two new pair of shoes. since I'm flat footer I use Asics GT 2000, this time I bought 2 (Gel- Kayano 27 MK).
[gtv3iw4] (score 2, diepte 0) I have two pairs of On Cloud shoes and they’re the most comfortable shoes I’ve ever had. They’re about $150 or more but they’re 100% worth the money. I can get through my three shifts and my feet are still happy by the end of it. But you can get them through Zappos and you get a $110 credit towards shoes so you can realistically get some for like $60
[gtvr3mo] (score 2, diepte 3) Ahh I don't see them on the listing 😣 can u tell me the exact name of them?
[gtw6ccp] (score 2, diepte 0) This place sucks
[gtxewdp] (score 2, diepte 0) I paid for the good high arch insoles off Zappos. The boots I wanted weren't "approved" so I bought those too and used the discount for my composite toe shoes and another set of insoles. 

I do my own stretches when I hurt during the shift. My shoes come off for every break and I swear by compression socks. 

Before work I drink a preworkout+ collagen smoothie and take 2 advil, 2 turmeric, a liquid magnesium and calcium supplement, and 2 more collagen supplements to keep my joints supported from the inside out. 

When I come home I plug up the tub while I shower with scalding hot water and put some epsom salts into the basin so I get that relief and I sleep with my legs up on a wedge pillow. 


I don't hurt as much as my husband does these days but my arms do fall asleep a lot still.
[gtsbblz] (score 1, diepte 1) 25 miles is 40.23 km
[gtsycsc] (score 1, diepte 1) Are those the adidas made by Kanye?
[gtt6uib] (score 1, diepte 1) Which ones ? I see there is a lot of version of the shoe, which is the one I would want ? or which ones are you using ?
[gtun5fx] (score 1, diepte 1) Yup I was a Cna as well I use a lacrosse ball .
[gttsz4t] (score 1, diepte 1) I'm glad I'm not the only one with the ultra boosts issue. When I first bought them they felt amazing. First day on the floor I wanted to cut my feet off. So now I have a 180$ pair of ultra boosts just sitting here.
[gttsu32] (score 1, diepte 0) You got me. I've tried like 8 different pairs of shoes. They only thing that seems to make it bareable is to change my shoes out midshift. So I'll wear a pair, then go out to my car and switch them out on my lunch break.
[gtu1onh] (score 1, diepte 0) A friend bought me like $75 shoes for my birthday and they were supposed to be super comfortable and all that. Those shoes are trash compared to a $30 pair of shoes I bought at Walmart. My cheap shoes are amazing and I've only felt at most a very minimal ache at the end of a shift, though most nights I don't have any pain at all!
[gtunb1v] (score 1, diepte 1) Were that Walmart brand or Dr. Scholl’s?
[gtv1msy] (score 1, diepte 2) They just say s sport which is prolly like a Walmart knock off of something
[gtvfl47] (score 1, diepte 3) Ok thanks!
[gtvo7zl] (score 1, diepte 2) 🤦🤯
[gtulp9f] (score 1, diepte 0) Nike react run https://www.nike.com/t/react-infinity-run-flyknit-mens-running-shoe-QbwPss

Honestly the soles are great in these, I have two pairs and I average around 27k steps a day. It’s probably time for a new pair but still I recommend them.
[gtv5sqg] (score 1, diepte 1) How do you get the $110 credit?
[gtvj3fa] (score 1, diepte 2) With the Mind Your Step program they began last year in partnership with Zappos, I actually received a $160 credit for my Ariat boots because I am a Prime member and a Zappos rewards member as well.
[gtw6lm3] (score 1, diepte 3) Name plz
[gtvjn1v] (score 1, diepte 0) I walk 10 miler per 4 hours worked. Safety shoes I recommend are Sketchers composite or steel toe. $50-$100 Non-safety shoes I’d recommend Sketchers Go Walks $35-$80 depending on availability and color. I use the Go Walks but have the safety shoes chillin til they make it mandatory. The insoles on the go walks worked well for 13 months. Then started to fall apart. Which led me to replace them with gel insoles. Which is about the same comfort level as the original insoles. My feet never hurt. Legs used to but I started stretching during the shift to prevent that. We only stretch before shift at stand up which I haven’t attended since before covid. Still stretch on my own before, during and after my shift. Helps a lot.

Edit: If money is an obstacle the Walmart sketcher equal will suffice for 4-6 months. When I first started I bought a pair and thanked myself with Sketchers later on when I had more money.
[gtwejv6] (score 1, diepte 0) I have developed plantar fasciitis from all the strain on my feet. It’s horrible...I just had to buy special inserts and I ordered a pair of new shoes hoping it will at least ease up. I’ve had to stay home a couple days bc I just couldn’t put weight on my feet some days.
[gtwk7o5] (score 1, diepte 0) Get some Dr. Schools inserts from CVS. I used their work edition and they run less than $25.00. Works wonders!
[gw9f79x] (score 1, diepte 1 OP) Thank you!
[gwa92di] (score 1, diepte 0 OP) Thanks for all the input  I'll keep you all updated. I went to a podiatrist and he's getting me a custom made insert that should be practically indestructible. I'll let you know how that works out.
[gtu7pwu] (score 0, diepte 1 OP) Sure!
[gttmn1e] (score 0, diepte 0) I've heard of memory foam sketchers but still not sure. Some say nike vapormax which is about  150 to 200 $. Anyone else have experience with these shoes and can you share your thoughts?  Thanks

=== THREAD 15340ts ===
SUBREDDIT: r/Target
DATUM: 2023-07-18  SCORE: 41  REACTIES: 80
TITEL: Does anyone else hate when people put their dirty a$$ feet up on chairs in the breakroom?
POST (source_id=post):
Or is it just a me thing?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[jshcazs] (score 193, diepte 0) Very little of what happens at work bothers me.
[jshamq8] (score 164, diepte 0) wait until you find out how much your coworkers dirty asses sweat in them things
[jshhgbq] (score 164, diepte 0) no, my feet hurt. it’s not hurting you. you should be changing out of ur clothes when u get home anyways so how does it really effect you.
[jshhod7] (score 137, diepte 2) ur mad people put their feet up in an already dirty break room. be so fr LMFAO
[jsi0p7x] (score 133, diepte 0) https://preview.redd.it/yeytsnyq9scb1.png?width=3024&format=png&auto=webp&s=1beadf5709abfe08eaa075bd5764af02b731266f
[jshkdb8] (score 123, diepte 0) doing it now bc my feet are throbbing 💅 and will never not do it! if it bothers you get your own thing of wipes and wipe the seat :p
[jshglq7] (score 62, diepte 0) If I’m on my 30, I’m putting my feet up. 6’4”, 300 lbs. I work in fulfillment, GM, and Front End. Even in my New Balances, I gotta give the dogs a rest during my shift or else my feet get so swollen that it impacts me the next day. Would you rather us put our dirty feet on the table where you eat from? Or the chair that only your back & behind cover? Better yet, how about I take off the shoes and put my stinky (but relatively cleaner than my shoes) feet up there so everyone in the breakroom can give ‘em a whiff? If it annoys you that much to sit in a chair that someone’s shoes have touched, go buy some of the bleach wipes we have in chems, they’re a pretty cheap solution.
[jshmzc5] (score 45, diepte 0) So you are crying that people are putting their feet on a surface that has nothing to do with any kind of food surface? 

Everyone is tired. We all walk around all day on our feet and not everyone has the most cushioned shoes. Go sit in your car if you have an issue with people trying to relax with the few minutes they are given.
[jshi2qa] (score 42, diepte 2) Are you taking the piss right now? Why should I adjust something necessary to mitigate my physical pain for your mental comfort? On top of that, if my feet are off the seat that doesn’t promote circulation which is how you reduce swelling from extended activity in the feet. I’m not arguing the fact that shoes (and by extension feet) are gross cause you’re right, they are. It’s a no brainer that the things that touch the ground are gross. This is ultimately a you problem; most regular folks don’t care about who’s propping their feet up in a common area, much less on something like a chair. Since you’re the one that cares, the onus is on you to do what you need to do to make yourself comfortable when you sit down. Not everyone else
[jshx2kh] (score 36, diepte 2) i heard it is actually good to elevate your legs after a long period of walking (like in fulfillment or general merchandise) because it lowers the pressure on your veins and “allows the blood that had been pooled [near the feet] to drain away”. 

so elevating or putting up your legs during a break can help improve productivity. (thats what i heard at least)
[jshocr7] (score 35, diepte 0) I’m willing to bet your ass is dirtier than my shoes tbh
[jsh88ge] (score 34, diepte 0) People do it at my store.

I think I did it once because my feet hurt really, really bad.
[jshnbkr] (score 29, diepte 0) On the chairs, I don’t really care. Thinking those plastic chairs arnt already caked with years of grime is just willful ignorance. Now if you’re putting them on the table or releasing foot fog, we got issues.
[jshnc2n] (score 24, diepte 0) if you care so much why don't you just wipe off the chair before you sit? i work fulfillment and sometimes my feet hurt like a bitch so i need to rest them
[jshxue8] (score 23, diepte 2) Bruh you made a whole ass post about people putting their feet up in the break room
[jsilgba] (score 15, diepte 1) Snail trails 🐌
[jsiau92] (score 12, diepte 2) You’re the one that was bothered so much to make a post. No need to get defensive because people don’t agree as strongly as you Lmao.
[jsht6xo] (score 12, diepte 0) Why does it matter, like your work clothes are going to get dirty regardless from the shift. I would be shocked if the tiny amount of dirt/dust from a chair was the dirtiest thing I came in contact with during a shift.
[jsike64] (score 11, diepte 1) Love your shoes
[jshjpfo] (score 8, diepte 0) i do. its a more comfortable position since i have back pain. only asses go there, which are already dirty
[jshupcu] (score 8, diepte 0) Do you also take into account people take shits with their bareass on the seat and I know for a fact dudes have no aim piss all over it too when it comes to using the TM bathroom.
[jshz7t3] (score 8, diepte 0) Just wait til you find out what else people put in those chairs, and what they do with THAT part of their body...
[jshw969] (score 7, diepte 0) Why would you just tell everybody you lay in the bed and sofa in your outside clothes like that 🤢
[jshvg24] (score 6, diepte 0) My hands touch way dirtier things at this job, I’ll never worry about someone’s feet being on a chair that my pants are gonna touch
[jshw1yo] (score 6, diepte 0) You sound like a wimp
[jshvv0x] (score 5, diepte 1) Yeah 👆This
[jshqsgd] (score 5, diepte 0) Why would you care? It’s not your chair the company who owns them in really could care less about you why should you care about them? Lol they could afford to replace the chairs in every store once a month and still make plenty of money I don’t see why you’d care maybe if they cared about you I could see it but respect is mutual.
[jsi7ahs] (score 5, diepte 0) Wait till you hear how much bacteria is on your phone. 

It's not someone else's home, so I see it as fine. At least they aren't putting their shoes on the table. 

You gotta learn how to pick your battles.
[jsidpps] (score 5, diepte 0) I think it’s very strange that you’d prefer people to take off their shoes filling up the room with the stinky ass foot sweat
[jshtboc] (score 4, diepte 0) No 
I'm always sore and it helps me get through my shift to be able to put them up
[jsiznzt] (score 4, diepte 1) Those shoes remind me of a baseball glove! Where did you get them?
[jsisapm] (score 4, diepte 0) Reading through these comments and from my own personal experience, nah. Sounds like a you problem. If you can't handle people putting their "dirty a$$ feet" on chairs in the break room, then you probably shouldn't be in retail. Btw how often do you wash the floors your house because the floors at target get washed daily, at least at my store.
[jshwh26] (score 3, diepte 0) As long as it's enough chairs for everyone coming in idgaf
[jsi7hnu] (score 3, diepte 0) I've just accepted that every single surface in the store is vile and powerwash my entire being as soon as I get home.
[jsiagan] (score 3, diepte 0) No I don’t really care a lot of times they do it because their knee/legs hurt and they may need to stretch it. No biggie. As long as I got a chair to sit on, go at it.
[jsibcpo] (score 3, diepte 0) Im rarely in the break room (I work starbucks so rarely get 15's and take my 30's in my car) but the times I was on the floor (store remodel, Starbucks closed for a while) there were times i just wanted my leg up for my break, or other times where I genuinely didn't feel good (unknown stomach issues) and having my leg up would help me a lot, especially if I was nauseous. Either way, there's much worse that goes into those chairs, I'd rather sit on a dirty footprint with my dark pants than someone's swamp ass puddle, the chances of those things being in a chair are very high when most of us can all share a common issue of having insanely hot stores.
[jsigifl] (score 3, diepte 0) As long as their shoes aren't wet I don't care.
[jsivdg4] (score 3, diepte 2) Should have apparently. No one told me when I started 8 years ago, but usually people are able to figure that part out.
[jsisszb] (score 2, diepte 1) I do it at the store and on public transit. I have no idea how anyone works retail and is at all bothered by it, honestly.
[jsis8ns] (score 2, diepte 2) Trust me, you don't want someone who also takes off their shoes in the breakroom 🤢
[ju659zv] (score 2, diepte 1) That or leaving used tp all over the restroom floor. I just want to know which trifling TM is doing this. Lol
[jshv39b] (score 2, diepte 0) Nah it’s the beard hairs, boogers, and piles of crumbs and soup droppings on the table for me. Just shows people don’t know how to clean up after themselves. I’m not bothered if my work pants get a little dirtier. Wipe down your chairs if you’re bothered by it.
[jshvbzq] (score 2, diepte 0) Nope, I even go as far as putting my calves on the corner of table with my feet hanging off to kick back.
[jsj3mdg] (score 2, diepte 2) Aha! Got them off stock x. They are Nike dunks
[jsi6qu7] (score 2, diepte 0) I sympathize with things bothering you that other people don’t get or understand, but I think chairs should be considered the same level of dirty as the floor from a germaphobe/OCD sufferer’s perspective
[jsi9bgj] (score 2, diepte 0) I prefer to put my feet up on the dash in the AC in my car on breaks lol
[jsio2bv] (score 2, diepte 0) Unless they’re taking off their shoes, picking their peeling foot skin and leaving it on piles on the tables, I don’t personally mind.
[jsip9mc] (score 2, diepte 0) Not really, no. Unless I’m getting paid to look after the people I work with, I don’t give a shit what they do. Even then I’m pretty lenient on my team.
[jsis30k] (score 2, diepte 0) This is why I wipe the table and the seat with the sanitizer wipes, while still on the clock. My ankles and legs swell, so I get why people do it.
[jsjbyjt] (score 2, diepte 0) I am tired🤷🏻‍♀️
[jsjokbo] (score 1, diepte 2) I cannot picture this. Can you explain it?
[jsjwukl] (score 1, diepte 3) you turn the seat so the the back is on either side of your legs, you put your legs up to where mostly your calfs/lower leg is on the seat. feet hang over the seat, off the side.
[jsitgcd] (score 1, diepte 2) I went to a job interview recently at a hospital and they warned me that I may have to deal with human waste. It took everything in me not to scoff and laugh as if our jobs don’t require that!
[jsiyi2z] (score 1, diepte 2) lmao
[jsimu7t] (score 1, diepte 1) Same
[jshuf0h] (score 1, diepte 0) I worked with a kid who put his feet ON THE TABLES.
[jsilk1q] (score 1, diepte 1) Hahahahaha
[jshw1np] (score 1, diepte 0) When is the last time you seen someone disinfect those chairs?? They cant get any nastier let people relax.
[ju65gq4] (score 1, diepte 1) I'd rather have shoes in a chair than smell someone's wet smelly foot bacteria.
[jsiutc2] (score 1, diepte 0) If it was the table, maybe. But the chair? Damn. Gonna get a sprinkle of dirt on my dark blue jeans.
[jsixg12] (score 1, diepte 0) UGH- no ty 😂
[jsizj0k] (score 1, diepte 0) I keep clorox wipes in my bag to clean my table and seat before sitting down. My feet throb. 

And honestly 99% of the people who walk into my break room don't even wash their hands so you should be wiping everything down anyway if you're that concerned.
[jsj2mqd] (score 1, diepte 0) I have a co worker of mine that cuts his finger nails in the break room. 🤮
[jsjg925] (score 1, diepte 0) never not putting my feet up
[jsjjmzs] (score 1, diepte 0) not much bothers me like that, but we had a guy who would legit take his shoes off and put his feet up. that was weird. shoes on, i’m like sure whatever, you do you, BUT the shoes off definitely weirded me out a tad. like self awareness, please.
[jsjl92a] (score 1, diepte 0) I do it but I’m not offended if it bothers you, we all have pet peeves, people got really heated over all of this lol
[jskaf6b] (score 1, diepte 0) We be using devices that are never cleaned and people stretching their legs on chairs is the biggest problem? If you have a problem with it just use a wipe and clean the chair you want to sit in people aren’t gonna stop putting there feet on chairs because people find it gross. Nobody gives a shit, people be putting their legs up and I’m jealous more than anything.
[jskbfz8] (score 1, diepte 0) There are antibacterial wipes everywhere in our breakroom. If it really bothered me, I'd wipe down the chair after wiping off the table. 

It doesnt bother me though.
[jsks82h] (score 1, diepte 0) i dont mind when it’s just on the chairs but i once saw a guy take his shoes off and put his gross smelly socks/feet on the table🤢
[jskz1ed] (score 1, diepte 0) What's worse, really, their sweaty butts, or the dirty feet?
[jsio43q] (score 0, diepte 0) Have you ever thought of how many team members dont wash their hands after taking a shit and touch all the equipment? Because, well... there you go.
[jsis7vh] (score 0, diepte 0) I've never actually seen that, I take all my breaks in my car. Can't stand the sound of people eating xD
[jsit881] (score 0, diepte 1 OP) Well, shit. Someone should have told me this 10 years ago when I started at target, I never would have stuck around.
[jsj0al1] (score 0, diepte 0) It is absolutely disgusting and disrespectful. That's almost as bad as people leaving all their trash and wrappers on the tables.
[jshb8nb] (score -3, diepte 1) nothing wrong with that. there's a way to do it without pitting shoes on the seat
[jshp668] (score -4, diepte 4) Yet they act like it’s home anyways. Honestly can’t deal with some of the nasty irresponsible ass shit some of my coworkers do in the break room.
[jsjjcda] (score -4, diepte 3) *Whole a$$
[jshhgt2] (score -7, diepte 3) I feel ya. people forget that there are neutral, and shared places in life where you can't just act like it's your home.
[jshzvhd] (score -8, diepte 0) People do that? Ew
[jsh61gy] (score -11, diepte 0) Gross. I've never seen anybody do that at my store.
(6 reacties met lagere score weggelaten)

=== THREAD 1ft5h3s ===
SUBREDDIT: r/pharmacy
DATUM: 2024-09-30  SCORE: 3  REACTIES: 79
TITEL: What are good shoes to wear?
POST (source_id=post):
My feet are starting to KILL ME. Like even on my days off my feet are extremely sore (mainly in the arch of my foot) and I’m starting to walk very funny when I’m barefoot due to pain. Maybe experiencing plantar fasciitis.. What kind of shoes do you guys use/recommend?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lppfxsw] (score 17, diepte 0) Hokas!

I can be on my feet all day with Hokas.
[lppnnmw] (score 16, diepte 0) Whatever you decide on, have at least TWO pairs of good shoes. You should not wear the same shoes two days in a row. They need time to dry out and for the insole to recover its cushioning that has been compressed by being worn all day.
[lpq2321] (score 15, diepte 0) Seriously though, get a ball (tennis ball to start, then progress to a lacross/massage ball) and roll out your feet.  It will be uncomfortable, especially at first, but you will absolutely feel the difference.  Think of it as deep tissue self massage for your feet.  Search YouTube for videos on specifics, or just start rolling 😁



Our feet carry a LOT of tension, and it carries up the body. (When my feet are particularly bad, I can feel it in my neck!).  Side benefits I've noticed rolling out: I feel more "connected" to the floor, especially when barefoot, and I find I'm steadier on my feet as a result.  My balance is better, and I have less pain in my feet.  Less likely to roll my foot or ankle if I step on an unexpected object in the dark (like a dog toy).



Hurts so good!
[lpq5olv] (score 15, diepte 1) Could you imagine if insurances covered a once a month foot massage since we’re standing on our feet all day? 🤪 what a dream that would be.

I’m sure I’ve read of pharmacists previously treating themselves to a massage every month or so. It’s the least we could do to treat our bodies after the physical demands of retail
[lppixf9] (score 9, diepte 0) Go to fleet feet and get your feet scanned. I tried all the popular brands prior and ended up with asics gel nimbus after the scan and have had no issues since.
[lpq2xgt] (score 8, diepte 3) Man you picked a pretty good nickname given these illogical, emotional, and insecure replies
[lppir1m] (score 8, diepte 0) Not sketchers
[lppyk0s] (score 7, diepte 8) Your threadddddddddd?
[lppq3ne] (score 7, diepte 1) I Combine with Compression socks and inserts.
[lppg25h] (score 7, diepte 0) Hokas or skechers! Life changing for me
[lppqm5l] (score 6, diepte 0) There is no shoe that is perfect for everyone. I wear brooks now but didn’t like Hokas. Wore sketchers for a while but the ones I had didn’t give me enough support throughout the day (other brands exist, just calling out that the ones mentioned in this thread may not work for everyone. YMMV)

Go to a reputable running store (or any footwear store) that will scan your feet and your walking pattern. 

Try on different recommendations, see what you like and don’t like. Ask about inserts as well. 

Be prepared to shell out ~150 for a single pair. Think of it as an investment in your future self.
[lppt4jc] (score 6, diepte 0) Good insoles are just as important than a good shoe
[lppicu4] (score 5, diepte 1) Your results may vary.
Hokas sadly doesnt work for me. Tried bondi 8, 7 and clifton 9s

My feet still hurt a lot especially the arches. 
😭
[lppznmz] (score 5, diepte 5) Yeah, I'm not sure why I didn't like the shoes either.
[lpq22hu] (score 5, diepte 9) Oh wow, that's pretty good. Thanks for the ideas and the engaging talk. I'll be sure to look into that.
[lppi7zg] (score 5, diepte 2) I have the arahi 6 and they seem fine for me!  I got checked to see what would work best for my feet though.

Haven't had any foot pain since switching and I'm in retail
[lppgwvz] (score 5, diepte 0) sketchers.

I'd recommend trying a Dr Scholls gel insert first as that greatly helped me too.

Also, I'm not sure these machines are in stores anymore but I used a machine at Walmart where you step on it and it shows you where you are putting all the pressure. I realized I was barely putting pressure towards the front of my feet so I would sometimes be mindful and lean forward to put more pressure towards the front and that used to help relieve pain as well.
[lpplf6d] (score 5, diepte 1) Brooks 100%
[lppite2] (score 4, diepte 3) Ok

have a day. :)
[lppvhqg] (score 3, diepte 6) Hello Karen or Chris. No one owns any thread. May the universe bless you
[lpq1of3] (score 3, diepte 7) Have you tried Fleet Feet? 

Boy, do I like Skechers, but maybe they can suggest something new.
[lpr7kas] (score 3, diepte 1 OP) Going to go this week! Never heard of this place but surprisingly have one near me! Thanks a lot.
[lppthl2] (score 3, diepte 0) The only thing that worked for me were the SOLE insoles. I struggled with pain for about a year and even tried physical therapy (which didn’t work because I didn’t do the exercises at home, so my fault). I just size up on new shoes and use the inserts with all my shoes and I haven’t had problems ever since.
[lpq1j7e] (score 3, diepte 1 OP) I bought those. They only helped for a week. I feel like they actually made things worse because I don’t have flat feel and i feel like my arch is not supported.
[lpqdqn0] (score 3, diepte 2) This should 100% be a thing!!
[lpqgb1z] (score 3, diepte 1 OP) I wouldn’t know it gets asked once a week cus Im not in this subreddit often. But thanks.
[lppsqk2] (score 2, diepte 4) That was a more mature reply
[lppop7s] (score 2, diepte 3) Hokas weren't comfortable for me. I do like Skechers though.
[lpq9l0n] (score 2, diepte 7) I'll have to check them out. I'm in the market for new shoes anyways.
[lprgl6x] (score 2, diepte 6) I’ve been wearing dansko over 10 years. However recently I prefer Sanita clogs since their production is in Europe while Dansko moved theirs to China. https://www.medelita.com/blog/the-difference-between-sanita-and-dansko-professional-clogs.html
[lpqi0n3] (score 2, diepte 1) This thread is atrocious.  You seriously make the worst threads.
[lppmzyd] (score 2, diepte 0) I like my allbirds but I have no feet problems
[lppsl1n] (score 2, diepte 1) I second going to a running store to find shoes that really work with your feet 


Hokas seem to get polarizing opinions so if you're gonna spend decent money at least mask sure it works for your feet
[lppxkwl] (score 2, diepte 0) Compression socks and ASICS
[lpqip07] (score 2, diepte 2) Damn that’s good to know. I’ve only had them for a month and they’ve been amazing so far. I guess only time will tell how long they last. 

I used to wear a pair of Nike Metcons at work then to the gym and they’ve lasted about 4 years. The cushion is not as good as it used to be but they still lasted a long time and I still use them in the gym. Might be worth looking into as they are not as bulky as the Hokas and look way nicer than sketchers.
[lpqo4iw] (score 2, diepte 0) Hoka’s and oncloud’s
[lprbfo1] (score 2, diepte 0) i think more important than shoes are good insoles. I've tried every brand of insoles on the market. Ultimately, I switched from my custom orthotics to this brand called [Fulton](https://walkfulton.com/) and nearly immediately my foot pain went away (and back pain). These are made from cork so they mold to your arch and absorb shock/impact & add stability. a bit pricey but obviously way more affordable than custom, and really comfortable.
[lprc7rz] (score 2, diepte 2) oh good luck!! i hope these help!! fingers (and toes) crossed for you
[lzyrjjc] (score 1, diepte 10) First day on reddit?
[lzyt4xn] (score 1, diepte 11) I could ask you the same, this post is 60 days old.
[lpsi79k] (score 1, diepte 11) Clearly 😂
[lpq4wtw] (score 1, diepte 4) Im a dansko person! They’re kind of clunky but combined with compression socks I’m not so sore in the evening/next day
[lpq6pwu] (score 1, diepte 6) It’s either Camdyn or Farrah. They’re definitely not cute lol but health > appearance.
[lpq56sp] (score 1, diepte 2) Im a Dansko person myself but definitely compression socks and most recently got inserts (so I can’t really review those yet but dang I didn’t realize just how flat my feet really were).

The compression socks I definitely keep for my longer days. But it’s also amazing how much my legs end up swelling when I come home and take them off
[lpphegi] (score 1, diepte 1 OP) Any type of hokas or a specific type?
[lppo2xh] (score 1, diepte 2) I use the binding. I believe they have the most cushion of all the hokas
[lprystq] (score 1, diepte 1) As someone who is tall/heavy and has back issues, Skechers are awful! I've found Hey Dudes to be the most comfortable weirdly.
[lpr3roc] (score 1, diepte 1 OP) Thank you!! This is great advice.
[lpq0r3c] (score 1, diepte 0) The closed toed crocs without holes
[lpr3a3h] (score 1, diepte 2 OP) I’m a new pharmacist and I’m actually considering this already. My boyfriend’s half assed foot massages are not cutting it anymore. I need a professional to deep tissue massage them, this pain is excruciating 😣
[lpq89j7] (score 1, diepte 0) Hoka Clifton 9! A LOT of cushion and support
[lpq8zbl] (score 1, diepte 0) Wolf and Shepherd
[lpqdwne] (score 1, diepte 0) I just picked myself up a pair of sketchers with the memory foam inserts and it’s patented “air cooling” tech. So comfortable
[lpqfhlu] (score 1, diepte 1 OP) I had 2 pairs of sketchers in the past. I found that they didn’t last as long as I would have liked. It felt like i needed to buy a new pair of shoes every 6 mos
[lpr122a] (score 1, diepte 3 OP) Yeah back when I used to be a tech working long hours, i ran through my memory foam sketchers every 6 months. Now that im finished with pharmacy school and am getting back into working full time hours on my feet again as a new grad pharmacist, I forgot how brutal this was.. I need something more durable. 😭
[lpqheat] (score 1, diepte 0) I like on cloud. I’m on my third pair. When my feet start hurting in them I know it’s time to get a new pair. I get a new pair every 8-10 months.
[lpqr45w] (score 1, diepte 0) Hoka one one
[lpqvsnf] (score 1, diepte 0) OnClouds. Beyond worth it. Softest shoes I’ve been wearing and less irritation in SI joints since wearing them.
[lpqwy6m] (score 1, diepte 0) hoka bondi, adidas ultraboosts,
[lpqxeb0] (score 1, diepte 0) Yeezy 350 v2
[lpqy6pr] (score 1, diepte 0) New pharmacists have this problem, including myself.  I found some Asics running shoes comfortable and more recently Merrill's , the kind with no laces.
[lpr7y9y] (score 1, diepte 1 OP) Yeeaaah. I used to be a tech full time in undergrad so my feet grew accustomed to standing for long periods. I started pharmacy school in 2020 and cut my hours to every other weekend for the last 4 years. Now that I’ve graduated and am back working full time, I am literally wanting to off myself on the clock. This pain is ruining me.
[lpr67d7] (score 1, diepte 0) Everyone’s feet is unique to them. It’ll be a lot of trial and error but it’s best to get fitted at a running store where they can perform tests to match you with the appropriate shoes. 

Like another person said, don’t wear the same pair of shoes two days in a row. Foam needs time to recover. 

Generally speaking, something with a larger surface area will be more comfortable for standing since its has more places to distribute weight, hence Hokas. I’d much rather wear New Balance Fresh Foam over Hokas if you’re taking aesthetics. 

Your arch, pronation, ankle or knee weakness, wide feet, etc. will all be factors in choosing the right shoe. Can’t just go off others’ recommendations.
[lprboa9] (score 1, diepte 1 OP) I will empty my bank account right now to stop this pain. Money is not an issue. Thank you so much, Im adding this to my list after getting a foot scan this week!
[lprchmk] (score 1, diepte 0) I can say I have tried so many different types of shoes meant for people on their feet all day and they’re all trash. They’re meant for people walking a lot. In retail we do a lot of standing in the same spot with occasional walking to the shelves and back to pickup and back to our computer. In my store I can pretty much reach what I need to with very few steps (unfortunately) so I’m more or less standing in the same spot all day.  All those “walking” shoes don’t really do much for us then. The ONLY shoes I can wear that are actually comfortable are Crocs. And like I said, I tried a ton of other shoes. They all did nothing. I read somewhere once that Crocs are better for standing versus walking and I hope it’s true because it’s the only shoes that I can wear. I no longer need to wear compression socks when I wear crocs. I leave them at work and only wear them in the pharmacy. Serious game changer. No one ever believes me and I was skeptical at first too but they are the best shoes I’ve had for work. They’re only $40 most of the time and yall are spending more on your Stanley cups so might as well give them a try!
[lprd9sc] (score 1, diepte 1 OP) I bought crocs. They were comfortable for a week. Then suddenly caused me an insane amount of pain and stiffness in my feet. I suspect because there is no arch support. The arches of my feet hurt badly. I feel like crocs are mainly okay for people with flat feet or something. I can walk around on them comfortably but standing in place with them has caused me so much pain 😭
[lps5bpt] (score 1, diepte 0) Compression socks did wonders for me.  I won't work without them.
[lq13v76] (score 1, diepte 0) It's already been said but: Brooks.

I've worked in pharmacy in various roles for 20 years. I've tried *a lot* of shoes. 

I wear nothing but Brooks these days.
[lq14fdh] (score 1, diepte 0) I rotate between Hokas and Altras
[lqd8ykz] (score 1, diepte 0) I just purchased a pair of Hoka Bondi and I love them ! They are so comfortable ! Plus I also noticed my co-pharmacist with me all owning hoka! Buy one and you won’t regret it!
[lpr845w] (score 0, diepte 9) What is your problem? Maybe they’re new to Reddit or just didn’t notice. Are you that insecure you have to call out everyone who comments under your comment? Is it really that big of a deal 😂 I feel sorry for you. Hope you feel better soon.
[lpr9zyn] (score 0, diepte 10) Clearly you’re not sharp enough to perceive the sarcasm in that response.
[lpq5fxm] (score 0, diepte 5) Which Dansko? I've never tried them before
[lpq1arn] (score -1, diepte 6) 🤦‍♂️
[lpq248r] (score -1, diepte 10) 👍
[lppz6cd] (score -2, diepte 9) Yes, you are a guest.
[lpq1rgd] (score -2, diepte 8) 🤦‍♂️
[lpqi833] (score -2, diepte 2) Thanks! 👌
[lppxs6s] (score -3, diepte 7) Sure, but since it’s my thread. I can dictate as I see fit.
[lpqg50n] (score -6, diepte 0) This question gets asked about once a week - do a little looking and you will find lots of recommendations. And none of them really matter because everyone’s feet are different.  Get some compression socks, and get fitted at a running store.
(5 reacties met lagere score weggelaten)

