# Label-batch batch_0171

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
Schrijf het resultaat naar `batch_0171.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: bsel0o, 34pq1h, uhzs8v).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD bsel0o ===
SUBREDDIT: r/xxfitness
DATUM: 2019-05-24  SCORE: 92  REACTIES: 58
TITEL: Gross but necessary cry for help, what do you do if you sweat so heavily your feet ruin your trainers?
POST (source_id=post):
Background:Commuting I walk 4+ miles a day minimum, I run frequently, lift weights at the gym, and hike at weekends. I have PCOS so my hormones are a bit whacky (but I am muscular and quite thin). 

My problem is that within 3 months of owning my trainers, I completely annihilate them with stench. I never wear without socks, I wear antibacterial/moisture wicking socks, I even got an 'Odor Eater' trainer spray & insoles but these didn't seem to work in the slightest. My girlfriend is at her wits end with my trainers. 

Do I wash them on cold/hot? Baking soda doesn't seem to have done much, do I scrub it in? Leave them outside in the fresh air for all eternity? Freeze them? Disinfectant? Are they all ruined? Do I have to chuck them? (They were all over £80 RIP)

Please help and please say I'm not the only female with this issue.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[eomj9zv] (score 121, diepte 0) I’ve heard that they really need to air out for a day or two and be completely dry if your feet are real sweaty. You shouldn’t wear the same pair every day if you can help it. If you can afford it, try keeping 2-3 pairs on hand you can rotate through, while continuing the inserts and sprays. It’ll cost more upfront but hopefully save you costs in ruined shoes. 

Have you also looked at putting deodorant on your feet? That can help a lot—especially prescription strength. Follow the instructions carefully because a lot of the prescription strength are meant to be put on the night before to be most effective. 

As far as saving this pair, maybe carefully washing them and letting them dry in the sun if possible. Sunshine is a great disinfectant.  I’ve used Lysol too and let them dry. It is hard to get smell out if it’s really set in though (speaking from experience).
[eomyfaf] (score 56, diepte 0) I think if you buy 3 pairs of trainers and alternate, they’ll cumulatively last longer than nine months. Ideally, you should never put on shoes that are still damp from the day before.
[eomqpdz] (score 31, diepte 0) Look up boot bananas. You put them in your shoes after wearing them to absorb the moisture, and they have a bit of scent to them too. I’m a climber and my shoes get super stinky in a hurry (I don’t wear socks with them, and they’re really closed in)... the boot bananas definitely help when I actually use them!
[eomutbb] (score 25, diepte 1) If you do try washing them, use Borax as well as detergent. It works wonders on gym stinky clothes and may also help here. And it’s cheap
[eon98de] (score 19, diepte 0) Shoes are only half the problem. You need two or three to alternate through to allow the others to dry.

But you also need to clean your feet. Like REALLY clean your feet. The smell is bacteria and the  bacteria are living in your dead skin. There's a purple pumice stone brand name "mr.punice" this is in my opinion the best pumice stone you can buy. You need to hit your feet with this every time you're in the shower. At first a heavier scrub is good. Over time you'll have worked the majority of the dead skin off and you can get by with a quick hit. Trim your toe nails, keep them short and clean underneath them with a nail scrub brush in the shower every day too. You can be really extra and moisturize your feet after. Which is a good idea anyway. I'd use a lotion like eucerin or amlactin that helps promote skin turn over or choose a lotion containing something like tea tree oil that will act as a natural antiseptic.

Pay attention to brand and materials. Some materials can have some reactions with your skin and this may be contributing to your issues.

I follow this foot care and my uniform boots are almost 4 years old now and my feet don't smell in the slightest after wearing them for 12 hours outdoors in the summer in the southern united states. I have had awful foot odor in the past.
[eomuzat] (score 16, diepte 0) Do you have hyperhidrosis (excessive sweating), or is it only a feet problem?
[eomv78u] (score 12, diepte 0) Okay this one might sound weird but I was in the position where my shoes stunk to the high heavens but couldn’t afford a new pair yet.

So I poured a little orange essential oil on the insoles and wiped. Then stuffed socks with clean kitty litter, made them about the size of my feet, put the essential oil in there too, and shoved them in my shoes for three days, just used flip flops.
It wasn’t a miracle fix, but the litter soaked up some sweat and the orange masked the stench. 
I took it a step further and just poured the litter in my shoes for another day or two but man that was a pain to get out... 

This is why I have to stick to Walmart shoes now. Or I just go barefoot around the gym. (Well, I’ve got foot protection on, but not shoes. I’m usually on the mats though)
[eomsxua] (score 11, diepte 0) I machine wash mine, usually with a load of towels. No bleach. Take the insoles out, but throw them in the wash too.

Air dry.

Alternating shoes is a good recommendation too.

My DH used to have a boot dryer, they worked well.
[eomhdck] (score 10, diepte 0) When mine get wet from rain or something I stuff them with newspaper, maybe you could try this each night? Stuff them before you go to bed each night, and try sitting them outside/by the fire/heater (if you live in a wet or humid area prob don’t leave them outside).

Edit- this may not help now but if you buy a new pair could slow the damage
[eoo1998] (score 10, diepte 1) > You shouldn’t wear the same pair every day if you can help it


This so much. Quickest way to destroy any shoe is to wear them constantly and not let them breathe/dry out.
[eon1ayk] (score 10, diepte 0) I've been rotting out sneakers with my prodigious foot sweat since the 6th grade. My feet sweat so much I wear socks with my dress shoes, never wear sandals, the whole bit. Tried prescription antiperspirants, pills...apparently botox injections would be effective, and also time consuming, painful, and pricey. So...no thanks.

I wear a pair of sneakers as my work shoes, and boy howdy, yuck. Recently, I washed them. I popped the laces and the insoles out, threw all the pieces in the washing machine with a bunch of towels, detergent, a heap of white vinegar. Washed on cold, delicate cycle. Let them air dry. And guess what! No more stink!

I also change out insoles for new, not smelly ones from the drug store sometimes, and I always buy cheaper shoes. I don't know if I can recommend washing them if they're leather uppers or suede or something, but if it's an all fabric/plastic piece, give it a shot?
[eon16rh] (score 9, diepte 2) Second this, we used borax when cloth diapering.   Or try some vinegar in the wash
[eonil9n] (score 9, diepte 1) This this this. I have the sweatiest girls feet and finally just broke down and bought more pairs of shoes. I rotate them ALL the time and replace any pair that starts to get too gross. I also started using a spray deodorant on my feet in the morning and actually think this has helped significantly, even if my feet still feel gross and stinky by the end of the day.
[eon36a1] (score 9, diepte 1) Yep, getting medical treatment (I think botox helps with sweating) might be a good solution.
[eon3qoo] (score 9, diepte 0) I have/had this issue. At work I wear a full jump suit with those blue shoe covers you see tradesmen wear when they have to work inside residential homes.  Sweat pools up and then promotes bacteria to grow (the bacteria is what stinks, not necessary your sweat) 


Sorry my solution is going to cost you some money.

Throw the shoes out. Possibly throw the socks out. You may consider them contaminated.  You can kill the bacteria but you will have to use harsh chemicals or high temp to do so, and that will probably ruin the glue and stitching of the shoe. 

You need a shoe dryer. I like the type that blows air on a timer. (https://www.amazon.com/PEET-Dryer-Original-2-Shoe-Electric/dp/B001J4HQ76)

Two pair of shoes, because you want them to completely dry.

A shoe disinfectant spray. I use https://www.amazon.com/10-Seconds-Shoe-Disinfectant-Deodorizer/dp/B00BSGDZVQ
or you can go to your local bowling ally and ask them what they use for the rental shoes.
[eon12tb] (score 8, diepte 0) Seconding the recommendation to alternate between 2+ pairs of trainers - giving them time to dry out should help limit the growth of odour causing bacteria. This is also a good recommendation for leather shoes - if you keep wearing the same pair day in day out they stretch more.

Also, check what material your socks are made of - I've worn nylon/polyester socks and noticed my feet stink afterwards. Once I switched to cotton, I didn't have any smelly feet issues.
[eonhyg5] (score 7, diepte 0) Oh yeah me too! I have hyperhydrosis of my hands and feet, it sucks! I’m also active, cycle or walk for transport and work on my feet, so every day my feet are soaked and I’m squelching around in it.

1st most important step of shoe preservation is LETTING THEM FULLY DRY BETWEEN WEARS. If they are totally dry before you wear them again, there should not be any, or minor, bacterial growth or stench. 

2nd: this means you need multiple pairs of daily shoes to rotate. It’s an initial investment, but they will all last much much longer. I have a lot of shoes of all types and if I can, try not to wear one pair for more than a few hours at a time.

3rd: FOOT POWDER INSIDE YOUR SOCKS. ITS SO GOOD. 

4th: I prefer wool socks with as high a wool content as possible to any synthetic antimibrobial stuff. 

5th: wash your feet and your socks as often as possible, in hot water with plenty of soap, and do multiple washes sometimes. Soak them in vinegar if there are lingering odor issues. I usually save up a weeks worth of socks and do an intensive hand wash in a bucket before putting them through the washer.

Hope it works for you! I spent 15 years being humiliated by stank shoes and feet before I figured all this out.
[eonjjuz] (score 7, diepte 0) the one advice that came in mind is that I rarely wear any shoes two days in a row. air out the shoes and use shoe inserts to fight against odor, but remember to put inserts into dry shoes. 

if the shoes are washable, many are, wash them on cold. 

in my experience, once the shoe starts stinking real bad, it's hard to combat. it's a lot about pro-active measure starting from day one.
[eomzc2z] (score 6, diepte 0) FWIW I have problems with athletes foot because I workout so much and my feet get wet.  Every single day I put foot powder on my feet before my socks, to help keep they dry throughout the day.  Might be worth trying if you don't already!
[eonj6sn] (score 6, diepte 0) I agree with advice to have multiple pairs, but really you just need to buy the kind that you can throw in the washing machine every few weeks.
[eongxil] (score 5, diepte 1) This is solid advice for shoes in general. Letting them dry out between wears does wonders for their longevity.
[eongnf0] (score 3, diepte 1) Okay came here to say this. I have this same smelly, sweaty feet issue (I'm a cocktail waitress/camera operator, so both jobs equal being on your feet for 8+ hours at a time) & I've tried *everything*, foot sprays, foot powders, essential oils, you name it. The other day I finally tried the old newspaper trick and it did wonders! I don't smell a thing! Now its something you have to continuously do, and finding newspaper isn't always easy, but SO worth it! No more smelly shoes
[epo6dlm] (score 3, diepte 2) I would recommend really doing your research on Botox with feet though desensitizing your feet can really mess with balance
[eoo24ph] (score 3, diepte 1) Multiple pairs of shoes so you can not wear the same ones every day!  It's the moisture that makes them stink because it allows/encourages bacterial growth, they need to dry out fully between wears which doesn't happen overnight.
[eoo4y0f] (score 3, diepte 2) The issue with that though is some people can’t afford two pairs of shoes which is why so many tricks are being shared to try to combat the smell . 

I personally have two sets of sneakers and two pairs of slides, but I wear slides to the gym when I know it’ll just be mat work and I won’t be in the fitness center, and I have a backup pair of shoes in case my puppy eats mine. Mine are 10 dollars from Walmart, but not everyone even has that luxury.
[eoo6rpp] (score 3, diepte 3) Oh I feel you, I know all about the paycheck to paycheck life and it sucks.  But like, if you wanted to save up to invest in some more expensive shoes, that would be the key, not wearing them every day.  I interpreted your comment as you stick to Walmart shoes because they get smelly too fast and you have to throw them out kind of thing haha.
[eooi9pa] (score 3, diepte 4) Oh no, I stick to Walmart shoes because right now it's all I can afford haha. (or...at least til I find a good Kmart)  I got two big puppers that need a lot of food and the 50 bucks I could put in a good pair of shoes goes to their 50lb bag of food for the month..and then don't even get me started on my spoiled little kitty hah. Extra pocket change goes to the princes and princess right now. Two just lost their sister, after a long battle with kidney disease so they get a little bit of spoiling
[eomxz5f] (score 3, diepte 0) I haven’t had this specific problem but when mine get wet from rain, dew, or puddles I just pop them on my boot dryer. That could be an easy and pretty cheap solution.

Maybe even rinse them out a bit first, as I’m sure the salt can’t be good for the shoe materials.
[eon027f] (score 3, diepte 0) Newspaper is the best thing I’ve used to dry out shoes.  Just stuff them in when they’re wet and they should be dry by the next day.   You could try tea bags or coffee grounds as deodorizers.  You can put the coffee grounds  in some old socks or pantyhose to keep it from being a mess.
[eon250m] (score 3, diepte 0) If you wash, cold water only and air dry  (If you have a fan or air filter position it to blow through them).

Heat will soften the adhesives.
[eoq3k4u] (score 3, diepte 1) Definitely this. Regular pedicures have really changed my foot smell lmao. And they look better too even though I abuse them.
[eoo1xbd] (score 3, diepte 0) The correct answer is that you can't wear the same pair every day, because they need to dry out fully.  They won't be able to dry properly just overnight if you sweat that much (even for people who don't sweat much this can be an issue), so you have this damp environment that you're then making warmer and wetter, it's a vicious cycle that just ensures you have an AMAZING environment for bacterial growth.  And bacteria are what make the stink.  Warm and wet is good for them.  Dry is not.  They can't grow without moisture.

&#x200B;

I'm prone to sweaty and smelly feet too, and when I used to wear the same pair of shoes every day or most days they would get just horrible.  It wasn't until I started making a conscious effort to switch up my shoes every day or every couple of days that it was resolved.  I don't wear the same shoes during the day and for exercise, either, I have specific training shoes and they come out of my bag and get opened up as much as possible to air the minute I get home from the gym.  All my shoes still get a little smelly over time, but it's more like a "normal" foot/shoe smell of older shoes instead of gassing the entire house now lol.

&#x200B;

As far as your current shoes, unfortunately, I would say they're fairly ruined unless you literally wash them, like, put them in the machine.  Or sometimes just letting them sit and air for like weeks/months can help, it takes time though.  But yeah your best bet is probably just buying 2-3 pairs of new ones and switching through them to prevent the smell in the first place, once it's there in something like a shoe, it's super tough to get rid of.  Keep trying to save your old ones if they're still in good condition, but it will take some effort and may not be possible, you need something to wear in the mean time.
[eon323c] (score 2, diepte 0) I had sweat issues as a teenager omg! I was so self conscious about it. Hopefully for me everyone was kind to me.
My solution was extiacil. They have it for feet too. Look it up. I think we sweat more when we are teenager. The product worked well and now I maintain my sweat under control with alum stone. I still sweat but it isn’t smelly. The other product blocks the sweating. It works very well
[eonjd6r] (score 2, diepte 1) Yes to this shoe dryer. It works great and is super quiet.
[eon3tow] (score 2, diepte 0) 1. Boot dryer
2. Multiple pairs of shoes
3. Wool socks

I have extremely sweaty feet and so does my SO who is a mailman. We have found that using the boot dryer to really dry out the sneakers and reduce bacteria helps. Leave them on the dryer for a day then switch to the other shoes. Wool socks are better IMO than the wicking/active socks for odor control. There are lots of great brands that make lightweight merino wool socks so it won’t feel too hot.
[eonqie8] (score 2, diepte 1) Maybe get a foot peel. Look up “baby feet foot mask” on amazon. Soak your feet in warm water for 30 mins first. Then mask for whatever the recommended time + 30 mins. Rinse off and wait. Feet should start peeling in about 7-10 days. Don’t put lotion on your feet until after the peeling is done.
[eou6rxd] (score 2, diepte 2) Walmart also sells foot peels
[eongjt6] (score 2, diepte 0) I know a  woman with the same problem and it was a foot fungus that caused such a strong odor. I would talk to a podiatrist.
[eongyhy] (score 2, diepte 0) Have you tried spraying your shoes with rubbing alcohol or cheap vodka? It is works wonders at killing the bacterial that causes the odor in smelly shoes. I got this tip from a co-worker and it is amazing! I was afraid that I would smell like distillery all day, but the alcohol smell dissipates pretty quickly leaving behind shoes that smell so much better. I usually just keep a small spray bottle by my shoes and spray everything once every couple of weeks. You could definitely do it daily though.

Also, i don't know if you've looked into this- but they do make medication to help control sweating. My sister had excessively sweaty palms and she was prescribed a medication that helped control it.
[eonhk3o] (score 2, diepte 0) If they get really gnarly, put them in the wash with Tide Sport. Stuff gets the grossest gym smells right out. Also, if you happen to get them wet from rain or something, stuff them full of paper towel or newspaper and be sure to add dryer sheets as well for that fresh scent.
[eonl6om] (score 2, diepte 0) i usually leave mine outside in the hot sun and it clears them up beautifully. sometimes, depending on the sneaker, you can also throw them in the wash :)
[eonxged] (score 2, diepte 0) I don't know if anyone suggested this yet, but I'd recommend natural fiber shoes and socks, ie. leather or textile for the shoes and cotton, wool or some other natural fiber for the socks. I do have normal sweaty but rather stinky feet (thanks dad for those genes...) and can't wear anything else than real leather or textile shoes.

To the gym I wear some cheap converse copy to the gym, but that might not be practical if you do anything else than weight lifting (they don't have any kind of cushioning or arch support etc.).
(15 reacties met lagere score weggelaten)

=== THREAD 34pq1h ===
SUBREDDIT: r/Fitness
DATUM: 2015-05-03  SCORE: 76  REACTIES: 58
TITEL: Squat tip to those of you with flat feet.
POST (source_id=post):
I have been stuck with my squats for ages now and all of a sudden with one simple change my squats got easier and the weight started rising again.

Check your feet's direction. Make sure its lined up to the direction your knees bend.

Mine were only slightly facing out from it due to the normal way I stand. It felt weird to squat with my feet more turned in but OMG it was easier and less stressful on my lower back.

I know this tip seems a little silly but for flat footed people its a big problem due to the collapsed arch

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cqwwi37] (score 70, diepte 0) everyone should squat with their knees following their feet. This is nothing special for people with flat feet.
[cqwywin] (score 15, diepte 0) This can be directed at OP and whoever else wants to read it. OP, it was easier and less stressful on your back once you turned your feet in, because if your feet are  more straight-forward you can generate torque at the hip. With feet turned out, you've already lost the ability to create that torque, so your low back has to pick up that extra force. Our glutes are some of the strongest muscles in our body, and work best through a hip that has been set up correctly. The ideal way to squat, in general, is to set feet slightly wider than shoulder width, feet facing forward (w/maybe the slightest turn out, I mean miniscule amount), neutral spine, head facing forward, not looking up or down. As you go down, keep your knees in line with your toes, feeling as if you're trying to spread the ground with your feet. This creates that torque from your hip that will stabilize your knee and keep force away from your back. After you hit depth, keep that active hip, "spread your knees" while pressing back up, and you're there. Squatting like this will light up your hips (they'll be weak in comparison to your quads), but damn you'll get strong. 

Sauce: studying DPT, biomechanics, worked with D1 collegiate athletes, have my USA-W sports performance coach cert, and I hoist.
[cqx1gum] (score 13, diepte 1) >feeling as if you're trying to spread the ground with your feet.

That's an awesome squat cue for glute activation, I've never heard that one before.

That reads like it's sarcasm but it's not.  I really do like that tip.
[cqwx6ql] (score 9, diepte 1) Truth.

I have flat feet and I've never felt like they were holding back my squat. Lack of sleep, not eating enough, being okay with where I am, and being too much of a pussy, yes, but not my flat feet.
[cqx67ba] (score 9, diepte 1) The difference is that if you have flat feet, pointing your toes out makes your ankle and foot roll inward. Meaning you are putting all this weight on the inside of your foot and on an ankle that's kinda rotated already. By pointing your toes forward you are able to keep your ankles centered. 

Source: had weak arches as a kid and did this all the time when running to avoid the pain that comes with repeatedly stretching out the arch of your foot.
[cqx15nx] (score 6, diepte 1) Ok, take a look at your foot, from the side. You should have a slight arch in the middle. If so, then your feet are normal.

Flat feet occur when this arch is collapsed or non-existent, so when the foot is viewed from the side it's straight. 
Here are some images to show you what flat feet are:


[foot arch
](http://footandankle-bh.com/wp-content/uploads/2014/08/Flat-Feet-1.bmp)


[how feet posture changes due to the lack of arch](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRo4ho5XcYPF_Gsq_dbru-EEad-mWRF1-0quSf4LdcFPykHT5AJ)

[footprint differences between normal feet and flat feet](http://www.pyroenergen.com/articles12/images/foot-arch.jpg)


Also, ffs guys, stop downvoting the poor dude for asking a question. They might've just not known what flat feet are, or English is their second language, or anything else.
[cqwy0oj] (score 6, diepte 0) I'm 6'5" and am constantly shuffling my size 16 flat feet even during the reps.  It's hard to find the right position.  I think the most effective position I've fnd yet though would be similar to what OP describes.
[cqwxadv] (score 5, diepte 0) What are non flat feets? O_o
[cqx4h24] (score 4, diepte 0) Also try practicing short foot. 
http://fitnesspainfree.com/4-easy-progressions-of-the-short-foot-to-keep-knee-and-foot-pain-at-bay/
[cqx5qum] (score 3, diepte 1) 6' 6", I have to point my toes out at 45 degrees out from from facing, and take some wide as fuck stance, and then barely hit parallel. It's rough.
[cqx1vhq] (score 3, diepte 1) Genuine questions: Are you sure this toes forward (and so knees forward)would work for everyone? Don't the various constructions of the hip socket dictate the way you squat? From what I understand if your hip socket is more closed in the front you'd be hitting bone on bone by squatting toes and knees forward and would need to point toes and knees out more and stuff like that, so foot turn out and stance width is different for everyone?

I read about the hip socket thing [here](http://themovementfix.com/the-best-kept-secret-why-people-have-to-squat-differently/). Thoughts?
[cqx4xws] (score 3, diepte 2) Nah you're right. Look at lifters like Greg Nuckols and Chris Duffin: they squat with a crazy wide stance with toes pointed way out. Then look at someone like Kyle Keogh (extreme example). People's squats will look different. You can still engage your glutes by twisting the floor apart on a squat with toes pointed out.
[cqxoxnl] (score 3, diepte 6) Sorry for the late reply but make sure you get your hips opened up before squatting. If you've been feeling more comfortable with out-turned feet, I would suspect you have some hip mobility issues. Google or YouTube the video for "Joe DeFranco Limber Eleven" and do that before you squat. You'll need a foam roller and a lacrosse ball, ideally. Great pre-routine mobility and warm-up work from Defranco. If you have too tight of hips and try to start with feet more forward, you're probably going to have depth problems and I don't want your lumbar spine reversing into butt wink to pick up the extra slack. The catch of having high force production in good positions is that you have to be pretty mobile to start with. Good luck!

Edit: dug through your videos and you're doing a fairly exaggerated low-bar squat. I had high-bar in mind. The biomechanics will change quite a bit. Unless you do high bar tomorrow, make smaller changes to your foot position and stance width, but still mobilize the hips. Each set work towards my description of squat form, but do gradual changes. You'll have to go a bit wider stance on low bar, but your feet should still be more forward-facing, keeping the knee above and outside the plane of the ankle. Just don't want you making a big change and hurting something, which would definitely go against our goal of a healthier squat! Once again, good luck.
[cqxbbos] (score 2, diepte 1) Also I think it's important not to extend your knees past your feet on the descend down. You lose the full motion of your gluteus if you do so.
[cqxaonl] (score 2, diepte 2) Are we doing it right though?
[cqxc9ic] (score 2, diepte 2) Toes should be forward, or just ever so slightly turned out. This is because this allows the ankle to work properly. The ankle is made to move on a specific axis: front to back. Try walking around with your feet pointing outward. Your ankle just lost the name "ankle" because it doesn't work correctly now. It's a hinge joint. Go try to open a door by pulling off-axis. You're going to break it somewhere.

The knees "follow the feet" as someone mentioned above; I like that. The knees can either be directly above the foot or wider, as you're going down. Never inside the plane of the foot though. When your knees come in, this is called valgus knee. It's accompanied by a collapsed ankle. This collapsed ankle will be seen by tracking the navicular bone (of the foot) down, called navicular drop. This is accompanied by tibial torsion, or an internal rotation of the shin bone. This keeps the ankle from working correctly and the knee from working correctly. It also "winds up" the ACL. Which isn't a big problem with squatting obviously, but that's why you'll see ACLs pop during a "plant" and twist move in dynamic sports. Those with flat feet are going to be more exposed to navicular drop and tibial torsion. Long story short, keep the knee directly above or outside of the foot/ankle. If you're not used to doing this, you're gonna feet your hip muscles heating up. Good.

As for the turning out of feet and super wide stances: stand up, assume a super wide stance, pointing your feet way out to the sides. Now externally rotate your thighs (turn your inner thighs forward). Now stop, because you can't. There is a total loss of stability at the hip joint, and this is going to have to be "picked up" somewhere else. AKA the back or knees.

Now, I haven't avoided the hip socket article. What I've told you are all real tangible concepts that apply across all structural differences. That's why I like studying biomechanics. Yes, there are anatomical differences across the spectrum, but physics does not change. Of course there is not a one-size fits all squat form, but there are certain principles that make for an ideal (and joint-healthy) squat. If you have terrible, crappy hip genetics, then you probably aren't going to be very good at squat. If your hips force you to compromise one way, then a different body part is going to have to pick up the slack. Thus, muscle imbalances are born.

Good question, and sorry I cannot address all problems, but like I said: **Biomechanics and physics don't change. Maximize stability and force production, and you will have a safer, healthier, and stronger squat (or any movement).**
[cqxl4jd] (score 2, diepte 3) Just commenting here because it's your more recent comment. I've been keeping my toes pointed way out lately and I'll try keeping them pointed more forward tomorrow.
[cqxlkic] (score 2, diepte 4) Don't expect a miraculous change off the bat, but you should feel more stable through the hip and you'll feel your hips/glutes picking up a lot more of the load versus your legs. Which is good because our glutes are incredible strong muscles. Give it a shot and feel free to let me know what you felt differently.
[cqxloyw] (score 2, diepte 5) Will do! I won't get to squat until quite a bit later tomorrow, but I'll come back to this and reply.
[cqyogop] (score 2, diepte 7) So I tried it out, I definitely didn't like it. It was alright in my earlier sets but as far as my working sets went, I failed one set and struggled with another before I switched back to my usual stance and did it much easier.


As for my width, I'm comfortable with where it's at. I've gone really wide and I've gone narrow, I prefer closer to narrow than wide, despite doing low bar. Just personal preference.
[cqyu8yk] (score 2, diepte 8) I encourage you to work on it. Like I said, it's not going to feel "right" on the first try. I used to squat wider with feet turned out. My glutes didn't activate well, partially from anterior pelvic tilt problems. But I tore down my form, dropped weight and started training with the bar, 95#, 135#, etc. Within 2 weeks of changing my form I added ~60 lbs to my squat max like butter. Was working on hip mobility, glute strength, and overall force production through my hips. I've always been very strong and have legs that make all jeans fit like jeggings. 

For perspective, as a 5'8, 156# 17 year old I squatted 375+, and that was with trashy form and poor programming (coaches had no clue how to program). This was some years ago. But incorporating my hips made my previous squat numbers look like child's play. And I was going ass to grass with my new form, almost bottoming out. I've always squatted high bar and done a great job of showing my chest to the mirror. My lower body was what was bad; weak hips/external rotators let my knees track in at high weights. As a result I had (and still have) giant vastus medialis muscles, but also had pain through my medial meniscus area.

With my line of study I have become hyper-aware of my body positions and my biomechanics. I can confidently say I can listen to my body better than the average cat. This really helped me work out kinks along the way with high success, and I'm thankful for gaining such awareness and knowledge. I've researched several different forms and landed on this one because it has the research to back it. It didn't feel quite right to change at first, but I stuck with it and now it feels effortless to put up what I once maxed out. If you were in my area I would work with you personally to help you out, but that's a slim chance.
[cqyyicq] (score 2, diepte 9) At the risk of being glib: [meanwhile, in China](https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xap1/t31.0-8/p180x540/859835_577024942352334_10881976_o.jpg), meanwhile [in the USA](https://www.youtube.com/watch?v=aziM5wucIHw), meanwhile [in the Ukraine](https://www.youtube.com/watch?v=k2fkma-8KG8) and [meanwhile](https://youtu.be/IqH0_6kH1dg?t=125) in [Russia](https://youtu.be/i9j_B0XVAv4?t=25) everyone is pointing their toes a lot more than "ever so slightly" out.

Those are some of the greatest weightlifters and powerlifters in the world today, and in the case of Klokov, Polovnikov and Lu Xiaojun have received the greatest coaching in the world since they hit puberty.  Why should we trust you over them?
[cqxvlvo] (score 2, diepte 1) I've never been able to do squats without weird grinding and tearing noises in one knee. I did the spreading motion and it feels/sounds smooth as butter. Thanks DPT guy.
[cqydarf] (score 2, diepte 1) Hey man. Before training legs today, I read this post, and I just want to say thank you. I finally feel as though my squat form is correct; I could really feel my glutes and quads working and had virtually no lower back pain. Thanks again dude!
[cqym8pc] (score 2, diepte 2) No, thank you! I'm glad you commented. Happy that all of my studies and practices are being put to use by people around the nation/world. Free information is a movement. Feel free to ask any questions that come up or more specifics.
[cqxagw7] (score 2, diepte 0) Get a good solid pair in insoles. A good pair can support a lot of weight. The top guy on our team squatted 800 last week and about a year ago did 960 in full gear. Including his bw that's 1200 pounds.
[cqxpyft] (score 1, diepte 2) > The difference is that if you have flat feet, pointing your toes out makes your ankle and foot roll inward

If that happens then you need better form.
You should be able to turn feet out and also hold your arch. Do this by spreading the ground, driving knees out, generating torque with your feet. whatever works.

Source: I have flat feet.
[cqxrwgz] (score 1, diepte 3) I agree, i should have said its a tendency rather than something that just happens.
[cqy8onp] (score 1, diepte 3) Okay, cool I find myself extending my knees over my feet pretty often. It's hard for me to not do it I agree.
[cr216ps] (score 1, diepte 3) Well... anecdotal evidence tells me thats the only way I can squat anything heavier than the empty bar with out my low back getting so tight I cant train for at least a week. 

That's just for me though, I really don't want to give anyone else advice for this seeing how much trouble I've had with it.
[cqxawfs] (score 1, diepte 2) Also works great for deadlifts and good mornings. Spread the ground and your knees wont buckle inwards.
[cqymqf1] (score 1, diepte 3) You actually can't to a certain degree though. And the wider you go, the more you force some of the glutes to pull off-axis, minimizing force production. Also, the hip is less stable in wider stances because it shortens up the lateral rotator group. There is a thing called length-tension relationship. Muscles pull optimally at the ~midpoint of their length, and they pull less optimally the further you stretch or shorten. This is why a pull up is harder from a full hang. Also why it's hard to hold an isometric contraction at full flexion. By going wide and externally rotating at the hip, you can't generate much force because you took yourself out of optimal force-production length. Also, you're lengthening the adductors out of their optimal range. I could go on and on. The advantages of going wide are cheating your way out of immobile hips and making parallel a shorter distance from the top, at the expense of force production and proper biomechanics. Just because people do something successfully doesn't mean they couldn't be doing it better.
[cqz8hna] (score 1, diepte 11) Lol.

How much less could you care?
[cr35l0m] (score 1, diepte 12) I really wonder what was said since the post got deleted...Either way I don't really trust this guy's advice because he disregards the fact that everyone has different body structure and he speaks in absolutes. The sign of someone who actually isn't qualified to give good advice.
[cr35qja] (score 1, diepte 13) It was like something like "I could care less about whether or not you trust me or explaining myself to you, I'm sick and tired of people picking what I'm saying apart, blah blah"

Nothing of any relevance or explanation, he just threw a hissy fit.
[cr36bkg] (score 1, diepte 14) Lol that's classic. It just screams "I'm talking out my ass so please don't check my claims for validity!"
[cqxo6da] (score 1, diepte 3) Jonnie Candito has a great [VIDEO](https://youtu.be/R_JSFYdzuLw) on this subject.
[cqz8stx] (score 1, diepte 9) This was beat to death a year and a half ago by Bob Takano , Brendan Murray and Kelly Starrett et al.


Here's a couple of links if you're interested. Although right now it seems like you're more interested in protecting your ego than trying to learn something.

http://breakingmuscle.com/mobility-recovery/moderating-the-knees-in-versus-knees-out-squat-debate

http://www.mobilitywod.com/2013/11/community-mwod-video-the-knees-in-squat/
[cqzu420] (score 1, diepte 10) Thanks for posting those links.
I'm glad somebody else realizes that elite oly lifters *just might* know what they are doing. But doubt some people will insist they are wrong, its bad form, or that its not intentional.
[cqzuwma] (score 1, diepte 11) Yeah, no one on the chinese national weightlifting team ever looked at Lu Xiaojun between the ages of 8 or whatever and now and said "hey bro, you're squatting wrong and making your hips all unstable".


OP is a goof.
[cqztq94] (score 1, diepte 9) Somebody should have told Salimi that he needed a stronger position, when he snatched 214kg - the world record in the heaviest division.
 
There's a fundamental difference between a valgus knee fault for the entire squat, and initiating the movement with a slight, brief, inward movement of the knees. If you spent any length of time studying weightlifters, you'd see its quite clearly intentional. Numerous elite athletes do it. You actually think these lifters consistently have an identical fault on *all* their warm ups, as their heaviest sets? That's frankly absurd.
>The fact that you think that shows me that you don't understand biomechanics well enough for us to have this conversation.

What a terrible attitude. I suppose Bob Takano (USA Weightlifting Hall of Fame) doesn't know enough about weightlifting to converse with you either.

I'm not sure if you are genuinely that arrogant, or you know you were wrong and are trying to bail to save face. I thought the point of /r/Fitness was to help each other and learn something, maybe not.
(15 reacties met lagere score weggelaten)

=== THREAD uhzs8v ===
SUBREDDIT: r/weddingplanning
DATUM: 2022-05-04  SCORE: 23  REACTIES: 58
TITEL: Ladies, how involved are your grooms in the wedding planning? Did they get cold feet? Advice requested.
POST (source_id=post):
We are supposed to be eloping in early June.  So far, I have booked a fantastic  make up artist and phenomenal photographer, found my dress and lost weight (went from a size 8 to a size 2-4)

My fiancé has done zero wedding preparation. No wedding rings have been ordered, no venue booked, etc. He is refusing to help and says things like he can’t decide if he wants to go through with it and none of our family or friends are allowed to attend. 

For a little context, we have been together for 14 years and we have a 10 year old daughter together.

Is this normal behavior? Were your grooms involved in the wedding or elopement process?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[i79es64] (score 267, diepte 0) He can't decide if he wants to go through with it?  None of your family and friends are "allowed" to attend?  Uh, no that's not normal groom behavior.
[i79ny3w] (score 91, diepte 0) >he can’t decide if he wants to go through with it

Ummmmm, I definitely wouldn't continue to plan until this is resolved!!

My fiancé is involved in wedding planning. I am definitely doing more, but he is doing more of other stuff - it's probably 2:1 ratio of the wedding stuff. Other grooms do more or less for various reasons. Many grooms are not interested and don't help which can be a problem that needs to be addressed.

But being involved in planning and wanting to get married are 2 completely different things and need to be addressed separately!!
[i7a4ouf] (score 83, diepte 1) Yeah, that’s a red flag parade, OP.
[i7a6fbk] (score 75, diepte 0) You deserve someone who enthusiastically wants to marry you.
[i7aktyy] (score 41, diepte 3) Please do not book any other vendors until you get this sorted out. Not only for the health of your relationship, but you will likely lose out on any deposits made if you don't proceed with the wedding. I'm surprised vendors are allowing you to book them if you don't have a venue with a secured date?
[i7aa9qp] (score 34, diepte 2 OP) Agreed, my gut it telling me it is a “red flag parade” as well.
[i79zhmm] (score 32, diepte 0) It’s common for some (not all) grooms to not be a big part of the planning process—to not care about centerpieces or linens colors or what song plays when. 

It’s absolutely not normal nor healthy  behavior to “refuse” to help; say “he can’t decide if he wants to go through with it” or not “allow” friends/family to attend. 

He sounds against marrying. (And possibly controlling). Have you talked to him about why? Have you talked with a therapist to figure out why you’re with someone who says such things? 

This doesn’t sound like disinterested in planning (but happy to get married), or normal cold feet…
[i79v3lt] (score 24, diepte 0) My husband was equally involved in wedding planning. The real issue here, though, is your SO saying he isn't sure he wants to go through with the wedding and that none of your friends or family are allowed to attend. That isn't anywhere near normal, and you two need to sit down and figure out what's going on.
[i7aatw3] (score 24, diepte 0) He can’t decide if he wants to go through with it, and you have a ten year old together??? Like if not now, when???? It sounds to me like he does not want to get married at all.
[i79gf40] (score 22, diepte 0) /r/waiting_to_wed

No, not normal behavior...after we got engaged when I asked about possible dates a year out he said "that seems long, surely it doesn't take a year to plan a wedding?"

His reaction made me comfortable to settle on a date 6 months out. In some ways I think bc they sit on a ring and buying a ring, they're usually quicker to accept the major change coming in than the time it takes for the women/proposed to ones to wrap their heads around being engaged.

Anyway, sorry you're going through this, the sub I mentioned has people from waiting on engagement to people dragging their feet for ungodly periods of time after getting engaged. Perspective might help. I know it isn't easy, but if marriage is important to you, you can open yourself up to someone who feels the same way.
[i7abjrg] (score 21, diepte 1 OP) All valid points. I will seek out a therapist this week. I’m starting to realize I may have commitment issues too if I continue to be with someone who doesn’t seem to want to marry me.
[i7ax3s8] (score 16, diepte 3) If you’re not even allowed to invite your family and friends that sounds borderline abusive.
[i7aoh47] (score 16, diepte 2) Honestly it sounds like you need a lawyer, not an officiant. This is highly manipulative behavior -- he is stringing you along to keep you just happy enough to keep a comfortable, familiar status quo. If your goals aren't aligned and marriage is important to you, there are men out there who want that. It's not fair or kind to you to string you along like this.
[i7acq3g] (score 8, diepte 1 OP) Unfortunately, it is the later. He was very excited 6 months ago when he was telling his family that we would be eloping.  Now he seems overly panicked about the thought of marriage. He has said multiple times, in the last month that he wants to be married just not legally— which is absolutely ridiculous seeing as how intertwined our lives are and honestly, I’m not interest in anything less.

Thank you for your response and congratulations on your up coming wedding.❤️
[i7b50nd] (score 8, diepte 2) I feel like you’re just wasting your life with someone who doesn’t really want to be with you.
[i79fch5] (score 7, diepte 0) I have to say not really normal groom behaviour. 

Did you make the decision to elope together? As it sounds like it might not be what he wants?

Just for some context we are eloping in October and he has already organised his outfit, rings and shoes that he wanted. There are definitely details he is less interested in - flowers etc, but there has been no hesitation from him in getting organised. 

It might be time to have a hard conversation to try and get on the same page or go back to the planning stages.
[i7a4g4h] (score 7, diepte 0) I think we need some clarity on a couple things, OP. My fiancé doesn’t want a wedding at all but that is a separate feeling from wanting to get married. He just thinks it’s a big waste of money. We are funding it ourselves and he does not care about any of it. I even picked the outfit the guys will wear because he said he didn’t want to and it’s “my wedding.” But he does want to be married to me. He did just say yesterday he wishes it were a smaller guest list with just his closest friends but not that anyone wasn’t allowed. There is a difference in not wanting to plan a wedding and not wanting to get married. If it’s the former, be very clear about exactly what, if any, decisions he cares to give any input on. If it’s the latter… maybe time to pause and reconsider the entire thing.
[i7ab550] (score 7, diepte 1 OP) Yeah, I don’t think he does. We have been engaged for an entire 10 years and he was “not ready” this entire time. 

About six months ago he was excitedly telling his family we would be eloping in June. Now, nothing but fear and anxiety. 🤷🏻‍♀️
[i7aehmd] (score 7, diepte 0) 🚩This seems to be more than cold feet. I’d have an honest conversation with your fiancé about this
[i7a11nn] (score 6, diepte 0) Not helping in planning is more common than it should be, the rest? Sounds like there is some big stuff brewing in his head
[i7aacuf] (score 5, diepte 1 OP) This was so helpful, thank you for the perspective.
[i7bx5p5] (score 5, diepte 2) Happy to hear you’re reaching out to a therapist and wish you the best OP!! You deserve to be treated with love and respect
[i7b5d5r] (score 4, diepte 2) I think you’ve gotten good advice, and I agree with all of it. I hate to freak you out more, but if hes concerned about the legal aspect alarm bells would be ringing in my head that he has something weird going on legally or financially in his background. Something related to a past arrest, or a mountain of debt? I would think really hard about marrying this guy, and have some serious frank conversations. Possibly do your own digging. Who knows, maybe something happened years ago he doesn’t want you involved in, but maybe hes blowing money on a secret credit card, I just don’t know but would be really worried about that. Of course, thats super extreme, so don’t freak, I have no context and don’t know the guy. Just something to think hard on before you sign anything.
[i7ajowv] (score 3, diepte 2) I'm so very sorry you're going through this. 

I also have an idea of what it's like to feel stuck in a relationship - or feel like you want to make it work because it's what you're used to. Hearing this and looking back at some of my own past mistakes, I recommend you find a therapist you trust and start seeing them regularly; and get away from this guy, *at least* for now. 

If he hasn't been ready for 10 years, if he is saying these sorts of things to you, he isn't going to ever be ready because it's not what he wants. You and your child deserve much, much better.
[i7ahfy5] (score 3, diepte 0) Nope nope nope nope nope absolutely not normal or okay. The next thing you plan really needs to be a relationship counselor, and nothing else.
[i7b4zte] (score 3, diepte 0) Not once has my fiancé said anything remotely close to not being sure he wants to go through with it, and honestly if he did say that, I’d cancel the wedding. There is a difference between panic about life changes (which we both have) and being unsure about wanting to get married. 

Also, I chose my fiancé because he does (honestly usually more than!) half of the emotional and physical labor in our relationship and home. It was incredibly important to me not to marry a man who felt comfortable making the other person in his relationship do all the work. I consider wedding planning a kind of test to see how two people work together in stressful situations. It’s fine if, in a relationship between a woman and a man, the woman is more interested in wedding details. It’s not fine if the man doesn’t take equal *responsibility* for the wedding. 

So no, what you’re describing is not normal behavior. It’s the behavior of someone who either doesn’t want to get married or is deliberately hurting you.
[i7bfqq6] (score 3, diepte 0) My fiancé hasn’t done much but if I ask him questions he’ll answer and give me opinions. (Another reason he doesn’t do much is bc I think I’m a control freak and NEED to d everything myself) 

I think the refusing is a bit red flaggy And his “can’t decide if he wants to go through with it” thing? I think he is just too comfortable with having you as his “side piece” without commitment. He needs to check himself. I hope for your sake he figures his shit out. :(
[i7bh0dy] (score 3, diepte 0) The fact that he said he isnt sure if he wants to go through with it is a major red flag. 

My fiance has been helping with the wedding preparations. However, I have been doing most of the planning. He will ask me from time to time what else needs to be done for the wedding. His immediate family are coming and they've invited some of their relatives. 

I'm sorry you are going through this. You guys have been together for a long time and have a daughter together. To me, it seems like he doesn't wanna get married. You deserve much better. Have a serious talk with him and decide from there. All the best!
[i7bzyqe] (score 2, diepte 1) Agreed. What OP described are major red flags and not just a groom being disinterested in wedding planning.
[i79o6jn] (score 2, diepte 0) I’ve done the vast majority of the planning, but I am a chronic over-planner with anxiety and our wedding is going to be fairly casual so there’s not a ton of moving pieces to coordinate (the only real vendor we have to deal with is our table/chair rental - everything else is either being handled ourselves or by family/friends). And in my fiancé’s defense, if I give him a task he does it, and if I ask him to help me make decisions he’s happy to. He’s just also totally fine letting me come up with the ideas (about the only thing he really wanted was that one of the wedding colors had to be blue, which I had expected long before we ever even started dating). Really, he’s just so happy we’re getting married that he doesn’t particularly CARE what we do or what things look like as long as we get to get married and celebrate with people we care about. 

Saying he can’t decide if he wants to go through with it and refusing to help and refusing to have anyone you care about attend? That’s definitely not what I would consider normal and I think you need to have a serious talk with your fiancé over whether or not he wants this marriage to happen at all.
[i79vlip] (score 2, diepte 0) My fiancé is somewhat involved.  I’m doing most of the major planning but he does give opinions and help when asked.  
Refusing to help and questioning the wedding doesn’t seem normal to me.  Unless he is questioning an event vs courthouse.
[i7a9vqt] (score 2, diepte 0) I'm doing everything by hand so there isn't too much for my fiance to do, but he's constantly asking what he can do to help take the stress off of me. He gives input and helps wherever he can. Even if he can't help at the moment, he usually hangs out to keep me company.   By reading these other comments though I sound lucky.
[i7anej8] (score 2, diepte 2) It’s not fair of him to play with your emotions like that, regardless of reason. Is pushing back the elopement an option? You should have no fears going in to a marriage. It’s too risky, especially with a child. I would definitely work through this in couples counseling before making a commitment, and that doesn’t have to be a bad thing. He may need to work through some deep stuff, and it’s always best to uncover it beforehand since the outcome can be unpredictable.
[i7alkck] (score 2, diepte 1) To elope is a bit of a dated term that in past referred to secretly running away to get married typically without close family and friends knowing. Now it's more of a broad term for a small wedding.
[i7am1pl] (score 2, diepte 0) I think it’s normal for grooms (at least mine) to not be extremely excited about wedding planning / not be as involved as brides.  However, it is certainly not normal for them to be doing so because of the reasons he stated.  Sounds like you guys need to have a discussion and re-evaluate the wedding plans.
[i7ambwf] (score 2, diepte 0) Ugh first off, I’m sorry he’s not stepping up! My fiancé has done a lot through the process with me. 

Edited: original post after reading comments as I believe this is deeper than a disagreement on a wedding, it’s a disagreement on a marriage which is a bigger conversation to have. 

I stated this in another comment but please do not go in to the marriage with these types of feelings, whatever you do. It doesn’t mean you need to break up necessarily. I’m sure you’re eager to get married after all this time but it’s not worth it if he’s still feeling like this. Everyone deserves a partner who wants to marry them. He needs to work through his commitment issues, and that’s up to you if you’re willing to work through them with him and to give it some more time. 

Best of luck to you. 💕
[i7ar9ym] (score 2, diepte 0) This is not normal behavior. My groom is extremely involved. Our original big wedding was postponed due to COVID; he still helped plan our legal elopement ceremony, and has since been an equal partner with planning the traditional reception. Sure, we are stressed about wedding planning, but the behavior you are describing is different. Does your partner even want to get married?
[i7bf0at] (score 2, diepte 0) This is not normal behaviour to me. Me and my fiancé have split wedding planning almost equally. Decided everything together, except each other’s outfits. We are now 4 days away and both eager for the day and both checking weather forecasts daily
[i7bfhyp] (score 2, diepte 0) I would talk to him and be honest about what you’re feeling
[i7blvli] (score 2, diepte 0) He cared about the venue, the food, the music, and the transportation. Well he didn’t care about the transportation but he got stuck with it. Between what he really cared about plus the weight of a perfect wedding from his family (and in turn, me), he had to have skin in the game. I did the research for venue/food/music but we both went to explore, and I handled florals, photographer, decor, and save the dates/invites. I can’t remember what else but I was pretty happy with his level of investment. We only had spats over the rehearsal dinner because his family wanted it to be basically a pre-wedding with everyone invited, so he had to shut that shit down lol
[i7br8az] (score 2, diepte 0) Not wanting to be involved in planning is one thing, but saying he can't decide if he wants to go through with it, and not "allowing" friends and family to attend is a completely other thing. My husband didn't want to be involved in planning other than helping me make decisions on things like food to serve, etc - and I was OK with that - but he never made comments that made me question whether or not he was having cold feet
[i7abvz5] (score 1, diepte 1 OP) We did make the decision to elope together, he has very bad anxiety so a full on wedding would be very hard on him.

I appreciate your providing context on what a normal elopement looks like. It is good to know that your groom is organized. Also, as a side note October is a great month for an elopement!
[i79jtdi] (score 1, diepte 0) it definitely happens that one person isn’t excited about weddings or the wedding planning process. however they should willingly help contribute if it’s too much work and you ask. but definitely red flags about the “i’m not sure” (if he’s referring to having a wedding at all or just being married???) and it’s in june. you need to talk about your joint life vision and be on the same page. sending you best wishes and a tight hug!
[ibo6vei] (score 1, diepte 2) What ended up happening?
[iboz9kx] (score 1, diepte 3 OP) He decided he hates the idea of marriage and we are still figuring things out. It has been painful to say the least.
[ibpn8ls] (score 1, diepte 4) I am sincerely so sorry you are going through this
[ibwy1fo] (score 1, diepte 5 OP) Thank you. ❤️
[i7a9tlk] (score 1, diepte 0) As everyone has mentioned, him saying he doesn’t know if he wants to go through with it is a giant red flag 🚩. My fiancé is enthusiastic about planning (though I’ve definitely taken the lead) and consistently talks about how he’s excited for our wedding and can’t wait to marry me. He goes to all our planning meetings and is very involved in decision making. I do a lot of the research and then we make the decisions together. And he’s taking lead on the honeymoon. 

You’re supposed to be eloping next month without a venue or people knowing date and time? That feels like it’s cutting it close. 14 years is a long time to be together for someone to say they can’t decide whether they want to go through with it, not to mention you have a child… I’d talk to him about this ASAP and get clarity on whether you should be moving on.
[i7agkzu] (score 1, diepte 0) My fiancé hasn’t done any planning because he owns and operates his own construction business and works every single day. I work for him helping him do stuff for his business, so I have a lot more free time to do the planning. It’s not that he isn’t interested, but he has to work a lot to keep his business running so it truly doesn’t bother me at all. I know this may not work for everyone but we have been together for 5 years and it has worked for us.
[i7ah1ja] (score 1, diepte 0) No that is not normal. My fiancé can be a bit hapless at times but he asks how to help regularly. He often expresses excitement/anticipation for the day.
(10 reacties met lagere score weggelaten)

