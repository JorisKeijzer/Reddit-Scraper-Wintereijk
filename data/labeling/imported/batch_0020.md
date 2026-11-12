# Label-batch batch_0020

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
Schrijf het resultaat naar `batch_0020.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1fvksnb, zq0j2o, tz7r1f).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1fvksnb ===
SUBREDDIT: r/ChronicPain
DATUM: 2024-10-03  SCORE: 11  REACTIES: 58
TITEL: What shoes should I look into getting for back pain and sciatica? 
POST (source_id=post):
The one thing I have yet to change is the shoes I wear. I just wear vans. My father wants to take me somewhere to get insoles sometime down the line but for now I just need recommendations on shoes. Just something for everyday wear and/or light exercise (like walking shoes). I just am unsure about what to consider when shopping for shoes to potentially help these issues.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lq7sx8c] (score 10, diepte 0) I love my Vans but they have zero support. I went to a podiatrist and got insoles made.
[lq7w69j] (score 9, diepte 0) I got a pair of Brooks ghost, and they are the best shoes I've ever bought. I've had 3 spinal fusions and 2 plates with 6 screws put in my right foot.
[lq7tdsd] (score 7, diepte 0) I live in birkenstocks as long as there's no snow. The arch support helps
[lq7u7an] (score 6, diepte 2) No problem, back pain really sucks. I've tried a lot of shoes and I really like these
[lq7ues4] (score 4, diepte 2) I have som sketchers that I use that I don’t need my insoles with. I don’t know if that helps. Good luck! Shoes have a big impact on my back too.
[lq7tgfj] (score 4, diepte 1 OP) Thank you for your response, I’ll look into those.
[lq80iuo] (score 4, diepte 0) Birkenstocks!!!!!
[lq868st] (score 4, diepte 0) I looked into an article by Prevention magazine that listed the best shoes, recommended by podiatrists and physical therapists, then just went and tried them on as I went down the list. I ended up with the second one, Hoka’s. They are very comfortable. Let me see if I can find that article for you. Found it! Here it is. Hope this helps. 

https://www.prevention.com/health/g46909054/best-shoes-for-back-pain/?utm_source=google&utm_medium=cpc&utm_campaign=mgu_ga_pre_m_bm_comm_org_us_g46909054&gad_source=1&gclid=Cj0KCQjwurS3BhCGARIsADdUH51E9NypykNechCqZeCCfWZ1nUiixgwjMWL2jCWplnEmUgCr8XkiuLQaAh2uEALw_wcB
[lq7tc5f] (score 3, diepte 1 OP) I am going to get custom insoles made in the future, I’m just so intimidated by shoe options. But I guess once I have the insoles, the shoes may not matter.. but I’ll do anything to help myself now!!
[lq87p87] (score 3, diepte 3) Same
[lq890jk] (score 3, diepte 1) I heard they are amazing.
[lq7w7cu] (score 3, diepte 0) I went to fleet feet and got the whole measurements done. Found brooks ghost very comfy on my fat Flintstone   feet. Also bought 2 pair of Orthofeet that come with 2 different insoles. Very comfortable and light
[lq83iha] (score 3, diepte 0) Keens and Clarks are great in my opinion.  Both are very supportive, don't smash the toes, have a decent place for the ball of the foot to land, and arches that feel right.  Also good heel cushion.  

Clarks are my business/busines casual staple.

Keens are my everything else except the gym shoe.  Even their sandals and their knit sandal-shoes are super supportive.  So are their hiking shoes, their casual shoes ... I have a ton.

For light exercise like walking for exercise, I'd say go to a running shoe store like Fleet Feet or similar and just try on the models.  They all vary so much in their footbed, it's really down to what works for you.

Oh and Tecnica and Salomon for more serious hiking shoes have always been very good, in my view.
[lq8cw3y] (score 3, diepte 0) Birkenstock sandals are incredibly helpful to alleviate back/sciatic pain for me. For actual shoes, I hate to say, New Balance.
[lq856sx] (score 2, diepte 2) I bought some cute Adidas at DSW for Fancy Sneakers. For daily sneakers, I wear Asics. When it’s hot, I wear Fitflops. They’re expensive but they last forever.
[lq8czfw] (score 2, diepte 1) Birkenstocks help sciatica SOOOOOOO MUCH!
[lq8x96n] (score 2, diepte 2) Really? due to the arch?
[lqcdzgj] (score 2, diepte 3) Yeah, I think it’s was the perfect arch support that was the most beneficial. I noticed if I stood and kinda put almost all my weight on the arch and lifted my toes and wiggled them around it provided so much relief to my sciatic pain.
[lq89c2u] (score 2, diepte 1) I tried those and even the wide wasn't wide enough. I had to give them to my cousin. I've bought so many sneakers. I need to go to a sneaker store and get fitted.
[lq8fh76] (score 2, diepte 2) I went to Dicks sporting goods and they did a fitting.
[lq8r0v2] (score 2, diepte 3) Sounds great!
[lqa5lpg] (score 2, diepte 1) Yes hokas are good
[lq86b87] (score 2, diepte 0) They're expensive but so worth it Kiziks and you don't have to bend over to put them on or tie them. They're so comfortable and give good arch support.  I wear the Athens Style.
[lq86bah] (score 2, diepte 0) Look for something that cushions you from hard surface impact when you walk. I find Nike Air are the best for my back.
[lq873kq] (score 2, diepte 0) I have Adidas cloud forms, and they are great. I have a ton of back problems, and I love these. I also like the style skate shoe.
[lq88l68] (score 2, diepte 0) Sketchers slips ons have been a lifesaver for me with two herniated discs
[lq8clkr] (score 2, diepte 0) I wear HOKAs. They are amazing. No pain in my feet or legs. I currently wear Rincon 3. I need a new pair but I can’t afford them so my son gets them for me for Christmas.
[lq8f32r] (score 2, diepte 1) HOKAs are the most comfortable, yet supportive, shoes I’ve ever worn.
[lq8fk2x] (score 2, diepte 2) Same! I tried Brooks but they were super uncomfortable for me. I would like to try the ON cloud shoes but they are so expensive.
[lq8fw30] (score 2, diepte 3) I have tried the ON clouds. Two pairs. Nowhere near as comfy as HOKAs.
[lq9bhbq] (score 2, diepte 1) New Balance are okay, but I swear by KSwiss. Mine are damn near four years old at this point and still going strong.
[lqd4r5k] (score 2, diepte 3) I personally like the [CMF series](https://kswiss.com/collections/best-sellers-men/products/03426-085-m), but that's really going to be dependent on taste.
[lqdwlat] (score 2, diepte 5) I wear an EEEE, and they fit great.
[lq8hk0q] (score 2, diepte 0) Look up Squat University on YT talk about barefoot and wide toe box shoes. I ditched my custom orthotics and expensive arch and back support shoes and took his advice and my back and feet are better for it. Before I was so dependent on the orthotics I couldn’t switch it up without pain. Now i can with no issue if I want to switch it up for fashion sake.
[lq8jvu8] (score 2, diepte 0) I bought shoes from Saucany and then got Orthotics from Biocorrect.  Made a world of difference.
[lq8ocip] (score 2, diepte 0) If you need good arch support, Naot makes wonderful shoes with replaceable cork footbeds. Though the shoes are a bit pricey, they are worth every cent if they feel good on your feet.
[lq8rt35] (score 2, diepte 0) Well you can buy really anything if you have a custom made pair of orthotics,which is usually the best way to go but other brands that are good are Asics, some new balances, hoka, reiker, vionic and brands that have a wide toe box, encourages proper heel to toe roll through movement and good, overall foot support. Sketchers have also came up with some good ones as well. Making sure they fit is key and also replacing them every 6 or so months (if worn frequently) is also important
[lq9fgvp] (score 2, diepte 0) If you have one, go to The Good Feet store. I noticed a difference immediately. That constant strain in my back was significantly less. I can actually walk without constant pain. I think they have a way for you to measure your feet at home too so you might be able to get them online. They are shoe inserts that don’t work very well with sandals, but they’ve worked for me in all my other shoes.
[lqklb2g] (score 2, diepte 1 OP) I’m 99% sure that’s the place my dad recommended to me, he has one near him. I don’t have one very close to me so I might look online and see if they do that. I hear a lot of good things about them. Thank you for reminding me they exist!!
[lq9y8ld] (score 2, diepte 0) Everyone’s feet are different even if you have back pain and other issues. That’s why I recommend getting a custom made insole. You’ll be able to wear it in any shoe you have so the cost in the long run will be less expensive. I have back and neck issues, even my spinal surgeon said my neck issues alone can affect how I walk. My Dr, who’s an osteopath says I just need support by my toes. I forget what it’s called atm but I don’t need arch support.  So that’s cool it saves me lots of money and I can still wear the shoes I love. I would try the good feet store too, hopefully they have come near you!!
[nb2ri7z] (score 1, diepte 2) I agree! I think everyone’s sciatica triggers are slightly different. I was unsure about the birks, but they were heaven when I put them on and no pain for my daily city walking!
[lqar34u] (score 1, diepte 1) They now have shoes and boots! I have two pairs of the suede shoes and love them. I’m waiting on a sale to try the boots
[lq87pdy] (score 1, diepte 0) Asics gel keyano. They are awesome!
[lq88vb3] (score 1, diepte 0) I have a personal trainer and the shoe fit is what is most important. There are sporting good stores that will do a fitting for you and recommend a shoe that would be perfect. Look around for one that specializes in running shoes.
[lq88xps] (score 1, diepte 0) New balance shoes are comfortable and supportive enough for me, and I found that the converse lifts have far more support than the ‘classic’ soled versions
[lq8ajk2] (score 1, diepte 0) Saucony trail runners have been my go to. Brooks caused my foot to keep going numb along with an aching throb with them. Didn’t matter how loose or tight they were either.
[lq8gg6i] (score 1, diepte 4) That’s good to know! I’ll stick with the HOKAs.
[lqceax5] (score 1, diepte 2) I’ll have to check em out. Any model in particular?
[lqdmf6z] (score 1, diepte 4) Right on, thank you. I actually like those in a couple different colors. I might have to try some out.
[lq8eof1] (score 1, diepte 0) HOKA Bondi 8.
[lq8lmp7] (score 1, diepte 0) I suggest going to an actual shoe store wear they properly,  measure your feet, watch you walk, ask what you are specifically looking for j  shoes and what activities, etc. I did that and told him the foot dr tod me I had pronation (ankles lean in) and lumbar back pain.

Pain, can't stand longHe agreed with the pronation. He then had me try on different brands with different styles (running, walking, etc), softer, firmer, etc. Ended up with Brooks Running (I do not run) in a certain style (can't remember the name) and they are specifically for pronation.  Been wearing them every since but now I think I need less of a lift under the heel. 

Unfortunately, it was a privately owned shoe store and it closed because of covid. Need to find another store that specifically sells running shoes, measures the feet, etc. Once I find a pair I like I buy more than one pair and get out a new pair every 6 months or so (shoe store advice - shoes don't last forever).
[lqkljf0] (score 1, diepte 1 OP) You know what, I think the mom and pop shoe store not far from my house does exactly that. Or well they at least measure pretty well. I think I’ll pay them a visit to see if they can do this for me.
[lq9544w] (score 1, diepte 0) I have found zero drop shoes helped me. I bought xero shoes. I love them and changed my world.
[lq9dmvq] (score 1, diepte 0) I have those same issues and I just recently bought the sketchers slip ins and they are wonderful IMO
[lq9mdc9] (score 1, diepte 0) The vans with the popcush soles are some of the only shoes I wear. They actually have pretty good arch support and are made for people that skateboard (I don’t). I’ve heard hoka’s are great for back pain but they’re not really in my price range and I can’t get over over how ugly I think they are. 

A friend that used to work at a shoe store told me to get some superfeet insoles. I’ve seen a few kinds at Sierra for like $20.
[lqalm2t] (score 1, diepte 0) Doc martins shoes. It takes a week or two to bed in but it’s worth it and helps me lots with walking.
[lqaropk] (score 1, diepte 0) I love sketchers. Fairly affordable. Great vision and insoles. And they have those slip in versions so no laces to tie 😊
[lqax9ai] (score 1, diepte 0) Seconding Brooks Ghost. Best shoes ever.
[lqdry9b] (score 1, diepte 0) Altra or Flux work well for me.
[lqe1dc6] (score 1, diepte 0) spring heel zcoil reduces back pain:
https://zcoil.com/pages/lower-back-pain-footwear?srsltid=AfmBOorbqRsXdMHskketX2N1l8yloZj23Kw0nPwCEoXG0c11YAQ1-Fay

=== THREAD zq0j2o ===
SUBREDDIT: r/goodyearwelt
DATUM: 2022-12-19  SCORE: 421  REACTIES: 58
TITEL: Your New Shoes are FLAWED... Whether or Not You Should RETURN Them
POST (source_id=post):
I see what I would call a pleathora of posts mainly on the Facebook "Allen Edmonds Enthusiasts" group, and the sub-reddits r/allenedmonds and r/goodyearwelt with people new to higher end shoes, asking if something they see as a problem is something they should return their shoes over. This post is meant to help clear the air on this issue. Of course the views stated here are mine, so you are free to disagree and act accordingly.

I'm Robert Powers, aka "Cobbler Bob". I've been running a YouTube channel since October of 2016, which currently has almost 14k subscribers. I like to find, repair, and polish old shoes. I currently own 28 pairs of dress shoes & boots, of which 12 pairs are Allen Edmonds. I haven't counted, but I've be bought, polished, and resold a few hundred pairs of shoes that mainly come from local thrift stores or eBay.

Premise: Have you been purchasing what I would call a "cheap" shoe, and finally decided to step up to a full grain Goodyear Welted shoe, only to have your heart sink when open the box because you found a flaw? First, what do I define as a "cheap" shoe? To me it's a shoe you'll probably pay $50-$150 for that probably has corrected grain or fake leather uppers, has a bonded on rubber sole, or has a sole that has the appearance of being stitched but isn't.

Allen Edmonds is often refeered to as the "gateway drug" to high end shoes. That reference means that they're generally not as high quality as true high end shoes like Crockett & Jones, Edward Green, TLB Mallorca Artista line, Gaziano & Girling, Magnanni, or even Alden, etc, but because they are often on sale, they are able to be purchased at a price point not out of reach for most people ($200-$350). So the question is, if I spent $50 to $150 dollars on a "cheap" shoe that's pretty much perfect looking out of the box every time, why when I spend $250 to $350 for a shoe like Allen Edmonds, why isn't it perfect every time?

The Wisconsin Shoeguy (YouTube: "Wi Shoeguy") said it best on a video interview on my channel: Allen Edmonds isn't so concerned with how the shoe looks out of the box, but they're more concerned with the longevity of the shoe. I agree.

[https://www.youtube.com/watch?v=kL3Ss\_reQ4U&t=8s](https://www.youtube.com/watch?v=kL3Ss_reQ4U&t=8s)

**Reason one:** Shoes with Full Grain leather uppers and either 270 degree or 360 degree Goodyear Welted leather soles are made from natural materials. Corrected grain leather is cheap leather coated with some kind of polymer coating. This coating covers all flaws in the leather, and gives it a durable scuff resistant surface. In my experience though, all of the shoes made recently (since 2000-ish) of corrected grain leather outside the USA will crack and split. It also is not as breathable, and sometimes the coating wears off to reveal a lighter shade, and you can't re-color it with polish. With the full grain leather, you're seeing the actual surface of the animal's hide. It's coming from what was a breathing animal. Phil Kalas, owner of Ashland Leather Co told me in a "Leather Talk" interview that leather tanning is taking an inconsistent raw material, and trying to make a consistent end product. It's not easy! But when done right, the end product can last for decades with superior beauty.

**Reason two:** The soles of a cheap shoe are often a one piece injection molded sole with fake stitches molded in, and the heel even molded on. A step up from this is an injection molded sole made to look like leather, with a fake plastic welt. The welt will often have stitches on it, and the sole will have stitches on the bottom side, but the stitch count per inch is usually different from the bottom to the top, prooving that they don't acually hold anything on and are purely decorative."How to Spot FAKE Shoe Sole Stitching"video: The GYW (Goodyear Welted) shoe sole must be cut, trimmed, grooved, stitched on, finished, then have (with AE) a 2 part heel base bonded and nailed on, then a top lift bonded on and finish sanded, then dyed to color. There are a lot more parts versus a standard shoe. AEs are not "hand made", they're machine made by a human operator, but the level of skill and number of steps taken are far greater than the cheap shoe. Therefore there are many more opportunities for small errors.

\*\*Problem #1: burnishing/patina irregularities:\*\*

Full grain leather, especially in the lighter shades is gorgeous. Walnut and ligher colors often have a burnishing applied (darkening at the tips of the toes, around the eye stays, and/or the sides of the vamp). With AE (Allen Edmonds) I believe this finishs is applied by hand with an airbrush. There can be inconsistencies with this finish, and it can have areas that are too dark or too inconsistent for your liking. Here is what it usually looks like: (pic 1)

[https://imgur.com/ws60SFV](https://imgur.com/ws60SFV)

Here is one you may not like: (pic 2)

[https://imgur.com/zsmpiui](https://imgur.com/zsmpiui)

notice it's more irregular, and the transition from dark to light is not as even. I'd be fine with the above, especially if it was less than $300.

Here is pic #3, the heel on my AE Strands (the same shoe in pic #1):

[https://imgur.com/RFyBDOX](https://imgur.com/RFyBDOX)

Notice the dark to light sudden transition. I'm perfectly okay with it. Again, it's a natural material, and the irregularity is still beautiful to me. You can even this out if you'd like with a medium brown cream shoe polish. I paid $315 for them and I'm a-okay with it. I consider it character.

\*\*Problem #2: crazing/cracking of the burnishing, usually on the toes: (pic 4):\*\*

[https://imgur.com/rptqqgV](https://imgur.com/rptqqgV)

I am guessing that the finish either dried too quickly and contracted, or the toes were flattened at some point. Either way, with some darker cream polish the color of the burnishing, and a few coats of wax polish on the toes (I would mirror shine it) that should dissapear. I would not return this shoe, I'd be mirror shining the toes anyway.

\*\*Problem 3: Construction & Finishing issues:\*\*

If you get this, where the stitching goes off the welt, RETURN it. This is a major structural problem. These are my AE MacNeils that had to be returned to AE and a new welt and outsoles were put on. See pics #5/6 below:

[https://imgur.com/jGgHymN](https://imgur.com/jGgHymN)

This is also major. The black thread is the top thread, indicating impropper thread tension. Return it (pic 7)[https://imgur.com/1ABQnuT](https://imgur.com/1ABQnuT)

This is minor. It's a piece of thread or leather trapped under the top welt stitch. Grab it with a pair of needle nose pliers and it should pull out. Now if the top thread is left loose, then you may want to return it, but I think this one would be fine. Pic 8 below:

[https://imgur.com/lVIy6mm](https://imgur.com/lVIy6mm)

These shoes have a turned up lip on the welt, called a split reverse welt. Notice the lip is smushed. See below pic 9/10:

[https://imgur.com/KnhLgGC](https://imgur.com/KnhLgGC)

Why do you have this on an expensive shoe and not a cheap one? Because most cheap shoes either don't have a welt at all, or if they do, it's not structural, and it's made of cheap injection molded plastic and has a costmetic only stitch, that although looks perfect every time, it will not last very long. Moisten the leather, and take a hard smooth object like the tip of a retractable pen or a pointed wooden dowel like a big chopstick or drumstick and smooth it back flat. It may not go back completely flat, but after it dries it will probably be smooth enought to not notice.

The sole stitch goes outside of the groove, like this in pic #11[https://imgur.com/F5AeL30](https://imgur.com/F5AeL30)This is a pair of AEs made in 2001. If this happens on the arch area where the threads won't contact the ground, let it go. It won't hurt anything. If the stitching on the sole is not 100% tidy, let it go. If this happends on the area where you walk, and the threads will break through prematurely, I'd return.

Minor scuffs out of the box, see pic #12/13 below:[https://imgur.com/rboWPjV](https://imgur.com/rboWPjV)95+% of the scuffs I see posted will go away with a little cream shoe polish. I'm a believer of polishing new shoes out of the box anyway, so it's no extra work for me. Remember, cheap corrected grain or fake leather has a plastic coating on the outside and is more scuff resistant. The downside to it though is when it does get scratched, it's harder to cover or correct. Full grain leather does show scuffs easier, but because of it's pliability and porousness, it readily accepts polish and conditioning creams better. You can polish out even light to moderate scratches, because the surface has no coating to abraid through. Polish these and move on, unless it's severe enought to where material has been removed.

This one is a cut, not a scratch, and it's on an area that is stressesd. RETURN without wearing it. See pic #14 below:

[https://imgur.com/jSmKdXB](https://imgur.com/jSmKdXB)

This next one, pic #15 below looks really bad for a new shoe. It appears as if someone poked holes through the upper. Believe it or not, but if you moisten the leather with moisturizer and rub it with a blunt object, like the blunt smooth end of a screwdriver handle, and back up the inside with your thumb, you can close those holes up to where polish will cover what's left. If I got a pair of AEs for LESS than $300 with these holes, and everything else was perfect, I'd burnish the holes shut as I stated above and be happy. If I paid full price and was not "handy", I would consider returning.

[https://imgur.com/qEzq7Sj](https://imgur.com/qEzq7Sj)

\*\*Problem area #4: Loose Grain:\*\*

Loose grain is a term to describe leather that is unusally wrinkly. It happens because the leather closer to the belly of the animal does not have the same properties as the areas closer to the spine and rump. Manufacturers are proabably trying to use more and more of the hyde to decrease material waste, and sometimes push it too far. In short, there is no fixing this, so decide quickly if you can live with it or not.Remember, this may not show up until you walk in them. Here's MY OPINION of some to follow:

Pic #16, my AE Achesons I bought new from AE directly on sale for $97... loose grain on the left shoe. They were $97, I am fine with it. Now if they were $297, back they would go.

[https://imgur.com/53qPEPi](https://imgur.com/53qPEPi)

Pic #17/18: in my opinion, the boots on the left would be okay IF they were purchased on sale at a good price, but the Oxfords on the right are terrible and I'd return them at any price, especially since the person here said the other shoe was perfect, and this was after one wear:

[https://imgur.com/P9KLYiB](https://imgur.com/P9KLYiB)

\*\*I've saved the best for last... problem #5: THE WELT JOINT:\*\*

To understand this one, you must understand what a welt is, and why it must have a joint. Did you know an automotive tire is made from flat rubber? Every traditional tire has a joint. The welt is a flat piece of leather, and on a 360 degree GYW shoe, it wraps all the way around the shoe. It therefore has a starting and stopping point. The welt is stitched onto the insole via the gemming and to the upper.

Here is a video explaining in detail the welt and how a Goodyear Welted shoe is constructed:

[https://i.ytimg.com/an\_webp/fpEpqJ0eO0g/mqdefault\_6s.webp?du=3000&sqp=CNDqgp0G&rs=AOn4CLD1U1mN7fZWlnSXzRkArxLfqyBiUg](https://i.ytimg.com/an_webp/fpEpqJ0eO0g/mqdefault_6s.webp?du=3000&sqp=CNDqgp0G&rs=AOn4CLD1U1mN7fZWlnSXzRkArxLfqyBiUg)

The welt is what the outsole of a GYW shoe is stitched too. Sometimes the welt joint is invisible, like pics #19 & #20 below:[https://imgur.com/SEe3Kew](https://imgur.com/SEe3Kew)

Sometimes it's neat, but visible like these next three examples, #21, 22, 23:

[https://imgur.com/4VKYkuG](https://imgur.com/4VKYkuG)

FYI, that last photo directly above, #23, is from a pair of Florsheim shell cordovan 93605's made in the 1970's or 1980's:

These next two examples,pic #24/25 are not as neat, but 100% functional. Don't return them:

[https://imgur.com/nBPfa9d](https://imgur.com/nBPfa9d)

Does this make sense? Allen Edmonds says that their Goodyear Welted shoes go though 212 different manufacturing steps. It's a whole different animal than a "cheap shoe". Don't get me wrong, I'm not saying some of these errors are okay. I'm saying that if you buy a new Goodyear Welted shoe on sale for less than $300, or in some cases less than $250, do not expect to get the same quality as an $800 Church's or Crockett & Jones, or a $500 Alden that won't go on sale. So if these minor errors are too egregious for you to live with, you'll need to step up to the $450 and UP range for a pair of shoes.

Justin Fitzpatrick talks about the welt joint in his article on The Shoe Snob:

[https://theshoesnobblog.com/tag/justin-fitzpatrick/](https://theshoesnobblog.com/tag/justin-fitzpatrick/)

## [Welt Joining - Good vs Bad](https://theshoesnobblog.com/welt-joining-good-vs-bad/)

The Shoe Snob blog is about seeing men wearing better shoes through education and sharing what is out there that deserves recognition.📷 [theshoesnobblog.com](https://theshoesnobblog.com).

I hope this helps, and here's a link to a video version of this article on my YouTube channel:

[https://youtu.be/CnYL3HkR0r8](https://youtu.be/CnYL3HkR0r8)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j0vo9q2] (score 91, diepte 0) Good post.

The last part is really important. Everything you showed is a flaw - it's just a matter of acknowledging the fact that $200-350 is "entry level" for a welted shoe, so some finishing trade offs should be expected.
[j0vr70j] (score 54, diepte 0) Solid writeup. One comment:

>Loose grain is a term to describe leather that is unusally wrinkly. It happens because the leather closer to the belly of the animal does not have the same properties as the areas closer to the spine and rump.

My understanding is that this is incorrect, as Loose Grain is a real, but rare and serious defect where the layers of the leather are separating. 

Heavy break is when there are a lot of deep wrinkles in the leather.
[j0vsbf4] (score 34, diepte 1 OP) Great point, you sound like you know more about this than me. This would be a great question for me to bring up with Phil at Ashland Leather, thanks for that.
[j0vqmdf] (score 16, diepte 1 OP) Maybe to you I failed in my goal, but I was trying to get people newer to nicer shoes to understand WHY a higher priced shoe may have more flaws than a lower priced shoe. Whether nor not you return it is your call. It's a value proposition, as I state at the end of the post, as to how much you're willing to pay to get the level of quality you think you should have. I have a pair of AEs I bought new from AE for $97. Is that expensive? Or how abuot the pair of Sanfords I did a video on that were $12 from eBay? Anyone that follows me knows I absolutely do NOT spend a lot for what I have. The most I've ever paid for a pair of shoes is $315 for my AE Strands on sale.
[j0wnnxk] (score 16, diepte 4) 'loose grain' refers to two different things - the actual definition which is where the grain is pulled from the flesh (the grain has fully delaminated from the flesh, causing there to be noticeable bubbles below the grain), and the colloquial definition which is "any type of grain break i don't like". u/Rioc45 is referring to the former, whereas most discussions use the latter since that's what everyone uses the term for anyhow.
[j0vscd0] (score 16, diepte 0) Thanks for the post! While I completely agree, I do expect the 'should I return this completely normal shoe' posts to keep flowing :P
[j0vzu6a] (score 12, diepte 2) Link? When discussing this we have ensure we are both talking about the same thing as "Loose Grain" is a term used imprecisely.

Interview with Nick Horween confirms my points here: 

https://www.stitchdown.com/horween-leather-school/what-is-loose-grain-leather/
[j0wqddz] (score 11, diepte 6) >"Your opinion"

Every comment on the seriousness of "Loose Grain" is going to be an opinion. . . Even if there was a Bible on leather terms ultimately the author's definition would still be an opinion.

It is my opinion it is a serious defect because when grain pulls away from the leather below (true loose grain), the leather can tear and split.

There are informed opinions and uniformed opinions, and I think mine is among the former.
[j0vo9dc] (score 10, diepte 0) Thanks for this awesome write up!  Super informative!
[j0vzvbx] (score 10, diepte 2) Please do
[j0x96r0] (score 10, diepte 6) thank god for small mercies
[j0w06m6] (score 10, diepte 0) Sticky or wiki this please!
[j0xoi3g] (score 10, diepte 0) Dear mods,

Please pin this.

Thanks.
[j0vq0cg] (score 9, diepte 0) Lovely info
[j0wm2nh] (score 9, diepte 4) >"But it’s rare enough that I don’t have any on my boots,"

The article can't even find a pair with real loose grain it to use as a photo.


>"And it’s generally caused when the grain is pulling away from the layers below."

That's a serious defect in my opinion.

Feel free to disagree but I'll stand by my view that it is a rare but serious defect beyond simply "heavy break."
[j0w6nmb] (score 9, diepte 0) I left the Allen Edmonds fb group because of the constant griping of what seemed to be stupid issues. Glad there is some clarity to help people make a good decision.
[j0vqc9k] (score 6, diepte 1 OP) You are very welcome!
[j0wudua] (score 6, diepte 0) Cobbler Bob! I've been watching your videos since about 2019, no idea you had a reddit account. Love your content man, and this is a great post.
[j0vw97r] (score 5, diepte 0) Thanks. It was very interesting to read this!
[j12wklm] (score 5, diepte 0) I bought a pair of the Grant Stone kangaroo boots and was a bit disappointed that they used leg leather on the shaft. I'm Aussie and know that part is generally discarded. It's far weaker just because it gets stretched out so much as the animal jumps around. Could have returned them but I thought fuck it, they've never worked with that leather before and it's cool that they didn't waste any. They clearly made a design choice because it's way softer and thus more comfortable on the ankles. Really happy with them.
[j0w8q52] (score 4, diepte 0) Honestly great post. It’s interesting to see the different perspectives of what someone would consider an actually flaw.
[j0z0qe9] (score 4, diepte 1) I'm not Cobbler Bob, but I would've also sent those back. That lug at the very edge with the very thin wall would've busted in no time, I'm sure. Also, with it all being off center, it could've created a weird feel when walking in addition to a strange wear pattern.
[j0wcqgj] (score 3, diepte 0) Awesome writeup, thank you. 

I had a question - i've got a pair of boots with loose grain,  it's not ideal but i don't mind it too bad. Can loose grain compromise the structural integrity of a boot? How does loose grain differ from Grain break?! 

Thank you! I subbed to your channel too!
[j0ynv5y] (score 3, diepte 3) Paraphrasing Phil Kalas, the industry term for grain break is the “coarse pebbling” due to folding the leather in on itself/wear. Loose grain is improperly used but it’s the large pebbling when the grain delaminates from the flesh. I’ve only seen true loose grain near the leg joints of a leather side. Loose grain has almost become synonymous with bad grain break due to consumer confusion.

Edit: To clarify, loose grain is not due to human wear. Nick Horween on the Stitchdown podcast says it’s from the belly or flexing regions of a cow during their life, that results in a more spongy skin layer.
(39 reacties met lagere score weggelaten)

=== THREAD tz7r1f ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-04-08  SCORE: 6  REACTIES: 57
TITEL: Just wanting confirmation from you kind geeks that I should return this unnecessary item they sold me on at the running store (orthotics) to pair with the On Cloud X “running” shoes. Both deeply regrettable purchases but at least I can get some $ back for these.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i3xgrm9] (score 30, diepte 0) Remember that these things are NOT designed to solve a specific problem you have; they're designed to sell you something by providing a veneer of legitimacy to an up-sell.

A podiatrist or physiotherapist are the only people you should get prescribed specific footwear or orthotics from. Even they will tell you that finding the right thing requires some trial and error, but at least their guesses are educated and not based in a desire to maximise profit (because that would be unethical and they don't want to risk their license so that their clinic can make a few extra $).
[i3xpl8i] (score 15, diepte 0) honestly insoles are a personal preference piece. if they feel good, go with them, if you don’t notice a difference take them back. i don’t get why people get so infuriated by insoles unless they too were tricked into buying a pair even when they didn’t feel any better.

the real fury here should be being recommended a Cloud X for running 😂 that dude should be fired - i’d take them in for your money back and tell them you weren’t sold a running shoe when that’s what you came in for.
[i3xlcwd] (score 13, diepte 3) I used to work at a running store and you'd be shocked by the amount of people I had to talk out of getting the CloudX for daily running.  I guess On's advertising really persuades people to think it's good for daily runs
[i3xgyb7] (score 10, diepte 1 OP) Ugh seriously. I’ve come to learn this lesson. Unfortunately the hard way. Having a word with their manager tomorrow.
[i3xjab9] (score 9, diepte 0) Return both.
[i3xzljz] (score 9, diepte 2) It's worth asking for, especially since the shoe isn't built for your needs but was sold as such. Even if they won't give a full refund they might give some prorated store credit or something. No reason not to ask, just be polite about it.
[i3z2yyd] (score 7, diepte 2) I wouldn’t shop at the store you used ever again. The return policy of a running store or store selling shoes for runners should be to give at least 30 days for returns. The store bills themselves as a running store, so they should offer this. 

For this reason contacting On would be my next step.

Worth noting: assume you are in the states, as I know some other countries are not as lenient on returns.
[i3xgn3e] (score 5, diepte 3 OP) Haha thanks for thinking my foot is normal. =p 

This analysis they did I think is meant to cause concern. I believed what they told me about how the pressure points of my feet will eventually cause injury in time. 

I am brand new to running. This purchase was to treat myself for killing all my goals, to upgrade my footwear and hopefully feel even better and get faster maybe hopefully lol. 

Going back to the store tomorrow to return the insoles and speak with manager. I hate to be that person but now that I’ve come to this sub (too late sadly) and seen all the negativity about the On Clouds plus my own unfortunate initial experiences with them, I really feel it’s faulty of their staff to be recommending those shoes based on the overwhelming feedback online that they are not at all suitable for runners. 

I appreciate your comment. I suppose I’m a rube when it comes to all things running but I’m learning. Trusted the sales people to help educate me. Sigh.
[i3xh5e6] (score 5, diepte 1 OP) Thank you. Makes a lot of sense.
[i3yufns] (score 5, diepte 1) Even then I’d be skeptical. Podiatrists love orthotics. No matter what. I swear if I went to a podiatrist with anything from an ingrown toenail to a compound fracture, they’d sell me orthotics.
[i3xzwek] (score 5, diepte 1) I'm amazed at how pushy my local running shop can be with some items. I think the employee is genuinely trying to be helpful but really pushes what brands they prefer. Even after asking about Mizunos 3 times I had to grab a box off the shelf myself to try on.
[i3x7rzq] (score 4, diepte 1 OP) Yea I haven’t experienced any issues whatsoever as far as pain / injuries in my 10 weeks of training for a 5K in neutral basic ass Nikes. Ironically, as soon as I wore the On Cloud sneakers I had pain in my lower right calf on the first run. Second run was the calf, lower right side of back, and outer hip. So so frustrating. Thank you for your comment.
[i3xhl1f] (score 4, diepte 4) Hey makes sense, we put a lot of trust in salespeople at the end of the day. Well done on getting those goals. If you're new I really recommend looking in the sidebar, there's a list of shoes recommended for neutral runners, you'll definitely find something in there, good luck!
[i3xfwyq] (score 4, diepte 0) The fact that the store sold you insoles with a brand new pair of shoes is laughable. Definitely return, and maybe find a new local store if there are any nearby.

I do not know for sure but I have heard that employees at some stores make commission on the insoles.
[i3xnxsp] (score 4, diepte 4) I would argue that qualifies, but it depends on how you’re running those 5Ks tbh. The Cloud X is a weird shoe, one that I don’t particularly care for, but it does have a use as a shorter “tempo” shoe. I just think it works better on a treadmill or in a gym setting where it’s being used to for multiple activities.
[i3yr6rl] (score 4, diepte 1) From my personal experience as run specialty outfitter, most of the people that buy On clouds from me do so because they let their friend convince them they are the best shoes. I actively try to talk customers down from buying certain On models if they will be doing any running or relying on them for work. There are several models I do recommend sometimes like the Stratus, Monster, Flow (for more experienced runners).
[i3ybw1j] (score 4, diepte 0) I like insoles, as they can make a good pair of shoes great, and shoes are designed with the bell curve in mind - if you're at either extreme, insoles can help a shoe fit better. That said, orthotic insoles should be based on some science of your needs, meaning a podiatrist or specialist.
[i3yyk0x] (score 4, diepte 0) Insoles have kept my plantar fasciitis at bay for a decade.

If you didn't have pain before (in your Nikes), no need to use insoles.
[i3xeity] (score 3, diepte 2) Why did you get them, we’re they just a sales add-on? You have a pretty normal-ass foot.
[i3xjqlq] (score 3, diepte 4) Yeah you've got a solid arch, props to you
[i3xltso] (score 3, diepte 5 OP) Damn never have I been so proud of my feets XD
[i3z2bkq] (score 3, diepte 6) I’ve got arches like that and running stores are always trying to sell me on some insert because of it. Been running for 28 years without inserts and my arches are fine!
[i3xh20l] (score 3, diepte 1 OP) I’m a rube to all things running. Learning every day. This sub is helpful, came a little too late on this poor judgement call.
[i3xlol4] (score 3, diepte 1 OP) Wish I could. ONs have been run in 2x & one walk. They have signs of wear & therefore do not qualify to be returned.
[i3xn17r] (score 3, diepte 0) I used to work in run specialty and this sort of stuff infuriated me to no end. When I had customers ask me about these one size fits all orthotics I told them that I would check with a podiatrist unless they are just getting a pair to put in their boots or something.

There is a local running store that pushes the curex orthotics to every customer and even the ones getting a pair of Asics Kayano or similar higher stability shoe.
[i3yltao] (score 3, diepte 1) I agree - I used to get my shoes at a store that would always try to sell you an insert. Sometimes the inserts were comfortable, especially with brands that didn’t have fractional sizing, it would improve the fit.
[i3z4zxf] (score 3, diepte 1) Yeah I bought some insoles with a pair of hoka. I knew it was an upsell but they've been comfortable and I haven't had the same foot pain I had with new balance so ...idk,  if it works I'm not too mad about it.  They aren't necessary but it was nice to get the scan that showed my foot width. I had been trying to navigate women's wide shoes to discover I'm an E width, so men's it is
[i3ymo1m] (score 3, diepte 0) Def return the ONs.
[i3xluqh] (score 2, diepte 5 OP) Appreciate you
[i40gss0] (score 2, diepte 8) I havent seen your gait but almost certainly not anything marketed as 'stability'
[i3yn66v] (score 2, diepte 1) It's really scummy. The store I work for doesn't do commissions, but some brands have started offering direct incentives like coupon codes for their products and entries into prize draws if you sell their product and then submit proof by uploading an image of the receipt with some personal identifier. They know that some retailers don't like doing commissions due to the effects it has on customer service, so they're instead appealing to the minimum wage retail workers who are willing to be unethical to make a little extra money (can't really blame them). 

Last I saw I don't think any of the running shoe or insole brands we carry were doing this type of thing, but some clothing and snow sports brands were.
[i3xribi] (score 2, diepte 5) Good use of the quotes on can - I always had a hard time pitching them as a viable running shoe as I didn't believe they were good enough to put my name behind
[i3z63tv] (score 2, diepte 1) Username doesn’t check out
[i4145a6] (score 2, diepte 2) On has 30 day policy. I worked a lot a store that sold on and it was never a problem.
[i3zgqjt] (score 1, diepte 7 OP) Alright arch twin, what running shoes do you like?
[i4169m9] (score 1, diepte 8) I wear Brooks which aren’t super exciting but they work great for me. Glycerine for my longer runs and Launch for shorter runs. Since my arches are so high I run into the issue of also having a high instep so even with alternative lacing a lot of shoes put my toes to sleep. So if you also have a high instep I highly recommend looking at alternative lacing patterns
[i40grqd] (score 1, diepte 7) the fact that you have arches like means you need less arch support, not more. crazy
[i415ya6] (score 1, diepte 8) Right?! Yet every time….”you really should have an insert with those arches…” Oof.
[i3yc3r2] (score 1, diepte 4) Many running stores will take back running shoes if they don't work for you.
[i40xb8x] (score 1, diepte 2) >Yea I haven’t experienced any issues whatsoever as far as pain / injuries in my 10 weeks of training for a 5K in neutral basic ass Nikes.

Never change a winning team =)
[i3xg7ue] (score 1, diepte 0) Return for sure. You have high arches but there are plenty of shoes that can support them. A lot of running stores pressure their employers to upsell insoles.
[i3xm7cl] (score 1, diepte 3 OP) Thanks for the link, I see “Best for: Mixed-sport workouts, short runs, ultralight” - what qualifies as a short run? I run 5K at a time, 4-5 times a week and told the girl this in the store.
[i41sxgj] (score 1, diepte 3) Do you think I can run in Hyperion tiempos?
[i3yxkx8] (score 1, diepte 1) Money, money, money! They sell well
[i3xjnni] (score 1, diepte 0) Orthotics are horse shit, particularly if you don't have injuries.

If you do have injuries, you can either rely on orthotics or strengthen your calves/feet. One of those is free

Also forget running stores. I always find it best to research online from forums like these and then buy online. Way more variety and you dont even have to go anywhere.
[i40h81i] (score 1, diepte 2) Buying your first running shoes is like buying a friggin car in how many different ways you can get it wrong. Sadly people dont have the time to research it - because its all extremely confusing and timeconsuming for the layman - but once you do you realise how unhelpful people at the store are. 

In the UK its even worse. Minimal stock usually - you get a choice of like 10 shoes in most places - and whoever is pushing the marketing hardest gets recommended.
[i3xlw9s] (score 1, diepte 0) Unless it's a significant amount of money, do yourself the favor and keep them. I bought mine ten years ago and I have used it the most in the last two years. LIFESAVER

I am more concerned with the shoe choice than the inserts
[i3yppho] (score 1, diepte 0) Depending on the laws in your country, you could return both. In Australia, if they did any kind of analysis and then sold you a specific shoe for a specific purpose, but then it turned out the shoe wasn't for for that purpose, you could return for a refund regardless of their store policy.
[i3yrsyt] (score 1, diepte 0) Just curious what other shoes you tried on? Did you go in with the intent to purchase an On shoe? Most of time, in my experience, customers who buy Ons are only willing to try that brand, and chose the one that feels the best on their foot in the store.

Just keep it and use it in the gym or for casual wear. You need more than one shoe anyway. 

As for the orthotics, do they feel good in your shoe? They work really well for people that work on their feet to help with pressure release. The types you buy at running stores are not corrective orthotics. They are meant to improve the experience in the shoe you purchase. I suppose some people have scummy sales tactics, but you are not forced to buy them.
[i3zfms5] (score 1, diepte 0) Why did you accept them in the first place?
[i3zgfr3] (score 1, diepte 1 OP) Because I’m a hopeless rube brand new to running and trusted the employees of this reputable running store to educate and advice me appropriately. Lesson learned.
[i414va9] (score 1, diepte 0) There is a reason why we do not recommend On shoes on this sub.
[i418jmt] (score 1, diepte 1 OP) Seems like there are many reasons. I found this sub too late.
[i419pdt] (score 1, diepte 2) Just make sure to read the wiki.😉
[i3xgk51] (score 0, diepte 0) Boggles my mind that people fall for that orthotic add-on BS
[i3yb69f] (score -2, diepte 0) Take it all back and get a pair of Nike Pegasus

