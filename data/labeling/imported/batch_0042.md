# Label-batch batch_0042

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
Schrijf het resultaat naar `batch_0042.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: oq2t8y, y1b4tc, 1h2zoah).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD oq2t8y ===
SUBREDDIT: r/BuyItForLife
DATUM: 2021-07-23  SCORE: 152  REACTIES: 150
TITEL: Indoor slippers with arch support
POST (source_id=post):
I’m on my feet all day, but I work from home and due to some back issue I have to take a 5 -10 min break and lie down every few hours so I prefer working in slippers rather than shoes. I’ve been wearing these typical slippers I can get in shoe shops which wear out pretty soon but aren’t really comfortable. 

Need some super comfortable slippers/slip on slippers/or those ones with the  thick roof like band across the top foot.

Tried ones from sketchers but they were like flip flops and looked easily breakable. 
Needs:
Great padding, thick sole to prevent pain in hell and balls of feet
Arch support: I tend to pronate and I have a low arch(between flat footed and normal)
I have duck feet, so wide toe area (they look like a V)
All my shoes and slippers have worn out most under my big toe on both feet, in case that’s relevant.

P.S. I’m in India, so please suggest accordingly, I don’t want to have to pay a fortune on shipping.


Edit: Thank you everyone, I'll check out all your suggestions and get one that my budget allows for now, and maybe get the other ones later too. I'll eventually end up owning all of them I suspect!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[h68z6jf] (score 84, diepte 0) Birkenstock Boston
[h694ize] (score 34, diepte 2) Comfort is definitely the highest priority with birkenstocks. The cork sole conforms to your foot which makes them exceedingly comfortable. I believe they also offer decent heel support, because of the shape of the sole. 

I use the Arizona model as my daily house shoes.
[h68z60w] (score 28, diepte 0) Are Birkenstock’s available to you?
[h691bex] (score 28, diepte 0) I'm in the UK and find Crocs or Croc clones are good for arch support. I can even put my prescribed orthotics in them.
[h697b0v] (score 26, diepte 0) Oofos!
[h6935hw] (score 22, diepte 0) Haflinger.
[h6a7ujx] (score 18, diepte 1) I went to slip-on Arizona Suede Birkies (very soft)  worn with socks during the winter and barefoot during summer. I know. I know.  I’m now a member of the “socks and sandals” club.
[h69bfd3] (score 17, diepte 0) Birkenstock total game changers for me. I own like 7 different pairs
[h6aae1d] (score 14, diepte 0) Vionics makes slippers and flip flops with arch support. I use the slippers in the winter and flip flops in the summer as my house shoes.
[h6961nc] (score 13, diepte 1) I agree with Haflinger.  They have great arch support and wool exterior and so nice and warm.  Not sure if they are available in your area but worth a look.
[h69ds14] (score 11, diepte 2) +1 for Birkenstock’s for comfort. Make sure you get the original cork footbed not their new soft one.

The original cork will be uncomfortable for a couple of weeks while it molds to your foot, but after it does you’ll never want to take them off.
[h69asym] (score 11, diepte 1) I wear oofos at the hospital and at home. Helps with my plantar fasciitis/flat feet. Highly recommend
[h69s95m] (score 9, diepte 1) Haflingers are a revolution for my feet. My wife's family had them as their house shoe's growing up but I was always skeptical because of the price. I finally bit the bullet and honestly....there's no going back. They feel like an extension of my feet and want to be buried in them when I die.
[h6aet38] (score 8, diepte 2) Same. When I tried them on in the store I audibly said “oh WOW!”

However, I have been reading an interesting study about being “barefoot” and how cheap shoes/sandals led to nearly 0 foot issues, and the reverse happened for those that wear shoes with supports. I’ve been wearing a pair of Lems for walking and running errands, and it’s been helping me personally. The shoes are basically something to put your feet in and 0 support, and after a short while my feet got better. I couldn’t believe it. I still did stretching during the transition, but my feet felt sore after wearing my tennis shoes. Feet are strange.
[h69h7qw] (score 7, diepte 3) Same here. Easily the best footwear for comfort and support. Especially nice with the soft footbed option.
[h69o6cj] (score 7, diepte 1) OP should definitely try Crocs. They are expensive, but Amazon often discounts them. They're pillows for your feet and will last forever.
[h6adx2n] (score 7, diepte 2) There are two things in this world that I can’t stand:  people who are intolerant of other people’s cultures and the Dutch.
[h6abr1k] (score 7, diepte 1) Highly recommend vionic slippers.  I could live in mine!
[h6aewl6] (score 7, diepte 1) I third the vionic's! They're not BIFL though, I need to replace mine at least every year because I live in them at home and the arch flattens. However, I have yet to find anything with good arch support that was a BIFL.
[h697utz] (score 6, diepte 0) I recently got 'GIESSWEIN' bootie slippers for a similarish reason. 

Alternatively you could try a proper shoe, but only wear them inside.
[h6b5ub8] (score 6, diepte 4) I have them done locally at a cobblers. There are a handful here. I suspect sending them in would be more $.
[h69obt6] (score 6, diepte 0) I am prone to a lot of foot pain so I bought a pair of sneakers that I only wear inside.
[h69jdt8] (score 5, diepte 2) If you're looking for the best arch support/comfort, birks are the answer.
[h69lyz4] (score 5, diepte 1) I second this!
[h69iafh] (score 5, diepte 1) I love my Crocs sandal/flip flops for my summer indoor shoes. They have a lot of support to them.
[h6a11mx] (score 5, diepte 3) my wife's mom has a pair that are 30 years old, my wife has a pair that is 15. I haven't seen or heard of a pair going to shit. The craftsmanship feels like it could maybe actually last for life, in reality the wool might get thin at the rubbing points (like inside of the toe) at some point but we are talking half century of use.
[h69peka] (score 5, diepte 1) Got my mom oofos for her plantar fasciitis, however she does replace them every 6 months as they stretch out
[h6b2u6x] (score 5, diepte 1) Me too (but only two pairs) — they healed my bad plantar fasciitis (caused by Hokas). Only problem with Birks is they’re not BifL — the soles on mine wear out after a year or two.
[h69iexu] (score 5, diepte 0) I have normal slippers and I just put insoles in them, like Dr. Scholls insoles. They sell them at pharmacies here. Not sure what they have in India, but if you don't know what I'm talking about you can Google it and find a similar product.
[h6a1nz0] (score 4, diepte 3) Agreed, I mistakenly bought some Birkis from germany and wore them as my travelling shoes walking around amsterdam and all around Germany for the remainder of the trip until my friends mom laughed at me and told me they were indeed the same slippers /u/JehovasFinesse  was looking at. (But an earlier model).
[h69yko2] (score 4, diepte 2) Birkenstock’s are the most comfortable pair of shoes I’ve ever owned. I would rather be wearing Birks than be barefoot. I recommend getting some with the softer leather straps for extra comfort. The ones I have are a pair of their women’s two strap sandals with suede leather straps. The suede leather is more expensive but very worth it in my opinion.
[h692zej] (score 4, diepte 1) Yeah, I was gonna suggest to use insoles with any regular sandal and maybe use a double sided tape if needed. 

Crocks are so comfortable though.
[h697wy5] (score 4, diepte 0) It does not last for life but for years, olukai sandals.

I have horrible flat feet and those sandals are the only thing that can last me at least 3 years before giving out.

I wear them almost everyday indoor.

I do have a separate one for outdoors well.
[h69o4lp] (score 4, diepte 0) I hear wooden shoes are actually pretty comfortable, not sure what brands are available there though.
[h6a7c7p] (score 4, diepte 1) my mother grew up wearing wooden shoes. She swears they were incredibly comfortable.
[h69mif3] (score 3, diepte 2) They also make a comfy wool felt design specifically for slipper use. I wear them around the house because my chiropodist basically prescribed them to me for home wear. I wear the Gizeh design when it’s too hot for the wool ones.
[h69sh6l] (score 3, diepte 2) dude look into halflingers.
[h6cudl5] (score 3, diepte 2) Socks and birks are like a cozy hug for your feet. 😌
[h6bkpwg] (score 3, diepte 1) Birkenstock Zermatt are fantastic
[h69znrd] (score 3, diepte 2) How long would you say a pair lasts you?
[h6b4xjy] (score 3, diepte 2) I have had 2 pair for 7-8 years. The rubber sole are still great. The wool sole pair are destroyed 4 -5 years.
[h6asj19] (score 3, diepte 3) r/barefootrunning
[h69siw6] (score 3, diepte 1) I live in my 3 pairs of Oofos sandals right now. Helps with my flat feet tremendously. Only thing better for me is a pair of motion control athletic shoes with my orthotics- but not in the summer.
[h69unde] (score 3, diepte 1) I just bought a pair of  Oofos sliders to replace a pair of Chacos flip flops that broke. By the first day they had already become my indoor/outdoor slippers as well as my sandals.
[h69uust] (score 3, diepte 1) Second or third this.  Got some for my 80 year old mother and she loves the arch support in them.  Wear some myself and agree.
[h6cqfzw] (score 3, diepte 2 OP) Awesome! I'm getting excited reading these  comments now!
Did you have a flattish foot or something else? What do you think the problem was in hindsight?
[h6b4hnz] (score 3, diepte 2) I have had mine resolved. Is pretty inexpensive, usually under $25 for the pair.
[h6b5rb7] (score 3, diepte 3) Cool. Do you have them repaired locally, or do you send them back to Birkenstock?
[h6ba34x] (score 3, diepte 5) That’s smart. I live in a small college town (US), and our local cobbler went out of business a few years ago.
[h6blvuf] (score 3, diepte 6) Yea, I don't think any slipper is BIFL so this thread is fair game 🤣
[h6a14g1] (score 3, diepte 0) I read this as slippers that arch Linux runs on.

I need help.
[h6a6g9k] (score 3, diepte 0) I buy Canterbury Sheepskin (like UGG but better crafted) slippers (watch for coupons), and put an arch insert in under the top insert. Basically, you take out the wool insert, put the arch support in, and put the insert back in. 

Size up if you do this. They will break in/compress in about a week so don’t worry too much if the wool is tight. 

https://shop.canterburyleather.com
[h6anhec] (score 3, diepte 1) Vionic is my go to for shoes now. 

Also OP which sketchers have you tried? I currently use Sketchers Outdoor Lifestyle slippers inside and they’re great. Also have pair from Baretraps.
[h6akhuj] (score 2, diepte 2) Birkenstock’s absolutely if you can get them, be prepared for them to take a few weeks to break in.
[h6crrlh] (score 2, diepte 2) Birkenstock has 100% always been a comfort/foot health brand, it’s the pandemic that has made comfort fashionable.
[h6cspb8] (score 2, diepte 2 OP) Probably can't get them wet with the tape right? The glue will wear off
[hazqmxa] (score 2, diepte 4) Don’t know if you solved already but try the Crocs literide flip. 

It’s absolutely the most comfortable slippers/flip flops I’ve ever had.
[h692zdt] (score 2, diepte 0) I've been wearing crocs sandals around the house for years as house slippers, I got them used at the thrift store. The bottoms are a little worn but they haven't broke yet. They're great on my wide feet, lots of room, some support.
[h6cr4p9] (score 2, diepte 2 OP) If only Amazon reviews were this honest.
[h6a75hr] (score 2, diepte 1) I bought a pair of haflinger slippers and within a year, both my big toes wore through the top. I love them and pretty disappointed.
[h6a8yv3] (score 2, diepte 1) Is there a particular style?

All of the reviews I'm seeing for various styles are 4/5 stars.
[h6aw6qp] (score 2, diepte 2) I I have the Grizzly Clog Slipper. I’m super picky about my shoes’ being comfortable, but I don’t think the shoes I prefer will work for anyone else so make sure you can return them if you don’t like them.
[h695z4s] (score 2, diepte 0) Bata has a fit flop knock off that is pretty comfortable. At least the last time I was in India it was there.
[h6cq7gx] (score 2, diepte 2 OP) That doesn't sound very BIFL, does she use them very roughly or something?
[h6cqnll] (score 2, diepte 2 OP) I got a pair of sketchers for my mom coz I felt secondhand pain looking at all the bad shoes and sandals she wore and we were taking a vacation where she'd be walking the entire day and I thought yeah, she won't survive. She was so excited she picked the hottest pink laces with pink sided shoes I've ever seen.
[h6cbh9j] (score 2, diepte 1) I suffered from major foot pain for months. Bought a pair of the Oofos sneaker-type shoes and the pain was gone in about 2 weeks max. I wore those things out - literally. Wore them everywhere until I wore right through the sole. I need to replace them. Best investment for feet one can make.
[h6csxww] (score 2, diepte 2) Ah sorry, I just scanned your post. Better not try felted wool booties either.

I'll just leave it up in case it helps someone else.
[h69gwub] (score 2, diepte 0) [Sole](https://yoursole.com/ca/shop/womens/footwear) is a great company that makes exactly what you are looking for.  They are Canadian so I am not sure if that works for you.
[h69naj1] (score 2, diepte 0) I use ortho inserts in regular cheap house shoes. The ones that are the same style as Vans slip-ons.
[h69nkoe] (score 2, diepte 0) I bought a pair of Teva Ember Mocs and put orthotics in them. Been going strong for a couple of years now. Would highly recommend them but it can be a bit tricky to get them for a reasonable price.
[h69o38q] (score 2, diepte 0) I bought a pair of 20$ croc in lime green for indoor use while at my standing desk. Also safe from having the kids stealing them due to the color...
[h69xkpp] (score 2, diepte 0) Tynor silican  insoles in any sports shoes

Or sketchers
[h69xyvv] (score 2, diepte 0) Haflinger

of those mentioned, they're the closes to BIFL.  I wear mine every day.  Just replaced my 1st pair after 7 years. 

/thread
[h6a91r1] (score 2, diepte 1) Is there a particular style?

All of the reviews I'm seeing for various styles are 4/5 stars.
[h6aj6xl] (score 2, diepte 2) The ones with arch support will be those with cork soles.  

I originally bought them after suffering plantar fasciaitis.  Wearing these helped quite a bit, and adding inserts to my other shoes eliminated the PF
[h69yhqu] (score 2, diepte 0) So I know it’s another name brand but take a good look at Sketchers before you discount them. I bought some sandals from them and they are the best supporting sandal I’ve ever had. They make different shoes that are similar.
[h69ytye] (score 2, diepte 0) My wife uses uggs Tasman slipper. Loves them.
[h6a0wet] (score 2, diepte 0) I'm headed to get New Balance shoes in a few hours specifically for the padding. I'm posting now so I remember to update when I've tested them. One of the benefits is supposed to be more specific measurements in store. I know you can order them online either way. A quick check says they opened one near New Delhi in 2016, hopefully they've caught on and more stores are available. I don't think they're as expensive as birkenstocks get but not cheap either.
[h6ctvef] (score 2, diepte 1 OP) Run in debug mode; with shoes.
[h6a1cbf] (score 2, diepte 0) Birkis 

https://www.birkenstockexpress.com/Buy/mens-slippers.cfm
(73 reacties met lagere score weggelaten)

=== THREAD y1b4tc ===
SUBREDDIT: r/Frugal
DATUM: 2022-10-11  SCORE: 3989  REACTIES: 141
TITEL: Picked up this moldy, broken vanity for $25 and only bought new knobs and feet. Now I have a piece of solid wood furniture.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[irwe736] (score 320, diepte 0) What a lovely, modern piece! I know some people are going to look at this and question how frugal it is, given how long it must have taken, but I figure you 1) practised or learnt a great skill; 2) potentially saved an old piece of furniture from the skip; 3) made this piece attractive for its next owner; and 4) spent time on a fun project, which you might have spent doing something much more expensive.

Great outcome, great work!
[irwarg3] (score 257, diepte 0 OP) Paid $25 for the vanity in picture 1. When I got there, it had been sitting in a barn and smelled of rat pee and had quite a bit of mold on it, especially the bottom. I spent several days really sanding everything and realized the very bottoms could not be saved (black stains), and decided to cut it off at the rounded part. Then I ordered and installed feet. I did a super slight white wash to keep the wood from turning orange/yellow, then applied polycrylic (actually still need two more coats). I did have to fix the drawer and apply new front faces under the drawers, but was able to reuse the wood pieces I had cut off in order to preserve the same wood-look. I also applied drawer liner after sanding and cleaning everything thoroughly.

It’s not perfect, but it will work great for my daughter!
[irwb4ov] (score 213, diepte 1) "not perfect"? Don't sell yourself short. That took some serious vision and creativity and it looks fantastic!
[irwkvvs] (score 177, diepte 1 OP) Thank you! And agreed!! I am a homemaker, so my “time” is not being taken away from earning money elsewhere. Plus, I do love a good project. There is something very satisfying about giving new life to an old piece. And real wood furniture is nearly impossible to come by anymore, especially for a reasonable price.
[irwuv0r] (score 91, diepte 0) I like what you’ve done, it looks wayyyyy better. But I have to ask, $25 for a broken, moldy vanity? They should’ve given it to you.
[irwlotc] (score 59, diepte 2 OP) I sanded and sanded and sanded. I also cleaned it several times. There is an enzyme cleaner that helps with the smell (Odorcide). My preferred method is using BIN Zinsser primer to lock in any smells, but since I was going for wood look without painting, I could not do that. I got the worst parts when I cut the bottom off (smell-wise), and will be spraying on the polycrylic even on the inside to seal any other odor in. It does not smell anymore except when you get some of the bottom inside parts wet, hence why I’ll be using the poly. Best of luck with your project! You can do it!!
[irwbhz7] (score 48, diepte 2 OP) Thank you, that is very kind! 🥰
[irwyioe] (score 45, diepte 1 OP) 😂 Thank you! She was very much emotionally attached to it. And I did not realize it was moldy until we got there because she used pic 1 in the ad before the mold happened.
[iry8yt7] (score 37, diepte 0) it looks phenomenal, but man I would be so nervous introducing a moldy piece into my home if I wasn't 110% certain all the mold was gone. Can you elaborate more on what steps you took toward remediation?
[irwjq4y] (score 31, diepte 1) This looks great! I have an old piece similar to this stored in a garage. The bottom has mouse droppings-did you have to apply anything to clean the wood or did you just sand it all off?
[irwqi2d] (score 25, diepte 2 OP) Acrylic white paint we already had. 20% paint, 80% water. Mix well. Brush on (small sections), then wipe off with paper towels. I did it rather quickly (almost immediately) since I just wanted it as a sort of haze to maintain the look of the wood. Polycrylic alone might have done the job, but I wanted to be extra sure to keep away from any yellow or orange tones.
[irwkxch] (score 22, diepte 0) Awesome work!  I especially like that you removed the ‘arches’.  It looks better without them imo.
[irwm2eo] (score 16, diepte 1 OP) Thank you! I agree. Much more modern. But they were also the worst offenders with the mold/pee smell. I cannot describe how bad the rat pee smells when wetting or cutting the wood. It took a lot to get it unsmelly. 😂
[irwgvjc] (score 12, diepte 0) I swear that, or one just like it, was in my family when i was a kid.  The broken drawer even rings a bell.....
[irwl1vi] (score 12, diepte 1 OP) She said it happened in her last move and they were unable to find the piece. She got it used when she was 12 in the 1950s. 😊
[irxc2ch] (score 11, diepte 1) Was about to say the same, OP thankfully you did so great it makes it worth it but man… people would sell anything these days.
[irz5owd] (score 9, diepte 1 OP) Sure! I will say that the mold was 95% on the old varnish, so considering that it took many, many sanding sessions just to get to the wood part, I feel quite confident that I got most of that right away. If you look at the picture of the broken drawer, you can see the spots I am talking about. They were sitting on top of the varnish and eating at it. On the original bottom feet, however, the varnish had been rubbed off from years of use, so the mold had a chance to get into the wood fibers there, which I eventually decided to cut off. The only parts that might have had remnants were low on the inside (unfinished), and some of the drawer bottoms (also lower ones). I sanded and sanded and washed with bleach water. Obviously, bleach can only do so much with fibrous material when it comes to mold, so I will also be spraying polycrylic over the inside to seal up any remnants that may want to come to life again (if ever). That’s about the best I can do/think of.
[iry91hg] (score 9, diepte 0) So what did you do about the moldy drawers?
[iry9r87] (score 8, diepte 0) How did you remove the rat pee smell? I inherited a dovetail dresser that I’m looking to redo. It was sitting in storage for 2 yrs and smells like rat pee. I left it to air outside about 2 days but still smells. I thinking of using bullseye primer after I figure out how to clean it.
[irxt5tt] (score 7, diepte 3) How do you make sure it doesn't have bugs inside?
[irwpqmy] (score 7, diepte 1) this looks gorgeous!! can I ask how you did the white wash?
[irxakh5] (score 7, diepte 1) How well do the drawers work? Waxing the drawer slides can help a huge amount with old furniture

Furniture wax exists or just paraffin works in a pinch
[irwnokk] (score 6, diepte 0) I love what you've done with that!  But I think it's not a vanity.  In my youth those were sold as student desks and a whole generation of kids in the '40s and '50s did their homework on them.  But they never looked this good.
[irz64qe] (score 6, diepte 1 OP) I used Odorcide, an enzyme cleaner as someone mentioned below. If you plan on painting it, I would also recommend Zinsser’s BIN primer over Bullseye. It’s more pricey but totally worth it!!
[irz41qc] (score 5, diepte 2 OP) They aren’t sticking at all as they are not super tight in there like you sometimes run into with old dressers etc., but thanks for the wax tip - I have some in the garage! I actually like waxed wood furniture as well (for the areas you do see and use), but I prefer polycrylic for durability and because I am too lazy to treat the piece over time again.
[irz4n1w] (score 5, diepte 2 OP) Lol That’s funny and can’t say I haven’t run into the same issue with other projects. 😂 At this point, hubs and I have done so much DIY and fixing up 4 houses that we own 90% of all tools we could reasonably need for most projects around the house.
[is08xtb] (score 5, diepte 3 OP) You are right, although Amish furniture isn’t accessible for all areas of the country, but also often is not very modern from what I have seen style-wise. But price is the main factor, hence why I posted in r/frugal.
[irwoje1] (score 5, diepte 1 OP) Thank you! The lady I purchased it from got it as a vanity when she was 12 in the 1950s (it was used then already). It is shallow enough that it works as such, and will for sure be used as a vanity by my 12 year-old! Kind of nice to have it coming full circle with renewed life.
[irwx4th] (score 5, diepte 0) I think you could make a living out of doing that if you wanted to. Get at goodwill auctions estate sales fix them up and resell
[irwyxuk] (score 5, diepte 0) The piece is stunning! Great work!

How did you hold the vanity so you got such a clean cut along the bottom?
[is07olq] (score 4, diepte 2) It is easy to come by, plenty of sites (typically Amish sellers) offer them... I can't contest the price part though.

I saw an awesome "L" desk with hutch made of solid wood, but it cost $7000. As much as I loved that desk I decided to skip on it for the foreseeable future.
[irza7v0] (score 4, diepte 1) I have the matching dresser.  Got is from my mom, who said it was her brother's, when he was a kid.  BTW my mom is 90.  Never knew what the wood would look like sanded down.  I LOVE it.  Great job OP.
[irzgyli] (score 4, diepte 2) How did you remove the mold and pee smell?
[irwyth5] (score 4, diepte 1 OP) I was happy to because she was so emotionally attached to it. It’s all good.
[irx9632] (score 4, diepte 1 OP) That is incredibly kind. I hope my daughter can one day pass it on if she has a daughter herself.
[iryr7o9] (score 4, diepte 0) I usually don't like changing a piece's style, but this came out pretty darn sharp! NICE!
[irxqxq8] (score 3, diepte 1) I have a similar desk and I hate how dust and cat hair builds up underneath it. How did you cut off the original feet? And what kind of drawer liner did you use?
[irwg79v] (score 3, diepte 0) It looks great. You did an amazing job.
[irwshah] (score 3, diepte 4) Ha, I had the opposite thought, because wood is fibrous if it might be possible to steam clean.  Some luthiers use steam to remove small dings and dents from guitar bodies so the steam definitely would penetrate at least a short way into the wood.  But, yeah, I think you’re right, it’s probably more likely that the volume of steam you’d need to even start to remove smells would just destroy the wood.

Great work again anyway!
[irwxxtv] (score 3, diepte 0) Worried where you live that you had to pay for this
[irwyjn6] (score 3, diepte 0) Wow this looks amazing! Great work!
[irx6oy7] (score 3, diepte 1 OP) Go for it!! I will warn you. The sanding took several different day sessions with rest days between because I was so dang sore and could not physically do any more. My chronic tennis elbow didn’t help either. 😂 But well worth it in the end!!
[irx7a0b] (score 3, diepte 1 OP) I have a Dewalt rotary (?) sander, which frankly, worked the least. I used it anyway for a lot of it. I also used a multi tool with sanding pad, especially in the corners (it actually worked better for me) and also sanded lots by hand. I think if I had spent money on paint stripper first (and good scraper), I could have saved me quite a few hours of sanding because the varnish was the hardest to get off, and it starts to gunk when you sand for too long. But I was too cheap because paint stripper is pricey.
[irx14e9] (score 3, diepte 0) I have the same desk!!! Mine is still ugly though
[irx6tuf] (score 3, diepte 1 OP) 😂 I think it has its charms before, as long as the rat pee and mold is a non-issue, of course.
[irx61ix] (score 3, diepte 0) Congratulations, this looks fantastic! I envy your skills!
[irx8tfh] (score 3, diepte 0) Has all the qualities of a piece that will stay with you and possibly your family for a long time.
[irx9k7u] (score 3, diepte 2) The thing looks fantastic! And how it became that way touches a soft spot with me. I love it when old stuff is given new life. 

Kudos to you. I think this kind of stuff makes the world just that bit of a better place.
[irz75gb] (score 3, diepte 1 OP) Supplies:
- Vanity itself $25
- Four feet $12.79
- Drawer pulls $20.79
- Drawer liner $13.90
- Acrylic paint for white wash $0 (already had it)
- Loads of sandpaper $0 (already had it)

So less than $75 or maybe $80 (with tax), but multiple sanding day sessions for sure.

It’s not for everyone, but I still feel like I came out on top for a solid wood piece of furniture.
[irxxnlh] (score 3, diepte 0) I have the same desk. My father refinished it and I adore it!
[irxz1p0] (score 3, diepte 0) Wow I love this! Great job.
[iry0zn3] (score 3, diepte 0) From nope to dope
[iry3s4w] (score 3, diepte 0) I like it. Huge improvement. But I think it needs more feet – on the medial side of both columns. Currently, I looks kinda unstable (even if it is stable) and like it wasn’t designed with those feet in mind.
[irz5ujc] (score 3, diepte 1 OP) Hi! I just replied to a similar question so I will copy pasta my reply here. Hope that clears it up.

Sure! I will say that the mold was 95% on the old varnish, so considering that it took many, many sanding sessions just to get to the wood part, I feel quite confident that I got most of that right away. If you look at the picture of the broken drawer, you can see the spots I am talking about. They were sitting on top of the varnish and eating at it. On the original bottom feet, however, the varnish had been rubbed off from years of use, so the mold had a chance to get into the wood fibers there, which I eventually decided to cut off. The only parts that might have had remnants were low on the inside (unfinished), and some of the drawer bottoms (also lower ones). I sanded and sanded and washed with bleach water. Obviously, bleach can only do so much with fibrous material when it comes to mold, so I will also be spraying polycrylic over the inside to seal up any remnants that may want to come to life again (if ever). That’s about the best I can do/think of.
[iryasm1] (score 3, diepte 1) Use a cleaner with enzymes that break down urine. Most pet stores or grocery stores that have a pet section have it.
[iryn7fy] (score 3, diepte 0) Nice legs!
[irz7vse] (score 3, diepte 1 OP) I won’t because I refinished it for my daughter.
[irz1scb] (score 3, diepte 0) +1 upvote for not just painting it and declaring it restored. So sick of that trend.
[iryf7ei] (score 2, diepte 1) That looks fantastic.

I'd have spent $25 on the piece, then sank enough to by a brand new desk in supplies, and come out with something that doesn't look near the nice at 5x the cost
[is03mnn] (score 2, diepte 2 OP) Oh, awesome! Thank you for sharing that info! Yes, I was very happy to see the beautiful wood grain.
[irwjd19] (score 2, diepte 0) Really nice!!
[irwq3xf] (score 2, diepte 3 OP) I have three small pieces left after I repurposed three other pieces to fix the drawer front and the front face below the drawers on each side. But I don’t think a steam cleaner will do much. On hard, solid surfaces, sure, but fibrous wood, I doubt. It’s also a fine line between cleaning and destroying the wood with water, I would think. But I am no expert by any means.
[irxbu1n] (score 2, diepte 4) Short term moisture generally only damages the surface of wood, and the temperature of steam wouldn't do much to the wood other than hydrate it

So it might work if the steam heat breaks down the organic material? Then let it dry for a week then sand it down again? But I'd also doubt it will get rid of the smell

The enzymatic cleaners designed for urine seems like a better bet (sounds like you did that), maybe that then steam, then more enzymatic (after the steam opens the wood cells)? Finishing with sanding

So basically I'm agreeing the way you did it was likely best, the poly should seal in almost all of it. Cracks and seams might be at risk of retaining odor?
[irwntcb] (score 2, diepte 0) This looks great. Where did you order the feet from? Looking for something similar for a project I’ve got
[irwou26] (score 2, diepte 0) this is incredible and looks so lovely! well done
[irwpcm9] (score 2, diepte 1 OP) Thank you! 🥰
[irwp73b] (score 2, diepte 0) I wish I could do this, but I have such fear.  I had such a fear of termites and bed bugs with soft items.
[irwpi7j] (score 2, diepte 1 OP) Definitely no termites on this. You should be able to see that kind of damage (and their tracks) right away - no reason to fear! You can do it!!
[iry1vp1] (score 2, diepte 2) Be careful that it stays dry. I had a formerly moldy desk that was fine until it got humid, then it got moldy again.
[irwqoed] (score 2, diepte 0) Nice job!
[irwvjko] (score 2, diepte 0) Damn I want this. Love the light wood with the black hardware.
[irwykfw] (score 2, diepte 1 OP) Thank you! 🥰
[irwyq35] (score 2, diepte 1 OP) I am way too slow with the progress!! And being a perfectionist does not help at all. 😭 But THANK YOU!
[irwxyz5] (score 2, diepte 0) Love this! Frugal and eco-friendly.
[irwyd41] (score 2, diepte 0) great deal! nice finishing. looks amazing!
[irwz5xz] (score 2, diepte 1 OP) I laid it sideways each way and used a track saw!
[irwzj8w] (score 2, diepte 0) Woah
[irwzwq8] (score 2, diepte 0) I've seen a couple of modern conversions that didn't change out the bottom and add feet.  That makes a huge difference.  I have a very similar dresser that I have and was considering donating it and looking for another used one, but it fits perfectly into the space it's in.  I may do the exact same conversion to it.
[irx0sdc] (score 2, diepte 0) How did you sand it? Like with what tools and methods?
[irxiwog] (score 2, diepte 2) Good to know thanks for replying. Looks great!
(60 reacties met lagere score weggelaten)

=== THREAD 1h2zoah ===
SUBREDDIT: r/Frugal
DATUM: 2024-11-30  SCORE: 313  REACTIES: 137
TITEL: Recently lost a big client/60% of my income (I’m freelance). Family are asking what gifts I want for Christmas but I have no clue. Looking for ideas that might help tide me over until I get back on my feet. 
POST (source_id=post):
Wasn’t sure which flair to choose but this seemed like the best one. 

Hope the title makes sense! I’m basically looking for any gift ideas I can give my family to get for me that might help reduce my outgoings/prevent me from spending as much before I find some new work e.g. I was thinking toiletries like deodorant, wash sets, but I have a lot of that stuff in bulk. 

I honestly wasn’t feeling very festive after losing such an important client and had originally told them that I don’t need anything, but my family’s love language is gift giving. 

Worth noting that I travel home to another country for Christmas, so also can’t stretch the boundaries of a 20kg suitcase too far! 

Thanks in advance 🙏🏻

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lzn03rt] (score 410, diepte 0) gift cards or cash to the places you frequent
[lzn0pac] (score 156, diepte 0) Gift cards to your favorite grocery store. Trader Joe’s has food as well as little treats, so that would be my preference.
[lzn1igu] (score 139, diepte 0) Things that will allow you to reduce single-use stuff - a bidet, reusable kitchen towels (to replace paper towel), that sort of thing. Basically things that cost a bit upfront but save a lot over time.
[lzn0s2t] (score 90, diepte 0) For families down on their luck I send public service utilities gift certificates to assist in paying utilities over the winter cold months. 

When I moved out on my own my dad would randomly gift these and they were my favorite!  Also gift cards to my favorite grocery store and local butcher.
[lzn3g08] (score 86, diepte 1 OP) Great idea - I can’t remember the last time I got a gift card either! Thank you 🫶🏻
[lzn0qqs] (score 76, diepte 0) If they won't do gift cards, have them buy you things like a slow cooker, bread maker, etc. but schedule them to be delivered after you arrive back home. They can print out a picture of the item and put it in a card for you.
[lzn7yni] (score 46, diepte 0) My parents used to do a “household” gift box. Things like laundry detergent, dishwasher pods, trash bags, toilet paper, paper towels, all that boring stuff that adds up. Enough to last a long time. I loved it as a gift!
[lzn0e4a] (score 38, diepte 0) Money. In my culture people will give red envelopes with money in them as gifts and if is absolutely banging.
[lznts08] (score 36, diepte 1) Also ask them to prepay streaming services -- like getting you a year of Apple+ or Netflix or Amazon Prime. Similarly, if you need to pay any recurring costs for professional subscriptions or the like, they would be a good ask also.
[lzn9arv] (score 27, diepte 2) Slow cookers are a dime a dozen at thrift stores or on fb marketplace, ask for an instant pot instead
[lzn369d] (score 25, diepte 1 OP) These are great ideas, thank you so much 🙏🏻
[lzn3a3z] (score 24, diepte 1 OP) Slow cooker could be a great call! Thank you so much!
[lznqfzq] (score 21, diepte 2) Gift cards to gas stations are always great too!
[lzn3c2z] (score 21, diepte 1 OP) Gift cards are a great call - thank you so much 🫶🏻
[lzn4ksi] (score 19, diepte 0) Heated/electric blankets. They cut the heating bill.


Nice warm indoor/outdoor slippers.


Gloves, scarf, cap set.


If you live in a warm climate ask for a nice air conditioner unit.
[lzn7rz2] (score 18, diepte 1) And gas station
[lzpwnrw] (score 16, diepte 2) Ask for VISA gift cards do that you can use them wherever you may need.
[lznbtlh] (score 16, diepte 4) Instant pot is smaller form and has multi functions, will cook things in quicker times, as well as slower times. Saves energy when you pressure cook. 

Crunchy/browning on food is the one hole in the instant pot abilities (or a high quality similar appliance - check bjs/costco for  deals). If that is really important to how you like to eat, check out a multicooker that comes with an air fryer.

 If you get the right sized appliance, it will continue to save energy ($) as you’ll be able to make a meal without using your main oven. Get an exciting one will give you a new hobby - replacing take out and making meal prep to stretch $.

Another gift idea, if you don’t already have a large collection - spice kits from penny’s (or d add one place similar). Hope you get some fun out of it too!
[lzn2tow] (score 14, diepte 1 OP) I’m a freelancer writer in tech. I was actually writing for CNN but they had mass layoffs recently and this of course included contract workers. I’ve actually started creating a print for my mother, and I’m also making her some jewellery for Christmas gifts. For others I’m doing a lot of shopping on Vinted for some second hand gems and also using my (basic) knitting skills to create gifts for others 🧶
[lzn1if7] (score 13, diepte 0) I would just let them know what’s going on with you, that you would like to keep Christmas small this year, and would appreciate cash or cards due to the ease of travel. Then I would pack your bag with fun/novel inexpensive gifts to bring back to your home country (strange or yummy foods/candies they can’t find at home.)
[lzp3yxt] (score 12, diepte 2) Adding to the list: Thermos and classic coffee maker over Keurig and Starbucks. Cookware over takeout. Water bottle over bottled water. Deli containers and glass tupperware over plastic bags.

Use wired or rechargeable devices over disposable batteries.
[lzn37w0] (score 9, diepte 1 OP) That’s a really kind gesture! I love that!
[lzn3q2d] (score 9, diepte 0) Laundry detergent sheets, would pack well and detergent can be expensive so that would help. Socks & underwear if your in need of new ones, also belt or wallet. Gas or grocery gift cards as every ones saying, but if they dont have the same businesses as where you live then a prepaid credit card. Maybe to feel more gift like they can pick out some shelf stable groceries on like Amazon and ship them to your address.
[lzn8ksp] (score 9, diepte 1 OP) Love that idea!
[lzn51aj] (score 8, diepte 2) Add sprouting supplies. Fresh vegetables are important to good nutrition, and that often gets overlooked when times are tight. If you have sprouting equipment and seeds then you can cut down on the food budget without sacrificing good nutrition.
[lzp580v] (score 7, diepte 1) When I was struggling my parents gave me grocery and gas station gift cards, helped me immensely. My dad also made an appt for my car to be serviced and told them to fix anything that needed it. I lived 45 minutes from town so a working, reliable vehicle was like money in the bank.
[lzn9k0t] (score 7, diepte 3 OP) I’ll have a look into the differences! I have a small kitchen with very little counter space so would also need to take that into consideration!
[lzn5e89] (score 7, diepte 0) Basics, like laundry and dish soaps, paper towels and toilet paper, cleaning supplies and yes, gift cards to buy what you need, where you frequently shop.
[lzn9eft] (score 7, diepte 2) It is stuff you will need anyway until you get onto a better financial footing. These everyday must-haves do chip away at your finances rather quickly. I did this for my friends a few Christmases ago during the height of Covid, rather than cheap knickknacks. I laughed at how thrilled they were to get such an oddball gift. We now regularly surprise each other with useful items (like plastic totes stuffed with cleaning supplies, dishtowels, washcloths and so on. Totes get used too once emptied) during holidays and birthdays. We also throw in hot chocolate packets, tea bags, instant coffee, sometimes canned or pouch chicken noodle soup (or other) soup mixes, warm socks. Like I said, we can be weird (we are from 40s to 60s, me being the old lady of the bunch) and all of us are tired of accumulating things that, while cute, are kind of useless. None of us want to dust those knickknacks anymore (we live in a dusty desert town) so practical stuff it is!
[lzn6pkl] (score 7, diepte 0) If you pay for heat, I have found that an electric blanket saved a lot of money on the heating bill. I would turn the heat WAY down, dress in sweats and a heating blanket and slept like a baby. I wore sweats to bed because the morning was cold until the heat kicked in. This works even better if you already have a programmable thermostat. Now that I think about it, my brother worked from home and told me that he saved money by using his blanket while he was at the computer for hours on end. Good luck until you’re back on your feet.
[lzn7g5y] (score 6, diepte 3) Hmm I need to tell him that lol.
[lzowe9j] (score 6, diepte 1) This might be a weird add-on but I got a bulk of reusable baby wipes for the pat-dry after the bidet and a wet/dry bag (baby or camping kind) for the clean/dirty ones and they’re so soft and low upfront cost too. I have a separate color for using as handkerchiefs because they’re so soft! 

(I’m also allergic to the whitening process in paper goods and the bamboo ones are so expensive so this was also a need for me but totally cost cutting!!)
[lzn6piz] (score 6, diepte 1 OP) Slippers is such a good call. Already got the electric blanket prepped from last year!
[lzn7dao] (score 6, diepte 1 OP) I got an electric blanket last heat! Game changer! I also called my electric company last week to reduce the power I had (way too much for my small space) so hoping that will help too 🙏🏻
[lznjcr9] (score 6, diepte 1) My mom does this. It was very helpful during my college years.
[lznakau] (score 6, diepte 0) An E-reader if you enjoy reading. I don't know how public libraries work in Spain but I was able to connect my Kobo e-reader to my local library here in the US and have greatly increased the number of books I've read without spending anything.
[lzrq91h] (score 5, diepte 2) When I wasn't working, my favorite thing was Kroger gift cards! They cover food AND gas!
[lzn5cms] (score 5, diepte 1) Chinese? My hubby said Im too old for one lol
[lzn7c3l] (score 5, diepte 2) Is it age restricted? When I worked for a Chinese owned company and they give us all red envelopes with $500 during CNY
[lznq8do] (score 5, diepte 2) My parents still do it for us kids, even though we're all grown. Everyone loves getting a red envelope!
[lzo0da5] (score 5, diepte 2) When it comes to family red envelope giving, I believe you age out of it once you get married. It's your turn to give them out to kids now! Younger nephews and nieces if you don't have your own kids.
[lzp2sji] (score 5, diepte 2) Ok. ALDI gift card.  Lidl gift card.
[lznp1nu] (score 5, diepte 4) [Here's a tutorial from this sub's archives](https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F1rnpyiqktgj81.png).

Strongly recommend buying the equipment as components instead of in kit form, because the kits don't really give you very much. The physical equipment usually takes one of two forms: plastic stackable sprouting trays or specialized lids. On your side of the Atlantic the trays are probably the thing to get. It takes 3 to 5 days for a batch of sprouts to go from start to harvest, so get at least 4 or 5 trays if you plan to eat sprouts daily. 

The other things to consider are sanitizing equipment, training, and seeds. Ordinary household bleach will clean your equipment before use: soak for 10 minutes and then rinse three times. Either request a book about sprouting or else watch tutorial videos--it's important to know what you're doing and follow best practices.

Some suppliers sell seeds specifically for sprouting, or you could go to a store that sells cooking seeds in the bulk bins and find out whether they sprout. Check an online catalog to learn about the varieties. I started out ordering three types of seeds from an online supplier: alfalfa, mung bean, and a salad mix (which had several different species selected for flavor and similar growth times). Later those purchases expanded to radish and broccoli seeds.

More recently I've been experimenting from the local bulk bins in grocery stores. Have found wheat berries that sprout into wheatgrass. French lentils and red lentils are also sprouting. Brought home garbanzo beans with plans to test those out too. Most legumes such as peas, etc. make edible sprouts if you can find viable seeds. Browse a seed supplier's selections to get an idea of what your options are.

Have been using wheatgrass in smoothies with carrot, wheat bran, and either banana or date, plus milk and nutmeg. (Fresh dates are inexpensive here because this is near a major cluster of date farms). Alfalfa goes well on sandwiches in place of lettuce. Stir fry the mung beans. Make salads or casseroles with some of the others. You could ask for a sprouting cookbook if you need ideas.
[lzp4cvt] (score 5, diepte 4) Slow cookers do what they say on the tin, cook things slowly. They're good for tough (and therefore cheap) cuts of meat like roast, but can also make soups, casseroles, etc.

Instant Pots have a pressure cooker function that will heat food above boiling temperature and keep it under pressure so it doesn't just turn to steam. Food can get hotter than is possible in a regular pot. I mostly use mine for beans and brown/wild rice since they can be cooked from dry quickly.
[lzn34eu] (score 5, diepte 1 OP) Thank you, I have done so, but they’re so set on The Gifts 🥹 I’ve already got most of their gifts planned, some handmade and some never used items from Vinted!
[lzn1kjf] (score 5, diepte 0) giftcards for Costco
[lzngqup] (score 5, diepte 0) If you have a gym membership or something similar that you enjoy and adds value to your life and mental health I would ask for them to pay a few months subscription or dues.
[lznqfm3] (score 5, diepte 0) If they don’t like to be too practical, memberships to local museums or gardens, etc, might be nice and give you some free entertainment in the down time.
[lzu5sga] (score 4, diepte 4) I assumed OP was in the U.S. and saw he just edited to say not.

Coincidentally I lived in Spain myself for 3 1/2 years so I understand. Ignore gas giftcards OP but you can let your relatives know they do El Corte Ingles gift cards online you can buy from anywhere.
[lzn2wjb] (score 4, diepte 1 OP) Great suggestion. Oh how I wish we had a Costco in this country! 🥹
[lzn6un2] (score 4, diepte 1 OP) I do need some new undies and socks — hadn’t even thought of things like that. Thank you!!
[lznntxt] (score 4, diepte 1) My husband struggles with cold. He has a heated mattress pad and a heated blanket. He prefers the heated mattress pad.
[lzn7teg] (score 3, diepte 1 OP) My dad usually does this and it often comes in a red envelope due to the holiday colours!!
[lzo2wcr] (score 3, diepte 2) Yeah, just let them know what happened and that’s it’s a true gift this year.
[lzqks9u] (score 3, diepte 2) I think they even offer gift card?
[lzn4dn0] (score 3, diepte 2) or another grocery store than you use a lot! when i lived in my homecountry, we also had a chain of stores where you can buy groceries and household items in bulk
[lzn4ojj] (score 3, diepte 2) Gift cards for what they do have in your country.
[lzn1sla] (score 3, diepte 0) Really nice of them to ask. Can I ask what sort of work you do (and what the nature of your client contract was)? Maybe you can return the favor: With your found time, you could potentially put those skills to use making genuinely thoughtful or useful gifts for friends and family, who in turn will want to talk about your skills/talents with others. As I’m sure you know, word-of-mouth and referrals can make all the difference in your career fortunes. Best of luck (and safe travels).
[lzn3bg5] (score 3, diepte 0) CASH IS KING 🤑
[lzn6mlb] (score 3, diepte 1 OP) This is a good idea. I’ll do some looking around for the best deals 🙏🏻
[lzqtml6] (score 3, diepte 1) Even better is a real wool blanket, if you can find one affordable or splurge.  Layered atop other blankets… there is no better textile.  Zero dollars on the utility bill.   (Lower half of bed, if you find wool itchy.)
[lzna8x2] (score 3, diepte 0) Gas gift cards. Food gift cards. Pay your heat for a month.
[lznlq86] (score 3, diepte 2) Yes, I use Libby
[lznb21c] (score 3, diepte 0) I’d ask for kitchen/cooking supplies. It’s a lot easier to eat in when you have the proper material
[lznbce5] (score 3, diepte 0) Grocery gift cards
[lznbjiq] (score 3, diepte 0) Subscriptions?
[lzu2tjj] (score 2, diepte 3) It depends on the transportation used most often. In the EU public transit & biking are more prevalent than in the USA.
[lzo3n5l] (score 2, diepte 1) Trader Joe’s isn’t international
[lznl4lo] (score 2, diepte 3) what do you recommend? I'm spending a ton of money on fresh vegetables because I am diabetic!
[lznwn4n] (score 2, diepte 3) I did this for several of my cousins when they graduated high school.  Bought a laundry basket & packed it full of stuff you don’t think about needing when you move in somewhere until you desperately need it!  First aid kits, flashlights, cleaning products, kitchen towels, and so on.  Plus their preferred brands of hygiene products to give them a head start. They all loved them!
[lzpyh6r] (score 2, diepte 4) My children's school does that too! They each received a laptop (small school) but also pizza slicer and a potato peeler, dish soap and sponge, other cleaning and laundry supplies, basically a whole lot of stuff to kit out a small apartment! I thought it was really neat too (this was in 2002,2003 and 2010.) Love that people are still doing this in other parts of the country!
[lzn6kce] (score 2, diepte 1 OP) Advertising what?
[lzn93yo] (score 2, diepte 3 OP) No mate. Just someone struggling to get by at the moment. Thanks though.
[lzn6h92] (score 2, diepte 0) Instant Pot (delivered to your home), air fryer, any small appliance you need that will wear out soon.  Gift cards to your favorite stores so you can buy what you need.
[lzn9skv] (score 2, diepte 2) Adding a souper cube to this-just broke down the turkey and made it into broth and shredded turkey meat. 2 rounds of the bones in the instant pot with some basic veggies and we have enough turkey broth to last probably until next thanksgiving? Going to make it into a shredded turkey soup and freeze it in the souper cube over a few days (popping the cubes out and putting them into gallon ziplock bags to store long term)
[lznl80k] (score 2, diepte 2) An IP allows me to healthy meal prep foods like dried beans, brown rice, soups, stews, and curries, chili, etc.  Pretty much all hands off.  I can freeze the excess in 1-2 meal sized portions, and mix and match with salads and fruit, roasted veggies, some chicken, eggs, —whatever is on sale that week.  So that it saves a lot of money and we go out to eat a whole lot less, as well as eat healthier and for cheaper!
[lznlbts] (score 2, diepte 2) instant pot for the win! but I really want to try an air fryer.
[lznlfhf] (score 2, diepte 1) what app do you use Libby?
[lzncgyy] (score 2, diepte 0) Grocery or gas cards
[lznczfo] (score 2, diepte 0) Groceries, toiletries, cleaning supplies, pet food/supplies (if you have a pet), subscriptions, gas card, oil change card.
(59 reacties met lagere score weggelaten)

