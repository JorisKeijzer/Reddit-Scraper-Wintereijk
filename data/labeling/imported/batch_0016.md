# Label-batch batch_0016

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
Schrijf het resultaat naar `batch_0016.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: kwtwu6, 1146t1f, w99v5d, 10bsih6, wo64b4).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD kwtwu6 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-01-14  SCORE: 5  REACTIES: 32
TITEL: Flat feet and underpronation?
POST (source_id=post):
Hi everyone! I just found and joined this sub and I was hoping you could help me with a question that has me a little perplexed but I'm not sure if this is the right sub to post it in. If its not the right sub or there is a better sub to post it on let me know and I'll take it down. 

I was looking online to buy a good pair of running shoes--the Nike infinity react to be more specific---for everyday use but I've found conflicting advice. I have flat feet and from everything I've read online I've found that I need stability shoes because I will be overpronating. I read that this means that I will be stepping more with the inside of my foot and this will show on my shoe with more wear on the inside edge of my shoes. However when I look at the wear on all of my shoes it is always more worn on the outside of the shoe. From what I've read this means I'm an underpronator but this is usually attributed to feet with high arches. When I searched online I only found articles that discuss flat feet and overpronation or high arches and underpronation but no articles that discuss flat feet and underpronation. I walk a lot for work and I read that the react are comfortable shoes that are good for walking/running and people who have flat feet. With everything I've read now I don't know what type of shoe would be best since they reccomend stability shoes for flat feet and neutral shoes for underpronators. 


If it helps I've owned the Nike lunarglides and the Nike Pegasus in the past. Both were comfortable but the most comfortable of the two running sneakers I had were the Nike lunarglides. I would go to a specialized running store but they don't have one where I live and the closest one is almost 3 hours away.

Thanks for your help!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gj6es0m] (score 6, diepte 0) Fellow flat foot supinator. In my experience you want to look for shoes with a good amount of Cushioning since your outside foot takes a pounding. Last year I ran mostly in the Saucony triumph 17 and the pegsasus 37s.
[gj7h281] (score 5, diepte 4) Just here to agree with @thisismyphonegfgf

I have big flat feet (US size 14) and pronate, and my Saucony Triumph 18’s are the most comfortable daily trainers I’ve tried in a long time!
[gj7uveg] (score 5, diepte 0) Flat foot supinator (underpronator) also, low arc, wear on outside. As mentioned above, sufficiently cushioned neutral running shoes is my advice, especially if you are a heel striker. I’m not a Nike runner, more of a Saucony guy. My current rotation: Saucony Triumph 17 (easy), Ride 13 (daily/long), Endorphin Speed (faster runs). The Triumphs are a bit too cushioned for my liking, the Ride 13’s will take over when they are retired. My shoes used to wear on the outside heel fast when I started running. While getting a better and faster runner I started to lift my feet a bit more :) and became more of a midfoot-forefoot striker. This will compensate for the lack of damping due to underpronation, requiring less cushioning, but takes some training. Still maybe some wear on the outside, but not a lot.

Not to say you must transform from heel striking, nothing wrong with that (it just happened to me), but if you’re landing mostly on the (heel) outside: cushioning is important ‘cause you’re getting less damping/travel from pronating.
[gj6j8e1] (score 4, diepte 2) Haha no we're definitely out there. Try a few and see how they feel. Also watch the level of wear on the outsoles. I have to retire shoes by 200 miles at most because my foot strike just grinds them down over time.
[gj6kgu3] (score 3, diepte 3 OP) Haha good to know! Thanks again I'll definitely look into those.
[gj6f4b4] (score 3, diepte 0) Flat foot underpronator here too!! I’ve been running in the Nike react miler, hoka Clifton 6, new balance 880v9, and my favorite, the saucony ride. I use neutral shoes since stability shoes will push our feet even further to the outside of the sole!
[gj6sd4x] (score 3, diepte 0) You know, when you look at me standing there, you'd say I have high arches. Watch me run and suddenly I have flat feet that land on the outside edge and sorta overpronate all the way in. It's ridiculous. I used Nike Air Structure for a long time but I've been getting pains recently. I've switched over to Altras currently to try and get more cushion with a big toe box. They feel good. Reading here is giving some other options -- thanks guys!
[gjdc5ui] (score 3, diepte 3) I think it's always good to have a healthy level of skepticism! Keep in mind that can apply to physical therapy as well, some therapists work different than others. Also some PTs may be able to evaluate your gait but not have much knowledge on the actual technology that exists in running shoes and how to use it. I don't mean to be a cynic but PT only works well if both parties are willing to work with each other and put in the effort. Depending on what you're trying to get out of running the recommendations may be different. If you're running to simply get in shape they may say one thing but if you show you're willing to invest time and energy into improving then there's a whole host of specific exercises to strengthen imbalances that will ultimately make you a better, faster, stronger runner. Another thing to keep in mind is that you may have imbalances now that would indicate a specific type of shoe may work well for you but as you address those imbalances and improve on them you may be able to utilize another type of shoe. Hope your  consultation goes well!
[gj7hs6a] (score 3, diepte 0) If you are running in neutral shoes and not getting injured and don’t find them uncomfortable then you don’t need to wear a stability shoe. The evidence that stability shoes reduce injury or that injury is caused by overpronation is pretty weak. 

Having said that the Nike Infinity React is not a traditional stability shoe, and from your description I think it would probably suit you quite well. There is also the React Miler and new Zoomx Invincible to consider from Nike. The Reebok Symmetros, Saucony Triumph, New Balance 1080, Asics Nimbus, Mizuno WaveRider and Brooks Ghost/Glycerin would also be good.

If you seriously want to get in to running it might be worth going to see a physical therapist to see if you have any weak muscles that need work due to your unique gait.
[gj6imw7] (score 2, diepte 1 OP) Thanks for the reply! I was seriously expecting someone to tell me I was crazy and it wasn't possible to be both. I'll see if I can try both of them in a store. I know footlocker or Champs will have the Nike Pegasus but hopefully they also have the Saucony triumph to try on as well.
[gj6js2e] (score 2, diepte 1 OP) Hi thanks for the advice! I had looked into the Nike Miler because it had the react like the infinity but ultimately liked how the infinity looked a little more. Am I correct in assuming they're built the same because they both have react and just have a different aesthetic or am I mistaken? I just checked out the 880 online and I like the look a lot! I have a pair of Hoka hiking shoes so I know how comfortable those are but they don't have them where I live. The ones I bought I picked up on a trip we made in an REI. In your experience would you also suggest I look into shoes that are more cushioned like the first poster recommended?
[gj7zg1w] (score 2, diepte 2) React miler has more react than react infinity. I think react infinity has the right balance of cushioning.
[gj9ouxo] (score 2, diepte 2) If the pandemic makes that difficult a number of stores can do something for you online. They may ask you to take a video of yourself walking in bare feet or something like that.
[gj9qivs] (score 2, diepte 1) I wouldn't necessarily rely on someone at a running specialty store to identify your gait, research has been done on specialty fitters ability to identify "overpronation" and it is very poor. There's also no definition for overpronation, there is no specific degree of motion at which pronation is classified as overpronation. I would definitely recommend trying on different shoes but be wary of specialty stores trying to classify you. Also the infinity react fits very narrow through the midfoot so if you have a very flat foot you would likely be pushing against the mesh on the side of the shoe and find it bothersome.
[gj9vjv2] (score 2, diepte 2) Noted (for myself and hopefully OP too). My point was that somebody who sells running shoes for a living will probably still provide something more meaningful than what OP had interpreted originally.
[gjdho2h] (score 2, diepte 4 OP) Thanks a lot buddy! I'll keep that in mind and try to have clear goals when I go in for the consultation :)
[gjgxugc] (score 2, diepte 4) This is a fantastic post.
[gj9qp1c] (score 2, diepte 2) Shoes have much less an impact on injuries than the shoe companies want you to think. The whole “over pronators need a stability shoe that stops them pronating  to avoid injury” thing has been proven to be untrue, and nearly every manufacturer has stopped doing this or is phasing it out. Nike, the biggest running shoe manufacturer, has stopped even using the term “stability shoe”. The best evidence we have at the moment shoes that the shoe that is most comfortable is the one least likely to cause injury. 

I’d definitely see if you can see a physical therapist, but probably focus more on form, strength and mobility than shoe choice :)
[id7gkoa] (score 2, diepte 2) I’m the same as you. I spoke to my doctor who said my supination was caused not by high arches but by weak inner knee muscles. She recommended laying with a towel rolled up under your knees and clenching only the inner knee muscles in a way that makes your kneecap move. Keep your hands on your outer knee muscles to make sure you’re not clenching them. It’s extremely difficult for me to do without moving the outer knee and I’m willing to bet it would be for you too. We supinators rely too much on the outer knee.
[gj98g9l] (score 2, diepte 0) Fellow flat foot supinator here.    I have enjoyed the Saucony Ride 13's, however I wore them down quickly.  I am not sure what your weight is, but I have finally realizing that the heavier we are, the softer the shoe, the quicker I go through shoes.  The people in the running store was too shy to tell me this outright, but one brave store clerk hinted at it.  :D  I have also really loved the Brooks Adrenaline 21- it is a stability shoe, feels soft and I don't think I am going to blow through them as fast as I did the Ride 13. FYI, Adrenaline 21 runs about 1/2 size small for me. I also like the cheaper but solid Saucony Cohesion 12.  For trail walking/hiking, a super comfortable shoe I like is the Saucony Guide 13 TR.  I also came across this video yesterday that explained what I wish I would have known 1 year ago. [https://www.youtube.com/watch?v=GNarHOc7y38](https://www.youtube.com/watch?v=GNarHOc7y38)
[gja5k23] (score 2, diepte 1 OP) Hi there, I'm 5'9" and I generally fluctuate in weight and can be anywhere from 140 to 152... I'm probably hovering around 150 since I haven't been exercising hehehe. Thanks for the video it was pretty informative!
[gja6q7v] (score 2, diepte 2) You are welcome.  Good luck in finding your most magical shoe.  I don't imagine that your weight will impact a comfy shoe.  :D
[gjd46s6] (score 2, diepte 0) I have completely FLAT feet (not low-arched) and am a very severe underpronator. So it can definitely happen. Neutral shoes work the best for me, but mild stability shoes are also okay, such as the Lunarglides. I think the Infinity Reacts might be a good choice, as I'd like to try them myself.
[gjgqqdv] (score 2, diepte 0) Some quick thoughts, I have wide flat feet as well and the wear patterns on my shoe, particularly the front area, mostly focus around the outer part.  I have been running in Ultraboosts (EnergyBoost and now UB 20). Before that I ran in more a minimalist pair of running shoes (which I lost and have since forgotten the brand) mixed in with a Goretex Addidas pair of shoes that is a lot firmer in the mid-sole than the UBs.

What I can say is that if you feel comfortable when running and feel no pain my impression is that you should not worry about it. In my case, all the shoes I have just mentioned worked. What I try to do is avoid shoes with high arch support. I have a pair of boots with this feature, and I can tell you that over time, it becomes more than just a slight niggle. One example that comes to mind is the Adidas Boston 9. I haven't run in it, but I have heard it has high arch support, which made it a no-go despite my positive experience so far with Adidas shoes.
[ie9r2vz] (score 2, diepte 0) Know this is an old thread, but just wanted to let you know that I was diagnosed by an orthopedic surgeon many years ago as a "flat-footed supinator". Rare, but not impossible. I also have Morton's Neuroma ... which makes sense to me intutively, that if I walk on the outside of my feet, I push off more with the little toes. Unfortunately, this makes appropriate running shoes very tough to find. I am currently wearing Brooks Glycerin. These have been very good, but still looking for that great/perfect shoe.
[gj6uqhz] (score 1, diepte 1 OP) I'm definitely gonna look into all the shoes that were recommended and shoes with more cushion now. Thanks for the suggestion!
[gj756tq] (score 1, diepte 0) I believe you have misunderstood overpronation. It doesn't mean you wear out the inside of your shoes, just that you roll inwards somewhat excessively after landing. There are some good videos online that show the difference this and a neutral gait. My suggestion is to visit a specialist shoe store and have them identify it, rather than rely on strangers here online! You are most likely an overpronator based on your description, but better to have somebody help you confirm in person.
[gj8apy9] (score 1, diepte 1 OP) I'll definitely try to make the trip to a specialized running store when I get a chance. Thanks for the advice!
[gjbgcgq] (score 1, diepte 2 OP) Hi! Yea for the most part I'm always a bit skeptical when I'm getting advice from someone with a vested interest in me buying something off of them but it's good to know that in this case it is more so because they aren't as good at identifying pronation as opposed to being a scummy sales person. I always feel that people in sales don't have my best interest in mind when recommending something so I'd rather do my own research for the most part. I went ahead and took /u/betterchangeyourmind advice and looked into my local physical therapy facility and they offer a free consultation so I'm gonna try and set up an appointment sometime soon. Thanks for the heads up!
[gj8bz5a] (score 1, diepte 1 OP) I'm gonna look into how much a consultation from a physical therapist is because I probably should get a professional evaluation before I run off and injure myself. Thanks for the list of suggestions I've got some researching to do now!
[gja7qhm] (score 1, diepte 3 OP) Awesome thats good to know! Thanks for all the details I appreciate the help :)
[gj8coa6] (score 1, diepte 1 OP) I'm gonna really look into the Saucony after everyone's suggestions. I've heard of them and seen them but I don't think I've ever tried on a pair. Thanks for the advice!
[gjdh8ll] (score 1, diepte 1 OP) Hey thanks for the reply fellow monkey :P... yea those are the ones I'm most interested in as well but I'm gonna look into and try all of the other shoes the other posters reccomend before settling on one.
[gjhzi0e] (score 1, diepte 1 OP) Yea I noticed that my feet hurt when I tried on a pair of hiking shoes that had arch support. I tried some on while at the store and they were uncomfortable within a few minutes of wearing them so I have steered clear from shoes like that ever since. Thanks for the suggestion!

=== THREAD 1146t1f ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-02-17  SCORE: 12  REACTIES: 32
TITEL: Are HOKAs still the ideal shoes for standing around?
POST (source_id=post):
I don't run marathons, but I have marathon standing-sessions. I'm in med school, and I need new shoes. Most of my shoe-related google searches have led me to this sub. Several people in recent posts have been claiming that HOKA has not innovated in the last few years, while other brands have overtaken them in terms of cushion. But is this only relevant for runners, or is it also relevant for people who just have to stand up for a really long time?

&#x200B;

My current shoes are the HOKA bondi 6, and I really like how they felt. But they're on their last legs. I got them like a year ago (which I assume is much slower than serious runners destroy their shoes). The worst is the lining of the back of the shoes has come off and will poke into the back of my feet if I'm not wearing thick enough socks.

&#x200B;

I'm just trying to get shoes that will maximize the amount of time before I get fatigued from standing/walking around. Of course I'm quite tired at the end of the day, but I don't have any serious foot-pain issues like plantar fasciitis. If they'll last longer or look better than my HOKAs, that's certainly a bonus?

&#x200B;

Many of my friends have oncloud and like them, but the ones I've seen here mentioned as innovating more than HOKA are ASICs and Saucony. Are these any good for standers?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j8upegx] (score 35, diepte 0) I don't think a lack of innovation for Hoka is really relevant if you're not running in them. That being said, their popularity has forced other brands to innovate and create something similar. Hokas are still by far and away the most popular choice for customers I have who are in healthcare and are still my favorite shoes to wear at work myself when I have a long day on my feet. Other similar options are the ones u/materix01 mentioned, as well as the Saucony Triumph. A lot of people's gripes about Hoka are about durability, but it seems like you're not having that issue.
[j8ukggb] (score 15, diepte 0) Hoka Bondi 8, Asics Nimbus 25, NB More V4 have all been popular standing shoes. You want cushioning but you also want something that's stable and not too soft.

Two years is honestly a pretty good amount of time to get out of a walking shoe.
[j8ur1xj] (score 11, diepte 0) Wouldn't an optimal standing shoe be a no rocker (flat bottom), no drop shoe?  Also, maybe for long term health of the foot, a minimalist shoe?  Do arches tend to collapse over time due to atrophy of the muscles in the foot, caused by overly cushioned and supportive shoes?  Just thinking aloud...
[j8utj8i] (score 10, diepte 1 OP) I'm open to this being true, although I would be a little disappointed to hear that trying to maximize comfort is inherently bad for my feet...

I'd probably want to see some data on it before before sacrificing comfort for this reason.
[j8uogpy] (score 6, diepte 0) I absolutely love my Clifton's for just every day bullshit.
[j8v0os4] (score 5, diepte 1) I'll add a Brooks Glycerin to that list, the plushines (is that even a word?) of that shoe are unbeatable.
[j8v27p4] (score 4, diepte 1) No. The Born to Run fad was over a while ago.
[j8v8n9p] (score 4, diepte 0) I’ve been wearing my Saucony Freedom 5 for my full time job that requires 8+ hours of mostly standing and really liking it. It has the right amount of firmness and stable base while static but still having some of that step in squish comfort and shock absorption of Pwrrun + insole/Pwrrun PB midsole. Upper is quite breathable too and heel hold is solid. It has limitations when used for actual running but I’ve really been liking it for using it for work/walking/working out etc.
[j8v0ktk] (score 3, diepte 1) My wife just got the NB More V4 for work / she is a PT and is on her feet all day. She absolutely loves them.
[j8v19lp] (score 3, diepte 2) plushines, no. plushiness, sure.
[j8ustne] (score 3, diepte 1 OP) I'd say that I am having the durability issue, but it's a sacrifice I'm willing to make if HOKAs are truly the best for my use-case.
[j8wz9de] (score 3, diepte 2) Anecdotally speaking, building up the leg strength for standing all day comes with time and practice. Personally I hate wearing Hokas around as a daily shoe because they feel awkward for anything not running, and the squishiness of the foam is really unstable and makes my foot hurt trying to do micro adjustments. (Source: running 2 hours a day and then working a day job at a standing desk)
[j8velzz] (score 3, diepte 0) I would stick with the Bondi if you found them enjoyable because the midsole foam hasn’t changed so they should still offer a feeling you enjoyed in the Bondi 6. If you wanted an incredibly similar option to compare to from another brand to make sure the Hoka feel is still for you, consider New Balance’s More V4 (similar stack height and drop as Bondi). As for preserving the heel structure, I find it to generally be related to excess friction eventually wearing down the lining of the shoe. The updated heel structure of the Bondi 8 uses less fluffy padding and allows for less heel movement, which should help minimize friction, but other things to consider that can be helpful include using a slightly compressive sweat wicking sock (avoid cotton as it tends to cause more friction than other more sweat wicking materials and compression minimizes sock movement that can lead to friction), pushing your heels against the back of the shoe when lacing up, possibly using the “runner’s loop” to secure the heel, and always fully lacing and unlacing the shoe when taking them off as opposed to kicking them off.
[j8vl7na] (score 3, diepte 0) While Hoka was the main option for comfort when Bondi 6 came out, their lack of innovation have let them down. Still using the similar foam while others have created better, more comfortable and lighter foam. Bondi 8 is also quite different than bondi 6. It’s become way more durable and stable (the durability on bondi 7 was horrible) but lost some of the comfort that it was known for. 

I have bondi 8 (and had 6 and 7). While 6 and 7 was too soft as a running shoe they were perfect as a work shoe (hard surface). Bondi 8 I use as a everyday shoe, but not a work shoe. Then I prefer Triumph.
[j8wob45] (score 3, diepte 0) Not a shoe comment, but have you tried compression hose? I worked in hospitals and my knee high compression hose made a massive difference with leg fatigue and overall tiredness.
[j8vo3p7] (score 2, diepte 1) I retired my Bondi 7 due to disintegrated heel padding.  Replaced with Nimbus 25, it feel stable and a bit more bounce when walking.  Pretty satisfied.
[j8v6ihm] (score 2, diepte 2) Got it! It could be worth trying some of the other options then for your next pair. Topo Phantoms are another option. Also, you may be able to wean yourself off of that level of cushion as you get used to being on your feet. You could even just try a less cushioned Hoka like the Clifton (Bondi is as thick as it gets).
[j8vq1df] (score 2, diepte 3) Agree with the phantom, they are not as high of a stack but they are extremely comfortable and stable for walking and standing.  I prefer a medium stack for walking and standing myself.
[j8ussx2] (score 2, diepte 0) I also stand all day and on concrete floors. I’ve been wearing Hokas for many years, but recently bought a pair of Oncloud Cloudmonsters. I’m really enjoying them and my feet are never sore at the end of the day. They are very cushy and have a great rolling motion when walking. I liked them so much I just bought a new pair for running.
[j8v9mxb] (score 2, diepte 0) Skechers is popular here. Goga mat is one of the plushest and softest cushions, and much cheaper.
[j8x20ce] (score 2, diepte 0) I’d say Birkenstock, preferably the Boston, clog, or any closed toe shoe
[j8zs5o9] (score 2, diepte 0) Check out the ON cloudmonster
[j8v2a0p] (score 1, diepte 2) You've got the right idea.
[jgtgvof] (score 1, diepte 3) I'm new to the shoe game and I have this issue, bout the micro adjustments on a surface too giving. What do you use for standing?
[j8ypjey] (score 1, diepte 2) You could have both. The Altra Torin or Olympus are super cushioned but don’t have a heel-toe offset.
[j8vpxwh] (score 1, diepte 1) I have the 3 and 4, 3 is significantly better, 4 is still good but the 3 had a softer bouncier feel and a more plush tongue and her collar.  5 looks more similar to the 4.  Both are Great for working out and walking.
[j8vazq6] (score 1, diepte 0) I wear the Clifton when I work, pretty comfy
[j9o0oxy] (score 1, diepte 1 OP) I can do my own research, but do you have any sock suggestions offhand? Or do you think whatever I find for "compression socks" on amazon should be fine?
[jcqvsqh] (score 1, diepte 2) Sorry for the delayed follow up. Feetures Elite Light Cushion are my go-to; they even offer a lifetime guarantee. OS1st and CEP also make good options. I would stick with well-established name brands such as the ones I mentioned as opposed to alternative options offered on Amazon.
[jmps0t1] (score 1, diepte 1) Which foam is better? Have you tried Gel Nimbus?
[jmqhojw] (score 1, diepte 2) Nimbus is comfortable. The foam is very soft. A bit too soft for me. Great as a walking shoe, but prefer a bit more responsiveness in the 
PRWrun + (Triumph).
[j8wflup] (score 1, diepte 0) Adidas Ultra Boost is a better looking shoe, good for standing. Just get a new pair of Hoka Bondi
[j8wo9lp] (score 1, diepte 0) I fell for the hype about Hoka's being great casual shoes and good for PF.  Bought a pair of Bondi's and now I regret it.  Too much arch support and way too narrow.  Had to trim my orthopedic insoles to get them to fit -- never had to do that for any other shoe.  
 Why, oh why didn't I just get another pair of Nimbus?
[j8x1f72] (score 1, diepte 0) I have a pair of Rincons and a pair of Rocket X, both great shoes and the Rincons are actually my favorite running shoes. But I don't like using them to walk or stand, I think que pronounced rocker isn't suitable for that and I like my toes on the ground while standing. Shoes like the Merrell Trail Glove are the type of shoes I prefer for that scenario: minimalist yet comfortable, 0 drop and a wide toe box. I also had a pair of nobulls that were surprisingly good for that. 

In any case, I know people that stand around in Cliftons all day and swear by it.
[j8z82ui] (score 1, diepte 0) https://www.hoka.com/en/us/mens-everyday-running-shoes/bondi-sr/192410928491.html?source=shoppingsite_PLA_1110520-BBLC-10.5&kpid=1110520-BBLC-10.5&utm_source=google&utm_medium=pla&gclid=Cj0KCQiA6LyfBhC3ARIsAG4gkF8Yjt3kOv14MmndovrjNqssLO85SDXCpzTCER5PAQ7ieYkWOs470LEaAlnPEALw_wcB&gclsrc=aw.ds

Bondi slip resistance

https://www.skechers.com/work-relaxed-fit-max-cushioning-elite-sr/108016.html

Sketchers slip resistance cheaper with max cushion
[jh8ibcn] (score 1, diepte 0) QQ Did you consider the Bondi SR? It is popular in the medical community due to its water resistance and slip resistance.
[j8vdcir] (score 0, diepte 0) They never were

=== THREAD w99v5d ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-07-27  SCORE: 7  REACTIES: 31
TITEL: So apparently my feet eat shoes … What to buy next?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ihu5mhi] (score 13, diepte 1) I think 650km is okay. No shoe is bomb proof so you'l probably have a similar result with other shoes
[ihudhes] (score 8, diepte 0) I’d say you should be changing up your shoes before that point anyway to be honest, cushioning will be bottoming out. I don’t think that’s a bad return for that mileage. But if you want value, I’d go with the triumph 19, think the rubber is a different compound. I’ve got about 150 miles on mine and literally not a mark on them. Nike infinity reacts are almost impossible to wear down as well
[ihunuzh] (score 8, diepte 0) First of all, 650 km is by no means bad return on a pair of running shoes. Secondly, such cracking has been known to affect beaded TPU-based foams like the PWRRUN+ found in the Triumphs. I had some cracking happen to my Ultraboost 20, though it was nowhere near as pronounced at as this.

What struck me, is that these are the Triumph 17, which have been released... over 2 years ago? I think the age of the foam was a definite contributor here. Foams deteriorate with time, irrespective of usage, which is why heavily stocking up on (discounted) shoes is not always a good idea. I am guessing that had you done those same 650 km on a fresher midsole that crack would not have happened/not to this extent at least.

Ultimately, we all wear out our shoes differently. For me, the most significant amount of wear is by far on the lateral side of the forefoot, followed by the medial side of the heel due to overpronation. You seem to have a much more neutral footstrike.

If the Triumph 17s worked for you, I would go with the Triumph 19 or 20, going by the mantra if it ain't really broke, don't fix it. You can always try something new of course. EVA-based midsoles might not crack, but they will lose their properties (i.e. start to feel dead) quite a bit quicker. It is impossible to predict what will give you the best durability. 650 km in an older pair of shoes seems good to me.
[ihu7qyv] (score 7, diepte 2) Triumph isn’t peba though
[ihu825y] (score 6, diepte 4) PWRRUN+ vs. PWRRUN pb, my guy. TPU and PEBA, respectively
[ihv8ogl] (score 6, diepte 2) Tell you what is a cracking “stable” neutral shoe, the ride 15. I have some of the same issues. Apparently the new speed 3 is a lot more stable as well
[ihu890m] (score 4, diepte 5) Thanks, my guy. I stand corrected.
[ihuocpo] (score 4, diepte 1) I have the Triumph 18 and 19 and they’re the best shoe for longevity of any other shoe I’ve had. I’ve had quite a fat share of shoes from NB, Nike, Hoka, and Saucony. I would get another pair of Triumph or the Endorphin Shift.
[ihuaark] (score 4, diepte 0) Although I don't personally like the styling. The adidas solar 4 haa a very good sole. Whether you go for the standard version or supported one(if you like more support at the ankle). Good traction, light and breathable, but sturdy and just enough support. Good laces as well.

I liked them, a lot, but ran through them quickly. (I'm bigger, 6'4" at 270).

Brooks adrenaline may also interest you, or sticking with Saucony. New triumphs maybe?
[ihtwein] (score 3, diepte 0 OP) These are my Triumph 17 with 650km on them. I’m 95 - 100kg and run about 5:00 - 5:30m/km. I got these Triumphs as I was told the midsole was bomb proof. I’ve never had a shoe split on me, so I’m curious whether I should get new Triumph 19 or move onto another brand? Any suggestions for a midsole to take on a heavy runner?

Edit: Just to be clear, Im not complaining, just a bit perplexed as I don’t even know how long I’ve been running like this  as I only happened to notice it when flexing the shoe. Otherwise the tread looks great.
[ihu0qwa] (score 3, diepte 1) It's a problem with this type of midsole, the ultraboost can also split in this way.
[ihusblh] (score 2, diepte 1) I am 160 pounds (72.5kg I think?) and my triumph 17 split the same way after 800km. I thinks that’s just the shoe does. I’ve got the 19s and feel like I will get the same distance out of them.
[ihv4ddu] (score 2, diepte 1 OP) Thanks for your suggestions! I completely agree, they were in semi retirement due to a pair of Endorphin Speeds, but I’m finding myself a bit too unstable on the Speeds so returned to the Triumphs, then discovered the cracking!
[ihvrsqr] (score 2, diepte 0) Brooks is a more durable shoe for heavier runners. Saucony SHIFTS last longer than triumph foam for heavier runners as well. I’d probably go shift 1s if you can find them on a deep dish discount
[ihu3uzo] (score 1, diepte 2 OP) Thanks! Is there a type of shoe I should look to getting instead of the triumph?
[ihu7xze] (score 1, diepte 3) Wot? Lol

I dead ass thought it was peba... My bad
[ihu8agp] (score 1, diepte 6) Cheers!
[ihwdoez] (score 1, diepte 1) This happened to my Triumph 17s as well - I was glad to see the outsole pattern was changed up on the 19 as I think it will better support the foam
[ihv45cm] (score 1, diepte 1 OP) Yeah I’m leaning towards new Triumphs. I’ve got a pair of Saucony Speeds but they’re strictly for speed work as I’m a bit unstable on them. I’ll keep the Triumphs for long distance.
[ihwsuvf] (score 1, diepte 2) Speed v3 is supposed to be pretty significantly wider (and more stable) FWIW.
[ihuotsq] (score 1, diepte 0) I used to only buy Adidas because the continental soles were unbreakable. They changed the shoes in the past few years (not to my liking) so I switched to something else, but they could an option for you if you like the feel.
[ihurvie] (score 1, diepte 0) That's pretty bad for only 650km. I have the Triumph 18, they are holding up really well for me so far.

Maybe try Adidas Solar Glide or Reebok Floatride Energy 3/4. Both I'd say are the most durable shoes I've owned.
[ihuxa69] (score 1, diepte 0) I had a tear in the exact same spot on my Triump 17s and they only had 100ish miles on them. I think it's a defect in that particular shoe rather than you being extra hard on shoes.

I contacted Saucony about it and sent them pics and they gave me an online credit for new shoes.
[ihv9oj1] (score 1, diepte 0) Go with something plated up front. The Skechers Persistence would be a great option.
[ihwm3sa] (score 1, diepte 0) I find the Reebok symmetros quite durable.
[ihy3tv5] (score 1, diepte 0) Saucony Endorphin Speed 2’s are great and so are Brooks Levitates!
[ihycng7] (score 1, diepte 0) That's not a bad longevity for someone your size.
[ii3ant5] (score 1, diepte 0) Hi. Just throwing my 2¢ in but Triumph 19 would be a great update for you. If you like the speed but are too wobbly, I got their new Tempus model and HOLY SMOKES. It’s one of their best shoes right now even though it’s new. Based off the speed but has an EVA wrap around the heel and under the arch for support.
[ii3dbad] (score 1, diepte 1 OP) Thanks for the help! I’ve ordered the Triumph 19 already as I think it’ll be good for my runners knee that’s developed recently (blaming a bit of weight gain and the speed wobble!) so I’m going to plod along in the triumph while getting back to it. With regards to the Tempus - I’m honestly definitely tempted. The speed was insanely quick for me improved my 5km sprint by 15s/km, but I just seem to be injuring myself using it. So I’m going to keep it in mind for future.
[ihu5bm1] (score 0, diepte 1) If you enjoy that peba midsole, try adidas or puma. Have you considered the tempus? I've heard it's good as a guidance shoe and has incorporated their higher tier foam. My assumption is that heavier guys would do well with a guidance shoe... Again, assumption lol.
[ihv3w7k] (score -1, diepte 0) ![gif](giphy|Phzg1XZgJTeZG)

=== THREAD 10bsih6 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-01-14  SCORE: 5  REACTIES: 31
TITEL: Should I try out Dr Scholl's insoles to get rid of my foot pain while running?
POST (source_id=post):
So I'm not exactly in the position where I can just buy a new shoe but whenever I run the bottom of my feet always start to hurt right around the middle. 

My first pair of running shoes was the Nike Pegasus 38 and the pain was horrible in that so I switched to the Hoka Mach 4's and while the pain happens less frequently it still hasn't gone yet. 

My local Walmart has a Dr Scholl's kiosk where if you stand on this mat it will measure the dimensions of your foot and where most of the pressure is and based on that it'll give you recommendations for insoles.

Is it worth a shot?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j4bzeva] (score 8, diepte 0) Insoles are okay until you build up your foot strength. You should look into foot and ankle strengthening exercises.
[j4c1z12] (score 8, diepte 0) I agree with strengthening the foot, as well as stretching. I'm an avid runner who experienced plantar fasciitis from running hard downhills on pavement last year. I've since made it a daily routine to stretch my feet, calves and ankles to ensure the muscles are relaxed and ready for my next run. If the arch is tight, every step will cause the muscles to stretch and lengthen which in turn creates pain. All the insert will do is pad the bottom of your foot and work as a crutch, never allowing the muscle to fully extend as it should.
[j4c9c60] (score 6, diepte 0) For the same money or a bit more try a pair of Superfeet.  Superfeet are amazing.  (try all on because they all feel different). Def do strengthening like all suggest
[j4d2qn0] (score 5, diepte 2) Dynamic warmups are really good for pre run to activate muscles used during running.
[j4cpfti] (score 4, diepte 1) I hear a lot of different opinions when it comes to stretching and running. Some people say stretching before running is bad and can cause potential injuries. Others say stretching before running is helpful. I myself stretch my legs/ ankles/ feet before running and I think it does help prevent certain pains, and mainly stiffness in my joints and muscles. Not sure what the best approach is.
[j4d2elx] (score 4, diepte 2) Roll before, stretch after. Muscle is like dough. If you stretch it cold, it breaks. My foot foller is in constant use.
[j4cnwng] (score 3, diepte 2) It could be plantar fasciitis, or some other muscle/tendon/bone issue that is causing your pain, not necessarily related to the shoes you're wearing. I would recommend getting evaluated by a physical therapist if possible.
[j4df52t] (score 3, diepte 2) I don’t know anything about stretching and injuries, but in general, not stretching increases the stiffness of your tendons which can help force and power. Some athletes try to capitalize on that.
[j4bvvyy] (score 2, diepte 0) I definitely replace the stock liners an d add cushion shoe liners to my hokas, they barely last 6 months otherwise. Way too expensive to buy those shoes twice a year. I have bone spurs in my knees, RA, and wear corrective orthotics for pronation. A couple years ago I sprained my ankle, fractured my tibia and seriously sprained the outer ligaments in my foot, which never seem to  recover, so cushion is a top priority for me. Definitely worth a try.
[j4bx0lk] (score 2, diepte 0) I think they're probably unlikely to help.

Where exactly are you feeling the pain in your feet? And does it only happen while running, or do you experience pain walking also?
[j4d8mxq] (score 2, diepte 3) I like to use an exercise band wrapped around the top of my foot. While sitting on the ground, I'll pull the band to create resistance and flex my foot in different directions to stretch the ankle. Hope that helps!
[j4dv1lj] (score 2, diepte 6) Okay thank you
[j4bu0wb] (score 1, diepte 0) I would give Currex insoles a shot or Z Liner insoles. Both are different and currex you need to know if you have a low medium or high arch pretty each to do just by seeing the imprint of your foot when it’s wet. Z liner has less structural support but they make my endorphin speed 2s wearable for me otherwise my foot will roll inward too much. Both are on Amazon or their respective websites
[j4cn1kt] (score 1, diepte 1 OP) I'm feeling the pain at the bottom of my feet in the middle. It only happens when I'm running.
[j4cnq8i] (score 1, diepte 1 OP) Would running with the insoles eliminate or at least reduce the pain though? 

Does it make sense to buy the insoles and do the foot strengthening exercises at the same time? 

Because right now I can barely run more than a mole because of the foot pain and I want to do more runs so that I can get in better shape for track season
[j4d7xui] (score 1, diepte 2) You can certainly give the inserts a try, you may find relief right away.  I just found in my past experience that stretching and strengthening ultimately helped "correct" the issue.
[j4d6xd2] (score 1, diepte 2) How do you stretch your ankles?
[j4d8ttc] (score 1, diepte 4) That does thank you
[j4dj45o] (score 1, diepte 3) Start doing squats.
[j4dk9fb] (score 1, diepte 4) I’m doing kettle bell squats.  I can’t do barbell squats due the flexibility issues.  I just hurt myself trying
[j4do0l6] (score 1, diepte 5) Rear leg elevated single leg squat is the way. The more you forcefully load your ankle with heavy resistance, the more mobility you will gain at the joint.
[j4dgpyo] (score 1, diepte 3) Yeah I remember I read something like that as well. Seems like  there are certain circumstances where stretching is recommended vs not stretching
[j5bj6h0] (score 1, diepte 1 OP) Do you have any reccomendations on how I should go about strengthening my foot?
[j4c6h04] (score 1, diepte 0) Honestly i just buy the generic Dr.Scholl insoles you find at walmart/riteaid and they work fine for me.

If you are having foot pains not sure any insole will help you.
[j4dt0ea] (score 1, diepte 1) Spend the extra money for Superfeet. I have it in all my shoes and you will feel an immediate improvement (walking or running).
[j4cwl2o] (score 1, diepte 0) If they remove the pain its a no brainer. Pain and potential injuries are not worth taking the risk for
[j4d2krf] (score 1, diepte 0) I would consider going to a podiatrist or physical therapist who is a runner or specialized in foot issue, so you can diagnose the root cause of your issue before spending unnecessary money.
[j4dix3r] (score 1, diepte 0) You'll know after you try. Personally Dr. Scholl insole helped me with PTTD. I strengthen my feet, stretch, relax but sometime your still get hurt. 

So far my exp with Scholl insole has been positive.
[j4e4axm] (score 1, diepte 0) Those are the lowest of the low in terms of insoles. Most of them barely have much support, if you can even find the more supportive ones at Walmart. I have flat feet where Ive had metatersal fusions and Ive had better luck with toe spreaders and more minimal support. The main issue is finding shoes wide enough. Ive used many insoles, even custom and none really helped much at all.
[j4fb89c] (score 1, diepte 0) ProFoot Miracle insoles. Best I've found. https://profoot.co/category/product-type/inserts-insoles/

If your experience is like mine, you'll need them for only a year before your feet strengthen and toughen and you may be able to get by with the shoe maker's original insoles.

I've had foot problems since I was a kid -- very narrow, bony feet, no meat on my soles to cushion for barefoot walking, high arches. Since I was a kid I've needed custom orthotics or custom fitted shoes, or makeshift stuff I put together trimming Dr Scholl's, moleskin, etc.

But the ProFoot Miracles are better and much lighter in weight. Cost less than $10 at Walgreens and other stores, or Amazon.

These aren't normal foam, gel or memory foam. The material molds to your foot and takes a set after some wearing. They're good for 6-12 months or longer depending on your weight, shoe type (longer life with flexible foot beds, shorter with hard foot beds such as cowboy boots), and activity. Usually when the insoles flatten too much on my hard foot bed leather boots, I move them to my snug-fitting clipless cycling shoes, or trim the toe-ends off to avoid crowding the toe box, and stack them in my 50 year old Herman Survivor winter boots for extra insulation.

I need them for my clipless cycling shoes, which have hard, rigid footbeds. The original insoles were thin and hard and I ended up with metatarsal hot spots on longer, hard pedaling rides. The ProFoot Miracles worked better than anything else I tried. 

When I resumed running in early 2020 I hadn't run at all in more than 30 years, only doing walks up to three miles occasionally. During running my arches were on fire, metatarsals felt bruised. The ProFoot Miracles fixed that. In some cases I stacked the ProFoot insoles on top of the original insoles (Adidas, Under Armour, whatever).

After a year of running my feet were strong enough to switch back to the original insoles for most of my running shoes: Adidas Solar Boost, Under Armour Hovr Sonics, Nike Pegasus 39, Endorphin Speed and Pro, Atreyu base model. I still prefer the ProFoot Miracles for the Adidas SL20, because the original insoles are too thin and I dislike the Lightstrike midsole -- feels like mushy cork, hard landing, no rebound.
[j4hg6bj] (score 1, diepte 0) About 4-5 years ago I ended up with the worst case of plantar fasciitis in both feet, although it was so much worse in one.  I’ve been a runner for years and this arch heel pain was the result of “saving” money by buying and wearing cheap ballet flats to a job where I’m on my feet all day from target.  I’ve always worn decent running shoes.  I was already using Superfeet insoles but in desperation I tried that exact Dr. Scholl’s kiosk you mentioned in a Bed Bath and Beyond store.  I spent 50.00 and wore them on top of my Superfeet insoles and the pain went away- it was the only way I could walk.  I did tons of deep calf stretches and foot strengthening exercises and after a few weeks it healed enough that I could just wear the Superfeet insoles.  Now, I don’t even need insoles, just good shoes with arch support.  I would say yes, you should give them a try in addition to stretching and foot strengthening exercises.  Replace your running sneakers after 300 miles or so.  Shop around for good deals, they’re out there on previous year’s models!

=== THREAD wo64b4 ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-08-14  SCORE: 3  REACTIES: 31
TITEL: Need wide toe box, max cushioning.
POST (source_id=post):
Hey everyone! Looking for some advice on something new to try. Currently training for my first marathon. I run in Kinvaras on my tread for short runs, Hoka Cliftons for long (and short) runs outside. 

The Hokas are giving me nasty callouses/blisters on the side of my big toes so I think I need something with a wider toe box. 

I also have high arches and struggle with plantar fasciitis on my left foot. It’s starting to flare a bit now that I’m adding volume. 

I tried Altra Torins on in the store and found them to be really comfortable, but I worry about zero drop on long runs and with the volume I have currently. 

Considering Topos too but I don’t have a store nearby to try those. 

Any thoughts on a great shoe for me?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ik9cy0l] (score 9, diepte 0) NB More v3
[ik9dsm2] (score 6, diepte 0) NB 1080. I have wide toe spread but not wide feet. They are my #1. ETA: I also have PF and high arches
[ik99kh1] (score 3, diepte 0) If the torins felt good I highly recommend getting used to them and getting a pair. Amazing shoe.
[ikagl8y] (score 3, diepte 1) This is a good recommendation. 1080’s mesh in the forefoot is forgiving while not impeding a good lockdown. I have wide toes, high arches and a low-volume mid foot and the 1080 works perfectly for me. Size down half a size from what you wear in your Cliftons if you go with the v12s, TTS with v10 or 11
[ikarstk] (score 3, diepte 0) If you want a wide toebox, go with New Balance. The Fresh Foam More v2, v3 or the 1080v12 have wide toeboxes, and are decent for a high arch/midfoot. They also have good cushioning. NB has a few running shoes in 6E too, the 1340 and 1540 but they are stability shoes.
[ik925tm] (score 2, diepte 0) Are you looking for a true wide, or a regular width that feels on the wider side?
[ik9j353] (score 2, diepte 1) Agree. Loved the torin 5, even with the tongue that cut  my ankles before I modified it.  Just ease into them. I went from Hoka to Torins last year for my marathon training. They served me well. Recently retired them at 500 miles.
[ikblv4p] (score 2, diepte 0) The only shoes with truly wide toe boxes (vs just "a generally wide shoe-shaped shoe") would be Altra or Topo Athletics.
[ik989fm] (score 1, diepte 1 OP) I don’t think my feet are wide overall, really I think I just need a roomier toe box.
[ik94w4p] (score 1, diepte 0) We have similar shaped feet. Try on the Saucony Tempus. It’s my new long run shoe and I love it. Nice wide toe box but I’m still able to lock it down. My run was 8 miles. I did a slow 6 mile run yesterday with the last mile at race pace. It roles nice, great cushion, and light. I don’t notice the stability elements at all. This is the shoe I’ve been looking for.
[ik98ezh] (score 1, diepte 1 OP) I often get pain with stability shoes, so the fact you didn’t notice is interesting!
[ik98kvu] (score 1, diepte 1 OP) I would worry about it being too loose. My foots itself isn’t wide, just seems to be the big toe and how I land.
[ika1r0e] (score 1, diepte 2) I hear ya. My right is wider than my left, so I went a half size up and wore thicker socks, which helped a little. My Cliftons wore out at about 250 miles, and were giving me blisters toward the end. Given their lifespan and price point, I went with with invincibles because they are similarly priced (when on sale), a bit wider and the upper has some stretch.
[ik98glx] (score 1, diepte 1 OP) I’ve actually never tried an ASICS.
[ika1d88] (score 1, diepte 2) I also need a wide toebox now per my podiatrist. While the Gliderides aren’t really super-wide they are pretty comfortable for me. I will say while I don’t use them as much, my Kinvara’s have the most generous toebox. 

runrepeat.com lets you filter shoes by toebox size and other parameters. I don’t know how totally solid that dataset is, but it’s worth it for ideas I guess.
[ikazzx8] (score 1, diepte 2) Also consider the Nimbus 23, or the 24 a 1/2 size up from what you normally wear. The toe box is very roomy, but seems shorter lengthwise.
[ikbl63m] (score 1, diepte 3) Wow I had the opposite experience with the nimbus 24. I felt the nimbus toe box to be super tight for my regular size. I tried sizing up but then got some heel slip.  Fwiw the cumulus 23 I had no problems and fine room in the toe box but the nimbus was too tight.
[ikc8ol3] (score 1, diepte 4) I seem to have small toes compared to most people, judging by feedback everywhere, even though I don't have a narrow food, just a slightly narrow heel. It may have something to do with having a low instep. My arch is high, but with a low instep, I suppose that would result in an overall "low volume" foot. \*guessing
[ik9alxg] (score 1, diepte 0) NB Supercomp Trainers come in a wide width. They are as cushioned as it gets so if you could find a store that carries both the normal and the wide you could find out if they have enough room.
[imxoohq] (score 1, diepte 1) Is this the best in the market now for Nb?
[imxq70f] (score 1, diepte 2) For recovery runs, yes. It has a wide platform/toebox and is very soft. After breaking it in, I actually find it too soft for me (weight 200lbs/90kg).
[imxr81r] (score 1, diepte 3) I see, what about daily trainers ? Is 1080v12 a better choice in this case ?
[ik9jkz1] (score 1, diepte 0) If you like the feel of the Cliftons other than the fit on your toes, try the New Balance FreshFoam More v3.  It has similar cushioning, but is roomier overall.

If the Kinvaras fit well and you want something that feels somewhat in between the Clifton and the Kinvara — cushioned, yet light and responsive — the Saucony Endorphin Speed 2 would be a good choice.
[ikb31s6] (score 1, diepte 0) I would personally go for the Altra Torins, particularly if the tongue was not an issue when trying them out. Since you can already run in 4 mm drop shoes (Kinvaras), transitioning to the 0 mm drop Torins should not be too difficult. I am guessing you will find the Torins easier to run in, since they have a lot more cushion than the Kinvaras/are more forgiving. The only worry I would have is regarding the tongue in the Torins. For me, it was not a problem, but many people had a different experience.
[ikbz4xr] (score 1, diepte 1 OP) The tongue was the reason I didn’t get the Torin 5, I was super bummed cuz the rest of it felt great! I’ve heard they’ve fixed it on the 6, but haven’t tried them yet.
[ikcu8c5] (score 1, diepte 2) Reports/costumer reviews I have seen suggest the tongue is still an issue in the Torin 6, though not as big as it was in the Torin 5. It's a tough one to be honest.

If possible, I would buy them from a store with a good return policy, do a gentle long run on a treadmill and see if the tongue is an issue, and if it is, return them. But that is a hassle I fully understand you would want to avoid.

I bought my pair of Torin 5 from a running store, after running in them for a few minutes on the in-store treadmill. Was constantly checking if the tongue was bothering me, it wasn't so I eventually bought them (full price). Later I found that they were a tad small (my left foot occasionally touches the front of the shoe, probably was too focused on the tongue to notice this). But the tongue has not bothered me since.

BTW, odd sizing is why you probably want to try them on before purchasing them. On paper I should have a thumb-width from toes to front of the shoes (as I do in all my other shoes in the same size). In practice, this is not the case.
[ikbanjv] (score 1, diepte 0) I had the same issue with Hoka Clifton 8. Very bizarre and disappointing as I really liked how they felt when I started using them.

Have you been to your local running store? If not,  let them know what’s happening and they can make a recommendation based on what you need.
[ikbz9aa] (score 1, diepte 1 OP) Yeah, that’s why I’m leaning towards one of those… just figured I’d ask in case there’s something I don’t know about!
[ikbzi17] (score 1, diepte 0 OP) Thank you everyone for your thoughts! I think I may order both and try them on the tread for a few miles and see how they go.
[ikvxd4s] (score 1, diepte 0) I had to double check the username because this is exactly what I would write.

I just returned my cliftons and am currently running in the NB 1080v12. I've only done a few runs so far so I can't give feedback, but this is what the shoe store recommended to me.
[ik94ww5] (score 0, diepte 0) Try the wide Cliftons?

