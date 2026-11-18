# Label-batch batch_0076

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
Schrijf het resultaat naar `batch_0076.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1d6o7ek, y9dg0w, 1rvw7cm).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1d6o7ek ===
SUBREDDIT: r/cna
DATUM: 2024-06-02  SCORE: 41  REACTIES: 94
TITEL: Comfortable shoes?
POST (source_id=post):
I just started working as a CNA. What kind of shoes do you guys prefer when working for long shifts?

I just worked two days and my feet is so sore:)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l6u1olk] (score 26, diepte 0) hokas
[l6u3t1i] (score 22, diepte 0) Sketchers
[l6v529a] (score 17, diepte 1) You're a psychopath
[l6u0skt] (score 16, diepte 0) Crocs....and wear ted hose/compression socks....seriously wear the socks....I know a lot of places don't allow Crocs....but I work at an Assisted Living as a Med Tech...honestly wide shoes...let those toes spread out....
[l6u62v5] (score 14, diepte 0) they might be ugly, and kind of expensive, but i LOVED my hokas!!
[l6u69u4] (score 14, diepte 0) I like my Cloves
[l6tr3j6] (score 9, diepte 0) I used to wear ASICS!
[l6twekn] (score 8, diepte 0) brooks ghost 15
[l6v0yan] (score 8, diepte 1) Agreed. Compression stockings with crocs are the best I’ve tried. I have the “bistro” style crocs with no holes in them. A little sweaty in there but nothing gets in and they are easy to clean!
[l6x2dbf] (score 8, diepte 1) I know they get hyped up a lot but it's for good reason. It instantly made a difference on my joints after I got a pair.
[l6v6luw] (score 5, diepte 1) Yes!  Louder for the people in the back!  With compression socks. IT WILL CHANGE YOUR WORK LIFE!
[l6v1gfl] (score 5, diepte 1) Can’t go wrong with em.
[l6v1525] (score 5, diepte 0) Me personally I wear vans
[l6x4oox] (score 4, diepte 1) I love my hokas!
[l6y6ps1] (score 4, diepte 1) their work shoes are kinda ugly but the healthcare line ones have a few cute ones!
[l6ubqlr] (score 4, diepte 1) me too!! waterproof as well :)
[l6trt6k] (score 3, diepte 1) Yes I do too !! I have the gel-keyano 28
[l6vmi7b] (score 3, diepte 1) Love my ASICS too! I wear compression socks religiously and switch out my insoles after 4-6 months.
[l6tudch] (score 3, diepte 0) I'm odd and wear black boots for my 16s. Nice insole, ankle support, non slip.
[l6xraw7] (score 3, diepte 2) i’ve had mine for a while and i find the price to be worth it!
[l6xrjc4] (score 3, diepte 3) yea they are worth it but break down easy. It is a known thing that happens
[l6xv5t5] (score 3, diepte 5) I only wear expensive foot wear. All brand name
 But I won’t buy another pair of these. They just don’t work for me. I love how they look and feel but the quality as in breaking down isn’t what I’m used to. Glad they work for you though because as a person with RA in their feet I get the trying to find some relief that when you do, you stick with it. I’m partial to dansko and Birkenstocks both have people that hate them, lol 
 lol
[l6yhhl7] (score 3, diepte 1) Yes! Sketchers slip ins with memory foam are the only ones that my feet like.
[l6v53aw] (score 3, diepte 2) 😂😂😂
[l6woqmq] (score 3, diepte 3) I’ve definitely pulled 12s in vans, lol.
[l6vfe0g] (score 2, diepte 1) I rock ASICS too!!!!
[l6tyto3] (score 2, diepte 0) Asic Gels ftw
[l6umy35] (score 2, diepte 1) This is what I see most on the nurses at my hospital.
[l6xr6gs] (score 2, diepte 1) Comfy but last about 12 weeks with constant wear and are super pricey.
[l6xs6zx] (score 2, diepte 4) I’ve never had an issue with any of my pairs. I would rather splurge and invest in a pair of shoes that I feel good on my feet in. I’ve had tremendous foot pain before that has really impacted my quality of life, and these shoes have really helped. But you can also go to a store that has foot analysis and they can get you fitted for a pair that works for your specific foot (whether they’re hokas or another brand)
[l6u2nc7] (score 2, diepte 0) I wear hokas and they had an option to pay in installments of like $30ish every two weeks.
[l6u31w2] (score 2, diepte 0) The bistro Crocs, for cooks. Cannot recommend them enough.
[l6vdp5u] (score 2, diepte 1) I’ve had them for 4 years second this!
[l6ugxb7] (score 2, diepte 0) Hokas and clouds are the general consensus where I am.
[l6unlk4] (score 2, diepte 0) i like my onclouds more than my hokas!
[l6unt8i] (score 2, diepte 0) Hokas
[l6uslb4] (score 2, diepte 0) Hokas
[l6uv220] (score 2, diepte 0) I love my hokas. But I’m obsessed with my ghost max brooks. It’s like walking on a cloud.
[l6uzp11] (score 2, diepte 0) New Balance V4 Running shoes
[l6vsqz9] (score 2, diepte 1) Nooooo way.
[l7awt2k] (score 2, diepte 1) Praying for your feet 🤣🤣
[l6v1q9c] (score 2, diepte 0) I prefer a really good pair of combat boots, like military surplus. Liquid resistant, good tread, good support, and keeps my ankles from rolling if I suddenly have to run. Easy to clean too! My last pair lasted me a solid 3 years of night shifts, 3x 12hrs a week.
[l6vdnqx] (score 2, diepte 0) Cloves been wearing them for 4 years very comfortable shoes for long shift
[l6vez3t] (score 2, diepte 0) I hated Hoka. Ended up just wearing Adidas
[l6vgrgx] (score 2, diepte 0) lol perhaps a hot take but i wear my broken in vans slip ons🤷🏻‍♀️
[l6viqns] (score 2, diepte 0) Hoka bondi
[l6vqi7k] (score 2, diepte 0) Hokas and invest in compression socks.
[l6wxmmq] (score 2, diepte 0) Saucony Triumph are sooooo comfy!
[l6ydbr9] (score 2, diepte 0) ngl i loved my dansko clogs lol
[l6wryz6] (score 1, diepte 2) I love my compression socks! I need to get some insoles. I am not in nursing anymore but the treadmill is killing my feet. I keep getting huge ass blisters on the balls of them.
[l6vb640] (score 1, diepte 2) YESS
[l6w9rjs] (score 1, diepte 2) Preach!
[l70cwc9] (score 1, diepte 1) The brooks walking shoe, big and ugly but I don't care lol
[l6tx72w] (score 1, diepte 0) I wear wedge sole boots, but it really weirds out the nurses so maybe don't do that
[l6y2gml] (score 1, diepte 1) Came to this!
[l6u2wkf] (score 1, diepte 0) I wear the donut Crocs I got for free during COVID. Have for fours years. Tread is still good and everything.
[l6u91hv] (score 1, diepte 0) Timberland pros , with thick aloe socks so I don’t get blisters on my heels .
[l6uc15e] (score 1, diepte 0) Nike 270’s, all day , everyday…
[l6uvotp] (score 1, diepte 0) Vivobarefoot Primus
[l6uzqyd] (score 1, diepte 0) ....Doc Martens boots... I love boots.
[l6v3jnl] (score 1, diepte 0) #wearthesocks
[l6vdwae] (score 1, diepte 0) waterproof on cloud 5
[l6vr0pi] (score 1, diepte 0) Asics.
[l6wl923] (score 1, diepte 0) Oofos!!! Saved my lower back and feet as a phleb (I used to be a CNA and wish I had these then).
[l6wpz4y] (score 1, diepte 0) Asics 😍. And try wide sizing...many people need wide sizing so their feet and properly spread out, they just don't know it. If you find yourself getting calluses on your toes, you probably need wide shoes
[l6wumxj] (score 1, diepte 0) I wear sketchers with some nice inserts and compression socks. Makes all the difference. They have really fun compression socks option now too.
[l6x68sg] (score 1, diepte 0) I really like ASICS Gel Kayano
[l6xi7dr] (score 1, diepte 0) Hokas 100%
[l6xmnum] (score 1, diepte 0) Brooks running shoes and compression socks. I tried crocs and could barely make it 3 hours, there's just not enough support
[l6xntua] (score 1, diepte 0) Hoka
[l6xyjvm] (score 1, diepte 0) When I first started I wore crocs with compression socks. When I worked psych I would wear sketchers go air max with compression socks. Now I work with the DD and scrubs are not allowed to promote the “home” feeling so I wear sketchers hiking sandles or I wear sketchers go air max with compression socks.
[l6y0hjq] (score 1, diepte 0) I bought brooks, hated them. Total waste of money for me. The shoes were way too stiff and tight. Then I randomly bought a $53 pair of Asics from Amazon. I'm about to order a second pair. Only bc I've used them outside of work too and they look bad now.
[l6y2f6v] (score 1, diepte 0) HOKA!!! By a large margin the most comfortable CNA shoes I have ever owned. Worth the investment. Just look at the foam compared to other brands, it’s like twice the size and thickness. Plus they tend to have a flat food with not much insole. All around the best shoes I have owned.
[l6ywhih] (score 1, diepte 0) Hokas Clifton 9
[l6z1asn] (score 1, diepte 0) They say Nike air max feel amazing some are over 100.00
[l6z979n] (score 1, diepte 0) I use running shoes.
[l6zcedr] (score 1, diepte 0) On Clouds
[l6zr643] (score 1, diepte 0) Stand+ which used to be Gales. So light weight, waterproof and purple wipe approved. Don’t forget to wear compression socks they saved my legs and feet.
[l7031pq] (score 1, diepte 0) No one else? Really?? ALTRA ALL THE WAY BABY. Amazon has really good deals sometimes for them too.
[l70h37u] (score 1, diepte 0) Sketchers, brooks, hokas, and ASICS are what my coworkers wear! I’ve just worn sketchers so far and they haven’t failed me after six months 🙂
(4 reacties met lagere score weggelaten)

=== THREAD y9dg0w ===
SUBREDDIT: r/Frugal
DATUM: 2022-10-20  SCORE: 553  REACTIES: 92
TITEL: The Value of Good Shoes - The least expensive option isn’t always best!
POST (source_id=post):
I like to wear a cross between hiking shoes and sneakers for my non-professional day-to-day and hiking purposes. I originally needed some new shoes when times were a bit lean (I work in real estate so lots of ups and downs). I bought the shoe on the right for $48 from my local discount shoe place. After about 2-3 months, they looked like this and became my 1-2 hour per week gardening shoe. I then purchased the shoe on the left (with vulcanized rubber soles) for $122. 2-3 months later, they’re not nearly as destroyed. They hurt my feet a lot less too. Good shoes are worth the investment!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[it52w87] (score 233, diepte 0) There’s a guy on YouTube that cuts shoes in half to expose the construction of them. It is surprising that more expensive doesn’t always mean best construction or even better materials. The one he did that showed TEVA sandals compared to a Walmart cheap version and the another knockoff, the TEVA was well constructed and resisted melting if you happened to step into a camp fire. But then something like Doc Martins are actually crap now. The channel is Rose Anvil if you want to check it out. It’s interesting to know more about a shoe before you buy one. But I will say I agree I won’t skimp on shoes, but I always like to make sure I’m getting the best bang for my buck.
[it50ssi] (score 62, diepte 1) Shoes, tires, bed.

Anything between you and the ground is worth the investment
[it54823] (score 62, diepte 1) I love this dude's channel. I like when he catches some companies building junk shoes and selling them at premium prices.
[it4y3ah] (score 55, diepte 0) Shoes and tires are two things I don't skimp on. They are literally the only thing between you and the road.
[it60ywa] (score 41, diepte 2) The Tevas video is an example of expensive being better, the docs video is an example of expensive not being better. Disclaimer, I love my doc 1460s but can confirm they are overpriced and should be better
[it5fz4t] (score 39, diepte 3) Weston Kay, he’s a leather worker. The channel is called Rose Anvil, he does all kinda of boots, work, fashion, dress, and he’s does the occasional sneaker too. 10/10 would recommend, lots of good info on what to look for when shopping
[it5csbh] (score 30, diepte 0) "The reason that the rich were so rich, Vimes reasoned, was because they managed to spend less money. Take boots, for example. He earned thirty-eight dollars a month plus allowances. A really good pair of leather boots cost fifty dollars. But an affordable pair of boots, which were sort of OK for a season or two and then leaked like hell when the cardboard gave out, cost about ten dollars. Those were the kind of boots Vimes always bought, and wore until the soles were so thin that he could tell where he was in Ankh-Morpork on a foggy night by the feel of the cobbles. But the thing was that good boots lasted for years and years. A man who could afford fifty dollars had a pair of boots that'd still be keeping his feet dry in ten years' time, while a poor man who could only afford cheap boots would have spent a hundred dollars on boots in the same time and would still have wet feet. This was the Captain Samuel Vimes "Boots" theory of socioeconomic unfairness." -Terry Pratchett
[it4y6bz] (score 26, diepte 0) Footwear should be as quality as possible.  Life is a drag when every step hurts.  “Get back on your feet” has real meaning and it hard to do in painful shoes.
[it5glpa] (score 26, diepte 1) I'm sorry but I am so sick of seeing this same excerpt reposted. It's reached "Steve Buscemi was a firefighter"  levels
[it5srwr] (score 20, diepte 3) And bras for those of us who need them. A good bra is as important as good shoes and a good mattress haha.
[it5tq80] (score 16, diepte 0) Are those Merrell? Mine lasted me at least 10 years for about $100
[it5f1y7] (score 13, diepte 2) Add a good chair if you work sitting down.
[it58qhr] (score 12, diepte 0) No matter where I’ve worked it’s been on my feet so wholeheartedly agree. I rotate  Birkenstocks, Skechers and Doc Martens at work. Also I cannot say enough for Vionic insoles; they’re \~ $35 but worth it.
[it5ga1v] (score 11, diepte 5) Unless you are running high mileage with low maintenance. If I put synthetic in my 300,000 Silverado at this point, I think it might just clean out everything keeping my truck together 😂
[it563u4] (score 11, diepte 0) Here’s a frugal shoe tip: if you’re a woman and have small feet (i.e. seven or smaller), shop in the kids section. Kids sizes follow the men’s sizes, so you would need find a kids shoe that is around two numerical sizes smaller than your normal size.
[it5bipx] (score 10, diepte 2) Shoes, tires, bed, brakes.
[it4zd8z] (score 10, diepte 0) Use at least few pairs as well. I have about 15 pairs of shoes currently, some are as old as 20 years, as I wear them occasionally. Seems to keep them lasting longer than wearing them day after day, same pair. Keep an eye out at thrifts and on eBay for barely worn used shoes. Definitely a saver there.
[it7m2vz] (score 9, diepte 4) [Here](https://www.youtube.com/c/RoseAnvil) is a link because no one else has put one.
[it5h6nz] (score 9, diepte 2) I get it. I do. But unless you can afford the og shoes, telling someone without the funds to "just buy better shoes" is not helpful at all. There are so few options out there and saving 6mos means you're stuck with shit in the interim.
[it5dvwq] (score 8, diepte 2) Who is this is?
[it606li] (score 8, diepte 1) I am confused. “More expensive isn’t the best construction” and then you say Teva, which is more expensive, was “well constructed” 

If you can clarify a little better that would be helpful. Or give brands that you recommend. Thank you!
[it674a3] (score 7, diepte 1) That and a bed. I will pay 5k if i have to for a good night sleep and no back problems 20 years from now
[it5bxm6] (score 7, diepte 1) If doing this just make sure the shoe has good support! I’ve found kids running shoes to have great support for a great price, depending on the brand.
[it6i6da] (score 7, diepte 1) Birkenstocks are so expensive in my country. Took the plunge four years ago and bought a pair as my summer shoes. I’ve been wearing them almost daily for the past four years and nobody believes me that my shoes are “that old”. Bonus points was that I didn’t need new shoes during my pregnancy since they were easy to slip on and off and wide enough that my feet could still fit
[it5hz4l] (score 7, diepte 4) Did you know Steve Buscemi was helping out on 9/11? And Kevin Conroy spoke in his Batman voice?
[it5qzhn] (score 7, diepte 0) The one on the left are Merrells. I recognize the tread pattern. If it is a Moab 2(their most popular hiking shoe), they are currently being discounted because Merrell is coming out with a Moab 3.
[it5bpug] (score 6, diepte 3) Shoes, tires, bed, brakes, oil

Edit: vehicle battery
[it61crr] (score 6, diepte 7) Oh I do oil changes at the proper intervals, I just don’t use synthetic oil. Synthetic oil is “cleaner” and has certain properties that degunk things. Which is great in a newer lower mileage vehicle, but I’m pretty sure the sludge is the only thing keeping my old ass rings and seals and stuff together. So I can pay more for synthetic and eventually be left with a repair bill after the accidental destruction, or keep rocking and rolling with oreilly’s cheapest 5w30 😂
[it76ckd] (score 6, diepte 4) Not there yet, luckily.

One more Krispy Kreme, then!
[it62xkp] (score 6, diepte 2) I don’t really have specific brands, I mean I wear new balance sneakers mostly cause they fit my arches well. I normally buy clearance for those. I own a pair of uggs I got from thread up, used, for $40, they were barely worn at all. I got a pair of calf high Columbia boots that are rated to -20f for real winter snow weather. I got those on clearance too normally $129 got them on sale at shoe depot for $49. I honestly wore my Uggs most of the winter when the snow wasn’t too deep, no socks, kept my feet toasty warm. They are comfortable enough to walk in.  I buy old navy flip flops for $3 but I also have a pair of $50 Crocs that I wear constantly most of the rest of the year… I’m not super picky or fancy with my shoes, I’m not a shoe girl.

&#x200B;

edit to add I owned a pair of Tevas lasted me like 8 years, and I’ve owned Docs, lasted me a year. That’s why I brought those two up cause I watched those videos not too long ago and thought it was interesting.
[it7si3h] (score 5, diepte 3) False, I got rid of my brakes and got a $15 anchor on ebay.
[it5rd3k] (score 5, diepte 1) And both are subject to durability vs. function tradeoffs. Tires that have good traction may use a softer rubber for more grip which wears faster. Tires that last longer may have good enough traction but are noisy.
[it5c4oi] (score 5, diepte 2) Exactly. Try different styles. It is worth a shot. I work at a sportswear store, and the kids shoes are roughly $20 less than their adult equivalent.
[it5hdbq] (score 5, diepte 3) I don't disagree. But I'm just talking about people reposting this damn quote a million times. It's trite
[it5hl72] (score 5, diepte 0) My everyday shoes cost 120.00 and last at least 2 years of everyday wear.  Merrill I have found is very supportive great arch and comfortable.
[it4xi5v] (score 4, diepte 0) I agree. That’s something I don’t skimp on anymore.
[it5iw5a] (score 4, diepte 5) Stop I'm already dead
[it7cajx] (score 4, diepte 1) It also has a vibram sole, which is known for being quality
[it7evc0] (score 4, diepte 0) I recognize that Merrell tread pattern on the left shoe, the Vibram rubber sole makes a huge difference.

I have some Merrell shoes that are twenty years old!

I have varicose veins (hereditary), so I feel tired legs more than the average person. Merrell shoes with the Vibram rubber soles, along with replacing the insole with Superfeet orthotics are the best if you are on your feet all day.
Around home I switch between Birkenstocks, Haflinger, Spenco, Chacos, and Ola'kai (? spelling).
[it5gnia] (score 3, diepte 6) Well 100% follow the owners manual on oil. Don’t kill your engine that’s too much and no longer frugal!
[it5iazz] (score 3, diepte 6) They have special high mileage oil now. I wonder if it addresses that.
[it5qw2r] (score 3, diepte 1) In my experience a $70 pair of Skeechers steal toes are as good as a $140 brands. They've always lasted till the next workplace shoe voucher of 2 years.
[it6o8bp] (score 3, diepte 1) Crying in size 10 ☹️
[it69uvn] (score 3, diepte 1) Vionic shoes - found then two years ago and love them!!
[it6wuqo] (score 3, diepte 1) I came into this thread specifically to find this somewhere.
[it5g5j8] (score 3, diepte 0) I bought a $5 pair of shoes on Wish once they lasted me 2 years without needing repairs. I buy work boots in the range of $100 - $300 and they usually last me 2 years.
[it5r15p] (score 3, diepte 1) I get 2 years out of my $55 New Balance.
[it6jgxe] (score 3, diepte 2) Try Saucony. I have crazy high arches and slightly wide feet and find that the toe box is incredibly comfortable. 

I buy their hiking sneakers because the leather outer sole covers the pinky toe area which is exactly where I wear a hole in them.
[it78wwc] (score 3, diepte 2) I use a Pinnacle insert with my shoes, Merrill's included. That may be something to try. Have a couple pairs of inserts and rotate them through the shoes you wear, then your feet get the same feel no matter which shoes you have on.
[it63twv] (score 3, diepte 1) It's out - Just ordered my 3 today.
[it64hyq] (score 3, diepte 2) How does the 3 compare? (I bought a pair of the 2s at an outlet mall, so it'll be a couple years before I need another pair)>
[it6e0ks] (score 3, diepte 0) good shoes are totally worth the investment. I'm all about this. Cheap shoes are usually crap and a lot of expensive shoes are just overpriced crap. You gotta hone in on those good, trusted brands and watch out for deals.

I came to the revelation that spending more can be frugal if you're buying quality. I used to spend $100 bucks on these "nice" work shoes but I'd have to replace them. They looked good so I ponied up. I came to find out there was a world of shoes outside of Nordstrom that were actually built to last. One pair of quality shoes can outlast low quality ones by years if not decades.
[it7ef5u] (score 3, diepte 1 OP) Moab 2’s
[it5emc2] (score 2, diepte 4) Agree on oil. Full synthetic.
[it4ydzd] (score 2, diepte 0) Shoes/footwear is important but price is almost the last thing to base your decision on. I've chucked 40d generic shoes after almost the same amount of time as 100d name brands.

I've known people who spend about 150d for a set of season shoes they use for a few years. I've got a 1-2 years old pair of ~60d shoes I could still get by with for another season.

Most shoes like almost everything else are made sometimes on the same assembly line as 3+ different companies/price classes. So yeah take some time to find a decent set of footwear. Compare prices/selection. If possible do a trial period.
[it5zp99] (score 2, diepte 4) Thanks
[it9dqhs] (score 2, diepte 2) All you have to search on YouTube is “Rose Anvil” or heck “cutting shoes in half” works too, you’ll find the guy’s channel. He’s got a ton of videos on all sorts of types of shoes and brands.
[it7h65s] (score 2, diepte 5) Did you know Steve Buscemi manned the barricade during 
The People's Revolution of the Glorious Twenty-Fifth of May?
[it698br] (score 2, diepte 3) > But unless you can afford the og shoes, telling someone without the funds to "just buy better shoes" is not helpful at all. 

Buying 'better' shoes isn't necessarily hard at all.  It just takes a keen eye for good workmanship and a little luck with getting a good price which means more frequent shopping or keener shopping habits.

I used to think that clothes were insanely expensive, until I figured out the system that works for me, which happens to be "Old Navy" and understanding how that all works and the channels of distribution.

If you're buying on a deadline, then sure, your options are limited.

This isn't really different than anything else in life.  If you don't have a deadline and plan ahead, it's cheaper to get your plane ticket months ahead, then the day before.

It's more expensive to get a huge freaking bag of rice, with better price per serving, than it is to go to the dollar store and purchasing ready made Uncle Ben's in a minute single serving that is actually very damn expensive.

So while I understand

>There are so few options out there and saving 6mos means you're stuck with shit in the interim.

It's such a self defeating and fulfilling prophecy that incentivizes very short term purchasing strategies that continually cascades one poor decision into the next poor decision.

"Use It Up, Wear It Out, Make it Do, or Do Without".  It's ok to fix or repair things to Make it Do.  I have a pair of shoes that have 'gone to shit', couldn't find anything, so I fixed them, and a couple of years later, they're still in rotation, since I've mastered how to repair them.  If I don't have options I like, I make options that work for me.

There is a point to concede that sure, when shoes go bad, something has to be done.  One can't walk barefoot.  But that's like saying a car suddenly just 'goes bad'.  Part of the responsibility of owning things, if you want maximum life out of them, is to keep them in good repair, and part of the process is inspecting it for signs that need attention.  Oil needs to be checked, tire pressures need to be topped up.  You need to walk around to see that all the lights are operating properly.

If you make a pair of shoes, that normally only lasts 1 year, but you make it stretch out for 2, you now should have enough money to buy either the same shoe, or a shoe that's twice as expensive and make that one last 4 (or a 4x multiplier per dollar)

If things need to be replaced, not having the money for it, one can still literally and figuratively limp along gingerly untill the funds do come in.

And while I do understand that a car, or a pair of shoes can be a huge expense, making the car or pair of shoes the first step in being mindful about the process of taking care of stuff, understanding how to take care of it, and plan for future repairs or replacement, is way too late.  The first step should be things like repairing clothing, maybe a hang dry is better, or even hang dry first and finish off in the dryer.

Or instead of buying dollar store single servings of rice, taking a micrometric step up and buying a 1lb bag of rice.  Doing that a couple of times, then maybe moving up to 5lbs bags, then 10lbs bags, and creating a backup fund that eventually may end up being large enough to just buy a new pair of $150 shoes.

Don't buy the $1 18ml travel toothpaste.  Maybe head to the dollar store and get that 60ml tube for the same $1.  That's a 3x multiplier.

Maybe not go out to eat?  Go home and for the $4 for fries and gravy at costco, instead get 5lbs of potatoes, and make fries at home, and have enough fries for 4 meals later.  That's a 5x multiplier.

Don't get me wrong, I also still make bad purchasing decisions.  I bought a pair of khaki pants from Uniqlo.  The manufacturing was impeccable.  It's incredible the design and workmanship that goes into them.  But the fabric, relatively speaking, is crap.  And I say this a someone who always washes their clothes in garment bags to prevent wear and hang to dry.  I'm going to only get maybe 4 years out of them.  I'll repair them as needed, but I'll get 6 years max out of them, and they're starting to look thin and floppy, so they'll be my 'I don't care, they're clean and in good repair and the pockets are still good' (my pants usually go thin above the knee.  If they were only crotch blow outs, I'd repair them to kingdom come.)  All is not lost.  I got them on sale for $10.

But a bad purchase should sting enough that it informs a better purchase so the frequency and duration of being stuck with shit in the interm, should become smaller and smaller.

At a certain point, one gains a knowledge, where things don't happen by accident.  They're planned for.  At this point, I can't ever see the need for a new car.  I can repair mine over and over again and get 1 years use from 1 months worth of car payments.
[it5z7jn] (score 2, diepte 1) I find that the arch doesn't hit my arch correctly. I was really looking forward to buying a pair because I have ridiculously high arches and was so disappointed
[it82chs] (score 2, diepte 1) They certainly look like Merrell. The new V3's are the best yet.
[it837ww] (score 2, diepte 1) that is the exact sole I see on the merrells I am wearing right now.
[it74bwa] (score 2, diepte 0) Looks like merrels. You made a great purchase. Mine lasted a solid 3 years of daily wear before they get relocated to hiking and yard work. Where they last another two or 3.
[it4x9op] (score 1, diepte 0) Hey RelayFX, thank you for your image contribution! We like to have discussions here on r/frugal. To avoid your post being removed; 

**If you're posting something you made, repaired or refurbished**, please leave a top-level comment under your post explaining how or why you went about it, how much it cost, how much time it took, etc., and share the recipe or materials needed. 

**If you're posting a general image**, please leave a comment explaining how it relates to frugality and any other details you'd like to share! Thank you for participating in r/frugal!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/Frugal) if you have any questions or concerns.*
[it61dty] (score 1, diepte 7) Haven’t really looked into it. It might!
(28 reacties met lagere score weggelaten)

=== THREAD 1rvw7cm ===
SUBREDDIT: r/AmazonFC
DATUM: 2026-03-17  SCORE: 43  REACTIES: 92
TITEL: This job is turning my feet into sloppy joes
POST (source_id=post):
My feet feel like I've been transported back to barefoot cotton picking slavery. These cheap ass shoes they let us order are not cutting it .. even with that basic ass insole. I have mad blisters on my shit. I'm soaking them daily but I also had to take a LOA to recover. Also booked an appointment for a podiatrist. Is anyone else in a similar situation?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oavhyn2] (score 47, diepte 0) for maybe the first couple months my feet hurt so bad I’d cry about it lol I’d soak and massage them daily too. Then one day they just… adapted. Never hurt that bad again. Took a solid 6 weeks but now I’m chillin with basic dr scholls heel comfort insoles.
[oavkhlb] (score 23, diepte 0) I had to finally bite the bullet and just order a pair of shoes online out of my own wallet. Best $45 I’ve ever spent
[oavkk5u] (score 19, diepte 1) Same, I remember people telling me I’d get used to it and I never believed them because of how badly my feet hurt lol and then they just stopped hurting
[oavvlks] (score 14, diepte 3) Have you ever tried this one.. (working at a warehouse)
[oavjbsp] (score 12, diepte 0) Since they give you a $110 credit, and a 15-20% discount on any shoe listed, don't cheap on the shoes you get.  I get Caterpillar Boots.  I get the free Protalus insole with the shoe, and I stack the factory insole on top of it. I also have my old pairs of boots that I cycle through so my boots have a chance to dry out.   

Main thing is, choose Work Boots from a Work Boot Brand, not Safety Shoes from an Athletic footware, or hiking shoe brand.
[oavm13f] (score 12, diepte 0) Saying barefoot cotton picking slavery is extremely disrespectful
[oawq09g] (score 9, diepte 1) Ehhh? 4 1/2 years at Amazon and my feet have never quite adjusted. I must be doing something wrong 😭
[oavnely] (score 8, diepte 2) Damn Sabrina you working at Amazon now?
[oavtulx] (score 8, diepte 0) Before anything else, make sure you're stretching properly and regularly. Always and forever. 

I've had bad foot issues due to fledgling arches and awkward pronation. The podiatrist visit is definitely a good idea; they'll undoubtedly try to reccomend custom insoles, which I personally use and support 110%. Crappy shoes may still have some stability and durability issues, but new insoles can at least get you on the right path. Also consider using similar OTC insoles in your casual shoes (I opt to use Spenco brand high support I soles and also have a pair of their arch supported sandals and slippers).

Socks are also going to play a role. Cheap socks do you no favors... you want some simple wool blends for better wicking, cushioning and durability. I use to plow through  big multi packs of Under Armour that were primarily synthetic material. Their cushioning just wouldn't hold up and would get pulverized in months. Nowadays I use Duluth blend coolerinos; they pretty expensive outside of regular sales, but they hold up *good*. My Duluth pairs cost multiple times those cheap UA socks, but they've also lasted several times as long. Helps cut down stickiness, too. 

If you don't have stomach issues, ibuprofen from the fastenal machines is your best bet for swelling/pain. Take acetaminophen in conjunction for more moderate pain. If it's really, really rough times, maybe consider a brief period of responsibly using hemp products or kratom or 7OH extra to not suffer too much. If you have the money margins to spare, I also highly reccomend a personal massage gun.

So basically, speaking from 8 years Amazon experience and a special handling site that required early adoption of safety shoes, here's my setup:

- third party shoes with custom podiatrist insoles
- wool blend socks for the padding, durability, and additional sweat control 
- 2x pairs of socks per shift in order to change during shift if my initial pair get too sweaty (I also change into some tennis shoes *immediately* when I get out to my car after shift)
- use a small ice pack and whatever otc anti-inflammatory of your choice like ibuprofen or acetaminophen to help reduce ankle pain after shift
- stretch with gusto
[oavs1fx] (score 5, diepte 1) This. I always rebuy the Just-Soso shoes
[oavp6pi] (score 5, diepte 0) You gotta say fuck Zappos and get a real pair of good shoes. Those Zappos shoes, all of them, are trash designed to fall apart. I never found a pair that felt even slightly comfortable. 

I’m wearing Puma composite toe work shoes, I have forgotten my feet exist for the last year. Part of it is the mental battle of course, but real work shoes are the best investment you will ever make.
[oavrygr] (score 5, diepte 1) Zappos sells Puma composite tied shoes you dolt
[oavs9pz] (score 5, diepte 2) “Not everyone…” when did I say that? I was giving advice to this specific person. How about you go back to school and learn how to read.
[oaxk6wq] (score 4, diepte 2) Same tenure and my feet feel like they are in vice grips by last break.
[oavntzp] (score 4, diepte 0) Definitely buy a larger size and ALWAYS a wide. Unless you have the narrowest feet in existence. I'm not a wide but I buy them in the safety shoes and you need to let your feet and toes spread out otherwise you'll cramp up in your arches and that's literally the worst pain I've ever felt
[oayq0bh] (score 3, diepte 2) Same I’ve been at Amazon for 3 years and by my 3rd shift my feet just go numb lol
[oax5tp4] (score 3, diepte 1) Dam, big ol work boots for up to 12 hours a day, idk about that
[oavk9le] (score 3, diepte 0) With the blisters make sure your shoes aren’t too tight or too loose. The common advice here is to size up to avoid the comp toe cover hurting your toes, which is good advice. But if you size up, you may need to wear thicker socks to compensate. Also you can get some pretty good insoles on Amazon for about $20. I like the walkhero heavy duty but anything with a more rigid heel support would probably work better than most basic insoles. Good idea to see a podiatrist to rule out any issues!
[oavned2] (score 3, diepte 0) Try the prolatus insoles. The ones we are allowed to order for free on Zappos.They are hard, but that's what your feet might need to feel supported. The cushy foam ones just made my feet hurt worse.
[oavsdcc] (score 3, diepte 2) Well I’ll be damned. I never see people rocking brand name safety shoes. They don’t have mine specifically but the ones they have don’t look too bad. Would never get low tops after knowing the shit my ankles have been through here.
[oavvrp4] (score 3, diepte 0) Xtra wide shoes make all the difference when you order your safety shoes from Zappos
[oaw7xul] (score 3, diepte 0) Also...dont wear the same shoes every day. Rotate them out. I have a couple pairs that  I switch between, and they really do need a day or do to recover from being flattened out.
[oawbmjo] (score 3, diepte 0) The shoes are excellent. The insoles work wonders. Lots of folks who do no physical activity or eat shitty, don't drink water or tie their shoes to tight etc etc tend to complain a lot.
[oaxanio] (score 3, diepte 0) Comparing Amazon to slavery is wild
[oavtpag] (score 2, diepte 1) At the state fair like 2 years ago I went to a stall with a guy who was selling insoles he invented. He said he was a physical therapist, he listened to me describe my foot pain, he examined my foot and said it seems like I had plantar fasciitis.

I bought some insoles from him, they hurt like hell for a few days, but my foot pain has been SO much better ever since then. I used to leave work due to foot pain, but I haven't had to since then. I never take them out of my work shoes. I have ridge shaped callouses on my feet.

They're weird, and they probably won't help everyone, but it was a massive game changer for me.

https://www.theridgewalk.com/
[oavj3lw] (score 2, diepte 0) I only discovered that I had the beginnings of Taylor's bunions after a few days in safety shoes. I ended up quitting because I was told it wasn't possible to get an accommodation for it and still work in the warehouse
[oavnk26] (score 2, diepte 1) That sounds like bullshit... Welllll you can't say it was a pre existing issue
[oaxopwy] (score 2, diepte 2) Stacking insoles is a horrible idea too. But you do you.
[oavvexi] (score 2, diepte 2) Furuian Steel Toe Sneakers is what they’re listed as on Amazon. I swear everyone in my warehouse has them. Super lightweight and comfortable
[oax1dva] (score 2, diepte 3) They're not too heavy being steel toe vs composite ?
[oaydqu2] (score 2, diepte 4) No not at all
[oaxth7q] (score 2, diepte 2) are those comfortable? i always see those around. do u order 1/2 a size or a size larger?
[oaxun5b] (score 2, diepte 3) The sole is super comfy but you'll probably have to replace them every 4-6 months. I have very wide feet so I had to go a full size up. All of the shoes I tried from Zappos were too narrow for me. Check the reviews on Amazon for sizing. 

Some sites specifically ban these shoes but if you see them around, you're good. Also. These shoes are usually about $10 cheaper during Prime sales.
[oaxv5pa] (score 2, diepte 4) i see them everywhere at my site & always thought they looked really good compared to other shoes. i have the timbs but was looking for sneakers for the spring! def will give them a try! thanks 😊
[oavrn8o] (score 2, diepte 1) Not everyone needs a wide. That’s crap advice.
[oavomf7] (score 2, diepte 0) Use that foot spray that numbs your feet. But i would only use it for when its HURTING like to even just stand there. Otherwise youll grow immune to the spray but i use the spray 2 times for 2 days(before clocking in, and after second period)  and tough it out for the 2 days of my work week also if you got athletes foot tea tree oil is good too, Diluted though, if you use straight tea tree oil its gonna burn if you got open cuts im a big girl and work the xl warehouse so all i do it walk on concrete floors and lift heavy crap and push carts shit so ive done just about everything, but that foot spray is my savior...and weed after a shift 🥲
[oawap21] (score 2, diepte 0) make sure you have good socks.  i would put vaseline on my toes and feet and put my socks on.  make sure you wash them separate from your other clothes or it will mark your shirts.  my feet were split open and i had tons of blisters until i started doing this.
[oax7cxp] (score 2, diepte 1) Not the best advice. My site audits for safety shoes every day.
[oay0a91] (score 2, diepte 1 OP) I think part of my trouble with this began when I tried some extra wide shoes. My feet were sliding around in them and that's how I got the first blisters. Now those blisters have gotten worse even with me changing shoes.
[oavgtns] (score 1, diepte 0) Welcome to AmazonFC, please be sure to read our submission guidelines and remain respectful of your fellow users. If this post isn't up to par with our submission guidelines, please make use of the report feature. Once it crosses a certain threshold the post will automatically be removed for moderator review. See [Amazon Resources Mega thread](https://www.reddit.com/r/AmazonFC/comments/umjgzv/amazon_resources_megathread/) here. We have a [Discord](https://discord.com/invite/t7jARCs) for those wanting to socialize on a different level with the community. Please enjoy your stay!


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmazonFC) if you have any questions or concerns.*
[oavhwrv] (score 1, diepte 0) My feet have been killing me as well. I’ve been with Amazon 12 years and never had an issue until they made safety shoes mandatory. So I feel it’s definitely the safety shoes.. I don’t have blisters but my feet are so sore on the soles of my feet and the top where my foot bends around the composite shell when I walk. I have made an appt with my regular Dr for a few other reasons but will be mentioning this to them.
[obctdgq] (score 1, diepte 2) Try different shoes ! Feet are kinda important
[oavrksi] (score 1, diepte 1) There’s nothing wrong with the safety shoes. Most people don’t want to wear heavy work boots and don’t need them either. Get a good fit, wear good socks, and get the right kind of insoles for your specific feet.
[ob0d2x4] (score 1, diepte 2) I've had my feet saved twice by steel toe or composite toe workboots at this point, so wearing good quality boots is a no brainer for me.
[oavkfx8] (score 1, diepte 0) I developed a terrible case of plantar fasciitis, I ended up buying a pair of redwings and they have helped so much . While my feet still hurt after 10 hrs ,but nothing like they did wearing those zappos shoes.
[oavmrd3] (score 1, diepte 1) Big same
[oavn0p1] (score 1, diepte 1) What did you buy ?
[oavnjou] (score 1, diepte 0) Gotta massage the knots out fam
[oavnpkn] (score 1, diepte 0) Size up the shoe and double the socks.
I  wear compression socks then put on regular socks on top of it. You can buy compression socks in zappos too and apply the Amazon benefit.
[oavpc67] (score 1, diepte 0) Simple fix: extra-wide shoes and the correct insole for your foot type.
[oaxqto0] (score 1, diepte 2) Try again 😂
[oavsbpp] (score 1, diepte 0) Bring fluffy socks and change socks at break time. When I was on the ship dock, that was the only way I could avoid the blisters.
[oavufbp] (score 1, diepte 0) If it reaches that point of going to Loa then report to wellness about a workplace injury
[ob17fef] (score 1, diepte 1) Legit question, what would you say?  Like Op, I'm having issues and thinking of taking an LOA.  I didn't think about reporting it to AmCare as an injury though.
[ob1aetm] (score 1, diepte 2) if it happened at work or because of work then it is work related and you need to report it to AmCare as you may be entitled to workers compensatin
[oax56ih] (score 1, diepte 1) I always go extra wide and at least a half size up to give extra room for comfort
[oavxan5] (score 1, diepte 0) Same same
[oawvd6k] (score 1, diepte 0) Do this. 

1. Do not pick your fresh blisters. Instead take a needle (I’ve even used a steak knife 🤣 no judgements) and stab into the bottom of the blister, right along the bottom of your foot and let it drain. DO NOT PULL THE BLISTER OFF. Just poke a hole big enough to drain. 

2. Once the blister has drained get some toilet paper or a cotton swab and put that over your blister. Do not use too big of a piece because you need the sports tape to stick to as much of your skin as possible. But you need that cotton or TP to absorb any liquid still in your blister. 

3. Get the white sports tape you get in the bandaid section and tape the cotton or TP to your foot. Tape it good! This will lead to zero friction and that blister will not only heal but prevent more from forming.

I sometimes will tape those spots on my feet where I know blisters will form even if there is no blister. I always have a roll of that tape with me. It’s helped many i work with as well. IMO sports tape works way better than bandaids or bandaids specifically made for blisters. Just make sure you use enough tape to where it will not be moved by your shoe. Like I would use inches of it and not only wrap it over my foot but also under so I knew that tape wasn’t gonna move.

Sorry this is long but I do hope it helps someone!!
[oax01wy] (score 1, diepte 1) Jesus Christ
[oaxi45n] (score 1, diepte 1 OP) Lol if I use TP it definitely won't be the Amazon provided stuff. That shit will have you raw asf after a few wipes
[oaxhf6z] (score 1, diepte 1 OP) I've been sent home one time before for wearing my Nikes in there. Mkt trying to get fired for something so preventable
[oax2uxt] (score 1, diepte 0) Bruh it’s gotta be your shoes. Try the new balance ones that everybody gets. Forgot what they’re called lmao. But it feels like ur walking on clouds
[p8hrlu0] (score 1, diepte 1) Which ones
[oax4rqv] (score 1, diepte 0) Nah yo I wear the Zappos on my days off lol my feet are strong
[oaxh45f] (score 1, diepte 1 OP) Haha I notice the nickname you picked
[oax63a8] (score 1, diepte 0) I ordered a lot of stuff that helps me
- compression socks
-compression sleeves
-Heel cups
-really good insoles

It helps me a lot. I still feel horrible around the last two hours but I could not imagine trying to work without any of the above. (My podiatrist told me that I have heel spurs- he said as long as I'm comfortable what I'm wearing isn't overkill). 

Seeing a podiatrist is a great idea, ever since I did I've been trying to follow his advice and I have a lot less foot pain overall. Even though I walk about 13K steps per shift. 

I also recommend some resistance bands to help do some stretches and I also got these ice packs you can wrap around your feet after your shifts. They are heavenly for those really rough days.
[oaxfzji] (score 1, diepte 0) Shoes for Crews are comfy af and food service people miles on them too. Maybe ?
[oaxhkfq] (score 1, diepte 0) Best shoe to get are the hey dudes men’s wide. If your toes feel squeezed get a bigger size. You should not feel the toe caps. Next take insole out and get dr. Soles gel work. I had to pay for them myself but will worth it.
[oaxi94a] (score 1, diepte 1) https://preview.redd.it/0z4g6kr81mpg1.jpeg?width=1125&format=pjpg&auto=webp&s=3ed1b733ea2a74056b0cbc222c74d844fbe9caa5

There are the best
[oaxj4js] (score 1, diepte 0) Just go to the Red Wing shoe store and buy some actual shoes that are worth a damn those apple spoons are all crap I’ve been through about 12 different pairs and none of them have even come close to fitting. Got a pair of redwing boots and I’ve been pain-free my entire career Zeppo is shit.
[oazaxjn] (score 1, diepte 1 OP) I'm talking about my feet not yours genius
[oazgnqq] (score 1, diepte 2) Oh no we got fancy feet McGee over here
[oaymebb] (score 1, diepte 0) Pls post a pic
[oazafm7] (score 1, diepte 1 OP) Lol no weirdo
[oaytk88] (score 1, diepte 0) Vaseline on them soles after work + overnight helped immensely. Wear worn socks over them to prevent  mess.
[oaz610m] (score 1, diepte 0) those shoes they give you are actually very good, some of the most comfortable soles i’ve worn. Just make sure u change them every 6 months or so. But yea, your feel will always be hurting from standing on concrete all day
[oazz9vp] (score 1, diepte 0) Get some mole skin for your current blisters. You will need to find some decent shoes, may need to go out of pocket to fond them.
Folks have had good luck with Red Wings, I always had better luck with Wolverine. My current pair are made by Brunt; I ordered them directly from Brunt and haven't had any issues since.

I went through 4 pair of shoes/ boots in the first year, saw a podiatrist and an ortho doc. I kept being told insoles (I went through 5 or 6 different types) and shoes.
Good luck
[ob01bm9] (score 1, diepte 1 OP) I'm gonna try the moleskine and I just ordered some shoes I've owned before off Amazon that I wore tf out of last year but I never had these issues with them. It feels like pirahnas are biting at my feet every time I walk.
[ob0mptt] (score 1, diepte 0) No seriously, my feet and ankles are so swollen and throbbing when I get off work, I have flat feet and that’s also a big reason why
[ob12wrh] (score 1, diepte 1 OP) I would get that checked out
(13 reacties met lagere score weggelaten)

