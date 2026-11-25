# Label-batch batch_0141

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
Schrijf het resultaat naar `batch_0141.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(4 threads: 1lt4tfc, xj3gg8, vxv1r5, 1vfmisg).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1lt4tfc ===
SUBREDDIT: r/Chefit
DATUM: 2025-07-06  SCORE: 18  REACTIES: 63
TITEL: Kitchen Shoes
POST (source_id=post):
What do y’all wear on your feet? Been working in kitchens over 20 years with no end in sight. I don’t think I’ve ever had kitchen shoes I could solidly recommend. Everything I’ve tried has ranged from underperforming to fine. Is there a gold standard of kitchen shoes I’m missing out on?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n1ny2jg] (score 16, diepte 0) Birkenstock tokio super grip
[n1nkw42] (score 12, diepte 0) Birkenstock leather
[n1nya75] (score 9, diepte 0) https://www.reddit.com/r/Chefit/s/g2PaXWEbqk

https://www.reddit.com/r/Chefit/s/DB0kHdKUdU

https://www.reddit.com/r/Chefit/s/bXzm89wFCA

https://www.reddit.com/r/Chefit/s/8x7OZ49wg0

https://www.reddit.com/r/Chefit/s/N7PgSDyX8M

https://www.reddit.com/r/Chefit/s/QrbqQe0Vug

https://www.reddit.com/r/Chefit/s/QyalflDH1v

https://www.reddit.com/r/Chefit/s/9vl8XcakBB

https://www.reddit.com/r/Chefit/s/DQVeE7ICon

https://www.reddit.com/r/Chefit/s/duaAnJE5Fx

https://www.reddit.com/r/Chefit/s/pqAR9Sv6T5

https://www.reddit.com/r/Chefit/s/TyWnn2VeZa

https://www.reddit.com/r/Chefit/s/YcxAkXmfKm

https://www.reddit.com/r/Chefit/s/zIdyJoIPwO

https://www.reddit.com/r/Chefit/s/2tnpLCsYfJ

https://www.reddit.com/r/Chefit/s/gcrw9mMXVO

https://www.reddit.com/r/Chefit/s/0WHXaBpxdK

https://www.reddit.com/r/Chefit/s/GRDIppJjox

https://www.reddit.com/r/Chefit/s/8S2ACejsBH

https://www.reddit.com/r/Chefit/s/tWtr1IryC0

https://www.reddit.com/r/Chefit/s/AGOuNbWgxo

https://www.reddit.com/r/Chefit/s/60IvZexMks

https://www.reddit.com/r/Chefit/s/Nf0KbY7TGQ

https://www.reddit.com/r/Chefit/s/vB3nplsFhs

https://www.reddit.com/r/Chefit/s/SJ6wLgd9Tt

https://www.reddit.com/r/Chefit/s/L23cxI1rzk

https://www.reddit.com/r/Chefit/s/3B1Rx1hEQV

https://www.reddit.com/r/Chefit/s/DqT0AbcjwN

https://www.reddit.com/r/Chefit/s/nVw6RAmIfe

https://www.reddit.com/r/Chefit/s/nkcipYwlqj

https://www.reddit.com/r/Chefit/s/wRnjJb8tLK

https://www.reddit.com/r/Chefit/s/UJKU4wFJUF

https://www.reddit.com/r/Chefit/s/8pIvthyv5z

https://www.reddit.com/r/Chefit/s/pQEE305fps
[n1nonmh] (score 7, diepte 0) Gonna copy/paste a comment I've made before whenever this question comes up:

  
I think the best type of shoe for each individual varies a lot depending on different factors. We're all built a bit differently physically and what exact type of job you have in the kitchen makes a huge difference.

I started out with kitchen sneakers but still had some minor issues. So I decided to try Clogs and Bistro crocs because they seemed to be so highly recommended across chef/kitchen subreddits.

They were absolutely NOT for me and made things much, much worse. I work in a somewhat smaller kitchen with a small crew. We have to multitask and perform lots of different roles throughout the day, so I'm constantly walking and moving around a lot, rushing around the kitchen and back of house areas.

I definitely don't think Crocs/Clogs are made for that type of work. From what I could tell, they have little to no heel/achilles support. I thought maybe I just needed to give them time to adjust or break them in, but after about 2 months of use I was literally limping by the end of my shifts and by the time I got home, I would basically collapse onto my chair because I could hardly walk anymore.

I assume if you work in a kitchen where you have more of a singular role on the line and are standing for long periods and not walking around much, clogs and crocs are probably pretty nice. I still wear my bistro crocs at home sometimes when I'm lounging or not walking around much and they are fairly comfy for that.

I ended up switching back to kitchen sneakers and it was the best decision I ever made for myself personally. I'm currently wearing Sketchers cessnock non-slip food service sneakers with Dr. Scholls heavy duty work insoles and I've found that to be the best combination for me personally.

My feet and back are feeling much better again overall, not perfect, but good enough. So for me personally I'm sticking with the kitchen sneaker type shoes.

I would say the best option is to weigh some of these different factors and possibly talk to a professional about what type of shoe would be best for you personally and the specific type of role you have in your kitchen. Or if you are willing to spend the money, buy a couple different types of shoes and test them out for long enough doing some trial and error to see if they are right for you.

  
If you are gonna stay in the industry for so long, it's worth it in the long run to spend the money to find the right type of shoe for you and avoid pain and potential health issues down the road.

I definitely wouldn't pick a shoe simply based off what other people recommend works for them, because it's not a guarantee it will work well for you.  One mans trash is another mans treasure and likewise, one mans treasure might be another mans trash.
[n1nmukf] (score 5, diepte 0) Hoke Bondi SR. Six years, three pairs.
[n1od67l] (score 3, diepte 1) I switched to these after being a Dansko Stan. Love them so much!
[n1nlrjv] (score 3, diepte 0) Birks
[n1nm7pe] (score 3, diepte 0) Birks.
[n1nxpsb] (score 3, diepte 0) SAS, once they get broken in they are by far the most comfortable work shoes I've ever worn. Idk if they're a regional thing or not but I swear by them.
[n1nyb7a] (score 3, diepte 0) I used croc bistro for about a decade. I use sketchers slip ons now. I dont buy expensive work shoes. They never last any longer
[n1obmyt] (score 3, diepte 0) Snibbs. Comfortable and waterproof. Easy to clean. I’ve been in kitchens twenty some odd years. Got these a few months ago and these are doing great. They have a wide foot option which was key for me.
[n1nljzx] (score 2, diepte 0) I used to have birkenstock but those eventually became uncomfortable for me.

I rock sketchers clogs now and find them to be way more comfortable. The soles are easier to replace with a specialty one if you need it. They are cheaper too, so I feel less bad about replacing them regularly.
[n1nxxxu] (score 2, diepte 1) I had the Cessnocks for years, keep this in mind:  if your feet are even slightly wide you really want to track down a wide pair.  Had several pairs that pinched my feet for six weeks until they were fully broken in.  Switched to the cheap Crocs and now I can stand all day.
[n1nm8ej] (score 2, diepte 0) I wear Keen work boots. Expensive, but I'm on my second pair in 7ish years. 

I also wear incredibly expensive socks- Darn Tough
[n1nru7x] (score 2, diepte 1) This. Keens. Made for hiking long days, perfect in the kitchen.
[n1nnypf] (score 2, diepte 0) Hoka Bondi.
[n1npkvy] (score 2, diepte 0) I have wide feet. I used to get new balance non stick sneakers, but they never lasted more than a year. Birkenstock works ok, but not super comfortable. Sanita lasted like 8 months for me. Bought Dansko; a bit narrow, I'm wearing them occasionally trying to stretch them out. I might just have to settle for Birkenstocks for the future.
[n1nppj1] (score 2, diepte 0) I’ve been wearing Danskos for years, lately been looking to try some boot style shoes like Blundstones
[n1nsxbk] (score 2, diepte 1) Swear by danskos chef clogs. Makes you feel taller too. Breaking in is a pain tho
[n1nqu5f] (score 2, diepte 0) Snibbs! Can't recommend them enough!
[n1nwdlk] (score 2, diepte 0) Hoka non-slips. Best kitchen shoe I’ve worn in years.
[n1r1o6r] (score 2, diepte 1) This is the only answer. Transitioned recently from the leather to the synthetic. I get a couple more months out of them
[n1olniw] (score 1, diepte 2) I rock the Tokio, love them, have a backup pair for when I need to get one resoled.
[n1nybjx] (score 1, diepte 2) That’s another reason why the Danskos weren’t great for me, they’re narrow by default and I got the pinching thing from them.
[nx5wnmu] (score 1, diepte 1) Which model?
[nx6tpef] (score 1, diepte 2) [San Jose 6" Waterproof](https://www.keenfootwear.com/products/mens-san-jose-6-waterproof-boot-soft-toe-cascade-brown) - *highly* recommend 🤘 the insoles as well. I bought the K20 insoles for my non-work shoes and they were great.

Each pair has lasted about 4 years, so far. I'm finally starting to think about buying my third. I bought my current boots in early 2022. They're still perfectly wearable (no holes, look fine) but the outer edges of the soles are starting to wear down a bit. 

O/T, but the price surprised me, when I looked em up just now. $165 is the cheapest I've ever seen them. It made me curious, so I dug through my email to find what the last pair cost me, they're $20 cheaper than in 2022. In 2026 that feels like a really pleasant surprise 🤣

There's also a $10 discount for signing up for their email or something like that 🤙
[n1npcxr] (score 1, diepte 0) Sfc clog style
[n1o7hda] (score 1, diepte 1) I’ve been wearing Doc Marten waterproof, non slips (to 8 different substances!) Chelsea’s for the last year. I feel like I’m on clouds all day long. 

The initial stretch involves 2 pairs of socks in 12 hour shifts for two weeks and was a little rough but totally worth it. 

I’ve got wide balls for my feet and the added space has made a tremendous difference in my overall quality of life.
[n1ql9ry] (score 1, diepte 1) 100 percent correct. Should be everyone's standard work shoe.
[n1nv0xv] (score 1, diepte 0) Red Wings
[n1nveui] (score 1, diepte 0) Anything but Crocs, and with an aftermarket insole. My current is ’Lexniush’ off Amazon, deep heel, high arch, gel under the heel and ball. Last 4-6mos but actually reversed my plantar fasciitis after destroying my feet with Crocs. Put them in your shoe of choice, (remove garbage factory insoles) enjoy.
[n1nvudh] (score 1, diepte 0) Sneaker from ShoesForCrews. They are non-slip and feel like normal sneakers. 
No steel or plastic in the nose, dunno if that is a requirement in the place where you work.
[n1oc3qo] (score 1, diepte 1) I second SAS expensive but worth it definitely the most comfortable shoe ive worn in the kitchen. Had some for 3 years recently wanted some boots so ive been rocking doc martens Chelsea's and I love em stylish comfortable and plenty of support.
[n1r45p1] (score 1, diepte 1) This should be pinned to the sub
[n1nzgvt] (score 1, diepte 0) A variety on Jalas and Sievi work boots with Haix insoles, but I'd only recommend Jalas as I've always found them to be way more comfortable vs. any other work boot(toe protection mandatory here)
[n1nzuau] (score 1, diepte 0) 20 dollar flat bottom running shoes from Amazon….they’re comfy, though not to run in, and they grip quite well…. It’s like being barefoot but sticky bottoms…
[n1ql3kc] (score 1, diepte 1) Yupp I've said this multiple times when asked. Snibbs were the greatest thing to happen to my feet and back. Use bothe the spacecloud and the clog.

Actually got the clog 3 months ago as an anti clog person and they are my go to now over my 3 pairs of spaceclouds.

Even have a 4th pair of space clouds at home I use to walk the dog.
[n1truds] (score 1, diepte 1) Seconding snibbs!! I got the spacecloud 2.0 and am very happy.  They’re quite comfortable for being on your feet all day and actually non-slip.
[n1ocvzy] (score 1, diepte 0) I use Dr Martenz nonslip high top leather boots and the external strap on nonstick cushioning pads you strap over your boots, and sofsoles working inserts
[n1oduy1] (score 1, diepte 0) Wore Birkenstocks for over 15 years, developed plantar fasciitis. Had to try different brands, am now a snibbs guy. Great shoe, lasts and completely worth the price.
[n1oqwvc] (score 1, diepte 0) Nobody weighing in with the New Balance non slip wide fit.
[n1pxnqk] (score 1, diepte 1) Ew balance is doing g away with the 626, which is what I e been wearing for years, super dissapoint
[n1q6sxj] (score 1, diepte 2) Noooo
[n1oxm0j] (score 1, diepte 0) I use Dansko Professional and they usually last me two years.
[n1p0fdx] (score 1, diepte 0) Vans Sk8 Highs
[n1pblf9] (score 1, diepte 0) Sika birchwood are elite
[n1pd31c] (score 1, diepte 0) Non slip crocs
[n1pix21] (score 1, diepte 0) I'm rocking some sitco clogs
[n1pr3ta] (score 1, diepte 0) Merrell , steel toed, no slip sole. Still solid and comfortable after two years.
[n1qa3vl] (score 1, diepte 0) [I recommend mellow walk. ](https://ca.mellowwalk.com/category/mellow-walk-safety)

I wear the Quentin's and they last 3-4 years before the tread dies. Composite toe and no laces, very comfortable. I'm on my third pair and plan on buying another pair soon. 


Strongly recommend.
[n1r2i56] (score 1, diepte 0) Birkenstock Super Birki's.
[n1r4efk] (score 1, diepte 0) Blundstones for me. Specifically the 500 boot.

If it's good enough for chefs and stagiers at Fäviken, it's good enough for any kitchen.
[n1rgmfc] (score 1, diepte 0) Birky Bostons, no strap on the back so I can eject quickly if hot liquid is spilled on my feet.
[n1rlyz2] (score 1, diepte 0) Birks QO400 & QO500, over the last 3.5 years. Leather & better than Tokio. You don’t have to worry about re soling
[n1shj9i] (score 1, diepte 0) Birkenstocks 🤌
[n1soyhr] (score 1, diepte 0) I love Mozo very sturdy shoe it is leather so does take a little breaking on but will fit like a glove once broken in and last a while. Downside is it cost 120$ but in my opinion it’s well worth it. https://www.chefuniforms.com/mozo-grind-vegan-mens-slip-resistant-chef-shoes/GRIND.html?dwvar_GRIND_color=BLACK&dwvar_GRIND_size=11&REFCODE=CHSHOPGG&ECID=ppc~pmax~Performance-Max---Shoes---No-Assets-2025~~~~~~~~~~&gad_source=1&gad_campaignid=16474389344&gbraid=0AAAAAD8oTqQ5etHxYHo4sih99IziZwCCD&gclid=CjwKCAjw4K3DBhBqEiwAYtG_9Jn6-VHk6O1ZamtDhHA3U1P5jgQhyvWfP0erxSgJbDa4ZlFM5zAXCRoC6CQQAvD_BwE

That’s what I wear everyday makes a 12 hour shift on my feet feel like 6 hour day.
[n1srcil] (score 1, diepte 0) No recommendations really I just replace mine every 6-7m  unless I'm working ot then it's like 4m. I just get non slips from Walmart anywhere between 40-60$.
[n1tbdkp] (score 1, diepte 0) Due to my giant feet, I buy whatever sneakers that will fit, usually Sketchers or New Balance. I also have FILA non slip work sneakers but they aren't very comfortable.
[n1trz8m] (score 1, diepte 0) I’m wearing keens. They don’t hold up as long as I’d like, especially for their cost. But they make my back and hip not hurt so I don’t plan on changing.
[n1vx0uh] (score 1, diepte 0) Almost 30 years in, have done Danskos, birks, hoka. Liked them all pretty much but I’ve moved to sneakers (hoka) since I’m really moving around a lot, not really on the line.

Just bought my first snibbs after reading this thread.
[n2uv1zc] (score 1, diepte 0) Hoka bondi, just got a new pair recently and they’re awesome
[n1nlqh3] (score 0, diepte 0) I got the Sketcher’s Cessnock and the Dansko XP clogs. Even though the Dansko’s had a higher rating the Sketcher’s are working out better for me in terms of comfort and support. The Dansko’s had too much arch and heel-lift and would affect my back after a few hours. I put PF insoles in the Sketcher’s and that worked best. Everyone is different and it helps to know your weak spots and fatigue points. Insoles can also make a huge difference in a lot of cases and can range in price from a few dollars to over a hundred but it’s an investment in health when you’re on your feet as much as we are.
[n1nn01q] (score 0, diepte 0) Sketchers and I cannot stress enough - good insoles.  Commercially made shoes do not come with good insoles. Get yourself some superfeet orange insoles
[n1nnq17] (score 0, diepte 0) The new armadilo is actually not bad. Just takes three weeks to arrive.  I’m adding a new insole. They are comfy and I’ve been wearing them about three months. Foot pain almost non existent
[n1nqetz] (score 0, diepte 1) I second the shoes for crews clogs. Cheap, surprisingly breathable, good grip, lightweight.
[n1npmxu] (score 0, diepte 0) crocs
[n1nsakz] (score 0, diepte 0) Combat boots or hey dude non slips

=== THREAD xj3gg8 ===
SUBREDDIT: r/retailhell
DATUM: 2022-09-20  SCORE: 42  REACTIES: 63
TITEL: My feet are on fire 🔥 at the end of my shift
POST (source_id=post):
Not only do I have to deal with customers who make my life hell, but when I come home from a long shift my body is a wreck, and especially my feet are killing me 😱

Any tips on how to get rid of foot pain?

&#x200B;

P.S. 

Did some research online and found these insoles. Has anybody tried cushifix and give feedback?

&#x200B;

https://preview.redd.it/bfqaazmkn1p91.png?width=1125&format=png&auto=webp&s=dbd73d0a2a3224d6075ed6a20ed2e05eb98d651d

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ip6aqse] (score 20, diepte 0) I suggest Skechers, invest in arch support/memory foam shoes. I'm sure there are other companies out there with these kinds of shoes but I have fallen arches and Skechers works for me to an extent.
[ip6k5ft] (score 17, diepte 2) Skechers. They don't just make trainers.
[ip6eh21] (score 15, diepte 0) It’s all in the shoes. Find what’s right for you. A lot of my colleagues and I have noticed our feet have grown since working retail. Some have gone up a size, my feet got wider so now I have to wear extra wide.
[ip6k6ge] (score 13, diepte 0) If your feet swell, some compression socks may help. My dad (a millwright) and my sister (a nurse) both swear by them. Just buy the low end of compression to try them out- it’s 8-15mmHg.
[ip6cjj3] (score 9, diepte 2) You can also ask your employer to purchase foam or rubber support mats to place where you stand behind the register. It helped me a bit plus insoles. Unfortunately the only good insoles I found were like $50 I think they were dr shoals
[ip6rmxb] (score 9, diepte 1 OP) I noticed that too. My old ballerinas from years ago no longer fit 🤣 

Have you ever tried insoles, can you maybe recommend a good brand other than the usual Dr. Scholls?
[ip6cdtd] (score 7, diepte 2) Try the brand superfeet or Dr.scholls, maybe see a podiatrist too to see what's causing the pain.
[ip6hofs] (score 7, diepte 0) Good padded socks, (think hiking)
Supportive shoes with room for toes,
Keep moving your feet, (whenever you get a new customer make fists with your toes)
Roll a golf ball or similar with your bare foot while seated at the end of the day.
Retail can be hard on your feet, these tips will help long and short term, to alleviate some symptoms now and to strengthen your feet so you won't have as many problems in the future.
Good luck and keep smiling!
[ip6mwss] (score 6, diepte 2) I wear "Bob's by sketchers".   I have some in brown leather, hopefully they come in black.    

I think it's a combination of shoes and getting used to it.

And, if you do tasks in one spot, like register or hanging clothes, ask them to get you an antifatigue mat, or I have seen people buy them themselves (no more expensive than shoes, but a pain)
[ip6u4be] (score 6, diepte 2) The copperfit ones they advertise on TV actually work really well. Walmart sells either them or a very close knock off.
[ip6soie] (score 5, diepte 1 OP) Never tried compression socks, do you recommend any specific brand?
[ip71gp6] (score 4, diepte 4) You're risking issues with the heart, stomach,  kidneys...even read about issues with the liver
[ip6qpp3] (score 4, diepte 3 OP) >ot, like register or hanging 

Interesting, never heard of a antifatigue mat. Thanks for the tips!
[ip6dfe5] (score 4, diepte 0) Experimenting with ice and heat has helped me.
[ip8j2xg] (score 4, diepte 2) Retail worker here and I love Dr. Motion brand compression socks. You can get them in no show for wearing with Vans, ankle for wearing with sneakers and crew for boots or whatever. Finding the right shoe is imperative tho!
[ip6r4zq] (score 4, diepte 0) Proper shoes with support, change your socks and shoes half way through your shift, support socks. Once you get home, try out a variety of creams. I use deep heat and tiger balm. 

If the pain persists, see a doctor. I was crippled until my doctor got me professionally made insoles. Look up plantar fasciitis. Not fun.
[ip6rpdo] (score 4, diepte 0) Lots of nurses who work in the OR (lots of standing still for long periods,) swear by their Danskos. I absolutely love mine, too, and I tend to do a lot of running around during my nursing shifts. Compression socks and then Tylenol at home.
[ip759jh] (score 4, diepte 0) warm epsom salt bath when you get home.  And like others have said get you some good insoles
[ip7azap] (score 4, diepte 0) Compression socks and a good insole with well fitted shoes.

This is gonna sound like bad advice for a tired retail worker: but you NEED to exercise. Build muscle in your feet and legs, stretch them. Having a healthy body that is used to harder activities makes you able to last longer

Edit to add: foot soaking end of shift with warm/hot water and Epsom salts.
[ip68d4z] (score 3, diepte 1 OP) On very busy days I do that too. But I was wondering if there are other ways to reduce my foot pain without taking pills.
[ip6atbu] (score 3, diepte 2) Please don't take Aleve often, it may lead to health issues.
[ip6bslh] (score 3, diepte 1 OP) I can't wear running or fitness shoes anymore at my new job. We have to wear black leather shoes. Have you tried any insoles, can you recommend a good brand?
[ip6x8ft] (score 3, diepte 3) I use Superfeet insoles and now no more blisters on the bottom of my feet
[ip7drcl] (score 3, diepte 2) They’re expensive but I bought a pair of Hokas (Bondi SR), and theyre leather and come in black. theyre orthopedic sneakers so they really help with arch support. I threw a pair of doctor scholls inserts in too!! That plus compression socks and even after a 10+ hour shift my feet don’t really hurt!!
[ip7blzd] (score 3, diepte 1) I second this. Skechers are the only shoes I can wear at work that don't hurt my fee. And they definitely have more than just fitness shoes. I was only allowed to wear solid black work shoes for a while, and this is where I would get my shoes.
[ip6ywlm] (score 3, diepte 2) I have only tried Dr.Scholls. There is a variety on insoles.com, but they are expensive.
[ip6f7w2] (score 3, diepte 0) Vibrating foot bath massagers can alleviate some of the pain.
[ip86hgq] (score 3, diepte 2) 4000mg per 24 hour period is the limit. I take two 500mg once a day after I've worked (which is three times a week), but yes, good point. We do love our livers. Sure hope you're also not drinking alcohol, at all Bobby Dirt.
[ip7ah0i] (score 3, diepte 0) Best "dress" shoes for people on their feet:  SAS shoes.   They are a little pricey at $175-$225 but WELL worth. I've been in retail 25+ years and standing on tile floors 8-9 hours per day.
[ip7bdcg] (score 3, diepte 0) Wear the shoes the nurses do. I changed to some cork insole Birkenstocks after too many trainers & steel toecaps failed to help. Great for your feet, not so much for your style.

A knock off massage punch-gun is a good investment too. It often made the difference between walking on needles the next day or not.
[ip7quzm] (score 3, diepte 0) Soak your feet in warm water and buy shoes with cushion in it
[ip80dww] (score 3, diepte 0) Depending on what state you're in/what insurance you have, talk to your doctor. Some states like NY, if you're on the NYS state healthcare stuff, you can actually get a pair of custom-fitted shoes with custom inserts, or steeltoe boots, once a year or so. Good to look at. Failing that, get properly fitted insoles and good shoes like New Balance, try to avoid standing when possible, and if the pain gets bad, epsom salt soaks help a little.

&#x200B;

But, again here, if you're getting foot pain? Talk to your doctor. Seriously. If you need to, look at other job options, because foot pain leads to standing weird and that leads to back pain, and you don't want to get that or make it worse. Spinal pain has been the most terrifying and debilitating thing I have ever experienced and I would not wish it on anyone I've ever met.
[ip9mthi] (score 2, diepte 4) Not that I’ve noticed! When I’m not at work I tend to wear flip flops or normal sneakers, and haven’t had a problem. I haven’t tried wearing different shoes at work though, so I can’t comment on how it would feel at work again without the hokas
[ip6rxxn] (score 2, diepte 1 OP) I tried padded socks a couple of times but didn't have much success with them plus my feet got hot 😅
[ip7kef6] (score 2, diepte 1) Good suggestions but I thought taking too much Tylenol or acetaminophen can damage the liver?  Be careful!
[ip6w8qm] (score 2, diepte 0) Adidas ultraboost ended my pain.
[ipa92q4] (score 2, diepte 1) I swear by SAS. Their sandals saved my feet.
[ipbgk0n] (score 2, diepte 2) Muscle building. Having bare bottom feet will obviously cause major foot pain without natural cushioning. If your job is also heavy lifting, I don't see how avoiding exercise would benefit you. Your work is not a replacement for exercise. Weight lifting will gradually allow your body to build muscles so that you can handle heavy items easier. Most large items in retail aren't shaped ideally to be picked up without certain mechanics but not having a strong foundation makes it that much more difficult.

Get a trainer. Sure you can start on your own but a trainer can spot your form to make sure you do the exercise right and avoid injury.
[ip7wo86] (score 2, diepte 1) Yeah exactly this. You aren't going to be winning any best style shoe awards with some of these types of shoes because often times they look a bit like what gramps or grams would wear but your feet will thank you at the end of the day and not telling you to chop em off when you get home... You aren't going to a fashion show at work are you?
[ip7cg51] (score 2, diepte 0) Insoles will save your life, trust me.
[ip7v3dt] (score 2, diepte 0) Size is really important; not just length but also width. Your feet also increase in size as the day progresses. One of my favourite brands is Florsheim because they also sellultiple widths of their shoes.
[ip6y1ev] (score 1, diepte 3) Wait, really? Just ulcers or something less expected?
[ip8bbdd] (score 1, diepte 4) They look like rubber bath mats but have thick foam on the bottom and are about twice as wide.
[ip8z49w] (score 1, diepte 3) Do you have any issues with going back to regular, non-Hokas after wearing these? Asking because Dansko is very similar to Hokas but I try not to recommend Dansko as people cannot go back to normal shoes afterwards due to increased foot pain.
[ip9nicu] (score 1, diepte 5) Thank you!! This is great to know, I hope we can start carrying Hokas at my work so I can quit recommending Danskos
[ip9pz3l] (score 1, diepte 3) Dollar Tree has them too.
[ip8jb9i] (score 1, diepte 3) I got mine my first pair at Marshall’s but never found them their again. Kohls has crew and ankle but for no show and liners I had to go to the Dr. Motion site.
[ip902b7] (score 1, diepte 3) Only on holidays or special occasions. Got enough health problems as is though especially with the sweets - I don't need any more problems with drinking... I walk on average 25,000 daily steps, 10 or 11 miles 5 days a work week at least... Custodian work is no joke...
[ipa4qdy] (score 1, diepte 1) Okay sorry if this is stupid to ask, but I literally never exercise - what sort of exercise do you mean? Like swimming or yoga for general fitness, or direct leg training like with weights or something? I've often felt like I need to do something to help me make my job more bearable (standing 8.5 hours and lots of heavy lifting) but idk where to start frankly
[ip7brtx] (score 1, diepte 0) Crocs
[ip7rcrg] (score 1, diepte 0) They have these slip on at Walmart. Just slip them on your feet and they work.
[ip7rnz2] (score 1, diepte 0) Invest in REALLY good shoes.  A lot of people love Danskos, my personal favorite are Taos.
[ip83tg3] (score 1, diepte 0) I like to wear short toe-less compression socks.i wear them at work and when i get home
[ip8igvp] (score 1, diepte 0) I works at Asics, and we have shoes for certain foot types. Example: high arches vs low/no arches, etc Also look into “pronation” and the way you walk. If your foot turns inward vs outwards when walking you need a shoe that will help correct/provide extra support for those areas.
[ip8ypyu] (score 1, diepte 0) NURSING SHOES!! I work in a scrub store and they have been a lifesaver - plus they're cute and affordable if you don't go for Klogs brand or clog style! Not to mention they last forever because they're built for constant wear in 12 hour shifts 5+ days a week.

Look into Infinity Footwear by Cherokee. They are the most comfortable shoes I've ever owned. Personally, I like the Bolt style, but they also have the Rush and Echo if you're into the Vans style, and some other tennis-style shoes too.

Out of all the nursing shoes out there, I do not recommend Dansko only if you are not willing to only wear Dansko the rest of your life. They have amazing support, but take a while to get used to (your feet will hurt MORE for a little while), and once you are used to them you physically cannot go back to regular shoes unless you're willing to deal with a painful transition. It's also very difficult to order Dansko online without trying them on, as they are all hand made and each pair will fit differently.

Edit: I saw in a further comment that you can only wear black leather shoes. Infinity has the FLOW style in all black leather for this!
[ipa3duk] (score 1, diepte 0) i like a nice hot foot bath with epsom salt. i have no idea if the epsom salt even does anything but the warm water feels amazing on tired achy feet. a lot of foot bath devices have massagers built-in too, so that can also be a benefit.

i helped with inventory the other night and i forgot to wear my good shoes with insoles and paid dearly for it, so i understand exactly how you feel lol.
[ipaayxc] (score 1, diepte 0) I really like my croc runners, I noticed a big difference in foot health when I started to use them. They are close enough to a black business shoe that no one bothers me at work.
[ipack53] (score 1, diepte 0) I have to ask, how many miles do you lay down in a day? Second question, how old are your shoes? Third, how frequently do you change insoles?

One of my ASMs estimates she does 12 -15 miles a day. I probably clock eight to ten, because I don't have to answer every 'oh shit' call from the registers or customer service (which are on opposite ends of the store). My current pair of Filas I've had for 11 months. These are basically on their last legs, because I swapped out insoles recently, and the foot and leg pain are not going away. I change my insoles when I change my mascara and toothbrush -- every three months like clockwork. 

New pair of Filas will be here on the 23rd. I recently started with compression socks. They've helped, but a new pair of shoes will help more.
[ipbwj6p] (score 1, diepte 0) I bought these insoles two weeks ago because my sister (who also works in retail) recommended them to me. So far I am happy with [cushifix](https://cushifix.com) insoles. My feet are less sore at the end of my shift and I stll have energy left to go on an walk with my dog.
[ipkfjxm] (score 1, diepte 0) Crocs or hay dudes only shoes I can stand and walk in for more then 2 hours with out my feet hurting to the point I can't stand or walk
[ip6811q] (score 0, diepte 0) I take Aleve before work.
[ip7thiq] (score -5, diepte 0) Damn maybe u should post some pictures of ur feet so we can see how bad it is‼️‼️‼️‼️

=== THREAD vxv1r5 ===
SUBREDDIT: r/AmazonFC
DATUM: 2022-07-13  SCORE: 36  REACTIES: 63
TITEL: does anyone else change out of their safety shoes to their normal shoes just on break because their feet hurt so much
POST (source_id=post):
[deleted]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ifyghwp] (score 40, diepte 0) I did this and those fuckers gave me a documented coaching for not wearing my safety shoes and I literally had them in a clear backpack and just came back from lunch. These niggas be keyboard happy with the write ups
[ifygyqe] (score 22, diepte 0) My safety shoes (boots) have become my every day shoes……they’re that comfortable
[ifym8ad] (score 21, diepte 1) I would have appealed that if you were not on the floor.
[ifyge36] (score 13, diepte 0) I take mines off in my car up until I gotta go back 😭
[ifyjhrk] (score 11, diepte 0) Nah no time. Just kick them off and hop into the shower first thing when I get home.
[ifz69tu] (score 8, diepte 1) Link??? Cause I need those
[ifym6dj] (score 7, diepte 0) No my timberland pros don’t hurt at all
[ifyx0mk] (score 7, diepte 0) Nope never wore my safety shoes before
[ifz8knt] (score 7, diepte 0) I wear slides to and back from work
[ifyhluh] (score 6, diepte 4) Yup
[ifyf5nc] (score 6, diepte 0) Lol I don’t wear mine. It’s fully mandatory for us starting the 17th.
[ifz1y9x] (score 6, diepte 0) Mine are more comfortable than normal shoes
[ifzjrha] (score 5, diepte 2) Yes, please share, mine are horrendous!!
[ifyjjd1] (score 4, diepte 1) Same i sometimes turn on my seat warmer for my back
[ifyf0ck] (score 3, diepte 1) I plan on keeping them on and hoping no one notices
[ifygwu1] (score 3, diepte 3) Caught?😂
[ig0jl3l] (score 3, diepte 1) Same, I take them off and I have a tennis ball I take with me to roll my foot on top of. Taking off my shoes on break is just as important as hitting my wax pen.
[ig1btj9] (score 3, diepte 1) If I had a car I'd be tempted to change into my pyjamas and have a nap😅
[ifymvda] (score 3, diepte 0) i used to come to my car to take my shoes off to let my feet breathe. move your toes around and try to stretch them a lil. made a huge difference in my foot comfort throughout the long day.
[ifyzbtt] (score 3, diepte 0) buy some good insoles , my sht usta hurt now i do my 10hr shifts like nothng
[ifz36da] (score 3, diepte 0) Not on break the second I reach my car after work it’s the first thing I do.
[ifz4jrw] (score 3, diepte 0) If they hurt, you didn't buy the right size. Do you think tradesmen are wearing boots that hurt their feet? Nope, mine are like walking on clouds.

People usually get them too narrow at first.
[ig1f99u] (score 3, diepte 1) How about when you get them 1.5 larger and extra extra wide and they still rub your damn toes? What are you supposed to do then? Any bigger and I'll start tripping on the f'ing clown shoes.
[ifye9ko] (score 2, diepte 0) And not back to the safety shoes? Yes.
[ifyfkln] (score 2, diepte 2) Mission unsuccessful 😭
[ig0w0k5] (score 2, diepte 2) I bought them 2 years ago off Zappos at Work. Pair of Ariat Boots….RealTek i believe??? Paired with some gel pads (chefs kiss)
[ifzf1rc] (score 2, diepte 0) Time to find more comfortable safety shoes.
[ifzf393] (score 2, diepte 0) No one even checks if you are swearing "safety shoes" at my FC
[ifzfzq9] (score 2, diepte 0) I just take mine tf off
[ifzgpsz] (score 2, diepte 0) My timberland pros are actually comfortable plus I have dr scholls inserts I’m so accustomed to wearing them I forget not to wear them on my days off😭
[ig04j02] (score 2, diepte 0) You need new safety shoes, my Reebok lites are amazing
[ifydyip] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.gg/amazonfc) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[ifyts54] (score 1, diepte 0) I don’t even wear safety shoes. My raggedy ass onclouds are the most comfortable footwear I’ve ever owned and I will never trade them for another shoe
[ifyxevb] (score 1, diepte 0) Tear up your regular shoes
[ig1ezbd] (score 1, diepte 1) Same here. I have a pair of flip flops or sandals waiting for me in my car. First thing I do is take those suckers off and chuck them onto the back floorboards so I don't have to look at them until I get home. lol.
[ifz4293] (score 1, diepte 0) bust out the slides 😮‍💨
[ig1can3] (score 1, diepte 1) I just wear regular military style boots cuz they have to be steel toe cap
[ifzul6e] (score 1, diepte 0) Just on break ? Idk that seems like a waste of time to me. You could always just take em out of the shoe while your sitting outside, but I mean you do you fam.
[ig05xxd] (score 1, diepte 0) No, my building they’re mandatory, first time caught is a write up second time is fired
[ig0cd5r] (score 1, diepte 1) That’s actually super against the policy to be threatening a fire? 

1st time: Talk trying to see barriers - issue you a pair of slip on clown shoes / re credit  
2nd time: Coaching with HR involved and wrote into ENAGE. 
3rd time: Write up for failure to wear PPE.
[ig0wae3] (score 1, diepte 2) I just work here, I also wear my safety shoes so it’s not a concern
[ig0bkj9] (score 1, diepte 0) You guys can actually ask your safety team to submit a re-credit to your account and order new shoes again - if they say  no they’re lying through their teeth. 

The styles are always changing depending on what Amazon is buying from other companies. Lately there’s been a lot of Skechers with the Arch Fit/ Cushioning.

You guys can also purchase BOGS slip on shoes with the comp toe and wear your regular shoes under it. It’s a big loop hole in the policy but checks all the boxes.
[ig0dieu] (score 1, diepte 0) So many people at my fc don’t wear safety shoes. Nobody gets told anything. However there’s always that one manager that picks and chooses.
[ig0dlo6] (score 1, diepte 0) I weren’t my regular shoes on my weekdays and safety on weekends.
[ig0iwvl] (score 1, diepte 0) How tf are yalls shoes always so uncomfortable, mf will complain about anything
[igexrib] (score 1, diepte 1) Because everybody’s feet is different because everybody is different what’s comfortable to you might not be comfortable to someone else no 2 people are the same
[igf063z] (score 1, diepte 2) Fat ass
[ig0orxn] (score 1, diepte 0) My safety shoes are actually extremely comfortable
[ig0pvis] (score 1, diepte 0) I just don’t wear safety shoes. I just avoid the safety guys anytime they walk around trying to scan people without them lol. Fuck those uncomfortable ass shoes I walk 20 miles a day
[ig0wvhq] (score 1, diepte 0) Y’all actually wearing safety shoes…
[ig0yy4j] (score 1, diepte 0) Do you use insoles?
[ig11ejo] (score 1, diepte 0) I've seen around 12 AA's come on with normal shoes because no one is checking anymore
[ig1bhzl] (score 1, diepte 0) I wore steel over toes and when I’d take them off during break a manger (new guy) would ask me to put them back on. Some ppl take their jobs too seriously.
[ig1ce3m] (score 1, diepte 0) How tf r u all wearing trainers we have to wear boots
[ig1mubg] (score 1, diepte 0) At my FC safety shoe enforcement has made AirPod and sitting at your station enforcement go bye bye. It seems they can only concentrate on one thing at a time.
[ig1mzzi] (score 1, diepte 0) Nah but I be wearing my crocs when I’m heading to work and put my work shoes when I get there and when I leave switch back to my crocs.
[ig1pexg] (score 1, diepte 1) There’s a dude at my fc that works in crocs. I thought it was the funniest shit the first time I noticed.
[ig1sl06] (score 1, diepte 0) Change? !!!    I go shoeless on my coffee break
[ig2aubo] (score 1, diepte 0) almost nobody at my facility wears them even tho it's been "mandatory" for a while. none of the managers I work with wear theirs. i went through so many pairs before I finally found a pair that's comfortable to wear for long periods of time and nobody even checks for them lol
[ig2riu1] (score 1, diepte 0) It is required at our site to wear safety shoes but I still see lots of people not wearing safety shoes during working hours. Security staff be like 🙈
[ig38z8y] (score 1, diepte 0) Nah
[ig40xc3] (score 1, diepte 0) I would be willing to take a pay cut to not wear these stupid shoes. This is insane.
[igltqn0] (score 1, diepte 0) Do you have to order off Zappos or can I order off *gasp* Amazon.

=== THREAD 1vfmisg ===
SUBREDDIT: r/Teachers
DATUM: 2026-08-04  SCORE: 23  REACTIES: 63
TITEL: Classic white sneakers that are comfy enough for teaching on your feet
POST (source_id=post):
I’m looking for a classic white women’s sneaker—something I can wear with jeans, dresses, etc. I’m a preschool teacher, so I’m on my feet literally all day. The right shoes make the difference between a good day and a day with a lot of back and knee pain. Can anyone recommend a great sneaker that’s supportive, not stiff to wear, and easy to clean? Good-looking is a plus, but secondary to comfort.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[p1qewjz] (score 28, diepte 0) Preschool teacher here with flat arches that are collapsing with age.  Go to a running store and get really good quality inserts that fit into any sneaker.  They really make a difference no matter what shoes you end up choosing.
[p1q6gsi] (score 20, diepte 0) I'm partial to my birkenstock sneakers.  White, classic and comfy
[p1q5rol] (score 12, diepte 0) My most supportive shoes by far are my hokas, but they do give dad sneaker a little bit (although some people are into that!). My Veja V-9s are my most comfortable fashion sneaker and I love those too!
[p1qaca8] (score 8, diepte 1) Yes, they are perfection! Cute, easy to wipe clean because they’re leather, and so comfy!
[p1qlh66] (score 8, diepte 3) I am so excited to have found this thread!
[p1q81p2] (score 8, diepte 0) New Balances did the trick for me, they come in lots of different styles.
[p1qai12] (score 8, diepte 0) Brooks Ghost Max.  I got all black ones and my daughter (entering nursing) got all white (leather) ones. They are THE BEST
[p1qlb87] (score 7, diepte 2) Yes, excellent arch support. They also come in narrow and wide widths.
[p1q8v65] (score 6, diepte 1) Came here to say the same thing. I love my Birkenstocks.
[p1q961g] (score 6, diepte 0) A lot of nurses recommend Hokas. My orthopedist also wears Hokas.
[p1q6iln] (score 5, diepte 0) Sambas
[p1q8j9k] (score 5, diepte 0) I just got onitsuka tigers and they are the most comfortable shoes I’ve ever worn. I have a few different types and they have the best cushion. Also I have custom orthotics so they help with support.
[p1r8ir8] (score 5, diepte 0) Dr scholls has a ton of difffent kinds of sneakers that are super comfortable. Lots of white options and if you want color they also have a bunch.
[p1qcyq7] (score 4, diepte 1) Do they have arch support inside?
[p1ql14d] (score 4, diepte 1) Yes, I almost exclusively wear Birkenstock Bend Low sneakers. I have them in every color.
[p1s7idx] (score 4, diepte 0) Whatever you choose, choose 2 or 3 (ideally) different pairs and rotate. My first ever boss was a podiatrist. His advice to me upon learning I was going into the teaching profession was to have “work shoes” (plural) that I can let rest and “dry” (yes, gross, but feet are feet) a day or two between wearing. My feet and shoes would be happier. 

I kept (retired now) a pair of sandals/slippers/grocery store knock offs of fancy brands that I’d slip on after school as I sat and graded/prepped. 

I taught middle school so it was Vans, Dr.Martens, and various Clark’s 2W I believe are discontinued or just made too narrow now. I replaced them all regularly, but like 3-5 years regularly rather than every school year growing up with school shoes as a student. 

Now I’m a New Balance (2W), Birks, and Camper person. But I don’t have any need to run or jump over a desk moments…good luck.
[p1sdglk] (score 3, diepte 0) Just get inserts!
[p1qiyxt] (score 2, diepte 1) Bingo! I've taught wearing my Sambas many times and never had a problem.
[p1q753d] (score 2, diepte 0) Saucony are amazing!
[p1q8wtf] (score 2, diepte 1) I'm wearing some right now! I tried on a whole bunch of the "usual suspects" (Nike, Adidas, Reebok, etc.) but in the end, the Saucony shoes felt the best.
[p1qdfgg] (score 2, diepte 2) I was having a lot of foot pain and went to a specialty store that does fittings. They recommended Saucony and I haven’t looked back. I even converted my mom!
[p1r7705] (score 2, diepte 1) This… my podiatrist finally talked me into them and my feet are much happier!
[p1qaiqb] (score 2, diepte 0) Check out Easy Spirit shoes, you can find them online.
[p1qcpwu] (score 2, diepte 0) This post's comments  might have some options for you
https://www.reddit.com/r/fashionwomens35/s/N9tbkV6Ndl
[p1qg7c2] (score 2, diepte 0) As a SPED teacher I wear Hokas to chase my runners (mine aren't white) and they are the most comfortable. For when I need plain white shoes for outfit purposes but still have to be able to walk and stand for long stretches, I wear Dr. Scholls.
[p1qi7bx] (score 2, diepte 2) I have 2 pairs of the women's Rebel Sports Sneakers. (I guess the soles are light brown though). They do have some other styles that are fully white.
[p1qges6] (score 2, diepte 0) Does Reebok still make the Princess line? My coworker swore by those.
[p1qi4vq] (score 2, diepte 0) I love my Allbirds Tree Runners! I have them in multiple colors. They look nice, are SO lightweight, and you can wash them in the washer!
[p1ql9hw] (score 2, diepte 0) New Balance 547 or 515s! I love love love NB!
[p1qn7kt] (score 2, diepte 0) I wear Adidas Superstars and they’ve been great! My husband collects Sambas and watches the sales, so I grabbed a new white pair when they went on sale for $60.
[p1qong8] (score 2, diepte 0) Oofos club
[p1r1kif] (score 2, diepte 0) Loooooove my OnCloud sneakers. I also have an old pair of Nike LowCourt sneakers that I have worn comfortably through the US and western Europe.
[p1q5jm3] (score 1, diepte 0) Olukai. Pricey but comfy and last forever
[p1vh53o] (score 1, diepte 1) Agreed, love these shoes.
[p1suidd] (score 1, diepte 1) Seconding HOKA, love my Clifton 10 shoes! I have high arches and they are so comfortable \[and never leave my feet or toes in pain, like flats do\].
[p1q9rnt] (score 1, diepte 0) Platform Converse shoes. I have a black pair that I can wear all day and my feet are fine, even with plantar fasciitis.
[p1qbe3d] (score 1, diepte 0) rothy’s. always comfy right out of the box and machine washable
[p1qbit1] (score 1, diepte 0) Brooks white leather sneakers are supportive and have a comfy, roomy toe box.
[p1qfsgq] (score 1, diepte 0) I love All birds for style/comfort, and I think they've got some all white options!
[p1qg51c] (score 1, diepte 0) I recommend Fila and Sketcher delights, did very well for my teaching activity.
[p1qgd61] (score 1, diepte 1 OP) Which Dr. Scholls do you like?
[p1rctfy] (score 1, diepte 1) Absolutely 2nd Hokas and Dr Scholls
[p1qi6c7] (score 1, diepte 0) I love my Allbirds Tree Runners! I have them in multiple colors. They look nice, are SO lightweight, and you can wash them in the washer!
[p1qj9v0] (score 1, diepte 0) I love my Adidas classics. Nice and wide too.
[p1qkepv] (score 1, diepte 0) Custom platform converse with extra insoles! I get a new color of leather each year. Soo comfy and versatile.
[p1qkj3l] (score 1, diepte 0) I have trouble finding footwear too.
[p1qn50v] (score 1, diepte 1) Chiming in another vote for NB! They are the only runners that consistently fit my orthotics and have enough room in the toes for my super wide feet.
[p1qlzmt] (score 1, diepte 0) Hey Dude, Karina style sneakers. Cute, very comfortable, dress up and down easily, and there are several variations of colors!
[p1qv7vk] (score 1, diepte 0) Eccos!
[p1r0kkr] (score 1, diepte 0) OrthoFeet makes good ones
[p1s2432] (score 1, diepte 1) Came here to say dr scholls
[p1rgnqz] (score 1, diepte 0) Dr. Scholls has white sneakers and they also come in different colors and patterns.
[p1rw5bt] (score 1, diepte 0) Vionic Winny.  I've gone through three white pairs and have several other colors too.  Arch support.
[p1rwbdb] (score 1, diepte 0) Another vote for Dr scholls. I teach art in a room with a concrete floor and they do the job.   
I also have some platform adidas that I love. That platform really helps make it easier to stand all day.
[p1s0iu1] (score 1, diepte 0) Dr. Scholls time out sneakers. Probably the most comfortable shoe I own. I also have high arches so need that support. I wore them on my vacation to Japan and my feet never hurt….the rest of me yes but not my feet.
[p1s1x3s] (score 1, diepte 0) Splurge - oncepts  
Affordable - vans
[p1saf6o] (score 1, diepte 0) Ooh, you have to try the Dr. Scholl’s  
Women’s Madison lace up. The white with the gold accents is so cute and comfy.
[p1sb1re] (score 1, diepte 0) I have a pair of Vejas and find them very comfy!
[p1sh5r4] (score 1, diepte 0) Veja shoes are hard to break in but once you do, they hold up and last a long time.
[p1sjvph] (score 1, diepte 0) I will live and die by my sketchers slip ins.  So comfortable.
[p1sn7uk] (score 1, diepte 0) I work as a lunch lady now, and swear by hoka brand shoes.
[p1u4wz6] (score 1, diepte 0) I can’t join the Hoka craze; they’re just too squishy. I carry some extra weight, have a really bad bunion.

Love my Adidas Nizza Platforms for these reasons; they offer resistance and lift every step. 

I’m K5 and wear them several times/week. I can usually get 3/4 of the school year out of them, and could get more if they held up better with serious washing. Black pair lasted about 2 years.
[p1ywetg] (score 1, diepte 0) I live in my ON’s. I do also have HOKAs.
[p26d7o5] (score 1, diepte 0) I’m happy with my Sambas

