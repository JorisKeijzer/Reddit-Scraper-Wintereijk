# Label-batch batch_0037

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
Schrijf het resultaat naar `batch_0037.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 8olrzk, 1mqifyk, unch1x).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 8olrzk ===
SUBREDDIT: r/Frugal
DATUM: 2018-06-04  SCORE: 1638  REACTIES: 244
TITEL: I know this is probably a no brainer for most of you, but buying new soles for my shoes instead of getting new shoes just saved me well over a hundred dollars.
POST (source_id=post):
Like I said in the title, I'm guessing everybody on here knows this, but it's worth repeating: When a pair of shoes become uncomfortable, see what kind of shape the sole is in and consider buying some nice $30 soles instead of paying $120 on a new pair of shoes. I just extended the life of two solid pairs of shoes. I live in New York so I walk everywhere and I work on my feet so comfortable solid shoes are important. The soles are always first to go. Does anyone know of any other fixes like this that can make a drastic difference?

Edit: A few of you have pointed out, I did make a mistake and confuse soles and insoles. I replaced the insoles on a pair of trail-runners and a pair of work shoes. To fix the soles on the outside part of the shoe you'd need to visit a cobbler and would cost closer to $100, still worth it if you have a nice pair of dress shoes.

Also, I'm getting called out on spending too much on my shoes, but $120 is not that bad if they are comfortable shoes that last. Shoes are one of the few things I'll spend money on, but I guess it may seem like a lot to some and not a lot to others.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e04ef7g] (score 306, diepte 0) In terms of altering/repairing things, my favourite is charity shop (US equivalent would be thrift shop I guess?) suits. 

If you spend half a day searching, I can pretty much guarantee that you’ll find a suit that fits you fairly well for next to no money- I’m 6’3 with wide shoulders, a small waist, and long legs, yet even I can find ones for me pretty easily. 

The real secret is then altering it. Take them to a good tailors (or do it yourself if you’re proficient), and they’ll alter it for an amount similar to what you paid for it. For instance, they might taper the trousers to a more modern fit and take them up to your leg length (another tip, always go long as you can always make them shorter), and they might replace missing suit buttons etc.

I work in a very appearance-driven industry where I am judged on how smart I look on a daily basis, and this has been a life-saver.

My daily wear suit retailed for circa £500. I paid £19 plus a further £25 in alterations, so £44 in total for a suit that is exceptionally high quality and looks like it was made for me. I regularly get more compliments for my attire than colleagues who have spent well over 10x what I spent on their outfits.
[e04glb7] (score 175, diepte 1) While I absolutely agree, it can take some serious effort to not end up with a thick tweed 80's suit with power shoulders... both my blazers were thrifted but it took a long time to find them.
[e04rx9k] (score 116, diepte 1) Here's your TIL. The part of the shoe that holds your heel is called the Quarter, there is an inner and an outer. The heel of a shoe is the part that strikes the ground. 

Make sure you are unlacing your shoes far enough to pull your feet out and push back in without needing to shove them in. Seems like its dumb advice but I used to break the quarters and it wasn't until I figured out they were breaking because I was forcing my feet in and out each time. When I was younger I hated new shoes because they weren't "broken in" and I couldn't kick my shoes off when I came home, it took me more than a decade to realize broken quarters are bad and lead to foot/ankle problems which lead to back problems which lead to cranky.
[e04jzkb] (score 114, diepte 0) Do you guys have any good methods for repairing the backs of your shoes (Inside heel area)? Mine typically get torn up at the same time the soles wear out.
[e04medm] (score 89, diepte 0) I just got a pair of vintage 70s Frye boots that looked pretty beat up and had some loose stitching. Took them to a shoe place that did a full clean/condition/polish and repaired the loose stitching for $18. I'm amazed how few people think to repair their shoes, especially very expensive shoes. I've had high heel taps replaced, soles replaced, and it is always worth it for well made shoes.
[e04vb6t] (score 71, diepte 2) >a thick tweed 80's suit with power shoulders 

You put that one back, that's mine!
[e04lomo] (score 57, diepte 0) Shoe polish.  Use it, on the entire shoe.  For a few dollars, it waterproofs your shoes and extends the life of the leather dramatically.  Used to wear uniform black oxfords at school, and lots of guys had a pair of shoes they never polished, rarely lasted two semesters, but if you kept them polished they'd last all four years with new heels and soles as required.

Bonus: it makes you look smart.
[e04mhjm] (score 48, diepte 1) Look in the thrift stores in the higher end part of town.  I have several quality tailored suits that I've paid less than $100 total each for.
[e04gjnq] (score 40, diepte 2) Not directly relevant no, but I thought it was in the spirit of “repair instead of buying new” ☺️
[e04lic3] (score 35, diepte 1) A good cobbler and do this for you, usually by stitching in extra material to reinforce it.
[e04oiz5] (score 34, diepte 1) This reminded me of a girl I knew in college who would buy a new pair of  Tory Burch boots every Winter because the precious year’s pair were too “torn up”. I wanted to ask her if I could have the old pair....
[e04lquh] (score 32, diepte 0) I have a local shoe repair place that will tell me if a repair is worth it prior to doing it. Try a non-chain. I had a $300 pair of leather dress shoes (you know I didn’t pay that right? :P) so I thought I’d get them repaired. They told me what they would have done and that they didn’t feel right charging me since the fix was so much easier than I thought it would be.

Also to throw it out there... if you have foot, leg, or back problems you probably will replace your insoles often anyway so this OP has a great point.
[e05evr8] (score 32, diepte 2) Having rich wasteful friends who give you their castoffs can be the most frugal decision of all
[e04zcx9] (score 31, diepte 1) Calm down satan
[e055t8m] (score 24, diepte 2) Cobbler here! We use pigskin backliners, we peel up the insole, place the liner underneath and stick and then stitch the new one in before setting the insock back down so that no loose material is around and then trim or fold the excess from the top. I charge £6 a pair.
[e04o5f4] (score 22, diepte 2) OP did ask if anyone had any similar type of fixes. I think this post is a perfectly relevant answer to that question.
[e04l3qy] (score 22, diepte 0) Where is the best place to buy soles.
[e04hf8p] (score 17, diepte 0) The way I walk the outside of my heal wears faster then the rest of the shoe, so I put a layer that Shoe Goo stuff on them and extended the life of my shoes too
[e04zygg] (score 16, diepte 2) If they're really chewed out, you can glue a tiny piece of foam into the hole beforehand. Did this with my skater shoes which are basically designed to get the back of the heel rubbed away.
[e04voaa] (score 16, diepte 2) You should’ve
[e04obzi] (score 15, diepte 1) Also, take pants and shirts in instead of buying small to have them widened... the factory creases when you increase the size width wise look terrible and don’t go away, especially on pants in the rear because now you have a middle seam in your ass crack and a crease on each side of the seam.

Steinmart in the US is a great place to find new pants that are of great quality considering the price, $40 including alteration looks like you have $100 pair of pants.

Costco for the shirts, $20 tops for a solid button down, even the tailor comments on how well they are made considering the price...
[e04ljia] (score 15, diepte 1) Most cobblers have little heel wedges that are much harder than shoe goo or similar and last much longer that they can attach to unevenly worn heels.
[e04roba] (score 15, diepte 2) I have my guy do that as soon as I buy a new pair.  That way the reinforcement wears out, not the heel.
[e056hgp] (score 14, diepte 2) Try to look for thrift shops near wealthy neighborhoods or even the random second shops that are less known. I volunteered at a second hand shop who’s proceeds went to battered women shelters and they got so much amazing, nice, even brand new items in. We would send anything out dated or stained to goodwill because we only kept the nicer things that would sell. I had bags abs bags of really modern and often brand new items donated.
[e04nxr9] (score 14, diepte 1) Meermin, Allen Edmonds, Alden. Great shoe companies. Cost between $200\-600\+. Get sunken metal toe plates installed and heel protectors. Makes shoes last a long time between sole replacements.
[e04vuve] (score 13, diepte 1) No one thrifts like Gaston!
[e04pl2k] (score 13, diepte 1) How do you take your shoes off? I used to always kick my shoes off without unlacing them and the backs were always torn up. I got on the habit of removing them properly and they stay in better shape for much longer now.
[e04sxvh] (score 13, diepte 2) TIL, thanks!
[e04usfk] (score 12, diepte 2) I wash my sneakers in the washing machine, whole.  Toss them in, let them go through a load, set them on the sidewalk to dry.  Always have that new-shoe look!
[e04lk07] (score 11, diepte 1) Singer brand makes iron on repair patches usually used for jeans. They come in different sizes and shapes and can be cut for custom areas, you can iron these into the heals of fabric lined shoes and sneakers. Works well, especially if done with a hot iron. Cheap fix and can be done over and over if they wear through.
[e04qz90] (score 11, diepte 2) Soles and insoles are two different things. 

Unless OP got them mixed up or isn't aware they are different .
[e04xrab] (score 11, diepte 3) Also only use cold wash..hot wash can melt the glue 😭.
[e04lvc8] (score 11, diepte 0) Just out of curiosity, what kind of shoes do you wear and how long does a pair last you?
I bought my last pair at a Marshalls, it cost me almost $40 and lasted around 9months before I got a whole in the sole from being on my feet all the time.
[e04vnmh] (score 11, diepte 1) For some reason we only have one shoe repair guy in the city of Little Rock and he was rude the only time I ever went it.  There is nothing better than a good cobbler
[e056c29] (score 10, diepte 2) >Look in the thrift stores in the higher end part of town.    

Does anyone else have the issue that they simply don't exist there?
[e04s1gv] (score 10, diepte 3) I think OP may have made the same mixup. Insoles might cost $30; a re-soling of a pair of decent shoes is going to be closer to $100.
[e04wvn6] (score 10, diepte 1) The thing I've learned from lurking expensive shoe subs is that people don't wear the same shoes day after day. They rotate a few pairs at least throughout the week. This obviously reduces wear time per shoe but also allows them to air/dry out between wears and apparently letting sweat build up is bad for shoes. Personally I wear a pair of shoes until they are unwearable, throw them away (they are falling apart at that point, completely separating and the soles have holes) and repeat.
[e05czt9] (score 9, diepte 3) Thank you for being a cobbler. Harder and harder to find them around here.
[e04woid] (score 9, diepte 1) On a preventative note, invest in a shoe horn. It'll completely change the way you put on your shoes and seriously helps keep the quarter from wearing out.
[e04pyvt] (score 9, diepte 1) But how long do they last though? If you buy $30 shoes every six months, you spend much more in the long run than if you buy a $300 pair of shoes that lasts you ten years. Frugal doesn’t always mean cheap.
[e04y8i2] (score 9, diepte 0) Do you mean the _soles_ (outside part that touches the ground) or the _insoles_ (inside the shoes, that your socks touch)? Big difference.
[e05f75t] (score 8, diepte 4) It's a trade that's done me well in life I can't complain. I trained between the ages of 18-21, took a break and came back to it. I enjoy the job and as you say, there aren't ma y of us.
[e04su4w] (score 8, diepte 0) Not all shoes can be re-soled.  I've taken four pair to a cobbler and two were rejected because they were glued-on, and not sewn-on soles.

But, overall, smart to look into it.
[e0564hx] (score 7, diepte 1) Cobbler here, glued on is NOT a reason to reject a pair. I do 5 or 6 cemented leather soles a week, as long as you have the right glues it's not a problem at all. And if it's rubber so ling as you have a good s10 primer you can do those just as easy. The only things I can't do are sketchers/echo and trainers because of the foam filler they use in those soles that just disintegrate if I put them even close to my finisher.
[e059inv] (score 6, diepte 3) We don't have a "higher end of town" in my area.....
[e056aub] (score 6, diepte 3) No one finds cheap high quality tops like Gaston!
[e04ql3i] (score 6, diepte 3) Woops, my bad. I need to go to bed. Im thinking insoles and this is a post about soles. Yes they are different
[e04sv4g] (score 6, diepte 1) You would take the shoes into a cobbler or shoe repair place and they will sell you soles. Usually as part of the replacement price (or listed on the same bill), if I'm not mistaken.
[e04m838] (score 6, diepte 0) How long should shoes typically last?
[e0552a7] (score 6, diepte 0) But....My shoes cost $30, and last me a few years.
[e055qb6] (score 5, diepte 3) I'm with you. Shoulder pads make me feel like a boss.
[e055z5w] (score 5, diepte 1) Cobbler here, you're not alone. 90% of heels I get are worn on the other edges (usually into the heel block..) we offer much harder wearing heel top pieces in various styles. Denser rubber, carbon-rubber composites (usually vibram) or 1/4 steels will get you much more use out of your footwear, and don't cost very much at all.
[e055wm8] (score 5, diepte 4) Cobbler here, for a rubber sole over the top of the leather I charge £25.95 with heels, leather is £45 for a half sole (where we "cut" the top half of the sole and replace) or £65 for a through sole which is us essentially rebuilding the entire bottom of your shoe with new heel blocks and top pieces.
[e051sv8] (score 5, diepte 2) Dr. Faustus, surely you must realize “soles” was not a misspelling. When you gathered “1000 soles” (500 pairs of shoes), you had fulfilled your end of the bargain. Now I must fulfill mine...
[e05d62p] (score 5, diepte 3) Yeah. Put them in a wash bag or pillowcase first to stop them getting scuffed by the drum, cool wash, add a little stain removal powder. Works very well. I'm vegan so don't have to worry about ruining leather.
[e04xmdp] (score 5, diepte 3) I've been wearing DMs almost every day for since the 80s. I currently own six pairs. My Made in Vietnam shoes are at least as good as my MIE shoes. Solovairs are just better-marketed DMs, they're not better shoes. To quote an earlier comment I wrote in another sub, since I don't feel like typing the whole thing out again:

>No one ever listens when I say this, but what the hell: The MiE stuff is just hype. I've worn DMs for thirty-odd years. [I currently have a pair of MiE work shoes from the 90s, a pair of MiE brogues from about 2000, a pair of 1461s and three pairs of ten year old Made in Vietnam Ordells that I wear almost every day. The Ordells are great shoes, at least as good as the MiE shoes.](https://i.imgur.com/w1QCbXq.jpg) I also bought and returned a pair of Solovairs, they were overpriced and had stitching flaws.

>The Made in China shoes are not as good. But Made in Vietnam DMs are every bit as good as MiE, and this is from someone who wears DMs virtually every day and has for decades. All the hype about non-MiE shoes is just hype. Solovair are overmarketed, overpriced DMs. They're not better. The MiE DMs are not better than the Made in Vietnam. They're just not.
[e04wp1d] (score 5, diepte 0) Resoling is very expensive in some places. Last time I did it it was 60 dollars for resoling on 100 dollar shoes.
[e04sypw] (score 4, diepte 1) Have you tried inserts? I have an insert for supination in my left shoe and it has fixed that issue.
[e04o4b0] (score 4, diepte 1) Honestly, I just put a strip of the Gorilla brand duct tape (black) over the place it usually wears out. You really can’t feel it, I swear!
[e04l1m2] (score 4, diepte 0) $120 is too much for a Kia
[e04pqhs] (score 4, diepte 2) Are soles and insoles the same thing? I know nothing about shoes.
[e04s69u] (score 4, diepte 1) Even sneakers?
[e04lvcl] (score 4, diepte 0) Where did you get the new soles? Did you go to a cobbler or buy them and attach them yourself?
[e04ohcu] (score 4, diepte 0) Hmm, usually the first place that a shoe fails for me is in the toe box and the front/top part of the shoe. They get scuffed and stitches start to fray. A couple of times, the material joining the top of the shoe to the sole is the part that gives out, so that my toes are poking out of the sides of the shoe.

I usually buy medium-quality shoes at best, so that may be due to the quality of materials, but if anyone has ideas to extend the life of those shoes, I'm all ears. I have yet to have the sole be the first thing that goes.
[e0561n9] (score 4, diepte 1) Cobbler here, if you find you're wearing through the toes abnormally fast then you have a few options. Metal taps are a great way to keep them going if you don't mind the odd click here and there as you walk (nowhere near as frequent as heel pieces though) or you can get a hard wearing resin toe piece put on instead!
[e04v3bt] (score 4, diepte 3) Being frugal isn't always about making enough money to make crappy decisions.
[e04qg8j] (score 4, diepte 0) I got gifted a pair of Salvatore Ferragamo men’s dress shoes ($650 retail)... 12 years later and i still wear them to work a couple times a week
And to weddings etc. I’ve had the heel soles replaced twice and once did a full sole replacement. And I take care of the uppers with proper leather shoe care, they still looks great.

Before getting these I used to get “cheap” $75 pairs that I would wear out in less than a year. You def get what you pay for.
[e04uuax] (score 4, diepte 1) Not sure if that's too much or to low
[e04rmj1] (score 4, diepte 0) Every time I buy a new pair of shoes the first thing I do is take them to my local cobbler and have give glue on a....heel buffer(?). Heel guard? A small piece of rubber covering the back heel.  Then as I walk my shoes don't wear out at the heel (I probate when I walk). The pad does wear down and when it does I take it back and have him replace the rubber. It's about 10 bucks each time.  Since then I've never had to toss a pair because the heel wears out. 

Also- when you buy new shoes, ask if the company sells inserts and shoelaces separately.  Buy a couple pairs.  They fit perfectly your shoes and also extend the life.
[e0569oy] (score 3, diepte 2) This. This is the Real Pro Tip. My personal fav find is my Burberry skirt from Goodwill.
[e05f3s8] (score 3, diepte 4) For there's no man in town quite as thrifty
[e05737o] (score 3, diepte 1) > For instance, they might taper the trousers to a more modern fit and take them up to your leg length

If it's taking up trousers (pants/strides) or a skirt then [hem webbing/hemming tape/fabric tape](https://www.wikihow.com/Hem-a-Pair-of-Pants#Using_Fabric_Tape_sub) can work surprisingly well. This is a white tape that melts when ironed and you use to glue the hem up.
[e04xuu0] (score 3, diepte 2) Huh. Link?
[e04xe40] (score 3, diepte 3) > not the heel.

saves you a trip to shelbyville
[e05ganq] (score 3, diepte 9) I wear steel toed dewalt boots all day myself sir so I know your pain. Memory foam insoles helped a whole lot for me too.
[e05fsj7] (score 3, diepte 9) It's very interesting to have everyone default assume i'm a guy on this site though. Subs like this don't matter but others, the reception can be verrry different.
(150 reacties met lagere score weggelaten)

=== THREAD 1mqifyk ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-08-15  SCORE: 678  REACTIES: 242
TITEL: Quality shoe insoles for work
POST (source_id=post):
I understand that shoe inserts aren't necessarily a buy it for life item I'm just looking for a good quality pair. 

These are somewhere around 6 months or so old, wore than 5 days a week, about 10 hours per day, probably average about 15,000 steps per day, on concrete. 

Looking for a solid pair.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[n8r0z01] (score 938, diepte 0) I'd get another one of those if you found them comfortable. Those look pretty good for that heavy of use for that long.
[n8r25wf] (score 306, diepte 0) So that’s the wear that I would expect on these. I used to work at a running store and we told people to change them by 1000 miles, because even the hard plastic starts to break down.

If we assume that 15K steps for you is 5 miles, that’s 25 miles/week, so about 600 miles in those six months. Add on the fact that you’re standing in them for 10+ hours and yeah, you’ll need to replace them every six months.
[n8ro320] (score 291, diepte 2) -Sun Shoe
[n8r1str] (score 276, diepte 0) Brother 6 months with the amount of movement you do is BIFL
[n8r2gnn] (score 269, diepte 1) “Break the shoe, lest it breaks you.” -Sun Tze’s brother, probably
[n8r1265] (score 86, diepte 0) Red wing shoes, the boot company,  makes insoles too. They're very good. 

To into the store if you can, they have a machine to measure your stride and find the best fitting insole.
[n8r2fqf] (score 57, diepte 0) Superfeet are only expected to last for six months, and same even for custom insoles. I'd say they did you good.
[n8rn5az] (score 56, diepte 1) I just replaced a pair of blue superfeet in bought ~2008. 

The fabric on the heel cups is still in fine shape. The toe beds finally wore thru. I’ve worn them probably 1/3 of the time for the past 17 years. 

Superfeet are worth the money. When I don’t wear decent support my Achilles starts to ache, as well as my knees.

This last pair of superfeet have been with me for my entire adult life. They were there when I lived in Africa. When my sister died. When married my wife. When I…..
[n8r7bgs] (score 51, diepte 1) Superfeet are awesome.
[n8rtp6z] (score 51, diepte 2) Podiatrist here. Second superfeet.
[n8ru43j] (score 45, diepte 1) I will also add that Superfeet is a really awesome local company here in my town (Bellingham, WA) and they do a lot of giving back to the community!
[n8r2d8q] (score 34, diepte 0) These are the best posts. Inadvertently showing us the best product for an expendable device.
[n8rw9a4] (score 32, diepte 1) Yeah, I feel like people in this sub misinterpret the phrase “buy it for life” and take it too literally sometimes
[n8r1c75] (score 32, diepte 0) I would say that 6 months is about the lifespan of shoe insole, but yours look more like what I'd expect after 18 months.

Personally, I swear by the Copperfit "Work Gear Comfort Insole", not because of any copper voodoo but because they are significantly thicker than most other insoles I've found.
[n8r1664] (score 31, diepte 1 OP) That's exactly what I did for these ones, I think it was a good feed store or something very similar.
[n8r773x] (score 26, diepte 1) Red Wing actually sells SuperFeet orthotics like this, just for work. They partnered up a few years back and the Volumental scanner and pressure pad they have will be used to measure everything to recommend one of these orthos. You even have the option of 3D printing them specifically for each foot.
[n8rpr4w] (score 17, diepte 3) Made me laugh--good one. Keeps me on reddit.
[n8r4shl] (score 17, diepte 0) I used to work for SOLE (itsyoursole) and they're fantastic. Great product, great customer service and amazing team. Insoles aren't meant to be buy it for life, but with SOLE I'm a customer for life.
[n8sd8qb] (score 16, diepte 2) You’re missing the fact that you’re really lucky.

People like me buy insoles because our feet stop working and each step is a trip to the pain cave. They also help chronic back, knee, and hip pain. 

But mostly they solve plantar fasciitis and other foot/ankle issues.

One of my favorite comedians describes plantar fasciitis as: “You wake up and your foot hurts, what the fuck is that.”
[n8r2a74] (score 15, diepte 2) Also Rose Anvil sell very thick leather insoles. I like them a lot!
[n8r3kuz] (score 15, diepte 1) Green Superfeet insoles are the best! But yeah, they only last 6-12 months with normal use.
[n8r8k6p] (score 15, diepte 0) Treadlabs. You have to buy the covers (I get mine every two years or so for shoes i wear all day every day) but the orthotic inserts that actually support your feet is covered for life.
[n8s4ngr] (score 14, diepte 2) Not going to do better than super feet for that level of wear!
[n8rs6qz] (score 13, diepte 1) Agreed.  I do about the same amount of steps in my shops and although my Superfeet last a little longer then that paired with wigwam socks and well fitting shoes. There looks to be a lot of friction happening there.
[n8s35nd] (score 13, diepte 4) You need to fit them to your arches.  Superfeet make many different shapes so you just size the arch and then use your old inserts from your shoes as a pattern to trace and cut them for a perfect fit.  In the photo OP put up you can see they have high arches because of the wear pattern
[n8rmyot] (score 10, diepte 2) I did have a pair last me five years, but when I told my podiatrist about it, she gave me a real 😳 look like I should have replaced them long ago. Haha. So idk?
[n8r2ujo] (score 10, diepte 0) Get real orthotics for true BIFL

Go see a foot doctor.
[n8r72l0] (score 10, diepte 0) I use superfeet but switched to Tread Lab ramble and feel more supported. They are equally cheap when you dont have to replace the sole as often and have more arch support with 3 levels you can easy size with their guide. The plastic base I have has been going on 5+ years and I change the top soft sole every 12-18 months depending on use.

https://treadlabs.com/collections/comfort-top-covers
https://a.co/d/1O8VWtP
[n8rsatl] (score 9, diepte 1) I agree. Those look like they handled it pretty good
[n8r8ngf] (score 9, diepte 1) I second them. I've had my pair for over 2 years now, combined with "Darn Tough" socks. My feet are in heaven
[n8r46ju] (score 9, diepte 0) I’ve had good luck with Powerstep Pinnacle Work Insoles. They’re very hard but they’re shaped like a foot so they feel good and last a long time. Fabric doesn’t seem to fall apart as fast as Superfeet
[n8r2i14] (score 8, diepte 0) I’m a mail carrier who walks 5-12 miles a day & I use Protalus insoles, they last longer than the boots do but of course that’s probably around their recommended life span anyway
[n8rbipi] (score 8, diepte 1) I went through 5+ types of insoles, including custom orthotics, while long-distance backpacking. I stuck with TreadLabs and now I have them in all of my shoes.
[n8rcvsp] (score 7, diepte 2) My husband really likes Vionic shoes and inserts for his non Vionic shoes.
[n8r3fxr] (score 7, diepte 0) I can attest to SuperFeet too. I had them in every work boot I’ve had. Great employee-owned company to support as well.
[n8tvgd7] (score 6, diepte 2) They are excellent insoles.
[n8r27ir] (score 6, diepte 0) I’d look into getting custom insoles at a podiatrist. They are expensive but you can get them refurbished. They lasted me a long time and just got them refurbished
[n8r9pfg] (score 6, diepte 2) Can’t speak to refurbishing but mine were $250 in 2020 and $375 in 2024.
[n8r4j1t] (score 6, diepte 1) My podiatrist told me not to waste my money on custom orthotics, just wear green Superfeet. So these are real orthotics. To be fair, the ones OP had are the casual pain relief superfeet, and not the green high arch all purpose superfeet, which last way longer and have a proper hard arch support, but still.
[n8r3557] (score 6, diepte 0) Frankly the bifl insoles are the ones you get at the orthopaedic. They are meant to last and are designed specifically for you.
[n8rpe9x] (score 6, diepte 0) You wore out those superfeet 3 months ago. Go see if runners world will give you a case price.
[n8szjpc] (score 5, diepte 3) Bless you
[n8vimhk] (score 5, diepte 2) I know that it might seem superficial to comment this but I have a knack for good foot/ankle posture and health. Insoles help even myself, because of my high arch. 

I would recommend some ankle/foot mobility and stability exercises if ankle pronation is an issue for you. Not calling you out or anything just offering advice for anyone else looking. Some things as simple as body weight calf raises, ankle stretching shin strengthening can all help. Shin exercises are really easy, just put your heel on a raised surface or even an incline and then lift your toes up. Repeat as many times as you can but don’t go so far as pain. Lower leg muscles are really important for good foot posture. Thanks for coming to my ted talk lol
[n8r9f42] (score 5, diepte 1) Same for custom? The ones my podiatrist make custom for me have typically lasted 5-7 years
[n8r6iq7] (score 5, diepte 1) Yes. The bake and wear system works so well too. Fits my shoe and foot so well.
[n8s439m] (score 5, diepte 1) Love my Treadlabs. I worked at a physical therapy clinic that made custom insoles and these are the ones that look and feel very similar to the custom ones at a fraction of the cost. They helped my plantar fasciitis tremendously.
[n8rwp9d] (score 5, diepte 0) I sell shoes and inserts full time in a full service fitting environment. This is expected wear for insoles. 

People have way too high expectations for something they’re putting their entire body weight on everyday for hours a day.
[pa328ln] (score 5, diepte 0) Ten hour days and about 15,000 steps on concrete are substantial use, so six months doesn’t automatically mean poor quality. If your old pair stayed comfortable until it wore down, another pair is a useful baseline. Compare replacement cost, surface durability and comfort late in a similar shift. Your plan to use two identical shoes is a sensible way to compare inserts without changing everything at once. Let each pair dry between uses and inspect the shoes themselves too. An expensive insert won’t restore a worn out shoe. Stride Soles is a good custom orthotic option to compare, but ask what parts are covered if the top surface wears out under your work schedule.
[n8tgut9] (score 4, diepte 3) Shu
[n8uwa0f] (score 4, diepte 3) [Made by the same guy who came up with superfeet](https://www.zipfit.com/shop/insoles)
[n8vggzt] (score 4, diepte 2) What you're probably missing is years on Earth. Age brings on lots of issues. One the first is typically foot pain. Arches fall, fat in your heals starts diminishing, tendons start tearing, bones spurs start forming.
[n8r4gdi] (score 4, diepte 2) Free with the right coverage.
[n8rjvnj] (score 4, diepte 1) I’ve put a lot of miles in work boots and have had Sole insoles with the poly (not cork) base for longer than a year.
[n8rcsi8] (score 4, diepte 0) I like the orange superfeet. They hold up well enough to lay me about a year. I
[n8rwxpu] (score 4, diepte 1 OP) I've heard that but never really tried. 

I'm a sucker for consistency/uniformity.  

I'll probably end up buying 2 of the same types of shoes, and give 2 different brand of insoles out to test.
[n8sl1f2] (score 3, diepte 2) I was thinking the same thing.  If they are doing that well after that kind of abuse, he probably should stick with that brand.  Six months at that rate of use is awesome for any insole.
[n8r2qv6] (score 3, diepte 1) how much is the cost and cost for refurbishing?
[n8r4358] (score 3, diepte 1) Another vote for Protalus. Also have their Birk-style sandals and love.
[n8r6q41] (score 3, diepte 1) Second for powerstep. 

Like you said, they are hard, but they really support well. For years I came home to foot pain that basically made it so I didn't do anything. Had a podiatrist recommend powerstep. Now I'm still doing 16k plus steps a day and have zero foot pain.
[n8r4eob] (score 3, diepte 0) Those are good ones. When I'm working (not as much as you) mine wear down in around 6 months as well.
Getting expensive insoles is a fool's errand, they will wear down, just by the nature of them being what they are
[n8rri44] (score 3, diepte 1) I have multiple pairs of SOLE insoles (all Active Thick, which describes me well hahaha) for everyday shoes and work boots. My work boots are leather mountaineering boots that have to be bombproof because of the various terrain I'm in for work (mud, bedrock, slopes, fallen trees, sand, gravel, and more) plus I'm kicking a shovel all day. I've had at least a couple pair of SOLEs since 2021 (just looked it up in email) and haven't needed to toss a pair yet. I weigh 280+ lbs and I do not tread lightly.
[n8vcoav] (score 3, diepte 2) THIS 

Just let them mold over time.
[n8r871a] (score 3, diepte 0) I'm a mail carrier and I finally sprung for a pair of upstep custom insoles. I have used the first pair I bought for the last two years and got another pair for my winter boots so I didn't have to take them in and out anymore. Expensive but very worth it.
[n8wd8dr] (score 3, diepte 1) Seconding tread labs. Fantastic inserts.
[n8rc5eh] (score 3, diepte 0) These guys are excellent. They made the prosthetic tail for that dolphin in the “dolphin tail” movie. 

https://hangerclinic.com/find-a-clinic/

They 3d scan your feet then 3d print carbon fiber midsole and cover it multiple layers of different foam and rubber. These are the nicest ones i’ve seen. They cost about $300-500 a pair. 

I get 2 pairs a year from the va but a pair can definitely last years with care. 

Superfeet insoles are just uppity dr schlolz.
[n8rfq6g] (score 3, diepte 0) FYI, even the best insoles should be replaced after 6-8 months if used every day.
[n8rglnq] (score 3, diepte 0) Most manufacturers recommend changing them every 3 to 4 months. So if those lasted 6 and were comfortable why not just stick with them?
[n8rgtcl] (score 3, diepte 0) I like the orange superfeet. Insoles aren’t BIFL, they’re a consumable.
[n8rrcpi] (score 3, diepte 0) OP do you have super rough/textured socks? I've had insoles that I've worn for years that have never worn through like that. Wondering if you might have really thick, large-knit cotton socks or something that might tend to tear these up more.
[nfs7qim] (score 3, diepte 0) Superfeet insoles typically last about 12 months for most, although you’re definitely putting in more steps than the majority of people. Stride Soles are good quality, their insoles generally for years and come with a warranty.
[n8s9ygm] (score 2, diepte 1) What is the point of insoles? I’ve never got them and try to buy shoes that are comfortable enough. Am I missing something?
[n8r5f3l] (score 2, diepte 2) I used to get mine from my podiatrist when I was on my parent’s insurance. They would have been around $200 without insurance. I’m sure it’s different everywhere though.
[n8r81p5] (score 2, diepte 2) So mine were $500 and refurbishing was $150. Unfortunately my insurance at the time only covered insoles if you’re diabetic (but apparently not if you’re born with high arches???) and this was in Atlanta GA so pretty high cost of living. They lasted me 5 years of every day use, long runs, weightlifting, daily walking at work, and long hikes. I’d shop around at different podiatrists in your city and see who has the best price!! I did not do that cause I was 20 and dumb
[n8rmd75] (score 2, diepte 1) Some custom orthotics are made of hard plastic. Basically indestructible
[n8r2nnc] (score 2, diepte 0) I really like Keen's insoles; I use the Utility K-30s whenever I wear out a shoe's provided insole. They have a bunch of different ones for differing arches and uses (Utility, Outdoor) and I think they give good support. 

[https://www.keenfootwear.com/collections/insoles?view=products](https://www.keenfootwear.com/collections/insoles?view=products)
[n8rprzq] (score 2, diepte 1) Yeah I've got keen in my work boots. After trying many different insoles they have been my favorite.
[n8r4u1f] (score 2, diepte 2) I've tried Spenco and Superfeet and a few other brands. Orthotics are the only way to go, all other insoles are comparatively trash.
[n8r3d4k] (score 2, diepte 1 OP) Pinched nerve in your back? Sciatica issues?  That's me
[n8r326y] (score 2, diepte 0) I walk 20K a day on concrete. These things burn out. It’s unfortunate you have to buy a pair often, but if you have found ones that work, stick with them.
[n8rfmi7] (score 2, diepte 1) I was told otherwise, that they should be replaced every 1-2 years.
(223 reacties met lagere score weggelaten)

=== THREAD unch1x ===
SUBREDDIT: r/Frugal
DATUM: 2022-05-11  SCORE: 2832  REACTIES: 232
TITEL: The shoes I’ve had since 8th grade. I’m now 22 and yes, my feet stoped growing when I was 13.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i876thr] (score 888, diepte 0) I always wonder at how little people walk to have shoes last that many years.
[i874hig] (score 448, diepte 0) Take care of your feet. Buy new shoes.
[i87cpl0] (score 279, diepte 1) Little people walk just like us regular folk walk. One step at a time 👍
[i87t2ml] (score 273, diepte 3) He's Swedish. Miles and medical bills means nothing to him.
[i87r69g] (score 258, diepte 1) Either that or they own many shoes and divide the wear between them. Personally, I walk several miles per day and can barely get a year out of a pair of shoes.
[i879b2t] (score 230, diepte 0) you've done your part for sustainability now get new shoes king
[i87bccl] (score 199, diepte 0) Not frugal. Cheap.  Your feet are worth some nice shoes.
[i87ib9q] (score 172, diepte 1 OP) These are my shoes I use during the summer which is pretty short here in Sweden.  My running she’s are dust after 2-3 years.
[i87rf9y] (score 140, diepte 2) That’s crazy long for running shoes…recommendation is every 500 miles or so to swap them out. You can usually go a little further but if you’re a moderate runner that’s still only 8-12 months per pair. Good shoes will save you on medical bills for your feet and knees long into your life
[i88cunf] (score 105, diepte 2) don't go cheap on feet and sleep. get yourself an upgrade my dude.
[i87212r] (score 103, diepte 0) But what do the soles look like?
[i87xobp] (score 76, diepte 1) Definitely. After years of wearing cheap shoes, at age 45 I developed plantar fasciitis, which involved pricey podiatrist visits, shots, and custom-made inserts. Now I don’t bat an eye at spending $100+ on one pair of shoes.
[i878ii0] (score 70, diepte 0) Condolences to your knees, hips and back.
[i887qtg] (score 67, diepte 4) >> So far I haven’t had any health issues with my feet, knees or the body overall whatsoever

Well you are 22 :)

People aren’t joking about 30 hitting like a brick wall if you don’t do maintenance stuff now.
[i88n1py] (score 65, diepte 1) Invest in everything that separates you from the ground. 

Shoes, mattress, tires, chair, etc. They're all worth a premium cost.
[i87v0pd] (score 55, diepte 4) Lol fair but health is still wealth.  Free healthcare won’t stop the pain of arthritis and other joint issues
[i87yqgd] (score 52, diepte 0) Bro please I know you’re just walking on flattened rubber at this point
[i87qcjs] (score 48, diepte 0) [OP's feet](https://i.imgur.com/VI4efKL.gif)
[i87u188] (score 40, diepte 2) If shoes are bad, old shoes are worse.

Edit: typo
[i87f158] (score 40, diepte 0) They may fit because they’re stretched to high heaven but I can’t imagine that it feels good to walk around all day in those
[i884ehj] (score 38, diepte 3 OP) I have no idea how long I run with my shoes but they’re definitely lasting more than 8-10 months but maybe I run less than than a moderate runner. I also cycle a lot which doesn’t really wear on my shoes. So far I haven’t had any health issues with my feet, knees or the body overall whatsoever but I guess I should be precautious with my health.
[i89ywo9] (score 37, diepte 2) So, I was pretty similar for a long time and then I bought a pair of Merrell Moab 2 hiking shoes for a trip in 2018. I just bought a new pair and only because some of the lugs got damaged climbing down Mt. Etna and subsequently (years later) started pulling the sole away from the shoe slightly. The tread is also mostly worn but they aren't quite to slicks yet. 



I'd spend many years buying a $30-$50 pair of shoes every year but for and extra $30-$50 I got a pair that lasted me four times as long.
[i885itk] (score 35, diepte 1 OP) No need to talk about that. 🙈
[i8758a0] (score 34, diepte 0) I (23f) have clothes that still fit me from 5th grade. I’m the same height as I was then and I’m about 5lbs heavier.
[i87zz29] (score 28, diepte 0) These are prison shoes.
[i87vgxm] (score 27, diepte 2) I get where you are coming from, but not everyone can be barefoot 100% time.

There are better options as shoes go for your body, so you need to wear good shoes in order to avoid doing any damage.

&#x200B;

For example, you would not run a marathon in boots or office shoes

&#x200B;

&#x200B;

\*I am talking strictly about shoes, I do understand bar feet are healthier to feet anatomy tho
[i87g5ym] (score 27, diepte 2) You could call it that. The reality is I was just a giant giant child.
[i88flv0] (score 24, diepte 3) I like the saying, "Never cheap out on the things under your feet. Bed, Shoes, and Tires.
[i87i5fu] (score 24, diepte 1) seriously. i don’t drive and walk holes through my soles so easy.
[i88jnvo] (score 24, diepte 5) Seconding this T_T

I'm in my early 30's and it's been lesson after lesson of facing the consequences to my unhealthy behavior.
[i88t05i] (score 22, diepte 5) As a 24 year old with joint pain, I am a little sad that I didn't make it to 30 before getting hit with the bricks.
[i899qar] (score 21, diepte 2) When I'm doing lots of cardio, a pair of running shoes last me 4-5 months if I'm lucky. If I'm in a lazy period and not doing much, my shoes easily last double the length of time if not more.
[i884cz0] (score 21, diepte 0) these shoes are doing you more bad than good at this point.
[i885q8o] (score 17, diepte 4) "Wild people" in other countries don't live very long
[i87mnyr] (score 17, diepte 2) That's still long. I don't think I hike that much, but I still went through 3 pairs of trail runners last year and two pairs of regular shoes.
[i87or3v] (score 16, diepte 0) Shoe stores HATE you.
[i88wp6m] (score 16, diepte 1) Hate him? They don't even know him
[i87hkpc] (score 15, diepte 2) What if they're playing hopscotch?
[i87rf2m] (score 14, diepte 0) Early knee / hip replacement is not frugal
[i88nc36] (score 13, diepte 2) Stepping on a rusty nail is bad for your feet. Dropping something heavy on your feet is bad for them. Dropping a live electrical wire is bad for your feet.

If you're chilling in a pristine field, go wild, go barefoot. But if you go places and especially if you do things, buy good shoes.

If you're in any kind of manual labor, but excellent shoes. Puncture plates, steel toe, electrical insulation, etc.
[i88mb39] (score 12, diepte 2) I used to be like you, wore the same pair of shoes for so long it was insane. I recently bought new shoes and not only do my walks feel 100x better my knee pain is literally completely gone overnight. Get better shoes man, your body will thank you. Don't cheap out on shit that saves your health, it isn't frugal at that point it's just painful.
[i88biuz] (score 12, diepte 2) Because many shoe designers over the past few decades actually take podiatry seriously in the design of their shoes, and your notion that shoes aren't good for your feet is arguably ignorant.
[i89z6uj] (score 12, diepte 2) Because fuck gravity, seriously
[i87n84x] (score 12, diepte 1) I still have my 8th grade graduation dress that still fits me and I’m in my 30s 😂 I think it’s vintage now
[i88xdnn] (score 11, diepte 4) As someone who goes barefoot as much as reasonable, sometimes shoes are just gonna be necessary no matter how toughened the skin gets. Wild people don't have to deal with heavy objects, live electrical wires, multi-inch rusty nails, razor sharp glass or used drug needles.
[i87thmz] (score 10, diepte 0) …..do you use a wheelchair?
[i8897rg] (score 9, diepte 2) Different climates play a huge role. 

There is no way top tier hiking boots (except for those that have stitching) are going to survive 10+ years of heat, humidity and sand. And even stitched ones require new soles.
[i888tod] (score 9, diepte 0) My feet hurt looking at this. 
Get some good shoes or you'll regret it later.
[i87qhj1] (score 8, diepte 2) Elaborate.
[i89xxfu] (score 8, diepte 7) Smoking, drinking, poor posture, poor diet, not taking vitamins, too much screen time, watching porn/masturbating too much. All things I wish I cut out sooner.
[i88n7uh] (score 8, diepte 3) If you can afford multiple pairs of running shoes, each pair lasts longer. Something about the spongy sole having more time to decompress, I think.

I ran every day for four years or so, but since I was lucky enough to have many pairs of good running shoes (my coach gave out lightly used or otherwise unsellable running gear for free to my whole team whenever he could), I could rotate them and didn’t need to retire any for a really long time. I’m just now wearing out my favorite pair, which are eight years old— I ran on them on average 4-8 km (3-5 miles ish) each week for three years and have been using them as my comfy general purpose around town / occasional hiking shoes in the five years since. Running mostly on dirt trails and grass for my first few years of having them may have helped reduce wear too, I think, compared to the shoes I used on pavement running days. They are for sure on their last legs, though. I still like walking around town in them because they’re really comfy and look nicer than my other comfy shoes (why are most running shoes neon colors that look ridiculous with casual outfits?) but they don’t have enough grip to be good hiking shoes anymore, and I wouldn’t plan to run any significant distance in them.
[i88ev2m] (score 8, diepte 0) Some things, are worth paying more for.
[i89k5r4] (score 7, diepte 6) Had unhealthy behaviors for most of my life. Started fixing it in my mid 30s and I feel better and better every year. LPT, start at the bottom and you can only go up.
[i87t28o] (score 7, diepte 2) At first I just assumed you lived in that country that discourages pedestrians
[i8791vp] (score 7, diepte 0) My doc martens I’ve had since I was 13. They’re a size 8.5 or 9, I can’t remember… I’m a size 10 a decade later, they just grew with me
[i88ngp3] (score 6, diepte 4) Everything that separates you from the ground, absolutely.
[i872fno] (score 6, diepte 0) Lucky you. At 18 I wore a size 9. Now I wear a 12.
[i8771tx] (score 6, diepte 1) Lucky!!
[i8a4qfz] (score 6, diepte 3) Can vouch for these shoes, they are amazing!
[i88d0ww] (score 6, diepte 2) My uncle buys a new pair of New Balances every couple years. I think they're his only shoe tbh but he loves going on walks so he must like the brand a lot to buy them for decades. I'm kind of considering a pair myself but not the ~$200 kind he says he gets.
[i87d1ju] (score 6, diepte 0) I really enjoy hearing how people can wear the same shoe for 9 whole years, I appreciate the commitment
[i8a4foh] (score 5, diepte 2) If they're not worth mentioning, then these shoes are not worth keeping.

Do yourself a favor and get a new pair. You can get almost new pairs at thrift stores for super cheap.
[i87vdhn] (score 5, diepte 2) Old shoes are far worse for your feet than new ones
[i87662j] (score 5, diepte 0) I've had a size 13 since I was 12.
[i88h9te] (score 5, diepte 2) Right? Smh
[i89p56k] (score 5, diepte 1) Their feet probably did grow. You can really morph you feet wearing shoes too tight. Millions of dudes wearing cowboy boots tend to wear them too tight. You can really bend your foot around. Hence the whole foot binding thing
[i89l7oy] (score 5, diepte 2) I’ll not look?
[i8abg87] (score 5, diepte 3) It's a shot from a comedy showing two feet with comically crooked toes
[i87tp9l] (score 5, diepte 0) I've had some of my shoes for years.  You guys dogging on OP for fucking up  his back, shoes can be repaired to ensure proper support over the years.

Although...these look like cheap ass Keds but props to the shoes for lasting that long, though I have to wonder how much walking he is actually doing in these lol
[i87ub4c] (score 5, diepte 0) You have an endocrine disorder?
[i87svyz] (score 4, diepte 2) Vill du att jag swishar dig pengar till ett par nya skor? ;) Kan vara bra för dina fötter efter 7 somrar.
[i884v0p] (score 4, diepte 3 OP) Haha, det är lugnt. Kan säga att mina kängor i hemvärnet gör betydligt mer skada på mina fötter än vad dessa skor gör.
[i889qbx] (score 4, diepte 4) Och lukten av dem kan inte vara bättre heller. ^^
Kämpa på och släpp fångarna fria så ofta du får tillfälle!
[i87vxv4] (score 4, diepte 1) I’m still wearing shoes from over 20 years ago.  I have many pairs, so they rotate
[i88a89s] (score 4, diepte 1) Right I’m so impressed. I’m in NYC and after a year my shoes are beat to death even when rotating pairs the soles are destroyed. Started just getting thrifted pairs of what I was buying bc its cheaper and they last the same amount of time pretty much. 

Yes I am taking recommendations for shoes that last! (Casual sneakers if y’all have any magical ones that last!)
[i87sel8] (score 4, diepte 0) You need to go outside and play more. You're shoes are too clean.
[i886viv] (score 4, diepte 0) My feet kept growing until I was 30. I kept buying new expensive gonna last a long time type shoes and my feet kept growing out of them. I was considering getting my growth plates broken or some other surgery to stop them as I am only 5'6" and size 12 which is huge for me as a woman. I was afraid they wouldn't stop growing. They have been stable for several years now so I think I am safe.
[i88dmr3] (score 4, diepte 1) Shoulda been a competitive swimmer.
[i887107] (score 4, diepte 0) I wore a size 8 adult women's in the 4th grade and was only 4'0" everyone called me a hobbit.
[i885vqf] (score 3, diepte 1 OP) Not really sure if I’m lucky. My feet stoped growing like 4 years before my body so my feet are really disproportionate compared to my length.
(146 reacties met lagere score weggelaten)

