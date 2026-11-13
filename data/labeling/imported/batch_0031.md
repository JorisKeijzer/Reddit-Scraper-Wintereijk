# Label-batch batch_0031

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
Schrijf het resultaat naar `batch_0031.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1h8fzmp, 17dxz10, a3uecc).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1h8fzmp ===
SUBREDDIT: r/goodyearwelt
DATUM: 2024-12-07  SCORE: 78  REACTIES: 64
TITEL: Oak Street Trench Boots vs Grant Stone Diesel Wide *ish Feet
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[m0sofbk] (score 28, diepte 0) This is info I’ve always wanted. Oak Street has often been clowned for how “wide” their toe boxes are and apparently the stock pictures don’t do it justice. From this pov, they look perfectly normal.
[m0slth5] (score 18, diepte 0 OP) Comparison of Oak Street Trench boots in size 11 vs Grant Stone Diesel in size 11E.  I have a bannock size of 11.25E and both of these boots feel about the same on my feet.  The Oak Streets hug my ankle and heel slightly more but really not noticeable once they are on the feet.  I walked around for a few minutes with both of them on as pictured and couldn't remember which was on which foot and they felt almost exactly the same size.

I really like both of these brands.  They both have great fit and finish to them.  Quality control is spot on on both of them.  They both are very comfortable and fit my foot very well with plenty of toe wiggle room and nice and snug heal and ankle hug.  The profile is slightly different but when looking at them in person, it really isn't that noticeable.  They are both very sleek.

I couldn't find a ton of info for wider feet comparing these two brands.  Hoping this helps the slightly wider foot crowd a little.
[m0sx694] (score 12, diepte 0) There is no size of GS that fits my foot right. I tried multiple times with multiple widths at GS’s direction…is what it is

Oakstreet’s Elston fits me perfectly
[m0svsg0] (score 10, diepte 1) I have toe splay and find the Oak Street Elston last to be extremely comfortable in the toe box. My experience with the GS UK last was pinched toes.

Actually wearing my Oak Streets today...

https://preview.redd.it/za6tlks9xb5e1.jpeg?width=3072&format=pjpg&auto=webp&s=6c28c0f40c1e700f2acd2cfabf31a0826404596f
[m0sqv77] (score 7, diepte 0) I recently tried to love gs boots but I couldn’t. The toe taper was too aggressive for my foot, it curves inward to soon/much and punches off my pinky toes. How does the oak street stack up in that regard?
[m0soq89] (score 6, diepte 1 OP) They are actually even closer in height than they appear in this picture due to the split welt on the Grant Stone and the Flat Welt on the Oak Street.  They truly are both really nice boots!
[m0tmo4p] (score 4, diepte 5) They are the natural chromexel. They have darkened a fair amount since I got them.

https://preview.redd.it/sjnanzg4vc5e1.jpeg?width=3195&format=pjpg&auto=webp&s=6850a400d126af8c7e88ad916776da4ba01706e3

It's not a perfect contrast because the light is a bit different between the photos but you get the idea .
[m0uik0y] (score 4, diepte 1 OP) 2024, Just got them. The welts look great on both boots, no puckering. Quality control is good all around.
[m0uv0c1] (score 3, diepte 1) It’s not as much that they are “wide” it’s that the toe isn’t as low profile. The profile of the toe probably has more impact on the aesthetic than the actual horizontal width. The “bulbous” shape gives the impression of a much larger boot simply because it’s more volume in the front even if they are both the same length and width. The GS might even be a bit longer.

I think some of the reason people size down too much in certain lasts like Red Wing no 8 is they have a tall toe box which just visually makes the boot look BIG. Same with Grant Stone’s Floyd last which has the exact same internal measurements as Leo. A lot of people take Floyd at a smaller size even though the lasts fit the same and it’s because optically Floyd just looks a lot bigger.
[m0ss561] (score 3, diepte 1 OP) The Oak Street doesn't touch my toe and I got the right size on the first try.  Zero hot spots or issues with Oak Street for me. My first pair of Grant Stone Diesels were 10.5E and I had that same problem.  They put pressure on my pinkie toe. I sold them and went half of a size up to 11E in these pictured and it fixed that issue for me.  They fit great with no issues or pressure anywhere.

  
What size Grant Stone boots do you have? Have you tried going up 0.5 or one size wider?
[m0uvy9q] (score 3, diepte 1) If you’re getting pressure in the 5th toe you should try taking Leo TTS. Going up in length rather than width typically results in more room for the pinkie toe since width is graded at the ball mostly and you get a slightly sharper taper when you add width. 

It’s funny that nobody ever considers going longer but it really works better in most cases than adding width unless you have a particularly wide foot.
[m0sxe7v] (score 3, diepte 2) For the Diesels I went with Natural Waxy Commander and Dark Kudu.  For the Oak Streets I got the English Tan Dublin Field Boot and the Minerva Liscio Olmo Trench.  All of them look fantastic and definitely looking forward to the patina.  My intent was to check out both of the Oak Streets and send one back, but I don't see that happening now.
[m0sxp96] (score 3, diepte 1 OP) That's too bad.  It sucks when you can't wear something because it doesn't fit well.  I have had that issue with sneakers in the summer.  I like Koio and Oliver Cabell, but they are too slim for me.  Beckett Siminon sneakers fit me well, but took multiple tries of different brands to find them.
[m0tq5ve] (score 3, diepte 1) +1 from me as well.

I really liked the Leather choices of GS but it just wont fit! What a shame that is....

On the other hand Oakstreet Boots felt supreme on my feet
[m0sy8pa] (score 3, diepte 0) I would go with Oak Street any day over Grant Stone.  The Grant Stone lasts don't fit me well.  

Lakeshore and Trench boots fit spot on and TTS.

I'd pick Parkhurst over both.
[m0tqbhb] (score 3, diepte 1) +1 for Parkhurst from me as well.

The duties are kinda steep but it's still well worth the money!
[m0t55fs] (score 3, diepte 0) Nice write and good comparison pics!

I have a OSB Trench 13 a Grant Stone Edwards 13E, so I’ll add my comparison to the mix. 

I’d agree they have more or less the same volume around the ball and toes, but the Trench is more anatomical on me. The GS has more width in the heel, not exactly sloppy, just a little more play. The Trench has a nice heel hug. I have wide toes and narrower heels, the Trench is pretty much made for me. 

They both feel great, but as you might guess, the Trench wins on comfort.
[m0t5pen] (score 2, diepte 3) Mine aren't brown at all, they almost look pink!
[m0t6fk3] (score 2, diepte 4 OP) Pink?! Can you post a pic of them?
[m0tqen0] (score 2, diepte 4) Hey thanks a bunch. Always nice to have more options for my clown feet. The Alden Indy is what drew me to boots in the first place. When I first got into it they were too expensive for me. Nowadays I can afford it but the price has kept going up and into the point where I hear people on here say they aren’t worth buying anymore so I never did. I know those pnw boots get all praise but a lot of them I don’t like the look of. Especially the ones that start to look like high heels
[m0v6c02] (score 2, diepte 6) Where might I look for the 2nds? I’m sure eBay is the answer for the others but something about used boots was always off putting to me. Not to mention with how much trouble I have with footwear in general any option that doesn’t have a return option is scary to me
[m0v61co] (score 2, diepte 2) I have tried that as well, and totally follow what you are saying. The only problem with that is if I go with more length now I’m starting to have a ton of extra size in front of the rest of my toes and my heel gets loose, I think my pinky is in and of itself a bit longer than average? So depending on the shape of the boot to make it long enough for that one makes it too long for the rest of them.
[m0yzf3k] (score 2, diepte 4) That was the conclusion I came to. As much as I wanted to like them I decided this particular brand simply doesn’t work for my variety of clown foot
[m0sso9w] (score 2, diepte 1) The Trench boot is throwing me off because the toe looks much higher and more bulbous than I’ve usually seen.
[m0stb5t] (score 2, diepte 3) Sorry, I should’ve started with - those are both cool boots! Personally, I love a split welt on a casual boot.
[m0svo6q] (score 2, diepte 0) I just did basically the same thing.  I bought two pairs of GS Diesels and 2 Oak Streets, one Trench and one Field boot.  All are flawless and no issues at all.   I'm an 11D, almost E on one side on a Brannock, with otherwise narrow, high arch feet but wide toe boxes due to bunions.  

For the Diesels, a 10.5E fits almost perfectly out of the box. They were just slightly tight at first, but broke in after a couple full day wears and fit perfect now.  I had tried a 10.5D, but they were too tight.  For both the Oak Streets, an 11D fits perfectly out of the box.  I've had one of their suede chukkas for years in the same last and size, so I knew the fit should work in these.  Like your picture shows, the Oak Streets are slightly rounder, but definitely not as bad as some had reported, at least in my opinion.
[m0sy2im] (score 2, diepte 3 OP) Those all sound great!  I really like the look of the English Tan Dublin!
[m0yqj7m] (score 2, diepte 2) Yea I tried a bunch. My one small toe was smashed no matter what size I tried
[m0sza04] (score 2, diepte 1 OP) All great brands!  I really like all three of those!  Parkhurst is just slightly to "pointy" for my taste. I really like the look of them from the side profile, just not top down. Always tough finding the right fit for your foot that also fits your personal taste!
[m0t5skh] (score 2, diepte 1 OP) I would 100% agree with this.  I would lean toward the Oak Street being more comfortable, but just barely. The Trench feels perfect.  The Diesel feels a little looser in the heel, but as long as the laces are tight, it isn't really an issue and they feel great! I wonder if the leather lining of the Grant Stone vs the lack of lining in the Oak Street contribute to this....I would buy either brand again!
[m0t9uw9] (score 2, diepte 0) This is some great info. Thanks for posting the pictures and descriptions of each boot.
[m0tntk3] (score 2, diepte 0) Wow oakstreet without puckering, what year is this ??
[m0t19s6] (score 1, diepte 1) My OSB Color 8 CXL look nothing like yours.
[m0t1s8f] (score 1, diepte 2 OP) They definitely tend toward brown with reds coming through in certain lights.
[m0t607e] (score 1, diepte 4 OP) Pink?!  Can you post a pic of these?
[m158u6d] (score 1, diepte 1) Which of the two are more supportive in terms of arch support?
[m1dcz5c] (score 1, diepte 2 OP) I really don’t have arch issues. My feet are slightly wide with a medium arch. Not high, not low….

I don’t feel anything in either boot that would say is arch “support” to me.
[m0t99om] (score 1, diepte 2) I’ve actually tried them in several sizes and they all give me the same problem. And going any bigger will start to get sloppy loose in other places, so I came to the conclusion that the boot simply does not work for me. I typically wear a 13w 12 in some brands.
[m0tomn4] (score 1, diepte 3) Alden [379x](https://www.brogueshop.com/collections/alden-military-379x-last?srsltid=AfmBOopPjvmq6o-cI8x2lXtyvFo_BFwjIe7UTxQk1-GFhSqrmccg-MmD) last, and [Iron Boots](https://iron-boots.com/collections/mto) Chosen One, Great Escape, and 5515 are all nice roomy toe boxes as well. 

Nicks Thurmans are nice, but I'd recommend going up a width. 

I hear good things about Whites [Swing last](https://eastwestapparel.co.uk/shop/whites-semi-dress-boots-swing-last-distressed-ro/). 

[Jim Green](https://jimgreenfootwear.com/product-category/all/?srsltid=AfmBOorouVndvY7fi8OAgnM5Z5zgmIExyuTl4PjJ9pgclkV7gJ9F3Bmo) if you want a "hold my beer" wide toe box.
[m0uw3st] (score 1, diepte 5) People don’t know what they are talking about. If you don’t wanna pay full retail you can find 2nds or gently used Indy boots for ~$400. And they are definitely worth the money.
[m0xdil6] (score 1, diepte 7) Shoemart sells them
[m0tc199] (score 1, diepte 2) Cool thanks! This pic makes those look nice and comfy up front, I might have to check them out. I was just poking in there website, is that the field boot?
[m0tgg5q] (score 1, diepte 3) Yes, it's the field boot. The trench boots is also on the same Elston last. 

The Lakeshores have a more narrow toe. 

Just be aware Oak Street is a bit notorious for having some welt puckering QC issues. If you choose to buy some take a good look before wearing them around.
[m0tlgk2] (score 1, diepte 4) Thanks a bunch, I’ll take this into consideration. Is yours the “natural” color? If so It looks much nicer in your picture than it did on the website.
[m0tnqdt] (score 1, diepte 6) Appreciate the responses, those ended up really handsome. Thanks.
[m0xifnp] (score 1, diepte 3) There’s no way that wearing GS TTS is unwearably long. We’re talking a couple mm difference between like a 9.5 E and 10D
[m0yp9eq] (score 1, diepte 3) There are diminishing returns on going up a half size if you have toe splay that is rubbing up against the side of the boot. 

1/2 size will not magically make the toebox wider to any significant degree. Unfortunately this is probably a last that you should just avoid, along with other similar lasts like the Alden Barrie.
[m0z623l] (score 1, diepte 5) Yep, you and me both bud
[m0srvev] (score 1, diepte 0) I think it’s funny that OP never identified which is which. Sure, many of us know what the different boot lasts are and can identify which is which, but the title doesn’t even line up with the photo (from left to right).
[m0ss9f3] (score 1, diepte 1 OP) Good point!  What's your guess?
[m0st4cr] (score 1, diepte 2 OP) The flat welt definitely gives it that effect.  It really isn't as noticeable in person.  I really like the Oak Streets and feel they look great in person.
[m0stxwx] (score 1, diepte 4 OP) No worries!  I appreciate it!  I am not sure which welt I like better, I think they both fit each of these boots well.  So many welt options!
[m0stdxg] (score 1, diepte 2 OP) Also, the Grant Stone is a leather sole which gives it a little sleeker profile compared to the Dainite Sole on the Oak Street.
[m0ssf8w] (score 1, diepte 0) Beautiful boots! “Very sleek,” no not at all. Chunky, rugged, and beautiful, yes absolutely.
[m0ssqun] (score 1, diepte 1 OP) Well, compared to some, they are definitely not sleek!  Compared to what I have worn in the past, they are very sleek! I do love them both.
[m0swhny] (score 1, diepte 1 OP) Great to hear!  Thanks for the input on your perspective of both brands! What leathers did you get?  

The 10.5E Diesels I had were the perfect length, but slightly tight on the pinkie toe. I really wanted them to work and tried to break them in, ultimately selling them as my pinkie was sore after all day wear. The added length of the 11E isn't really noticeable and corrects that issue for me.  11 in Oak Street is perfect.
[m0t9bul] (score 1, diepte 1) i've had several pair of GS over the past few years 
i'm a brannock between 7 and 7.5
only have experience with their Leo last with both garrison and diesel as well as a cap toe thrown in there somewhere 

best fitting pairs - and really the only ones that i have kept or still wear - are a 6E diesel cxl and a 7D garrison deer

glad to see the Truman info b/c i've been quite interested - however - shoemarket's black friday knocked my ass out with 4 new acquisitions
[m0tbz9u] (score 1, diepte 1) Same here, shame because they have some really fun, interesting leathers.
[m0vkehj] (score 1, diepte 1) I struggle with this too. Fortunately for me I can find a size that just about fits, so as long as they lace I’m good. I really want their loafers but they are either sole crushingly tight or too loose
[m0yotz0] (score 1, diepte 1) Yep regarding GS. 

Sad too, because I went all in with them in the beginning.
[m1jiyeg] (score 1, diepte 3) Same for me. Really love that the company does, but the taper and celastic toe box are aggressive. If you don’t have the right foot shape, the Leo is a real outer toe cruncher. Also a big heel and vamp too.
[m0tcyzu] (score 1, diepte 1) Love both my Trenches and Lakeshores. Does Parkhurst size the same?
[m0t3qz1] (score 1, diepte 0) F f f.
[m0tai0a] (score 1, diepte 1 OP) I appreciate it!  Hope to help those interested in these two brands.
[m0v0k7q] (score 1, diepte 0) 10.5 HTT and 11.5 HTB on Brannock.  Feet are wide around the ball area, but overall low volume and a skinny heel.  10.5 OSBs fit great with a green Spenco insole.  10.5 D GS Diesels were too narrow and I felt like I was standing on the welt.  10.5E Diesels gave me bad heel slip in right boot even after many hours of break in.  GS is letting me exchange for 10 E.  Hoping this is the magic Grantstone size for me.  Love the look of the Diesels.
[m0v4l4x] (score 1, diepte 0) So that creasing on Grant Stones is normal? I just took delivery of my first pair ever yesterday and it creased like that on my first step of try-on.
[m0v6o0v] (score 1, diepte 1 OP) Yes. Completely normal.
[m0v6sb7] (score 1, diepte 2) Good to know, thanks!
[m0w0c53] (score 1, diepte 0) I have super wide feet like a 4 F in Nick's if they would do it. 5E in JK didn't fit and 3E allen edmonds isn't wide enough.  Eventually when in not poor ill be getting fully custom bespoke done. Everything else is just not wide enough to accommodate my boat feet...
[m1r5cgi] (score 1, diepte 0) Get the Parkhurst 618 last, which is wide through the forefoot, and ditch GS and OSB for good.
[m1s25zz] (score 1, diepte 1 OP) Why would I ditch them?  Oak Street and Grant Stone make quality products that are comfortable and good quality.  Parkhurst has had plenty of QC issues and the owner isn't the friendliest of people.  I know this because I purchased a pair and sent them back to him due to QC issues.  They were unworn minus trying them on on a cloth with 0 issues from me.  They were unworn condition as new.  He isn't the easiest person to deal with.  I would have done an exchange, but elected to do a refund due to his condescending emails and lack of professionalism. I do like Parkhurst boots and may purchase another pair in the future.  But, the one thing holding me back is I don't really want to support a person that isn't friendly to his customers in my experience.  I will have to get past that if I find a pair interesting enough to purchase.  I have also read this numerous times from other posters with similar experiences to mine....search for it.  On the flip side, Grant Stone has great customer service when I did an exchange for fitment issues.  Grant Stone is very helpful, good communication and a seamless exchange process.  Oak Street, I haven't had a need to communicate with their customer service.
[m1uzimb] (score 1, diepte 2) I just find the GS and OSB lasts really dull. Of of course I don't want my boots made in China.
[m1v2nns] (score 1, diepte 3 OP) Of course?  As if everyone thinks like you?Why does it matter where they are made if they are quality?  Grant Stone is based in Michigan and factory in China. They use leather from Horween in Chicago and other tanneries. 

Parkhurst is made in Spain I believe. Leather from all over. So, obviously it isn’t a USA only thing. 

Boring?  They are all very similar. Haven’t heard that one before. 

Honestly, you sound like an entitled Karen. You haven’t contributed anything meaningful to this post. Just bashed a couple companies and said another non US manufactured brand is better.
[m1vitry] (score 1, diepte 4) I'm not entitled. I just don't like buying stuff made in China, especially anything that costs more than $5 in Walmart (most of my boots are made in Canada). Don't pretend things made in Europe are on the same lower level as things made in China. And I've owned all three brands. GS and OSB have vanilla lasts. It is what it is. Sorry if I hurt your delicate feelings.
(2 reacties met lagere score weggelaten)

=== THREAD 17dxz10 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-10-22  SCORE: 18  REACTIES: 60
TITEL: Foot leveler says I over pronate but shoes show supination
POST (source_id=post):
Over pronate but shoes look supinate

Hello everyone,
So I’m looking at new shoes for my daily walking for work. I have stenosis in L4 and L5 which made half my left foot up to the calf numb. My chiropractor got measurements last year and it shows my pronation to be moderate/severe at 113 which means I over pronate in my left leg. I bought the Hoka Arahi because of this and I also got custom orthotics from foot levelers. My shoes wear looks like I supinate which makes me think that maybe my orthotics is the cause of this? I read that it’s better to get neutral shoes for supination but I wanted to know if I should get stability shoes again. I bought ASICS Kayano 130 which is similar to my Arahi but should I go with the ghost 15 brooks? When I tried those on, they felt great but when standing in them compared to the ASICS, I felt more pressure on the bottom of my feet. 
Do you think I should sticks with the Kayano or should I get the neutral shoes because I feel the orthotics will help with the over pronation?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k5zmv1h] (score 62, diepte 0) Podiatrists trigger me a bit so take this with a brain of salt.  Those i cross paths with seem to have the same answer for everything, orthotics and stability shoes.
[k603khp] (score 27, diepte 1) This guy wasn't treated by a podiatrist. A licensed podiatrist would never recommend foot levelers.
[k5zqnhv] (score 24, diepte 0) You might be a rare pronating supinator
[k60dd3f] (score 23, diepte 2) This right here!

This chiropractor has bamboozled OP... They could do with seeing a qualified healthcare professional like a podiatrist or physiotherapist
[k5znnv9] (score 15, diepte 1) +1 on this. Honestly the best thing for most people is to work on muscle imbalances. There is no simple “cure”.
[k603h1c] (score 12, diepte 0) Oh foot levelers. Throw those away. Foot levelers is a scam. There's a reason no licsened podiatrist or pedorthist uses them. They prey on chiropractors who do not know much about feet anyway. Then the chiropractors and/or PTs sell them to everyone that will listen. They will also push you to get a bunch of pairs for every pair of shoes.

If you need custom orthotics, go to a licensed podiatrist who had a reputation for working with runners. Don't buy "orthotics" from chiropractors, PTs, or shoe salesmen. Rule of thumb: if they are evaluating your feet from a standing, weight bearing position, run away!
[k605zyk] (score 11, diepte 0) The whole pronation vs supination thing is dumb and needs to die. We are supposed to land supinated then pronate through and push off the mid foot and big toe. If you ding believe me, lol so videos of elite runners. You can’t tell much about how someone will do that from standing still.
[k6148co] (score 8, diepte 3) In my experience physical therapy is the best thing you can do unless you need surgery or or have a broken bone. They can help fix  the underlying muscle/strength problem. You also have to put in the work they give you. Not a doctor and this is just anecdotal so grain of salt and all that
[k5zwq04] (score 8, diepte 2) If you're struggling with running injuries, you should go to a sports physiotherapist, not Fleet Feet or chiropractors. Find a sports physio who specialises in running and they will be able to diagnose properly.

It's expensive but it will be worth it and will save you the money you're looking to spend on shoes to fix the issue. Shoes don't cure injuries, physiotherapy and prehab does.
[k5zt3bt] (score 7, diepte 0) I wouldn't try to read too much into the wear pattern on your shoes. The wear might just be caused by how your feet happen to scuff across the ground for example, not necessarily how you are landing. Has anyone watched you run and analyzed your running gait?

Also - note that custom orthotics are generally intended to be worn in neutral shoes. Did your podiatrist give you guidance on that?

And in terms of the Hoka Arahi - do you enjoy running in them? And do you find them comfortable? And are you able to run in them without pain/injury? If the answer all of those questions is yes, then I'd say there is no need to switch to another shoe.
[k60dkap] (score 5, diepte 1) This comment cracked me up, I hope you're being ironic and don't believe this is a thing
[k60e5nm] (score 5, diepte 1) This right here.

So many not so smart people believing in it though. 

Chiropractors, shoes sales people, etc will take people's money by telling them all sorts of misinformation
[k5zpx71] (score 4, diepte 1) What about when you run?
[k606bnp] (score 4, diepte 3) If you don’t know where those imbalances are then  yes that is a good way forward.
[k6115pv] (score 4, diepte 1) They utter "Brooks", in their sleep.
[k5zsriw] (score 4, diepte 0) How exactly do your shoes show supination? Just because shoes are more worn more on one side than the other, doesn't mean your supinating or pronating. It's more likely that you're just dragging your feet specifically in that area, but outsole wear is not indicative of pronation or supination at all.
[k5zkzna] (score 3, diepte 0 OP) Also, I went to fleet feet to get my shoes fitted and they say I have a low arch and then they told me I supinate when I walked on this pad barefoot
[k5zs656] (score 3, diepte 2 OP) Would a physical therapist be better for this?
[k60l076] (score 3, diepte 7) I’m not a physio, nor a medical professional. Will never claim to be. I am a certified running coach in the UK though.

And yes I’m confident in what I’m talking about due to the knowledge and understanding that I’ve learnt over many years of running, then reading many books and studies regarding running injuries, injury prevention and different running “trends”.

In terms of tests, the ones set out in [this book by Jay Dicharry](https://www.amazon.co.uk/Anatomy-Runners-Unlocking-Potential-Prevention/dp/1620871599/) worked well for me to assess the areas I should focus on.
[k5ztrzz] (score 3, diepte 0) Aren’t you supposed to wear neutrals with custom orthotics so you don’t get corrected too far over? 

I remember putting my custom orthotics in dress shoes but swapped to stability sneakers and they wore normally.
[k61ahcj] (score 3, diepte 1) This is the right answer. Don't wear corrective insoles with corrective shoes.
[k60lgfd] (score 3, diepte 0) Your feet behave differently when you’re running compared to when you’re standing still. The footscans are more beneficial if you just have pain while standing more so than when you’re being active. A physio will likely be better as they can check mechanics.
[k60vdhs] (score 3, diepte 0) Stop going to the chiropractor first.
[k61gi2n] (score 3, diepte 0) 1. cease going to the chiropractor, for anything 

2. get some neutral shoes and start strength training alongside your running routine
[k62vnox] (score 3, diepte 0) Chiropractors are quacks with a fancy name
[k687ypn] (score 2, diepte 2) He was treated by a chiropractor which is like going to a toothiologist with a dental issue.

Chirpopracy isn't a science, it's untested bullshit.
[k60du2g] (score 2, diepte 2) "I was just reading online"... This is your problem sadly. 

These comments are mostly misinformation and wrong, following advice online as opposed to going to see a *qualified* healthcare professional is what you're doing wrong
[k89eq7v] (score 2, diepte 2) Fleet feet measured me too. Said I pronate. The salesman came to this conclusion after having me stand still on a scale thing. He did not have me run or walk (even though there was a treadmill right next to it) he just said I pronate. I told him I just did a half marathon with basic running shoes from Payless (UA charged 8s) and that the outsides of my feet and knees are killing me.(it band problems) He told me to buy a pair of NB 860s v13s for mild over pronation or brooks adrenalines. He only had NBs in stock in one color and said that my feet and knees would continue to hurt without them. Well 50 miles later and I have worse IT band problems and constant injuries in my feet. Turns out I supinate when I run and stand neutral. I tried some orthotic inserts (super feet low arch run support) just made it worse. Would not trust (Madison, Wisconsin) fleet feet at all. Cut your losses and move on. 

Just get a neutral shoe dude and work on muscle strengthening. I do single calf raises, resistance band work, kettlebell/mobility exercises and try to cross train as much as possible. It takes a while for your ankles and feet to get stronger, but after you should be fine with most neutral running shoes.
[k604z7y] (score 2, diepte 1 OP) I actually went to a podiatrist and they gave me these hard plastic orthotics which I stopped wearing because it felt very uncomfortable and hurt my feet. But maybe that was because of the shoe I put them in
[k6056xv] (score 2, diepte 2) Was it a sports podiatrist that specifically works with runners? Some need a rigid orthotic but most do fine with semi rigid. How long did you wait to get acclimated to it?
[k63adl2] (score 2, diepte 4) Try finding a Podiatrist or PT that actually run. Local runners should be able to recommend one
[k60gv79] (score 2, diepte 3) Sadly the truth
[k61f2aj] (score 2, diepte 2) Certain brands that will not be named would die overnight if they had to stop selling their propaganda about pronating feet and the benefits of stability shoes.
[k64lpf6] (score 2, diepte 0) I have the same pattern. This is my best guess based on my particular running mechanics.

I’m flat footed and overpronate. I spent A Lot of time finding stability focused shoes until I gave up (like 15 different pairs) none of them felt right. In the end I landed on a pair of over the counter heat moulded inserts from Sole (they work great for me) inside a neutral pair of shoes like the Saucony Triumph 20s which offer some stability on top.

My tread wears out the same as you’re showing because I have incredibly tight and inflexible calves meaning I tend to land on the outer edge of my foot then roll inwards. This will show the wear pattern you’ve got.
[k65d5b2] (score 2, diepte 1 OP) Yes! That’s exactly what I do when I walk. My left calf is smaller and that’s is exactly what happens. I went and bought the ghost brooks 15, neutral shoes and put my orthotics in. I’ll see how it goes.  Thank you for sharing
[k60dhix] (score 1, diepte 4) Out of curiosity, how would YOU "know where those imbalances are"?
[k60gh2j] (score 1, diepte 5) Experience of running, understanding where your tightness and issues commonly materialise. Also numerous “tests” that you can perform yourself to work out those weaknesses.

I don’t deny that a physio/medical professional would be better at it than me working it out myself, but since I worked them out and worked on fixing them in a sensible fashion I’ve been running stronger, faster in races and without injury.
[k5zp4ic] (score 1, diepte 0) Shoes don’t lie!
[k6882e9] (score 1, diepte 1) Chiropractors do though
[k5ztqqk] (score 1, diepte 0 OP) Oh, they didn’t tell me it was for neutral shoe. To answer your other questions, they are extremely comfortable and I love them. I just noticed the wear on them and thought that they were the wrong shoes. No pain in the knees or any injuries. I do have back pain here and there and I’m not sure it’s the shoes. But if I stand too long, that’s when I felt it. Before I couldn’t stand more than 5 minutes before feeling an ache but now, I can go about 30-45 minutes before noticing anything p
[k5zuflf] (score 1, diepte 1 OP) They didn’t tell me that they are suppose to be in neutral shoes.
[k5zugde] (score 1, diepte 1 OP) They didn’t tell me that they are suppose to be in neutral shoes.
[k60dw4h] (score 1, diepte 1) Where did you learn this from?
[k60796k] (score 1, diepte 3 OP) Oh it wasn’t a sports podiatrist, maybe that is where it went wrong. This was a few years ago, so I can remember too well. I wore them for probably a year. I just felt it made no difference, felt awkward, and when I injured my back a second time with running in them ( I did Muay Thai and we did twice a week runs), I stopped wearing them
[k60fq8q] (score 1, diepte 2) Dumb people need to make a living too
[k63orwp] (score 1, diepte 3) Stability shoes still have benefits, but it’s not due to anything you can discern from static standing posture.
[k65g0ac] (score 1, diepte 2) Hope it works out for you.
[k66txt0] (score 1, diepte 0) I agree with comments to ignore this quack-y scam. Foot levelers (and custom orthotics) are a joke. I've tried every brand of insoles on the market because of my tendency to overpronate. Ultimately, I switched from my custom insoles to this brand called [Fulton](https://walkfulton.com) and nearly immediately my foot pain went away (& knee pain). These are made from cork so they mold to your arch and absorb shock/impact. a bit pricey but obviously way more affordable than custom, and really comfortable.
[k687r5k] (score 1, diepte 0) Here's a complete list of situations where a chiropractor can help you:




(Took a while to type all those out but I wanted to be exhaustive)
[ks942o4] (score 1, diepte 0) This doesn't show pronation. The report has their "crooked-man" skeleton to show you that your body is out of alignment, thus needing footlevelers orthotics to hold your adjustments longer.
[k5zs2zq] (score 0, diepte 2 OP) I try to avoid running because it puts too much pressure on my back and end up hurting it. My doctor said to avoid high impact sports which is why I don’t run or do marital arts anymore .
[k61f7s7] (score 0, diepte 3) Why would go to Fleet feet then?
[k60d803] (score 0, diepte 2) "muscles imbalances" is yet another thing the general population should stop obsessing about.
[k60gj67] (score 0, diepte 3) Why would the general population care about muscle imbalances?
[k60gtrs] (score 0, diepte 4) Exactly, why would they?
[k5zt711] (score 0, diepte 1 OP) I was just reading online. But I will say my custom orthotics was due to the foot levers says I overpronate (last year) but fleet feet says I supinate when they measured me yesterday
[k5zynv0] (score 0, diepte 0) I realized that clearly elevating the heel (ur insole seems to do that, making the drop even taller) puts the feet & muscles in an unnatural position and that leads to imbalance causing and exaggerating pron/supination, and then if you just use constantly these insoles your body never learns to actually run neutral (kinda) because it grows around having help. The moment I found shoes that fit me well I didn't have any more issues, often you just need a really good stable fit to have the needed support, not a fixing pattern
[k607l2f] (score 0, diepte 1 OP) Haha I just recently started reading into it. I hear what you are saying about standing still. When my podiatrist a few years ago gave me orthotics he said my ball of foot would kick/slide out which was happening. Foot levelers don’t measure me walking but fleetfeet did
[k60h30p] (score -1, diepte 6) Interested to know what tests I could do?

Also what does tightness mean?

Are you a physiotherapist? From your comments it seems like you are very confident in what you're talking about
[k60o4fz] (score -2, diepte 2) Good catch saw the orthotics and stability shows and the brain turned off
[k5zswfl] (score -2, diepte 1 OP) I was thinking this too! lol when I walked just know, I noticed my left foot does does touch the edge of my foot first. My right foot hits the floor inward. My left calf atrophied and is two inches smaller than my right calf and it’s been like that for a long time even when I try to work it out. Stenosis left my calf and foot numb which could be why. Maybe I should get a stability and neutral shoe? lol but all seriousness maybe neutral shoes and then hope the orthotics will help with overpronation?

=== THREAD a3uecc ===
SUBREDDIT: r/goodyearwelt
DATUM: 2018-12-07  SCORE: 43  REACTIES: 55
TITEL: You're screwed if you have big feet. I tried finding decent fitting boots over a year. (Size 14B US)
POST (source_id=post):
Preface: I have size 14B feet according to a brannock. This experience started due to the realisation that my Red Wing 875s didn't fit properly and my little toe was getting crushed to the point of significant discomfort. I live in the UK so you'll have to factor that in.

I'm going to list all the different boots I tried with their sizing advice in brackets. I'll then leave a comment.

* **Red Wing 875 - 13D** (go half a size down from brannock). Smushed my toes together so too small.

* **Red Wing 875 - 13EE** (go half a size down from brannock). Smushed my toes together so still too small. 

* **Red Wing 8119 - 13D** (go half to full size down from brannock). Smushed my toes together, length was fine.

* **Red Wing Beckman - 13D** (go half to full size down from brannock). Too narrow.

* **Thorogood Moc Toe - 14D** (go half size down from brannock). Way too big, lots of heel slip.

* **Thorogood Moc Toe - 13EE** (go half size down from brannock). Too short. Big toe sustaining too much rubbing.

* **Thorogood Moc Toe - 13D** (go half size down from brannock). Just too small everywhere.

* **LL Bean Katahdin (Same as Chippewa) - 14D** (go half size down from brannock). Too big, tried to wear them with insoles and the heel slip never went away. Started causing knee pain.

* **LL Bean Katahdin (Same as Chippewa) - 13EE** (go half size down from brannock). Too short. Big toes hitting the front of the boot.

* **LL Bean Katahdin (Same as Chippewa) - 13D** (go half size down from brannock). Too small everywhere.

* **Wolverine 1000 Mile - 13D** (go half to full size down from brannock). Too narrow. Length was good.

* **RM Williams Comfort - 13G(UK)** (TTS) - Too narrow and too short.

* **RM Williams Comfort - 13H(UK)** (TTS) - Too short but weirdly, very loose as well. Very weird fitting boot.

* **Solovair 8 inch Derby - 13UK** (TTS) - Too short and very strange fit. This boot probably uses the Dr Martens 59 last which is narrow and shorter than the *comfort last*. Shame because these were really nice boots. 

* **Dr Martens 1460 MONO - 13UK** (TTS) - Uses the 59 last so too short and too narrow.

* **Dr Martens 1460 Smooth - 13UK** (TTS) - It fits! Probably the comfort last.

* **Dr Martens 1460 MIE - 13UK** (TTS) - Uses the 59 last, too short and too narrow.

* **Loake Chatham - 12.5G UK** (???) - Probably a bit too narrow. Length was good.

* **Loake Chatham - 13G UK** (???) - Bit of heel slip so probably too big.

* **Sanders Thirsk - 13G UK** (???) - Who the hell is this boot for really? Entire last must've been shaped like a rugby ball.

* **Trickers Burford 13 UK** (TTS) - No heel slip, good width and length but maybe too roomy. Boot destroys my knees and feet.

* **Trickers Stow 13 UK** (TTS) - Seemed to fit great (same last as Burford) but I'm apprehensive after my prior experience.

* **Viberg Service Boot - 12E** (full size down) - END labelled their sizes incorrectly so yeah, this didn't fit.

So Jesus, that's quite a few pairs of boots I've tried on and I only managed to keep one pair (the trickers). Here's some thoughts I've gathered from all this:

1) The lack of half sizes when you enter clown-feet territory is awful. I understand why it's done (why cater to the 1%?) but man, it's frustrating to see so many pairs of shoes which would've most likely fit properly had a half size existed.

2) The European disdain for width-sizing is just as frustrating. The UK produces many fine pairs of shoes, but if one has an awkward foot width, it means that shoe is off limits.

3) Brannock sizing seems to completely break down at larger sizes. It seems weird to think my feet are a B width (and they really are) and yet, all these boots which were standard and wide widths provided all these problems for me. How does a 14B brannock end up requiring a 13G UK boot? Doesn't make any sense. If you have big feet, your Brannock size doesn't matter as far as I can tell. Especially width-wise.

4) Congratulations to [Loake](www.loake.co.uk) for actually providing size 12.5 UK/13.5 US shoes. I'm very confident I'll find some decent fitting shoes in their selection.

Conclusion: I think the lesson I've learnt from this is I should just go bespoke (or *custom* at the very least). If you have feet bigger than a 14 then you're even more screwed than I am. Feels bad man. I think people at the post office are starting to recognise me from all the returns I've done.

I'm not even sure if this post is actually worth reading. I just compiled my thoughts to assist my sanity.

**Boots on the horizon** - I'm not giving up, here's a list of boots which I'm keen to try on at some point: Viberg service boot, custom White's semi-dress, Solovair chelsea boot (different last to the derby).

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eb9ag27] (score 17, diepte 0) I feel your pain but in jeans. I'm a 30 waist and 36 inseam. Finding proper fitting jeans is a nightmare.
[eb9athy] (score 16, diepte 1) Lots of raw denim makers have long inseams, 36 is pretty long, but some of them get up there.
[eb9bux8] (score 14, diepte 0) Tell me about it. Size 16, here. Some days I want to unsubscribe from this sub when I see all these beautifully made boots I can never wear.
[eb9ceuo] (score 13, diepte 2) I thought 36 inches was the norm (if not longer), but I could be wrong.
[eb9izf8] (score 12, diepte 0) 15D here. White's and Wesco are your friend.
[eb9asrb] (score 7, diepte 0) Hey man! I feel your pain. I wear a 14D - 14E in all my sneakers. I don't know if thats my actual brannock measurement, but I wanted to make sure to give you a couple recommendations. 

Grant Stone's 13E fits excellently, after some break-in. Their Ottawa boot fit me flawlessly.

I wear a 13EEE in many Allen Edmonds; my most recent is a Randolph, and it may be one of my best fitting shoes yet.

Alden's Barrie last in 13E is one of my favorite things. Bit more expensive, but holy moly. Its comfortable.
[eb9ee5c] (score 7, diepte 0) I've found the Brannock device to be not very useful at larger sizes. You should have a look at Wesco boots - they have a huge range of stock sizes (4AA - 16EEE) and can do a truly custom fit as well for you.
[eb9bzkt] (score 5, diepte 0) You don’t need your big toe right? Wouldn’t that be easier?
[ebag6hf] (score 5, diepte 2) They do, but you forgot a crucial aspect with Alden... Since your size is so special, no returns.

If it doesn't fit, aw shucks, I guess you'll have to try a different size, wait another +6 months for a pair that might not fit, and resell this pair at a loss.
[eb9e1gt] (score 4, diepte 0) Whites has a ton of lasts (as in shear number of sizes and widths) including uncommon widths like C so I would go with that.  Most companies are not going to invest in widths beyond D or EE because once you cover normal and wide sizes that’s like 98% of people.
[eb9nsmd] (score 3, diepte 1) Look at higher end denim brands. Most jeans done with selvedge raw denim have 1 size inseam around 36 and you typically hem. r/rawdenim
[ebb5ab0] (score 3, diepte 1) I’m a 15. So I feel all of your pain. Finding regular shoes is a pain enough as it is.
[eb9bvbo] (score 3, diepte 0) I totally understand. My feet aren't as big as yours, but they're wide. Some shoes will work fine in regular widths, but I've decided to stop trying on shoes from brands that don't offer wide widths because too often I'm disappointed that no size fits me. Obviously this advice doesn't help you, but I do like your idea of going custom. Just can't justify the cost right now.
[ebabahx] (score 3, diepte 1) Alden too I believe goes up to absurd sizes. You just have to order through someone and wait a long time.
[eba4or4] (score 3, diepte 0) Try Winson or Zebshoes.
[eb9alig] (score 2, diepte 1) In second thought I can get my jeans tailored. Can't do that to boots. Your situations stinks. Tbh I haven't looked too much into it, but have you looked at Allen Edmonds? I know my dad has 13E, and I know his AE shoes are the only ones that fit him properly.
[eb9sjyr] (score 2, diepte 3) Standard unhemmed inseam is 34" for raw denim.
[eb9onhk] (score 2, diepte 1) Might I suggest [Dearborn](https://dearborndenim.us/collections/men/products/tailored-fit-medium-wash?variant=43402163782)? Go one waist size up for this fit.
[ebah8j1] (score 2, diepte 2) I will definitely check those out thank you!
[eb9b9ev] (score 2, diepte 0) Awesome list.  I'm about a size below yours, and wide, and I've all but given up on most of the common brands.

I'm hoping to pull the trigger on some custom from (I know you're in the UK but): [Rancourt & Co](https://www.rancourtandcompany.com/men-s/boots.html) in the new year, so will have to see how that goes.  They have a printable size guide to use on their site.
[ebcflbi] (score 2, diepte 1) Do you know any sneaker brands that have wide withs? I have yet to find any so i just make vans and converse stretch
[ebd46o1] (score 2, diepte 3) Ill will check it out
[eb9ofky] (score 2, diepte 0) Sounds like you need MTO and not bespoke ($$$!). 

Some of the Indonesian makers will have you send in a tracing of your foot. Perhaps that would work for you.
[eba6qml] (score 2, diepte 0) https://www.bakershoe.com/product/custom-semi-dress-whites-boots
[ebasqw5] (score 2, diepte 0) My experience with all 3 pair of my Thorogood boots is heel slip happens until they break it. My friend just got a pair of roofer boots and was thinking of adding padding for the heel slip, I told him to wait...now he says they’re perfect. 

Just saying, if heel slip was your only issue, you may want to reconsider.
[ebbh0e2] (score 2, diepte 0) Same problem, opposite direction (6.5 C). In terms of standard deviations from the mean, we are both less than 1% of the shoe market. Curse those 9Ds skewing the stats.

I've been very happy with service from Baker Shoe, they guarantee the fit if you use their sizing methods and guidance, and can broker Nicks, Whites and Wesco customs at fair prices.
[ebaoaib] (score 1, diepte 1) Iron Heart makes long inseams. I'm a 33x36
[ebaa9u4] (score 1, diepte 1) +1 on grant stone, 13D worked for me. I'm 14C and haven't had as much trouble finding boots that fit, however I may be less particular about analyzing the fit.
[ebax4to] (score 1, diepte 1) 14e/ee here. I thank you for testing the Alden’s out!
[ebcnut4] (score 1, diepte 2) New Balance! They're fairly good quality for the price. I feel like I have seen Asics in wide widths as well but haven't bought any.
[eb9e94i] (score 1, diepte 0) Try Crockett and Jones - some of their dress boot lasts are super long, so you might be able to get into a 12.5. They also fit narrower than standard so you can possibly get a decent fit.

&#x200B;

Otherwise, Edward Green makes everything in every width as far as I know, and I'm pretty sure there was a pair of bespoke George Cleverleys in size 13 on eBay recently / now.
[eb9gjk2] (score 1, diepte 0) Have you tried any MTO brands? I bet they might have lasts available for unusual sizes even if they don't need them often.
[eb9i1or] (score 1, diepte 0) I worked at a show factory for a couple of years - in the pattern room.  We had a policy of making custom for anyone with big or strange feet at the MSRP.   This included making a last etc right through finished product. A single designer would take it from start to finish. I usually graded and hand cut the leather. The designers told me this was pretty common practice.
[eb9nr34] (score 1, diepte 0) Here is my answer to everything. Have you tried Aldens? They have great lasts for wide feet that aren’t actually wide sizes, e.g. Barrie, Trubalance, Modified.
[eb9nyo8] (score 1, diepte 0) I have a Dalton in Dark Chili size 14 AAA Narrow coming in from Allen Edmonds. Interested?

These would be new in box, I will receive Monday.

&#x200B;

\*PMed
[eb9scol] (score 1, diepte 0) I am size 16 and bought boots four or five years ago from a company called Georgia Giant. They are definitely work boots but they are very well made for the price. I would recommend them.
[eba5937] (score 1, diepte 0) Just here as a to show my support to another 14B brother. Someone else who I’m competing with on eBay saved searches.
[ebabpxu] (score 1, diepte 0) At 12EEEE I feel your pain
[ebal1ii] (score 1, diepte 0) I dont quite understand this. My feet are 14D on the Brannock (14.5 on my left foot) and I hardly have any trouble with finding boots to fit. Red wings, wolverines, Justin's, Tecovas, Allen Edmonds never had an issue with any of them.
[ebao90w] (score 1, diepte 0) 14US here, can fit 13 Viberg & RW fortunately. I just did the Wesco [custom fitting program](https://www.wescoboots.com/builder/CustomFitting.aspx) so if you are wiling to drop some coin (looks like you are lol) then this might be worth looking into.
[ebaquq5] (score 1, diepte 0) It may need some updating, but there is a [Bigfoot's Guide](https://www.reddit.com/r/goodyearwelt/comments/3u3f58/the_bigfoots_guide_to_goodyearwelt).
[ebat2u6] (score 1, diepte 0) I have the same issue with condom
[muppaxn] (score 1, diepte 1) 14 NARROW????
[ebat31b] (score 1, diepte 0) Yep. My problem is I have a 12.5 /13  US boot but border on an A width.
[ebaw952] (score 1, diepte 0) Why not give a set of Nicks boots a shot? They do a fitment guaranty so if they don’t fit they make them fit. Hand made to each of your feet.
[ebax6l0] (score 1, diepte 0) I have kind of the opposite problem, I wear a size 8EEEE.  Trying to find shoes/boots that wide in such a small size is painful.
[ebdjuqz] (score 1, diepte 0) I feel your pain. I've got it even worse, my feet are all over the map. My feet measure a 13 heel to toe, but are 14.5 heel to ball, so that's what i try to fit. However, my width measures between an A and B, but i have an even narrower heel and low instep. I've been through all kinds of redwings and thorogoods. If i ever scrape the money together, i think I'm gonna order a pair of Whites made with their 38 swing last. I need the arch support or i start developing heel spurs and lower back pain. Sucks, cause redwing iron rangers are one of my favorite looking boots, but they just don't work for me.
[ebey0t3] (score 1, diepte 0) have you tried sizing up tho

&#x200B;

I have wide feet and wear true to size in red wing rather than size down and it works for me. you get a little heel slippage but they're sturdy and wear in to your feet a little anyway.
[ebf5ynq] (score 1, diepte 0) Maybe our friend /u/zebshoes/ could do something for you?
[ebh5vdy] (score 1, diepte 0) I’m a 14.5. Should I stay away from redwings then?
[ebhfuiq] (score 1, diepte 1 OP) You may be okay since some Red Wing models come in 14D
[ebj2uge] (score 1, diepte 0) Hey on the bright side when things go at super clearance your size is typically in stock, no?

Ask me how many times I ever see a 10 or 11...

OSB had waxed natural trench boots in the low/mid 200 range earlier today... got excited and clicked to see only size 14 listed.
[ec3aglb] (score 1, diepte 0) I wear a 13C or 13B depending on the maker and have a really narrow heel as in loafers I take a 12.5A.  I’ve just relented and gone with custom Alden’s after figuring out my size in the three or four most popular lasts...
[ef62fzw] (score 1, diepte 0) If you email me [customerservices@nps-shoes.com](mailto:customerservices@nps-shoes.com) I will be more than happy to send you a document of the internal dimensions of all the lasts we use in our manufacturing.
[eb9ibs2] (score 0, diepte 0) Try Cobbler Union, 312 last. If it works nicely, do MTOs and get any shoe you want made on it. Or just go with the ones they have (I don’t know how many pairs you’re looking for). The brand runs wide, and that last runs wide within the brand. Could help
[eb9swh1] (score -8, diepte 0) You've tried a lot of garbage shoes. 

Quit being a drama queen and buy a pair of Whites from Baker Shoes. Send in your foot tracings and STFU already. White's is the truth. As a person rocking a EEEE width, White's is the one and only answer.

