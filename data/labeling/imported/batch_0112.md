# Label-batch batch_0112

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
Schrijf het resultaat naar `batch_0112.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1cucih8, 2ten06, 7ec73o).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1cucih8 ===
SUBREDDIT: r/weddingplanning
DATUM: 2024-05-17  SCORE: 87  REACTIES: 216
TITEL: What are we wearing on our feet? 
POST (source_id=post):
This post is specifically towards the brides that can’t wear heels!  Show me your non-heeled wedding shoes!!! I’m thinking I wanna get lacey white sneakers but not 100% sure.
I have plantar fasciitis so I cannot wear heels or wedges without excruciating pain.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[l4htd3x] (score 97, diepte 0) I’m planning on wearing converse and embroidering flowers in my wedding colors on them.
[l4j9fkd] (score 59, diepte 0) I’m an amputee, and can’t wear heels without a special prosthesis. I didn’t want to be uncomfortable all day, so I opted for tennis shoes! Best decision ever. I was so comfortable all day!

https://preview.redd.it/gzj72vclx21d1.jpeg?width=1179&format=pjpg&auto=webp&s=64fd2772c79382de3a6eeda47280b3653a02fd9a
[l4htf5g] (score 45, diepte 0) I got [these](https://www.etsy.com/listing/974479106/venus-leather-ballet-flats-boho-wedding?click_key=aaec52ac185f3fca141f1451a728c0b269922407%3A974479106&click_sum=865e0a68&ref=shop_home_feat_3&frs=1) flats from BaliELF on etsy!

https://preview.redd.it/pb5105zz811d1.jpeg?width=4032&format=pjpg&auto=webp&s=12fc9021fc6cf0a32739ed728064a0d611e5418a
[l4igmo7] (score 41, diepte 0) My wedding is a long ways out but I’m planning on getting myself some nice birks

https://preview.redd.it/rtzkm3z1y11d1.jpeg?width=1179&format=pjpg&auto=webp&s=5f93d44e8ec14780d432b82c9fe1c3ee3d3756fa
[l4icz63] (score 36, diepte 1) converse currently has a line out that features embroidered flowers!!
[l4ibzwp] (score 36, diepte 0) https://preview.redd.it/xsp6qc6ws11d1.jpeg?width=1080&format=pjpg&auto=webp&s=9b5ef81951d62f3a156d859aa2ab983de6ec21c1
[l4htleb] (score 33, diepte 0) Betty Johnson pearl sneakers!
[l4i51oz] (score 29, diepte 0) I had emergency foot surgery 3 months before my wedding so I couldn’t wear heels either. I wore white Allbirds flats with inserts in them (my surgeon said that’s also recommended for plantar fasciitis) and I walked and danced all night in them. And one month before the wedding I could barely walk again, so I would definitely recommend the allbirds! If anyone is interested I can provide a link!
[l4iomyg] (score 20, diepte 0) Lowkey considering white chacos cause im ALWAYS in chacos for my plantar fasciitis…I already have such a strong tan line 😂
[l4ikuju] (score 19, diepte 2) Omg thank you for this info!! I was torn between converse or vans for the reception but this just sealed the deal for me
[l4i4ww9] (score 13, diepte 0) I’ll be wearing Tieks. I love the look of the Betsey Johnson flats and Badgley Mischka flats but unfortunately both were not comfortable for me, and life is too short to wear uncomfortable shoes!
[l4i5hr3] (score 13, diepte 0) I just bought these flats from Kailee P! They’re super cute and comfy so far https://www.kaileep.com/collections/bridalflats/products/white-satin-pointy-toe-flats-with-mini-pearls-and-ankle-strap
[l4idstj] (score 13, diepte 0) I’m thinking about wearing birks lol
[l4kd0gs] (score 13, diepte 0) https://preview.redd.it/pl70jiy9m41d1.jpeg?width=2000&format=pjpg&auto=webp&s=e57c5ddbf3a6b70755051ab9ddec174837bd0bfa

I am a crazy person and glued a shit ton of pearls to a pair of flats
[l4jf9ds] (score 11, diepte 1) Love the silk laces!!
[l4i0lrc] (score 10, diepte 0) Sparkly doc martens
[l4hu6sz] (score 9, diepte 0) Im going into some sparkly Keds from Kate Spade after the first dance!
[l4ip2q6] (score 9, diepte 0) Skechers floral sneakers! (Ignore the tag still one them)

https://preview.redd.it/a631q50t721d1.jpeg?width=1080&format=pjpg&auto=webp&s=943a8687d3bae488b3438eaa4bcbc1832518a6f0
[l4ix99t] (score 9, diepte 0) https://preview.redd.it/0hxzr7vyh21d1.jpeg?width=794&format=pjpg&auto=webp&s=d0025687bd8e8358c8156276059b1c36021c79f2
[l4ii3st] (score 8, diepte 1) I know this this is post about not heels. But I just absolutely love her shoes I got myself the booties!
[l4iqvgq] (score 8, diepte 0) Im going barefoot with Henna and jewery
[l4hpyza] (score 7, diepte 0) I wore platform sandals that I can rewear.
[l4l94rn] (score 7, diepte 1) https://preview.redd.it/31r48a0ge61d1.jpeg?width=1065&format=pjpg&auto=webp&s=b9dffa5ded523caff3323887a5688f7fc27a530f

I wore Tieks! They were so comfy
[l4iivpm] (score 7, diepte 1 OP) Link please!!
[l4id7qg] (score 7, diepte 0) I'm getting custom Chucks :)
[l4kqfuf] (score 6, diepte 1) I'm wearing converse high tops! 
I customized them on the converse website, they have a lace  pattern to complement my dress and they say "I do" on the mid sole. 
I usually love wearing heels, but we're having a backyard wedding and I didn't want to sink in the grass.
[l4l7aln] (score 6, diepte 2) I guess they technically will be! I really just wanted shoes I could wear again and I've always loved colorful shoes. Plus blue is FH's favorite color so I've been trying to incorporate it where I can!
[l4iduc0] (score 6, diepte 1) Her line is SO CUTE
[l4ifiii] (score 6, diepte 2) I love everything!!! I wanted the pearl boots, but decided it wasn't worth it to wear heels. And I think I could wear the sneakers for future things too!!! I'm so excited about them. And my dress has pearls on them!
[l4htodx] (score 6, diepte 0) So I bought the [Ivy Bella Belle](https://www.bellabelleshoes.com/collections/wedding-flats/products/ivy-lace-and-pearl-wedding-flats) flats second hand on Poshmark (because I’m not going to spend $400 on shoes I wear once lol) and also ordered [the Celia flats](https://www.bellabelleshoes.com/collections/wedding-flats/products/celia-dorsay-nude-lace-wedding-flats) to try on for sizing. I’m gonna be honest….neither are very comfortable. I have a slim foot but the toe box felt quite snug on either side of my foot. The company claims they make “the most comfortable long-wearing wedding shoes” so I was pretty surprised by how unimpressed I was. Especially for the price.

I wear a lot of [Birdies shoes](https://birdies.com/collections/all?filter.p.m.product.color_filter_values=White&filter.p.m.product.color_filter_values=Neutral&filter.p.m.product.color_filter_values=Gold&filter.p.m.product.color_filter_values=Silver&filter.v.availability=1) and they are SO comfy, so if any of their silver or gold flats are your style they might be worth checking out.

[Kailee P](https://www.kaileep.com/collections/women-shoes/bridal-flats) is another brand that has flats, as does [Betsy Johnson](https://betseyjohnson.com/collections/wedding-shoes?filters=Type,Type:Flats) and [Badgley Mischka](https://www.badgleymischka.com/wedding-shop/ceremony/bridal-shoes/#/filter:custom_heel_height:0-1in$2520Flat). I’m not loving BM’s current flat offerings but on Poshmark they have some really pretty ones from past seasons.
[l4ivz2b] (score 5, diepte 2) https://www.allbirds.com/products/womens-tree-breezers-natural-white?price-tiers=msrp%2Ctier-1%2Ctier-2%2Ctier-3%2Ctier-4

They are sooo comfy!
[l4i647m] (score 5, diepte 0) I got [these sandals](https://styletwits.com/products/melissa-femme-classy-sandal-2-colors?variant=40665731792975) in beige back when Melissa still had them in stock. My requirements were: must be mostly flat so I'm not towering over my fiancé, must be comfy and not pointy toed, not too dressy bc I want something I can wear again, and it needed a heel strap so my shoes aren't slapping around like flip flops or flying off my feet. I considered doing sneakers, especially ones embroidered with flowers or something cute, but really preferred sandals or something nice like that with my wedding dress. I was able to get these guys for about $10 on black Friday which I just took as a sign lol.
[l4i7gwd] (score 5, diepte 0) Docs for the ceremony and photos for a bit of height (I’ve had them years and they are moulded to my feet) then crocs for the reception meal etc
[l4ic6b6] (score 5, diepte 0) I wore Naturalizers :)
[l4ilox9] (score 5, diepte 0) I have plantar fasciitis! Platform heels actually don’t hurt me at all! But I still had some emergency nice looking sandals to change in to just in case lol. But I was fine!
[l4iolsc] (score 5, diepte 0) I got the Dr Marten Voss sandals in white. It looks like the white with white soles aren’t on their website anymore (or they are but there’s no option to purchase them so maybe they’re just out of stock?) but they’re so comfy. I wanted a platform but not a heel and wanted to make sure they were comfy and they’re sooo comfy.
[l4j5cqw] (score 5, diepte 1) Same here. I had those cute Betsey Johnson heels but they weigh 800 pounds so I was back in my rainbows as soon as possible 

We were in a beachfront house so it fit the vibe super well
[l4j5am8] (score 5, diepte 0) https://preview.redd.it/qd3dpoy5s21d1.jpeg?width=1290&format=pjpg&auto=webp&s=6536de19aaf85437fa207d280c7977272f913ccf

I got these from Target! They’re actually pretty cushioned for target shoes
[l4krrti] (score 4, diepte 1) omg were they your something blue 🥺 they’re so cute
[l4i1vlf] (score 4, diepte 0) Not me but my friends wife wore sneakers with pearls embroidered on them and put on a matching jacket with pearl accents during the reception it was cute
[l4ice5f] (score 4, diepte 0) I wore a pair of Bobs, [these](https:// www.rackroomshoes.com/p/
skechers-womens-flexpadrille-3-0-pastel-sky-slip-on-sneaker/105023) specifically. I have wide feet and shitty ankles. These are super duper comfy, feet didn't hurt a smidge the entire day. They actually swayed me away from continuing to wear converse as my daily wear lol.
[l4ihryp] (score 4, diepte 0) I wore silver Birdies mules that had a rhinestone strap. I’m also roughly my husband’s height so they’re my new go-to to most formal events.
[l4ivz6t] (score 4, diepte 0) https://preview.redd.it/z8pe6licg21d1.jpeg?width=3024&format=pjpg&auto=webp&s=2080216c439bf7a7b1ef034e9d6e2e1c4166b09c

These are mine!
[l4izeza] (score 4, diepte 0) I wore my flip flops 🤣 I had heels for the ceremony that I wore for first look, but they weren’t comfortable at all so I switched. For the reception I put on my white docs with blue laces.
[l4izuge] (score 4, diepte 0) I am wearing heels but I am also planning on getting custom Air Force Ones for when I take them off to dance! I definitely recommend this route, a good artist can customize them to make them look lacy. If you know any sneakerheads, ask them for recommendations or search #sneakerhead on the Gram
[l4j0a4p] (score 4, diepte 0) I got the Betsy Johnson pearl sneakers for my reception!
[l4jbcct] (score 4, diepte 0) https://preview.redd.it/ifezms95031d1.png?width=1080&format=pjpg&auto=webp&s=6b686c55553f348b46bd424b99fb9169d57cd958
[l4jht7z] (score 4, diepte 0) I found a bunch of listings for custom embroidered converse on Etsy, so my fiancee and I will both have embroidered converse with flowers and our wedding date!
[l4l8zk9] (score 4, diepte 0) I'm wearing these cute, breathable flats! My dress is blush and has similar detailing 🥰

https://preview.redd.it/wtl16pa9e61d1.png?width=1080&format=pjpg&auto=webp&s=561c958df1145a21b1607e22ec8b1187b468722f
[l4k8x7f] (score 3, diepte 1) No way this is literally what I’m doing too!!!
[l4kazth] (score 3, diepte 1) My cousin did this and they turned out so pretty!
[l4i3o7z] (score 3, diepte 0) I wore sparkly flats. Like  [these](https://www.macys.com/shop/product/betsey-johnson-womens-jude-evening-flats?ID=7133453)
[l4l7m63] (score 3, diepte 1) I love my allbirds! I wear them all the time
[l4j7lah] (score 3, diepte 1) Mine are very similar but without the pearl detailing. I'm 5'7" and the ceremony is outside - heels were never going to be an option🤣
[l4i7b9n] (score 3, diepte 0) AllBirds white flats
[l4i8q4v] (score 3, diepte 0) I wore naturalizers, plain white leather shoes with low heels, they were so comfortable
[l4ibzmu] (score 3, diepte 0) My DIL wore blue flats.
[l4mcpag] (score 3, diepte 1) kourtney and travis vibes!! (i sincerely mean that as a compliment btw haha)
[l4idau6] (score 3, diepte 0) White cloud slides 🫣 for a grassy outdoor wedding
[l4ife9q] (score 3, diepte 1) Yes I got white Birkenstocks!
[l4ifj8f] (score 3, diepte 0) I ordered "bridal" Keds an Amazon!

https://a.co/d/8MCPSYM
[l4ijhep] (score 3, diepte 0) I’m wearing heels for photos and ceremony but I’m changing into platform converse during cocktail hour!
[l4jkccl] (score 3, diepte 2) I got mine from the Philippines. But you can find some anywhere! I’ve seen them at macys, dillards, ect.
[l4la7d3] (score 3, diepte 1) What?!? Chacos caused my PF and tendon issues! I mean good for you, but I'm annoyed I can't wear them any more.
[l4iqbqx] (score 3, diepte 0) I got married a little over a decade ago and the no heels thing was the one thing my husband requested for the wedding because he’s already an inch shorter than me.

I looked everywhere for white lace ballet flats. At the time, you couldn’t find them anywhere. I ended up wearing white satin ballet flats.
[l4iqzbn] (score 3, diepte 0) Boots :) but my wedding is in a ranch so this was an easy out from heels.
[l4iv3ps] (score 3, diepte 0) I’m wearing a pair of crocs. It’s like sandals and lifts me up the perfect height for my dress so I do t have to get it altered. There’s no reason why anyone would see my feet because there’s so much fabric!
[l4mk383] (score 3, diepte 1) Your something blue!!
[l4jj226] (score 3, diepte 1) 😮 these are so beautiful
[l4ixtir] (score 3, diepte 0) I’m wearing white birkenstocks!
[l4iyw6x] (score 3, diepte 0) I'm going untraditional with burgundy heels for the ceremony and burgundy Keds for the ceremony to match my bridesmaids' dresses!
[l4j4c10] (score 3, diepte 0) I wore white ballet flats. Simple, comfortable, and cheap!
[l4jue6g] (score 3, diepte 1) I have had these in my cart today but I was disappointed they are more ivory 😭 They are so cute though!
[l4juqzb] (score 3, diepte 2) Ah yes they are more ivory! My dress is a non traditional color so the ivory didn’t really matter to me. I hope you find ones that work for you!
[l4j5df0] (score 3, diepte 0) These Birkenstock sneakers are listed as "seafoam" but in person they read as Tiffany Blue:

[https://www.birkenstock.com/us/bend-low-natural-leather/bendlow-smu-naturalleather-0-rubber-u\_11686.html?gad\_source=1&gclid=Cj0KCQjwgJyyBhCGARIsAK8LVLNWqkIBcgUSwner4jTVsxWVb3WDtGYO9zXFeG-nmolJ5ZduETEF0VIaAk10EALw\_wcB](https://www.birkenstock.com/us/bend-low-natural-leather/bendlow-smu-naturalleather-0-rubber-u_11686.html?gad_source=1&gclid=Cj0KCQjwgJyyBhCGARIsAK8LVLNWqkIBcgUSwner4jTVsxWVb3WDtGYO9zXFeG-nmolJ5ZduETEF0VIaAk10EALw_wcB)

I changed into them for dancing.

If you need legit legit arch support, converse or lacy white sneakers aren't really gonna cut it unless you add insoles.
[l4jg7ll] (score 3, diepte 1) Wow these are to die for!!
[l4l0w63] (score 3, diepte 1) Getting these same ones!!!!
[l4mcb9s] (score 3, diepte 1) i am wearing these exact shoes at my wedding in august!! they're surprisingly good quality too, considering the price!
[l4jb5wi] (score 3, diepte 0) I got custom light blue platform Converse for my wedding. They have dark blue hearts on the bottom, with our wedding date in white on the backs. As a bride that cannot wear heels, one recommendation: Spring the extra $5 for "comfort soles" in your Converse. The extra cushion was surprisingly worth it, even with socks.
[l4jbcg2] (score 3, diepte 0) I’m ordering from the converse wedding collection!
(158 reacties met lagere score weggelaten)

=== THREAD 2ten06 ===
SUBREDDIT: r/Fitness
DATUM: 2015-01-23  SCORE: 794  REACTIES: 170
TITEL: Finally found a quick way to squat with my heels on the ground, if it can help someone ( tight Achille tendon/flexibility issue for noobs...)
POST (source_id=post):
So I don't know how common this problem is, I thought it was anatomical and I would have to use a wedge all the time, but it's actually fixable in most cases.

If you have difficulties squatting without lifting your heels, you probably have a tight Achilles tendon or ankle joint. 

In order to fix it, you can stretch [the conventional way*](http://youtu.be/C-0Qe80fUaU?t=3m24s) or do what I did: 

Walk on an inclined treadmill (30°) and keep your feet, heel included, on the treadmill until the end of the motion - do not walk just on the front of your feet. It will hurt at the beginning but after 3 sessions ( 10 minutes each*) of doing that I was, to my surprise, able to squat normally and do the "third world squat" without falling :) 

Don't give up on this exercise even if you're having difficulties at first, it's pretty awesome when you can finally do it.

*Edited to add a few more details

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cnycx1b] (score 134, diepte 0) This is dynamic stretching.

There are actually a multitude of studies which compare dynamic stretching to static, and when you look into it, the dynamic stretching they use is "light jogging" for the calves.
[cnyjok7] (score 103, diepte 6) I didn't mention that because it's not true
[cnyjjuq] (score 66, diepte 4) I feel like this is talked about almost every day and people are always confused by it.

See [this review of stretching science](http://www.strengthandconditioningresearch.com/2013/11/18/stretching/) for starters.

While they cover acute performance reduction due to static stretching, that's not the primary reason it's a poor warmup. It's a poor warmup because it's a poor warmup. Stretching doesn't improve blood flow to tissues, raise the heart rate, recruit muscle fibers, or even prepare the CNS for certain movement patterns. In fact, it can engage the parasympathetic nervous system which is largely responsible for relaxation - something you do not want during exercise; you want the SNS engaged.
[cnyg2xe] (score 63, diepte 1) Yes, they should never leave the ground.
[cnyhsvt] (score 58, diepte 2) >Your ankles are just leg wrists and heels foot palms.

That sentence made more sense to me than it had any right to.
[cnyge3k] (score 44, diepte 2) I do not understand the question. Are you asking for the benefits and negatives of static and dynamic stretching? Both increase flexibility. Static stretching, however, is a poor warmup.
[cnyg1wo] (score 40, diepte 1) Yup. Compare to bench; you want to press straight through your wrists with your palms. Your ankles are just leg wrists and heels foot palms.
[cnymvya] (score 30, diepte 7) [X] rekt 

[ ] not rekt
[cnylrci] (score 30, diepte 2) Student physical therapist here: 

Solid research shows that static stretching will actually increase range of motion (slightly) more than dynamic for a period of time. HOWEVER, it also reduces your POWER output. If you are warming up to be able to weight lift or do powerful movements, you want to do dynamic stretching. 

It's always good to get a little bit warm before stretching (i.e. 5 min walking or on a stationary bike) to prevent a strain. 

However, while at home and when you're not going to prep for a workout, it's better to do static stretching once warm. Maximum benefits are gained at 30 seconds, except for the elderly which will receive a gain in range of motion up to 60 seconds. 

Hope that helped.
[cnyfla2] (score 29, diepte 0) Wow this is a great tip, will have to try it out... 

So your heels are suppose to remain on the ground throughout the squat? ... like the whole time?

EDIT: Ok I get it! I've never done squat. (...I'll see myself out)
[cnyjxxw] (score 18, diepte 7) That's badass
[cnyo8kf] (score 18, diepte 4) > Static stretching makes the body used to being in a more stretched position, while dynamic actually trains the muscle so that it can function in the new range.

This is nonsense. Flexibility is gained by desensitizing the stretch reflex. Both forms of stretching do this.

> If we only do static stretches there might come problems of us being able to move in ranges where we have no power, and harming ourselves.

This would be a fine sentiment if dynamic stretching trained the agonist muscle. It does not, it trains the antagonist. You still need to strength train the agonist in order to gain strength in newfound ranges of motion.

> Science isn't 100% clear yet

Science isn't 100% clear about most things. But we have best guesses. What happens when muscles stretch and how flexibility gained is pretty thoroughly researched, providing us enough information to make recommendations.
[cnytawc] (score 18, diepte 1) For some reason, I have a difficult time doing an empty bar. My balance feels way off with no weight on the bar.
[cnyg0s4] (score 17, diepte 1) What are some of the benefits/negatives of each?
[cnyiyoa] (score 16, diepte 2) > Your ankles are just leg wrists and heels foot palms.

[/r/nocontext](http://www.reddit.com/tb/2tfe3y)
[cnylv08] (score 16, diepte 5) To add, although you probably already know this, but putting more heavy weight on the front of your foot (i.e. balls of your feet/toes) will put a lot of stress on your knees. This becomes problematic as you get older.
[cnyjw6i] (score 15, diepte 0) You should also get flat bottom shoes. Biggest mistake is to do squats with arched shoes!!!!
[cnykqvl] (score 13, diepte 7) SAVAGE
[cnyl4g8] (score 13, diepte 3) Practicing the third world squat is good as well. Make sure to focus on keeping your heels down for that as well.
[cnyj7m4] (score 12, diepte 3) > Static stretching, however, is a poor warmup.

Do you have more information on that?
[cnyucb7] (score 11, diepte 5) God damn, people be gettin' shit on.
[cnyjbqv] (score 11, diepte 2) That's crazy. I never knew there were people who would squat on their toes basically. That sounds frighteningly unsafe and very painful.
[cnyy8d7] (score 10, diepte 8) Wow. That may have some connection to how frequently I tear the crotch out of pants. Guess I'll have to retire the "my penis thinks he's the kool-aid guy" story.
[cnykho8] (score 10, diepte 0) Oh man! This sounds like my exact problem! Thanks for the recommendation!
[cnynqrk] (score 9, diepte 5) I got coached towards better form by some really helpful coaches.  

Some *very* helpful exercises when you start are [wall squats and goblet squats](http://breakingmuscle.com/mobility-recovery/squat-therapy-4-drills-that-will-improve-your-squat).  Also, engage your core.  Most people with APT can rock their hips back with effort.  While squatting, take in a deep breath and squeeze your quads, butt and core.  Some people find it easier to stay on their heels with front squats.  

Finally, squat stretch every single day.  Every day.  Do it.  Don't not do it.
[cnynixu] (score 9, diepte 0) Does anyone else plop an empty bar on their back, and go A2G holding at the bottom a few times before adding any real weight?

That seems to loosen things up for me.  Although my problem is in the hip flexors and not the heels.
[cnyk9rj] (score 8, diepte 7) Daaamnn
[cnyko5z] (score 8, diepte 2) TIL I have been squatting wrong. I put the weigh ton the balls of my feet, will have to try OP's advice.
[cnyp2a5] (score 7, diepte 8) I think that would work better with the check boxes on the left side.
[cnyo5dm] (score 7, diepte 6) anterior pelvic tilt?

bad posture, sticking your ass out behind you and pushing the belly out in front
[cnylvo4] (score 7, diepte 3) > I put the weight on the balls of my feet

Damn, how much weight did you squat this way?
[cnylxnx] (score 7, diepte 4) I just recently got into weight lifting, I actually stopped doing squats because I knew my form wasn't great and I had the APT issue that is cuasing me to shift my weight to front of my feet, for now I just do other basic leg exercises until I correct my APT. I was only doing ~125lbs when I was doing it.
[cnyg6fb] (score 7, diepte 1) Yes, your heels should not only be on the ground, but your weight should be evenly distributed on the foot.  As OP noted, the move onto the toes is often caused by a lack of ankle flexibility.  You can put a small weight under your heels while developing that flexibility and it will help you squat without leaning forward.
[cnykjp3] (score 7, diepte 0) What about when the actual joint is too restrictive? I tried really hard over a couple days to stretch my achilles tendon but it turned out the joint was the problem, it started hurting in the *front* of the ankle where the shinbone connects to the foot during the stretching attempts. Is there any way to strongly mobilize the joint's range of motion in that direction? Is it even supposed to blockade at all?
[cnygchw] (score 6, diepte 2) I know there is research out there that says static stretching before activity can reduce the top end of your strength/power, so I only dynamic stretch before max attempts. I still static stretch before some of my lifts just because I like it
[cnyoiwh] (score 6, diepte 4) > So for short term mobility, at least one muscle group in at least one human continues to receive good benefits from static stretching for up to 3 minutes or so with absolutely nothing special happening at the 30 second mark. 

This is while standing, and you have an external load (your torso) pulling on the muscle. Try this while seated and I imagine you will not gain ROM for the full 3 minutes.

While it doesn't have an officially accepted term, using an external load to assist a stretch is commonly called "loaded stretching" and is an amazing way to gain flexibility.
[cnyt16h] (score 6, diepte 1) I don't think an arch is the problem, isn't it the soft padding/thickness of the sole?
[cnyb3q8] (score 5, diepte 0) I think I'll try this out...thanks!
[cnykh23] (score 5, diepte 4) Well, not stretching at all was a bad idea. But you probably were right with being less explosive.
[cnyqcmw] (score 5, diepte 5) I was curious about how phrakture warms up. So I googled and came up with [this](http://phraktured.net/molding-mobility.html) if anyone else was curious. Looks like another good way to increase mobility and I'm reading more about it now.
[cnyjiqo] (score 5, diepte 3 OP) I think very few people use the squat rack ( to do squats...they sure seem to have found other uses for it :p) because they fail miserably on their first attempt.

I was really close to giving up too  as I would often fall when attempting to do it, until I randomly hopped on that inclined treadmill.

At my gym I think maybe 5% of people do squats, but that may be because they just don't like doing legs...
[cnynw0l] (score 5, diepte 1) My coaches insisted I go barefoot until I got some proper shoes.  I never squatted in athletic shoes enough to notice the "instability" people refer to.
[cnyb1g8] (score 4, diepte 0) Thanks for sharing. I don't have that problem but I can only imagine how frustrating it is lol.
[cnytjdr] (score 4, diepte 7) AYYYYYYYY
[cnyj51b] (score 4, diepte 3) Where's 10-guy?
[cnyccp7] (score 3, diepte 0) If you have this problem early on, you might just need to give it time.  It took me a few weeks to stay back on my heels because it feels unnatural in a squat position because it felt like I would fall backwards doing it.  Other than OP's recommendation, I would also add that you should make sure you at the very least have shoes with a decent heel.  A pair of Nike Free 3.0's is going to be miserable.
[cnygk25] (score 3, diepte 1) Is this true? I've squatted barefoot since I started lifting and I have no problem staying back on my heels. Is it bad for me to do this?

When I'm at the gym I don't go barefoot I wear UTLab Ninjas which are flat.
[cnygtds] (score 3, diepte 2) He's saying people with ankle issues should use shoes with those heels, to compensate for those issues. If what you're doing works for you, keep doing it.
[cnym9pr] (score 3, diepte 3) I read on Chinese blogs (the official chinese weightlifting team's coaches' blog) that the Chinese weightlifting team actually do both static and dynamic stretches, and from their studies, static stretching does help them warm up, in addition to the usual benefits of stretching to reduce injury rates, which differs from the results of Western studies.

However, it's pretty much agreed from both sides that static stretching does reduce explosiveness and max strength for the session
[cnz1u9y] (score 3, diepte 6) [This research review](http://www.strengthandconditioningresearch.com/2013/11/18/stretching/), which is linked up the chain, covers 4 meta analyses that cover 19 different studies on stretching and injury rates. The authors conclude:

> In summary, the literature is conflicting whether regular stretching appears to be ineffective for reducing the risk of sports injury, whether the stretching is performed immediately prior to exercise or at another time.

This is not the same as what I said above, it's important to understand that a "unclear" or "conflicting" result for these sorts of things means that it should not be recommended for this modality. The research is slightly unclear (though, more studies than not show no reduction in injury rate), which means we don't know WHY it is unclear.

They authors later conclude the paper with:

> It is unclear at present whether regular stretching is effective for reducing the risk of sports injury, either when the stretching is performed immediately prior to exercise or at another time. Coaches looking to reduce injury risk in their athletes should therefore look to other training modalities for this purpose.
[cnz304i] (score 3, diepte 7) (Someone already did the Rekt thing earlier)
[cnymupv] (score 3, diepte 3) Great actually! I've been doing static warrior pose after my workouts to loosen up my tight, APT-inducing, hips, and now I know that I gotta make that extra push to 30 seconds.
[cnynbyb] (score 3, diepte 3) This is just an anecdote, so I recognize its light value but thought I'd share since it seems to be a recurring observation opposed to the 30 second to a minute claim:

When my hamstrings are tight (I haven't worked out that day) and I stretch cold, it takes me over a minute to be able to reach my toes with 99% straight legs.  But if I hold the stretch and don't push too hard, I will always get there.  

Occasionally if I hold it for a long time, I will be able to bend my fingers by pressing the tips against the ground.  

So for short term mobility, at least one muscle group in at least one human continues to receive good benefits from static stretching for up to 3 minutes or so with absolutely nothing special happening at the 30 second mark.  

Also, be skeptical of nice round numbers whenever you are talking about physiology.  Our bodies are noisy scribbles of data, and each of us different.  30 seconds and a minute are just nice clean numbers for our brains, and our muscles have no idea what a "reasonable" interval is.
[cnz0cq7] (score 3, diepte 4) > Our bodies are noisy scribbles of data,

Best description of a human body I have read in a while.  Thanks.
[cnylc8z] (score 3, diepte 4) Third World Squat? Going to have to look that one up. I have APT so after reading some comments here I believe that's the main reason I cant go heel to ground, but I have been working on my APT for about 3 weeks now with some improvement.
[cnynoqd] (score 3, diepte 5) > APT

What is this?
[cnyofrl] (score 3, diepte 9) Guess i should work harder.
[cnyqw31] (score 3, diepte 7) Yup, I never realized my posture was that bad until someone pointed it out at the gym. I went online, examined my posture, and realized why I have so many issues. Clothes don't fit right either due to APT.
[cnykav9] (score 3, diepte 1) I think squat shoes help with ankle mobility issues, and help you get proper depth.
[cnz2gg6] (score 3, diepte 3) I just wanted to point out that having arch supports isn't a bad thing. It helps me to distribute weight properly across my feet and reduces stress on my knees. (Bunion, flat footed)
[cnyopff] (score 3, diepte 1) You'll want to stretch for more than just a couple days, it could take weeks to notice much but make sure you're not over stretching and pushing to hard, that might be why you feel that pain. Also, stretch your hips ALOT because that could help your back stay straight while your hips bend. The reason I say that is because I used to not be on the heals super well and stretched my Achilles thinking it was that but it was actually because my hips were to tight so my back would go forward and to compensate I would come up a tad on my heals
[cnyyuue] (score 3, diepte 2) I have this problem. What kind of hip stretches did you use?
[cnykrwd] (score 3, diepte 1 OP) This is the "static" way to do it, didn't really work for me but if you don't have access to an inclined treadmill you should give it a try

http://youtu.be/C-0Qe80fUaU?t=3m20s
[cnyl5mc] (score 3, diepte 0) Thank you for this tip, I will try it.  If I can improve in just a few sessions, or even a few weeks, that will be amazing.

I've tried stretching and 3rd world squatting with assistance for balance for MONTHS with little or no results.  I'll give it a shot!
[cnyvb4b] (score 3, diepte 2) Try it with the bar in the front.  Or add a couple of 25s or something light.
[cnyt8y6] (score 3, diepte 1) That's to strengthen the muscles on your shins. This is more akin to heel-drops.
[cnyowy7] (score 2, diepte 3) I'm putting together a form check video of deads and squats. 

Just looking at the vid myself I realized I have some issues that need fixing.
[cnyrotj] (score 2, diepte 1) Sorry - but this is terrible advice.

Giving someone lifters or shoes with a heel to squat in, when they already have dorsiflexion problems, is feeding the issue. Instead of squatting with weight, they should be working ankle dorsiflexion drills, probably doing a load of hip openers to loosen up there pelvis, and using goblet squats and wall squats as corrective exercises to reset movement patterns and get used to the feeling of weight through the heels. 
Goblet squats can become heavy if they want to feel the burn, but not before the above is addressed.

Keep in mind - for a lot of people who sit down all day long, and dont have active lifestyles etc, this can take weeks to months to get happening properly. It all depends on the client or person training and how willing they are to do the daily work. 

Source: Correcting literally hundreds of people's squats in fitness classes and PT sessions.
[cnyx6re] (score 2, diepte 5) You sound very sure when there are studies everywhere that contradict one another.

Do you have any good sources backing that up?
[cnypcmc] (score 2, diepte 7) Ooooo kill 'em!
[cnyqlea] (score 2, diepte 6) This is also linked in the wiki.
[cnyg29s] (score 2, diepte 1 OP) Yes otherwise you can lose balance and fall when you're carrying heavy weights...:/ It's dangerous and pretty humiliating 

I thought this was the most helpful video for this exercise

https://www.youtube.com/watch?v=Dy28eq2PjcM
[cnyod5l] (score 2, diepte 8) it seems to be fairly common, luckily enough it also seems quite fixable with a little bit of work and time
[cnypvym] (score 2, diepte 11) Well, I had an idea that I probably have such an issue but never directly worked on it.  I've *always* been inflexible so I kind of just let it ride.
[cnyn8bg] (score 2, diepte 7) sounds like you'll make it, brah
[cnyxj9c] (score 2, diepte 6) Thanks Tony! I am reading into those squats now.
[cnyvquu] (score 2, diepte 3) I'm really glad you learned this because coming up onto your toes would be down right dangerous once you start lifting heavier and heavier weight. 

Also, /u/tony_chu made some great suggestions for you if you feel like getting back into it.
(91 reacties met lagere score weggelaten)

=== THREAD 7ec73o ===
SUBREDDIT: r/xxfitness
DATUM: 2017-11-20  SCORE: 1794  REACTIES: 145
TITEL: I'm The Morbidly Obese Girl Who Posted Two Days Ago About Blistering Feet And Other Beginners' Issues. I Can't Believe The Progress I Have Already Made. You All Are Incredible! (Update)
POST (source_id=post):
Hello again, ladies!

Well...  This has been completely unexpected.  It is freaking blowing my mind!  The physical and mental changes that have already occurred in less than a week are nearly unbelievable.  Where do I start...?  Let me try to break it down into bullet points.  Hopefully this will encourage some of you lurking ladies with similar struggles to get up and moving!

*  I have had insomnia for about 4 years now.  I have slept about as much in the past *five days* as I was averaging *per month.*  I've been getting about 8-9 hours of sleep a night, only waking up to use the bathroom then immediately falling asleep again.  This means I am no longer taking 50mg of trazodone *plus* 50mg of diphenhydramine per night to only get 2-3 hours of sleep at best.  Holy crap...

*  I have more energy.  Obviously, part of this would stem from actually being able to sleep again.  But even after going hard at walking and/or jogging for 3 hours per day, I am more energized than I was before.  The runner's high is a real thing.  When I started, I thought I would just come home and crash.  **Nope!**  I'm catching up on all of the housework that has been neglected for a month or so.

*  This is the least anxiety that I have ever felt.  Even when I think about being a little girl, I cannot remember anxiety levels that were this low.  Now, it is most certainly still present, but it has gone from dangerously high to the point that I couldn't cope with daily life 
to something that is more than manageable without medication.  It has shocked my family, friends, psychiatrist, and therapist.  My mental health team has been stressing an increase in physical activity for years, as well as my other doctors and specialists.  But, to quote my psychiatrist, he said, "This sort of change in this amount of time is unprecedented in my experience.  You have even more potential than we have given you credit for."

*  The same is true for my depression.  I feel like I'm in a new world.

*  I don't want to get drunk anymore.  I don't feel the need.  No cravings and no temptation.

* It takes *significantly* more movement to get me out of breath.  A week ago I couldn't walk up half of the 15 stairs to my apartment door located immediately at the top.  Now it's just like walking on a flat surface.  I'm definitely no star athlete, but I thought this would take months to accomplish.

*  My body is healing faster.  I had some deep wounds from self-harming the day before I began walking.  They were deeper than usual and are nearly healed now (it usually takes at least two weeks for scabbing to go away).  It's beautiful, and so symbolic of the changes I'm initiating.

Here are some of the pointers that I have adopted that have made things even better!

*  Athletic tape on hot spots and non-cotton socks.  Girls!  My feet feel *great* today after about a 3.80 mile hike around the lake.  I took it easy yesterday to give my feet a rest (I only walked about a mile and a half).  Note that this is very rough terrain with multiple steep inclines and rapid elevation changes.  The three hills I have to go up at the end of the trail have even been named by the park service as "Pain," "Misery," and "Hope."  What's even better?  **I got these new socks and athletic tape at the Dollar Tree because I am out of work and we are struggling financially at the moment.**

*  Foot pampering, such as soaking, lotions (not on blisters that have popped, of course.)

*  Slowing it down.  I intend to walk at least 3 miles daily 5-6 days per week with a maximum of 4.25 for the time being.  I was able to push myself harder going a shorter distance, which, ultimately, made it much more of a success.  MFP and another app I'm using said, today, I burned more calories than during any walk so far even though the time was quite a bit less and the distance was much less.  I was able to push myself harder and keep my heartrate higher (my phone measures bpm and oxygen saturation in my blood).  As a conservative estimate, *I burned about 250 extra calories in less time and over a lesser distance.*  Based on what MFP and my other apps say, though, it was closer to an extra 320.  That's cool!

My parents were elated to hear that I want an REI gift card for Christmas (my dad especially).  The support from this community, my family, and the few close friends I have shared this with, has been overwhelming.  Not only does it motivate me due to their encouragement, but telling other people has given me a new level of accountability.  I can't wait to show them what I've got.

TL;DR:  Based on your suggestions and my persistence, things are going better than anyone, including my doctors, could have anticipated.  You are all amazing!  :)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dq3z4mj] (score 349, diepte 0) You are doing a great job! Your story would be fit in /r/EOOD, which stands for “exercising out of depression”, if you wish to share it there.
[dq3yju9] (score 147, diepte 0) So fucking proud of you and you’ve inspired me to get off my ass!
[dq408bu] (score 137, diepte 0) You are amazing, and you can do this! I was in your position 10 years ago, and now I'm fit as hell. That's going to be you before long.

And the anxiety reducing effect is huge and real - as you see. I depend on exercise to handle my anxiety, and it works. You're developing a really powerful tool here to change your entire life. Good luck, and I hope you enjoy the process.
[dq3zwb1] (score 101, diepte 1 OP) Wow, didn't even know that was a sub!  I will certainly post it there.  Thank you!  :D
[dq41jh8] (score 58, diepte 0) I think I missed your first post but wow, this has got to be one of the most cheerful and uplifting posts I’ve seen in a long while. It’s really heartwarming to read about how much better you’re feeling and how bloody happy you are for it. If things are good now, imagine how you’re going to feel this time next year!
[dq40090] (score 56, diepte 1 OP) Thank you!  Getting up and active is much easier (and much, much more fun) than it sounds.  :)
[dq419b2] (score 48, diepte 1 OP) Awesome!  I love hearing stories from people who have made it a permanent lifestyle choice.  That is my goal.  This is the cheapest, most effective health-boost I have ever had.  I'm having a blast!
[dq3xxez] (score 41, diepte 0) Amazing! What a great start, I’m so glad you’re feeling positive :)
[dq49r7u] (score 38, diepte 0) >  I got these new socks and athletic tape at the Dollar Tree because I am out of work and we are struggling financially at the moment.

I am the one who recommended double-layer socks. If you want to try them out, I'll ship a pair or two to your house. Feel free to PM me!
[dq41uf8] (score 36, diepte 1 OP) Thank you!

Thinking about how I'll feel a year from now...  It's indescribable.  I can say without exaggeration that this is the most hopeful, positive outlook I have ever had for the future.  Especially after 7 years of consistent failure in nearly everything I did (which is something I was not used to when it started happening), I feel like I'm getting back on track.  :)
[dq3yshb] (score 34, diepte 0) This is such a joy to read! Keep up the incredible work mate. Be proud of yourself and know you have all of our support ❤️
[dq4ny6v] (score 30, diepte 1) I love finding random subs in comments, I work midnights and with this winter sunlight crap its really been making me have the blues pretty bad lately. Gonna go read up in this sub now thank you :D
[dq44ge1] (score 29, diepte 0) As someone who struggles with severe anxiety and depression, I feel you on this. Even with meds, my issues are not managed without regular exercise. I do strength training at the gym with great physical and mental results, but have wanted to get into hiking and outdoor exercise for awhile now. You are such an inspiration to get the hell outside and let the sunshine and fresh air reset my brain chemicals. I’m so proud of you - your post made me tear up 💜
[dq406vy] (score 19, diepte 0) Love how positive and driven you are! Truly uplifting to see this update. Keep going <3
[dq4f6ew] (score 18, diepte 1 OP) Oh my gosh!  Thank you!!!  I would *love* to try those out!
[dq43jb7] (score 17, diepte 2) Exercise helps my anxiety so much too! Even if I do have a bad day (which rarely happen), I know that I just need to hit the gym and I’ll feel 100x better!
[dq432qa] (score 17, diepte 0) This is really inspiring.  I went back to the gym today after a long lapse and weight gain.  It was discouraging to realize how out of shape I’m in.  Thanks for being so positive and inspiring me to stick with it!
[dq451by] (score 17, diepte 0) I was getting teary eyed reading this, I am so happy for you!! My dear sister in law is morbidly obese, but has recently begun walking, eating better, and making other positive changes, and I hope she does as well as you have!
[dq416my] (score 16, diepte 1 OP) Thank you!  I'm through the hardest part-- getting started.  Now that I've got some solid momentum going, I'll be damned if I stop.  It's amazing!  :)  <3
[dq42xbg] (score 14, diepte 2) If you're on instagram, check out Fatgirlfedup. She's amazing, motivational, inspirational, and has lost 303 pounds with more to go.
[dq4n3v2] (score 13, diepte 2) If you do lose your momentum - don't beat yourself up. Just remember how good this feels, scale back a bit, and then pick it up again when you're ready. It's not always going to be amazing - that's just life. Go hard when you feel like it, take a break when you need, and cut yourself a lot of slack.
[dq40xfy] (score 13, diepte 0) I came across your post browsing randomly. Keep up the great work! I'm so happy for you :D
[dq4w78k] (score 12, diepte 2) Look into getting a light box. You may not have a full blown case of SAD, or seasonal affect disorder, but look into it and see your doctor.
[dq4eno2] (score 11, diepte 1 OP) Aww!  Thank you!  There is a big difference to me when I get exercise outside versus being in a gym.  I do plan on transitioning to the gym as it gets colder out, but I likely will not be going there as much as I go outside still.  The cold doesn't really bother me.  Rain is more of an issue, though.  :p
[dq47g4q] (score 11, diepte 0) Girl I am SO fucking proud of you.  You're off to a great start - when you feel like you don't wanna get up and exercise, fuckin' do it anyway because even if you feel like you're not seeing progress, you're cementing your good habits.  If you backslide a little, don't beat yourself up too  much - just do better tomorrow.
[dq3z2xb] (score 10, diepte 0) KEEP IT UP GURL!!! :))) you’re doing fantastic.
[dq49uax] (score 8, diepte 3) I absolutely depend on it. I have to structure my life so that I get the exercise I need, which can be a pain, at times, but it's a lot easier than suffering needlessly or taking drugs with crummy side effects.
[dq43rsw] (score 8, diepte 1 OP) Thank you!  Even if you have backtracked a bit, you can always choose to move forward.  For me, being in the worst shape of my life is what finally got me up and has kept me moving.  Remember your previous potential.  If you did that, you can do even more!  :)
[dq4eh0c] (score 8, diepte 1 OP) No.  I have never been.  I was incorrectly diagnosed with bipolar disorder several years ago and it was only during a hospitalization in the early summer of this year that they determined that this was an incorrect diagnosis.  They did a *lot* of testing on me to deduce that I have major depression instead, and also apparently interviewed my parents, sister, fiance, and my two closest friends.
[dq4wb42] (score 7, diepte 3) Can you just buy those online? I may have to make an appt with a GP and see what they can help me with, switching shifts isn't really an option currently
[dq4ylz6] (score 7, diepte 4) I have a light box at work that I got on Amazon to wake me up in the morning.
[dq40731] (score 7, diepte 0) Great work!!! Proud of you!
[dq433f6] (score 7, diepte 0) Just had to congratulate you and tell you how happy it made me to read this!

I hope you keep it up and continue to find joy and success. Hold onto this feeling and use it to get you through the tough moments!
[dq4lx4h] (score 7, diepte 0) You are amazing, and I really hope you share your journey with us, and I wish all the best to you!

Some days are going to be tougher than others, some days you'll feel weaker than others, some days stronger. But don't let it discourage or hold you back, and don't feel bad and come down on yourself if you give in now and again! I know it's easy to get caught up in the dismal mindset of "I should have done *this*.." "I'm such a failure for not doing *that*.." or "Ugh I'm just a loathsome piece of shit, why do I even bother.." and let it rule you some days, but a day off is allowed! And try to combat those thoughts with self-empowering ones (for some strange reason I feel too self conscious to type those out, I can't bare *that much* of myself to strangers). Also, if you don't do your exercise you have set for that day, remind yourself that tomorrow is a new day with new opportunities and challenges for you to conquer! But on those days when you fight through it and do it anyway, you'll feel empowered and elevated. Something my therapist suggested to me was to keep a workout journal. Write down what I did, the good, the bad, etc, but always end on a positive note.

I feel like I'm sort of being a downer with my comment. I'm really not intending to be, I just want you to know that it's okay to feel like that, to have those days... they will leave you alone and not take over the more you do it. But, you've got this. You've already overcome the hardest part! I'm excited for you!
[dq4o3pc] (score 6, diepte 1) That's a subreddit? Holy crap, awesome! I doubt I'll ever get off SSRIs, but exercise does help a lot.
[dq410gj] (score 6, diepte 1 OP) Thank you!  I surely will!  😀
[dq46txk] (score 6, diepte 1) My dad does this, since he has buckets and buckets of it around on the farm, lol.
[dq423no] (score 6, diepte 0) I am so excited for you!  Keep going!
[dq47vkc] (score 6, diepte 0) Congrats OP!! I'm so happy to see this update. Just remember to look back on why you're doing this when things get tough and you want to give up. It's okay, most of us experience it at some point in time!
[dq4jetf] (score 5, diepte 1) Not OP, but I'm going to look for that. Thank you for the suggestion. Sadly, my hands aren't blistered from something fun like rowing, but from gripping a steering wheel at my driving heavy job. :(
[dq44ukq] (score 5, diepte 0) Gl on your journey.  It won’t be easy but it will be so worth it!
[dq4eqlp] (score 5, diepte 1 OP) Thank you!  Keep encouraging her, and I'm sure she will!  I have found that I am eating much less without trying but am also inadvertently eating better as well.  I think it's because I'm not able to eat as much, so I'm able to afford more expensive, healthier options.  :)
[dq458qf] (score 5, diepte 0) This is amazing. There’s nothing like a bucket full of positive reinforcement to continually remind you that you’re in the right place, especially when you’re putting so much of your mental and physical energy into something. That can feel sort of displaced no matter the pursuit, and getting that immediate return is just an incredible feeling. Plus, you have so much return later to look forward to. Health is the gift that keeps on giving. I’m so happy for you!
[dq45t25] (score 5, diepte 0) this is amazing to read! Keep it up girl! I wanted to ask if you live in the country or next to a park where you have these walks available to you? I’d love to do what you are doing but  I’m in the middle of a big city and worried about pollution
[dq4f1me] (score 5, diepte 1 OP) I actually live in Raleigh, NC.  This is about the citiest (lol) that it gets here.  But people here like their nature.  There are a lot of parks and nature trails within 5-15 minutes of me, and even more within 30-35 minutes away.  I've been using a map called All Trails to find different trails based on distance from my home, type of trial, trail length, difficulty, and whatnot.  The trail I have been using is the second closest one to me being less than ten minutes away.
[dq47l6z] (score 5, diepte 0) That is absolutely incredible, is it weird to feel proud of a stranger because I am so proud! What a world of change for you! You've got me super motivated to go take a walk too, except that's probably a bad idea with the flu. Also, Dollar Tree ftw, half of my family's kitchen is stocked with cooking utensils from that store.
[dq4aozg] (score 5, diepte 0) I am really excited for a 6 mnth and 1 year update! dont forget to come back later and show us how much ass you have been kicking!
[dq4fjod] (score 5, diepte 0) *I don't want to get drunk anymore. I don't feel the need. No cravings and no temptation.*

This right here. I need to start running again for this very reason.

Thank you for inspiring me!
[dq4mjzr] (score 5, diepte 0) Hey, great work! Just a caveat: trackers can quite easily over-estimate calorie burn. Take care if you're eating back your exercise calories that you're not relying too much on that number. :) 320 actually sounds pretty reasonable for the distance though.

Keep it up! Motivation is fleeting, so when you find it flagging or you want to skip a day, remember that you're building a habit and that means heading out on days that maybe you don't want to. You'll find that it's very rare to regret a workout. Once you get out there you'll feel great :) and you know that already from the experiences you've had so far.

Cheering you on!
[dq43nqa] (score 4, diepte 3 OP) Will do!  Thank you!  :)
[dq44d31] (score 4, diepte 0) Hey girl, keep it up. You're giving the rest of us lots of inspiration!
[dq4yroe] (score 4, diepte 2) Get a good rain jacket and you'll be fine! There is very little truly bad weather, just the wrong clothes.

Source: Grew up in Ireland
[dq45fyu] (score 4, diepte 0) This made me SO happy to read, you go girl!!! Keep on moving and it’ll only get better. I did miss your first post- can you (or anyone) comment with a link to it so I can check it out?? Woohoo for progress!!
[dq45q2y] (score 4, diepte 0) Yay! You got this :D
[dq4pq1y] (score 4, diepte 2) Even if you never share it with anyone else, you will be so glad you have it for you. It’ll help make you thankful for ever day you’re less that person and more the happy, healthy, positive person you’re becoming in these posts and on those hikes. If you hit a rough patch in the future, it’s nice to look at that picture and go, “whoa. I’m so not that person anymore.”
[dq4fop9] (score 4, diepte 0) This is wonderful to read! I started biking and running after I got out of rehab for substance abuse four years ago, and it has completely changed my life. Being outdoors and being active are the foundation of my sobriety and maintaining my mental health. I'm amazed at how its kept my depression and anxiety at bay. Best of luck on your journey! 🖤
[dq4fs06] (score 4, diepte 0) This makes me happy! You go girl! ✊🏻
[dq4w8k6] (score 4, diepte 0) Not sure if it’s been mentioned but [if your shoes rub the tops of your feet, your toes feel too restricted, the shoe feels too tight on the top of your feet, or your heels slip up and down you may find that using an alternate shoe lacing method will reduce pain.](https://lifehacker.com/5864915/reduce-foot-pain-with-alternate-shoe-lacing-methods/amp).
(87 reacties met lagere score weggelaten)

