# Label-batch batch_0084

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
Schrijf het resultaat naar `batch_0084.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1scm7tj, 1kt7yf7, uz9nvj).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1scm7tj ===
SUBREDDIT: r/BuyItForLife
DATUM: 2026-04-04  SCORE: 129  REACTIES: 83
TITEL: Finally bought Clark's Desert Boots and my feet are paying for it
POST (source_id=post):
Been seeing these recommended everywhere for years. The perfect casual boot that goes with everything. Found a pair on sale and grabbed them in beeswax leather. Put them on and walked around my apartment thinking these are fine, people exaggerate about the break in. Then I wore them to work for a full day and by 3pm I was limping. The soles have zero cushioning. It's like walking on a leather wrapped brick. My heels hurt for two days.

I've been wearing them around the house with thick socks and they're slowly getting better. The leather is softening up. I can see why people love them once they're broken in. They look great with jeans and chinos. Simple and classic. But man that first week was rough.

The sizing was weird too. I sized down a full size from my sneaker size and they're still a little loose in the heel. Tried heel grips but they made it worse. Now I just tie them tighter and deal with it.

For those who've had these, how long did break in actually take for you? And does the sole ever get more comfortable or do you just get used to the pain?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[oebzhy5] (score 111, diepte 0) I don't think they're very comfortable shoes. I had a pair when I was a teenager.. like a decade ago
[oebz3fr] (score 73, diepte 0) That’s a whole lot of work just to wear a pair of boots. I wear Wolverine 1000 mile boots and they were comfortable out of the box 🤷‍♂️
[oec1lye] (score 45, diepte 0) Clark's are known to use a slightly different sizing to most manufacturers, plus they have lots of half-sizes that most other brands don't offer.

https://www.clarks.com/en-de/fit-guide
[oecgstu] (score 45, diepte 0) I’m pretty sure Clark’s Desert Boots stopped being BIFL a decade ago…
[oec31ly] (score 44, diepte 2) Bears, beets, Battlestar Galactica.
[oebzovh] (score 29, diepte 0) I've had both actual Desert Boots with the crepe rubber sole and Bushacre 2. Never had any issue with either, so not sure what to tell you.

Is it possibly because you're off on sizing?
[oebzd8u] (score 19, diepte 1) Fashion first
[oebzwax] (score 17, diepte 1) facts wolverines are way better
[oec0izg] (score 16, diepte 0) Desert boots were great a long long time ago, when they were made in UK. I bought a pair 3 years ago, put them on and immediately was shocked and disappointed at the quality and the way they felt.  Pain, too narrow. Took them back the next day.  Crap.
[oecbout] (score 15, diepte 4) I think this is a reference to The Office (U.S. version)
[oedhr2o] (score 14, diepte 1) If you are interested in Clarks, you are probably not cross shopping with Wolverines. Different tools.
[oec5fod] (score 14, diepte 0) Had those in college, couldn’t imagine my feet going through that now. 

Look into the Patton boot from Allen Edmonds. Similar style but way way more comfortable
[oebzt3e] (score 12, diepte 0) Throw some Dr. Scholl's inserts in those bad boys.
[oeejzxe] (score 11, diepte 1) Even a decade ago they weren't. I dont think theyve ever been resoleable.
[oec9k0t] (score 9, diepte 3) i don't know what this means, but I like these three things
[oeceana] (score 8, diepte 2) Bot account, block and ignore.
[oecoz6v] (score 8, diepte 1) That is so interesting! I bought a pair, gotta be forty years ago, and I thought the sizing was so off and I haven't bought them since. I never forgot and have wondered about the fit. There's another well known brand, can't think of the name now, but their shoes were always too narrow for my standard size six foot.
[oecbdz5] (score 7, diepte 0) Try tying with a heel lock: https://www.outdoors.org/resources/amc-outdoors/outdoor-resources/know-this-hiking-boot-lacing-technique-the-heel-lock/
[oedtw62] (score 7, diepte 1) Clark's as a whole hasn't been good for closer to 20 years.
[oec5gto] (score 6, diepte 0) I had a pair a decade ago and they were so cute, but never felt good. The rubber sole is nice, but there is no arch support, and the heels slipped on me. Not one I recommend.
[oec10kc] (score 5, diepte 1) Those things even made my kids feet hurt and they can withstand anything
[oeeokkr] (score 5, diepte 2) Probably Salomon.  Salomon runs narrow.  I love them as I have skis for feet.  But I hate that 9/10 of their shoes have pull-cord “speed laces” instead of tie/em-up laces.
[oeedrv0] (score 4, diepte 1) Likewise. I love my Desert Boots. No problems at all.
[oecujg0] (score 4, diepte 1) Yeah they’re a great boot when you’re in your twenties and your body “just works” lol
[oecei6b] (score 4, diepte 0) I bought pair of Nike Air Zoom Wild Horse 4 shoes. The soles were surprisingly harsh for a running shoe and for Nike in general because they are normally super comfy. I bought some Bauerfeind viscoheel insoles for a different issue. Threw those in and wow, what a difference. If not for those insoles the shoes would not be wearable. I have been wearing this setup for couple months now and the shoe is loosening up but the insoles make it work.
[oec9zzc] (score 3, diepte 1) Same with my RM Williams Comfort Craftsmen Chelseas and Rigger Boots. Both with amazing to wear straight out of the box.
[oekmiyh] (score 3, diepte 2) Pretty sure the Wolverine 1k mile boots have a lot of cross over with Clark deserts boot owners.
[oec4im4] (score 3, diepte 0) Even upstream for years. If sized right they take a few weeks.
[oec93hb] (score 3, diepte 0) Have had a pair for years in the suede, they’re great, but I have always worn them with insoles I got at REI.
[oecc1ii] (score 3, diepte 0) Why don't you just replace the insole? I never use the stock insoles in any of my shoes that I wear regularly.
[oechniw] (score 3, diepte 1) They didn't design them to have adequate toe room for an insole swap in my experience. I had bad luck using full length and even 3/4 length.
[oecicz6] (score 3, diepte 2) You have to remove the existing insoles. They are glued in but you can still tear them out.
[oecoa3t] (score 3, diepte 0) Drill sergeant said “put your boots on and turn the shower on”.  I still break in boots that way.
[oecp2ks] (score 3, diepte 0) The crepe sole on Desert Boots is a deliberate design choice from the 1950s - natural rubber that molds to your foot but offers zero arch support. Break-in is usually 2-3 weeks of daily wear. The heel slip issue is normal and resolves as the suede colar conforms. If comfort is the priority swap in a thin leather insole.
[oefvatt] (score 2, diepte 2) RM Williams quality dropped off of a cliff and plunged into the depths of hell a few years ago since they were bought out. Definitely not BIFL quality anymore, even if you're just a concrete cowboy using them for normal wear.
[oedrn8u] (score 2, diepte 2) Don't use the orthotics or hard plastic arch, then.
[oecpt82] (score 2, diepte 2) Bad bot account. Ignore.
[oeiu394] (score 2, diepte 3) Hah, I have the same problem but I absolutely love the speed laces!
[oecvvuw] (score 2, diepte 1) Allen Edmonds Chandler looks much closer
[oecb1f8] (score 2, diepte 0) Try the Veldskoen South African chukka.  Very comfortable and better made.
[oecif5o] (score 2, diepte 3) I did. Still failed.
[oecizcs] (score 2, diepte 4) Ah, bummer. You might try some thin insoles [like these](https://treadlabs.com/products/ramble-thin-insoles?variant=29497375260695) which are designed for this kind of problem, but they still might not work well for you. Recommend doing the paper test to make sure you get the right arch height for your foot.
[oecjqfe] (score 2, diepte 5) I tried several things and then donated them.
[oech9j2] (score 2, diepte 0) I was optimistic but those didn't go well for me at all. 

Severe lack of insole. 

Added SuperFeet Green. 

Inside became too short and began scraping skin off my toe tops. Even with good socks. Thick socks also didn't help and didn't fit. 

Tried SuperFeet 3/4 length. A bit more toe space but still no dice. 

Couldn't tighten them anywhere near well enough to stay on my narrow feet because they're an extremely loose style that barely holds on. 

Gave up and donated them. 

I also ordered a pair of custom White's I spent forever measuring for but even after tons of break in they are also too short and the vamp scrapes skin off the mid top of my foot. 

I went to the Danner factory the other day and got a pair of Bull Runs. Still working on the breakin. But they fit quite well using the same SuperFeet 3/4 length I had gotten to try and salvage the Clarks.
[oecoxns] (score 2, diepte 0) I tried Clark's, and they didn't fit my high instep. Replaced with Jim Green Vellies, and love those. Did take a minute to break in, but after that it was all good.
[oeilglh] (score 2, diepte 1) Soooo much better than Clark’s and so much more comfortable!
[oect2iw] (score 2, diepte 0) If you regularly wear a shoe with a lot of support foot pain is common if you switch to a shoe that does not have a lot of support. The foot gets weak. This is a common problem when people move to a minimal barefoot style shoe. It goes away as your foot gets stronger.
[oenolcm] (score 1, diepte 3) In what way, beyond them both being boots? There is a certain simplicity with the Clarks that is not in most of the 1000 mile line, perhaps with the Legacy Cort, but even then, the look and style is not similar. The others are not close. The Clark chukka is a much more relaxed and laid-back style than the Wolverine offerings. I personally wouldn't shop the Wolverine unless I wanted something distinctly more boot-like. I consider the Clarks more of a lifestyle/casual footwear than the Wolverines.

That said, I do really like the look of the Legacy Cort, so I am glad for having read the comment about the 1000 Mile line.
[oerbb2d] (score 1, diepte 4) They’re fashion/casual/life style boots. The type of person that’s interesting in a desert boot would probably also be interested in other types of casual/life style boots. The r/boots subreddit is testament to that. 

The 1k boots are definitely more boot like but they’re not dress boots by any means. In the same category as iron rangers, blacksmiths, and heritage Mocs. Wolverine also made a 1k chukka a few years back. There’s still NIB models for sale on eBay. Definitely more upscale than Clark’s desert. 

Point is Clark’s boots tend to be a pathway to the greater boot world. At least from what I’ve encountered in my time in the boot subs.

The Legacy Cort looks pretty good for the price. But alas, no wide options so I don’t even bother with Wolverine 1k boots.
[oeco82y] (score 1, diepte 1) reminds me of breaking in my red wings, painful start
[oejdlq4] (score 1, diepte 1) Why do they hate size 11?   Big gap there.
[ofw3vsh] (score 1, diepte 1) This fit-guide does not fit me. I have a 41, but my Clarks are 40. And the heel is always very loose, but it's supposed to be, I guess.
[oegg5b4] (score 1, diepte 1) Also from South Africa, the Jim Green Vellies. 

I think they may be a bit more rugged looking than the Clarks, but the Jim Green boots & shoes I’ve had have had easy break-ins. I don’t own the Vellies, but have the Shoellie, which is similar to the Vellie but cut more like a shoe.
[oecej71] (score 1, diepte 0) Texarado boots seem to be it.
[oecff0w] (score 1, diepte 0) Apply some of this, it makes a world of difference in softening the leather: https://www.obenaufs.com/natural-preserving-oils-p/leather-oil.htm?srsltid=AfmBOoqquBS8TStcuzdsfGHK0uN8Z93IsokcOOBSMvGqDwuQpluZFt1O
[oqs82m9] (score 1, diepte 2) They always have been, and there are plenty of examples online.
[oejrs23] (score 1, diepte 1) I wear them almost every day and have bought a new pair every 3 years for the last 12 years. So all to say, you are correct they are not BIFL
[oet5f7p] (score 1, diepte 1) But this sub isn't bifl. It's bifty (buy it for ten years). Half the recommendations on here are randomly low quality stuff people have just had around for a while and the other half is just a tier above that. 

I almost never see bifl products on this sub. Clarks are significantly higher quality than almost any $120 sneaker you can buy today, but they aren't like buying a pair of heritage red wings or whites.
[oecilmt] (score 1, diepte 0) I find the bushacre rubber sole to be a bit more hard on the foot than the crepe sole. The crepe sole doesn't last as long but I find them more comfy out the box.
[oed8cn2] (score 1, diepte 0) If I don't tie them very tight, they rattle around and cause pain. But if I tie them up snug (not cinched down) then they are pretty nice for casual shoes.
[oedb76m] (score 1, diepte 0) I add padded insoles and they fit much better if you add an additional grommet for your laces near the top. (2 vs 3 pairs of holes)

So yeah not great out of the box
[oedhjz5] (score 1, diepte 0) Clarks are great, but not BIFL. I probably got 4 years of daily wear from mine. The crepe sole is soft, and will wear out eventually, and they are not resolable. They are a solid, simple shoe.

You are correct about the cushioning. Your feet get used to it at some point. Kinda like wearing wraparound flip flops.
[oednpa4] (score 1, diepte 0) I have 4 pairs of these including the beeswax ones.  Those ones are so brutal on your feet but the other ones are soft and very comfortable.  I hated the beeswax ones because they were so stiff and uncomfortable.
[oedoty8] (score 1, diepte 0) I have one pair I've had for twelve years.   The same beewax you bought.  The leather looks worn, but they are solid and comfortable. 


I have a new pair I bought about 6 years ago, and again, perfectly comfortable for me. 


I've worn these walking all over NYC for work and more and I've never had problems with them.
[oee5429] (score 1, diepte 0) Yeah those suck. My mom always wore them when I was growing up in the 80s/90s- she liked the light suede ones. I bought a dark brown leather pair 15 years ago and my feet always paid when I wore them. They never wore in and I eventually donated them. They were just useless as shoes on me.
[oeecc9o] (score 1, diepte 0) The crepe sole on Desert Boots never really gets cushioned but it does conform to your foot shape after about two weeks. The real trick is sizing. Go a full size down from your sneaker size and half down from your dress shoe. The beeswax leather molds beautifully once broken in.
[oeeeper] (score 1, diepte 0) Those beeswax ones hurt to even put on, I immediately rejected them. Know idea how any make it out of the shop.

Clarks are in no way BiFL, but they are cool as heck. I've got some outrageous Wallabees and will eventually get some 'Treks but they are very much fashion (albeit classic) rather than something I expect to outlast me.
[oeefxzc] (score 1, diepte 0) That sounds like what happens when I break in new snowboard boots
[oeehxro] (score 1, diepte 0) Not just uncomfortable, they’re freezing.
[oeeog49] (score 1, diepte 0) If you’re in the UK, Russell & Bromley are having a closing down sale
[oeepqcd] (score 1, diepte 0) I have been so attracted to Clarks Chukka Boots and keep asking the salesman at a local shoe store to try them on.  I have trusted him for many years and his reaction to my request is always the same; a grimace on his face and a very slow movement of his head no-no.  Now I understand why.  Thanks for your input.
[oeeqcyh] (score 1, diepte 0) My most comfortable pair of dress shoes are old Clarks, but a different model.  Not chukkas.  Never chukkas.

Meanwhile, my Clarks were three times as old as my Hush Puppies that dry rotted right off my feet on the dance floor at my cousin’s wedding last summer.  And my old Clarks are *still* kicking.  They were really made to last.

All chukkas are unwearable, though, at least for me, at least until I’m confined to a wheelchair.  They’re great for modeling on mannequins.
[oeeutkr] (score 1, diepte 0) I bought a pair of crepe soled classic Clarks desert boots 15 years ago by trying them on and picking a pair that fit and then wearing them. I honestly never experienced a break in period and consider them to be pretty comfortable versatile shoes. They haven’t been in the rotation a ton just because… they were so ubiquitous for a minute and maybe still look like a “dressed by the internet 10 years ago” shoe? But I still have that pair and an other pair I bought shortly after in my closet, there been good shoes.
[oeexvdc] (score 1, diepte 0) About heel slippage: get [tongue pads](https://ralynshoecare.com/product/ralyn-tongue-pads/); in my opinion heel grips are useless, or worse.
[oef72b3] (score 1, diepte 0) Barefoot shoes have changed my life. You shouldn’t have to be in pain. You should read about how good they are for you. There’s tons of high quality brands that last for years.
[oefhqxi] (score 1, diepte 0) I don’t think it’s the lack of cushioning as much as it’s the elevated heel. Even though many modern shoes have it, elevated heels collapse your arches and negatively impact the way your knees hips and back stack on top of it. I think some people are more affected than others, once I switched to shoes with zero drop it basically fixed my body.
[oeftmyj] (score 1, diepte 0) This is the sole reason I always take a size larger than my normal wear
[oefz9mt] (score 1, diepte 0) I've had a couple of pairs, and IMO, there is no 'break-in.'  They are just extremely uncomfortable boots.
[oegc1y6] (score 1, diepte 0) FWIW, I’ve been really disappointed with Clarks. I have a pair of Allen Edmonds and they blow the Clark’s out of the water. They’re pricier, but I’m not sure if it’s worth even buying the Clark’s for me at this point since the difference in quality is so vast.
[oeilaho] (score 1, diepte 0) I had two pairs and I honestly never thought they were comfortable. The fact that they don’t have a shank becomes apparent when you are on your feet for an extended time. Strongly suggest you take a look at Jim Green Vellies. They are a type of desert boots as well, and just feel more substantial. They also have high quality leather options (rough out will last a long time). So much more comfortable and can be re-soled. (Check out their African Rangers, too - love mine)
(16 reacties met lagere score weggelaten)

=== THREAD 1kt7yf7 ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-05-23  SCORE: 36  REACTIES: 83
TITEL: Best sandals for walking men – What do you recommend for long walks?
POST (source_id=post):
Looking for sandals that can handle long walks comfortably without causing pain or blisters. Are
there any that offer real arch support, good grip, and won’t break apart in a season? Materials
and durability are key here—what are the best walking sandals you’ve tried?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mtrkodg] (score 44, diepte 0) Bedrock sandals
[mtrjsep] (score 37, diepte 0) Tiva and chaco are both brands of "hiking" sandal. They used to be pretty high quality, but I'm not sure if they are still any good.
[mtrldje] (score 18, diepte 0) Teva sandals. I have the hurricane xlt and spend hours hiking in them in the summer. 
I also have a pair of closed toe keens which are good to protect your toes. 


Birkenstocks are fine for short walks but they wear down fast and aren’t good in the elements.
[mtrkrt5] (score 14, diepte 0) I put a lot of miles in Keen Uneeks with no problems.
[mtrjl33] (score 13, diepte 0) I was really hoping my leather Birkenstocks would do the trick, but it turns out I'm in the small segment of the population that experiences nerve damage leading to toe numbness from the little ridges on the Birkenstock foot pad. Bummer! Took me a year to regain full feeling in my big toe after wearing them for a while without realizing what was going on.
[mtrkkhl] (score 11, diepte 1) I like chacos, but they are probably not as good as they used to be
[mtrkszc] (score 10, diepte 0) Chacos.  The only sandals I've seen with any arch support.
[mtrj620] (score 8, diepte 0) Birkenstock Arizona.... Don't look any further
[mtrlhj7] (score 7, diepte 1) They are good for short walks but not great for long walks and different weather.
[mtrvut1] (score 7, diepte 1) Oh man. I just walked 20-30k steps a day in Portugal for a week exclusively wearing Birks. They were perfect (except the one time I stepped in a puddle and they got wet)
[mtrlyhg] (score 7, diepte 1) Second this. Absolutely love mine.  And they offer resoling
[mtrl4b9] (score 6, diepte 1) I like my keen fisherman style.   Need the toe protection because I’m a big clumsy oaf.
[mts26oh] (score 6, diepte 0) Keens
[mtrtdnp] (score 5, diepte 4) Yep,  order them on the website under the custom tab.  And you get to make whatever pair you want with the soles you want.  Also looks like everything is 25% off for memorial day.  

Plus they are repairable so if you get the custom and get them repaired when the time comes you could easily get 10years out of them with hard use.
[mtro2ry] (score 4, diepte 1) Third this
[mtrxsbp] (score 4, diepte 0) Keens hands down
[mtrj081] (score 3, diepte 0) Mephisto shark are super comfortable & durable. I’ve worn them to Disney with no issues.
[mttq6nf] (score 3, diepte 7) You can get them to repair/replace the footbed or straps as well. But if it’s just a smell, toss them in a freezer to kill the bacteria.
[mtrm98x] (score 3, diepte 1) 100%, the perfect shoe.
[mtrsezm] (score 3, diepte 1) Agree. I have had the terra fi line since I was in college (now terra fi 5) and love them. I'm a big guy (6'4", 275) and they are comfortable. I wear them to do lawn work, at the beach, moderate hiking, fishing, etc. Only reason I replace them is because I wear them out after 2-3 years of constant wear from March to October every year. I'm about to go on a trip to Rome this summer and plan on wearing nothing else on my feet.
[mtrm1t5] (score 3, diepte 0) I’ve had Tevas and Chacos and both are fine however I broke my big toe a long time ago and anything that goes around the outside of my toe hurts. 

My current favorites are a pair of Bedrock Cairns. They barely look worn after three summers and don’t cause any chafing. They have a thong that goes between your toes and that can take a little getting used to if you aren’t a regular flip-flop wearer.
[mtrpdsp] (score 3, diepte 0) i’ve had Teva, Chaco, and Keen. All are good, depending on what you expect to be doing in them.

Teva’s are a good alrounder.  but your foot can slide around on the foot bed, especially if it gets wet. And I don’t think the grip is all that great.  

Chaco was invented by river rafting guides with a single figure 8 style web/strap with a buckle that will never come loose/come off once you tighten it.  So very good in fast water rapids or anywhere you have a Risk of the sandal coming off.   It is far more secure for uneven ground than Teva because it goes around a big toe.  (Yes I know they have other models). Great arch support, and the soul is made by Vibram, which is the same as most high-end hiking boots.  Super grippy.  Only they are a bit heavy because of how thick the heavy rubber soul is.  

I am currently rocking a pair of Keens with the mostly covered /enclosed toe box.  

They use a neoprene sleeve over your 4 foot with a rip cord strap to tighten it, and a dedicated heel.   

They are lighter weight, but still with an excellent grippy sole.  

I love that I can just fold down the heel cup flat and wear it like a slip on yet it still feels plenty secure.  

The partly enclosed toolbox is a bit of a pain if you get gravel and rocks inside, which is why I wear it like a slip on to easily kick it off and shake the rocks out without having to bend over to take it off. 

In every case, the above sandals took some getting used to in terms of blisters or irritation at high- friction spots.  You may want to invest in some Leukotape/blister tape while breaking them in and on your longer walks. Or thin socks!.  And definitely do break them in.  

And finally, I once owned a pair of Nike Air Terreo which were the best sandals I ever owned.  They looked a bit like the Keens, but no closed toe box.
They also had a heel that could fold down to wear like  slip on.  

I checked through all of South Asia, including Annapurna circuit and Annapurna base camp (all, but about three days when I needed my hiking boots because of the cold and snow). They were incredible and lasted forever. By the time I needed to replace them, I learned they had gone out of production.   I tried desperately to find a pair around the world anywhere at any price with no luck.

I have an extra wide 4 foot so with the Keens, I was very nervous.  They have a wide toe box, but I didn’t think wide enough so I upsized by at least one if not, two sizes and it was totally fine.

Best of luck, let us know what you decide, and let us know if you’re happy
[mtrtgrh] (score 2, diepte 2) I agree. I love them for around the house and maybe even walking the dog. But I brought them on vacation and grew fatigued and found hot spots  for sure.
[mtrr1zr] (score 2, diepte 3) Is that something you do online?
[mts5jlw] (score 2, diepte 5) I resoled a pair I picked up in 2015 (the Grateful Dead 50th ones) last fall and they’re good as new.
[mtx971k] (score 2, diepte 1) I bought some Teva Hurricanes a few years ago, and have put a truly ludicrous amount of miles on them (I walk a tremendous amount and hate to wear shoes). They aren't BIFL, in that they aren't resoleable, but this is also a situation where the "for life" is going to describe exceptionally few if any products.

You do want to ball out on the fancier tevas, though--I got a pair of the "original universal" that are reaching the end of their life.
[mzf3u9a] (score 2, diepte 4) i mean resole-able is a strong word, I'm pretty sure all the dude did was cut a vibram sole to shape and glue it to the bottom 😅
[mtryhv3] (score 2, diepte 1) Was not expecting fellow barefoot shoe enthusiasts out here in the wilds! I just had mine resoled!
[mtt8h4a] (score 2, diepte 1) Yup look no further
[mtrtast] (score 2, diepte 2) They are great sandals. I basically live in them all summer.
[mtweu2g] (score 2, diepte 1) The tevas are nice indeed. Especially the hurricane series, good grip. There's quite a spread of them.
[mtrmig2] (score 2, diepte 0) Keens are ok.  They're certainly durable and have a lower arch.  Birkenstock's arch is way too high for me; they are just unwearable.  

If you want to drop the cash, I really like Mephistos.  They fit great, are comfortable and I wear them year-round and get about 3-5 years out of a pair.  Like really- except for hiking or yard work, that's what I wear.
[mtronw9] (score 2, diepte 0) Birkenstock Arizona. 

It has fantastic arch support. Probably the best available. The footbed is made of organic material that will mould exactly to your feet over time. This does mean it takes a while to break them in. The Regular footbed is what I would recommend along with real leather as the uppers (or straps). One caveat though is that they do not like getting wet. 

There are many variants of that style. The [Arizona Grip](https://www.birkenstock.com/us/arizona-grip-natural-leather/arizona-vintagewood-naturalleather-0-evarubber-m_1700.html) version has fantastic quality leather and a real rubber outsole that lasts longer and has better grip than the standard EVA foam soles.

I bought my first Arizonas 16 years ago. They were so comfortable I only wear Birkenstock footwear now. I stil have that pair. They are going to the cobbler for their third full rebuild (new footbed and soles) imminently.
[mttpf8b] (score 2, diepte 3) Thank you. That's good info.
[mtruxo5] (score 2, diepte 0) I got some merrel Moab sandals last summer, I’m over 500 miles on them and they’re feeling like they might have another 500 in them.
[mtrxoaw] (score 2, diepte 0) All recommendations are likely good, but no matter which ones you get you will have to slowly break in and get your feet used to. 

Go for short walks first. Come home at the first sign of a blister forming. 

My teva sandals are great, but I was tightening and loosening quite a bit for a while until they fit perfectly
[mu0wvdv] (score 2, diepte 0) Oofos slides are surprisingly good for walks. Incredible support and haven’t had much issue with blisters. Wouldn’t recommend for hiking through a bunch of rocks and dirt but for day to day walking they rule
[mtrqx6i] (score 1, diepte 2) Chacos are def not what they used to be but if you make custom custom chacos then they are “assembled” in US and are much better than they standard chacos which are all made over seas now.  It’s worth the extra bucks
[mtv8qy4] (score 1, diepte 8) Good to know, thanks! Those bad boys are going in the freezer shortly
[mtx3yi9] (score 1, diepte 1) Hiked the Long Trail, Cohos Trail, and a good chunk of the northern AT in Tevas.
[mzdji7u] (score 1, diepte 2) I got my teva hurricanes in 2021, resoled a few months ago. The resole hasn't quite worked out, i need to carve it to make it grippier in different situations. Buuut one of the smaller side ankle strap just snapped and makes me quite sad.
[mzeif3k] (score 1, diepte 3) I honestly had no idea they were resoleable, that's great news for me.
[mtthafb] (score 1, diepte 1) I live in the tropics and wear them every single day. Super comfy and secure. I’m almost ready for my third pair of soles on mine.
[mttpgbo] (score 1, diepte 1) Bedrock gang strong!! 🦍 I have had the one since the OGs - those were like 4mm thick and I still use as camp slippers. I have a second pair (cairn 3D) since they came out and wear them all summer - camping, kayaking, gardening, etc). I can wear these everyday if I could. 
Only thing I’d caution is these “barefoot” style are hard on your feet initially but your foot strength improves immensely and you forget that you’re wearing these.
[mtumua3] (score 1, diepte 1) I wish they did something other than zero drop, which doesn't work for me over distance walking.
[mtrl30y] (score 1, diepte 0) I’m on my third pair of Tuva in Florida. I get about 7 or more years out of them in almost daily wear.
[mtrrk0r] (score 1, diepte 1) Been looking at Tevas this weekend. Never heard of them but I did like their grips
[mtrtqzx] (score 1, diepte 2) I haven’t tried the Terra fi. I need to replace mine this year so maybe I’ll try them out!
[mtx2mnw] (score 1, diepte 1) They can be resolved though, ya?
[mtrnbgk] (score 1, diepte 0) I like Tevas or any of the varieties of Birkenstocks.
[mtrnuev] (score 1, diepte 0) Tevas. I’ve never had to replace a pair of them except for when my dogs were puppies and chewed them up.
[mtrxu61] (score 1, diepte 1) How much do you pay for the rebuilds?
[mttban9] (score 1, diepte 2) £55 for a new Birkenstock footbed and Vibram soles (they are better than Birkenstock soles) in London (UK). That was last year. It might have gone up since. Considering the work that goes into a full rebuild, I think it would be justified. The price includes labour. 

For comparison, the cheapest real leather [Arizonas](https://www.birkenstock.com/gb/arizona-natural-leather/arizona-core-naturalleather-0-eva-u_10.html) are £95. So the saving in relation to new is £40 with zero breaking-in time on the uppers. This [price list](https://www.mzztrzz.com/collections/birkenstock) from a Californian supplier shows the cost of parts in the US. So £55 was very reasonable, maybe even too low.
[mtroz6m] (score 1, diepte 0) The squishy Tevas that mold to your feet over time.  I had a 20 year old pair that my wife mistakenly threw away.
[mtrp32m] (score 1, diepte 0) Chacos
[mtrqk13] (score 1, diepte 0) I have really enjoyed my Birkenstock Atacamas, they are going on 3 years old and have held up pretty well. I should be able to get another couple years out of them at least.
[mtrrk04] (score 1, diepte 0) Chacos.
[mtrta8y] (score 1, diepte 0) Teva
[mtrtp0n] (score 1, diepte 0) Bedrock! No shoe is really bifl, but they have a resoling program. They are extremely good, i have put many hundreds of miles on them. They are the only shoes I wear pretty much
[mtrv6u9] (score 1, diepte 0) Altras is a running brand that has sandals.
[mtrw4r2] (score 1, diepte 0) When I take my man out for a walk it's strictly barefoot, I don't want him running off too fast.
[mts7ao0] (score 1, diepte 0) Birkenstock
[mtt46c7] (score 1, diepte 0) My Keens closed toe sandals last well over a decade and I wear them daily whilst walking for miles with my dogs.  Well worth the money and they hold appearance forever.
[mttk2na] (score 1, diepte 0) OluKai - the expensive ones their like $100+ leather foot bed. I did Disney and Epcot in those and my feet felt unbothered multiple 10+ miles a day.
[mttqx2t] (score 1, diepte 0) I've had a pair of Keen Newport H2 for around 15 years now and they are lasting really well, used for hiking and for beaches.
[mttyfaf] (score 1, diepte 0) Birkenstocks are great once broken in. They are plenty durable if you find a cobbler to replace the soles as needed.
[mttzqp4] (score 1, diepte 0) Dunham Nolan sandals have been serving me well for the past 5 years. They are a bit obscure since the company is mostly known for boots. They are part of the Rockport Group owned by New Balance.

I found these when looking for sandals with buckles - adjust once and then click them on/off. I hate fixing and tearing Velcro each time.

Aesthetic is subjective. They look the part of a durable, weather resistant, comfortable sandal. Definitely function over fancy.
[mtu5swx] (score 1, diepte 0) I’ve had a couple pairs of Teva hurricanes and walked/hiked quite a bit in them. I’m not a sandal person per se and I’m pretty choosy about footwear fit. I tried a couple pairs of Chacos on but they felt perceptibly heavier than the Tevas.
[mtufx97] (score 1, diepte 0) I have a pair of Teva Sandals that hold up great for long walks. I hike and run in them too, I forget the model but they are a little more robust (and a bit more expensive)  than the standard model
[mturee0] (score 1, diepte 0) Teva universal trail.
[mtva2c8] (score 1, diepte 0) Have worn Keen sandals for hiking for many years. They're great.
[mtvhco9] (score 1, diepte 0) I thru hiked the PCT and a fair number of my trail buddies wore Chacos for that and did well. I've seen Teva recommended elsewhere in the thread and those DID NOT do well from what I saw. The sole is too rigid and that caused blisters. I wore boots because wearing sandals to walk 30 miles a day is fuckin' nuts and I don't care about the evidence I saw to the contrary with my own eyes I'm not going to buy into that nonsense.
[mtvo94b] (score 1, diepte 0) Bedrock Cairn Sandals. The Evo C will give you the most arch support. They'll mold to your feet after you break them in. Bedrock will resole them for $65. 

Wore my Evos every day for 2 years before they had to get resoled. Went on 5+ mile hikes and swam with them too.
[mtwo9gw] (score 1, diepte 0) Can't beat FitFlops for me. Used them for years
[mtxapah] (score 1, diepte 0) Chacos Z1 classics. Great arch support, super comfortable, and they're repairable.
[mtrhp9a] (score 0, diepte 0) I think what you’re looking for is a pair of tennis shoes.
[mts8ayo] (score 0, diepte 3) really? Like their premium soft footbed etc? I have a hard time taking then off bc the support is so good lol
[mts9nqc] (score 0, diepte 6) Does the process remove the upper part of the sole as well? I love my chacos but they tend to get a bit ripe after a few years of wear
[mts86e0] (score 0, diepte 2) I didn’t even know that ! Good to know when I wear out mine :)
[mtsadpq] (score 0, diepte 1) Can't say enough good things about these! Took em to Yosemite and Grand Canyon and couldn't be happier!
(8 reacties met lagere score weggelaten)

=== THREAD uz9nvj ===
SUBREDDIT: r/USPS
DATUM: 2022-05-27  SCORE: 58  REACTIES: 83
TITEL: What's your record? Postal math and mapping states 3.59 miles away from delivery location when I'm two feet away.. 🤔
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ia8yyhc] (score 23, diepte 0) And the other day our PM said that the system was flawless 🤦‍♂️
[ia923qk] (score 23, diepte 1 OP) Everything is flawless and efficient at the post office..
[ia8zas0] (score 10, diepte 0) I had close to a mile but damn. You win. Lol.
[ia9es63] (score 10, diepte 0) next time you get a parcel that says its that far away scan it with the load tool again…
the label says one address but the load tool says another
[ia92bde] (score 9, diepte 1) I've definitely been stopped from doing something stupid by this screen before.
[ia8zktr] (score 8, diepte 1 OP) There has to be someone here in the double digits.. 😂 I swear I had one when this program first started that was 20 or so miles away from delivery location..
[ia963kv] (score 8, diepte 0) 4.05 right outside their mailbox. I even have the picture!
[ia9au0c] (score 7, diepte 2) It's all flawless-(until it isn't)
[ia9nb8w] (score 6, diepte 3) 28% of the time it's 100% accurate.
[ia91dg1] (score 5, diepte 0) The answer is always YES
[ia95hns] (score 5, diepte 1 OP) I was told to stop using any amount of IQ when I started working here.. Soo..
[ia9jnej] (score 4, diepte 2) Word didn’t you know lol
[ia9j8rq] (score 3, diepte 2) The town I carry in shares a zip code with another town farther away. Some addresses are the same in each town. As a consequence, a lot of the stuff I’ll have that shares an address will have the wrong town name on it. I frequently get between 11 and 12 miles on those packages.
[ia93dlr] (score 3, diepte 2 OP) Definitely. When it's meant to work it works.. unfortunately the "working" part is in question-
[ia93zlm] (score 3, diepte 0) That’s close enough. Now if it was 3.69 I’d have a problem
[ia96j0d] (score 3, diepte 0) I have one place that always scans at 5.3 miles away. On Amazon Sunday it gets placed on the route on the completely opposite side of town. Makes for a 40 minute round trip if you follow it in order.
[ia97667] (score 3, diepte 2) Told management about it 4 years ago. Said they'll get it fixed. Still waiting....
[ia9d06z] (score 3, diepte 0) Old scanner, but had a sample request for a box that was easily two miles away and said something like 30ft.  I was before the box, so I stopped…sorted through about 50 boxes with of stuff and scanned it!  F around and find out…
[ia9dwv6] (score 3, diepte 1 OP) Don't get me started on sample requests.. I received one a few months ago on my way back to the office after delivering the route. It was only 12 miles away 😂
[ia9j595] (score 3, diepte 1 OP) In a rural area I could see it happening- 4 miles is pretty nuts lol
[ia9jbzi] (score 2, diepte 3 OP) 😳 accuracy is dialed!
[ia91wni] (score 2, diepte 1 OP) True that. I spend more time answering yes than the actual delivery itself. Such a great system.
[ia96u8i] (score 2, diepte 1 OP) Now we are talking! Lol
[ia96xov] (score 2, diepte 1 OP) Lol.. now that's efficiency at its finest.
[ia9d4fy] (score 2, diepte 1 OP) Please tell me the scanner self-destructs if you do that 😂
[iaah72s] (score 2, diepte 1) If you don’t hit enter or yes or no, it’ll go back to the regular screen. When you get to the actual location you can pull it back up by hitting “w” on the menu. “W” only shows up when you have a sample request. I’ve had problems for ages with it going off before I’m at the address it wants and it always happens when the address I am at has something that needs scanning. Hate it.
[ia9doez] (score 2, diepte 0) no it is just an option that says something like package left on property or whatever. get use to using it every time and you'll never get that damn "too far away" message again
[iabyqlw] (score 2, diepte 1) This right here. It’s a current scam that’s being pulled on us. Gotta be vigilant.
[iadlw7g] (score 2, diepte 2) care to elaborate on said scam ?
[iaefgfg] (score 2, diepte 3) There is a barcode recycling scam that has been seen in multiple areas already. This might be related as it happened to me a few days ago. The return address is 
Return1
950 Francisco St
Torrance, CA

It leads back to an Amazon seller. If you see this return address be wary.
[ia9f0wz] (score 2, diepte 0) 7.6 miles, I had to show the people why I was laughing
[ia9f6bf] (score 2, diepte 1 OP) 🔥🔥 Nice! 

It's even better when management "tries" to use the scanners and discipline as far as being off route..
[ia9fvtq] (score 2, diepte 2) Yeah our union rep already told them if they do that he will personally make sure all talks take as long as they can since they're wasting his time.
[ia9h0kk] (score 2, diepte 0) Didn't take the pic but had one over 4 miles the other day. Highway Contract Route in the Colorado mountains so I wasn't surprised. Some people's mail boxes are nowhere near their actual homes.
[ia9i630] (score 2, diepte 0) Whenever I get these, I back-out and check the “load truck.” Almost always has a different address under load truck than the label indicates. Not sure how or why the glitch?
[ia9nx7k] (score 2, diepte 0) Maybe the tracking number linked to a different address
[ia9yutg] (score 2, diepte 2) Damnnnn in that case your Sup running Sundays is just a fuckup lol 😂
[ia9z8x8] (score 2, diepte 2) Super annoying
[iaa6c1m] (score 2, diepte 0) This is interesting. I sell on eBay and occasionally scammers will alter the label so the barcode is correct for going to my house BUT the label is to another business or home a few miles away. 

Was able to verify by pulling an image off one of the sorter machines so, the scanner could be correct and the label manipulated.
[iab6jz6] (score 2, diepte 1 OP) Interesting- it's sad that it's even an issue. Glad you were able to investigate it and find a source of the issue. I'm guessing they are altering it on eBay's end?
[iac31js] (score 2, diepte 2) We just had a service talk about this. We are holding all parcels that distances this far off.
Almost all the barcodes have been scanned 6 or 7 times at different addresses in our area. Most dont have numbers..... just the barcode.

Bring this to your Postmasters attention. Its a scam.
[iac6t8t] (score 2, diepte 3 OP) We have been receiving packages with barcodes only and without tracking numbers printed on the label. Those are being held, and according to our supervisors it will be delivered but as a postage due.. lol

I'll talk to them about the distance, but like everything else it usually results in just a shrug. Standards are clearly a priority..
[iaatddz] (score 2, diepte 0) 11.3 miles 🤣
[iaayec3] (score 2, diepte 0) Bad geo fence, let your sup know could be affecting other things
[iab67b6] (score 2, diepte 1 OP) They have known about this issue since the program rolled out- carriers constantly notify them of geo-fence and AMS issues but the only response from them is a shrug.
[iab94wq] (score 2, diepte 2) That’s a shame, such an easy fix too
[iabofga] (score 2, diepte 0) I had one that was around this far off… three and some change.
[iabotoz] (score 2, diepte 0) You win, so far as I know! The record in my office is about 9500 feet.
[iabvsqh] (score 2, diepte 0) Not sure because i didn't get a message like this, but scanner took me to the opposite side of town once, and tried to tell me the police station was a residence 10 minutes away on another.

Now i always have my phone Google maps running as well and then i take a guess when they disagree (usually the phone is right)!
[iac77fw] (score 2, diepte 1 OP) Lol.. timely, accurate and efficient. But how dare you have any time wasting practices.
[iacvq8j] (score 2, diepte 2) And if manglement ever chastises me for "using my phone while on duty", I'll happily deposit packages wherever their scanner tells me to, be that at the wrong house, or the middle of a lake.
[iacw5yv] (score 2, diepte 3 OP) Exactly. The funny thing is you probably would actually win that fight..
[iabw62r] (score 2, diepte 0) Got a long reverse from just picking it up and a hard braking when walking around the office with it. Didn't even head out to the street yet.
[iac70k9] (score 2, diepte 1 OP) Nice! 😂 I remember I got pulled in for being "off route" but the address it flagged me on was on my route and my dedicated lunch spot in the 1564A..
[ia95lrl] (score 1, diepte 1 OP) I agree.. a tenth of a mile more would have been way too drastic and unacceptable.
[ia99iwl] (score 1, diepte 2) Lol!
[ia981jr] (score 1, diepte 3 OP) The ADHOC- (driver skill training program) was told it was receiving a new DDC training program years ago. Constantly told it's coming out soon.. So for at least the next 20 years, new hires and retrains get the watch the terrible animated course 😂 

We all know everything happens overnight at the PO..
[ia9cuzs] (score 1, diepte 0) hit yes, then esc. choose option 6. this will solve the issue.
[ia9e3eb] (score 1, diepte 1 OP) Awesome. Appreciate the heads up on that- I'll give it a shot
[ia9reqm] (score 1, diepte 2) Parcel locker is the one that overrides the distance.
[ia9jc1t] (score 1, diepte 2) If it ever happens again I'll definitely snap a picture. It was one of those places that gets a parcel like every other month.
[ia9j1wg] (score 1, diepte 1 OP) I've never thought to look at the load truck. Interesting for sure..
[ia9jm65] (score 1, diepte 0) Scanner don’t lie
[ia9jsf2] (score 1, diepte 1 OP) Scanner is just as honest and accurate as management.. 😂
[ia9nozi] (score 1, diepte 0) The best is when you have two packages that both read wildly different, yet still both are incorrect
[ia9q7bz] (score 1, diepte 0) I’ve had it say 1.39 miles on me when I was literally at the front door of the house any closer I would have been in their living room
[ia9shv7] (score 1, diepte 0) Mine was over 1000 miles once pffft. Great system
[ia9sltl] (score 1, diepte 0) There’s one street on a route I do pretty often where I’m always ~7.62 miles away from the delivery point. I’ve checked and double checked that I’m in the correct location so now I just always roll with it
[ia9t4n1] (score 1, diepte 0) So it was a forward?
[ia9towo] (score 1, diepte 1 OP) Nope. Accurate name and address.. lived at address for over 10 years
[ia9vrb7] (score 1, diepte 0) You probably have a fake barcode scannable. People have been scamming USPS lately with crap barcodes, literally caught one today on my first loop
[ia9wqog] (score 1, diepte 1 OP) Amazon with this one
[iab6ov9] (score 1, diepte 3 OP) I hear stories about Sunday 😂
[ia9wmsp] (score 1, diepte 0) What's the lowest you've got? I think mine was like 39 feet. Now my scanner won't update and the GPS thing doesn't work,, so I don't have to deal with it at all.
[ia9y7pc] (score 1, diepte 1 OP) I think 39ft is the lowest I've seen as well..
[iaa36nl] (score 1, diepte 0) Now you're thinking with portals...?
[iaa3q4k] (score 1, diepte 0) Those are most likely scam barcodes with return address in Torrance, CA.
[iab7863] (score 1, diepte 2) Scammers are very sophisticated & if I didn’t work here I never would have figured it out in time and even then it took jumping through some hoops because initially you just assume it was misdelivered so your fury is directed at the carrier. I pretty quickly determined it wasn’t his fault (for clarity this was an item being returned and once it’s scanned delivered u have three days to issue a refund or ebay will) in this case the scammer was supposed to return a MacBook, instead he returned a bag of costume jewelery and mailed it to a jewelry store but with the ebay provided return barcode attached to the label. I assume they used Acrobat to alter the label tho I imagine there are many similiar apps these days.

Apparently it has been going on for a few years.
Ebay was aware of it & absorbed the loss.

Edited to add, the label they used was purchased at usps online so the weight etc would match up with what they had returned but they overlayed the eBay barcode over the other barcode -
[iab690v] (score 1, diepte 1 OP) Double digits! 😂
[iac7i2r] (score 1, diepte 3 OP) Yep. If this company would just focus on service standards, being more efficient and communication it would eliminate 80% of its problems.
(3 reacties met lagere score weggelaten)

