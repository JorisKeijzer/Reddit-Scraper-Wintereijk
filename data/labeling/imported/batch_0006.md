# Label-batch batch_0006

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
Schrijf het resultaat naar `batch_0006.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1s1yvgm, 109ybw2, 1cezcqg).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1s1yvgm ===
SUBREDDIT: r/Shoes
DATUM: 2026-03-24  SCORE: 13  REACTIES: 74
TITEL: House Shoe Recommendations
POST (source_id=post):
I’m a SAHM to twins and my body is starting to revolt. I’m assuming standing and walking all around the house with hardwood floors is  causing my foot pain every time I get out of bed or couch. It’s more of an ache, nothing sharp.

I need a recommendation for a shoe or slipper I can wear around the house that aren’t heavy and have arch support. Price isn’t a factor.

Would love opinions from people who have been in the same boat!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oc4izn8] (score 19, diepte 0) Crocs. I never understood the appeal until I went to urgent care because I thought my foot was broken and after paying for X-rays, was diagnosed with “foot pain” and told to stop walking around barefoot on hardwood floors. 

Crocs are lightweight, supportive, cool in the summer and easy to wear with wool socks in the winter, and infinitely washable. There’s no memory foam to sink/deflate or lining to get stinky. I could not recommend crocs more. 10/10
[oc4gmzv] (score 9, diepte 0) Birkenstock Arizona
[oc4ovfp] (score 5, diepte 1) Changed my life! I have them on three colors. LOVE THEM they saved my feet.
[oc4j3qi] (score 4, diepte 0) Hoka recovery slides
[oc4osnl] (score 4, diepte 0) Get a good pair of tennis shoes and an insole. Take good care of your feet, otherwise they’ll give you trouble forever. Ask me how I know.
[oc4ess5] (score 3, diepte 0) I wear birkenstock EVA arizonas. Add socks in the winter. They're about $50 but last forever.
[oc4gqi4] (score 3, diepte 0) Orthofeet slippers
[oc4hx5a] (score 3, diepte 0) Birkenstock Arizona for summer and clog for winter.

On Cloud - the slip ons are my favorite
[oc4uwms] (score 3, diepte 1) Yup seconding this. Crocs saved me. I’m a par time stay at home mom…Hardwood floors at home and concrete floors at work. I switched to crocs whenever I could and I have no pain.
[oc4wtet] (score 3, diepte 1) Another vote for Crocs. I developed plantar fasciitis during covid after working from home and walking around on my hardwood floors with no shoes on for multiple months. Crocs literally saved me and now I have lined slippers for winter and flip flops for summer my condition pretty much resolved itself after better house shoes.
[oc4nv83] (score 3, diepte 1) I found Oofos much more comfortable than Hokas. I have both
[oc61267] (score 3, diepte 2) I’m the opposite. I found Hoka to be far more comfortable than Oofos. The hardness of the Hoka was more supportive than the Oofos foam. Also, bc I have wider feet, the Oofos was too uncomfortable.
[oc4ligh] (score 3, diepte 0) Vionic slippers and/or regular shoes.
[oc4s7ym] (score 3, diepte 0) Sounds like plantar fasciitis, which I have.  Stretches specific to the problem helps.  The podiatrist also had me wear a foot brace at night for a couple months.  The main thing that helped me was getting shoes designed for people with plantar fasciitis.  It’s a brand called Kuru.  When I wear them I have little to no foot pain.  When I don’t wear them, my feet hurt.
[oc4ef1i] (score 2, diepte 0) I’ve had 3 foot and ankle surgeries and Haflingers are the best thing I’ve found. I practically live in them. Highly recommend
[oc4yv21] (score 2, diepte 1) I wear the EVA version of this as house shoes and my arches are so much happier for it.
[oc53c8o] (score 2, diepte 2) Definitely Oofos- I have a wide foot and I find the flip flops to be more comfortable than the slide
[oc53jc6] (score 2, diepte 3) Me too!
[oc56xq5] (score 2, diepte 2) Oofos for the win! I have slides so that I can wear with socks. I even bring them with me when I travel and wear around the hotel.
[oc4pwwz] (score 2, diepte 1) I thrift these and they are amazing.
[oc50va6] (score 2, diepte 1) Yes OP!! The Vionic house slide were reco'd by my podiatrist and they completely stopped my plantar fasciitis pain.
[oc4nb5q] (score 2, diepte 0) Birdies. They have layers of comfort foam and great soles. 


https://birdies.com/
[oc4nj5t] (score 2, diepte 0) Oofos all the way!!!  I have a pair and only wear them in the house and we have hardwood floors
[oc4rdos] (score 2, diepte 0) Birkenstock zermatt slippers. I had the same thing as you, I would be barefoot and started getting pain in my feet. I got these after my doc visit and they totally solved the problem. They are pricey but totally worth it.
[oc4u0j1] (score 2, diepte 0) Sahm of 2 high recommend Oofos...
https://www.r.rediem.io/79R6-P9K85G2K
[oc4xvop] (score 2, diepte 0) In my experience, nothing will help your foot fatigue better than support hose—and I mean *real* support hose, like medical grade ones. I buy mine (toeless!) and wear them all the time when I’m going to be on our tile and wood floors at home for more than just a minute. I started wearing them when I worked long hours as a nurse and it made the biggest difference in the world. I got a lot of other nurses wearing them, too, just from conversations about their feet and legs aching/hurting. They all loved them, too. I get the 20-30mmHg of compression thigh highs (with a stay up band). You might want to start with the 15-20mmHg. I’m gonna link the ones I buy, but look around if you want to try the 15-20mmHg. Of note, the 30-40mmHg were just too much for me. I did try them but had a tough time getting them past my ankle and heel, so I didn’t continue using them. 

https://www.ameswalker.com/products/aw-style-4-sheer-support-closed-toe-thigh-highs-w-top-band-15-20-mmhg
[oc5cufg] (score 2, diepte 0) Crocs are actually great! 

I used to wear Oofos too which are super cushion-y if that’s what you’re looking for. They are marketed as recovery slippers.
[oc4dwg3] (score 1, diepte 0) Men's Slippers https://share.google/xHH97diXaA2Gzm5l0

I love these slippers. This is the men's but I'm pretty sure they also make a women's.
[p3wc1y0] (score 1, diepte 1) Are these good if you have low arches? No flat feet but mine are average or low I guess lol. I wear these house shoes I got from Khols  and they make he walk funny and my feet hurt. All these suggestion for for high arch people ugh. I have tried the ooffos slides twice but the arch support makes me feel like I am walking on logs. I have had crocs twice but I think they made my feet wider and in a C shape. Ugh...so frustrating.
[oc5iz50] (score 1, diepte 1) Croc clogs + socks. The lined ones get gross and without socks, they rip up your feet. A pair lasts about a year for me before they get worn down enough that I start having foot pain again, which is pretty good for a pair of shoes I wear basically every day.
[oc4n1yq] (score 1, diepte 1) Seconding this
[oc7331a] (score 1, diepte 3) Agree on the oofos
[oc80mtw] (score 1, diepte 3 OP) Regular slides or with Velcro? I’m in between those!
[oc8zqd2] (score 1, diepte 4) I just do regular. The kind I have are kind of wide so they’re easy to wear with socks. But I have another pair that fit more narrowly and don’t work as well with socks. So if you’re worried, go Velcro and you get the best of both worlds. 🙂
[oc9dmt2] (score 1, diepte 3) Same - I prefer the firmness of the Hokas
[oc4rrb5] (score 1, diepte 2) That’s great. I’ve never seen them while thrifting. They are pretty much the only shoes I wear.
[oc4lw9u] (score 1, diepte 0) Easy spirit Traveltime. So comfy!!
[oc4ust7] (score 1, diepte 1 OP) Which style?
[oc56d3h] (score 1, diepte 2) Oofos all the way!!!  I have a pair and only wear them in the house. I have hardwood floors 

Flip flops 

My grand has the slides and loves them!
[oc72nyj] (score 1, diepte 2) I have fallen in love with Oofos to the point where I have multiple pairs for different seasons.  I love the way the flip flops feel the most.  I wear them in the summer.  I wear the slides the most out of the year with socks.  I change the sock type depending on the weather.  When it's really cold, I wear the clogs.  TBH, I could go without the clogs.  My feet sweat too easily in them.
[oc7f2vp] (score 1, diepte 3 OP) Do you use the Velcro strap or the regular slides?
[ocft9sf] (score 1, diepte 4) I have just regular slides. I didn't even consider the ones with velcro. I'm not sure if they weren't available or if i just didn't see them.

Either way, knowing what I know now, I might consider them. My slides are actually a bit too loose when I wear thin socks.  Not enough for me to not wear them, but enough to notice.
[ocfwn3p] (score 1, diepte 5 OP) That’s what I’ve read in the reviews. I went no Velcro but sized down since I’m typically a half size. It’s 3 stops away on the Amazon truck and I’m so excited for my feet. 😂
[oc4oz69] (score 1, diepte 0) I swear by my vionic slippers, tons of styles. I even got some forms sister in law and mom. I also do crocs.
[oc4qgmh] (score 1, diepte 0) I wear Crocs now after developing plantar fasciitis - it’s crazy how an off brand bubble slide has been the most comfortable after trying so many brands.  Custom
orthodics from  a podiatrist plus calf massages are what I hear work best.
[oc4quo4] (score 1, diepte 0) Look at Yellow Box flip flops/sandals, they’re super comfy, I have high arches & RA, love them
[oc4t41n] (score 1, diepte 0) [https://novelship.com/birkenstock-gizeh-essentials-eva-black-0128201](https://novelship.com/birkenstock-gizeh-essentials-eva-black-0128201) i like this for house walking and standing, can try another model if you like to but i recommend birkenstock for real!
[oc4t6a2] (score 1, diepte 0) Haflingers or Birkenstock. After my Haflingers finally wore out, I got some wool Birkenstock house shoes, and I love them.
[oc4tkh8] (score 1, diepte 0) Joining the Birkenstock sandals as house shoes chorus. I wear Mayaris (the one with the toe strap instead of the Arizona slide) for things like cooking and cleaning and poking around my house.
[oc4wk2q] (score 1, diepte 0) Vionics are my favorite shoes. They provide arch support.
[p3wb3hx] (score 1, diepte 1) Wow thanks so much for this!
[p4c9z8g] (score 1, diepte 2) You’re so welcome!
[oc4y5v2] (score 1, diepte 0) All day on my hardwood or tile floors it's the Giza Birkenstock sandal. I have one pair dedicated to indoor / at home wear only. Great support without being bouncy, and ergonomically healthy for feet. 

My 2nd home pair are Oofos recovery sandals. Mega bouncy and fun. I do wear the Birkenstocks with more frequency yet really like these when I want to change things up.
[oc50smr] (score 1, diepte 0) All of these options are actual shoes, not house shoes. I’ve bought 5 pairs of these house shoes, they save my feet at home and I was having issues like yours, which ended up being horrible plantar fasciitis. I can’t go anywhere without these now. Very supportive and the most comfortable slippers I’ve ever owned. 

https://www.amazon.com/gp/aw/d/B08CK569H1?psc=1&ref=ppx_pop_mob_b_asin_title&th=1#immersive-view_1774321141631
[oc529xd] (score 1, diepte 0) Keen Howser III. It’s a slip on shoe with arch support and it has a rubber sole to prevent slipping. It also has a rubber coating over the toes which has saved me from stubbing my toes on multiple occasions. [Keen](https://www.keenfootwear.com/products/womens-howser-iii-slide-magnet-birch)
[oc52lhd] (score 1, diepte 0) I really like my Geisswein slippers. They have a sturdy enough sole that I can go out to get the mail but they are also flexible and cozy.
[oc54j2g] (score 1, diepte 0) I would never admit this outside of my home but I agree- crocs. I have the platform sandal style. They have so much cushioning and are so comfortable. I also have plantar fasciitis and they don’t hurt my feet at all.
[oc5x4li] (score 1, diepte 0) I swear by the brand Oofos.  They were originally designed for long distance runner's.  I came across them when I needed knee pain relief.  Available at their website, [Zappos.com](http://Zappos.com) or Amazon.
[oc6sath] (score 1, diepte 0) Allbirds slip on loungers or slippers, Vionic flip flops during the summer.
[oc6up7f] (score 1, diepte 0) Spenco
[oc72dve] (score 1, diepte 0) Oofos!
[oc7fism] (score 1, diepte 1) I love the regular slides, but the clogs are my favorite. I find them even more comfortable.
[oc73sjn] (score 1, diepte 0) At first I read this as “horse shoe” apologies.
[oc78px2] (score 1, diepte 0) I am use Hoka Recovery Slides. Recommended by my orthopedist.
[oc7a5an] (score 1, diepte 0) I really like vionic brand slippers and the oofos clogs.
[oc7bfew] (score 1, diepte 0) I had this problem and many more body aches and pains that I thought was just aging. Then I noticed on my Apple Watch one day that I had walked 4.5 miles in a day when I had not left the house! And that’s on mostly hard wood floors. 

It occurred to me that I wouldn’t dream of going on a 4.5 mile walk outside in anything other than running shoes. So I went to a running store and the guy there told me that he sold this one pair of Brooks running shoes to all the nurses at the local hospital. 

So I bought a pair and boom, all my aches and pains were gone! Now I swear by having an inside pair of running shoes I don’t wear outside. Sounds excessive but makes the difference
[oc7cjh8] (score 1, diepte 0) If money isn't a factor, I suggest you see an orthopedic doctor. She/he can tell you exactly what kind of support you need. In my case, I was sent to an orthopedic shop, had molds of my feet made, and now have custom inserts. They have alleviated my back and hip pain. You may not need that but you do need to address your the exact issue you have. Who knows, Crocs may be adequate cushion. Or you may need additional support for specific areas. 

I can understand that, as a new mother, time may be a factor. If so, [orthofeet.com](http://orthofeet.com) sells shoes with good cushion and foot support online.
[oc7fj74] (score 1, diepte 1 OP) Time is definitely a factor right now. I do have a good podiatrist as I had bunion surgery x2 in high school haha. I was a cross country runner so I’ve had my fair share of aches and pains. If choosing one of these shoes doesn’t alleviate the pain I’ll definitely take a trip back to my doctor!
[oc7ifu6] (score 1, diepte 0) Keen targhee 2 or 3. Have neuropathy in my feet and they are the only shoes that dont make me suffer!
[oc7zuz9] (score 1, diepte 0) Birkenstock Arizona
[oc87l7b] (score 1, diepte 0) You might possibly be dealing with plantar fasciitis, consult your doctor for evaluation and diagnosis. PT can be helpful for any chronic pain, I can’t recommend it strongly enough! With shoes, Dansko and Sanita are often recommended for people with plantar fasciitis. They make clogs and o-en backed clogs, as well as a whole line of cute sandals and other shoes these days. Switching to them cured PF and all foot pain for my mil. They are very firm and can take some getting used to, but I loved them and wore them to work for years. The orthopedic surgeon who reconstructed my son’s feet wore them too, and I always see them anytime I’m at the hospital on both doctors and nurses, at the podiatrists office, orthopedic doctor’s office, etc.
[oc8asda] (score 1, diepte 0) I have fitflop slippers and they’re really comfortable. I similarly experience pain from going barefoot, but also if it requires actually putting the shoe on, I won’t wear them. 

Also slippers means you won’t wear them outside. Which in my opinion immediately takes a house shoe to outside shoe
[oc8mn2l] (score 1, diepte 0) Oofos! My elderly dad is a cancer survivor and has neuropathy. He gets pain walking on hardwood floors without support. His doctor recommended Oofos slides, now we all have them because they’re awesome.
[oc8smdn] (score 1, diepte 0) Glerups. I've gotten them for every woman in my life over 30 and I still randomly get texts from people being like omg these are the best ever. [https://www.glerups.com](https://www.glerups.com)
[oc8wmvo] (score 1, diepte 0) [Merrells Mocs](https://www.merrell.com/US/en/hut-moc-2/?rst=Slippers).  My absolute go tos.
[oc8y2qb] (score 1, diepte 0) https://www.rei.com/product/209999/teva-reember-terrain-slip-ons-womens. Incredibly comfortable. Lots of cushioning
[occp2uq] (score 1, diepte 0) As an Oofos owner, can’t disagree with everyone here on comfort. But they are not natural let’s be honest, and on impulse I popped on these Fulton slides the other night. Prolly overpaid, but so far loving them!
[ojs7kfn] (score 1, diepte 0) My favorites are Skechers slides with Arch Fit
[ok34llb] (score 1, diepte 0) @forward_frosting _680 how did oofos work out?
[ok3qy7d] (score 1, diepte 1 OP) When I put them on the pain immediately goes away! It’s like walking on air haha.
(2 reacties met lagere score weggelaten)

=== THREAD 109ybw2 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-01-12  SCORE: 17  REACTIES: 73
TITEL: Are stability shoes redundant?
POST (source_id=post):
Hi all,

I went into the ASICS store to ask to try on a pair of Cumulus for my bi weekly jog around the park (no marathons here!). After doing their gait analysis on the treadmill they told me I over pronate and should be in either the Kayanos or the GT 2000 10s (if I wanted something lighter, which I did).

I was a little disappointed by this as the Cumulus felt a bit softer underfoot than the acceptably light GT 2000 10s., but resolved to go along with the advice 

Then, however, I discovered this article:  [Best running shoes for overpronation | Solereview](https://www.solereview.com/best-running-shoes-for-overpronators/)

The article argues that stability shoes don't really help to correct overpronation and a more a relic of an older time of less durable shoe tech, and a marketing ploy to give some runners what they *think* they need.

I found it quite interesting and persuasive, but couldn't really find this view replicated on the other major shoe review sites.

So I thought I'd ask for views here. Certainly I'd quite like to avoid the need to run in a stability shoe, guidance shoe or whatever if a moderately stable neutral shoe is plenty good enough. Ideally, I think I'd just like to get the Cumulus.

(The final part of this puzzle in my life is that I have developed a bit of a knee issue on the medial side. A sports medicine consultant I know, however, has told me this is more likely to be a glute/hamstring strength issue rather than a result of running in neutral Nikes for the last few years.... Still, I did think it wouldn't hurt to try a stability shoe.... before I actually tried one on and missed the softness.)

 Thanks so much in advance for any thoughts!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j41iv3t] (score 62, diepte 0) Any time somebody tells me they’re going to the running store to get a analysis and shoe footing I tell them before they go to Enjoy their stability shoe…mainly brooks lol
[j40xzq9] (score 40, diepte 0) The stability shoe thing is mostly marketing pseudoscience. With that said, if you find a particular kind of shoe works well for you, it doesn’t matter if the reason is as described. If you find yourself developing an injury after changing shoes, try something different.
[j41pvui] (score 18, diepte 0) This study found that moderate pronation in a neutral shoe is associated with a decreased risk of injury

https://pubmed.ncbi.nlm.nih.gov/23766439/

In this study https://pubmed.ncbi.nlm.nih.gov/20584759/ that randomly assigned neutral, mild, and severe pronatora to neutral, stability, or motion control shoes, the motion control shoe wearers had the most injuries, missed the most days, and reported the highest level of pain, the mild pronators did better in the neutral shoe than the stability shoe, and neutral feet did better in stability shoes. They didn’t draw any conclusions for severe pronators though. 


Personally running stores tell me to buy stability shoes but I’ve only ever had bad experiences with them so I avoid them and have been tending toward a stable neutral with great success. Have you tried a Brooks Ghost? I switched from the GT-2000s and Kayanos to them and love them.
[j42c6wo] (score 15, diepte 1) I can't speak for others, but we sell about 75% neutral shoes.
[j40xsmg] (score 13, diepte 0) If you want the Cumulus get them, run with them, and you will find out if they are fine for you or if you need more stable shoes. If everything is fine after a month or so of running with them that type of shoes is for you, if you start having some kind of discomfort or aches you probably need a different type of shoes.

Personally I like stable running shoes and dislike soft ones. But every runner is different and have different preferences and needs, so they prefer and need different running shoes.
[j446oxl] (score 13, diepte 3) Why would they?  This is a niche sub for those who are way too in to shore and do a stupid amount of research on said shoes.  The amount of shoe reviews I have read about shoes I will never buy nor had any intention to is foolish...
[j410i1b] (score 8, diepte 0) If the shoe works for you, do not listen to store advice, since they literally give everyone stability shoes.

I was discussing with someone in the weekly thread that used to run 3000km a year, on how they were running in stability shoes because the store told them so which is crazy.
[j41dbyn] (score 8, diepte 0) Many shoes listed as neutral actually have moderate pronation support. 

All of my Adidas shoes have discreet but visible structure or bias to minimize pronation. In some shoes it's a plastic wedge on the medial heel surface: every Boost shoe I've seen; most casual lifestyle sneakers. The original version SL20 lacks that plastic wedge, but the heels are visibly biased to reduce pronation.

My Under Armour Hovr Sonics and Nike Peg 39 have heels subtly biased to reduce pronation. Gotta look closely to see it.

Only my Saucony Endorphin Pro 1 and Speed 2 appear to be completely neutral. That might account for my perception that these shoes demand more attention during a run to get the best results.

I've tried one stability shoe recently, the Saucony Guide 15. Hated it. Walked around the store for 15 and was thoroughly annoyed by the structure trying to force me to walk a certain way. 

But I'm a neutral runner with slight supination as I pick up the pace, and definite supination sprinting. It's never caused any problems.
[j447m8c] (score 8, diepte 4) The way you described and at the same time destroyed everyone at this sub....
[j42d8nd] (score 7, diepte 3) Yep! And I've seen three posts here so far saying that all running stores only fit stability shoes for people, which might have been true fifteen years ago. Certainly isn't true now. If a person came in and said they ran 3000km last year in the 2000s, you know what I would pull for him? 2000s and similar shoes. His feet clearly like guidance features, so why should he change to the Cumulus? Clearly if he wants to try on the Cumulus and asked about it, I'd talk with him about the differences and have him try it on. But it seems like everyone in this sub loves to shit on run shops when they haven't stepped foot in one in 10 years.
[j4151h3] (score 7, diepte 0) They said exactly the same to me in the ASICS store with the same recommendations. I just ignored it and cracked on with the shoes I wanted (Novablast 2 and Noosa Tri 14) and have had no issues thus far. But obviously each person is different. I think a lot of it is marketing and I find that most people I talk to who have a gait analysis get recommended a stability shoe! I think it’s more just finding what works for you.
[j41sz9a] (score 7, diepte 0) Running store worker here

My personal thoughts are that an analysis can only suggest what kind of shoe you might want. Key word might. If you're getting irritation from probation or flat feet is when stability shoes come into question. If you feel alright in neutral shoes even if you pronate or have flat feet or whatever it may be, then nobody should stop you. Plantar is a completely different discussion, stability shoe/insert for you buddy. The only thing I will say with absolute confidence is that if you have a completely neutral gate then I will refuse you a stability shoe, especially the higher level ones like the Gaviota, Omni, etc.

I do strongly disagree that it's a price gouge tactic, as most stability shoes with like one or two exceptions have the same price as their neutral counterparts, and you can always use inserts in neutral shoes which is significantly cheaper.

Basically, you chose
[j432mzw] (score 6, diepte 4) Sure, if you run on roads roads are not flat they are cambered. Your shoes will not wear evenly even though there is nothing wrong with your form.

If you run on trails than the effect may be even more magnified. 

Doctor’s of Running are a great resource on this. They have a YouTube channel and a website. It may be worth a look.
[j431gna] (score 6, diepte 2) We're not quite there, but we're over 60%. I feel like most of the people on this sub haven't been in a run store in years.
[j44d6og] (score 6, diepte 5) Right, and if you're in the running community, wouldn't you want to support independent shops? Sure, some have flaws, but by in large they're getting a population of people wearing improper footwear into better footwear.
[j41byep] (score 5, diepte 1) I agree but considering what OP said I would add a small asterisk there

>I went into the ASICS store to ask to try on a pair of Cumulus for my bi weekly jog around the park\[...\]I was a little disappointed by this as the Cumulus felt a bit softer underfoot than the acceptably light GT 2000 10s.

What OP noticed was that Cumulus were a bit softer, if you only go for couple minutes run or a few straight lines the only thing you will notice are basically this, how hard/soft it is, how heavy/light it is

But soft doesn't necessary mean better, it's alluring when trying on the shoes very quickly but might not work for a full run (30mn to 1h) for whatever individual reason.

Eg. maybe the GT 2000 are better for him, maybe it's the Cumulus, a judgement shouldn't be made based on marketing pronation stuff nor on how soft it feels when walking a couple steps, even if the softness is very alluring
[j41d57c] (score 5, diepte 0) I would like to share my experience...which may be VERY similar to many new runners...

Went to running shoe store for gait and foot analysis to identify needs.

Told I have overpronation...recomendation stability shoe. Saucony Hurricane 23 chosen from a few.

Ran from 5k to HM distances for first time.

Got better at running faster...did strength training and foot strengthening excersices...got faster.

Di more self driven research on this sub...new world of options mentioned and watch like 100 youtube review of various more "stable" neutrals...chose Hoka Rocket X after a try on...knocked 23 mins off HM time.

Looked at strange wear pattern on shoe...(rear outer heel and forefoot wea) found out I don't overpronate but supinate all along and that running store was wrong...

Moral...try on find what works...the store experts not always right!!!
[j41mc2p] (score 5, diepte 0) You won’t hear it from the shoe brands because everything they publish is written by a marketing department.
[j41pjxl] (score 5, diepte 0) I purchased the Cumulus as my first pair of daily runners to run 5, 5, 10k in a week. 

They were exceptionally soft underfoot when walking but they definitely compress when running and feel supported underfoot, not cushy when running. 

I find it’s a great show for under 10km, although I’ve run up to 30k in them. Currently just reached 300km since August in these pair. 

If you’re running 15-30 mins casually then these will last a long time.
[j41q25x] (score 5, diepte 0) IMO, I would definitely avoid soft/plush cushion shoes. Not only are they going to allow for uncontrolled excessive joint movement which also works it way up to the knees and hips, they’re going to exacerbate overpronation.
[j42rukx] (score 4, diepte 2) You can’t tell anything from your outsole wear pattern.
[j41wx0g] (score 4, diepte 0) Agree with most of what has been written here. I asked and researched the same Q last year, having historically used 'gentle' stability on running store advice as a new runner (ASICS GT, then Brooks Adrenalines), then in light of articles similar to the one you found tried a cautious switch to neutral (Saucony Ride 15) and prefer it. I'd agree with the caveats that a significant minority of runners have running styles which benefit from extra supportive footwear, and that it's more likely that newer runners may not have developed conditioning for varied muscles. 
So I think the standard response of running shops hugely pushing gentle stability shoes (often to newer runners, and/or those who are attending because they are concerned there may be significant overpronation problems with their running style) isn't as cynical as it's always made out to be, and is arguably in the 'it won't hurt, and might help' category, provided they're only gentle stability shoes. (Much harsher stability tech for those who don't need it *can* hurt, by changing running form).
For those buying follow-on shoes and with no reason to think there's a medical reason to need anything stability (i.e the majority), I'd say neutral, prioritising whatever you personally like.
[j41gooh] (score 3, diepte 1) Also, just look at the soles of your running and walking shoes. That'll indicate whether we have any gait issues that might benefit from a special shoe. 

I'm surprised my shoes still wear pretty normally and equally on both feet, despite aging and injuries.
[j41n5rs] (score 3, diepte 3) So far the only obvious pronator I've seen of the many YouTubers with running and shoe review channels is Emily Heller (Run Like Heller). It only affects one foot. She's aware of it. It might catch up with her later but she's young enough now it probably won't matter. 

I suppose it's possible to buy a stability shoe for one foot and a neutral shoe with comparable midsole material and stack for the other. Hip tilt from injuries causes me to shim one of my clipless cycling shoes to get more comfortable, smooth pedaling. It's a subtle thing but I don't want to risk a knee injury so I check my ergonomics often and make adjustments as needed.

With access to thousands of hours of high def video of pro runners online it's easy to see that most runners do roll slightly inward from the lateral heel/foot edge as they put weight on the foot strike. 

I haven't video recorded myself but when I look down I can see the same thing in my foot strike. But the sole wear patterns on my shoes all show the same consistent pattern of wear to the outer edge and forefoot from running, and outer heels from walking. Very even wear on both shoes, every pair, from my 50 year old hiking boots to my running shoes.
[j41lffd] (score 3, diepte 2) Yeah, the Speedroll rocker on the Saucony Endorphins took me several runs, about 50 miles total, before I finally got the hang of going with the flow rather than fighting the shoe. I had to bend my knee slightly and focus on consciously dropping the foot at the moment of touchdown, rolling and pushing off smoothly, rather than landing on any particular part of the soles. That won't come naturally.

I was on the verge of selling both the Pro and Speed, but after a significantly better 5k this week I decided to keep working with the shoes.

FWIW, I'm a heel striking plodder in easy runs, heel/midfoot with forefoot push-offs when I pick up the pace. The Endorphins work better for me at a tempo or faster pace. They won't be my choice for daily trainers. I still like my Adidas Solar Boost for easy day, plodding and walking. But I do like the PWRRUN midsoles.
[j41g5ap] (score 3, diepte 0) You just need to find what works for you. The Cumulus will definitely feel softer, but if you try on the GT-2000v11, you'll find those are quite a bit softer than the v10 due to the change in foam. As the article notes, true stability shoes are becoming less and less rigid and stiff, so there's a much smaller space between something like the Cumulus and the 2000 then there used to be. In regards to your desire to completely avoid stability shoes, do you have a reason for that? It seems arbitrary to completely boot a shoe like the Tempus off to side because it's considered a "stability" shoe.
[j41mpt5] (score 3, diepte 0) Running shoes are notorious for handing out stability shoes like candy. If you have a serious over pronation problem it may be necessary but a small amount of over pronation will probably not be an issue. I have run in stability shoes and recently went to a neutral daily trainer shoe and haven’t noticed any difference really. Unless you over pronate so much that it causes you an injury or pain, then try out a neutral shoe and if it works for you then keep using it.
[j43qq5a] (score 3, diepte 2) That seems to suggest a very poor controlled experiment! They should have controlled for body weight and running experience in the group selections I think.
[j41rsu8] (score 3, diepte 1) This here can't be stated enough.  Hoka Bondi 7 was my first (and last) max stack shoe, and led to a nasty stress fracture.
[j42439f] (score 3, diepte 0) I have experience working at specialty run stores and running d1. I think that the results wearing different shoes are so varied. I know some extremely talented neutral runners that only will wear shoes with mild stability. I have also seen shoes with a significant medial posting (NB 860) really help people run pain free although perhaps this is less about pronation and more about collapsing arches. I absolutely think there is a place for stability shoes and use a couple pairs in my rotation. But they aren’t the answer for everyone, you need to personally experiment and find what works best for you. In my experience a light stability shoe like the GT 2000 or older models of the Nike structure or brooks adrenaline will work well with the largest percent of runners.
[j42g3mj] (score 3, diepte 0) Most people dont need stability shoes, and for those who do, they are more of a bandaid to cover up an underlying issue. It's the same as having your knee permanently k-taped in my eyes. 

I've done a complete running mechanics analysis at a running clinic recently and the physio said amongst many other things that I pronate at lower paces. I was waiting for him to say that that I should go and buy stability shoes but instead he said it's not an issue at all. He said my ankles and feet are actually quite strong regardless of what he is seeing on the video clips and said I should continue wearing neutral shoes. He also showed me a couple drills for single leg stability that I should do as part of my warm up routine to improve balance when landing.

If in doubt, go see a professional. This session costed £90, lasted two hours and it was probably the best investment as far as my running goes. My knee/hip niggles are going away and my running economy improved.
[j43i2ev] (score 3, diepte 0) I used to think that but now I’m being training in running shoe fittings and gait analysis. Things I have learnt:
- stability shoes can help increase the life of a shoe if you pronate as the foam on that side is stronger through either structural or material means 
- there are different kinds of pronation and different shoes suit the different kinds. Take myself for example, I have a mild, mid foot pronation so really structured shoes with stiff heels won’t suit me. I can either run in mild stability shoes like the GT-2000, the saucony guides or neutral shoes like the ASICS nimbus/ nimbus lite. I shouldn’t do all of my training in neutral shoes though as I will wear the shoes down faster and not having any support at all could cause me issues
- we’re taught that after we do a barefoot analysis on people to always start them in a neutral shoe to see whether observed pronation is still visible before moving onto more supportive shoes
- it’s not about correcting pronation but it’s giving your feet the support they need to carry all the force that your body is putting into the ground safely

In OP’s case, maybe they’re just not suited to ASICS shoes and that’s why I’d go to a specialist running store that carries a range of brands rather than just to a single branded store. Stability shoes that feel nice and bouncy do exist and I know that because that’s what I like myself!
(41 reacties met lagere score weggelaten)

=== THREAD 1cezcqg ===
SUBREDDIT: r/thenetherlands
DATUM: 2024-04-28  SCORE: 122  REACTIES: 68
TITEL: Ook tot jaren celstraf veroordeelden op vrije voeten door personeelstekort
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l1m20sp] (score 206, diepte 0) Ik weet nog wel dat we een paar jaar geleden trots allemaal gevangenissen aan het sluiten waren omdat we er te veel hadden en het stond allemaal leeg. Al het personeel omgeschoold. En nu hebben we dit. 

Straks gaan we gevangenissen privatiseren en targets geven, net als in Amerika. Kan niet mis gaan. Bij de verzekeringen en het OV is het immers ook zo goed gegaan.
[l1m3990] (score 160, diepte 0) Personeelstekort is een van de ergste eufemismes waar onze overheid, en het bedrijfsleven, zich van bedient.

Dit personeel is of geforceerd omgeschoold, of ontslagen, of de functie is zo in onbalans kwa werk/omstandigheden en arbeidsvoorwaarden dat niemand hem meer wil doen.  In al deze gevallen is het beleid wat hier ten grondslag aan ligt.

Door het personeelstekort als een losstaand ‘ding’ te verpakken haal je de discussie weg over de onderliggende redenen en kom je dus nooit tot een echte oplossing. 

Benoemen en bouwen: “door het personeelsbeleid van de afgelopen jaren is … ontstaan”
[l1m4ogf] (score 61, diepte 1) Je zou bijna gaan denken dat het een vooropgezet plan was om de boel in de soep te laten lopen. Laat een probleem ontstaan. De maatschappij zal uiteindelijk protesteren en oplossingen eisen. Daarna de oplossing bieden door middel van privatisering. en dan is het kringetje rond en kunnen de heren hun zakken vullen.
[l1m38d1] (score 51, diepte 1) >Hoe kan dit zo erg mis gaan in Nederland?

Er gaat niets mis. Mensen stemmen al decennia voor partijen die de boel kapot maken dus dit soort problemen zijn gewoon bewuste keuzes van stemmend Nederland.
[l1m5067] (score 51, diepte 1) Dat was gewoon een bezuiniging met als excuus dat het zo "goed ging met de misdaadcijfers".  Veroordeelden kregen/krijgen daarnaast ook vaak taakstraf of enkelband ipv gevangenisstraf volgens mij.
[l1m3hlr] (score 46, diepte 2) en hoe groter de puinhopen van rechts, hoe harder we roepen:"nog iets rechtser, deze keer gaat het werken"
[l1m09n7] (score 44, diepte 1) > Hoe kan dit zo erg mis gaan in Nederland?

Wanbestuur.
[l1lus7w] (score 43, diepte 0 OP) Hoe kan dit zo erg mis gaan in Nederland?

Als je wordt veroordeeld voor ruim 4 jaar cel dan val je wat mij betreft wel onder de noemer 'zware crimineel"

Ook het idee om de (kleine) celstraffen uit te zetten vind ik erg slecht. Je hebt een (erg domme) fout gemaakt, krijgt er een straf voor opgelegd en die moet je dan ergens in de komende paar jaar gaan uitzitten? Dan heb je toch ook geen vooruitzicht, kom je wellicht in de knel met je werk e. d.

Nou heb je met een personeelstekort het natuurlijk ook wel moeilijk om alle straffen te volbrengen, maar dit had je natuurlijk aan kunnen zien komen en is dus gewoon zeer slecht management geweest.
[l1m3qpz] (score 35, diepte 2) Dat is niet het probleem hier. Het probleem is hetzelfde als met asielopvang: VVD wurgbeleid. Plek voor 1000 gevangen en je hebt er een maand lang maar 900? Capaciteit terugbezuinigen naar 900, kijk allemaal de VVD heeft weer geld bespaard! 


 Dat doe je zo een paar keer tot je die capaciteit wel nodig hebt en dan is het er niet. Maar in de tussentijd heb je wel wat geld overgehouden op papier. 


 Als een wurgslang die steeds wat harder knijpt als je uitademt.
[l1m8wbf] (score 35, diepte 1) “Luie millennials willen niet meer werken voor een salaris waar in deze huizenmarkt niks mee te doen is”
[l1m828p] (score 34, diepte 1) “Niemand wil x werk meer doen, dus we moeten wel gastarbeiders exploiteren!”
[l1m9bvi] (score 32, diepte 2) Fuck huizenmarkt. Zelfs in de supermarkt is het al bijna niet meer te doen.
[l1m8vrv] (score 27, diepte 1) > Hoe kan dit zo erg mis gaan in Nederland?

Door je ambtenaren te zien als kostenposten en erin gaan zitten hakken alsof het oproepkrachten of seizoensarbeiders zijn.

Resultaat Nederland B.V. voor meer dan tien jaar.
[l1m41oc] (score 24, diepte 3) Vergeet niet dat je wel moet roepen dat het allemaal de schuld is van het beleid van Groen Links!
[l1mh8q5] (score 15, diepte 3) Ja zeker. Ik zie geen reden waarom ik er van uit zou moeten gaan dat zij voorstander zouden zijn van een op de zelfde manier bezuinigen. Zij hebben nooit de kans gekregen om mee te regeren en in hun verkiezings plannen geven ze geen enkele indicator dat ze dit probleem gaan verergeren. In tegenstelling tot veel rechtse partijen die allemaal roepen dat straffe omhoog moeten zonder dat ze willen investeren kn de capaciteit.


Je hoeft niet alles goed te vinden van een partij maar het is absurd om GroenLinks hierin iets te verwijten.
[l1mynpk] (score 14, diepte 1) Mijn pa stond toen vooraan de rij met boze gevangenismedewerkers en zij zagen de bui al hangen. Daar is ook nog voor geprotesteerd etc. Maar dat maakte niet uit, PI Alphen zou de grootste supergevangenis worden in Nederland en dan kon de rest dicht. Toen is inderdaad de helft van het personeel weggegaan, want ja, wie wil er nou een uur extra reizen? 

Afijn nu zijn we hier. Je hebt het precies goed.
[l1maihw] (score 11, diepte 6) En dat voor een MBO 2 opleiding, geen ervaring vereist en een overheids CAO. Sterker nog, een MBO diploma is niet nodig, kun je ook on-the-job halen.


Dat zijn toch zeker geen slechte voorwaarden.
[l1mrl33] (score 11, diepte 3) Zo "wappie" is die opmerking toch niet? Er zijn helaas veel voorbeelden van de laatste paar decennia, en termen zoals Limoen Socialisme bestaan ook als gevolg hiervan.
[l1mg7pb] (score 10, diepte 2) Aangevuld met belabberde media om de pijnpunten duidelijk te maken. Want laten we wel wezen: dit zou gewoon reden moeten zijn om de VVD hard op zijn plaat te laten gaan als handhavingspartij. Hoe de neuk kun je criminelen zo weinig in de weg staan. Met je personeelstekorten...
[l1mcao5] (score 10, diepte 1) Eigenlijk vind ik dat erger dan een gewone gevangenisstraf want je kunt het veel moeilijker achter je laten en verder met je leven. Het is dus een veel zwaardere straf op deze manier.
[l1m0va2] (score 10, diepte 0) Erg onprettig, woon nabij een cafe die blijkbaar dient als criminelenhol. Laatste tijd meerdere keren opgevangen dat er open en bloot besproken werd hoe lang mensen moesten "zitten". Altijd weer een wtf momentje.
[l1n2xxi] (score 10, diepte 3) Ondertussen is het eerder een welbekende tactiek. Hoe vaak hebben we nu al gezien, zowel in Nederland als in andere landen, dat sociale voorzieningen compleet worden uitgekleed? En hoe vaak wordt vervolgens geroepen dat een genationaliseerd systeem kut is en dat het beter geprivatiseerd kon worden, waarna het nog kutter wordt?

Het is best wel een patroon. Of iedereen die rechts is, is (aldus de bekende uitspraak) volledig geschift door telkens hetzelfde te proberen en andere resultaten te verwachten, of dit is gewoon expres.
[l1mc7xr] (score 9, diepte 1) Dit is deels wel waar maar er is ook in absolute cijfers een mismatch tussen het aantal banen en beschikbare beroepsbevolking. Dan kan je de arbeidsomstandigheden voor gevangenispersoneel wel verbeteren, maar als je daarmee personeel van bijv. de politie wegtrekt dan heb je onder aan de streep geen oplossing maar loop je enkel met mensen te schuiven.
[l1mezxs] (score 7, diepte 7) Dit is een medior rol, dus ze verwachten dat je al enige werkervaring hebt en niet direct uit de schoolbanken komt. Ja, er is de mogelijkheid om dit te doen terwijl je de opleiding doet, maar dan moet je er wel vanuit gaan dat je aan de onderkant van de schaal, of misschien misschien een schaal lager word ingezet. 

Het is wat moeilijk vergelijken omdat ik niet even makkelijk kan zien of dingen zoals vakantiegeld er nog bovenop komen. Maar laten we er vanuit gaan dat het om basissalaris gaat. Als je in je achterhoofd houd dat het [minimumuurloon 13.27 is](https://www.rijksoverheid.nl/onderwerpen/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2024), dan kom je met een 36 urige werkweek uit op 2078 euro per maand (uitgaande van 4,35 weken in een maand, wat het gemiddelde is). Ben je bereid 40 uur te werken, dan kom je op een maandsalaris van 2309 euro. 

Als je dus net uit de schoolbank komt/mee bezig bent, word je waarschijnlijk aan de onderkant van de schaal geplaatst en verdien je ongeveer 150 euro meer dan minimumloon. Dat kan meer worden met onregelmatigheidstoeslagen. 

En ja, ga je meer verdienen naarmate je er langer zit en ervaring opdoet. Maar er word verwacht dat [het modaalsalaris in 2024 rond de 42.000 euro] gaat zitten, of rond de 3500 euro per maand. Daar kun je met onregelmatigheidstoeslagen in het top van de schaal dus wel aan komen.

Het zijn geen slechte voorwaarden, maar het is ook geen vetpot, en zeker gezien het fysieke component wat er in zit kan ik mij voorstellen dat genoeg mensen dit niet kunnen of willen. Zeker als je nog moet beginnen, kan je ook thuis gaan [werken in een callcenter voor 14.49 per uur](https://www.studentenwerk.nl/vacatures/2567751-thuiswerken-als-klantadviseur-voor-kpn-in-regio-utrecht), waarmee je met 40 uur uit komt op 2521 euro (inclusief vakantiegeld).
[l1nujcj] (score 7, diepte 2) > Je zou bijna gaan denken dat het een vooropgezet plan was om de boel in de soep te laten lopen.

Ja.  
Verpleegtehuizen? Gesloopt, letterlijk. Nu wil men die terug (maar niet politiek Den Haag, die vinden dat je het zelf maar moet regelen)  
Woningen? VVD-coryfee Stef Blok ging naar beurzen en congressen om onze woningmarkt te promoten als investeringsmodel, naast dat woningbouwverenigingen miljarden moesten weggeven aan Den Haag.  
Asielzoekerscentra, COA en IND: al jarenlang veel te weinig geld en nu gigantische problemen (waarbij de politiek onwil om dit op te lossen er mijlenver op ligt maar er simpelweg niets gebeurt)  
En-nog-veel-meer.  
  
En hier dus exact hetzelfde. Allemaal halleluja-verhalen dat gevangenissen niet meer nodig zijn, maar ondertussen gewoon tekorten aan personeel laten oplopen tot criminelen niet opgesloten kunnen worden.  
Het frusterende is dat minister Weerwind nu de wind van voren krijgt, maar hij er niet veel aan kan doen, omdat gevangenissen niet onder hem vallen, die vallen onder Yesilgöz van justitie. Dus het is lekker bashen op een D66'er terwijl de VVD schuldig is. En zo schuiven we weer lekker verder op naar extreem-rechts, naar het fascisme.
[l1n12pw] (score 7, diepte 2) Ze zouden eens wat meer moeten luisteren naar mensen die er verstand van hebben. 80% van de politiek zit er voor eigen gewin en denken dat ze alles weten. Terwijl vaak genoeg blijkt dat dat niet het geval is.
[l1mejti] (score 6, diepte 3) Ze zouden in ieder geval een oplossing zoeken, in plaats van mensen gewoon zonder consequenties of reïntegratie weer vrij te laten. Dit is het slechtste van beide werelden.
[l1mjcv3] (score 6, diepte 3) Raar beeld van links heb jij.
[l1mr2rl] (score 6, diepte 2) Zeker als je je leven weer wilt opbouwen. Stel je hebt geen baan vanwege je misdaad (of een andere reden). Dat kan, maar als je niet weet wanneer je de straf kan uitzitten maakt dit het wel extra lastig om de stap te zetten naar solliciteren voor een (vaste) baan.
[l1m4sb1] (score 6, diepte 2) Dit plus fascisme
[l1mfzc9] (score 6, diepte 2) Mja precies. Het begon bij het afbrokkelen van handhaving. Politie is nu altijd te druk met wat anders om echt hulp te bieden. Ambulances moeten van ver komen en de brandweer laat liever wat gecontroleerd uitfikken dan dat ze op tijd de boel blussen.

We hebben ook niet echt grote rampen gehad om veel hulpverleners nodig te hebben, anders was dit al veel eerder een probleem geweest. Maar de politiek ziet het gewoon als bezuiniging en denkt al aan waar ze dat geld anders aan uit gaan geven. Ondertussen is de zorg, het onderwijs, het OV en de politie zo uitgekleed dat ze eigenlijk al lang niet meer hun baan goed kunnen doen. En met de karige salarissen ga je het alleen nog maar doen als je het als je roeping ziet.

Ondertussen gaan de criminelen vrolijk door en zien ze de politie alleen als hinder ipv hun grote tegenstander die lastig te verslaan is. Auto's worden aan de lopende band gejat en gaan naar het buitenland toe waar ze vogelvrij zijn. Het proces om diefstal af te handelen is gewoon onderdeel van het systeem ipv dat ze echt moeite doen om te zorgen dat de criminaliteit minder wordt. Dit systeem is echt kapot en het is jammer dat de bevolking denkt dat het nieuwe kabinet het wel gaat oplossen...
[l1mf0zf] (score 6, diepte 1) dit was toendertijd natuurlijk het werkelijke plan.
[l1n2bqe] (score 6, diepte 2) Oh ja ik sowieso ook. Ik merk steeds meer "veramerikanisering" om het maar een naam te geven. Ik kan me niet voorstellen dat ze uit sociaal standpunt ook echt die kant op willen. Maar als je kijkt naar hoeveel poen al die Amerikaanse politici harken, kan ik me best voorstellen dat het vanuit de politiek een prima richting lijkt. Dan zou je in theorie nog een eerste kamer hebben ter controle. Maar die zit ondertussen zo vol met lobbyisten met 39 banen, dat het moreel kompas daar ook ver te zoeken is.

De uiteindelijke vraag is dan denk ik ook: Hoe komen we in godsnaam uit deze neerwaartse spiraal, zonder alle goede politici aan het zakenleven te verliezen?
[l1mj6pc] (score 6, diepte 2) Ik snap je punt, maar dit is wel precies hoe het werkt in ons systeem. De meeste mensen zullen een baan zoeken die ze leuk vinden en die goed genoeg betaalt. Als je te weinig salaris krijgt om van te leven ga je opzoek naar een baan waar je meer krijgt. Werkgevers weten dat ook en moeten dus zorgen dat ze mensen lokken met leuk werk en een aantrekkelijk salaris.


Dit mechanisme zorgt ervoor dat arbeid altijd uitgevoerd wordt op de plek waar het de meeste waarde oplevert. Voor zowel de werknemer als de werkgever. Dit is onderdeel van een kapitalistisch systeem en zorgt ervoor dat we op de lange termijn met z'n allen maximaal financieel resultaat halen.


Of maximaal rijk worden het juiste doel is voor ons als maatschappij is natuurlijk de vraag, maar dat is een heel andere discussie.
[l1m1my3] (score 5, diepte 1) Hoe kan het zo misgaan.  

Heb jij zin om te werken in het gevangeniswezen? Ik niet in ieder geval.

Het betaald bepaald niet geweldig, niet raar dat mensen er niet voor in de rij staan.
[l1mkugu] (score 5, diepte 3) \^ zie ook onze IC capaciteit gedurende Covid.   
Oké tot op zekere hoogte valt daar ook nog wel iets voor te zeggen omdat de IC tyfusduur is en het de reden is dat Duitsland na de V.S. het duurste zorgsysteem van de wereld heeft, maar er wordt in NL bijna nooit gekeken m.b.t. beleid wat dan de ideale afweging zou zijn tussen. Er wordt gewoon bezuinigd als er overcapaciteit is, zonder toekomstvisie.
[l1n1uav] (score 5, diepte 1) Na jaren VVD en nu nóg rechtser aanstaande coalitie, zou ik dat maar niet hardop zeggen. Ik acht ze ertoe in staat.
[l1myxhi] (score 5, diepte 0) Wat hier ook interessant is: door deze kunstmatige personeelstekorten is ook het niveau van de bewaarders flink gedaald omdat we de eisen moesten verlagen. We halen nu mensen binnen die eigenlijk niet zouden mogen werken binnen een PI: denk aan bewaarders die smokkelen e.d. 

Leuk he?
[l1m4rp5] (score 4, diepte 2) Salaris plus toeslagen is echt wel mooi hoor daar.
[l1m93h1] (score 4, diepte 5) Hier een [vacature voor complexbeveiliger op medior niveau in Almelo](https://www.werkenvoornederland.nl/vacatures/complexbeveiliger-medior-DJI-2024-0233). Genoemd salaris is €2.421 - €2.945 met tot 750 euro euro aan onregelmatige diensten toeslag.
[l1mfjii] (score 4, diepte 8) Ze noemen het medior maar je hebt geen werkervaring nodig volgens de vacature. Tja..


En natuurlijk begin je onderin de schaal als je geen ervaring hebt, niet heel verwonderlijk toch?


Bijna niemand begint op een modaal salaris he, de meeste mensen werken ook daar naar toe. Callcenter.. dat is het ultieme k*t werk, dan is beveiliger heel wat beter werk. Zo fysiek is het ook helemaal niet, amper zelfs.


Dus is het een vetpot? Nee klopt, zeker niet. Maar het is een MBO2 baan met minimale eisen en minimaal tot matige werkdruk. Elke beveligingsbaan is veelal 'aanwezig zijn voor het geval dat'.
[l1mnyze] (score 4, diepte 3) Tot nu toe zijn het de partijen als de VVD en CDA die hiervoor (en de meeste andere problemen waar we nu mee zitten) hebben gezorgd. Blind roepen over GL dat zij hetzelfde zouden doen terwijl zij in de afgelopen 15 jaar niet echt wat te zeggen hebben gehad is weer typisch van die rechtse bullshit.
[l1mgsm0] (score 4, diepte 3) Dat dan inderdaad weer niet.
[l1n16bq] (score 4, diepte 3) Hey maar PI Alphen is wel een heel leuke gevangenis, dan hebben we er dan weer voor terug gekregen. 🤮
[l1n3l2s] (score 4, diepte 3) Die Eerste Kamer is gewoon een tweede Tweede Kamer. Behalve dat daar soms een extra politiek spelletje heerst, waardoor ideeën weliswaar alsnog worden afgeschoten, maar niet om de juiste redenen.
[l1m6lev] (score 3, diepte 3) 2600 tot 3200 bruto. Het is maar wat je mooi noemt.
[l1m748z] (score 3, diepte 4) Is dat kaal salaris of met toeslagen?


En hey je zit droog en hoeft er niet bepaald stapels diplomas voor te hebben. Het is ook geen hartchirurgie he.
[l1ma2jw] (score 3, diepte 1) Ik had geen straf gekregen. Wel kliniek. Ging in beroep, want dossier klopte niet. Moest 4,5 jaar lang in de gevangenis doorbrengen om vrijgesteld te worden van iets dat duidelijk verzonnen was. Beroep, cassatie, hoge rechter etc. Aan de ene kant ben ik blij dat het mogelijk is om jezelf te verdedigen, dat is niet overal zo. Aan de andere kant - WTF?!
[l1obibv] (score 3, diepte 1) > Laatste tijd meerdere keren opgevangen dat er open en bloot besproken werd hoe lang mensen moesten "zitten"

*"Hoi! Waar hebben jullie het over? Owja, ik mag nog even blijven zitten... Ik moet van mijn vriendin wel vóór middernacht thuis zijn."*
[l1maa4n] (score 3, diepte 0) Maar het gaat goed met de economie!
[l1mvhnd] (score 2, diepte 9) Ik denk niet dat je werkdruk of hoeveelheid kutwerk zomaar in kunt schatten zonder het werk te doen?

Maar je moet dus wel (bezig zijn met) MBO2 om het te mogen doen. En als je er mee bezig bent of net klaar mee bent, verdien je ongeveer net zo veel als ongeschoold werk in een call center. Ik zou oprecht een hoger salaris verwachten voor werk waarbij je een hogere kans hebt om fysiek gewond te kunnen raken, er een bepaalde fysiek van je word verwacht en je een opleiding voor nodig hebt.
[l1mw97p] (score 2, diepte 10) Je kunt werkdruk niet weten zonder het te doen, je kunt zeker een inschatting doen. 


 Beveiliger klinkt heftig, ik ken er meerdere ik verschillende settings, er gebeurd werkelijk niks. Je bent 99% aanwezig ter preventie. Een leraar voor de klas loopt tegenwoordig nog meer fysiek risico. Beveiliger is ook helemaal geen fysiek beroep, je wandelt rondjes, zit, en let op. 


 Ja je moet MBO 2 hebben maar is dat, en dit bedoel ik niet respectloos, ook niet echt de onderste laag van de opleidingsniveau piramide? Moet daar een fortuin tegenover staan? 


 En jij vindt het bijzonder dat je weinig betaalt krijgt als je *geen* diploma hebt. Wat daar bijzonder aan is, is dat het überhaupt kan en dat zegt ook meteen al meer dan genoeg over de heftigheid van de baan.
[l1me5hs] (score 2, diepte 4) Echt wel mooi en als je een beetje rondshopt voor een goede positie in een goed team op een goeie lokatie dan heb je het echt niet verkeerd hoor.

Natuurlijk, een zzp IT'er met gewilde schaarse skills heeft 5x zoveel. Maar daar gaat het  nu even niet over.

Er zijn heel veel beroepen die matig tot flink onder modaal verdienen. Dan is dit echt niet verkeerd.

Bij een volgende crisis zullen de tekorten zo verdwenen zijn want dan weten werkzoekenden deze banen ineens heel snel weer op waarde te schatten.
(16 reacties met lagere score weggelaten)

