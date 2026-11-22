# Label-batch batch_0116

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
Schrijf het resultaat naar `batch_0116.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 8rky61, 5ymeiv, 1q0o049).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 8rky61 ===
SUBREDDIT: r/weddingplanning
DATUM: 2018-06-16  SCORE: 82  REACTIES: 92
TITEL: What do you think? You think I can pull it off? I think it has a great summer feel! (And yay for comfortable feet!)
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[e0s5qw0] (score 105, diepte 0) Personally, I feel like the vibe your dress is giving off and the vibe of the shoes don’t match. The dress is just a little too formal to go with that particular shoe. I definitely think you could still wear a comfy shoe, but maybe something on the fancier side, like wedding Keds or Toms, or even like a comfy ballet flat.
[e0s63lc] (score 26, diepte 1 OP) Thank you for your honesty! 
The thing is, I think you might be right but none of your suggestions feel very...”me”. I’ve had pretty bad dress regret and decided to own it and add the edgier style I usually have. I usually have a bit of a “raw edge” to my clothing. I like converse and will wear those even after the wedding, ballet flats definitely not. 
Still, I really appreciate your comment! People rarely dare to be honest in real life :)
[e0s623d] (score 15, diepte 0) I say hell yes. Take a few photos with the dress hiding the shoes if you’re worried about regretting it- but little details like this make the day yours. (And they are not a horrible pairing, IMO)
[e0s8bna] (score 15, diepte 0) Okay I'm glad that other post was removed! Wear what you feel confident and beautiful in. If those shoes make you feel like a baddass on your wedding day- Rock them. I am wearing berkinstocks! Because they are comfortable! And they are me! Are they what society says a bride should wear? Nope. But guess what- society isn't the one who will end up with blisters. The last thing I want to be worrying about on my wedding day is my feet! You do you girl!
[e0se9pw] (score 14, diepte 2) It was a super sexist comment saying women shouldn't wear converse and that we basically needed to look nice all the time or else we look like a middle schooler. It was rude, so I reported it.
[e0sqlex] (score 13, diepte 2) Would you wear something like a granny boot after the wedding? I’m wearing brown leather lace up boots with my beaded lace and tulle dress, but that’s because I wear boots most of my waking life. I think they would look great with your dress if you DO want to change it up. 

Ultimately, I think you should wear whatever shoes will make you happy and make you feel like yourself. They’re not even going to show most of the time, and (for myself)  “does the vibe of my shoes match the vibe of my dress” is just one of those things I can’t bring myself to care about a year into wedding planning. The converse aren’t my thing necessarily, but I also wouldn’t give it a second thought if I caught a peek of mint green sneakers under a fancy dress because I would just assume that’s what made YOU feel fabulous.
[e0s8k8x] (score 12, diepte 0) My dress was hemmed a little long and I never saw my shoes at all except when i pulled up my skirt for a photo. I went barefoot the entire reception. I think you should wear the shoes that make you happy and if you are worried about them constantly showing and not matching just make sure the dress isn’t hemmed too short :)
[e0sl2hp] (score 11, diepte 3) I think for that vibe, your dress would look dope with a real when I'm looking black leather boots. Probably a semi slouchy engineer boot. 

The colorful Chucks thing requires a little less formal of a dress in my opinion.
[e0sm9cx] (score 8, diepte 3 OP) Oh no D:
After the drama with the dress my future husband is gonna hate me...But maybe I should go look for a pale pink converse instead...
[e0s6ymw] (score 7, diepte 1) I agree with you, however I think you could also go the rocker chick in a dress vibe and depending on other accessories I think it would look great!
[e0smv2h] (score 7, diepte 4) I think that'll work a lot better!
[e0sded2] (score 7, diepte 3) Something snotty like “women who wear converse haven’t grown up.” And I asked what they do wear and was presented with a “basic bitch” list. “Flats for this, heels for this, running shoes for this, and converse is all middle schoolers and high schoolers so that’s a red flag.” I’m paraphrasing because they deleted their comment before I could post mine to call them on the rudeness and bizarre expectation for a stranger and her wedding, so I can’t refer back. 

Anyway, that user is a troll and I went through the post history and they literally are the type to refer to black people as “dindu nuffins,” so basically they’re trash and they know it but wanted to shit on your day. And that’s not cool.
[e0sdb23] (score 7, diepte 0) YES. YES YES a thousand times YES.  I love the vibe of the mint green with the light pink dress. That reminds me of watermelon or some kind of excellent ice cream flavor. You should go for it!
[e0s9z7l] (score 6, diepte 0) I’m wearing converse with my a-line tulle for both ceremony and reception because they feel the most like me!! You do you!
[e0szug0] (score 6, diepte 0) I definitely think you can pull off the Converse! However, I'm not feeling that green color with your dress. It clashes a bit too much imo. I think a pale pink or even light blue color would look much better, especially if they end up in photos. :)
[e0sa0et] (score 5, diepte 2 OP) I’d love to get a vibe like that! What other accessories would you suggest?
[e0slx8u] (score 5, diepte 2) My shoes peeped out A LOT more than I expected. Any kind of shot where I'm moving showed my shoes either from the movement or from me holding up my slightly too long dress.

It made me realize how relieved I was that I went with nude shoes. A bright pop of color in so many of my shots (including walking down the aisle) would've been really distracting and stood out too much against the white dress. 

Just keep this in mind, do you want a bright green attracting your eye?
[e0sjreu] (score 5, diepte 0) I'm not against wearing comfy shoes or even converse with your wedding dress, but the colors are definitely clashing. The dress is an "pale" pink and the shoes are a "pastel" green, and the difference in tones is like nails on a chalkboard to me. It should either be both pale or both pastel. And since it's probably easier to trade shoes I'd go with something like [these](http://www.isug.co.uk/converse-all-star-dainty-oxford-light-green-m4498-p-1012.html).
[e0s65p6] (score 4, diepte 1 OP) Thank you!
I don’t think the shoes will show at all. It still needs to be fitted and right now I’m  a giant duster when I wear it :D
[e0s6wu6] (score 4, diepte 1 OP) Thanks for your encouragement! 
When I first mentioned wanting “different” shoes the first response was: “Oh? You’re wearing dr Martens?”
But considering we’re marrying in the middle of summer that didn’t seem ideal to me XD This is a much more summer proof choice! (And great for dancing)
So yeah...I think it suits me :)
[e0sbe8x] (score 4, diepte 2) http://i.imgur.com/gW9frIS.jpg

She's a baseball fan.
[e0s6mk1] (score 4, diepte 0) I wore those exact same shoes, color and all and it was an amazing decision! I had a tea length dress so they were on display, but they were also comfortable and very much my personality so it worked.
[e0s7j1v] (score 4, diepte 1) What shoes do grown up women wear, expert?
[e0s9dc5] (score 4, diepte 0) Own it girl! I love it, it seems like it would flatter your personality. The only person who should be worried about what is on your feet is you!!! Make sure to get extra pictures with your shoes.
[e0sct1m] (score 4, diepte 1 OP) You’ve got different shoes for the part? Or no party?
And you’re so right! It does feel like me to wear something definitely not heels :’)
[e0t1fsl] (score 3, diepte 4) I think a pale pink would look so good! I don’t know if they do but a rose goldish would look good too.
[e0sd81m] (score 3, diepte 2 OP) I never saw that comment. What did it say?
[e0sdq2h] (score 3, diepte 4 OP) Well, I guess there are some people who have personal rules for what to wear in every kind of situations and I guess I can see the appeal. But you’re right! Imposing those rules on others is a total douche move.

Thank you for sticking up for an internet stranger! I think that’s pretty damn cool of you :)
[e0sehms] (score 3, diepte 3 OP) Pfffft...lame. Thanks for reporting.
Funny how some people get so uncomfortable by out of the box ideas! Thanks for satisfying my curiosity though!
[e0segm9] (score 3, diepte 2) Sooo cute! You could even have  bridesmaids wear some too. I like wearing heels but I know they would come off as soon as the ceremony was over and then I would be tripping over my dress so converse or keds is what I’ll go with. 

When you look back I bet you will be so much happier wearing these then going with heels.
[e0sd1nv] (score 3, diepte 2) Just my converse! All day! I can’t wait to have the most comfortable feet at my wedding!
[e0sdtpd] (score 3, diepte 1 OP) That’s a pretty fun idea! I’m going to look into that! 
Maybe I’ll even add the date on the back of the shoes too...
[e0snmse] (score 3, diepte 2) I would steer away from the pink because it will probably clash instead of match. The blue might look cute as well, but I think green contrasts with pink better than blue, personally. :) Any way, I'm sure they'll look super cute!!
[e0v4hag] (score 3, diepte 1 OP) Thanks! I’m going shopping again on Wednesday. You’re probably right!
[e0tf6ik] (score 2, diepte 5) I love the chucks with a dess, doing more or less the same for the reception (dark red/burgundy chucks, yay!). 
But i agree with the super colourful comment...maybe opt for more neutral chucks? Something dark blue, cream, or even the black ones would work fine imho :)
[e0sn707] (score 2, diepte 3) Leather, a jacket or braclets. Black lace gloves, Chucky jewerly (maybe same colour as shoes) dramatic lip colour. Also don't take fashion advice from me I'm the least fashion forward.
[e0sd6wm] (score 2, diepte 3 OP) Haha, great picture!
[e0sf029] (score 2, diepte 4) Thanks! I hope you go with whatever you are comfortable with on your day, most people will only remember the overall experience. 
The ones who remember your shoes, will do so with a smile "That's so like her" :)
[e0sdvpd] (score 2, diepte 5) No problem! I too wear whatever fits my personal style. I sometimes wish I had more structure with my clothing and knew what to wear in all situations, but I don't, so I wear what I'm comfortable in. It's your wedding. Wear whatever you feel comfortable in! And congrats!
[e0sczha] (score 2, diepte 1 OP) You’ve got me all hyped up! And you’re so right too!
Also, what did that other post say? I didn’t see it. 
And berkinstocks are very comfortable! No blisters for you!
[e0sd5u4] (score 2, diepte 1 OP) You’re so right!
I’m actually kinda surprised by how many  people have expressed their opinions and tried to talk me into heels! It’s almost as if they worry more than I do about my shoes. 
And I just might! I was thinking of one where I pull up the dress with one hand and hold my finger to my lips with the other, maybe even wink. Kinda like a little secret between me and the photographer! :D
[e0senv3] (score 2, diepte 3 OP) It just feels more like me! And in the end that’s all I want.

Maybe you could do both if you have the funds? Wear heels for the ceremony or whatever and just throw on the converse/keds when your feet start hurting!
[e0sedux] (score 2, diepte 4) And I hope you choose to be too!! No matter what decision  you make, you’ll look incredible.
[e0sef3n] (score 2, diepte 5 OP) Thank you so much! Right now the converse are feeling really good! :D
[e0sdksz] (score 2, diepte 0) Do it! You’re not even gonna see your shoes I swear except for when you sit. Love the blush and turquoise combo. Converse is the way to go with sneakers and a dress. If you wanna “match” the dress add some lace laces. But comfy feet are KEY, it’s summer! And again I promise no one sees your shoes much at all
[e0sj2ng] (score 2, diepte 0) I would be tempted to go with red or white converse! I live them I put my feet in and it feels like coming home! You'll look awesome im sure
[e0slmeb] (score 2, diepte 1 OP) I thought so too! But now I’m not so sure. Maybe I should go with a pale blue or pink instead...
[e0sn6s5] (score 2, diepte 2) These might be cool https://www.office.co.uk/view/product/office_catalog/2,400/1551593260

I do think the colour of the ones you have is a little jarring, but I love the overall idea. Would you wear sequined converse again? There are rose gold ones that might be lovely as well.
Or these! 
http://www.converse.com/on/demandware.store/Sites-converse-gb-Site/en_GB/Product-Variation?pid=ID00657&dwvar_ID00657_color=white%2Fblack%2Fwhite&overrideDefaultSizeSelect=true&csid=PS%7cGOOGLE%7cShopping_Ads%7cGO_SH_UK_AllStars_LowTopCanvas&product_country=GB&product_id=557989C_5&gclid=EAIaIQobChMIyv62867Z2wIVr73tCh2BFw9vEAQYAiABEgLcj_D_BwE&gclsrc=aw.ds
[e0sncmn] (score 2, diepte 3 OP) I love the first ones! Except for the whole out of stock thing. Also, they’re a little too purple aren’t they? Probably safer to go with pale pink only...
[e0v2bbo] (score 2, diepte 3 OP) Thank you so much!
[e0snihf] (score 2, diepte 0) If your wedding dress is floor-length (like all long wedding dresses), your feet really won't show anyways. I didnt realize the bride at the wedding I went to last weekend was rocking Birkenstocks under her gown until way late into the night and she was holding the front of her dress up while dancing. I say go for it. Your wedding should reflect you and its totally key to be comfortable ...plus people dancing always look the best and you can totally dance the night away in those.
[e0t39n0] (score 2, diepte 0) It’s your day and you might as well show who they’re marrying by being you.  Whatever you decide, my only advice would be to run it by the photographers so they know how to work with it.  I don’t know what your venue is like, but hopefully the color has enough contrast with the material below your feet.  Dare to be comfortable... hah!
[e0te2b6] (score 2, diepte 0) My a friend of a friend wore red converse with her lace wedding gown. Her photos were beautiful, the pop of color worked so well. I love the idea!
[e0tef7r] (score 2, diepte 0) I wore yellow converse with my long lacy white dress. It rocked. My bridesmaids also had lacy dresses and the same yellow converse. Do it. I think the blush pink and teal look really nice together. [picture of the bridal party rocking the canvas. ](https://imgur.com/a/J88ZDwS)
[e0v2giz] (score 2, diepte 1 OP) Thanks! I love those yellow converse, they're such a nice shade!
I'm just worried whether these clash with the dress too much. I don't mind them popping, as long as they do it tastefully :P
[e0ug7d9] (score 2, diepte 0) I love the shoes, but I can't help but feel as if the color is a bit off? If you went for maybe a creme/light pink color I would imagine it going together with your dress better! BUT you're the bride! If you feel comfortable and confident and can see yourself getting married in those shoes than that is what truly matters.
[e0sll93] (score 1, diepte 4 OP) Thank you for your suggestion! I think I know what you’re going for...maybe? But I’m not really feeling it. Thanks for thinking along though!
[e0v2y4d] (score 1, diepte 5 OP) What do you think of this one? (the pink one)
http://www.converse.com/nl/nl/regular/chuck-taylor-all-star-ombre-metallic/559871C_085.html

Or this?
https://www.ziengs.nl/product/converse-low-top-chuck-taylor-all-star-sneakers-roze-roze/17774-36/?channable=e44376.MjI2MTIwNjQwMA&gclid=EAIaIQobChMIysaJs_Pc2wIVECQrCh38rwdPEAQYAyABEgIG8PD_BwE#
[e0v2yev] (score 1, diepte 5 OP) What do you think of this one? (The pink one, not the gold colour)
http://www.converse.com/nl/nl/regular/chuck-taylor-all-star-ombre-metallic/559871C_085.html

Or this one? 
https://www.ziengs.nl/product/converse-low-top-chuck-taylor-all-star-sneakers-roze-roze/17774-36/?channable=e44376.MjI2MTIwNjQwMA&gclid=EAIaIQobChMIysaJs_Pc2wIVECQrCh38rwdPEAQYAyABEgIG8PD_BwE#
[e0va3ob] (score 1, diepte 6) I love both of those options!! I like the pink one if you’re looking for something to still stand out a bit, but I really think the second pair will go very well and be more subtle
[e0s68dr] (score 1, diepte 0) I've had several brides wear similar shoes, their dress was floor length and it wasn't too noticable, yet a cute detail nonetheless.

If that's your style, wear them proudly and dance the night away.
[e0s6yu0] (score 1, diepte 1 OP) Really?! That’s really cool!
Thanks! It’s great knowing I’m not alone!

Edited to add: love your name btw
[e0scp01] (score 1, diepte 1 OP) That’s a great tip, thanks! I’ll be sure to keep that in mind when I see my seamstress!
[e0sda7e] (score 1, diepte 3 OP) Haha, very true! You’ll be the envy of any high heeled guest!
[e0sdg58] (score 1, diepte 1 OP) That’s what I was thinking! And very summer needs at least one good ice cream right? 
I’m glad you picked up on that! I was afraid it might be the wrong shade of pink for mint green. But I’m glad you think it works too! Thanks!
[e0v2e4a] (score 1, diepte 1 OP) I'm reconsidering white converse. I never really liked the colour though...But I might even draw/paint on them, I do like to be creative...Though I'd worry about ruining them, probably.
[e0v3efh] (score 1, diepte 2) oh i like that idea, maybe get some cheaper basic (unbranded) ones to practice on?
[e0v3jhu] (score 1, diepte 3 OP) I've also found  this one
http://www.converse.com/nl/nl/regular/chuck-taylor-all-star-ombre-metallic/559871C.html (the pink colour)
Or this one 
https://www.ziengs.nl/product/converse-low-top-chuck-taylor-all-star-sneakers-roze-roze/17774-36/?channable=e44376.MjI2MTIwNjQwMA&gclid=EAIaIQobChMIysaJs_Pc2wIVECQrCh38rwdPEAQYAyABEgIG8PD_BwE
I'm considering ordering them both and sending the one back that doesn't match my dress. But then white and painting on them still sounds fun too...
[e0v5dnw] (score 1, diepte 4) omg they are both lovely !
[e0v5h5p] (score 1, diepte 5 OP) Thanks! I prefer the metalic ones, I think..but of course they're sold out in my size...So the search continues!
[e0v6hp8] (score 1, diepte 6) haha thats just typical!!!
[e0sk1jd] (score 1, diepte 1 OP) I get where you’re coming from, thanks for the advice!
I don’t like the colour of the one you’ve linked though...But a shop near my house had a kinda pale blue. Might check that one out...
I like this colour though!
[e0slbv0] (score 1, diepte 0) I love it!! The light green and the blush go together so perfectly too! :)
[e0to8r9] (score 1, diepte 4) Have you heard of irregular choice? They have wacky shoes in lots of different colours. Trainers and heels. https://www.irregularchoice.com/womens/trainers.html
[e0v2ay1] (score 1, diepte 5 OP) I love those!!! Especially the puppy-love ones. Only they're a little more expensive than I was looking for. They're briljant though!
Do you think the pink ones of these would look alright? They're a little more in my price range...Especially now that I accidentally got summer shoes instead. 
http://www.converse.com/nl/nl/regular/chuck-taylor-all-star-ombre-metallic/559871C.html
[e0v4fz8] (score 1, diepte 6) Absolutely, and if you want to customize them at all it isn't that difficult to attach patches etc on. Maybe pokemon patches? https://www.etsy.com/uk/market/pokemon_patches
[e0v4j9b] (score 1, diepte 7 OP) Patches are a cute idea! (And of course they don’t have the shoes I’ve linked you in my size. Boo.)
Nevertheless, thank you for your ideas! You’ve really helped me out!
[e0v4ybo] (score 1, diepte 8) What size are you? Maybe I can find something similar? I'm pretty bored!
(12 reacties met lagere score weggelaten)

=== THREAD 5ymeiv ===
SUBREDDIT: r/loseit
DATUM: 2017-03-10  SCORE: 95  REACTIES: 87
TITEL: ...my feet are smaller?
POST (source_id=post):
I notice that I'm often able to fit into a smaller size show, now. I normally wore an Women's 11 without a hope of fitting into a 10, now I can get away with wearing a 10 sometimes! 

I put on a pair of sneakers that I haven't not worn since pre-weight loss and they were a lot roomier than I remember. I also felt like I carried/balanced myself differently.

Is this a real thing?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[der79jn] (score 50, diepte 0) I lost a whole shoe size...and a beautiful shoe collection :(

On the bright side, i have a new beautiful shoe collection :)

also, necklaces are longer, bracelets and rings don't fit, and some purses (that used to look great) now look ridiculously big
[der5ljf] (score 17, diepte 0) Definitely real. Congratulations on your hard work and your new shoes!
[der5q4d] (score 15, diepte 2) Yup. This exactly. Fat doesn't pile up there like it does on torsos and legs, but there's fat there.
[der7e0b] (score 13, diepte 1 OP) Aw, that's sad! But I feel, it's like opened up a whole new world of shoes to me (way easier to find size 10 than 11). 

But yep! I know the feeling! I tried on an old watch the other day and I could remove it without undoing it. Safe to say I'll need to remove a link or two before I'll be able to wear it again. 

Nice job!
[der5t4q] (score 9, diepte 3 OP) So crazy! I guess when you're fat you don't really start to notice all of the things until you start to lose the weight.
[dera4kx] (score 9, diepte 6) As someone who just purchased a wedding ring that's already kinda loose, I feel this pain.
[der9jbv] (score 9, diepte 1) About necklaces - at some point, I had gotten so big I broke my favorite octopus necklace when I tried to put it on at the chain (a cheap one at that). Went from used to fit fine, to kind of tight, to snap. Worst feeling ever. You reminded me that I need to buy a new one now since my neck is a normal size again!
[der9xaf] (score 9, diepte 0) Yep. Fat is in a ton of places. Hell, when people get custom ear implants like custom ear plugs or ear phones, when they lose quite a bit of weight the shape and size of the ear canal changes and they have to get refit. 

I was always the type of guy who fit a definite 12 wide or double wide in some cases. Now I still fit 12, but some shoes like dress shoes and tennis sneakers that are typically sized up fit perfect as 12. I don't think my weight loss affected my width more so than me becoming fitter as I don't feet uncomfortable in normal width shoes (outside the Asian-marketed sizes that run narrow). I just bought three pairs of shoes: 11.5 boots that fit perfect, 12 tennis shoes that fit perfect, 12 running shoes that are described as "a little narrow" that fit perfect.
[der5zpx] (score 8, diepte 4) Yup. For me it was the tendons in my hands. So trippy.
[der9e8f] (score 8, diepte 0) Yay! That's so awesome! I was a womens size 9 for ever and then I started packing on the pounds and went up to a 10. That was one of my more embarrassing moments, realizing I was so fat I went up a shoe size. I recently got back down to my regular shoe size in December and until winter is over, I'm still wearing my size 10 boots. But I did order a pair of sneakers for spring and was still hesitant so I got a 9.5 size. Slightly too big. 😅 Sticking with it anyways to remind myself how we get stuck in our own heads with the old numbers. 

Congratulations! Wait until you can see the veins in your feet. One morning I looked down and was like, whoa I'm veiny. Hey the fat is gone!
[der5n6i] (score 7, diepte 1 OP) So weird! How does that even happen? Just like less fatty tissue on my feet as well?

Thank you! :)
[der6ty6] (score 7, diepte 0) My shoe size hasn't changed but I have noticed my feet appear slimmer.. longer somehow. So funny where we store fat.
[der65k3] (score 6, diepte 5 OP) Yes! Or like watches/rings that become too large!!
[der61vx] (score 6, diepte 0) Yeah, this is a thing, or it can be. I'm hoping to go down from an 8W to an 8 (which is what I used to wear).
[der67qm] (score 6, diepte 1 OP) So weird! Hope that you're able to do it! I used to have to **hunt** for wide calf boots (try finding cute, affordable wide calf boots in size 11!!) but now I don't even need them. My wide calf pair from last season are much to large in the leg.
[der6z7k] (score 6, diepte 0) Dude same! I shrunk from a women's 7.5 to women's 6.5 lol
[des6msg] (score 5, diepte 1) I bought a brand new pair of Tieks not anticipating this when I started my weight loss journey. Now they are getting kind of loose ;_;...
[derb0fz] (score 4, diepte 0) This is one of those weight loss things I reaaaally hope happens to me. Being a 10.5 is a pain in the ass because *apparently* half sizes don't exist above a size 10. :|
[derdj55] (score 3, diepte 7) Same here. Bought another ring a few months after the wedding. The smaller one is already getting too loose 3 months later. It will sometimes fall off whenever I wash my hands giving me mini-panic attacks that it'll go down a drain.
[der82h8] (score 3, diepte 2) Thanks, you too!
[der9oa0] (score 3, diepte 0) Yep. Depending on weight and fitness, your feet can shrink a size or more. 

At one point in my life, I was running sprints before bedtime, in my bare feet. My arches seemed to get higher, and my feet got shorter! 

Note: I was already seriously skinny when I was doing this. If I tried running barefoot sprints now, I wouldn't make it fifty yards.
[derez12] (score 3, diepte 1) Yeah, I think not only do they swell, but mine seem to have gotten flatter. Like the arches collapsed a bit from all of that weight. Now I'm looking forward to (hopefully) going down a size when I finish losing weight :)
[deroz55] (score 3, diepte 0) I more lost weight in my ankles which was strange.
[der72td] (score 2, diepte 0) I did have one pair of shoes that didn't fit, that suddenly did, but now none of them do.  Strangely enough my feet seem to be getting longer, probably an old man thing.
[der7dcp] (score 2, diepte 0) I bought a pair of closeout boots from an online store going out of business. The darn things were way too uncomfortable to wear.... until now. They fit like a charm and are actually starting to get slightly loose.
[der9my9] (score 2, diepte 1 OP) Yeah, I think everyone has had an embarrassing moment of realization along those lines. Congratulations on returning to your normal size! I totally get what you mean about getting stuck in our own heads. I still tend to gravitate towards the XL section of clothing in stores, when in reality I can probably wear a M now. Old habits die hard (but in a great way).

Thank you and congratulations to you as well. I've notice a bit of a difference, but can't wait for that day. Collarbones were a crazy thing, too!
[derfy3z] (score 2, diepte 3 OP) I feel like we should start some kind of clothing swap through this site... is that a thing?? You totally need to get out there, girl! And it's truly an incredible feeling - best of luck to you!!
[derkq0n] (score 2, diepte 4) 💜💜💜
[der9xim] (score 2, diepte 0) Awesome! I went up a shoe size during pregnancy and they have not gone back down. I threw away all of my old shoes except my favorite pair. Hopefully I will get to wear them again one day. Your post has given me hope!
[deret4m] (score 2, diepte 1 OP) Oh I totally feel that. The only place/brand I've *ever* seen a size 10.5 is Nike! Also why don't they make half sizes after 10? Like half sizes suddenly stop? How dumb. 

Good luck!
[derc5ty] (score 2, diepte 0) Finally confirmation this is a thing! I went from a men's 16 to a men's 13-14 and when I mention it people look at me like I'm crazy.
[dereuli] (score 2, diepte 1 OP) Haha wow that's a big jump! I'm sure it's easier to find size 13/14 rather than 16. Nice work!!
[derit41] (score 2, diepte 2) It really is. It's also weird to explain to people who haven't had this experience. I used to have an amazing collection of beautiful shoes. High heels and boots and clogs *sigh*. I now have 4 pairs. My indoor gym shoes, my outdoor running shoes, my every day runners and a pair of shoes for when runners aren't appropriate.

I miss my shoes. :,(
[derj1su] (score 2, diepte 3 OP) Absolutely! Ugh that's disappointing,
I'm sorry. But that only means one thing, more **shoe shopping**. Congratulations on your progress.
[derevcp] (score 2, diepte 1 OP) That's so crazy! Keep up the good work!!
[derexlc] (score 2, diepte 1 OP) Haha being a size 11 is such a pain in the ass, isn't it? So many brands just stop at size 10. Good luck, keep up the good work!!
[derfvhb] (score 2, diepte 3 OP) Haha yep! It's the worst... like having feel that **won't fit into a size 11!?** That's one way to make a girl feel special. Thank you, you as well!
[dereufq] (score 2, diepte 0) Yep, it's a thing.

I never thought it would happen to me, since despite gaining weight I never gained a shoe size. I've been a EU 41 since I was 13/14 years old. But as of last November I'm a size EU 40. My pretty heals don't fit anymore :( Losing weight is an expensive hobby. :P
[derf7s2] (score 2, diepte 1 OP) No way, really? How cool!
[derfpht] (score 2, diepte 1 OP) Me either, but hey I'll take it!
[derg6dx] (score 2, diepte 0) I didn't lose a shoe size but any fitted hats that I had I had to give away.  Lost a good 1/2 inch on my head.
[dergg8x] (score 2, diepte 0) I had a pair of bright red Keds that I wore in highschool. They were too tight for years, but they fit now.
[derho5o] (score 2, diepte 1 OP) That's awesome! Gotta love Keds! Nice job!
[derhl2b] (score 2, diepte 0) I am the same way. Before I began, I purchased some timberland chukka boots and they fit great. Now, since I've started running and losing weight, they rub my heels and are very uncomfortable to wear.
[derhphf] (score 2, diepte 1 OP) Ugh, disappointing about the shoes, but great job on the weight loss. Congrats!
[dern279] (score 2, diepte 0) Dude. A year ago I got rid of all my heels because I never wore them. For some reason, it had not occurred to me that wearing heels was so painful because I was *fat* and not because I wasn't used to wearing them. 70+ pounds later, I regret that I got rid of all of them because I bet I could wear the hell out of them now.

But a lot of the flats that I kept I also had to get rid of during my weight loss because they were suddenly gigantic. Weight loss is a weird thing!!!
[derou3f] (score 2, diepte 1 OP) Wow, that's a huge jump. Congrats on the weight loss!
[derostv] (score 2, diepte 1 OP) Ooh, hi stats twin! Similarly though, i had been a size 11 my entire life since fully grown (I'm only 21 so I don't know if that counts?) but I have also been overweight my entire life as well. Hope it happens for ya!
[derqpy8] (score 2, diepte 3 OP) Well I hope your feet shine a little!!! Good luck and keep up the good work!!
[derrvz5] (score 2, diepte 1 OP) Wow, that's awesome! And definitely an added plus!!
[derfzp1] (score 1, diepte 7 OP) Yes! I mean there could be *worse* things, but it still sucks! Congrats on your progress, though!
[der7928] (score 1, diepte 1 OP) It really is! Nice job!!
[der78sd] (score 1, diepte 1 OP) Wow, that's crazy! Nice job!
[der7afi] (score 1, diepte 1 OP) That's too weird! Keep up the good work!!
[der8e1l] (score 1, diepte 2) I used to be 10-10.5.  Then those were too tight, but long enough, now I wear 11-11.5, and my toes almost touch the end, but lots of wiggle room on the sides.  I have to heel lock my running shoes now.
[der8n4k] (score 1, diepte 3 OP) That's so odd... I wonder why that is?
[deupaw8] (score 1, diepte 2) My watch has gone from next to last hole to 4 holes in (3 to 4 in the past few weeks), at least it's a plastic band swatch so there's still plenty of play.
[deupodu] (score 1, diepte 3 OP) Wow, that's awesome! Congrats on your amazing progress!!
[der7g31] (score 1, diepte 1 OP) Ahh that's awesome news! Congratulations - keep up the good work!! 🎉
[der9ya9] (score 1, diepte 2) I haven't braved out of plus size clothes yet, still too scared even though my XL clothes are getting baggy. My SW was in the high 200s, but my CW is closing in on your SW. I can feel my collarbone again (easily), but can't yet see it. Can't wait for that moment.
[deretp4] (score 1, diepte 1 OP) Glad I could give you some home! Good luck!
[dercdtx] (score 1, diepte 0) Yup. Definitely a thing. It always throws me off too.
[dereuue] (score 1, diepte 1 OP) So crazy! It's unreal!
[derdlv6] (score 1, diepte 0) Yep. I remember going up a half size when I started gaining. (The majority of my weight gain was during an unhealthy 4.5yr relationship)
[dereq14] (score 1, diepte 0) Yes, right now I'm a 9.5-10, but when I lost weight the first time I was a comfortable 9. I think when you're bigger, your feet also tend to swell more to support the weight, so that makes a difference too.
[derewej] (score 1, diepte 1 OP) Yeah, that would make sense! Too crazy! I still got flippers, but now they're a little bit smaller! Keep up the good work!
[deretkg] (score 1, diepte 0) Ahhh I'm so excited! I am also a women's 11, and have a bunch of shoes that no longer fit me comfortably. And size 10s are so much more common than 11s. Yay! Just another thing to look forward to :)
[derft7s] (score 1, diepte 2) Yes! Or lots of brands run small, so even if you do manage to find an 11, it's still too tight. Thanks so much, congrats on your progress!!!
[derezcv] (score 1, diepte 1 OP) It totally is, isn't it! But your body with thank you... and we don't have those expensive medical bills/medications. At least it's a more fun, expensive hobby, huh?
[derna8n] (score 1, diepte 2) Oh absolutely. I just got really pissed off when it happened. I budgeted for new clothes all year, so that was fine, but new shoes?! Also, what's the point in my health game to a new shoe size?

Anyway, it still amuses me now. I still feel weird trying on shoes in my new size though, like it isn't real.
[derp2ch] (score 1, diepte 3 OP) Sorry, I guess what I meant by that was when you said losing weight was expensive, I was trying to elude to the fact that it's not as expensive (and way less fun) than medical expenses. 

Congratulations! What an incredible ion you've done!
[derf2it] (score 1, diepte 0) I noticed this too! Another thing that shocked me was having to adjust my snapbacks because they were getting loose
[derfnzl] (score 1, diepte 0) I wouldn't have predicted this, but I guess it makes sense.
[derlhd3] (score 1, diepte 0) Definitely a real thing! I used to wear a 7.5/8, now I'm a 6.5/7. Luckily I've never been much of a shoe person, so I didn't have a ton of awesome shoes I shrank out of.

Congrats! Time to go shoe shopping :D
[derotic] (score 1, diepte 1 OP) Wow, that's insane!

Thank you, you too!
[derowvz] (score 1, diepte 1 OP) Weight loss is so weird!! It's crazy to notice the things you never did when you were heavier. I seems like I was blind to it all. 

Congratulations on your weight loss! Giving away your heels only means on thing, time to go shoe shopping!!
[dern4pn] (score 1, diepte 0) Went from Men's 12 to 10 by losing 60lbs
[dero8nm] (score 1, diepte 0) Hi stat twin! As a women's size 12, I am very very hopeful this will happen. I'm trying to think back... I've been a 12 since I was fully grown, but I've also been at least slightly overweight. Hm...
[derqo5d] (score 1, diepte 2) I'm already super excited for all the stores I can now go in who won't be like "sorry we don't carry that size" YES!
[derp353] (score 1, diepte 1 OP) Still a loss! Nice job!
(7 reacties met lagere score weggelaten)

=== THREAD 1q0o049 ===
SUBREDDIT: r/Mommit
DATUM: 2025-12-31  SCORE: 69  REACTIES: 86
TITEL: Update to my sister in law bringing hand foot and mouth to Christmas.
POST (source_id=post):
Previous post linked here: [https://www.reddit.com/r/Mommit/comments/1puj79g/yet\_another\_christmas\_drama/](https://www.reddit.com/r/Mommit/comments/1puj79g/yet_another_christmas_drama/)

The tldr; SIL brought my nephew (almost 2) who was miserable, had fever and was in pain with hand foot and mouth to Christmas day. I faced what I perceived was judgement for suggesting they shouldn't have brought their child to Christmas privately to my husband, and I felt like I was being treated like a grinch for taking my one year old home from family Christmas (this was publicly communicated as graciously as I could) to prevent him catching hand foot and mouth disease. I wondered if I was going crazy. It ended well and I perceived at the time, that my in laws supported my decision and my husband said it was the right decision. I wanted to move on.

  
I am really feeling frustrated and again am feeling like I'm going crazy. The good news is the limited contact meant my son never caught hand foot and mouth disease. The bad news is my husband trying to convince me that my parents in law were on my side/he agreed with me was not actually true. While my husband states he agrees with me, apparently my in laws spent the rest of Christmas day agreeing with my sister in law and saying things like I'm being over protective, everyone catches hand foot and mouth disease, and I was over reacting/was a grinch. They compared it to chicken pox.

  
I genuinely feel my SIL was negligent in catering to her baby's needs, who cried the whole time and was unhappy, and negligent in social responsibility for making sure my son doesn't suffer like her kid did. Not to mention the adults. It sounds like a few people have hand foot and mouth disease now from that event. 

  
I don't know how to approach this going forward. For context, this is the second time my sister in law brought her hand foot and mouth child to a family event. The first was a few months ago at my father in laws birthday, where my husband and I also had to not attend because we didn't want our (at the time 7 month old) baby getting sick, their justification was my parents in law were already "exposed" anyway - but the reality was they didn't catch it before my nephew was there for my FILs birthday. Apparently after that event, for two weeks, everyone who attended either had COVID or HFMD. Why does my nephew keep getting HFMD? There were two strains across the summer and winter and he caught both as he has moved across two day cares.

I'm not sure how to approach this going forward. This behaviour is unacceptable, and is one of many examples of this behaviour. I would feel better if she was more considerate, but the fact is no one apart from my other SIL (not the one with a baby) appears to agree with us in the family.... does anyone have any advice for how to approach this sort of family relationship issue going forward? I've historically told my SIL things bluntly and clearly, which she always responds by bursting into tears and then I become the bad guy. My husband has the same response. My husband, SIL (not with baby) and parents in law all said the same thing as well- historically they've tried to correct selfishness/encourage her being more considerate but all she does is burst into tears and doesn't change her behaviour.

  
So what do I do?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[nwze7rx] (score 202, diepte 0) You did the right thing by leaving. No reason your child needed to get sick. If she cries, she cries. Continue to protect your kid. I'd she continues to drag an actively sick kid to things, leave.
[nwzf3sz] (score 101, diepte 0) I’d take my child home from a party if another kid has chicken pox, too, so that’s a bizarre comparison for your in-laws to make. HFM might not be particularly dangerous, but it is painful! No good parent would willingly expose their child to it.
[nwzetls] (score 92, diepte 0) Unfortunately you can’t control her, just yourself. Everytime she brings her sick child, please leave. My son caught HFM and was miserable. He couldn’t eat or swallow. I caught it from him. I lost 15 pounds 🥲 you did the right thing. Even if they don’t agree with you, who cares? Just leave.
[nwzff6f] (score 52, diepte 0) Not everyone gets HFM. We’ve managed to avoid
[nwzj0xl] (score 48, diepte 1) The difference between HFM and chicken pox is that you don’t build immunity to it so you can keep catching it and each time babies are miserable! OP well done for leaving, this isn’t even a question. I woudl’ve done the same!
[nx07qbp] (score 26, diepte 1) And the husband needs to join them as a damn united front.
[nwzilhf] (score 23, diepte 0) There's a reason why the Varicella vaccine is required for schools now, so that children don't get (or are less likely to get) *chicken pox*.

Sadly, there is no HFM vaccine. I grew up in the era of "chicken pox parties", where if one child got it, all the other parents let their children get exposed to get it over with. It was miserable for children and parents alike; I personally had the chicken pox, immediately followed by strep throat, which was immediately followed by scarlet fever. I missed around a month of school in the 3rd grade.

Only one of my children has had HFM, and as soon as it was recognized and diagnosed, we made arrangements to keep him home. We did not drag him out and about.

SIL with the baby needs to put her big girl panties on and quit being a sniveling child, and properly care for her child. Missing a family function or two isn't going to hurt the child -or her- in the grand scheme of things.
[nwzqlyl] (score 22, diepte 2) You DO build immunity to the specific virus that caused that round of HFM. The difference between chicken pox and HFM is actually that there is only ONE virus that causes chicken pox while there are many different viruses that cause the symptoms commonly called HFM. 

My kid got HFM once and even though his pediatrician said we could let him go back to daycare once the sores scabbed over, I still kept him out until the scabs were gone because I didn’t want anyone else to get it. OP’s husband’s family sucks.
[nwzem3k] (score 15, diepte 0) Hand foot and mouth is a very unpleasant illness. Yes many kids catch it and recover, but in the meantime many are uncomfortable and if adults catch it they can be miserable. My preschooler had it this fall (outbreak in the class) but my one year old did not catch it thankfully.

If someone knowingly exposed my kid in a social setting I would be very upset and I would certainly leave. Your in-laws are not reasonable people and there are no magic words you can use that will make them reasonable people. Any normal person would agree that actively spreading an unpleasant illness to another baby is not a reasonable thing to do, these people apparently don't agree with that. My in-laws (never this dramatically) also have different ideas about health/illness/germ management and I simply don't care and assert my boundaries because I am in charge of keeping my own kids as healthy and safe as possible. 

Your in-laws (and husband) have decided that nothing is more important than a selfish adult not crying and that includes your baby's health. This is a shocking thing. I would insist my husband acknowledge how crazy this is but all you can do with the rest of them is hold the very reasonable boundary of protecting your baby's health.
[nwzjc47] (score 15, diepte 0) I swore your kid was gonna have it, HFM is so freaking contagious. Sorry your in laws suck but  yourself so lucky your kid didn’t get it.
[nwzmakq] (score 13, diepte 1) One of my kids had it when he was 1. We were crazy about hand washing/not sharing food/drinks and neither parent or our 4 year old got it. The 3 of us that were unaffected had never had symptoms of it at any other time of our lives previously either. 

My kid that had it though was absolutely miserable. It’s the sickest he’s ever been, it lasted weeks, and he lost all his toenails a few months after.
[nwzgnc6] (score 11, diepte 0) My grandkids who are in daycare seem to get HFM every other month. It is rapid in daycares. Not only do their parents not take them anywhere so they don’t spread it, we don’t want to get it so we are ok with them staying away. It is very contagious. You are not wrong. She was very irresponsible bringing him.
[nwzqfcd] (score 10, diepte 2) You actually do build immunity to each HFM strain, but there are many, many strains.
[nwzwjm1] (score 9, diepte 1) Exactly this.
[nx0dqu1] (score 7, diepte 0) People never fail to amaze. This woman brought a child with active HFM to family events with other children *twice* and her parents say that’s fine? 

Regardless of what they said after you left, they may not even agree with her. They’ve catered to this burst into tears whenever someone calls her out bs for decades. They lack the fortitude to deal with her boo-hooing. I’d say to continue skipping events when her kid is sick, but they’re at the point now where they just won’t tell you. If you don’t want your child exposed, you’ll have to forgo every event she and her child attend. 

What an awful disservice they’ve done all of you.
[nx1o8ai] (score 6, diepte 3) I was extremely upset to find out there are over 17 strains of hfm. 😭
[nwzfmk6] (score 6, diepte 0) It feels like whatever the issue is, your SIL will remain the same. Protecting your family (and sanity!) is the best at to go about it. That being said just be ready for unpleasant backhanded compliments / conversations but ultimately that's the price to pay in order to protect your family. It sucks but better safe than sorry.
[nwzgshz] (score 6, diepte 0) You did the right thing by leaving   Your SIL is not very considerate.  Honestly I would maybe consider doing some holidays separate from SIL.   Like going the weekend before Christmas to ILs and celebrate your own Christmas at home.
[nwzjgqs] (score 6, diepte 0) She’s not a good person. Missing something is much better than potentially getting people sick. Every time.
[nwzjq8s] (score 6, diepte 0) There are multiple strains of HFM and so you can definitely catch it more than once. And not everyone suffers the same symptoms! I think it’s something like half the population may show no symptoms at all (you’d have to check the stats on that) while some get it so bad they lose their nails. Good job protecting your kid. While your child may eventually catch it, doesn’t mean you have to expose them to it so they catch every strain while at such a young age!
[nwzqurb] (score 5, diepte 3) well my point was you can get HFM many times still stands
[nwzqrkb] (score 5, diepte 2) Hasn’t your oldest been vaccinated against chickenpox?
[nwzfnwb] (score 5, diepte 0) The way you approach this going forward is by spending holidays elsewhere
[nwzi57d] (score 5, diepte 0) HFM is painful. I caught it a couple years ago from my daughter when I didn’t know what it was. Holy MOLY do the sores in your mouth hurt. The fact that they’re ok with this means they all deserve a bad bout of the disease. And for you to mention it everytime. Continue leaving when she brings her kids sick. Loudly state the everyone that if they want to risk getting sick then by all means have fun doing so.
[nwznply] (score 5, diepte 0) I think it’s clear she’s going to keep acting the same way. She relies on other people saying “Well, she’s here now, it is what it is, it won’t be that bad,” to excuse her behavior. My best friend’s dad died of Covid because of people like her. It’s not okay. You’ll keep holding her accountable, she’ll keep insisting that all decisions made by her are understandable and fine, and you’ll keep playing defense with your kid’s health. She should’ve left the party, not you.
[nwzosqo] (score 5, diepte 0) There are soooo many strains, it’s not a “catch it and become immune” illness.

You made the right choice. Sorry your husband is being difficult.
[nwzqjtl] (score 5, diepte 0) If it’s like chickenpox they mean preventable and contagious then yes it is.

You did the right thing going home and continue to do so.

If they care so little about your child’s well-being then they don’t get to spend time with him.

My brother ended up in the hospital with chicken pox as a kid because he didn’t have much externally but he had so much internally he couldn’t eat and it started to interfere with his breathing.
[nx00u2p] (score 5, diepte 0) I would have done exactly what you did. Hand, foot and mouth is terrible. My son had it and really suffered. Every child does NOT get it so your in laws justification was ridiculous. Your sister in law was completely wrong for bringing a sick kid to Christmas.
[nwzqp69] (score 4, diepte 1) In-laws probably grew up in the age of chicken pox parties to get all the kids sick so it was done and over with in one time period, before they got old enough for it to be more dangerous. Stg that HFM was not common at all in the 90s, none of the younger boomer-age grandparents I know had even heard of HFM when my kid got it. Theyre likely running on assumptions about childhood illnesses and the severity thereof.
[nx0jurd] (score 4, diepte 3) I lasted 37 years without chicken pox, before I  then finally was able to receive the vaccine!  And I was definitely exposed. I remember carpooling to ballet class, sitting next to a kid who noticed she was breaking out in pox sores immediately after we got out of the car (and we were crammed into the backseat together). I assumed I had some sort of natural immunity, like I had been infected at some point but remained asymptomatic. I still tried to get vaccinated as an adult, but found it ridiculously difficult to access the shot. 

It was only when I got pregnant that they tested my blood and found I didn’t have any chickenpox antibodies. Was finally able to get the vaccine.
[nx0hmpv] (score 3, diepte 1 OP) Thank you for your clear words of wisdom. I had wondered if there was a specific action I could take so that they listened and could behave better, but you're absolutely right. I will let it go and just have to wear whatever insults they say behind my back.
[nwzeq2r] (score 3, diepte 0) I would stand my ground and not show them that it even matters to you (the way they act) because all that matters is your son.  People like to be miserable and bossy and bullies.  I wouldn't give them the satisfaction of bringing me to their level.  Just do what you feel is right and don't justify it with excuses.  Because you'll neve please everybody,  especially hyper sensitive people like her or your in laws.  So just let it roll off and keep moving forward in your own life.  You don't have to respond or act on anything.  Just take care of your kid,  that's all that matters.
[nwzjrkv] (score 3, diepte 0) HFM is one of those illnesses the daycare tells every kid in the class about, because they’re trying to stop spread. I’m a bit more lax than some in that I think it’s ok to bring a fever-free but snotty-nosed kid to an event. But bringing a kid with HFM is insane. Neither of my kids have ever gotten it, and I would really like to keep it that way. Common colds are inevitable. HFM isn’t.
[nwzlcu4] (score 3, diepte 0) You did the right thing! Your SIL and your in-laws are selfish jerks. Yea, it sucks missing things while kids are sick - but this is life with young toddlers. It sounds like this is a pattern / I’m not sure there’s anything to do with your SIL, age sounds like a pain in the ass. But I would set real clear boundaries with your husband about what you will and will not accept in terms of illness exposure for your child. He needs to be on your team, not on his sister’s team.
[nx0kvoz] (score 3, diepte 1) Why isn't her husband's lack of involvement being said enough?  This isn't about the ILs anymore; he should be defending HIS child's health more than OP.
[nwzx8z2] (score 3, diepte 0) I hope your in laws get HFMD…
[nwzyqs1] (score 3, diepte 0) You don’t cater to her tears. Leave/make her leave your house. It doesn’t matter that most kids get HFM at least once - it’s irresponsible to knowingly expose sick children to healthy ones.
[nx06hrm] (score 2, diepte 2) Omg that sounds intense for your poor bubs. 

But kudos to you for not catching it! How did you carry him / change him / feed him etc? Did you wear gloves? 

I’m trying to prepare just in case mine gets it.
[nwznm3f] (score 2, diepte 1) My oldest is 10… never had it, have avoided chicken pox too.
[nx0h46s] (score 2, diepte 1) A tip to your children - that daycare doesn’t have adequate cleaning procedures if it goes around every month. That’s…. Not normal. Even in daycare world where a new illness every 6-8 weeks is pretty typical.
[nwzmpam] (score 2, diepte 0) People are unfortunately very inconsiderate. We also had to bow out from a Christmas bunch with my SIL’s families, because three of the guests had gastro, but were still going to attend. 

I think you did the right thing by leaving.
[nwzoje0] (score 2, diepte 0) We've had hfmd twice and even though everyone catches it, it's still great to not have it! You never know how bad it's going be. I kept lo home as much as possible to stop the transmission or was fully transparent with anyone we did see to let them do their own risk analysis. 

And when my kid is miserable, we snuggle on the sofa. I don't drag him around places! 

So please, keep leaving if she pulls these stunts!
[nwzpit6] (score 2, diepte 0) Since it’s your husbands family, I’d have him send a text that says something like, “In the future, please let us know if you are ill as we are not comfortable attending an event where we might catch something.” If they respond angrily, he could just say he understands they were comfortable putting themselves at risk of HFMD, but you were not.

I have this with my family. They tried bringing children with HFMD to a party, and I said absolutely not. I had that and it sucks. And yeah, pretty much every kid gets it, but I’m not going to put my family at risk of catching it again. It can literally make fingernails fall off. It’s so gross.
[nwzpqqe] (score 2, diepte 0) There’s nothing to address here. Do not apologize or over explain, you will just appear defensive. Keep calm and carry on leaving when she decides to show up sick!
[nwzq3xr] (score 2, diepte 0) Honestly, I wouldn’t say anything to her. Because she’s just gonna start to cry. Ignore her. Whenever she comes near you walk away. Wash your hands after she touches you. keep everything light and cold. Same for your in-laws? 
Don’t leave your son alone with those people. Because they’ll babysit your kid and her kid and your baby will definitely catch it.
[nwzsrwt] (score 2, diepte 0) Everyone gets HFM? I honestly don’t know of anyone who has had it, and the kids in my family went to daycare and preschools.
[nx0mrg7] (score 2, diepte 1) Agree. Until this sub I didn’t know it was a thing kids got - we only hear about it in cattle.
[nwztlhz] (score 2, diepte 0) You definitely did the right thing and if it happens again I would get up and leave immediately. My kids are 5 and 2 and luckily they have never had it. I pray it never happens because it seems miserable and painful. I’ll do every thing in my power to prevent them from getting it.
[nx0sz1d] (score 2, diepte 0) Hfm sucks so bad. My kids and I had it in the spring. I would run from anyone with it. And I’m an adult. For my kids I’d probably cuss someone out. That’s messed up.
[nx196iw] (score 2, diepte 0) My kids have never had HFM. Not everyone gets it and not everyone should or wants too. 

Your SIL seems to be a narcissist. Selfish and uncaring. I’d steer clear of her. She doesn’t care about other people or her own kid. So sad.
(34 reacties met lagere score weggelaten)

