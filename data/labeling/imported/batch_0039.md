# Label-batch batch_0039

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
Schrijf het resultaat naar `batch_0039.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 8au70o, 18olz18, 1k2vtgb).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 8au70o ===
SUBREDDIT: r/Frugal
DATUM: 2018-04-08  SCORE: 1937  REACTIES: 198
TITEL: Have small feet? Youth sizes are usually 15-25% cheaper for the exact same shoe.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dx1oq4v] (score 698, diepte 0) Don't recommend this for athletic shoes, the quality is much lower in my experience.
[dx1ww8c] (score 215, diepte 1) I used to work weekends at a shoe store for a few years, and made it a point of understanding customer needs.

Kids converse in sizes that fit adults are generally built the same way, and they have more radical styling. Also, more of the larger converse kids sizes end up in the clearance rack. Some Nike athletics change build quality after kids size 4 to be of a higher quality, similar to the adult quality, but not the same. The adult quality ones are always best.

However, girls dress shoes rarely go above a size 5 for this reason - they expect you to jump up to Womens at that point.

But yea, a majority of other brands are built very shitty for kids. Pull up the insoles every time to confirm it. I've seen some kids shoes with fucking cardboard in them.
[dx1l8im] (score 136, diepte 0) Clothes too, I'm a kids L/XL and can often find some cute stuff at target.
[dx1vodh] (score 87, diepte 1) This 100%! I sold shoes (sports specific) for years and even the same model from the same brand between women's and kids for example would have significantly poorer materials and often much less structure (no torsion control for example) so you get what you pay for.
[dx1khxe] (score 84, diepte 0) Can confirm, SO did this to get cheaper slippers at LL Bean.
[dx1q2ox] (score 84, diepte 1) I'm a 5'7", 165 lb dude and I can wear kids XL.
[dx1uv1m] (score 62, diepte 1) This is true for all styles of shoe
[dx1y3b5] (score 50, diepte 3) From my experience, if you have wider feet, buy boy's shoes. If you have narrower, women's.

I have wide feet, and wear a women's size 6.5-7.5 depending on the shoe, but they are often ill-fitting because I have, like, duck feet, haha. When I buy the same shoes in a boy's size 4-5, they fit better, because they are cut wider through the toe box.
[dx1mvhv] (score 47, diepte 2) I was just sad they didn't have a children's equivalent of a men's 12.  There has to be some giant-footed kid somewhere, right?
[dx1kabu] (score 44, diepte 0) You don't pay tax on kids shoes, at least in the UK you don't. Sometimes the kids shoes are less than half the price, it's crazy.
[dx1rseb] (score 35, diepte 0) For some reason I'm a 9 in women's shoes and a 6 in kids shoes.
[dx20ow0] (score 31, diepte 2) Is it because kids generally fly through shoe sizes quickly?
[dx1m37f] (score 30, diepte 1) I did this with LLBean duck boots 4 years ago. Kids sizes were much much cheaper and came in better colors IMO.
[dx21ded] (score 29, diepte 3) Yeah and you've never seen kids shred shoes. Honestly, you'll be lucky if most school kids shoes last 2-3 months (for kids).
[dx1xt7f] (score 28, diepte 2) I'm a 6 in boy/men Nike sneakers (8 women), is if still worth buying them in boys/men?
[dx1uii8] (score 28, diepte 0) My friend needed mary Janes with no heel for an outdoor square dance themed wedding where she was a bridesmaid. I was so jealous that she can shop the kids section.
[dx1qpzj] (score 27, diepte 1) The kids slippers are cheaper, but they aren’t made of the same materials. I have kids LLBean slippers and they’re fake fur inside, not real shearling. The suede is still durable, I’ve work them for seven years now with no sign of stopping, but if I bought a pair now I’d go for adults. Wool is just a great material.
[dx1rrm3] (score 26, diepte 4) Kids are getting larger.
[dx24zw6] (score 23, diepte 1) Youth sizes are equivalent to US womens size minus 2. So a women's 7 would wear a youth 5 for example. Maybe the conversation is a bit flexible in your case though, plus there's always variance from shoe to shoe.
[dx1s4fw] (score 22, diepte 0) I wear a size 6 in women's. I can purchase the exact same style shoes in the youth department for sometimes half the cost.
[dx1z9zz] (score 22, diepte 0) You're not really getting the same thing though. Jordans, Nike's, Ultraboosts, they are doesn't have the same quality as their adult shoes.
[dx1v7de] (score 21, diepte 0) I bought kids Hunter rain boots for a lot less than the adult version. And they’re a bit shorter, so they’re easier to drive in than the adult boots.
[dx2amby] (score 20, diepte 1) Yeah but I got hot pink Air Force Ones for $20.
[dx1ybe2] (score 19, diepte 3) If you're a woman, I'd be raiding the men's clearance section for size 6's hardcore, especially at places like DSW that might have a few dozen pairs in your size. It's always full of great buys at all of the big chains near me. Of course, this all depends on the width of your foot and if you feel comfortable in a D width shoe. Where I worked (Shoe Carnival) we were frequently transferring hard to find sizes out to other stores that would actually sell them, so your mileage may vary.

Size 7 and 8 in Womens tends to go fast, so if you already want a D width, then yea do the men's shoes. I had about 15% of women do just that when coming in. They loved the idea of getting some white shoes with a little bit of color, instead of always being pink and aqua colored for athletics like most are now.
[dx1y7c3] (score 19, diepte 1) When I was buying running sneakers (local store) the guy explained to me that while I would fit into kids' shoes, they don't have the support/cushion needed for most women.  This might be moot if you're into the barefoot type of shoes but it seemed to make sense to me, and the shoes I did buy were awesome.

But converse, slippers, trendy shoes that might not need to last a year, or other things that won't get a ton of hard use?  I definitely buy kids when I can!
[dx1wz1k] (score 19, diepte 0) You mean my male size 7 feet can have velcro again! A dream come true!
[dx20pdj] (score 19, diepte 0) Be careful with shoes. I got Plantar fasciitis because of my shoes... The three months of physical therapy visits far exceeded any savings from cheap shoes. Never mind the excruciating pain.

Now I carefully researched shoes before buying them.
[dx1uttb] (score 18, diepte 0) Unfortunately I have the worst size for anyone. I'm a size 7.5. Kids shoes stop at 7 and adults start at 8. Like yes shoe companies everyone just magically increases one size!

So I usually shop at vans cause it's not sized by adults or kids. Plus they're cheap and comfortable.
[dx1oj3r] (score 16, diepte 1) What are you in normal sizes? I'm a small and sometimes an extra small.
[dx28zmh] (score 16, diepte 4) Kids shred shoes

Let's lower the quality then!

And so the cycle begins
[dx276dj] (score 15, diepte 4) When I was a kid getting new shoes was once at the start of the school year. Have they gotten that bad?
[dx1y3lu] (score 13, diepte 1) I worked in sales and manufacturing for a MAJOR company that owns multiple top tiered shoes. 

Youth shoes and adults are NOT the same, you are right. Children’s feet grow at such a high rate of speed, they want value over quality (or long term longevity) so the materials are much lower in quality.
[dx1xhsp] (score 12, diepte 3) I was a giant-footed kid. Jumped up to adult sizes around 8 or 9 and by 11 was wearing 11's. Kids at school made fun of me because they thought I was wearing shoes way too big for me for some reason. Right, my parents bought me $50 shoes that were massive on me for no reason.
[dx1yjy5] (score 12, diepte 4) I bought some little boys knit adidas recently, and they've already got a hole. I have a similar pair in  womens and they're twice as old, but in way better shape.
[dx1yl57] (score 12, diepte 5) Interesting-my boy's adidas have been indestructible, but my lady ones failed me. 

edit: could be a width factor in my case b/c of fat-ass feets.
[dx1ypi4] (score 12, diepte 4) DUDE. IF ONLY. My stubby feet are apparently tater tot sized and relegated to the kid's section, haha.
[dx1siv5] (score 11, diepte 0) Can confirm. Work in retail. Youth sizes are wildly cheaper
[dx1zzr9] (score 11, diepte 0) I used to look for shoes for my grandmother.  She wore size 2 in children's, and it was really hard to find something without big bird on it.
[dx2atk8] (score 9, diepte 2) We're the same size, I need to try this. Does it fit more like a regular small or medium? I'm always wishing there was something in between.
[dx1tshv] (score 8, diepte 0) My feet are just a bit too big for kids shoes, but I do fit the XL kids socks.  I was getting annoyed with adult socks, they supposedly fit size 7.5 to 12 or something like that.  Sure they fit, but the gray heel ends up halfway up my calf.  I think with kids sizes, I get 2 more pairs for the same price, or something like that too.
[dx1utbe] (score 8, diepte 0) Good tip! I wear a size 7 mens..although I usually get a good deal at Ross or a similar clearance shoe section as it isn't a real popular size.
[dx1ww3l] (score 8, diepte 0) It works really well with things like Uggs which have similar styles for kids and adults. I'm an 8 in women's but a 6 in kids. The shafts are a little narrower and not as tall but good quality.
[dx1xngb] (score 8, diepte 1) They make velcro shoes for adults. I had a pair a couple years ago, size 13.
[dx2anly] (score 8, diepte 1) What should one research about shoes to prevent that?
[dx21okp] (score 7, diepte 2) I paid $40 less for my Uggs (same colour that I wanted) since I fit in to a large kids'.
[dx1vyti] (score 7, diepte 0) I get kids converse and never seen a difference in quality from regular. I've also bought kids Nikes that I used for running for almost 6 months until my puppy ate them 😥
[dx24lgh] (score 7, diepte 1) I wear a size 2.5 kids and it seems like within the last 6 or 7 years there has been an increase in kids shoes looking like adult ones.  I can easily find kids shoes with heels now even.  Not sure if its really a good thing, but now im not limited to rainbow bright light up shoes.  (Who am i kidding, I would rock those)
[dx1ouz0] (score 6, diepte 2) Like a small/medium in ladies tops (I have a small chest) and in pants I'm currently an 8. More like XL in kids.
[dx1oxi5] (score 6, diepte 3) I'm barely a b cup, and wear size 4 pants. But this surprises me honestly
[dx1rt2w] (score 6, diepte 5) This is very true. Which is sad
[dx1ome2] (score 6, diepte 1) I do this with shirts/sweaters! As a woman, boys' pants don't really fit right (except for sweats), but the shirts look half decent.
[dx1pys5] (score 6, diepte 2) I've found it works well with long underwear - I can get stuff that's warm and sturdy.  And it's stretchy and meant to be worn tight so you don't have to worry as much about fit.
[dx2giuh] (score 6, diepte 4) OMG thank you! I wear a 6.5W because, like you, my feet are basically squares. So hard to find in women's. They seem to think only people who wear size 9+ can also have wide feet. I'll have to shop the boy's section next time.
[dx1v17x] (score 6, diepte 0) I've been picked at for doing this, but I have saved tons of money over the years by purchasing children shoes.
[dx2drt2] (score 6, diepte 1) I’ve had great luck with uggs. A 6/6.5 in womens is a 4 in Kid uggs. And Zappos is a great place to buy clearance kind said uggs
[dx2fdds] (score 6, diepte 0) The same is true for clothes. I’m a petite dude (5”6” about 135) with a soccer player type of build, and have found that some boys clothes fit better and cost a fraction of their same-sized adult counterparts.
    
For example, At Nordstrom Rack, I bought Lucky jeans in size 18-20 (boys) instead of 28-30 mens, and the price was $24.99 vs $69.99...for the same brand with the same fit and quality. I’ve found awesome deals on shirts, jackets, etc. as well. I have relatively big feet for a short dude though, so I can’t comment on youth vs. adult shoe quality.
    
On another positive note, my toddler son and I will probably be able to share clothes soon, because he’s growing like a weed, so I’ve got that going for me.
[dx2a5os] (score 5, diepte 1) In many states in the US, you don't pay tax on any clothing, including shoes. At least not until you get up to some really high price limit.
[dx292hq] (score 5, diepte 4) Could it be because the quality of them is lower?
[dx2bn7e] (score 5, diepte 4) I have to get my son a new pair of New Balance around every 6-8 months so you'd be surprised. He's just 4 now. His shoes are always ratty after the second week. We rotate between two pairs (and if it's winter we have the snow boots with a sneaker base).. I know my experience may not be the norm but his feet just don't grow as fast as you are claiming. I get his foot size rechecked every 3 months.
[dx1xi1g] (score 5, diepte 1) Bearpaw!
[dx2dsuz] (score 5, diepte 1) Adults can be longer, though same width.
[dx33vqb] (score 5, diepte 1) WTF?!

Shoes is shoes, you wears what fits!  

Little old lady here, with child-size feet, who wears Converse and DMs and Clarks!  Along with jeans and hoodies and t-shirts btw!
[dx2ausm] (score 5, diepte 0) One of the few perks of being a small dude. I get to buy youth XL football jerseys for a lot cheaper then men's S lol
[dx2o51c] (score 5, diepte 0) A counterexample-- I always found the exorbitant price of tiny tiny name brand sneakers to be funny. It's a four inch long shoe and like $40. Gotta deck yo damn kids out.
[dx2ovn8] (score 5, diepte 0) What's the youth equivalent for men's size 13?
[dx2kzea] (score 4, diepte 3) More like a medium. Just know that these clothes were designed for kids who haven't hit puberty yet so they may be tight in a few places.

Please try the clothes on prior to buying.
[dx2hr2q] (score 4, diepte 2) How else could you find a Pokémon and Minecraft shirt for yourself.
[dx2c95i] (score 4, diepte 2) It's also moot if you have custom inserts you're transferring into the shoe. Then you're just looking for a quality shell pretty much.

Which may be the way to go for some. It took me like forever to find a pair of shoes that supported my feet well. But I would go thru shoes so fast i would have to buy 2 pairs when I found something.

Now with custom inserts I literally can just go to Walmart and buy something and not worry about it. 

Matter of fact the aria brand at Walmart has been holding up better than what I used to buy
[dx2jta5] (score 4, diepte 1) Me too! Currently wearing a boy size 3 converse.
[dx2fu4q] (score 4, diepte 3) I still have mine from 1992. I think the newer ones are inferior quality-I tend to buy mine secondhand, honestly, because they tend to pop up on resale sites unworn or nearly unworn for a fraction of the price. Docs are easy to source for higher quality-just look for the ones that were made in England.
[dx1vtm2] (score 4, diepte 0) I can wear size 3 in kids' Converse All Stars. They look just like the adult version and cost me $20 less.
[dx1z3oq] (score 4, diepte 0) This is also true for sunglasses. Adult Ray Bans cost around $150, but kid's Ray Bans cost around $70. I told a small-ish male friend this, and he happily saved $75 on his last pair of sunglasses!
[dx1zo7m] (score 4, diepte 0) Youth XL is same size as adult small for shirts
[dx21d0e] (score 4, diepte 0) Plus they have sweet lights in the soles.
[dx2cdtt] (score 3, diepte 7) Not allowed? More like they just plain don't want to. They're very much still allowed to play outside
[dx31y0t] (score 3, diepte 3) Just a heads up. I’m a guy about the same size

If you want a sports jersey, try and find a “women’s” small.

In quote because it’s the same cut (usually, just make sure) as men’s and it fits way better than a guys small, which is usually made for someone that’s like 5’6”
[dx2fw9f] (score 3, diepte 1) I have a super short torso and love the kid's section for sweaters that are actually the right length.
[dx2cpsm] (score 3, diepte 2) I’m a US women’s size 8 and all the conversion charts I’ve seen place me at a 5.5. So if you’re saying women’s 7 is a child’s 5, and the other commenter says a 9 is a 6, then our numbers all line up but I don’t think simply subtracting 2 sizes is quite right. 

 I think the sizes are equal at size 3 (hypothetically, I’m not sure if women’s shoes are sold that small) and each size increment for women’s shoes equals a half size increment in children’s shoes. 

So if it’s women’s size/child’s size, the sizing table would look like this:
-3/3
-4/3.5
-5/4
-6/4.5
-7/5
-8/5.5
-9/6
-10/6.5
-11/7

And I believe that men’s shoe sizes work out so that equal size shoes in woman’s shoe is 2 increments above the men’s size. So women’s/men’s looks like this:
-5/3
-6/4
-7/5
-8/6
-9/7
-10/8
-11/9. 

So men’s/women’s/child’s sizes are:
-3/5/4
-4/6/4.5
-5/7/5
-6/8/5.5
-7/9/6
-8/10/6.5
-9/11/7 

And I’m guessing if you’re a man with feet larger than a size 9 or women with feet larger than a size 11 (assuming kids size 7 shoes are common), then this hack doesn’t work for you. If your feet are smaller than a men’s 3 or women’s 3, I assume you’re either a child or someone who has already had to figure out this life hack just to buy shoes haha. 

Edit: also it looks like a men’s to child’s size chart would be similar to the women’s/child’s chart but with size 5 as a the middle point. So men’s/child’s would be:
-5/5
-6/5.5
-7/6
-8/6.5
-9/7
[dx2fzha] (score 3, diepte 3) There is some variance. I'm a 6.5-7.5 for women's shoes, usually a 7. I have boy's shoes in everything from a 4-6, most often a 4-5.
[dx2iaio] (score 3, diepte 1) Kid's sizes are in men's sizing.  Take your regular size and subtract 1.5, sometimes 2 depending on the brand.  They are also wider than women's shoes.
(110 reacties met lagere score weggelaten)

=== THREAD 18olz18 ===
SUBREDDIT: r/WorkBoots
DATUM: 2023-12-22  SCORE: 75  REACTIES: 184
TITEL: I have ridiculously wide feet, especially right one. Tried so many shoes, and all of them make me feel discomfort.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[kei124e] (score 21, diepte 0) I have a few pairs of Red Wing King Toes and they are the only safety toed shoes I'll wear.
[kei1efe] (score 17, diepte 0) Maybe it's time to go custom brands like nicks, JK, Frank's, etc. may be known for their custom logger boots. But they have spread into more standard style work boots nowadays, too. The price is double what you may be used to paying, but having a perfectly fitting boot that will last years may make it worth it in the long run.
[keizzav] (score 12, diepte 0) EEEEE width here. Custom Whites’s and Nicks are the only fit I have.
[kei4rqd] (score 8, diepte 0) Keen Cincinnati for sure
[kei2obz] (score 7, diepte 0) For cheaper brands, I’ve had amazing luck with Merrell and Keen for my feet

Redwing I’ve heard good things

For higher end brands (like Nicks), composite toe should still fit since they are more bulbous but steel toe tends to constrict a bit more than I’d like
[keidfhw] (score 5, diepte 1) It looks like those Setter Wing-Shooters only go up to 2E width. Try the Redwing 606 or 2240. If you actually go into the store they'll measure and fit you and ensure the fit. The "H" widths fits my son's 5E feet.
[keklxx9] (score 5, diepte 1) Just get a pair of Keen dude
[kei0ctf] (score 5, diepte 0) Redwing king toe or Keen Cincinnati maybe
[kekb2zi] (score 5, diepte 1) This is the way, go to a red wing store and get fitted. I don’t have the wide foot issue but my red wings are by far the best boots I’ve ever owned.
[kei4x2c] (score 5, diepte 0) If you don’t need the safety toe, order a pair of Thurman lasted boots from Nicks. They should accommodate your feet well.

If work does require a steel toe, it’s worth checking with a podiatrist to see if they will write you note saying that due to the shape of steel toe caps your feet aren’t compatible with them and that you should be exempted from the rule because wearing steel toes will cause you undue pain and damage your feet.
[keiy822] (score 4, diepte 2) Completely subjective. Also, like I mentioned, nowadays, they have tons of models that aren't in the logger style, but still with the custom fit and heavy duty construction.
[keibavk] (score 4, diepte 0) I think you’re evolving back into a chimp. That this is going to be a hand in a few generations.
[keig4pe] (score 4, diepte 0) I would try some keen boots, the wide size is the only wide i can wear without feeling my toes get smashed together
[kehy13k] (score 3, diepte 0 OP) I’ve tried so many work boots and all of them making my right foot feel very discomfort. The big toe always touching the wall, and nail is always in pain. Bought another pair Irish Setters, a lot of our guys wearing it, they are very good, but not for me. This one’s on the picture is 13 widest ones. I’ve read that there’s exist a Red Wing King Toe, planning to try them too, if they will not fit, then I don’t know. Is it possible to adjust toe box somehow?
[kel2w1c] (score 3, diepte 1) Had a coworker that was blessed with gout.  Those were the only boots he could wear. OP might benefit from looking around in a gout subreddit to get those guys' take on it.
[kei56p8] (score 3, diepte 1) This !!
[kei53og] (score 3, diepte 0) Try Keens. They make a moc toe that’s wider than those. I have a pair. They broke in nicely.
[kei7vgw] (score 3, diepte 0) Jim green boots
[kekh6d5] (score 3, diepte 1) I’ve tried most of the brands recommended on this page, and Jim Green are the only ones that really had a wide enough toe box for my feet. Not their Vellies, but I have both their ranger boots and their full grain hiking boots.  I did end up going up up a half size. Get their crepe soles not their waffle soles.
[kekwjhh] (score 3, diepte 1) Feet are suppose to look like that…
[kelyt3o] (score 3, diepte 2) If the uppers are in good shape why not
[kejte6g] (score 3, diepte 0) Another vote for Keens
[kevfbs1] (score 2, diepte 1) We are in similar boats. I'm a 12 EEEEE and on top of that, I'm missing a bone in each foot. As a result, if im not really careful about insoles and arches, I get Jones fractures. A set of customs where they modify a last to fit you is the only way to go. I've had White's, nicks, and JKs. IMO the JKs are the best at actually getting you a perfect fit. I got a pair of custom 2.0 OTs in bison leather. It's worlds better than White's or Nicks. $780, but no more trouble with fit or Jones fractures. It's 100% worth going to Spokane to get fit at JK.
[kem2ggu] (score 2, diepte 2) I have gout. I've spent 1000s on boots and still haven't found a pair that I completely like. Gout sucks
[kemm058] (score 2, diepte 3) God bless you,  my friend.  I couldn't imagine what it must be like. In my coworkers case, all he did was eat good food and drink a few good beers
[keieufw] (score 2, diepte 1) They’re a little more expensive but they’re also be recrafted. So you don’t necessarily have to always buy new boots
[kej07gk] (score 2, diepte 2) The logger heel with the high arch support is the most comfortable style of boots I have ever worn. Sometimes I don’t want to take mine off at the end of the day.
[kejurut] (score 2, diepte 1) With Nicks you can get custom pairs built specifically to your foot size and shape. Up to EEEEEE
[kemyge8] (score 2, diepte 1) Any Keen Work Boot. They're so wide that I buy keens in normal width and all other shoes in wide lol. love all my keen footwear
[keip656] (score 2, diepte 1) FYI : Nick's only offers their Thurman last up to FFF width, which is too narrow for my feet (11.5in circumference around the ball of my feet).
[keiporh] (score 2, diepte 1) Keens are the best I've found for my feet too, though the build quality is nowhere near the traditional boot brands. I love thorogoods but the toes are too narrow for me now. I wish there was a thorogood build quality with the keen foot shape without going full custom...
[kei67z8] (score 2, diepte 0) Keen for boots and Altra for shoes. I also have Hobbit feet.

I tried Red Wing King toe, still way too narrow for my feet.
[kekfodx] (score 2, diepte 1) Which Keen did you settle on?  I normally wear the Detroits steel toe, but tried ordered the Cincinnati in wide with steel toe and I think I'm going to return them.  Altras are the best too.
[keo1i6d] (score 2, diepte 2) https://m.youtube.com/shorts/U4NiUBV-Qn0?si=OjI3qGuEmtBQahBz

Here's the vid I meant to send. Altra has different sized widths with large toe box.
[kei7syu] (score 2, diepte 0) Carolina 5020  Wide Toe Box changed my life. Even wide sizes in other shoes had me fighting to put my foot in. I just thought that was how shoes were supposed to fit. Then I got the right size, 11EEEE, and it was a game changer. No more fighting my boots on or off, no more blowing the sides off the sole.
[kei87e9] (score 2, diepte 0) Same problem as me, you're going to want to be looking for something with a wide toe box. It finally unlocked finding the right shoes for me. The tapered toe smashes out little piggies and makes life miserable.
[keibgk4] (score 2, diepte 0) Redwing king toe has been mentioned numerous times and I'm gonna say it again.  They fit and they last. It's the only work boot my Triple E foot can tolerate for 10 hrs a day.
[keixl44] (score 2, diepte 0) Have u tried wearing them sideways
[kelrpg7] (score 2, diepte 1) I live in wildlands fire country and every season there’s dudes getting rid of their boots. I’ve been temped to resole em.
[kepa9u6] (score 2, diepte 1) Pic saved, but you called me out over a day ago. How'd you know!
[kej1xqe] (score 2, diepte 0) I have 14EEEE size feet. I wear Belleville boots. Belleville 390s in the summer and Belleville 770s in the winter. 
https://www.bellevilleboot.com/index.php?l=product_detail&p=10
https://tacticalgear.com/belleville-390-hot-weather~1#/2194/0,2332,23537/1
[kej2gl5] (score 2, diepte 0) With you, brother (see username).

JK boots can go 5E wide. The other PNW Bootmakers can too, but the ones I’ve tried either left the heel a bit loose or had too much volume for Flintstone feet.

For a lighter boot look into Lems & Duckfeet. Keens also come in wide sizes.

HOKA & New Balance for running shoes.

Allen Edmonds EEE for a dressier boot/shoe.

And while expensive and possibly not worth the money, Alden’s Indy really does have a phenomenal last.

Good luck and stomp on.✊🏼🦶🏼

Focus on rounder toes
[keja0kh] (score 2, diepte 0) Try altra's. Also barefoot shoes, vivo barefoot, and look into birkenstocks. They accompany wide toe boxes.
[kejbf03] (score 2, diepte 0) I have the same feet! 

I also have the means to spend whatever on comfortable footware (and I do as I can be a bit boujee). However, when it comes to work boots, I haven't found any thus far more comfortable than a pair of $109 Justin slip on (model MJ1013) waterproof steel toes. They're made in Vietnam and are probably not the highest quality nor longest lasting, but they are comfortable so I don't really care. They came from Academy and break-in was about a week. Buy them a bit snug.
[kekag35] (score 2, diepte 0) Stop with the lace up round toe boots.  Try an Ariat square toe wide pull on boot with no laces. A coworker told me when I was bitching about boots to stop with the laces like I’m playing a sport…….tried them and I’m on my 4th pair(my work buys one pair a year for us)

https://preview.redd.it/c131g5bs7z7c1.jpeg?width=828&format=pjpg&auto=webp&s=876e97b3f7c493fd1b78f2092ed139f74348cbf7
[keooid4] (score 2, diepte 0) Are you a Sasquatch?
[keidjne] (score 1, diepte 1) The king toe are probably the widest shoes I’ve ever seen. They were actually too wide
[kejszr6] (score 1, diepte 1) Have you tried a wide square toe?
[kejxzz3] (score 1, diepte 1) I've struggled with the exact same issues you have along with wearing custom orthotic inserts that add volume because of the raised arch cramming the top of my arch into the tongue/lace area on most boots I've tried.  If you're not going custom(Nicks, Jk, etc) then Carolina 1809 has a 4e that fit my wide ass foot with wiggle room to spare.  I've worn them over a year and have held up to some serious abuse(fleet field mechanic). I will recommend getting some tufftoe or kg's bootguard to cover the toes as I rubbed holes over the steel toes in the first few weeks.  Keens also fit but they don't last more than 6 months without having to use their warranty.  Also Ariat wide square toe fit but the midsole support collapses pretty fast and hurt the soles of my feet.
[kepb0xq] (score 1, diepte 1) Keen are pretty comfortable, like wearing a hiking boot, but their toe box changed last year (what the guy at the store told me).. I hurt my toes just buying the same old pair as I had every year. Back to the king toe. I just wasted 145 bucks on some Rocky’s that felt pretty good until I’d been in them for 5 or 6 hours. Then my big toes felt like they’d been hit with hammers. So back to my king toes. One thing about red wing, they take awhile to break in, you’ll want to buy the new insoles relatively soon after the boots, and the insoles take a minute to break in too
[keqj2qz] (score 1, diepte 1) Sucks you are having fit issues. Nobody wants painful feet everyday. 

Redwing stores here have digital scanners, then they offer you the best fit shoe based on needs like safety toe and such. In my case one foot is bigger than the other so that is the size I shop for. A brannock device is accurate as well. Measure both, take pictures for reference. Also, going up one size can buy more room typically,  you are extra wide so trying on until you find what works is important.  

If the redwing scanner helps, their boots go on clearance in the summer, typically around August. Around here the odd sizes go for super cheap.  Hope this helps and good luck!
[kezhvba] (score 1, diepte 2) Mail in sizing for me worked perfect!
[kei0x81] (score 1, diepte 0) Danner Bull Run Chelsea's, the Chelsea's run wider in the toe box than other boots and may work for you.
[keo2yxm] (score 1, diepte 3) Lose weight and it’ll go away.
[keo4sah] (score 1, diepte 4) I wish it was that easy.
[keo9z02] (score 1, diepte 4) No, it won't.
[keoilzi] (score 1, diepte 5) Gout is the bodies inability to regulate uric acid. This inability to regulate uric acid is a product metabolic disease. Metabolic disease is caused by moving too little and eating too much in 99% of cases.
[keou6og] (score 1, diepte 6) Obesity can cause gout, but losing weight is not an automatic cure. It can help reduce flare-ups if obesity was the cause of it for that particular person, but it's not always the cause.
[keou9lv] (score 1, diepte 6) My disagreement is that their gout will be cured if they lose weight. That's not the case for everyone.
[keqgw0y] (score 1, diepte 7) Of course its not the case for everyone…nothing usually is, but what harm is there in losing weight? If they dont lose weight they will have worse problems than gout and it is indeed one of the precursors to diabetes.
[kesxo1y] (score 1, diepte 8) Saying that if they lose weight, it will definitely go away is just false. Weight loss can help many things, but that doesn't mean it will cure their specific issues. They may be a normal weight or underweight, in which case, the advice would be harmful.
[keszoz0] (score 1, diepte 9) According to the American health institute. 1%-2%   of people that have gout have a normal bmi…..slim chance op is not overweight. Ive had gout for a decade, countless doctors, podiatrist, rheumatologist…..your not gunna tell me anything new
[ketcokh] (score 1, diepte 10) I think you're missing my point. You can't give unsolicited medical advice to random people on the internet without even knowing their circumstances and without being a medical professional. Telling someone that losing weight WILL cure their gout is just stupid. One, because it won't work for everyone, even if their gout is caused by obesity, and two, most people who are overweight realize that it could help. You're not giving anyone new information. "Lose weight" is the first thing any overweight person hears when they have any medical condition, even if it wasn't caused by being overweight, so I'm sure they've heard it all before. Saying that it COULD help would be fine, but the way the comment was worded makes it sound like a guaranteed cure, which it's not.
[keuet06] (score 1, diepte 11) I didn’t say “lose weight”, get over yourself. Of all the shit that happens on the web, your over here on Christmas eve policing Reddit. Merry Christmas and good day!
[kfosedp] (score 1, diepte 12) You can do what you want. I'm just explaining why your comment is unhelpful and incorrect. You're free to say whatever you want, and I'm free to give constructive criticism when I see a comment I disagree with. Merry Christmas and happy New Year.
[kep2phj] (score 1, diepte 4) Look at his ankle dude is not overweight just big ass foot
[ker2tcq] (score 1, diepte 5) Not the same person
[kexaze5] (score 1, diepte 4) Probably stop drinking too
[kerxcwy] (score 1, diepte 3) Yes it does suck, used to load trucks and one of my drivers had it. Could barely walk some days, other days he was ok but you could still tell. He also said the same thing about boots. Always would tell him to immediately sit down, relax. I’ll handle the placards and everything.
[kerxors] (score 1, diepte 3) Talk to your Dr about putting you on Allopurinol. I used to get gout and uric acid kidney stones a lot. Even though my uric acid levels were within range my Dr said sometimes your body just doesn’t like it in the higher side of “normal” (which mine was). After being on Allopurinol for over 10 years now I haven’t has gout or kidney stones since. It’s been wonderful.
[kerxzaa] (score 1, diepte 4) I did and I had a few side effects one being the rash. But I am to the point I get one bad one a year, but the older I get I might learn to deal with the rash.
[keryg5o] (score 1, diepte 5) Oh ok. That sucks. I was fortunate I guess and had zero side effects from it. Do they at least give you prednisone to help get rid of the gout when it flares up?
[kerypti] (score 1, diepte 6) Yea I keep a script on hand. Haven't used prednisone in over a year. But I am heavily considering allo again.
[kes092n] (score 1, diepte 7) Yeah it worked for me. Luckily I didn’t get a rash though. Between gout and kidney stones though I would have gladly taken the rash. LOL they were horrible!
[ketuah1] (score 1, diepte 3) Read the book "Drop Acid" right up your alley from someone who used to have gout.
[keyrtfk] (score 1, diepte 3) My dad eats frozen cherries in a shake. Apparently cherries help process uric acid.
[kemhfi0] (score 1, diepte 1) I 2nd the King Toe shoes. I have wide af feet, and can’t squeeze into normal work boots. Used them for about 3 years before they finally gave out. The leather strap on the metatarsal guard finally gave out. Still had plenty of tread on the bottom. Went through about 5 pairs of shoe laces during that time lol..

When it came time to replace them, I switched to the Timberland Met Guards because they make them in extra wide toe as well. What I like about the Timberlands is that they have lace locks, so no more shoe laces coming loose. They make the same boot without Met Guards.
[kemr96l] (score 1, diepte 1) I have wide feet and I’m really happy with the work version of their classic moc toe boots. They’re also made in the USA.
[keolccl] (score 1, diepte 1) My feet are squares and Red Wings are the only boots I can wear comfortably
[kepke6a] (score 1, diepte 1) He needs extra wide king toes
(377 reacties met lagere score weggelaten)

=== THREAD 1k2vtgb ===
SUBREDDIT: r/BuyItForLife
DATUM: 2025-04-19  SCORE: 74  REACTIES: 180
TITEL: The Best Sandals on the Market? ARCH SUPPORT IS KEY
POST (source_id=post):
Hey, so I’m on the hunt for some really comfortable sandals that I can walk around in. Its about to get so hot where I live that I can’t really fathom wearing trainers all summer so I need some comfortable options that won’t wear out too soon. I need something with great arch support and sturdy straps so my foot doesn’t have to do all the work of lifting the shoe as well as walking. And don’t worry, I’m not gonna rock the socks and sandals situation. 

Please drop your comfiest options (some neutral coloured ones like black or brown would be best) and added bonus if they don’t make me look like a middle aged dad.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[mnx6ako] (score 263, diepte 0) Unpopular comment incoming-I live in Birkenstocks and they make my feet feel better than any other sandals and I'm proud to be a middle aged dad.
[mnx7ee7] (score 158, diepte 0) Chacos have options with good arch support.  And Birkenstocks too.
[mnx7t23] (score 51, diepte 0) Olu Kai have always had great arch support and are well made.
[mnxb43q] (score 43, diepte 1) As long as they match the Subi
[mnx7oio] (score 36, diepte 0) Switching from Clarks to Vionic sandals got rid of my planter fasciatis
[mnx7z4n] (score 34, diepte 0) The higher-end Chacos. I've been in sandals pretty much my entire life, and I've run the gamut from Tevas and Birkenstocks to bedrock to chacos. While each has its own pros and cons, you have specifically wished for arch support. For context, I am a disabled veteran and have run the rodeo of pain in my back and through my legs. 

Chacos are the answer for your problem. They have a podiatrist and orthopedist-approved sole with great arch support. The straps are infinitely customizable to what you're doing. Make sure you do a good fitting at a place like REI that specializes in outdoor sandals.
[mnxcxrj] (score 28, diepte 1) > Chacos have options

They even will let you design your own NMIC pair.
[mnxaiji] (score 23, diepte 1) Soft footbed birks are a game changer. Perfection.
[mnx84h3] (score 20, diepte 1) Birks are great once they’re broken in. That break in period took some time but totally worth it! I wear Birkenstocks for work and they’ve treated me well for 3 years.
[mnxmc9u] (score 20, diepte 2) Seconding the mychacos option, the vibram sole will last the longest out of their options
[mnx6b0u] (score 18, diepte 0) OOFOS
[mnxhnfa] (score 13, diepte 2) I have the Classic z/1 sandals and they have great arch support.
[mnxbsnq] (score 13, diepte 0) For arch support, I like Hoka recovery slides.
[mnxf0fy] (score 12, diepte 2) Stop I just choked on my drink, you’re a real one for that!
[mnxao8j] (score 12, diepte 0) Love my Teva’s. I live in them during the summer months, and they’ve been going strong since 2017
[mnx90pn] (score 11, diepte 1) Birkenstock seconded.  For years avoiding them because stupid german birks and socks meme, but i got a par of the most standard ones and wow.
[mnxqqli] (score 11, diepte 1) I was a Birkenstocks girl fully (still love them) but after moving to Florida my every day flip flops are now Olukai. I wore them on a 4 day Disney trip and the only thing not tired by the end were my feet.  I wear them pretty much any time I'm not in the shower or bed and they hold up pretty well.
[mnxapm1] (score 11, diepte 0) Naot feel like heaven on my feet and are built to last.
[mnxapo5] (score 11, diepte 0) Mephisto were recommended by my podiatrist. I wear them as house sandals and they are great.
[mnxbb6m] (score 10, diepte 2) Just don’t get the cloud footbed; that’s the squishier one, and it wears out a lot faster. They’re also bringing back the Vibram outsole outside of custom styles with the rapid pro styles, so that’s a step forward. And they’re increasing the number of styles that have wide sizes available. 

If you are willing to go for a custom style, my understanding is that those are still made in the US, and you can choose from a few different outsoles.
[mnxzahs] (score 10, diepte 0) Archies only do flip flops and slides but their arch support is next level.
[mnxde8z] (score 9, diepte 1) I need a lot of arch support and I wore my Birks walking all over Rome with zero pain.
[mnx6zu9] (score 9, diepte 0) Rainbows
[mnx9ejd] (score 9, diepte 1) I’ve seen some people saying the quality of Chacos has declined due to manufacturing changes, but I have a 20 year old pair that’s still going strong. I love that you can get them resoled and the straps replaced. I’ve had them resoled once with the Vibram sole that’s like a hiking boot. The straps and footbed are still in great condition even after years of hiking and kayaking. Great arch support.
[mnxezrv] (score 9, diepte 0) Archies all day, they are almost BIFL in durability and are designed specifically for arch support
[mnxappz] (score 8, diepte 1) I have and really like both, but chacos are just so heavy, and the toe strap takes a long time to get used to. They also take forever to break in. I recently switched to bedrocks which are way more comfortable but don’t have arch support…but maybe there’s something else out there that has arch support and isn’t heavy and super uncomfortable??
[mnxkihu] (score 8, diepte 2) They're the archiest around, try em on.
[mnyfy3k] (score 8, diepte 1) Was scrolling looking for this suggestion! Bought a pair several years ago and haven’t looked back. Perfect black flip flop that goes with everything. I live at the beach so they get heavy everyday wear. Easy to rinse off if needed and quick dry!
[mo0meol] (score 7, diepte 2) Z2 chacos have the toe strap, I always get the Z1 without toe strap.
[mnyrn1v] (score 7, diepte 2) My wife’s doctor suggested them as well. She’s had hers for probably 7 years and they still look great.
[mnxb65q] (score 7, diepte 0) I swear by reefs. They can be more comfortable than most shoes in my opinion.
[mnxkjoq] (score 6, diepte 2) Maybe try the narrow ones?
[mnxw802] (score 6, diepte 2) I love mine.  I had to buy a pair when I was in FL and my flops blew out while going out to dinner and the only shop around had a pair.  I about choked on the price but once I slipped it on, it like a cloud.   I wear them all day and never have an issue.
[mnxdfht] (score 6, diepte 1) I did not want to wear OOFOS. I am not a fan of the look. But after dealing with Achilles tendinitis for months I caved. They are now my favorite hands down. I do still wear my birks that I’ve worn for years but the oofos are a dream.
[mnz6yrn] (score 6, diepte 3) yeah if I ever get another pair of chacos, it will be customs. My last two pairs were.
[mnx99bh] (score 6, diepte 1) I’m eyeing the Vionics sandals!
[mnx9i83] (score 6, diepte 0) I just discovered that many local shoe repair stores also carry high end shoes!  I recently went into a place and could have bought the entire store. Super comfortable and cute shoes. 

Berkinstocks have fantastic arch support
[mnxczdu] (score 6, diepte 1) I have had Naots for a long time- one pair black, one brown, same style. I love them so much! I got each pair resoled, and they have lasted about 8-10 years including the resoling (I don't think they'll make it through this summer). I live in a place that has winter, so they don't get worn year-round. I need serious arch support too, and these have been great. 

I also have loved Tevas, Keen flip flops, and Birks. But the Naots work well for a situation that's slightly less informal- like for a job that doesn't allow flip flops. Naots are better at looking "normal," as opposed to "hippie" or "outdoor sports."
[mnx76ua] (score 5, diepte 1) I wish they fit my foot. I try a few pairs on every year and I’m size 10.5 no matter what and a size 9 in Birks are too big still.
[mnx6yfr] (score 5, diepte 0) Keen wk450
[mnx7ice] (score 5, diepte 1) Seconding both of these
[mnzrjgn] (score 5, diepte 2) They’re so archy I can’t wear them for long. My husband loves his, though.
[mo0rpjg] (score 5, diepte 3) Same. I got rid of mine. They didn’t hit in the right place and they hurt my feet with those big arches.
[mnxhb7l] (score 5, diepte 1) I bought Vionic slippers to help deal with my Achilles tendinitis.
[mnx85dj] (score 5, diepte 1) The only tough part about my Olu Kai’s were the first few weeks when the toe separator thingy needs to be broken in. After that, I had my first pair last for 9 years before they gave out.
[mnxa41v] (score 5, diepte 0) Adding to the Chaco or Birkenstock chorus. Chaco also has an easy repair process for their Z sandals. You can resole, restrap, etc., for a small fee. I've had the same ones since 2010 and am probably due for my second resole soon.

That being said, OP, I've found that you either have Birkenstock feet or you have Chaco feet. I used to have Chaco feet. A couple of pregnancies later, Chacos are just a touch uncomfortable for me, so I only wear them on wet days. Birkenstocks around the house, to the store on clear, dry days, etc.
[mnxd7gb] (score 5, diepte 1) I LOVE my FitFlops, have had them for years, like their slim profile, and they're more comfortable than all of my sports shoes!
[mnypbaj] (score 5, diepte 2) And the tong part is attached so it won’t pop like other brands
[mnx6jiz] (score 4, diepte 0) Check out bedrock sandals
[mnx7hhy] (score 4, diepte 1) Adding to this comment, I really like my bedrocks. Though I haven't gotten to the point that they need repair just yet, they seem to be completely rebuildable. My Chacos generally got two updates of straps or soles before the foot bed started deteriorating. That would make the bedrocks more bifl in my mind.

Still, even their most supportive model (Cairn Evo 3d Pro) lacks the arch support of Chacos Z sandals so may not be ideal for someone needing extra arch support.
[mo0noke] (score 4, diepte 2) I have 2 pair and i use them as hiking/backpacking sandals. 

And with Chaco you can replace the sole & the straps
[mnxa2g4] (score 4, diepte 0) Merrell is the way to go. I exclusively wear their sandals during summer vacations and have walked miles at a time in them with no fatigue, blisters (I can also walk a lot in Teva, but there's a blister time period every year), or pain.

My 80 yr old mom also wears them and was having a problem with her back. The orthopedic doctor asked what shoes she regularly wore. She showed him her Merrell sandals. He said it's what recommends to people with back and knee pain.
[mo0tok5] (score 3, diepte 3) [These!](https://www.birkenstock.com/us/tokio-super-grip-natural-leather/tokio-core-naturalleather-0-evarubbersupergrip-u_19.html?dwvar_tokio-core-naturalleather-0-evarubbersupergrip-u__19_width=N&dwvar_tokio-core-naturalleather-0-evarubbersupergrip-u__19_size=230&gad_source=1&gbraid=0AAAAADPjTNzZM13BIABrrWxHlcjsyY325&gclid=CjwKCAjwk43ABhBIEiwAvvMEB5ApnLA7jV-QwgkW0ulMPdiOVPsV-AAhAjrGvmuRb9nkKMCJBYdkzhoC52kQAvD_BwE) I have them in white because that was the only color they had but I get A LOT of compliments on them.
[mnxfk14] (score 3, diepte 1) Birks feel like someone is stabbing my feet they are so uncomfortable the pain is excruciating. If there is anyone out there with slightly lower arches, beware!
[mnxsutz] (score 3, diepte 1) And the can be resoled
[mnx9332] (score 3, diepte 1) Yep. All day.
[mnxh2up] (score 3, diepte 2) I tried oofos on for a few minutes in the store and I thought they felt just alright. Is there a breaking in period with them?
[mnxj6oa] (score 3, diepte 3) I’m my experience, they don’t really need to be “broken in” but you need to just get used to how they feel because they do feel weird at first. Make sure you have the right size as well
[mnxi5s6] (score 3, diepte 2) Yep.  I now only wear Solomon Trek shoes as my daily casual "sneaker" for the support to solve my plantar fascitis.  I missed being able to wear sandals for more than an hour or so.  Oofoos solved that.  I can wear and walk in them for long periods of time without repercussions.  Happy feet.
[mnxbt9n] (score 3, diepte 1) Love those—but they have ZERO arch support.
[mnxpq8z] (score 3, diepte 1) Yes agreed, my go-to. The double layer ones in particular have decent arch support. Rainbows can last a good amount of time and you can mail your used ones in for their reuse/recycle program
[mnxgzyk] (score 3, diepte 1) Is there a specific models? I did image search and they have exactly 0 arch support from what I am looking at.
[mnz30dz] (score 3, diepte 2) Suggest you try a pair from Zappos before you get a custom pair you can't return.  I like Chacos, but the classic z/1 and z/2 heel edge hurts my foot so I can't wear them everyday.   Zappos has free returns.
[mo0ghcl] (score 3, diepte 3) That’s a great endorsement, thank you for sharing!
[mnz7nig] (score 3, diepte 1) I remember seeing my podiatrist for PF and she chastised me that she didn't want to see me without my orthotics.. till the day I showed up apologizing up and down while wearing my Chacos and she said, no worries those are great! lol.
[mnyadyv] (score 3, diepte 1) My Teva Hurricanes had the strap pull out after about 3 weeks. I contacted the company and they said Hurricanes were discontinued and they would not warranty or replace them. I believed them, then found out about a year later that they were lying, Hurricanes were never discontinued are still offered to this day. Teva is a deceptive company with poor quality products.
[mnxyfh0] (score 3, diepte 1) They are like walking on marshmallows and the best for any foot fatigue and recovery. I’m on my 3rd pair.
[mnxct2y] (score 3, diepte 0) Birkenstocks are cool these days
[mnxdxdf] (score 3, diepte 0) Have tried 90% of the sandals mentioned here and some are good.  None are as good as Sole — sandals made by a footbed company.
[mnxgzr0] (score 3, diepte 0) I swear by SAS shoes. Pricy but worth it. 

https://www.sasshoes.com/mens-sandals/
[mnyt2ny] (score 3, diepte 0) I've had good experience with KEEN. The Targhee 3 hiking sandle is great. I hiked all over Hawaii in those. Had them for a few years and they never lost support. I'd still have them if my goober of a Dane didn't chew them up.
[mnxxkdb] (score 2, diepte 3) And i don't know what about them is so good specifically. I don't normally like that structured of a flip flop, I don't usually do thongs but whatever it is,  it works!
[mnxt1b4] (score 2, diepte 1) I have a pair of softmoc branded birk knock offs that have so far lasted 5 times longer than my last pair of birks. 

I wear them with socks all the time. Fashion be damned, It’s so comfy.
[mnz7dha] (score 2, diepte 1) I loved them. Then blamed them for a years-long bout of PF and why I'm leery of new shoes/brands. Then tried them again a couple years ago, have several pairs, stll can't walk long in them. They don't aggravate my PF anymore but I think I've evolve to learning to avoid a flare-up but man do they fuck up my calves, which in turn causes me to wake up with painful cramps. WTF, man ugh. I still wear them around the house or for quick drives out.
[mnxuvgs] (score 2, diepte 1) Hand down the best. Not very stylish unfortunately but what they lack in style they more than make it up with comfort.
[mo3x57z] (score 2, diepte 1) I'm on my second pair of Keen Newports and love them.
[mo17onr] (score 2, diepte 1) I hated my Vionic sandals :( I sold them on Poshmark. They had arch support but it didn't work for my foot. It's a longer, more sloped sort of support, it's hard to explain. I needed the arch support to be shorter, I guess my arches are short, idk. It came too far to my heel and too far towards the ball of my foot. It actually made my plantar fasciitis worse. However, I wear 3-4 pairs of their flats to work daily, and those are great. Dunno what it is about the flip flops but they destroyed me.
[mo0i4q2] (score 2, diepte 2) I am going through that now. My old ones died not too long ago.
[mnxdki1] (score 2, diepte 2) I agree that Naots look more dressed up. I just got a new pair of their ankle boots for my office job and not only do they look like any other non-orthopedic ankle boots, I let out a little sigh of joy every time I put them on 😆 I have a 5 year old pair of ankle boots that still look brand new but the sole is just pounded down because I wore them every day and walked a lot- nowhere to get them resoled around here unfortunately.
[mny3c11] (score 2, diepte 3) I had some Naot heels for a long time. They were the only "fancy" shoes I owned that I could wear for more than a couple of hours. Heels AND a cork foot bed?? Absolute heaven!
(114 reacties met lagere score weggelaten)

