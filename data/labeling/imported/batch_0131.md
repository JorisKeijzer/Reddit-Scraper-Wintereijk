# Label-batch batch_0131

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
Schrijf het resultaat naar `batch_0131.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 17dchw9, 1rx50tl, 1m99kf6).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 17dchw9 ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2023-10-21  SCORE: 85  REACTIES: 88
TITEL: recommendations for comfy shoes to wear around the house??
POST (source_id=post):
i have plantar fasciitis along with fibromyalgia and it hurts my feet so much to walk on the hard tile floors around my house and i’ve tried so many different types of house shoes but i haven’t found any ones that i really like :(

crocs are too hard and flat and regular furry slippers just make me get overheated because i can’t regulate the temperature in my hands or feet very well :/ 


p.s. u know those squishy anti fatigue mats that u can get for ur kitchen??? i wish i could have all of the flooring in my house made out of whatever that is

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k5vtyql] (score 41, diepte 0) I invested in a pair of Birkenstocks. Lifechanging for my feet. I thought they were overrated but the arch support is real.
[k5vvgsp] (score 21, diepte 0) I personally LOVE oofo’s sandals. Oofo’s have great arch support, are softer than crocs, and last a long time with regular wear.
[k5vy25g] (score 16, diepte 0) You should never walk barefoot with Plantar Fasciitis.  You are increasing the micro tears in the tendon that runs along the bottom of your foot.  The best shoe to wear is a hard soled shoe that doesn’t flex to allow the tendon to heal. No sandals or open back shoes either.
[k5w7ssn] (score 15, diepte 1) Another vote for Birks. I disparaged them my whole life because, idk … punk rock? And they’re expensive. I highly recommend getting fitted at a store if you can, but they’re easy to return online if you guess your size wrong. You won’t regret the investment. I have arthritis in my back and I think they help with that too.
[k5w520s] (score 10, diepte 1) I wear the Birks made from EVA foam (like crocs) inside, and regular Birks outside.
[k5wlm5a] (score 10, diepte 0) I love Sketchers and they make slippers
[k5vw2tm] (score 9, diepte 1) Yep, I wear Birkenstocks as slippers year round. And live in them through spring/summer/early autumn.
[k5vxq1l] (score 8, diepte 0) Vionic slippers are my favorite house shoes. They have a couple open-toe styles.
[k5w1bcl] (score 6, diepte 1) 100% Birks.

Around the house, I wear Zermatts in colder weather and Arizonas when it’s warmer.
[k5w7vtq] (score 5, diepte 2) The foam ones are great!
[k5wb7zn] (score 5, diepte 1) Oofos Oofos Oofos! This is the way.
[k5wg2ep] (score 5, diepte 1) Another vote for these. They are very reminiscent of the squishy mats you mentioned.
[k5wlhk9] (score 5, diepte 1) Yep! Oofos are my summer house shoes. I love them. Comfy and durable!

I do switch to memory foam slippers in the winter, but it’s cold where I live.
[k5x6ojf] (score 5, diepte 0) Birkenstocks are fantastic. The ones that were life changing are the all rubber/plastic ones. So soft underfoot. I had plantar faciitis and achillies tendonitis and could hardly walk. I slipped on the birkkenstocks and they were amazing!!!
[k5w5erl] (score 4, diepte 0) I cured my plantar fasciitis with Birkenstock Soft Beds. In like less than a week. I also had tile and hardwood floors and destroyed my feet by not wearing shoes with arch support. I now have LVP installed over my hard surfaces and it's much easier on my feet. But I wear Birks all year long inside and outside.
[k5wa26r] (score 4, diepte 0) Oofos have been a game changer for me!
[k5w4nkr] (score 3, diepte 1) Birks for life!
[k5wcu35] (score 3, diepte 1) Another Birk vote! Make sure to break in before saying you hate them. So many people don’t do a slow break in. If you didn’t have foot issues I would say fully go for it but you’ll need time. 

They make house slippers too. It’s how I got my husband used to wearing Birkenstock. Now he wears their boots and sneakers. He has horrible PF and refuses to do anything about it. 
Got my son into wearing them too. He works in a kitchen and wears their culinary ones. He has several pairs of the sneakers too. 

I like both types of footbeds but I don’t have any foot issues. Have around 30 pairs that include a few sneakers. Honestly can’t stand other shoes now. I do want to try barefoot shoes but I just can’t get seem to find any I like.
[k5xvutm] (score 3, diepte 1) Man I wish I could love berks! I think they’re so cute! Unfortunately, the little ridges between the foot and toes, plus between the toes themselves…. The pain KILLS me even just trying them on in-store. 

OP, have you tried real sheepskin slippers? I have Raynaud’s and issues with both heat intolerance AND cold intolerance. They’re the only things that keep my toes/feet a comfortable temperature. I live in them! [Here’s](https://www.uggsince1974.com.au/products/womens-genuine-australian-made-sheepskin-ugg-slippers-classic-slipper-natural) a pair I adore. I’ve had this most recent pair for almost 5 years now and they’re still going strong.
[k5wnptk] (score 3, diepte 1) Which Oofos do you all recommend? I’m new to the brand!
[k5xp57f] (score 3, diepte 1) Yes - Oofos all the way
[k5w3n01] (score 3, diepte 0) Orthofeet are really helpful and you can sort shoes by plantar fascitis on their website.   Also come in wides and extra wides if you need that.
[k5whatl] (score 3, diepte 0) I got you!!! These saved my feet!! https://www.amazon.com/BRONAX-Slippers-Lightweight-Bathroom-Platform/dp/B09TPFR22V/ref=sxbs_pa_sp_phone_search_thematic_btf_sspa?content-id=amzn1.sym.0a1d2d3a-9dd6-4aff-96a4-5a0a5094a2f8%3Aamzn1.sym.0a1d2d3a-9dd6-4aff-96a4-5a0a5094a2f8&crid=18OS7YEK2QVDS&cv_ct_cx=foam+sandals&keywords=foam+sandals&pd_rd_i=B09TPFR22V&pd_rd_r=1fe79410-5761-400e-9545-0bd10933c4b2&pd_rd_w=aQpCy&pd_rd_wg=H4V4j&pf_rd_p=0a1d2d3a-9dd6-4aff-96a4-5a0a5094a2f8&pf_rd_r=Z2MB2T7QF0AHW9HA5G8R&qid=1697932834&sprefix=foam+sandals%2Caps%2C235&sr=1-2-50a2b317-b617-44c1-b7a6-daec194a2368-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfdGhlbWF0aWNfYnRm&psc=1
[k5xfz1p] (score 3, diepte 1) Throwing in a vote for Sketchers. If they didn't make shoes, I'd be sunk. Bought a pair today, in fact.
[k5x8bj1] (score 3, diepte 0) There are two brands of wool slippers I love. The wool is breathable and not hot at all, Gieswein and Haflinger. Great support.
[k5xac91] (score 3, diepte 0) Sketchers, the foam ones (go walks?)
[k5xfic4] (score 3, diepte 0) Hoka shoes and sandals 24/7. Take the quiz for best type of outdoor shoes for you. Worth every single penny.

https://www.hoka.com/en/us/all-gender-footwear/ora-recovery-slide-3/1135061.html?dwvar_1135061_color=CKC
[k5x854o] (score 2, diepte 1) They were as good as I thought they’d be 🙁
[k5wei1d] (score 2, diepte 0) I may have to try some Birkenstocks but for now my crocs are getting the job done.
[k5y4c3x] (score 2, diepte 1) Yes sketchers all the way!
The sneaker ones with stretchy fabric material is like wearing a sock it's so comfortable and it breathes, so great temperature regulation. They are super lightweight and the sole is flexible. And the inlay is memory foam so great pressure distribution. I personally use an extra memory foam sole inlay on top. Oh and you never have to tie your shoelaces. They're amazing.
[k5y8ufi] (score 2, diepte 1) Another vote for Sketchers here. I’ve got a pair of flip flops with great arch support that are so comfy that I wear around the house.
[k5y8xq7] (score 2, diepte 2) I got a pair of their boots last year and they're as comfy as slippers
[k5woe0y] (score 2, diepte 0) You can spa slippers on amazon.. they are a fuzzy flip flop with memory foam. The maker is acorn. 

I have a pair for day and night.
[k5wy11x] (score 2, diepte 0) Oofoos. They were developed by an Orthopedic surgeon and Physical therapists.

They are not cheap for plastic clogs, but ohhhh do they make everything feel better.
[k5x012x] (score 2, diepte 0) Those anti fatigue mats are the best! I just have one at my kitchen sink. Shoes wise, I feel the same about crocs. For the longest time I wore Birkenstocks in the house, but I've switched to New Balance slides recently and they are much more supportive than I expected. A little squishier than the Birks.
[k5x0g7b] (score 2, diepte 0) Birks with the cork bed. They are the most comfortable shoe but you do have to break them in a bit so they mold to your foot. I absolutely cannot ever walk around barefoot.
[k5z1anf] (score 2, diepte 1) I love my Haflinger mules!
[k5xms12] (score 2, diepte 1) I have degenerative arthritis in my foot, have had multiple surgeries, and swear by Hoka. My podiatrist recommended them as one brand to try. She also recommended Oofas but they fit me weird. If you’re able to see a podiatrist I recommend it. Good luck 😊
[k5xzlgw] (score 2, diepte 0) Are you sure you have plantar fasciitis? Because fibromyalgia gives me pain which mimics plantar fasciitis, but I haven’t done enough exercise to actually cause it. But the good news is that it is easier to treat the mimic-pain than it is to cure plantar fasciitis. 
My recommendation is to get shoes cheap second hand from eBay from the brands recommended to you, so for the same budget, you can try out many different types of shoe till you find the right one - or the right ones. My feet like changing shoes, rather than wearing the same pair all day.
[k5zhvn8] (score 2, diepte 0) Oofos. Just wish they were cuter.
[k5zkjxg] (score 2, diepte 0) I live in Uggs but they may make you hot. For what it’s worth they don’t make me hot. I recommend Uggs, Coquette style
[k5zw6s9] (score 1, diepte 1) Agreed!
[k60wn85] (score 1, diepte 1) Yes, came here to say this! i wear them with socks around the house
[k5zjfl9] (score 1, diepte 2) I’ve only ever used the slide sandals- but it seems any of their products under sandal are similar and “award winning”
[kvucqrq] (score 1, diepte 1) Okay yes you are correct. So what is the best shoe to wear indoors for this?
[kvvkvtp] (score 1, diepte 2) A hard soled shoe to prevent the tendon on the bottom of your foot from grtting more micro tears.  Doesn’t natter what shoe as long as it has a hard sole.  Nothing is going to be comfy when PF is acting up.
[k5w2y1b] (score 1, diepte 0) Hoka one makes awesome "recovery" sandals that are like walking on a cloud, but they are not cheap! Ooofo also makes very comfy "recovery" sandals that are also pricey.
These are almost as good as the Hokas but about half the price if affordability is a priority:
KuaiLu Mens Recovery Sandals Orthotic Thick Cushion Open Toe Sport Slides, Reduces Stress on Feet With Comfortable Plantar Fasciitis, Joints & Back Post-Exercise
 
[https://a.co/d/5ewtW3g](https://a.co/d/5ewtW3g)
[k5wgm46] (score 1, diepte 0) "Sole" brans heat form orthotics were a foot saver for me. I've got 2 sets, one in my indoor shoes, and the other in my outside footwear.
[k61srac] (score 1, diepte 1) These saved me!!! I have far more pairs than any one person should own. The comfort is just incredible. So springy. So spongy.
[k63ze01] (score 1, diepte 2) Agreed! They feel like clouds!
[k5whjoy] (score 1, diepte 0) I recently discovered Aetrex, and they work SO well for my feet. I have a pair of the slides as my house shoes, and a couple of wedges that are similarly comfy. https://www.aetrex.com
[k5wij7d] (score 1, diepte 0) Ofoos are the BEST slides for in and out of the house. They are made for people with plantar fasciitis so lots of arch support snd super comfy. A bit pricey but sooooo worth it I have like 5 pairs now. They have slippers now I might need some 😂

https://www.oofos.com/?&&gclid=CjwKCAjw7c2pBhAZEiwA88pOFzaE1_dhUwveTZlYIqZvmNtwnUhicdSkhR8KC-uzPYtQcZdJY14I8RoCv64QAvD_BwE&gclsrc=aw.ds
[k5wnbnu] (score 1, diepte 0) Adidas comfort slides are great! They get comfier after you wear them for a while - a bit like memory foam. Make sure you get the comfort slides and not the others.
[k5z4unh] (score 1, diepte 1) Yeeesssssss. I wear mine all the time. In the winter, I bring them to work to change into. No one has said anything about them, but I wouldn’t stop even if they did. My Adidas slides are non-negotiable. 

I’ve dealt with plantar fasciitis for years but I don’t have any foot pain anymore, unless I wear shoes with no padding (*gazes longingly at my converse*).
[k5wnmst] (score 1, diepte 0) I hate Kanye west but Yeezy slides are what I wear around the house, very comfortable but not really affordable at all
[k5wy8i2] (score 1, diepte 0) My adias sandals. The old original black and white. I where them out of bed every day
[k5yf6tw] (score 1, diepte 1) Agree, best Birks ever.
[k5xf166] (score 1, diepte 0) Orthotics and Saucony shoes cause the insoles come out and they fit well with the orthotic.
[k5xo15s] (score 1, diepte 0) I swear Adidas slides around the house! I have a pair for throughout the day that I wear with socks (pre-fibro fashionista me is dead inside) and a pair that I put on after my shower and I'm getting ready for bed.
[k5xr4iz] (score 1, diepte 0) I put insoles in everything, including slippers. Without good foot support, no slipper is going to help. My feet are bothering me right now, enough that I’m putting my shoes on instead. Back to the calf/Achilles stretches.
[k5xttri] (score 1, diepte 0) Easy Spirit slip on . I feel like I'm walking on marbles . It's miserable. I recently got them from Amazon $45.. They're completely comfortable.  I would send you the link,  but I don't know how to.
[k5xvqsv] (score 1, diepte 0) It’s as if you read my mind. Thank you for posting.
[k5xxw80] (score 1, diepte 0) My mum can only wear hiking sandles these days because of the plantar fascitis pain. It's recurring and she struggles to be barefoot for even 10 min anymore. She wears one similar to the strava brand. Has about 4 pair now in different colours and wears them absolutely everywhere, and has an inside only pair.
[k5xy1uc] (score 1, diepte 0) I put some adjustable insoles in all my shoes, they are expensive, so I just have two sets I swap between shoes. 

(https://orthosole.com/shop/orthosole-insoles/) 

Took me a few day's of wear and swapping the supports about to work out the best setup for my feet, but they are worth every penny.
[k5xy4d2] (score 1, diepte 0) Oofos recovery slides! They are so amazing I almost never want to wear “proper“ shoes.
[k5y5iec] (score 1, diepte 0) Oofos recovery slides.

I have a foot and ankle conditions that makes plantar fascitis look like a vacation. Oofos recovery slides changed everything, huge increase in quality of life and ability to stand and walk around.
[k5y5z7x] (score 1, diepte 0) I wear Bobs slippers for indoors and skeetcher trainers for outdoors. With the Bob's slippers I can manage to stand to do for a while to do some ironing. Although Bob's slippers were £25 to buy best thing I've ever purchased.
[k5yd8lf] (score 1, diepte 0) Hoka Bondi during the day, crocs at night/home.
[k5yeeod] (score 1, diepte 0) I live in Birkenstocks with the soft footbed and have for many years
[k5yj5wx] (score 1, diepte 0) I wear birkenstocks Sandler's around. The cusion really helps.
[k5ysjzu] (score 1, diepte 0) Mephisto sandals, recommended by my chiropractor. First pair lasted over 10 yrs
[k5yx8a3] (score 1, diepte 0) Search for cloud slippers, similar to crocs but softer
[k5z5llp] (score 1, diepte 0) I also can’t wear most slippers as my feet will get way too hot, but there is one kind I can. These [Isotoner slippers](https://a.co/d/1gNxc4i). They have memory foam insoles and aren’t too hot, at least for me. Plus they’re slip on so they’re easy to put on and take off.
[k5z7ymj] (score 1, diepte 0) Chacos:  https://www.chacos.com/US/en/explore-product-features-1/#:\~:text=Chaco%20products%20are%20supportive%20and,support%20for%20all%2Dday%20wear.
[k5ze3i7] (score 1, diepte 0) I wear the Crocs slides and they're super comfortable. I couldn't wear Birkenstocks because the foot shape is so different from my own that they hurt.
[k60ii52] (score 1, diepte 1) You’re so right! They won’t win any style awards but they are so comfy.
[k5zp0oc] (score 1, diepte 0) Cushionnaire!!! I bought the slippers off Amazon. I have multiple other shoes for plantar fascitis, this one is by far my favorite and it's not as expensive. I think it was like $40. Bought my husband a pair also . It feels like you are walking on clouds. My feet feel utter relief when I slip them on.
[k5zpbu4] (score 1, diepte 1) If you are looking for that squishy anti fatigue feeling, these shoes will definitely do it for you.
[k5zyiub] (score 1, diepte 0) My podiatrist recommend Hoka recovery slides for my high arches/plantar fasciitis. They're really comfortable and supportive.
[k607gs1] (score 1, diepte 0) I wear happy flops or Birkenstocks around the house and the discomfort is pretty much nonexistent
(10 reacties met lagere score weggelaten)

=== THREAD 1rx50tl ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2026-03-18  SCORE: 20  REACTIES: 76
TITEL: Best shoes for foot pain?
POST (source_id=post):
My feet always hurt when I’m putting pressure on them, from the moment I wake up in the morning. I’m trying to figure out the best shoes for this pain when I’m still trying to do things like short trips to a theme park or an occasional concert. So standing and walking mainly, more of an every day shoe but probably an athletic shoe. 

So what’re your suggestions?

I’ve had a pair of sketchers for 2 years I like, but I feel like I could do better. I like their slip ins, but I’m overwhelmed on which “comfort technologies” I should look into most for foot pain? Anyone have sketchers specific thoughts as well?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ob5762k] (score 17, diepte 0) Size 300 of gabapentin a good socks 😂 💜
[ob59mpf] (score 13, diepte 0) Hokas - Clifton model. Gained a lot of weight, got clumsy, twisting my ankles but these are keeping me stable.
[ob4g34h] (score 8, diepte 0) I like brooks glycerin with my insoles. If you have a running store called fleet feet so there and het fitted. Its free
[ob4glq6] (score 8, diepte 0) You will hate this but walking boots with after market sport insoles are the only thing that works for me.
[ob5jcsm] (score 7, diepte 0) Another vote for Hokas here. I'd try on several pairs since they have various designs depending on your foot shape and stride. Also, don't forget good socks. As a matter of fact, I'd consider buying some athletic compression style socks as a first line of defense. Used to be you could only buy fancy running socks with compression ribbing on the instep, but I have been finding many department stores are carrying their version which are a little more affordable. A good pair of compression socks can help many pairs of shoes be more comfortable. I also have several removable pairs of insoles that I swap into my dress shoes or boots as needed.
[ob60767] (score 7, diepte 0) I travel a lot for work and the best "trick" I've found is never wearing the same shoes two days in a row. I switch between my Allbirds and Sketchers as well as sketchers for my sandals. The sandals have good arch support. 


I also fell in love with the brand after an interaction with them at promo shoot they were doing at the hotel I was at. I got chatting with one of the guys who told me it was Allbirds and I hapoened to be wearing my Allbirds and I got excited and pointed out my shoes. The dude got even MORE excited and told EVERYONE. Another dude came over and we were chatting just small talk as we were waiting for an Uber and when the Uber pulled up he gave me his card, turns out he was the global brand rep or something like that and told me to email him and he'll send me AND my friend new shoes! And he actually came thru and sent them! So they obviously won my brand loyalty as well. Haha
[ob5rp1c] (score 6, diepte 0) I’ve always relied on Birkenstock and Dr Martens for my orthopaedic needs.
[ob4ndbr] (score 4, diepte 1) Brooks are great for your feet, expensive but good running shoes help prevent PF flares
[ob4keuu] (score 4, diepte 0) I can completely relate. My legs are really sensitive to hard surfaces and harder the surface, the more it hurts. Plus I have bilateral sciatitica which makes me feel hell. Although I have recognised that the softer the sole of shoe or slipper, the less pain I feel.
[ob5le2z] (score 4, diepte 0) Stay away from anything that is super stiff and unforgiving like moto boots, stay away from slip ones like vans that are just flat rubber under ur foot w some fabric on top. Personally I like to get shoes that are at least half a size too big so I can really pad them out with multiple inserts with arch support, usually high tops tied tight to avoid ankle pain too. Really any shoe that isn't super flat or stiff. A lot of skate shoes have nice built in extra padding too.
[ob4j0ed] (score 3, diepte 0) I go through this with my heels. I’m sorry you are going through this as well. 

For slippers inside I have found that the thicker the sole or hard soles that have memory foam that doesn’t deflate after wearing them works wonders. The more space between my feet and the ground the better. You can tell what memory foam is going to work by pressing on it in the stores. 

Outside shoes are TOMS (look for sales shoes). Court Tennis Shoes have become my go to for outside too. I have found Puma’s to be the best. They are made with a thick sole and their memory foam holds up. I wear a 6 1/2, so I end up in a 7 or 7 1/2 because of the thick memory foam. 

You can find the slippers and Puma’s at Burlington, Ross, TJ Maxx and Marshalls. Slippers start at $14.99 and lower. Puma’s range between $29.99 to $39.99.
[ob4msbr] (score 3, diepte 0) I really love my Crocs. I get the ones with the thicker sole/ platform. I have regular ones and sandals and both of them are super comfortable and I can wear them all day!
[ob5dgnc] (score 3, diepte 0) Hoka shoes are all I can wear.  I was able to do Sketchers until recently.  Anything else I can’t tolerate! Crocs. Nope.  Nike. Nope.  Sandals. Nope.
[ob6c10e] (score 3, diepte 1) I always thought Doc Martens had no support.  Am I wrong?  I’d love a pair lol.
[ob8zr8n] (score 3, diepte 1) I needed a "the world isn't all bad" reminder today- so cool. What an awesome thing for him to do.
[ob5zf5p] (score 2, diepte 2) Ya its helped me a ton. I have some nice hokka boots bit i think the key was the insoles i was fitted for
[ob4sy2k] (score 2, diepte 2) Thanks. Yes it is horrible. Plus I think fibro amplifies it.
[ob5l30b] (score 2, diepte 1 OP) I want to love crocs, but the one pair I’ve bought has the pokey bits in the foot bed and are so painful to wear 😭
[ob6ar1h] (score 2, diepte 1) Ooh, which socks?
[ob8wwwr] (score 2, diepte 2) Not my original comment, and they're obnoxiously expensive if you can't find them on sale, but "wright socks" have been awesome for me. 

They have 2 thinner layers (to help avoid blisters, etc) and back when I would run I wore them almost exclusively and never had any issues. Still my favorite socks in my drawer.
[ob723ux] (score 2, diepte 1) I have a pair of these and I love them. I work retail and asked the employee at the shoe store what her favorite work shoes are and she recommended these. I was using a pair of New Balances with custom insoles before and they weren’t near as good.
[ob6nwhr] (score 2, diepte 2) A pair of arch support insoles might do the trick. They have cushiony soles, which is why they came to mind for you. They were originally designed for people who were on their feet for long periods.
[ob7s3w6] (score 2, diepte 2) I swear by my Docs! I can wear them for hours and my feet don’t feel like they are bleeding. For wear and stability, it’s Doc Martens all the way.
[ob7qf18] (score 2, diepte 1) I said the same thing! Life savers especially since I’m a college kid that has to walk all over campus
[ob63ave] (score 2, diepte 0) Man, I feel you! Foot pain from the moment you wake up is the worst. From my experience, it’s all about support over fluff. Forget the ultra-soft memory foam unless it’s paired with real arch support, Skechers Arch Fit line actually does that and is way better than their regular slip-ons. Hoka Clifton/Bondi are like walking on clouds all day and Brooks Adrenaline gives more structure if your arches need help. Honestly, throw in a good insole and a few stretches for your calves and arches and you can survive theme parks, concerts or just standing around without hating your life.
[ob654ue] (score 2, diepte 0) I've had many sneakers over the years that were amazing for 6 months and then hurt my everything. They had no visible wear, or anything like that so they hadn't broken down. I found the secret was insoles. I, too, was overwhelmed by all the drug store options and terminology.

I found the fp insoles from an instagram ad (the bowling ball ones if you've seen it). They're advertised as super duper shock absorbing for athletes. I figured, give them a shot, see if they absorb the painful surfaces I'm always on. They're amazing. I bought the custom insole ones, that you bake in an oven on super low temperature for 3 minutes, then wear and they mould to your foot. I have instep support, and they made all the difference for standing for long periods.

Another secret is: many pairs of shoes. A lot of people only wear the same pair of shoes day in and day out, which apparently is bad for your feet. You need to switch it up daily in order to keep training your muscles.

Third secret: graduated compression socks. You want light compression to start with, as I find that wearing compression for too long can be more painful. But for those extra bad days, add in a bit of support to your legs, feet, and ankles.

If you like sketchers, stick with sketchers. I'm partial to Puma, and I especially like that I can wear the kids sizes so I get cheaper shoes and more fun options.
[ob6dm8w] (score 2, diepte 0) This is out of left field and doesn't help everyone, but have you tried barefoot shoes? They're the only type of shoe that helps my foot/knee pain.
[ob7rlj2] (score 2, diepte 1) I've been wondering about those. A friend of mine Raves about them and I was thinking of trying some barefoot sandals this summer.
[ob7vzm0] (score 2, diepte 2) I used to work as a nurse aide at a hospital and I tried every shoe under the sun. Barefoot shoes were the only ones that didn't cripple me after a long shift. Plus my proprioception is god awful so it really helps to have as much feedback as possible.
[ob6oa76] (score 2, diepte 0) I like Hokas but they are expensive. A key aspect a lot of people leave out of this convo though is that most people are not replacing their sneakers when they break down. About 300-500 miles of walking or generally once a yearish for most people. (The more you're on your feet the sooner you should replace them essentially). And it's not just the treads, the cushioning can compact and the support structures start to break down. The best constructed and comfortable for you shoe you can afford to replace annually is the shoe you should be wearing.
[ob8za0q] (score 2, diepte 0) OP!! I know this has been commented on a bunch, but I'd strongly recommend going to a ***small running store*** in your area. Not one of the chains, definitely not in a mall. 

The smaller, mom and pop running stores are a little more niche, and in my experience the staff in them are *awesome* at looking at your feet, how you walk, what your problem areas are, and getting you into the right  shoes for you. They can also help with inserts if they think you would benefit from them. 

Imo runners are the people to ask about shoes and foot issues. Some of the stores I've been in have even had different surfaces or small paths in the store you can walk on to really get a feel for what feels best for you. Cannot blindly recommend you to your local running store enough! 

You could always go in person to try on different shoes and order online if it's more expensive in store. I've also had stores offer to match online prices as well. Not to nickel and dime them, but I've been on some pretty tight budgets in the past and good shoes are expensive. 

That said, I've had plantar fasciitis in the past, so:

1. if I'm going to be on my feet a lot, I'll wear an arch support- they look similar to wrist sweat bands if that makes any sense. Just slide your foot in and they sit mid foot in a O around your foot. Please google, I'm doing a horrible job describing them ha. 

2. Dropped heel shoes have been night and day for me. I do ***so*** much better in drop heel shoes in terms of pain, fatigue, everything. I love my Altra sneakers, they're the only brand I'll buy now. They are pricy, but you can usually find deals like REI right now is doing 20% off a regular priced item for members; I've also got some on Amazon, but 100% don't buy without trying them on first, dropped heels aren't for everyone. 

3. Toe spacers. I have a bit of a bunion on both feet which is usually fine unless I'm standing/walking all the time. But if I get home and put these on for an hr or a few hrs, I really does help.
[obe07gc] (score 2, diepte 0) ASICS runners. I can’t wear anything else for too long except my ASICS .
[ob5l51e] (score 1, diepte 1) Running stores generally are incredibly helpful. I got fitted at a local one and it was great.
[ob6ag1h] (score 1, diepte 3) That's awesome! They got me a pair of ON running shoes and showed me an alternative way to lace them so they don't hurt the top of my feet. Could not recommend more.
[ob4lhc4] (score 1, diepte 1) Hugs. Bilateral sciatica sounds horrible.
[ob6wcp9] (score 1, diepte 1) Make sure you wear socks because your feet absorb chemicals from the Crocs as the shoes heat up. I love my Crocs too!
[ob4uaky] (score 1, diepte 0) I went to see a podiatrist last year and my feet are all sorts of fucked up (RA, hypermobile, fibro). On her rec I got some speciality structured trainers (Nike Structure, but tried a few brands before deciding on the Nike ones), and they’re amazing. My feet love them.
[ob4wc0r] (score 1, diepte 0) For fun sneakers I wear comfy cush vans. For athletic sneakers I wear On sneakers and for Chelsea boots I wear Sorel Harlow boots. I also have had back surgery and I have bunions I'm a mess lol
[ob5iq4g] (score 1, diepte 0) I can't tolerate sketchers. I have been using footwear from this brand called Happenstance - they have sandals and shoes, and about the only thing I'm able to be comfortable wearing. Not sure if it's available outside my country though.
[ob5jety] (score 1, diepte 0) I have the same trouble, orthotics have not helped in my case as the pain is in the connective tissue and in between all the foot and ankle bones.
[ob5lscn] (score 1, diepte 1 OP) Yeah, when I went to the podiatrist they said there’s nothing wrong with my feet 😭 so he said orthotics would do nothing for me! Now I’m on the search for the softest cushion shoes that last the longest
[ob5ogcu] (score 1, diepte 0) I’ve switched over to Oofos for slides and they’re very comfy, think crocs but not as weird looking and not a clog. I can wear these all day without getting fatigued. For walking / running I went to get fitted properly, it did cost a lot more but I’ve got issues with my feet and gait etc so it did help in the long run as opposed to buying a pair of Hokas online as I wanted to (and I still kinda do but I think try ons are definitely required due to the price point). 

Something else I have recently tried are Pilates socks (for grip) at home but the compression kind.  So I keep my feet warm and the little grippy dots keep me from falling over cause stability ain’t my thing and I also get to kind of train my feet (grounding them, spreading toes, stuff I learned in Pilates to help with stability).

It’s not a one size fits all i have learned, and best of luck finding something that works and gives you relief that is affordable (cause we know pain isn’t cheap!). Compression socks are actually pretty great and they have them in super cute designs, sometimes with extra features- even padded etc
[ob5r587] (score 1, diepte 0) The only shoes that have been keeping my feet pain free is the Hoka Gaviota and the Hoka Cielo x1. I had to give up my Doc Martens, my Nike's and all of my high heels because it was just way too painful to wear them.
[ob5rfjc] (score 1, diepte 0) Orthofeet with the stretchy tops but the key is to pair them with sock liners and bamboo socks. Make sure you buy them about a half size larger than normal.
[ob91107] (score 1, diepte 3) Oooh! This reminded me of a pair of dansko clogs I had like, sheesh, years ago when I needed "professional" shoes but was walking a few miles per day between all the back/forth. There's a reason they got so popular in the medical field back in the day! They broke in easily, and I swear they were the *most* comfortable shoes I had owned up until that point, and despite significant wear and tear, they always polished up well and looked nice. 

Maybe not the most fashion forward anymore (?) ha, but if sneakers don't fit the dress code, I'd definitely recommend dansko clogs.
[ob5szag] (score 1, diepte 0) I had plantar fasciitis for years it left within a few days once I switched to barefoot shoes; I bought men’s shoes at first which are wider and helped and I’ve only purchased barefoot shoes since. Currently I have Origo sneakers which are good and some from vivobarefoot they are pricy but legit my feet no longer hurt! Every single morning I’d wake up it felt like I was walking on bruised feet
[ob5t4e3] (score 1, diepte 0) Another vote for Hokas. A lot of nurses wear them. I love Clifton 10 in wide. I have custom orthotics. Also recommend Dr Motion diabetic socks. I’m not diabetic but I hate compression socks.
[ob5viu4] (score 1, diepte 0) I like Vionic
[ob5y04k] (score 1, diepte 0) If you need a waterproof Chelsea boot, blundstones have been my go to for years. I get really bad chilblains sometimes and it doesn’t aggravate that. Not too heavy to wear in summer, great for walking on various terrain and offers at least some ankle support. They are sturdy and one pair gets a lot of mileage.
[ober0h2] (score 1, diepte 1) Yes to switching up your shoes regularly!! Hokas and Birkenstocks have been great for me. I love Kiziks for quick trips or walking around the house-but have to add insoles if going to be wearing them long. 
I’ll have to try a pair of Allhirds. I’ve been getting ads for them recently.
[ob918th] (score 1, diepte 1) If you ever run into needing to find a different insole, smaller running stores have workers who will explain what you want based on your foot. Some of them even have machines to make custom insoles in store.
[ob6cgy5] (score 1, diepte 0) Odd recommendation: Cowboy boots. The real ones that are meant for working and come from the feed store. I have a pair of Justin boots that I can slog around in all day. Sometimes highly structured boots/shoes are way better for pain than cushy insoles because they keep your feet from moving around when they shouldn't. Bonus: Cowboy boots don't need to be tied, so you don't have to bend over.
[ob6ubf1] (score 1, diepte 0) I love most styles of Orthofeet. I have boots, sandals and trainers. Great return policy. Buy straight from the company.
[ob78bzq] (score 1, diepte 0) Alegrias are my brand of choice.  They're expensive if you buy them new but I've had a lot of success on Poshmark and eBay getting them half price or better, even if I replace the soles.  They're the only brand I can consistently wear without dying in pain the next day.
[ob79tb9] (score 1, diepte 0) I wear Hokas for work and Skechers to go out in.
[ob7d3ot] (score 1, diepte 0) Another vote for Hoka. The Gaviota sneaker for out of the house and the recovery slides for my house slippers. 

I do also really like Crocs Dylan Platform. Took me awhile to get used to the insole and man my feet sweat, but they’re cute and sooooo good for pain. 

For winter boots, I did the Timberland Roxie Lane which has been great for support, but worth knowing they run a bit narrower than the other shoes I wear.
[ob7m234] (score 1, diepte 0) Hokas. Life changing.
[ob7q8vq] (score 1, diepte 0) Words from my own rheumatologist, BIRKENSTOCKS!!! They used to be my daily shoes (still are in the summer) but I got some new Mary Jane doc martins that also do well on my feet
[ob7sxsd] (score 1, diepte 0) Brooks
[ob7varu] (score 1, diepte 0) Barefoot shoes (or at least very wide) w/ thick socks while you get used to it. It hurts at first but it'll improve as your weight gets more evenly distributed across your foot and overall gait improves as a result of said redistribution. It also helps balance, which ik is big for me
[ob7zjsb] (score 1, diepte 0) Hokas and oofo slides
(26 reacties met lagere score weggelaten)

=== THREAD 1m99kf6 ===
SUBREDDIT: r/Fibromyalgia
DATUM: 2025-07-25  SCORE: 21  REACTIES: 69
TITEL: what shoes have worked best for you?
POST (source_id=post):
i’m recently diagnosed and am making many adjustments to my old lifestyle—including finding painless shoes. 

the top picks are currently hokas, orthofeet, or kuru. do you guys have a favorite brand, or just use orthotic insoles? pls share! 

i did the wet test to see if I have flat feet and it looked normal. but the pain when I walk is always in my arch, so I’m not sure if i need arch support, or just better cushioning and more structure. i should probably see a podiatrist but it would just feel like a waste of time for them to me it’s fibro pain.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n55g7if] (score 11, diepte 0) Skechers and/or Hokas.  There are over 200 issues associated with  Fibromyalgia.  Some of them involve feet.  See a board certified  podiatrist.
[n55iebj] (score 11, diepte 1 OP) i’ve been putting off making an appt because i’m so tired of not getting answers/solutions! but ur right- thanks for the push, i’ll look into it now.
[n57pz9h] (score 8, diepte 2) I just started seeing a new provider who has many Fibro patients. He went through my complete medical history before I had even met with him and then asked me multiple questions during our appointment. He spent over an hour with me and even invited my partner to come in to be my advocate and hear our discussion about my case. Additionally, he not only caught spurs and compression in two of my vertebrae (my primary doc & a radiologist looked at the same recent X-ray and said they didn’t see anything out of the ordinary despite my repeated complaints of pain in exactly the C6 & C7 area) but ordered an MRI and asked why I’d never seen a podiatrist if I have tingling in my feet and occasional zaps of pain. I haven’t been yet but I had no idea to even ask for this. That’s why finding a caretaker who is an expert in fibromyalgia can be such a gift. He said that so many docs see that “fibromyalgia” diagnosis and just automatically assume everything wrong with you is fibromyalgia pain, I.e., they stop looking at individual symptoms/complaints and don’t research for an underlying cause.
[n55sizp] (score 8, diepte 0) I went to Roadrunner and got the foot scan and custom insoles (~$100). They recommended New Balance 860v14 because I needed stability. The insole works okay in some of the shoes I already have but I just got a pair of the NB and it’s definitely way better with that combo.
[n55qlf5] (score 5, diepte 0) I love my kiziks for walking the dogs. The 'step into feature' works really well and they are really comfy for my wide, short feet. I know some other brands so the step in, but I haven't tried these. But the kiziks I haven't had to untie or tie since the first time. Bending over to tie the shoes always hurts my back and belly :( 

I also recently got given a pair of croc style slides (I think nautica?) that I NEVER would have bought but now I can see why chefs wear them. Easy for quick trips out of the house or even in the yard. The lack of a back prevents any blisters and they just..float with your feet. Easy peasys
[n55tj24] (score 5, diepte 1 OP) thanks for sharing! didn’t know sports stores did foot scans! i’ll look into it :)
[n55i6et] (score 4, diepte 0) Hokas were life changing for me. I love them.
[n57r8gw] (score 3, diepte 2) If your insurance offers integrative care, see what they can offer. I’ve seen an acupuncturist for a couple years and now a chiropractor doctor who turned out to be a fibromyalgia expert. He’s now referred me to a podiatrist also in the same integrative clinic. He hasn’t even done an adjustment yet. He wants to avail me of every option for treatment of my worst symptoms.
[n59sz95] (score 3, diepte 2) I firmly believe that every Fibromyalgia patient should have a pain management specialist.  Even if you only see them every six months to remain an active patient in the practice.  If you ever end up in ER or need surgery they are an invaluable tool. 

Also, every Fibromyalgia patient should have an in lab sleep study done.  Fibromyalgia interrupts the deep sleep cycle with short bursts of high intensity brain activity.    Lack of restorative sleep causes an increase in pain, fatigue, headaches and loss of cognitive function.  See a sleep specialist too.
[n561em0] (score 3, diepte 1) It’s funny, I thought I liked hokas, but only recently figured out after years of wearing them that they were causing my back to hurt worse when I wore them for walks. (I’m dealing with fibro pain and pain from a herniated disc.) Now I take walks in my Birkenstocks and the pain is much less. I know a lot of people who love hokas though.
[n55rbw3] (score 3, diepte 0) following bc i need the same advice 🥺
[n55s0yv] (score 3, diepte 0) I have wide feet, small bunions, and a high arch. I basically live in Crocs or Docs. And I need to put a high arch support insert in my Docs. 

Being barefoot and standing for any length of time causes me a searing pain, like standing on hot coals. So I basically live in Crocs when I am home.
[n560yy0] (score 3, diepte 0) I have high arches. Clark’s shoes were the best for working. Even got me over a case of plantar fasciitis one time. Vionics are good also. Definitely Sketchers for everyday!
[n56kema] (score 3, diepte 0) Honestly, I have zero foot pain now that I switched to barefoot/zero drop shoes. If I wear anything else, I end up hurting. I can get away with Birkenstock sandals on occasion but not two days in a row. The last sneaker I tried to wear hurt my feet, legs, and back before I even got out of the house.
[n56mu14] (score 3, diepte 1) Yes I was going to suggest barefoot shoes! Or at least that’s what’s worked best for me. So many of the pains I used to have went away. Some I even forgot about until I tried wearing crocs again and realized that some of my pains came from most non-barefoot shoes not being flat and so bending my toes backwards with every step 😬 and my feet have much better alignment now, and when I need a little extra ankle stability, I just wear little barefoot boots with laces and that gives me enough. I have hEDS and a million things but yeah I have never been happier with shoes than since switching over to barefoot. It does take time to do it slowly so you don’t hurt yourself in the adjustment but yeah big fan
[n575me2] (score 3, diepte 0) Try Oofos.  They're amazing! I've got the flip flops, slides & lace ups. Worth every penny and you can find them on sale    ☺️ can't wear anything else and I've got neuropathy in my feet as well
[n55g4jn] (score 2, diepte 0) I like flats with support and 2 inch platform sandals that are effectively flat to my feet. Can no longer wear heels or any higher heel. Lumbar surgery stopped the heels
[of2qdrj] (score 2, diepte 3) I don’t know if it’s okay to respond to a comment after this much time.  I’m still learning this app.  But I was looking at footwear, seeing so many ads for Hike footwear.  I ended up getting Hokas  for support.  
But I really wanted to say that Your provider is really awesome! Mine never even mentions my fibromyalgia.  He didn’t diagnose it himself, I actually saw a Fibro specialist out of town for my diagnosis .  I wonder if that’s why.   My primary is with an integrative practice, and sends me to pain management for pain related symptoms.  I never knew a podiatrist could help.  I’m so glad you spoke up.
[n56spti] (score 2, diepte 1) As someone who’s newly diagnosed, I appreciate your insight. Everyone’s experience is different, but I wonder which other specialists I should start hunting down.
[n580ww0] (score 2, diepte 3) Thank you for this! It’s great you’re building such a comprehensive care team. I started seeing both an acupuncturist and a chiropractor this year, but for other issues. Luckily the main issue is in the past, as I’m two weeks post-op and healing well. Now I need to double down on addressing the fibromyalgia and osteoarthritis diagnoses I’ve picked up this year.
[n5bwrqr] (score 2, diepte 4) Sounds like we’ve had similar journeys. I’m almost 7 years in now but have also had surgeries and a car wreck since. As well as an osteoarthritis & bone spurs diagnosis. Good on you for seeking treatment not just for the tangible stuff (if that makes sense) but also the weird randomness fibromyalgia can throw at us.
[n5bx8cf] (score 2, diepte 5) Interesting. So sorry to read about the surgeries and car accident. And the bone spurs in both my hips thank you!
[n55l9ls] (score 2, diepte 2) That's mainly what I use- have a couple of pairs. I also look for max stability and cushioning. I also have a pair of hiking boots and a pair of hiking shoes. I walk a lot and before Hokas I was getting plantar fasciitis from time to time.
[n62itj8] (score 2, diepte 4) Also, Hoka. Can't remember the specific names of the model. The boots are a few years old- I don't think they make that particular model anymore. The shoes are some hiking shoes- can't remember what they were called. Remind me to check them and get back to you.
[n55jwqe] (score 2, diepte 0) I have a pair of brooks cloudwalkers. Also don’t cheap out on replacing them often enough for you.
[n55tvbw] (score 2, diepte 1 OP) never heard of that brand. thanks for the recommendation!
[n56bl83] (score 2, diepte 1) Same for me: Crocs at home and Docs everywhere else now.
[n567bfy] (score 2, diepte 2) This is how I buy my shoes.  I recommend doing it this way because in my experience, I choose a different brand every time.  I don't know if it's weight gain, age, pregnancy or what but I don't consistently buy the same shoe. 

Don't be afraid to veer from their recommendation. I think they recommended like C width but I went with a wider shoe. Run around the store, turn sharp corners don't be shy make sure the shoe really really fits.
[n59rvk7] (score 2, diepte 2) Came here to say I went to a place that did foot scans & gait recordings & spent over an hour finding the right shoes & socks for the most comfort. My whole body felt better in the new shoes. I went w/ Solomon shoes, extra comfy inserts & feetures socks. Life changing. Still painful feet but way better than before!
[n59swrx] (score 2, diepte 4) All the shoe store places I've been to, that do the mapping, did it for free! The first place wanted $1000 for their shoes & inserts. Yeah right! The second place did even more Intel into my feet for free, way nicer & more info & only wanted $250 for shoes, socks & inserts. Find a free place!
[n59tck9] (score 2, diepte 5 OP) thank you!
[n562o5f] (score 2, diepte 0) I did the test to find the proper shoe on Brooks' website. The shoe it recommended, the Adrenaline GTS, has worked great for me. I've used those shoes exclusively for 5 years now and I notice a huge difference in pain if I wear any other shoes, even if it's a different model of Brooks shoes. I've also got really bad fallen arches so I swear by Dr. Scholl's Plantar Fasciatis inserts and it really does make a difference.

Added bonus is they have black shoes with black soles so I wear my Brooks to work instead of dress shoes. Total game changer.
[n5cvsx1] (score 2, diepte 1) Brooks ghosts have been great for my wide feet. Hokas are suffacating and i dint like the excessice squishy. Brooks shoes are a better balance of soft and firm.
[n56bpen] (score 2, diepte 0) My favorites are Skechers currently. And my mountain hiking shoes perhaps even better, because the Skechers are tearing through the spot above my heels, now that they're really worn out. But they were great when they were still intact.
[n56lxyw] (score 2, diepte 0) I use Birkenstock sandals (with socks, don't judge) for every day errands, Hey Dudes if I'm out but not walking a lot (like movies or casual dinner), and kiziks for when I need to walk a lot (like walking the dog). 
The birks are great because they're solid, so they keep my feet from flexing weird.
The Dudes are super lightweight and look less casual than sandals for being out. 
The kiziks have the best support, I never need to fix the tongue or tie them, and the hands free heel hasn't worn down at all. They fit perfectly snug so they aren't rubbing my ankles or sliding off constantly.
[n56lyb1] (score 2, diepte 0) You need to go to a shoe store that has you walk in the store or on a treadmill to fit you with the correct type of shoe.  The shoe that is right for me may not be right for you!  Hokas are awful for me!  All of my foot doctors say New Balance or Asics.  I have worn the same shoe since 2000.  All 3 of my podiatrists recommend the same shoe for me. As bad as my feet hurt and I want soft comfort, those are not the right shoes for me.  When the first Dr. handed me this stiff shoe insert, I thought he was crazy!  Stability shoes are what I need.
[n56pkhv] (score 2, diepte 0) Hokas, Oofos, Fit Flops. On the higher end - Donald Pliner and Robert Clergiere. Purchased on sale and the quality is there -last super long, comfy, and look amazing. But I always go back to Hokas.
[n5be8he] (score 2, diepte 1) Agreed!

I tried Oofos once and got hooked and ended up giving away most of my other shoes, that's how great they are. 

Whatever fat pads I used to have under my heels are completely gone, and at some point every step I'd take or every moment standing became torture. My ortho gave me gel heel cushions which really helped, but were impractical with slip-on shoes which are all I wear. I actually tried gluing and stapling the heel cushions to my Adidas slides which was mostly a disaster.

Oofos have so much cushioning and I've had so much relief from them it's incredible. I wear them all the time, in and out of the house, and now I'm back to walking a lot more and can do dishes/laundry/etc without severe pain.

Their return policy is great so if you try them but don't like them you can return them for a full refund. I swear by the slides, the flip-flops didn't work as well for me.
[n5799rp] (score 2, diepte 0) I’ve been wearing [Parasole recovery socks](https://kytin.com/) as shoes and my foot, leg, and back pain disappeared within a week. They’re machine wash and hang dry.
[ofbtcmp] (score 1, diepte 4) I think you were replying to someone ahead of me maybe but I did want to mention just in case that the doctor I saw is not my primary—he’s a doctor of chiropractic medicine and he’s part of an integrative medicine office. I also see an acupuncturist there (or did before it got cut from my benefits), and a physiatry doctor. I was supposed to undergo a medial branch ablation surgery this very week to relieve that C6/C7 pain but my benefits wouldn’t cover it so I had to cancel. I can still get trigger point injections though. I have been helped by the integrative health physicians more than all my other doctors over the years combined. Yes, it’s absolutely ok to respond to old posts!
[ofgebu0] (score 1, diepte 5) Yes I was replying to you. I think I assumed your new provider was your primary. But you clarified, that it was a chiropractor.  Thank you. My integrative doctor hasn’t been as helpful.
[n5br8hw] (score 1, diepte 3) Excellent tips, thank you!

I started seeing a pain management specialist this year, but only for a cyst pressing on a major nerve in my shoulder. Celebrex 200mg twice a day has helped many other pains too though. I haven’t followed up on my sleep specialist referral because I was crawling through chemical menopause leading up to my very recent hysterectomy and oophorectomy. Sounds like I might luckily be on the right track, just need to heal a bit longer.

So sorry to OP for blabbing on your post. Clearly I’m a bit overwhelmed 😅 Maybe some of this helps you or others along the way? Please do keep us updated about your shoes! 🤍
[n5h3dad] (score 1, diepte 1) I don't wear anything else than sketchers anymore
Do need to use an orthopedic insole too but all other shoes are too tight/pricy
[n55k8r6] (score 1, diepte 1) Which kind of Hokas would you recommend? I’ve been looking at the Graviota since I was told they have the most cushion and stability.
[n55tlch] (score 1, diepte 3) What brand is your hiking boots and shoes?
[n62iz61] (score 1, diepte 5) Thank you!
[n55l8r7] (score 1, diepte 1 OP) thanks for the tip!
[n55whgx] (score 1, diepte 1) I am a Kizik wearer also! They are the best. I also have plantar fasciitis and Kiziks allow me to do plenty of walking.
[n59s4kp] (score 1, diepte 3 OP) for people who have done this— are there any places that offer this service that take insurance?
[n55vxrv] (score 1, diepte 0) Crocs and hokas
[n58tiq8] (score 1, diepte 1) You have both fibromyalgia and high archers? You are me.
[n561vnm] (score 1, diepte 0) I can only wear hokas. Clifton 10s. I have 3 pairs and get a new pair every 6 months. And I have custom inserts from my podiatrist.
[n569l1r] (score 1, diepte 0) Hokas all the way
[n56ab1q] (score 1, diepte 0) I live in Hoka’s and Crocs. Hoka’s the Clifton or Skyward.  They are both incredible. Days when my feet are so painful I can barely put my feet down then it’s Crocs Recovery, which are engineered for post marathons so for very tender feet. Crocs Exho are also engineered for walking outside and the professional ones for hospo workers and nurses are also fantastic.
[n56hhst] (score 1, diepte 0) I wore crocs for years. I got some keen sandals and they’re just as comfy and way more durable.
[n56i1xq] (score 1, diepte 0) Hookas; I hate the price, but my feet and back love them.
[n56jhf0] (score 1, diepte 0) Hokas. I like the hybrid hiking boot because I need a lot of ankle support.
[n56ka7r] (score 1, diepte 0) Kiziks!!! Comfy sneakers that are designed to step into so you don’t have to bend over/I rarely even have to tie them. Game changer. And still comfy with thicker compression socks
[p38bqni] (score 1, diepte 2) I’ve been wearing these for years and just realized it might be what’s activating my hip dysplasia pain. My feet are fine but I can’t run an errand without pain in my hips. Do you feel like your joints do fine in these on concrete?
[n56nd0m] (score 1, diepte 0) Clark's are my go to shoes.. I have very narrow feet and they have a few narrow options in different styles for all occasions.
[n56thab] (score 1, diepte 0) I love my Hokas, despite how they look. One pair has carbon fiber plates inside to keep it from bending, which is awesome for big toe arthritis. Oofos for around the house are fantastic, too.
[n57ky7j] (score 1, diepte 0) Hoka, Cobb Hill, Dansko
[n57s5k5] (score 1, diepte 0) I recently bought a pair of knockoff Birkenstocks for easy footwear when hanging out at campsites. Now I wear them all the time. They’re so comfortable. I also love my Merrell sandals—they’re similar to Tevas hiking sandals.
[n57xiz6] (score 1, diepte 0) My 13 year old daughter, who has fibromyalgia, really likes her Oofos sandals in the summer.
[n581vsj] (score 1, diepte 0) Sketchers, Vionics, Ecco, Taos
[n585tsq] (score 1, diepte 0) Hokas some new balances and vionics. Also i got custom insoles at a running store that i put in all my shoes. If I am not wearing any of the above mentioned items, I have a massive lower back or knee flare up. Even if I walk just a short distance. I had to give up my heels years ago. (!!) And now I no longer feel cute because nothing beats a sexy high heel. But I’d rather be able to walk the next day than feed my ego for a few hours.
[n58kwpz] (score 1, diepte 0) Hands down the best shoes I've even worn are On Clouds. My feet never hurt unless I walk like 20k steps.  Best shoes ever!!!
[n58nna7] (score 1, diepte 0) Sketchers
[n5acp3a] (score 1, diepte 0) Adidas Ultraboost works for me on bad days..
[n5ak792] (score 1, diepte 0) I look for something with memory foam. Skechers has a nice memory foam slip on sneaker type shoe, and I just got memory foam flip flops off Amazon that are super comfy
(8 reacties met lagere score weggelaten)

