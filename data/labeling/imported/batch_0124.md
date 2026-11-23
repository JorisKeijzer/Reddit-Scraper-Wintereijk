# Label-batch batch_0124

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
Schrijf het resultaat naar `batch_0124.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 31hzb9, zp5xfd, 1ni59ak).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 31hzb9 ===
SUBREDDIT: r/xxfitness
DATUM: 2015-04-05  SCORE: 228  REACTIES: 69
TITEL: Hitting Squat Depth and Keeping Your Heels Planted
POST (source_id=post):
Hi all,

Both here and in the XXFitness Facebook group, we get a lot of posts about ladies being unable to hit depth on squats, or not being able to squat without their heels coming up off the ground. These two things are actually more or less one thing: ankle/calf mobility problems. They are usually not hamstring problems: I have possibly the shortest hamstrings in the world (along with the rest of my family) and can easily and happily sit at the bottom of a toddler squat with good posture. 

**CAUSES:**

1. Sitting a lot: Sitting in a chair usually involves hours of us relaxing with bad posture in a position that is not even equivalent to parallel depth. This creates a position that feels natural/normal, so going deeper feels weird and unnatural and our body is completely conditioned to not going that deep any more.
2. High Heels: High heels shorten the calf muscles. Nuff said.
3. Bad form: You've gotten away with quarter- or half-squats your whole life, or you've only done squats in a situation like BodyPump where nobody goes to depth at all. You've therefore created a muscle memory for squats that doesn't jive with going all the way to depth and has probably built in some bad habits.

**EFFECTS:**

1. An inability to 'sit back' into a squat and maintain an upright posture, instead bending forward/over as you descend.
2. Heels raising off the ground as you go deeper
3. 'Hitting the wall' on depth

**STRATEGIES:**

1. [Calf stretch against a wall](http://i.ytimg.com/vi/f1HzSAuB-Vw/maxresdefault.jpg): Runners will be familiar with this one.
2. [Foam roll your calves](http://www.mindinmotionkc.com/wp-content/uploads/2014/03/foam-rolling-calf-muscle.jpg): Either with both legs or one leg as pictured. Roll the calves out before squatting by rolling back and forth. Once you've done that a few times, roll again but this time stop every time you feel tightness/pain, stop and take 5-10 deep breaths while trying to relax that area around the roller, then continue and repeat as necessary.
3. Toddler/Third-World Squats Daily - YES SERIOUSLY DAILY. [This is what it looks like](https://fitisafeministissue.files.wordpress.com/2013/05/cfc9e-toddler-squat1.jpg) (though please ignore the 'no knees over toes' suggestion: now proven to be a myth): Squatting to absolute depth without collapsing your spine. But if you're seriously having that much of a depth/heel-raising problem then you'll probably need to spend at least the first few weeks holding onto a chair, pole or table [like this](http://i.ytimg.com/vi/dc3V3f45nOI/maxresdefault.jpg). Don't freak out if you can't get all the way down at all, even while holding on. Just go as low as you can with your heels down for 10-20 deep breaths and try to go a little lower on each exhale. These must be done daily, if not multiple times a day. You can do them anywhere: watching TV, feeding the cat, listening to music, waiting for the train, etc. 
4. A fun tip I've found helpful: Either raise your toes while squatting or curl them under. This takes them out of the equation and makes it a lot harder to rely on them to take the weight. 
5. [Box squats](http://organicfitness.com/wp-content/uploads/2014/07/eirik-garnas-organic-fitness-box-squat.jpg): Until you can hit depth, learn to 'sit back' into a squat by putting a box at parallel or just below parallel behind you. Descend with heels planted until you feel the box touch your butt, then shoot straight back up. Do not sit *down*, sit *back*: Focus on pulling your butt back onto the box (as though someone were pulling your hips back [like this](http://jasonferruggia.com/wp-content/uploads/2011/08/box-squat.jpg) rather than just descending. Keep the tension in your core throughout the movement, do not collapse or relax once on the box.
6. If your problem is on the ascent: Rather than thinking 'heels down', some people respond better to metaphorical cues such as "Push the earth away from you" or "Separate the ground beneath you with your feet". These cues help with both keeping the knees out and pushing through your heels on the ascent.
7. **If in doubt, try taking your feet a bit wider and/or turning your toes out more.** Those with long levers (particularly long femurs) often need to take a stance in between a traditional squat and a sumo squat. Some trainers get weirdly prescriptive with foot distance and angle, but the reality is that whatever feels most comfortable for you is probably the right way to go. 
8. **Lighten the load**: If you can hit depth with a bodyweight squat, you should be able to hit depth with all your squats. If you can't, the weight might simply be too heavy for you. Start with a lighter barbell or try [goblet squats with a kettlebell or dumbbell](http://1y2u3hx8yml32svgcf0087imj.wpengine.netdna-cdn.com/wp-content/uploads/2014/03/myfitnesspal-goblet-squat.jpg)

**Got more tips or information on causes/effects/solutions? Add them in the comments and I'll edit them in so we can use this post in the FAQ**

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cq1u6oz] (score 21, diepte 0) Hold up--I don't need to worry so much about my knees going over my toes a little? I have VERY long femurs and can only get down to depth by allowing them to track forward a bit, or I fall on my ass. But my coach always yells at me, so I try and rearrange myself to fold up in a convenient way but it just isn't happening for me.
[cq1tk93] (score 16, diepte 0) Thanks for this, this is my problem so these will really help! And thank you for putting links in picture form, not videos! :D
[cq1vk6x] (score 15, diepte 1 OP) Myth. One of many articles: www.biomechfit.com/2012/02/09/3-squatting-myths-that-refuse-to-die
[cq1w0tk] (score 11, diepte 0) [Supple](http://imgur.com/QyVGH4h) Leopard, reporting in! Ever since I injured my glute med on Smolov, I hang out in this position in warm up squat sets and when stretching at night. To get started, I often use the squat rack, but even now prefer holding on to it because I can really pull deep into it with my back and hips. I swear I've never seen anyone do it at my gym, but after a few suggestions to people, I see all kinds of people doing it. Single best exercise for mobility ever!
[cq22j5w] (score 9, diepte 1) Your coach is an ass.

Yes, in a perfect world, where everyone respected each other and good healthcare was available to all people and the tax code could be printed in a single large binder and everyone had the same proportions, it's true that your knees would not stick out past your toes until you were very, very deep in the squat, but we just don't live in that world!

For *some* people, for example those with long femurs, it's okay for their knees to stick out past the toes if everything else is copacetic.
[cq1vp3x] (score 7, diepte 1) As long as your knees are in the same *direction* as your toes, you're good.
[cq1w9ee] (score 7, diepte 0) i was doing quarter squats until i watched this video from alan thrall 
https://www.youtube.com/watch?v=zvGr7wXQfwE

I have been using this methods for about 2 weeks every other day and am almost at the point where i can properly perform a highbar squat again. I have a good 70+ pounds i am trying to lose and did not believe I would be able to squat with my gut meat in the way XD  but using this video drastically improved my mobility
[cq1tl6u] (score 5, diepte 1 OP) Yeah I'm personally not a big fan of videos unless I seek them out myself - I like to see at a glance what I'm trying to achieve!
[cq1we3m] (score 5, diepte 2) This changes EVERYTHING!
[cq1u7z2] (score 5, diepte 0) Thanks for posting, I have massively been struggling with this. When ever I toddler squat my heels spring up like I'm wearing wedges. I'll try these to see if I'm not just doomed by ridiculously inflexible ankles :) thanks for the advice!
[cvfgldu] (score 5, diepte 1) You posted this five months ago and I'm crying right now thank you
[cq26ef5] (score 5, diepte 0) Everyone's body is a bit different.  For some people,  no matter how much stretching you do,  squatting to depth will be nearly impossible with a narrow stance. The way the bones fit into the sockets will affect how you can squat. 

What worked for me was widening my stance and turning my feet out a bit more.  I played around with it until I figured out what worked. As long as your knees track with your toes ( without going beyond your toes ) you're OK. 

There was an article on it.  I'll see if I can find it.

Also,  BOX SQUATS, yes!
[cq1spfe] (score 4, diepte 0) Thanks for this! I'll be trying out your suggestions in the morning.
[cq244bx] (score 4, diepte 2) Wow...TIL, thank you
[cq22g0y] (score 4, diepte 4) This is amazing. I am so happy to hear this. All this time I thought I was a bad squatter.
[cq22z1t] (score 4, diepte 1) Everyone has vastly different anatomy. Thigh length, the shape of your hips, trunk length, calf flexibility, etc. Hitting parallel is really the most important part. You don't need to go ATG with weighed squats because that means you're relaxing your glutes and hamstrings to get there and are actually sacrificing potential strength. If you need to get deeper and you feel anatomically unable to, go with a wider stance. Don't beat yourself up about it either because that's just the way your body is.
[cq1tle8] (score 3, diepte 1 OP) Awesome! As with most things related to fitness - consistency and patience are the key ingredients :)
[cq1tjx9] (score 3, diepte 1 OP) Does it feel unstable? If not then I wouldn't worry too much about it. However if you're about to tip backwards then you probably need to work on keeping your weight over your centre, perhaps film yourself and have a look at whether your  knees are tracking forwards enough, since I imagine trying to keep the weight back would contribute to the feet rising. As usual though, the best thing to do would be to film a short form check for us so we can see what's happening.
[cq1wdxp] (score 3, diepte 2) He is an older gentleman with a degree in buiomechanics, and a one time powerlifter. But I had to stop working with him for financial reasons, so have been on my own for a while
[cq1x7dg] (score 3, diepte 3) The reason I ask is "don't let your knees go over your toes" is a load of hooey that keeps getting repeated.  As long as your knees follow the same path as your toes (i.e., your knees track over your big toe) their position fore or aft is determined by your center of gravity and bar path.  If you are putting your weight over your midfoot - which takes weight off your toes and puts it on your heels - the actual bar position will determine where your knees end up.  If you are using a lower bar position it will require your knees to travel forward to maintain balance.  If you are doing a high bar or front squat, your knees will be further back.
[cq2o5lz] (score 3, diepte 3) Probably Sweden.
[cq2jck8] (score 3, diepte 2 OP) Forgot this simple thing. Will add it in once I'm back at a computer!
[cq1xmk6] (score 3, diepte 0) This was great. 

I have a tear in my meniscus and have dislocated my patella twice. The second time while doing PT, after a few weeks, they asked me if there was anything I wanted to do that I still felt unable to do. I told them a third world squat. They didn't know what that was so I had to show them.
[cq21s0v] (score 3, diepte 0) One of the things that really helped me was something like a box squat where I adjust a bench low enough so that my hips are just lower than my knees. I sit in the bench with a bar or PVC on my back in the approximate position. I start to lean forward until the weight goes onto my feet, tighten my abs, and stand up.  I do the opposite of that motion to go back down.  I feel like it let's my body learn the position it should be in without having to concentrate on balance and all those other things.  It really is learning the squat in reverse.
[cq29i65] (score 3, diepte 2) This is very true; some people physically cannot go far below parallel without sitting into their ligaments (like me), which can lead to bad form and/or injury. The best way to find out is through trial and error and seeing a qualified physical therapist that specializes in strength training to get alternatives/exercises to optimize your personal anatomy.
[cq2cbgc] (score 3, diepte 1) My ankles simply don't dorsiflex far enough to third-world squat with heels down and the weight over my feet, even after 5 years of doing that pose twice a week in yoga class. It took me years to train myself into flexing my ankles enough to put my heels down when walking (I never did as a little kid, at all), so going beyond a 90 degree bend is pretty much impossible.
[cq1w50d] (score 2, diepte 1) > But my coach always yells at me

Is this an actual coach, or a personal trainer who thinks he/she knows what they are doing?
[cq2lwet] (score 2, diepte 2) i'm there's at least one european country that fits this description.
[cq1vkr5] (score 2, diepte 1 OP) Hold onto something and accept that you will sometimes fall backwards onto your bottom ;)
[cq1ytfx] (score 2, diepte 1) Curious, how is that going?
[cq26p98] (score 2, diepte 1) girl, I've dislocated my knee caps like at least 5 times each! Not in like 10 yrs, thank God. It sucks.
[cq2j6qf] (score 2, diepte 3) I am definitely more careful! The burden of knowledge. Mine do have some residual soreness. I'm not sure exactly why. 

I did not have surgery and unless I tear a ligament, I have no plans to. I have weak ligaments and connective tissue issues, which is why mine go out but luckily nothing has torn yet. It started when I was a kid, when your joints are more mobile, so the thinking was that I would just grow out of it. my other joint issues I haven't grown out of. Mostly mine d/l due to trauma and I haven't hit them on anything or come down wrong! ugh, just thinking about it is giving me nervous sweats. I can pop mine back in, so at least that saves me a trip to the ER. I know mine are a little more lateral in that they don't really fit into the groove your femur/tibia makes which doesn't help!
[cq1y5g8] (score 2, diepte 0) What do I do about seriously uneven ankle mobility? My right heel always lifts off the ground way earlier than my left one.
[cq227n7] (score 2, diepte 0) I don't know what your qualifications are or if you're even the right person to ask, but is possible for some people not not be able to ATG third world squat? In my yoga class, there are a lot of people who can't, and even the teacher has to tip toe to balance. Maybe due to excessively long femurs, but her flexibility doesn't seem to be the issue. Just the tipping, point, I guess
[cq2ajyy] (score 2, diepte 0) Can we talk about feet width for squats? I can always get down to the bottom with flat heels if my feet are spread far enough apart. How far is too far? I'm going to keep working on those strategies, too.
[cq4lj6t] (score 2, diepte 3 OP) Not really. I mean you can start getting into sumo territory, but as long as it feels and looks like a squat and you're safely hitting parallel or below with heels planted and weight over your centre, I as a trainer wouldnt care how wide your feet are. Some are weirdly prescriptive about it but I say go with whatever works and keeps you safe!
[cq1t16b] (score 1, diepte 0) What if your toes/front of your feet always come up?
[cq24598] (score 1, diepte 2) Huh, I will attempt to do so! Thanks for the advice.
[cq245x6] (score 1, diepte 2) Oh, and it does feel unstable. :/ but I will try to film myself somehow!
[cq1thdb] (score 1, diepte 0) Thanks for this! I have some mobility issues and will definitely be trying these tips to see if it helps.
[cq1u4q9] (score 1, diepte 0) Working with my physiotherapist we are also doing squats with one of those giant exercise balls against the wall, once form is right adding increasingly heavy dumbbells. Granted we are also working on shoulder mobility an I need another inch or two to be able to hold the bar comfortably.
[cq2ls5d] (score 1, diepte 2) > www.biomechfit.com/2012/02/09/3-squatting-myths-that-refuse-to-die

not only that, but this video is very informative: http://www.biomechfit.com/2011/12/06/hip-drive-in-the-squat

now i have something to show people for the difference between a low and high bar squat.
[cut0534] (score 1, diepte 1) Here's a good video explaining the issue clearly: https://www.youtube.com/watch?v=iBHc323QwFE
[cq26g6b] (score 1, diepte 1) Try a wider stance and turning your feet out a bit more.
[cq3eco7] (score 1, diepte 1) so do you just do a couple reps, and sit there for like 30 secs? I need to start doing these
[ctjy2jm] (score 1, diepte 1) Sorry I'm new, in the picture is that an okay position to squat into? if that makes sense? I sit like that all the time so that could be helpful
[ctm2elr] (score 1, diepte 2) Squat into with weight? If you are doing low bar squats, you wouldn't squat that deep, only to parallel. But squatting in that position body weight and holding it helps those of us with bad mobility. I hope I interpreted your question correctly?
[ctngfko] (score 1, diepte 3) No sorry, I mean like I'm brand new. Im just getting started. I squat while holding a 20lbs thing of cat litter. I know thats really funny but it helps haha
[cq24bsm] (score 1, diepte 2) I can fully do a third world squat but sometimes can't stay down in the position for too long. I'm getting back into exercising, Crossfit, and I often wear some kind of compression and support if we are doing anything like squats, dead-lifts etc. It ache sometimes and i just baby it a bit. Since I went 2.5 years between dislocations the doctor didn't see surgery as necessary. It has been 2 years now since the last dislocation.
[cq2imfg] (score 1, diepte 2) It DOES suck! The second time I was a single mom (to an almost 4 year old) and they were like, stay off your feet, don't lift anything. All I could do was offer a sarcastic stare. Sure, that's easy. 

PT the second time for me was faster and easier, but I also feel less "sound" in my knee. It aches more, it worries me more and I hesitate when I don't think I have to.  Mental issues I suppose. 

Have you had surgery? Have they suggested it? Because I have gone so long between dislocations and respond well to PT, they have put off surgery. Which is good is some ways, a lot of ways, but sometimes I wonder if a quick surgery could make way for lots of years with few issues. 

10 years!! Awesome. Any hints as to how you have managed that long? I know I need to lose a few pounds which always takes pressure off the knee. Apparently I have a "J" curve to my patella? It has been a few years to my terminology might not be correct but I remember the J part very specifically.
[cq1y1h6] (score 1, diepte 0) Awesome post, thanks! I'm just getting in to lifting and am arranging a few sessions with a coach to work on my posture, in particular for squats. My heels come up for sure. A couple of questions (for you or anyone that has input):

1) Did you ever have the heel raise? If so, with consistent, daily work, how long did it take you to get your heels to the ground in proper form?
2) Have you ever worn lift shoes or used a block as part of the transition? Thoughts on doing that?
[cq26hyj] (score 1, diepte 1) I had three heel raise.  I widened my stance and turned my toes out more.  Problem fixed! Never work lift shoes.
[cq23jtn] (score 1, diepte 2) I'm wondering if there are actual leverages that make it impossible to go ATG
[cq26jkn] (score 1, diepte 3) I don't think so.  As mentioned,  widening your stance and turning your toes out more will fix the lack of flexibility issues. At least in my experience.
[cq26xjd] (score 1, diepte 4) oh okay, yeah i was hoping someone who would know for sure could weigh in
(17 reacties met lagere score weggelaten)

=== THREAD zp5xfd ===
SUBREDDIT: r/weddingplanning
DATUM: 2022-12-18  SCORE: 172  REACTIES: 69
TITEL: After searching forever, I FINALLY found shoes that give me some height without hurting my feet. They're so comfy! But are they too plain and not bridal-y enough?
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j0r77vj] (score 172, diepte 0) Besides some specific shots of your shoes that the photographer may take, no one is going to see your shoes. I would opt for comfort on a day when you’re going to be on your feet and dancing for the majority of it. I switched into flats for dancing with a short dress and the shoes were super plain, and I don’t even notice when I look back in pictures - but I would remember if I felt awful and uncomfortable!

If you want to spice it up, maybe opt for some fun blue nail polish or some bridal type design on your toes?
[j0rgif1] (score 66, diepte 0) You could maybe get some shoe clips to make them a bit more bridal-y?
[j0rjiu9] (score 50, diepte 0) I’ve looked high and low, going back and forth and then I had the realization that when it’s over the last thing I’ll ever think about is the shoes I wore. 

Comfort is your priority! If you feel good in them all day long that’s what matters… plus you can totally wear them again and get some good bang for your buck!
[j0ru4u9] (score 43, diepte 2) Just a word of caution with clips -- make sure to test out how they work with your dress (if it's long). Anything sharp will catch in the dress constantly and potentially rip something.
[j0r898g] (score 37, diepte 1 OP) Oh bridal type nail polish on my toes is a great idea! And thank you for the perspective on things, it totally makes sense that the shoes wouldn't even be that visible. :)
[j0rhpub] (score 21, diepte 1 OP) Ooh shoe clips! That's a wonderful idea, thank you!
[j0rtnbs] (score 21, diepte 0) If you’re a bride and you’re wearing them, they are totally bridal enough!
[j0rhrao] (score 19, diepte 0) They are great!
Have a pain free wedding and wear the shoes that enable you to have fun! 
My shoes are in maybe 5 of the 900+ photo's the photographer took. And i used 2 in the album. So to put it in perspective...
[j0rxaes] (score 15, diepte 2) 98% of the “important” decisions about your wedding are actually inconsequential. Keep things in perspective. 

What matters:  

- everyone who is important shows up on time:  bride, groom, witnesses and officiant, plus loved ones.    
- food, drink and music are enjoyable    
- everyone behaves themselves 

What’s really not that important:  

- clothes.   
- flowers.   
- color scheme.   
- “balanced” bridal party.
[j0rvzg2] (score 11, diepte 3 OP) Oh gosh yeah I don't want that, thanks for the tip
[j0rn7qz] (score 10, diepte 0) This is exactly the type of shoes I'm looking for, comfort over everything but still cute. I think they're lovely 😍
[j0rnc4f] (score 10, diepte 0) No one is going to look under your dress. As long as you’re comfy that’s all that matters. Maybe bedazzle them if you want or don’t. I’m wearing white sneakers after I take off my heels.
[j0rm3ik] (score 9, diepte 1 OP) Haha you're right, I am absolutely overthinking this. Thank you!
[j0rtrwk] (score 9, diepte 0) Professional wedding photographer here - Honestly if they’re comfy than wear them! Most wedding dresses are long and cover shoes anyway. You don’t want to be miserable on your wedding day with shows that hurt your feet! Cause if you do that’s all that will be on your mind is your feet hurting. I’ve seen many many wedding shoes and these will work totally fine! Again, can’t even seen them under the dress normally.
[j0rmncb] (score 8, diepte 1 OP) These are from Madewell!
[j0rgcrb] (score 7, diepte 0) I think they are super cute and will look adorable under a wedding gown (:
[j0s8zsk] (score 7, diepte 3 OP) They are Lina sandals from Madewell!
[j0sbdb3] (score 7, diepte 4) I saw they make a [metallic](https://www.madewell.com/the-lina-platform-sandal-in-crinkled-leather-NH952.html?dwvar_NH952_color=EE3115&cgid=shoes-heels#start=5) version as well
[j0rn76j] (score 6, diepte 2) I can’t tell you how many times I’ve told my friends they were other thinking things when they were planning their weddings… then I turned around and did the exact same thing 😂 as long as you’re happy you wear whatever you want! ❤️
[j0rlnkg] (score 5, diepte 0) Can you provide the brand?
[j0rvuka] (score 5, diepte 3 OP) Dug through my old order email, haha, they are the Lina platform sandal.
[j0rpg5o] (score 5, diepte 1) After so many people recommended Naturalizer I invested in a pair of flats for a wedding I was in. I broke my toe dancing in them, but didn't even notice at first because I also pinched the nerve to that half of my foot. I will be wearing dressed up combat boots to my own wedding reception.
[j0recql] (score 4, diepte 0) Honest opinion- they don’t seem very bridal to me. Maybe to change into for the reception but for the ceremony I would find different shoes. Just my personal opinion
[j0rskt2] (score 4, diepte 1) Yes came here to say this! Etsy has cute affordable ones
[j0romdd] (score 4, diepte 0) I’m personally only wearing pretty shoes for photos and then changing into trainers 😅
Do what ever makes you comfortable! We spend far too much on our weddings day to be uncomfortable or in pain.
[j0rtbre] (score 4, diepte 0) Bedazzle it! Seriously though, you can find beautiful lace and other decorative ribbons in craft or fabric stores and put them on to make it look nicer.
[j0s4crm] (score 3, diepte 2) I was so excited thinking since I thought these would be great Madewell dupes...

Weird question, do you have wide feet? I've almost bought these but I have wide feet and sandals can be hard and they're on the too-expensive end for me to gamble on.
[j0rv048] (score 3, diepte 0) If your dress is long, almost no one will see or notice your shoes unless you make a point of showing them off for photos or whatever. These are great because you can rewear them. Just have some nice toenail polish on if people get a glimpse.
[j0ta02i] (score 2, diepte 4) That and make sure they don’t press on your toes too uncomfortably too!
[j0rtefo] (score 2, diepte 2) What's the name?
[j0rzu27] (score 2, diepte 4) You are so kind
[j0s5z8i] (score 2, diepte 3 OP) I have weirdly shaped feet where they're mostly very narrow but are very bony and wide right by the toes, so heels tend to hurt really bad. I'm not certain but if you have overall wide feet these might be too narrow for you. However, I also tried Aerosoles Cosmos and they were waaay too wide on my feet so I returned them. Maybe those would work for you! Turns out they have a very easy return policy with free shipping, as I found out! Haha.
[j0rmlo2] (score 2, diepte 1 OP) I have, yes! Unfortunately even the normal width are too wide for my feet and ankles and they fall right off. That's a problem I've had in general with the comfort brands. It happened with Aerosoles too.
[j0rp3wp] (score 2, diepte 1 OP) Aw thank you! That makes me feel more confident. :)
[j0s77wj] (score 2, diepte 2) Can we ask what kind they are?
[j0rnujx] (score 2, diepte 0) Super cute and no one will notice under the dress. My focus was to find something that I felt comfortable and pretty in. So you pick what you love!
[j0ruffa] (score 2, diepte 0) Just slap some glitter on those babies!
[j0rxdkn] (score 2, diepte 0) I think they’re lovely shoes! Most people won’t notice them at all. My SIL wore crocs on her wedding day and literally no one knew!
[j0rxgvw] (score 2, diepte 0) you can jazz em up so easy if you want! buy some [ribbon](https://a.co/d/2gf9hRe) and tie a poofy bow on the back, get a [clip on](https://a.co/d/0U3TFiF) shoe decoration - it can be so fun :)
[j0stwun] (score 2, diepte 1 OP) I do have a full length dress! That's really good to know, my choice to get these was definitely motivated by the desire to dance the night away, haha.
[j0t6q55] (score 2, diepte 0) You could glue pearls or rhinestones on
[j0tmwll] (score 2, diepte 0) Do you want any attention drawn to your feet? It should be about your face and your dress. The plainer the better. Keep attention focused where it matters
[j0udpqg] (score 2, diepte 0) I spent $200 on a pair of white heels for my wedding and ended up wearing slippers the entire night, don’t worry too much about shoes looking bridal enough!
[j0thl62] (score 1, diepte 4) It sounds like these are not the shoes for me. Which is sad but thank you for filling me in!
[j0rlujk] (score 1, diepte 0) Have you looked at Naturalizer at all?
[j0rtc9g] (score 1, diepte 0) Where are they from? This is exactly what I have in mind
[j0ryphs] (score 1, diepte 0) Those are cute and if comfortable, wear them! I am wearing nude Naturlizer Berlin pumps for my wedding because they are my most comfortable heels and I can wear them all day. I'll be adding some fun shoe clips to dress them up, but honestly no one will be looking that closely at your feet. Hope your wedding is everything you want it to be! Enjoy it!
[j0sbvdi] (score 1, diepte 0) I was tossing up between high and low heeled variants of the same shoe for my wedding, leaning toward the higher heel because I’m pretty damn short and thought it would look more ~elegant~ and ~bridal~ …Showed both to a friend, thinking they’d agree with me, but they immediately said, “When you’re standing there committing your life to [partner], you don’t want to be thinking about your feet.” When ya put it that way… I bought the low heel and don’t regret it. 😁
[j0scszc] (score 1, diepte 0) No one will see your shoes. Go with what is comfortable.
[j0sg0hj] (score 1, diepte 0) Can you jazz em up yourself with a glue gun or special craft glue?
[j0sj6s9] (score 1, diepte 0) They look great, to up the wow bridal factor you could get a bridal pedicure, get some pretty shoe clips whatever.
[j0sm2fn] (score 1, diepte 0) Do you have a full-length dress? If so, who cares! Be comfy. Seriously. I wore not-so-formal shoes with my dress, and I'm so glad I did! I walked the aisle, took pics for 45 minutes, danced for 4 straight hours (and only missed about 3-4 songs), and I ended up with only two small blisters on my big toes with no pain the whole night. And in none of the pics can you see my shoes.
[j0sxrez] (score 1, diepte 2) Yea, my guests were asking my husband if I was OK because I basically never left the dance floor 😄

If I'm being honest, I can't understand why women buy shoes at $500+ for their wedding with a full-length gown, outside of getting pictures for Instagram. And I've been at many weddings where women wear those super expensive, fancy shoes and end up taking them off right after the first dance. 

My best advice for your wedding is to be comfortable overall! Comfort for your shoes, dress, jewelry, makeup, hair, etc. Don't overdo it! If you don't normally wear stilletos and giant earrings and heavy makeup, don't do it for your wedding. You want to look beautiful, but you should also try to be yourself.
[j0snvh5] (score 1, diepte 0) Go to a thrift or fabric store and get a little white lace, take it to a seamstress and ask if they would see the edges of the toe and ankle piece maybe? Or paint small white flowers on the wood by the heel? I think they’re so cute as is, these are just suggestions in case 🖤
[j0sps06] (score 1, diepte 0) Or if you have any dance/dance mom friends they could bedazzle those up in no time.
[j0sqvt8] (score 1, diepte 0) If your dress is long you’re not going to see you shoes. Take it from me

I got heels that I thought I could bear and it was so bad and I was cranky during photos. At one point I needed to take them off before the ceremony because they were killing me!
[j0su668] (score 1, diepte 0) If they are comfortable, wear them !
[j0surwk] (score 1, diepte 0) I got a tall gorgeous pair of heels and a pair of backup comfies. I changed into comfies after 5 minutes. No one’s looking at your feet but you will remember if you spend your day in misery bc of your shoes
[j0szyod] (score 1, diepte 0) Honestly only you know your event also. Some people have very casual weddings. You could also wear these most of the night and then get something just for some pics
[j0tb4ws] (score 1, diepte 0) I had very plain but comfy light colored wedges and my seamstress was able to add some lace and embellishments leftover from altering my dress. They turned out great. Comfy, beautiful and one a kind.
[j0tbghk] (score 1, diepte 0) They’re adorbs and I love them for you!
[j0tf9dz] (score 1, diepte 0) You could add bling or lace. Whatever matches your dress
[j0twcts] (score 1, diepte 0) I went for little satin wedges, as I can't wear higher heels due to injury. Honestly very few people saw them and I could have easily changed into other shoes if I needed to. But I didn't have to :) 
If you want to make them more...bridal? You could always glue some ivory satin ribbon or lace to the straps? Less likely to get in the way than those shoe pins.
[j0u8nj7] (score 1, diepte 0) I had 2 sets of shoes! For pictures and actual ceremony I wore a vintage red heel. For dancing and reception I switched to my crocs 😅 Now, my dress covered the crocs for the most part, but it was worth it.
[j0ue8qn] (score 1, diepte 0) I had similar nude heels that were kind of plain for the walk down the aisle, then switched into white sneakers for the reception. No regrets, no one could see my shoes anyway and nobody cared about if they were bridal-y or not. Wear what is comfy! :)
[j0uhr5k] (score 1, diepte 0) I think they are a little too plain for the special day. Maybe something with a little bedazzle
[j0uhrbs] (score 1, diepte 0) Agree with comments that shoes are barely visible if you're wearing a long gown and a lot of brides end up taking off their Badgley Mischkas at some point during the night anyway. Don't sweat it. If you love how they feel, go for it!
[j0vjj7r] (score 1, diepte 0) Most bridal shops sell liquid shoe dye in several different colors. The shoes could also be blinged out with glued-on crystals or sequins. Hope this helps.
[j0ydov2] (score 1, diepte 0) I got married in sparkly flipflops, awfully comfortable. I was 8 months pregnant at the time, couldn't wear heels, and did not have the funds for decent shoes. We had an afternoon catered picknick in the local petting zoo, and no dancing, so I was fine.

=== THREAD 1ni59ak ===
SUBREDDIT: r/rheumatoid
DATUM: 2025-09-16  SCORE: 27  REACTIES: 69
TITEL: Best shoes for RA sufferer who is on their feet all day?
POST (source_id=post):
Hello! 
Longtime lurker, first time poster. 
I work a restaurant hosting job and I’m on my feet the entire shift. I have rheumatoid arthritis and it targets my feet and hands the most. I also have poor posture and most of my weight falls on my heels. 
With all the information provided above, what shoes do you recommend? 
Thanks in advance!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[negswky] (score 24, diepte 0) I can only wear Hokas at my job. I've tried almost all the other brands & Hokas are the ones that work for me. So comfortable. 

I personally buy the Bondi :)
[negosxv] (score 23, diepte 0) Anything with a box toe and good supports is key. I personally love Altra's, Keens and I hear a lot of people like Hoka's too
[negnpl6] (score 15, diepte 0) Hoka's...sometimes the only shoe I can wear.
[negmxro] (score 11, diepte 0) Crocs
[neind5h] (score 11, diepte 0) Tips from someone that walks 20k steps each day at work:

Find a comfort or athletic shoe store and have them do a fitting. I went to one that had me walk on this platform that measures gait/pressure/etc. Turns out I need a lot of arch support. Prices may higher at stores like these, but I think it's worth it.

Quality insoles make a big difference. Buy shoes a half size bigger - or get the insoles first and try shoes on with them. I used to buy insoles when I bought shoes at the running shoe store, but I found something similar on Amazon that was cheaper and still worked great.

Compression socks make a difference too, at least for me. I have a couple knee-high pair that help when I start to get shin splints.

Everyone is different, but Hokas (Clifton) are by far the most comfortable shoe I've tried, with the least fatigue & pain at the end of the day. Brooks (Ghost) I liked also. I tried a couple On Clouds, which were comfortable but I did start to hurt at the end of the day. And I like Ecco shoes (ankle boots or a leather sneaker) when I need something more polished.

Good luck!
[negz602] (score 10, diepte 1) Bondi.  This is the way. Can confirm.
[negpyjl] (score 8, diepte 1) I second the Altra’s. The only shoe that has room for my toes when they’re swollen. Those and surprisingly sk8 hi top vans
[negifil] (score 7, diepte 0) I wear Keens when I am hiking. Large toe box. These are the only shoes that allow me to stand for a long time. They have women’s work shoes in black, too. https://www.keenfootwear.com/collections/womens-manufacturing
[nei8tju] (score 7, diepte 1) This!! I got it in my toes and hokas quickly became the only shoes I can wear for longer than 30min
[negsowt] (score 6, diepte 1) Crocs are my go-to. I use classic crocs at home and for casual wear, and the professional series slingback clogs for a slightly for polished look with more support.
[neh17la] (score 6, diepte 2) Altra shoes used to last so much better. For the past year or so every pair I get seems to fall apart way too quickly. Topo seems to be slightly better quality. And they have the same very wide toe box.
[negyw1i] (score 5, diepte 1) This is the way. There is no other.

(Shhhhhh... don't even pretend there is another)😉🥸

They have a professional line for nurses and on your feet all day wearers and they are all leather exteriors.  I love these.
[nek3543] (score 5, diepte 3) Bondi SR's

https://www.hoka.com/en/us/mens-recovery-comfort-shoes/bondi-sr/1110520.html
[nehvgdz] (score 5, diepte 0) I love ASICS. I’m a dog walker and my shoes must be comfortable. Asics have a ton of cushioning and a wide toe box. I do replace them about every 9 months or so. I end up wearing them more than any of my other shoes.
[neigaur] (score 5, diepte 0) I decided price was not an object and after trying on ALL the Hokas and similar shoes in an upscale sporting goods store, I tried on a pair of New Balance fresh foam x  (my husband wears NB and I really did not want to like them) and was amazed with the fit and comfort. I'm sold! They were a little less expensive than Hokas, I didn't care! They fit great and my arthritic feet are happy!
[nej8cw2] (score 5, diepte 0) I wear Hokas every day on my 5 mile walk through woods. Excellent support and comfort😁
[nelx3rv] (score 4, diepte 2) Yes crocs! It's almost all I wear. The squish they have cushions my joints like no other. I wear doc marten sandals too but they take lots of time to break in and are heavy, so while they are comfortable, on bad fatigue days making my legs heavier isn't ideal. Crocs have so many cute styles, people always compliment my shoes and are shocked when I say they are crocs. There is one pair I bought recently and unfortunately they aren't as supportive in the heel. This is the 1st time this happened. They are no longer available on the site it looks like. They looked similar to the stomp fisherman sandal but open toe and not huge platform. Anyway if you can, try them on. Also Crocs go on sale all the time, especially on tiktok shop. Do wait for the next sale.
[nejzs1u] (score 4, diepte 2) I wear Clifton, but they have a few styles to try. Now I want to try the professional line discussed above.
[negpaxe] (score 4, diepte 0) I was having problems finding a kitchen shoe and tried Hoka. They were great but the soles separated from my toe area at 8months. Switched to a pair of Brooks for over a year and they are still in pretty excellent shape, and it takes a 15hr day for my feet to really hurt.
[neh1c1x] (score 4, diepte 3) Yeah I can imagine the laceless would be bad for work.  

The laced Bondi SR say specifically for work.

https://www.hoka.com/en/us/mens-recovery-comfort-shoes/bondi-sr/1110520.html
[neidjat] (score 4, diepte 0) Soles of my feet is the one place I feel RA pain every day despite treatment. I’ve tried several shoes and the one that does it far and away the best for me are the On Cloud Cloudmonster Void. Incredibly supportive and goes me a feeling of stability, plus there’s a little bounce in the heel to give me a needed spring in my step.  Just ordered a second pair in a different color.
[neijbhp] (score 4, diepte 0) no shoes. barefoot shoes have made my knee effusion go away. of course this took immense effort but i could barely walk or bend my left knee. 

once i found out that big cushions on your feet make them weak but not just your feet the ligaments, ankles, knees, hips, back, all the tiny muscles, and your fascia. This damages your posture greatly as well. 

so regular shoes were reducing my foot’s natural motion. which uses my muscles, ligaments, and fascia to pull Excess water off of my joint!! 

this took serval months and everyday i went on a walk i focused on stepping up onto things with my left knee. to promote more full movements to. 

Cushions are a lie. but we have been cushioned for so long it would take literally years of effort to strengthen and go back to thin soles.
[negmauf] (score 3, diepte 0) I'm on my feet all day, I work in the trades. I really like vionic, they're orthopedic and come in many different styles. My other favorite is the converse run star. They're platforms with a thick sole that makes them super comfortable to stand in all day.
[negshqe] (score 3, diepte 1) The Altra’s fit was great for me. Only problem was how fast they wore out with moderate use. For the price, I expected them to last longer. I had the women’s Olympus, and the whole shoe broke down very easily in only a year and a half.
[neh5avj] (score 3, diepte 3) I dont know about these and I will have to look into them. However, I have been using the Nike Air monarch with the 4e, so their extra extra wide. Good fit, reasonable support, and under $100. 

That said, I tend to squish the arch supports pretty flat after a year or so, but the cushioning in general stays good, and the toe box is wide, it accommodates a high instep, and I have yet to destroy an outside of these shoes. Even with daily wear, including in snow.
[nejoqgh] (score 3, diepte 1) I got a pair of white Brooks because white was on sale. Been wearing them during my bar shifts for well over a year. The other day a customer was like “those are cute shoes, are they new? I laughed pretty hard. She thought my super old white brooks were a brand new pair of gray brooks bahaha
[negzp6g] (score 3, diepte 2) I just received the Bondi 9, and wow, they are so much more comfortable than the Bondi 8 for me!

I purchased a pair of their new skyward laceless cuz I love that peachy color, but when I texted with an agent, she said that it really is best as a casual shoe, unfortunately (meant for recovery).
[nehcr81] (score 3, diepte 0) I just have orthapedic souls that cut to size in all my shoes.
[nehpixa] (score 3, diepte 0) Get a referral for to an orthopedic doctor and get some inserts.
[neit4d0] (score 3, diepte 0) Oofos
[neixiy5] (score 3, diepte 0) I'm on my feet all day and after trying tons and tons of shoes, a lady at a shoe store helped me find a pair of insoles and they were the game changer. I just explained to her the parts of my feet that hurt and I tried a set and it felt weird for a few days but then my feet have never been happier!
[neizps5] (score 3, diepte 0) I'm on my feet all day and after trying tons and tons of shoes, a lady at a shoe store helped me find a pair of insoles and they were the game changer. I just explained to her the parts of my feet that hurt and I tried a set and it felt weird for a few days but then my feet have never been happier!
[nejfr3b] (score 3, diepte 0) I’m a school lunch lady with rheumatoid arthritis; Hokas are amazing if you can afford them. My other favorite pair is a Costco/Kirkland brand pair I got for $15 at a Canadian Costco. Best if luck on your search, glad you are taking g good care of your feet!
[nejrn8g] (score 3, diepte 0) Adidas Stan Smith's are my go to, they are comfy, well constructed and come in small sizes.
[nek7d9n] (score 3, diepte 0) Many people swear by HOKAS!  I keep meaning to go to our local shoe store to get some.  I first became aware of HOKAS at the hospital… a bunch of nurses were wearing them.  I was so intrigued that a large swath of the nursing staff were wearing the same brand of tenny, I asked what it was.  Later I realized that a bunch of clerks at our grocery store were wearing them.  All the shining feedback I got on the footwear sold me.   Hands down every person said:  Best shoe ever!Great compliment from normies who spend their working life on their feet.  Now I just need to be able to get my hands to a point where I can safely drive my car to the shoe store.
[nekkrhx] (score 3, diepte 0) I wear Hokas if I’m going to be on my feet all day or walking. For standing still, I find the Hokas with the thickest, cushiest soles. For walking, it’s usually the Bondi’s. For shorter periods I’ll do Birkenstocks.
[nemgc1k] (score 3, diepte 0) Hokas. Have a black and a white pair. They last forever!!!!!!! I’ve even had orthotics put in when I had torn tendons- I swear these shoes helped me heal. Also don’t go barefoot in your house. I have Hoka slides as slippers.
[nej8pw0] (score 2, diepte 2) I have Target IV. They run large, tbh I call them my clown shoes but they’re comfortable
[nem3mdo] (score 2, diepte 2) Right! I work outside and have the winter boots and the weird looking tennis shoes. They are actually holding up way longer than sketchers and artiats
[neo7yb1] (score 2, diepte 1) I’ve found crocs to be terrible - no actual arch or sole support and my podiatrist recommended strongly against them. Can’t understand how they’re comfy for other ppl aside from the fact that they’re cushiony!
[nek03a1] (score 2, diepte 2) Where do I find these? I want a pair.
[nen89gk] (score 2, diepte 2) Bondi :)
[nek19qw] (score 2, diepte 2) Regular...but you should measure and make sure what you need? I am right on the edge of reg and wide, but my feet slide around in the wide.
[neqgx9j] (score 2, diepte 2) I have wear the Vans with comfycush
[nej07cy] (score 2, diepte 2) A year and a half of moderate use is a long time for a tennis shoe. During heavy use they break down in 6 months (any shoe). I love my Altra's. I tend to make sure the shoe has zero heel drop as well. I find on days that my feet are bothering me my Altra's are the only thing I can comfortably wear.
[negtayy] (score 2, diepte 1) I still have my Brooks shoes (I forget which style even though I wore them today cuz i'm on staycation) & I really like them for casual use. But they didn't help my feet when I wore them all day for my shift. They aggravated my plantar fasciitis.
[nemgf51] (score 2, diepte 1) Same with Bondi!
[negx65p] (score 2, diepte 0) https://mizunousa.com/men/shoes/running/?p=2
[neh53v6] (score 2, diepte 0) I don’t really have specific shoes that come to mind because I use my custom orthotics. I absolutely love my custom orthotics! I just swap out the insoles of whatever shoe I’m going to wear with the custom orthotics. 

I used to get regular shoe inserts and get shoes with support in them but nothing has worked better than my orthotics that I’ve got! 

Such a big difference for me with my hips, feet, and knees when using my custom orthotics. They have lasted me a few years so far. I am still in pain regardless but I last longer with those.
[nehd67d] (score 2, diepte 0) I wear Joya shoes. They are a Swiss brand. Expensive but the last for ages and have great cushioning. I also get custom orthotics on my health insurance which makes a huge difference
[nehp94c] (score 2, diepte 0) I'm the same mainly in my ankles and feet, I wear anything that is Adidas cloudfoam during a flair, very comfortable and soft on the feet
[neib4xf] (score 2, diepte 0) Birkenstocks. Always.
[neidute] (score 2, diepte 0) Birkenstocks saved me.
[neiepyb] (score 2, diepte 0) Altra lone peak’s with carbon fiber foot plates off Amazon. That’s what has helped me. I have an appt for custom in soles on Wednesday.
[neiho5u] (score 2, diepte 0) New Balance 880’s. I got tired of trying different shoes and finally went to an orthopedist who recommended them and some orthotic insoles.

Magic!
[nen408f] (score 2, diepte 1) And New Balance 1080’s
[nejj9sj] (score 2, diepte 0) I’m a bartender with MCTD that often gives flares in my various joints/hands/feet etc. I have been alternating between dansko professional clogs and Brooks running shoes every shift. I like the danskos because their structure and arch support make my overall posture better, but I can’t wear them every day because they will eventually hurt my feet. Sometimes I can wear them two or three 8+ hour shifts in a row and they don’t hurt my feet at all though! All depends how bad my feet and ankles are flaring. If you try danskos, size up. They’re very firm and your heel is supposed to wiggle up and down a bit while you walk.
[nejqx9i] (score 2, diepte 0) New balancefresh foam
[nel5pce] (score 2, diepte 0) Chacos!
[nelf3js] (score 2, diepte 0) Birkenstock has an entire collection of professional slip resistant shoes. I’m really fond of the QO 500 that they make, which just so happens to be in this line. It comes in both men’s and women’s. The toe bed of this shoe matches the natural form and profile of your flat foot. This has been an absolute game changer for my RA feet, especially at work! I will say because they’re Birkenstocks they’re a bit on the pricier side, but in my opinion you’re paying for comfort and a quality product.
[nep0pxm] (score 2, diepte 0) OrthoFeet for me (not RA but lupus and OA and bunions and very needed up feet plus some surgical interventions after a broken ankle-fibula so the ankle is mostly metal with nail, pins and screws and a metal tightrope inside holding it all together; lots of pain in the also damaged joints). 

They do last, and have multi-adaptable insole inserts for various conditions. But gosh they’re expensive.
[nep2v57] (score 2, diepte 0) I like Vionic recovery shoes/sandals.
[negkppm] (score 1, diepte 1 OP) Which Keens specifically?
[nem3tfr] (score 1, diepte 3) That's where I get a bunch, the TikTok shop, I am easily influenced I guess.  But I notice a huge difference in pain.  I spend a lot of time on my feet
[oi1tkof] (score 1, diepte 2) Same! They kill me!
[nehonom] (score 1, diepte 1) which model do you like?
[nejfwg4] (score 1, diepte 1) Do y'all get the wide version or regular?
[nek6wec] (score 1, diepte 3) Heard, thank you!
[ngqv5xt] (score 1, diepte 2) Van? Really?? I guess I've never tried those
[nelsiwo] (score 1, diepte 1) Big fan of Keen Hiking boots. Yes they are pricey but well worth it.
[net9d3e] (score 1, diepte 1) I came here to recommend Keens. They're all I will wear
[nen7rf0] (score 1, diepte 4) Once I return my laceless, i'm going to order the SR :) I've got high hopes!
[net8wji] (score 1, diepte 1) Same here! ASICS. I have an indoor and outdoor pair and replace them every 9 months. I have serious foot issues and they bring me the most comfort. Can’t wear anything else. Not even sandals 😩
[nen8pnn] (score 1, diepte 1) I use afterpay because it is offered on hoka's site, and that's the only way I can afford them.
[nepkfcb] (score 1, diepte 0) Skechers and their memory foam shoes were the only shoes I could handle wearing for a couple years in the beginning of my diagnosis. They also make restaurant-grade shoes. I HIGHLY recommend taking a look!
[nepm7h3] (score 1, diepte 0) Hoka Bondi’s, they come in all black if you need that for your job.
[neqmtlu] (score 1, diepte 0) Birkenstock and Hoka
[nezkega] (score 1, diepte 0) I wear kitchen/chef's clogs by Dansko. Got cute patent pleather ones a couple of years ago. No one cares that I'm not a chef :)
[nf79s4p] (score 1, diepte 0) Hoka Gaviota 5's with stabilizing insoles while out and Oofos recovery sandals when home. 🤌

Fleet Feet does the 3d model of your foot and gait for a custom fit.
[nfah04r] (score 1, diepte 1 OP) Does Fleet Feet charge for that?
(5 reacties met lagere score weggelaten)

