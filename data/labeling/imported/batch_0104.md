# Label-batch batch_0104

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
Schrijf het resultaat naar `batch_0104.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1aclm0f, yuurcf, 1x07waq).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1aclm0f ===
SUBREDDIT: r/hiking
DATUM: 2024-01-27  SCORE: 72  REACTIES: 145
TITEL: What insoles do you use and/or would recommend?
POST (source_id=post):
I'm looking for a good set of insoles that will last. I typically do not have issues with my feet but I do like insoles that give arch support.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kjv3j27] (score 125, diepte 0) Depends on your feet honestly, I know it’s a boring answer
[kjv0xj7] (score 56, diepte 0) Honestly I’m on my way to REI to buy my next pair of Superfeet Hike Support because it’s time to replace them. My feet have been so much better on hikes since using them, and have relieved the plantar fasciitis pain / numbness I used to get.
[kjv6tqv] (score 28, diepte 1) This. Go to a good shoe store, try on a bunch of shoes, tell them what feels right feels weird whatever. Have them measure your feet. Walk out with your perfect pair
[kjv3ksc] (score 21, diepte 0) I've tried lots of insoles and always go back to Superfeet (the green ones work best for me). I've even gotten insoles from a chiropodist and a physio and they're so uncomfortable, it's like I can never break them in, they're horrible. Superfeet cost a lot but I've found they're worth it.
[kjvb93u] (score 16, diepte 1) PF sufferer here, thanks for the advice. I have just spent the last seven hours walking around NYC in my Altras and it's not enough.
[kjvb4pn] (score 16, diepte 2) Getting measured is key. I normally wear an 11.5 but because I have a high arch, 10.5 insoles lined up with my arch better. That made a huge difference in comfort. Before I sized down, insoles always felt like there was a bar under my arch and were not comfortable.
[kjw1gr8] (score 13, diepte 2) Alternatively, go to a good podiatrist and have them fit you for custom orthotics. I was in and out in 30 minutes, $100, insoles now fit my individual feet.
[kjv7uwm] (score 12, diepte 0) I like SOLE insoles and use them in my light work boots and my casual boots. Go with the grey low-volume ones if your shoes are already a good fit volume-wise (i.e. if the eyelets are in parallel rows when laced) the red mid-volume ones take up too much space imo. I stand, climb ladders, and do manual work 8-14 hours per day, 4-5 days per week and can't live without them. They are definitely for mid-high arch people though. If you're more flat-footed, go with Super Feet from what I hear. When I worked at an outdoor retailer people swore by Super Feet, especially the custom molded ones for ski boots.

Be prepared to work through some arch pressure/discomfort if you're using insoles for the first time. Going from no support to proper support is an adjustment and can be uncomfortable to painful depending on how long you're standing on them at first.
[kjv35mg] (score 11, diepte 0) Every time I tried to get an OTC insole replacement it just ended up making my feet hurt. I just get replacement insoles from Merrells and get them for all my shoes and replace them about once every two years for my regular shoes and for my hiking boots about once every 6 months to a year.
[kjw44wk] (score 11, diepte 3) Where are you getting $100 customs? Customs usually run $300+ and those are a cheap pair.
[kjwdbbs] (score 11, diepte 4) My local podiatrist. He used a plastic that he can heat-mold to your feet, rather than the old casting method. Did it in house, so I walked right out with them on. The plastic can be remodeled, too, so I can go back in a few years to get them refit without having to buy a new pair.

And I actually lied.  Just checked the mail - they sent me back $47. So they actually only cost me $53!
[kjvhiz7] (score 10, diepte 2) Hot tip: take them out of the box and make sure your feet don’t spill over the sides. Walked into REI thinking I was a B from their size chart, turns out I’m a D to avoid spilling over the sides. Best tip I got from the employee, and definitely saved my flat feet from pain.
[kjvaf75] (score 9, diepte 0) Hot take: OTC in-soles are a scam
[kjw0wad] (score 9, diepte 0) I typically wear my normal barefoot shoes hiking

[Linky link](https://www.lemsshoes.com/collections/lems-barefoot-series/products/mens-primal-zen)

They're really comfy and my feet stopped hurting after hikes when I switched to them

The mesh on top lets in basically everything so I'll probably swap to a pair of boots sold by them that are as close to the shoes as possible as they make my feet feel so awesome
[kjv6quh] (score 8, diepte 1) My othro recommended spenco for extra arch support.
[kjvg019] (score 8, diepte 0) "Up to 500+ miles" means "not more than at least 500 miles, but maybe less." This statement means absolutely nothing.
[kjwxrso] (score 8, diepte 0) Go barefoot. barefoot shoes.  


I think we are not built for shoes with heel drop and all the other things.  


flat feet can be correct by going barefoot, you can train up the arch in your feets again.
[kjxcakx] (score 8, diepte 0) Personally I don’t use any. I wear barefoot/minimalist shoes and boots and during summer I hike in my earth runners sandals which are amazing.
[kjvnnza] (score 6, diepte 1) "Foot strengthening exercises! What you need is stronger feet!" is what I resist posting on every "what shoe/insole will feel like walking on clouds?" post.
[kjvkbcd] (score 6, diepte 0) When I get to a podiatrist a few months ago I asked if she would recommend the superfeet greens and she said yes, but she recommended me Powerstep instead. I’ve made the switch and I won’t go back. They’re built better AND cheaper.
[pa2ju09] (score 6, diepte 0) Try replacements in the boots you actually hike in, with your usual socks. Check heel hold, arch contact and toe room when walking downhill, not just standing on a flat floor. For longevity, compare the base and top cover separately and ask what can be replaced when each wears. Test on shorter hikes before a long trip. A durable insert is only useful if its shape stays comfortable for you. Stride Soles is a good custom orthotic option if you want the contour made for your feet, but since you don’t usually have foot issues, I wouldn’t assume you need to spend more than a comfortable retail insert costs.
[kjvn0ri] (score 5, diepte 1) It also really depends on the shoe/boot. For my zamberlan boots the insoles that zamberlan sells are the only ones that fit the boot well. Do not need insoles sold separately for my hokas.
[kjvro5x] (score 5, diepte 1) Same here, they’re great! I first had a pair of green but they’re quite high volume, they’re worn out now but I kept them for some barefoot moccasins for loafing around. Day to day I use a pair of oranges in my blundstones, and a pair of blues in my Zamberlan hiking boots, but also use a set of their ‘half’ insoles (no forefoot) on a pair of grenson good year welt boots that have a narrow / low volume toe box so not enough space for a full insole. Basically, I love em, and make every shoe better by giving proper arch support and having a secure heel cup.
[kjw2gpc] (score 5, diepte 1) My friend loves to point this out. "Geico can save you up to $XXX or more." it means NOTHING. "up to or more" literally means every number in existence
[kjvva6k] (score 5, diepte 0) I’ve been using Superfeet for over ten years.  They last a really long time.  I have a few pairs because I get tired of changing them out of my shoes all the time.  They make a big difference.
[kjxe6bt] (score 5, diepte 0) Vivobarefoot
[kjvf6ft] (score 4, diepte 1) If you're looking at Superfeet, there is a "quiz" on their website to help you determine which color to try.
[kjv78re] (score 4, diepte 0) If you live by a roadrunner sports they do custom insoles that are specific to your feet. They are a bit pricey though in comparison to store bought ones.
[kjvc1yw] (score 4, diepte 0) Do you have good benefits or heath insurance from work? 
If so go to a podiatrist. They will make you custom orthotics that will last longer and work for you. Generics can be good but they won’t be perfect.
[kjvdns4] (score 4, diepte 0) Research generally does not support the use of custom orthotics over OTC insoles (unless your feet are really jacked). I usually recommend superfeet to my patients but whatever insoles you choose, you should not be able to bend it in half at the arch (IE most Dr. Scholls). If it bends under the force of your hand, imagine what your full body weight will do to it.
[kjvtdb5] (score 4, diepte 0) Cure-Ex insoles have been a game changer. I wear them at work, running, hiking, and when I’m doing high altitude mountaineering in South America. They made it so my lower back pain is so much better.
[kjvxy6d] (score 4, diepte 0) Those green superfeet in the photo are the ones coach in Marion hooked me up with and worked out great. Needed more heel drop in the altras and alleviated all of my Achilles pain
[kjx8r6d] (score 3, diepte 3) can confirm I followed the size chart and ended up returning and getting a larger size
[kjvvs3f] (score 3, diepte 1) When I first got PF and was falling when standing up, I genuinely thought I would be doomed forever. Someone recommended the greens and I’ve never had it since. That was in 2005.
[kjw31pt] (score 3, diepte 3) It’s just really weird how well they work. Like I have tried to run without them and anything over 3 miles and it’s PF all over again. They are costly but worth it. And thank you for the update I would hate to have gone looking for them and then freaked out if I didn’t know they were renamed and couldn’t find them
[kjvt5tp] (score 3, diepte 1) I use those too. They definitely need broken in first, but once I did it really help to alleviate foot pain I was getting from running.
[kjv9dos] (score 3, diepte 0) superfeet light blue are my go-to
[kjvep2m] (score 3, diepte 0) There are good one on AliExpress for 10$ from the 3angni. Most of the other insoles there are shit though.
[kjvh3xd] (score 3, diepte 0) I have very high arches and the Powerstep Green insoles are my fav. I like the blue ones for casual shoes
[kjvh7xj] (score 3, diepte 0) I like super feet but their selection of wide is limited and expensive. You should try sole as well. They have some in store rei. Then go buy from Amazon for better size and thickness selection. I have large volume and wide feet and they sell thin wide plastic for my feet.
[kjvjvlt] (score 3, diepte 0) Game changers by FP Insoles. You pop them in the oven for 5 minutes and then put them in your boots/shoes and it molds around your foot. I use them for wildland firefighting and it indeed was a game jabbed for me.
[kjwf0xu] (score 3, diepte 1) Powerstep are the right way to go for top of the line OTC.  They are significantly better than superfeet.   I get mine off Amazon.
[kjvltqp] (score 3, diepte 0) Dr. Scholl's Heavy Duty. I don't feel much difference between the cheap and the expensive so I go cheap and replace them about once a year.
[kjvmj9w] (score 3, diepte 0) Obsessed with my green superfeet.
[kjvowyh] (score 3, diepte 0) Move game day, they are marketed for basketball but I find them very comfortable and affordable for walking and hiking.
[kjvvazo] (score 3, diepte 0) Superfeet now forever always. Green.
[kjw7clu] (score 3, diepte 0) It all depends on your feet. I use Superfeet Trailblazer insoles because they give me both the support and cushion I need. You might need more firm, less firm, flexible, etc.

Here are some good ones to look into, though. 

Superfeet Green and Trailblazer (the insoles with ridges on the bottom, like the Blue, can cut through GTX liners).

Cadence. 

SOLE Performance. 

Currex. 

Tread Labs.
[kjwa6yi] (score 3, diepte 0) I use super feet green insoles. They were what saved me after developing PF from being too ambitious on an early in the season thru hike.
[kjybztg] (score 3, diepte 1) Only right answer
[n8pavnt] (score 3, diepte 0) As someone who has to be on his feet for about 8 hours each day I have tried everything - from gel socks, to inserts, heel cups and more. Nothing really provided the relief I needed. At best, I was able to get just a little, short-lived relief. Fast forward to getting Stride Soles inserts and my career has literally been saved. I can't remember the last time I was without foot pain and fatigue. With these insoles, I enjoy full support and comfort. They may be more expensive than over-the-counter products but they are well worth it. I had to get a few pairs so I could have one for each shoe. I'm so happy that my days of chronic foot pain are over, thanks to Stride Soles.
[kjw2oui] (score 2, diepte 2) My husband just bought two pairs of those for himself today! They changed the style name to “All-Purpose” now.
[kjvrsqz] (score 2, diepte 1 OP) I didn't realize you can get original replacement insoles for shoes
[m1v9ot6] (score 2, diepte 5) That's absolutely insanely good value. I can't find any custom orthotics for that price in the UK.
[kjw7w43] (score 2, diepte 2) 3 types is way too simplified, and their highest arch is like 4 out of 10  at most in terms of arch height. 

You really need to be able to adjust the arch support forward and backwards to suit most people also.
[kjyhapz] (score 2, diepte 3) This is more important than most people realize.  I have long toes proportional to the length of my feet and most full length insoles just hit me in the wrong spot.  I've had better luck with 3/4 insoles since it is the heel to arch measurement rather than toe to arch.
[kjv5v1r] (score 2, diepte 0) My arches on my right and left foot are both collapsed. I’ve been through a lot of different insoles, but I’ve had the best slept with the ones I buy at The Good Feet Store.
[kjwrf8o] (score 2, diepte 1 OP) I'll try these out. I have mid to high arches so hopefully these will be good. How long does a pair last you? Bought a pair of super feet and really like them but they were damn expensive and only lasted me 3 or 4 months of work (I also climb ladders quite a bit and/or I'm always on my feet).
[kjx2fkf] (score 2, diepte 2) The  "active" line is made of plastic and lasts forever. The "performance" line is made of cork, it molds to your feet but will eventually break down.

"Thick" is obviously stronger than "medium" or "thin".

They are the best for high arches. Buy directly from the Sole website for best selection/shipping/discounts.
[kjycjj5] (score 2, diepte 3 OP) Thanks, I'll look into these more. I did the little questionnaire on their website, they suggested the medium ones
[kjwypmh] (score 2, diepte 1) I have these as well and they extended the life of my merrel Moabs greatly. I dig the cork in them.
[kjv8h04] (score 2, diepte 0) I have a custom one, as I have one foot more flat than the other...a personal one is likely better than some general one
[kjvf3ty] (score 2, diepte 2) Just providing a counterpoint to what Big Insole wants you to think. Unless you go to a podiatrist and get a proper diagnosis, you probably don’t need a $60 insole

But what do I know? Jack shit. Same as you. I’ve hiked the triple crown without insoles. So there’s that
[kjv9kyh] (score 2, diepte 0) Customer made orthotics
[kjx40u8] (score 2, diepte 2) I mean, if they work for you, go for it. Not everyone is the same. Heck, some people dig barefoot running. Maybe you’re someone that doesn’t really need that much support and that’s fine too. If it ain’t broke, don’t fix it. But most people that come to my clinic come because it is broke. Insoles aren’t the answer for everyone.
[kk1qntw] (score 2, diepte 2) It’s not a cushioned insole. It hardens as it molds. Just feels like a shoe. They’re super shock absorbent and super super comfortable. I wear logging boots for work but they don’t support my incredibly high arch. These boots are heavy and entirely made of thick leather. My feet hurt so bad until I got the insoles. 

If you go onto their instagram, I think they test their insoles and a bunch of others by dropping a bowling ball on it.
[kk1qtyr] (score 2, diepte 3) What size boot are you by chance? I have an extra pair I don’t need (that I got for free by the company). Could totally send them over if they’re your size.
[kjyyw1t] (score 2, diepte 1 OP) I didn't know they had a heavy duty pair
[kjvmp57] (score 2, diepte 0) I’ve recently started using the Sidas 3Feet Outdoor Gel insoles (I lost one of my insoles!!) and they are AMAZING! I didn’t want to spend 45€ just on insoles but I’m so glad I did now. Can’t recommend them enough. Never thought good quality insoles would make such a difference
[m80dvhm] (score 2, diepte 1) Did you order the same size as the boots you wear or ordered based on foot lenght?
[m80f4qd] (score 2, diepte 2) IIRC there were no sizes but arch sizes. I went to the Salomon shop and they had a scanner for my feet so based on their scan of my foot arch, they recommended the Low type. The insole has guidelines you can use to cut down to fit smaller shoes.
[kjvtlzi] (score 2, diepte 0) Not a great answer but I got custom inserts due to multiple foot issues. Best money I’ve ever spent.
[kjzaxj9] (score 2, diepte 1 OP) Do you use them with no insoles?
[kjw3a1e] (score 2, diepte 0) Superfeet...it changed my life as a major flatt footer.
[kjw45j0] (score 2, diepte 0) Super Feet
[nnuzh0i] (score 2, diepte 1) Just saw this...do you have any specific thoughts and experience with the Cadence brand?
[nnver5q] (score 2, diepte 3) OK, thanks!
[kjwapmx] (score 2, diepte 0) Another +1 for Superfeet!
[kjwifn9] (score 2, diepte 0) Different insoles for different feet, but you gotta get the hard plastic kind, not the squishy memory foam kind.  So they work as well at the end of the day as the start.
[kjwk5h6] (score 2, diepte 0) Custom is best, Superfeet are decent semi custom insoles.
[kjwrfau] (score 2, diepte 0) Depends on your feet. My Merrels were great out of the box and have lasted years of bi-weekly usage
(114 reacties met lagere score weggelaten)

=== THREAD yuurcf ===
SUBREDDIT: r/solotravel
DATUM: 2022-11-14  SCORE: 30  REACTIES: 121
TITEL: Best shoes for travel?
POST (source_id=post):
I will go to SEA for four months from January. I need to get some new shoes before the trip, which especially support my feet but also hopefully look decent for daily wearing in hot weather with shorts. 

Currently I live in a city and wear leather Blundstone boots almost every day. I also have two pairs of Vans but I found out that these flat-soles shoes were the source of some significant foot pain and knee problems when I wear them often. I don’t want to bring leather boots on my trip so I’m looking for something that’s the best of both worlds (style & function). 

Any ideas?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iwbbv7t] (score 67, diepte 0) Unless I'm doing some really, really hard-core hiking, my go-to is trail runners. Sturdy enough to hike with, but also look enough like sneakers that you can wear them around town and not look crazy.
[iwbc5zu] (score 21, diepte 0) I'd choose a pair of (trail) runners and a pair of sandals.
Almost more important: make sure they're comfortable and worn in! If you can walk a marathon on your vans, they might work for you. But since you still have some time, I'd try to get a pair of trailrunners and sandals.

But I brought running shoes&flipflops and that also worked fine
[iwbdprz] (score 17, diepte 0) I am doing the exact same thing as you and have been doing research for almost the exact same reason.. ultimately the trainers that offer the best support whilst also looking ok will be running trainers - like Nike Infinity flyknit or New Balance 808 , I’m gonna get one of those all in black so don’t look too naff. Obviously not the best for hiking but for general long walks around they should hold up whilst also being comfortable and great support. There’s also Adidas ‘air bouncers’ or something, not sure that name is right but they have a brand with good support.. also Hoka is a good walking shoe brand but I don’t like the look of them much
[iwc608q] (score 14, diepte 1) trail runners for every trip! Love them, can't go overseas without them. They are so versatile and light.
[iwbceq8] (score 12, diepte 0) I went for the foam versions of Birkenstocks - mad comfortable, pretty durable, and waterproof for humidity/rain. Plus you can clean them off in the shower and use them as shower shoes. Win win!
[iwc3af8] (score 11, diepte 1) They do everything ok and nothing perfectly. (Assuming you don't trail run).
[iwd50iw] (score 11, diepte 1) Yes! Have a pair of Altra Lone Peaks that I take everywhere. Usually throw in a pair of sandals as well for casual days.
[iwbe7qs] (score 10, diepte 0) Keen is a brand I like for shoes in my every day life.  I think they have hiking sandals that could be what you’re looking for.  I like my sandals because they cover the toes and have sturdy straps.
[iwbf15i] (score 8, diepte 1) Yeah.  I did 282km in Vietnam with mine.  Perfect.  Well ventilated, dry quickly, don't keep water in.

They're maybe not dressy enough in some people's eyes for every day use, but I've long since given up caring what other people think.
[iwbfmwj] (score 8, diepte 0) I just wanted to tell you my biggest discovery!!!! if you’re ever in East Malaysia, you could get one of those thing called “kampung adidas” which is like 12RM = around $2? Its made of rubber and amazing for climbing and hiking, easy to clean off and while not the best looking, its cheap. 

I bought the shoes there to wear for days when im gonna be sweaty and outdoor, so I don’t have to bring extra shoes lol.
[iwcaa0n] (score 8, diepte 1) I’ll second these, they’re the #1 shoe on the Appalachian Trail, great tread, lightweight, big toe box, great for anyone who plans on hiking on their trip.  They are a little ugly heh. 

I also like Hokas for more city walking type trips.
[iwbiqbj] (score 6, diepte 1) Very good point about being humidity/rain proof. I have the OG Birkinstocks and live in a humid environment. They area always molding on me. It's mad annoying. I've been eyeing their foam version...
[iwbeqy6] (score 6, diepte 1 OP) Ok I will look into the options you mentioned and see which fits my criteria best - thanks!
[iwbv5gm] (score 6, diepte 0) I just traveled Europe with the Altra Lone Peaks. Super comfortable, huge toe box, great for hiking. And I got away with wearing them in bars too. My only gripe is the blue color I got was super easy to get dirty, otherwise nice shoes.

https://www.altrarunning.com/shop/lone-peak-family/men-39%3Bs-lone-peak-6-al0a547l?variationId=242
[iwc34x4] (score 6, diepte 0) Hoka Bondi.

Nurses and retail workers who are on their feet all day wear them. 


I wore them walking on hard concrete floors at work 20,000+ steps per day.

Never had pain in my legs or feet since I bought them.
[iwcmsfu] (score 5, diepte 1) I have a pair of Nike trailrunners I've been using for travel for the last 2 years. They're incredible.
[iwbl6m7] (score 5, diepte 2) Yeah I’ve had that with the OG foot bed… it’s pretty gross haha. The EVA ones are a fair bit cheaper too and you can go a bit mad on colour choices if that’s your vibe
[iwbkuu4] (score 5, diepte 1) 100% agree! My best ever shoe purchase. Super durable, lightweight, waterproof, really good foot and arch support, and good enough to use both everyday and on shorter/moderate difficulty hikes.
[iwbgnnr] (score 5, diepte 3 OP) Weird - I give you an upvote anyway for sharing and engaging!
[iwbuhaa] (score 5, diepte 2) I’m a teacher and we’re not supposed to wear open toed shoes so I wear these.  Comfy for teaching all day as well!!
[iwbg14x] (score 5, diepte 0) Had the same dilemma, went for Birkenstock sandals and since I'm gonna trek in central America for low Salewa trekking shoes - light, soft and supportive will also do the job in civilisation, at least for me.https://www.campz.ch/salewa-wildfire-lederschuhe-damen-M988251.html?vgid=G1440600
[iwbi7pv] (score 5, diepte 0) I wear tevas, but in your case id go with chacos because they have more arch support. I also have a pair of white/brown adidas that are very casual while also being comfy with plenty of arch support for when I need a closed toe shoe.
[iwccyin] (score 5, diepte 0) Teva sandals! I’m currently traveling asia and wear my everyday, so comfy
[iwbdigm] (score 4, diepte 1 OP) Ok thanks
[iwdlgb0] (score 4, diepte 2) Altras are great!
[iwbd7ke] (score 4, diepte 0) Joggers and flip flops or sandals. All you need
[iwbrnu2] (score 4, diepte 1) Both my husband and I bought Keen as water shoes and ended up wearing them everyday. I have the closed toe Rosa and they are so comfortable!
[iwbgxnd] (score 4, diepte 1 OP) I won’t be in Malaysia but I’ll check it out and morel my eyes open for something similar :)
[iwbh5zx] (score 3, diepte 2) Sure. Here you go. https://www.decathlon.in/qr/8500473/-1
[iwblrm1] (score 3, diepte 0) This was a long time issue. Seemed like every two trips I'd buy a new pair trying to find the right ones. I used to bring a reusable grocery bag as my personal item on flights to store my dirty laundry and a separate pair of hiking shoes.

Recently I got sick of carrying that, and I managed to find Adidas terrex ax3 hiking shoes. They don't look like hiking shoes and just look like sneakers but have the same supportive feel of hiking shoes. They were also only like 48$, so far so good.
[iwc0ox6] (score 3, diepte 0) If you're willing to drop some money, I used my air max 95s almost exclusively on my trip, walking around. Feels like I'm walking on clouds.
[iwbdjtd] (score 2, diepte 1 OP) The problem is flip flops don’t typically support my feet enough - or do you have a specific brand in mind?
[iwc909w] (score 2, diepte 2) Try sandals with a very good cushion. I am having some similar to these and walk on average 25k steps everyday in them in SEA. In Bangkok and KL, on the beach, through water, in the rain, everywhere. Going strong in the sixth month now. 

https://www.skechers.de/skechers-gowalk-arch-fit-sandal/229020_BKCC.html
[iwbd8ix] (score 2, diepte 0) If you have Decathlon in your city, go for their walking shoes. I wear them when traveling across SEA. These shoes look good and are very comfortable for long walks. They go well with shorts. I can comfortably walk around 6.2 miles or 10 km a day while wearing them.
[iwbdmit] (score 2, diepte 1 OP) I do have a decathlon here. Could you maybe share a link of the type of shoes you have?
[iwcqqmf] (score 2, diepte 1) The all black is a good idea however I'll caution you against the flyknit as they leak water like a sieve. I had triple black stan smith's that worked well for me as they were easy to wash and fairly water resistant. I've also had pairs in the past so I knew they fit my feet well.
[iwbgly3] (score 2, diepte 1 OP) Great I will check out Keen!
[iwfmeog] (score 2, diepte 1) Another Keen user here, only use them when I go on holiday, so my original pair have lasted me several years, They've great for walking around the ghats of Varanasi which are sometimes very slippy due to all the silt and other muck (cow shit) that you sometimes find yourself stepping in. Had a pair of Crocs previous to those and they were lethal on wet surfaces
[iwbgzh2] (score 2, diepte 1 OP) Great thanks for the idea!
[iwbj2tw] (score 2, diepte 1) A word of warning on Chacos, be sure to wear them before your trip. Every time I wear my Chacos I get blisters the first time. Once I'm acclimated to them, they are fine.
[iwbjny2] (score 2, diepte 2) Agreed, I always have to fiddle with the straps until I get them just right. That is one reason I prefer tevas, the other is because tevas are lighter and flex with your foot.
[iwbmsfm] (score 2, diepte 1) Your remark is exactly what I was going to say so I'll second that. I got Teva's and Chocos but have always ended up just taking Tevas.  The originals. They are low cost and surprisingly hold up well to LOTS of walking.  Wore them all over Thailand, and also took them to Lisbon, Portugal which is super hilly and they were perfectly fine.
[iwbwutp] (score 2, diepte 0) Lems are my go to travel shoe now. They look good for going to restaurants and bars and are also perfect for hiking etc. super comfortable and durable.
[iwdgycu] (score 2, diepte 1) AIR MAX 95 LFG
[iwc3o1s] (score 2, diepte 0) I did it in a pair of vans. They can easily be thrown in the wash if they get a little dirty.
[iwc49aq] (score 2, diepte 0) Some ideas, and imo all of these would look fine with shorts:

For hot weather:

adidas ultraboost (heat rdy if you really need breathability, otherwise the 19 or 20 seems to be preferred), Nike Pegasus Trail

All-around if you need durability and some water resistance:

adidas ultraboost Gore-Tex, Nike Pegasus trail 2 gore-Tex, Nike ACG gore-Tex mountain fly 

If you need more waterproofing and want a higher shoe:
Adidas Terrex Free Hiker Gore-Tex 

If I had to pick just one I’d prob pick one of the Gore-Tex models for the extra durability
[iwc5ks5] (score 2, diepte 0) We're a big fan of [Rothy's](https://rothys.com/collections/mens-shoes). They have both Men's and Woman's shoes in many styles.   
They're stylish. There's little to no break in time. They're washable and they are made from recyclable materials. I wear these everywhere. They are almost exclusively what I bring even if we'll be walking a lot.
[iwcckdd] (score 2, diepte 1) White is the worst choice for travelling; I've made that mistake. They'll get filthy so quick and are harder to clean. Buy dark coloured shoes for travelling is my advice.
[iwe60yk] (score 2, diepte 1) I have had a pair for almost 20 years that are indestructible.
[iwdayac] (score 2, diepte 0) The lightest shoe you can find that's comfortable.

I am serious, weight is the no 1 thing you should think about. Durability is a bit of a non-issue because most shoes will fall apart after long term constant use.

So I'd go with something like Adidas Boston or Adizeros, light, comfy and will last for a while.
[iwed2mt] (score 2, diepte 1) SEA = South East Asia (Thailand, Vietnam, Malaysia, Indonasia, etc..)
[krdoi22] (score 1, diepte 2) are they any good in the rain? worried about that
[krei974] (score 1, diepte 3) Depends on your preference and the climate you're traveling to. If I'm going to a heavy rain region in winter, I'll also bring waterproof boots on vacation. But I don't like the heaviness of waterproof boots, so I almost always bring trailer runners on international trips, rain or shine. They are super light, dry so much faster than leather or suede, and enable you to walk more miles per day (in my opinion). Where are you going?
[krejhmn] (score 1, diepte 4) well its more like my local area had a bunch of rain recently. I might get different shoes later.
[krh3kcb] (score 1, diepte 5) It's all up to your preference. I like walking around in trail runners in the rain because I don't mind my feet getting wet and I love how light and grippy they are.
[krdogym] (score 1, diepte 2) are they any good in the rain?
[krdojop] (score 1, diepte 3) Yeah they’re fine
[iweetks] (score 1, diepte 1) Trail runners seem to be an all-around shoes
[krdofmb] (score 1, diepte 2) are they any good in the rain?
[krdofa8] (score 1, diepte 1) are they any good in the rain?
[iwbfgh1] (score 1, diepte 1) I have a pair of Moses with me and agree. Wearing them about half the time
[iwbha46] (score 1, diepte 3) Sorry, I just assumed that you are a guy. They have these for women as well.
[iwdqusx] (score 1, diepte 1) Idk, my experience with decathlon brand products are mixed, they are ok most of the time but with shoes I would really spend a bit more if you can afford it
[iwbezei] (score 1, diepte 2) Cool someone seems to have down voted me though so don’t take what I say for gospel, just doing research like anybody else but supposedly someone disagrees with my conclusion lol
[iwcrd74] (score 1, diepte 2) Thanks that is good to know. I’m going in the hot season so was more concerned with breathable than waterproof but definitely good to be aware of they’re leaky so thank you!
[iwe96oe] (score 1, diepte 1) I think you'll find the humidity is a lot for enclosed shoes + socks

Everyone will be wearing sandals in SEA, perhaps look into a sturdier one of those
[iwbw8bp] (score 1, diepte 0) Roger Federer ONs- imo best fusion of function and fashion. The premium version has a carbon fiber sole which results in a lightweight, but sturdy shoe. Think new balance comfort with stan smith fashion and nike free run weight
[iwfa30l] (score 1, diepte 1) damn never seen these before, they look great. how would you rate them in terms of all day walking?

edit: there seems to be 4 different variations, which ones are you referring to?
[iwbzgzo] (score 1, diepte 0) I like the arcteryx Norvan shoes.  They’re good for hiking, walking, water, and even a bit formal if necessary.  Pretty comfortable too.
[iwc5yj4] (score 1, diepte 0) I also had vans - brown leather - which were cool to wear to dinner - but too hard on knees and feet for long walks.. so had a pair of black sketchers (don’t laugh, they’re insanely comfortable, with arch support).  I also have a pair of Keen sandals - but didn’t bring those last trip, just they sketchers.
[iwc6u3d] (score 1, diepte 0) I’ve got some really comfy NIKE gortex trail trainers. I also love Birkenstock sandals which are sturdy and have an orthopaedic sole. Can be worn with socks to keep tootsies warm on flights too. Definitely an underrated shoe Birkenstocks.
[iwc70hf] (score 1, diepte 0) I like my Fluevog Derby Swirl boots in Denim suede (I also have the yellow/orange pair, and will probably get the purple ones when I can fit it into my budget). They are extraordinarily comfortable and look good with whatever. I have terrible feet (plus am old, so have less foot padding), and I wore the Fluevogs all over Peru and Ecuador. They looked good and performed well at Macchu Picchu, in the rainforest, and in the cities, with hiking pants, shorts, or skirts.
[iwc93fy] (score 1, diepte 0) Sketchers for me. So many styles.  All lightweight with good support.
[iwcechf] (score 1, diepte 2) I find that for most people, white goes with the almost all clothing and looks good on most people.
[iwcf1qo] (score 1, diepte 3) Until they're different shades of white, grey, black, and brown yeah.
[iwekzg6] (score 1, diepte 2) I’ve had mine for less than 6 months but that’s a positive outlook if they last that long! 😅
[iwekwle] (score 1, diepte 1) Another Tevas fan here. Walking on them is a dream.
[iwcd56w] (score 1, diepte 0) I did Vietnam in high ankle hiking boots. Do not recommend (although they DID save my ankle from getting a *really* bad burn when my motorbike fell onto me while trying to learn how to hop the curb to park). Too heavy and sweaty. 

I have taken a shine to Salomons lately, the regular sneaker shape— the waterproof ones with the drawstring laces. Super easy to break in, not too heavy, good support, quick to get on and off, and as mentioned, waterproof. 

Definitely need a pair of cheap flip flops. Depending on how big your feet are you will want to grab them before you arrive.
[iwcikwt] (score 1, diepte 0) For your sandals, Croc Serena sandals or tulum sandals are super comfortable and supportive and don’t look like crocs
[iwclc91] (score 1, diepte 0) Birkenstocks with a pair of hiking shoes if you need something like that.
(50 reacties met lagere score weggelaten)

=== THREAD 1x07waq ===
SUBREDDIT: r/solotravel
DATUM: 2026-10-07  SCORE: 41  REACTIES: 115
TITEL: Solo traveller struggling to find my feet in Argentina. Any advice?
POST (source_id=post):
I’ve got some time off between jobs and wanted to use it for solo travel, where the only person I needed to answer to was myself.  
I’ve travelled solo in Asia before and loved it, but wanted to push myself somewhere new so chose Argentina.  
I’m in Buenos Aires now and struggling to find my feet a little. The non stop rain isn’t helping, but I also feel more adrift and more conscious of safety and the language barrier than I expected. In Asia I felt swept along by the cities: the food, smells, street life and general sensory overload. So far BA feels less welcoming immediately stimulating to me, and being alone is amplifying that.  
I really want to give Argentina a proper chance but wondering if I should consider other options. I’m heading to Mendoza and then Salta/Jujuy, which I’m excited about but the weather also looks quite bad.  
Would love any advice from locals and solo travellers: did BA take a while to click for you? Are Mendoza and Salta/Jujuy still enjoyable in the rain? I am wondering if I should reroute to get the best out of this time off. Any tips would be so appreciated.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[peiovgj] (score 75, diepte 0) Frankly SEA is backpacking on easy mode. kind of normal to feel more challenged by most of SA. But it is an amazing continent with so much to offer. Certain you’ll find your stride if you stick with it.

Definitely way way better hiking and mountains so take advantage of that as much as you can
[pejbh4v] (score 53, diepte 2) There is a lot of infrastructure in place for tourists in SEA and it's quite cheap compared to South America.
[peka8j2] (score 31, diepte 6) that was a few years ago. not relevant now.

prices have well over doubled in blue dollar USD terms. close to tripled.
[pejiw17] (score 25, diepte 4) Depends where you go. Bolivia, parts of Peru, a lot of Colombia, yes. Argentina, especially Buenos Aires, not so much.
[peipzph] (score 25, diepte 0) Rain definitely isnt helping lol, feels like were in London or something. 

I think one of Bs As strongest points is its cultural activities, which can be hard to locate if you dont know them beforehand

 I recently discovered a site that puts all those events together, you can sort for date and neighborhood: www.otraplanes.com

Hope this helps!!
[pej962q] (score 18, diepte 2) I mean it’s just a well known fact. The “why” is probably hard to exactly explain but to simplify my opinion on it, it’s been very safe and extremely travelled for decades now. This means there are a ton of travelers and a huge infrastructure to support it. It’s also very very affordable so more room for error with your wallet. 

Bangkok is one of the most traveled destinations in the world for example
[pepkclf] (score 16, diepte 0) Hi, I’m from Argentina myself. Not Buenos Aires, but still.

I’ll be blunt and say that it all depends on the assumptions and expectations you’re bringing with you.

If you’re looking for that “everyone is warm and friendly”, “the weather is nice”, “everything is cheap” kind of vibe, or if you’re expecting women to throw themselves at you the way some travellers apparently expect when they come to Latin America, then Argentina probably isn’t for you. I’d keep moving.

People who fall in love with Argentina fall in love with it for what it actually *is*.
[pekh5di] (score 15, diepte 2) English is also your defacto tourism language in South East Asia which makes life easier for a lot of tourists.
[peir3l2] (score 13, diepte 0) Throw on a rain coat and join a walking tour - recommend a city center and Recoleta cemetery tour  
Grab lunch and browse books at the El Ateneo Grand Splendid bookstore  
Palermo is a great neighborhood to wander around - I stayed there, did a great food tour  
If you want a splurge - The Argentine Experience is one of my all-time favorite cooking classes  
Go to a Tango show - I ubered from my hotel  
Visit a museum  
[](https://turismo.buenosaires.gob.ar/en/otros-establecimientos/el-ateneo-grand-splendid-bookstore)
[pem7btu] (score 12, diepte 0) BA, capital city, is like having vacation on New York. Like, it's the worst place to "find your feet".

Go to tourist-approved points (I recommend the south), not the capital city. You won't find things enjoyable for a tourist in the capital.

That, and the capital city is ROBBERY with those prices. Like, really.
[peipwda] (score 9, diepte 0) Sometimes you don't vibe with a place and thats ok. I personally like Buenos Aires a lot but I can see why some don't. The weather as you say probably doesn't help. 

Take into account that Argentinian nightlife starts really late (midnight is early!) so that could be a reason. Go to the theater Colon, the Ateneo bookstore, hang around the parks during the day, go to the universities and check what events there are.
[peiq1vf] (score 9, diepte 0) I did Salta/Jujuy and BA last year. I found the people up north much friendlier and welcoming. You should check out Salta, it's a beautiful and charming small city. Jujuy was fine but pretty rough around the edges if i'm honest.
[pen5bnf] (score 9, diepte 1) I am at a loss. Where are these hostile locals? I feel like everyone is grand here.
[pej1zkr] (score 8, diepte 0) I was in BA for several months and wouldn't go back. I regret not spending more time in other cities. I found it hard to connect with porteños
[peldqrh] (score 8, diepte 1) Montevideo is dead
[pelv4r5] (score 8, diepte 0) Argentine here. Think of Buenos Aires like New York (at least the stereotype?) it's such a big city and a lot of people are borderline hostile. The rest of Argentina do not like people from BsAs a lot.

You are going to love Mendoza. It's such a beautiful city. Also I recommend visiting Córdoba. You can stay in the city (Nueva Córdoba neighborhood is very safe) which has a great night life. Since it has a lot of universities it is a really young city. And it has a lot of really nice places you can go for the day to be close to nature. Such as rivers, hiking trails, etc.

Also, the most beautiful place in Argentina (and the world if you ask me) is Bariloche. It is expensive but god. It's just so pretty. If you like nature, hiking, etc. It's the best. Hitchhiking is specially common there so moving around is really cheap and easy.
[pejerfl] (score 7, diepte 2) I usually really like them, but I HATED the walking tour I took in Buenos Aires. The guide spent the entire hour I was there (before I escaped) talking about how European the argentinians are—how they aren't like other Latinos, blah blah, Italy, Spain...
[pekeeco] (score 7, diepte 0) It's not just you OP.

I went solo a few years ago and BA is one of the few cities I've been to that if I didn't go back, I'd be fine with that. The locals were borderline hostile and it wasn't just an encounter or 2. Almost pretty much across the board and I'm fluent Spanish speaker.

Mendoza was MUCH better but I'm also very much into wines.

Have you spent any time in Uruguay? I felt Montevideo was much better as well.
[pej834h] (score 6, diepte 1) How come? What is making SEA easier to travel?
[peo0lzg] (score 6, diepte 3) Well no. There's no need to use the overly fake style the US usually has, so that's not it.

The excuse I've heard most often is "Buenos Aires is a big city." blah blah. Sure it's not a country bumpkin town, but the locals are a lot friendlier in London, Tokyo, Mexico City, Paris, Madrid, Santiago, Berlin, Bogota, Hong Kong, Lisbon and Porto by comparison. 

Hell, even the locals in Beijing despite the language barrier were friendly. None of these cities are small.

The attitude I got in Buenos Aires as a whole was one of "why are you here. why are you bothering me. go away", which made it very easy to NOT spend any money.

Now Mendoza, was very different. People there didn't come across as wanting to kill you (not in the literal sense of course) for asking a simple question.

I'm not going to say that I ever felt unsafe in Buenos Aires, but it's certainly not welcoming.
[peo4tjm] (score 6, diepte 5) If you're in the business of hospitality and don't have the demeanour for it, maybe you need to change careers?

Like going into a shop and everything is priced, except for the one item hence needing to ask the price. Sales staff made it seem like you were demanding their kidney. Sorry I disturbed from playing around on your phone in an empty store. 🙄
[peme8a4] (score 5, diepte 1) The Argentine Experience was the perfect way to start my mostly solo trip in Argentina! Absolutely worth it for the welcoming vibe and one of the best meals I had on my trip. I ended up buying a mate cup from them too.
[pejg1k1] (score 4, diepte 0) I loved walking around BA in the rain lol. It feels relaxing to me and everything is less crowded. I would try a food spot, coffee, site/ people watch and then go to bars and I loved it. I also found everyone super friendly and helpful. Got lots of local recommendations instead of the tourist stuff
[pengwdw] (score 4, diepte 2) Everywhere ? Especially taxi drivers are outright bullies.
[peqygfc] (score 4, diepte 3) Had an older taxi driver go the wrong neighborhood, told him it was not what I said, and then go on and on about how right he was when I corrected him. Meter was running the whole time, so it’s not like he wasn’t getting paid for his error. I kept telling him he would get paid and to shut his mouth, over and over while he complained like grandpa Simpson. 

When he finally dropped me off he admitted he got it wrong and offered for me to pay less. I thanked him and paid the meter price.
[pekh665] (score 4, diepte 0) I skipped Argentina for that reason. Just left Buones Aires on to Brazil.

I did not feel too welcomed there. And the price of everything just seemed extortionate. 

It was hard to integrate, the backpacking community is really spread out across South America. But where I've noticed it the most is Colombia, Peru and Bolivia more SEA vibes. 

Chile was fine, Argetinia so skipable If your from Europe, same difference.
[peqzb6f] (score 4, diepte 1) That bad monetary policy has been around for decades. Blaming a single president is ignoring the context that led up to his inauguration.
[peit0w9] (score 3, diepte 1) Yes free walking tours are a great idea, this one was really good https://www.guruwalk.com/es/gurus/9u8ny1dxymfldcgmiw28
[pejnhod] (score 3, diepte 0) I felt the same way in BA.  Way less tourists than SEA, so most people you encounter are going about their daily lives.  Add difficult to understand Spanish, and it can get very lonely.  

2 choices: become comfortable with being by yourself, or find a new place.  If you choose to stay, sign up for walking tours and bicycle tours.  These offer a low cost way to see the city, speak your native language, and meet other tourists.  If you decide to move to a new place in SA, consider Peru.  Lovely peaceful people and indigenous culture; slow Spanish speakers and much more English in the many tourist areas; and unbelievably beautiful terrain in the mountains.
[peotnl4] (score 3, diepte 3) I lived 26 years in Córdoba and now 7 years in Buenos Aires (in a working class neighbourhood). Buenos Aires is A LOT safer.

I agree that both places are safe for Latin America, though!!

edit: also agree that OP needs to visit Bariloche! Beautiful place
[pfdp4lo] (score 3, diepte 1) *La ciudad de la furia*
[per5m9v] (score 3, diepte 0) lol i live in buenos aires and yeah its been rainy

there are a lot of beautiful things in buenos aires, but other commenters are right that you have to change your expectations of it. i love it because it's so unique and full of life to me. what have you done in buenos aires so far/where have you been?
[peipji3] (score 2, diepte 1 OP) Thank you ❤️
[penizwz] (score 2, diepte 1 OP) Thank you!!
[peiqbwy] (score 2, diepte 0) I've not been to Argentina, but have Chile & Colombia, so can give some advice. 

All of my travels had predominantly been in Europe, and then a bit in Asia, before heading to South America for the first time in 2024. It's a very different experience, the language barrier probably the biggest challenge for me personally. It took me a couple of days in Santiago, to get comfortable & start enjoying my trip - I had actually after the first day, had thoughts of getting out & flying somewhere familiar, it was just so different, confronting, making me feel super anxious. 

Try & do some activities you're familiar & comfortable doing, even if that's something simple like going to a few cafes, bars, hikes etc.. 

Stick at it.
[peohtpl] (score 2, diepte 4) Yes, but those were very isolated experiences. Overall, I really liked Argentina; the people are wonderful.
[pemuroe] (score 2, diepte 3) Not sure if they have a special NA price/option, but I remember the food more than anything else!
[peo7pl0] (score 2, diepte 3) I'm pretty sure someone at our table didn't drink and they had soda or something else. There are wine pairings for the meals, but there is SO MUCH FOOD and the experience is totally worth it for the food alone. Think someone also had some food allergies and they were able to work with that. Only people I would not recommend this for is if you don't eat meat.  
  
I had a great group at my table - mix of couples, friends, and some solo travelers.  
  
Don't eat lunch before you go.   
  
They let us take the leftover dessert home with us.
[pej033h] (score 2, diepte 1) *Japanese garden
[pej25qj] (score 2, diepte 0) i struggled in BA and im a seasoned traveler. only thing that changed things was meeting other women my age at the hostels. i found the city overwhelming and ive been all over europe and SA alone
[pejdkbq] (score 2, diepte 0) I felt somewhat lonely in BsAs (didn't stay at a hostel) but going to Mundolingo was a lot of fun for socializing. Wish I'd gone clubbing but managed to get a cold on the weekend I was there.
[peqf3du] (score 2, diepte 1) When you just accept the rain and accept you'll be wet it suddenly feels a lot better indeed
[pejzu9i] (score 2, diepte 0) I was in Mendoza for a month and loved it. Went hiking a lot, worked remotely. Met some cool people
[pelkikk] (score 2, diepte 2) Quieter yes, but the locals aren't as hostile and it's an easy day trip (or a few more) from Buenos Aires.
[pem7l9w] (score 2, diepte 1) Going for vacation to Buenos Aires is the problem, imho. If you give it a next shot try the south!
[pel5i25] (score 2, diepte 0) I am originally from Buenos Aires, living in the Netherlands for the last 7 years. I really liked it during my University years, the night life (starts at midnight, so yeah yo have to be on the young side to enjoy it). I don't enjoy it anymore but I go every year to visit family (and enjoy the sunshine during the European winter).
People is more rude than it used to be, it feels like when I go to the US and everybody is MAGA/anti-MAGA. And the best thing are concerts, cultural activities. If you are from Europe, it feels like a city from Southern Europe like Madrid or Naples. And yeah, it is currently super expensive, I stay there for some months so I bring olive oil and stuff like that to save some money because prices are way higher than in the Netherlands. But steaks are great, but clearly not a bargain anymore (it is cultural to eat steak regularly). But Buenos Aires could be the base for exploring really nice places... lime Mendoza and the wine region, and I just love Patagonia... cities like Bariloche, San Martin de los Andes, Esquel, Puerto Madryn, Ushuaia and El Calafate... because they are the gateway for amazing nature, but yeah, it is very expensive. To give you an idea, while I was in Buenos Aires last year in March it was cheaper to do a 2 week vacation in New Zealand (both islands) than spending that money in Bariloche for the same amount of time.
[peyayhz] (score 2, diepte 4) Yea, I’d agree. I lived in Cordoba for years. Nuevo Cordoba can be fun if you find your group and like going out and partying, but it’s very university town esque. I also feel much safer in Belgrano where I live now.
[peq41ng] (score 2, diepte 1) They have not mentioned anything about prices so I don’t know why you are so focused on this?
[peojkoq] (score 2, diepte 0) is it maybe just a bit of culture shock and you just need to give it time to adjust? Grab an umbrella, take an uber to a few places you want to visit so you haven't got to figure out getting from place to place safely and just take it all in, I haven't yet visited Argentina but have spent a tonne of time in Mexico etc as well as Asia, yes most places are not how south East Asia is, but if you have your wits about you, look confident, research areas to avoid etc then for the most part then you should be fine.
[pephr95] (score 2, diepte 0) I’m porteño and every foreigner who I meet here loves the city and the vibes, maybe it’s just not your kind of place to “find your feet”
[peqcztb] (score 2, diepte 0) Argentina is going through an economic crisis right now. A huge part of the population is living hand to mouth as prices have gone through the roof due to the current president's monetary policy. Tourism is way down due to crazy high prices. It's not a good time to visit from an value stand point and it's not a good time to visit from a social stand point. 

All that said, if you manage to get past your preconceived tourist ideas, you'll get to see a side of Argentina most tourists are too blind to see. The choice is yours.
[pexsjk2] (score 1, diepte 2) Everything is affordable, English is more spoken in hospitality/service, it's a popular destination for tourism & has tourism infrastructure and there a loads of Western backpackers. In Latin America, especially the southern cone, if you aren't at least A2 Spanish and feel confident/comfortable speaking the language it will be very difficult.
[penj21x] (score 1, diepte 1 OP) Appreciate that thank you!
[pekx4cc] (score 1, diepte 1 OP) Thank you so much. Appreciate this 🙏
[pej0aow] (score 1, diepte 2) Thanks for the correction, last time I was there was in 2011 so my memory failed me a bit.
[pej7n8c] (score 1, diepte 0) What district are you in?
[peqheva] (score 1, diepte 2) My waterproof pants and jacket kept me dry and made things easier
[pejiw1i] (score 1, diepte 0) I spent a week solo in BA last May. Didn’t speak to a single soul. I did theatre colon tour and watched tango show. I enjoyed ‘me time’ at a different cafe every day. Feels like Paris to be honest. Roaming around and walking aimlessly is my go to activity. Saturday was chaos with street shows and busking all that. It was fun
[pejlp3t] (score 1, diepte 0) Sign up for some tours? Usually helps me when I’m desperate for something to do
[peqeexf] (score 1, diepte 3) Taxi drivers are bullies everywhere I've been in Latin America, I'd never take one when I can just take an Uber for cheaper or similar price
[penjitx] (score 1, diepte 2) They want us Argentines to be super cheery and helpful and servicial all the time like we're not dividing our day into protesting the government and going to work lol. When we're not that's when we are hostile
(59 reacties met lagere score weggelaten)

