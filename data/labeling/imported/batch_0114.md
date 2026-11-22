# Label-batch batch_0114

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
Schrijf het resultaat naar `batch_0114.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(3 threads: 1g6xchx, zr5zko, 5pvgn6).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 1g6xchx ===
SUBREDDIT: r/loseit
DATUM: 2024-10-19  SCORE: 34  REACTIES: 119
TITEL: Plantar fasciitis won't freaking heal
POST (source_id=post):
It's been probably more than a year now and my dang foot won't heal. It's only in one of them. I've tried every single sole there is, every brand of workout shoe, inserts etc. 

Resting is not an option. I won't stop working out and I walk about 10k steps a day minimum. I have 3 dogs so I can't stop doing that. I lift heavy and don't want to stop.
I have a Spartan race in a month and was going to start running again to set myself up better. But I'm scared to. Right now it feels worse than in a long time, it normally goes away with activity, now I can feel it when walking. 

I've lost 50 pounds and still need to lose 40, I know that it plays a part , but it takes time and I can't rush it. 

Any ideas for this? I'm stubborn as hell, but it's been over a year. It has to heal at some point?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[lsmcitr] (score 97, diepte 0) Do not walk barefoot around the house if you are right now. That exacerbated mine so much. I also like the Oofos slides.
[lsmdvrh] (score 63, diepte 0) I had plantar fasciitis so bad for 8 months that I honestly wanted to pursue a surgical fix. The only thing that helped was resting (less than 2000 steps per day) and PT for 3 months. 

Now I am fully healed and just keeping up with preventative measures.
[lsmebtf] (score 46, diepte 2) Visit the r/plantarfasciitis sub for more tips
[lsn8com] (score 44, diepte 0) It won’t freaking heal because you won’t let it. 
Your body can’t repair itself if you keep irritating the damaged area.  You need to rest it. If you’ve caused permanent damage, things can get a lot worse. 

If you are going to remain active as a lifestyle, you are going to have to learn how to navigate injuries, my friend. Which includes rest.
[lsn2xsv] (score 34, diepte 2) Sorry...healing not an option then.

Tendonitis requires rest to heal.

I've been the dumbass who doesn't want to believe it.   Keeps pushing it.   It won't go well...
[lsmew81] (score 34, diepte 0) You are stubborn and stupid if I may kindly say so. I recognise it because I did stuff like this too.

Used to run about 200km a week along with plyometrics (which included things like box jumps, lunge jumps, burpees, lots of impact on my feet), lifting weights and did not want to stop as I had sporting goals. Developed on and off pain.

What helped:

Learnt to stretch my feet, ankles, calves first thing when I got out of bed every day.

I use Lightfeet socks to cushion my feet, I swear by these.

Learnt to tie my shoelaces correctly for my foot and arch type, narrow feet.

I had already years before that done coaching that included fixing my gait so that was actually good - includes video study and correction, not sure what your gait is like.

Reworked my schedule and reduced plyo replacing with an additional weight lifting session that did not trigger the plantar fasciitis pain at all, reduced my incidental walking (I walked to and from work, to and from training - so cut that down and let go of some of my ego).

Built in a bit of skipping in my routine as that strengthened the front of my feet and also doesn’t land on the heel (balls of the feet) so again avoided the PF pain.

Haven’t suffered from it in years.
[lsmu3lj] (score 29, diepte 2) Seriously? Lol. Buy some Hoka flip flops and stop hurting immediately.
[lsmqcid] (score 23, diepte 2) I’ll just add that there is a brace made for that which I would wear during the night while I slept.  It helped a lot.   I got it off Amazon.  Best of luck.
[lsmidc1] (score 23, diepte 0) Mine only healed after I completely rested it for like, several months.  Kept steps to less than 5000, stopped squating and deadlifting (did leg extensions, curls, and cable pull through instead).   I also had to buy new shoes, finding a set of sneakers that worked well for me (sketchers arch fit. Very very padded, made a huge difference). I also found some super padded slides to wear around the house.

I’m serious on the rest thing. Every time you are on your feet long enough that they hurt, you are irritating that tissue and prolonging the cycle of inflammation and irritation. I kept resting for shorter periods, would feel a bit better, then pissed them off again when I went and became active again.

Even now I try to mix up my walking with time on elliptical machines to give my feet a rest.
[lsmchlh] (score 21, diepte 2) You realize you can fully rupture your fasicia if you don’t allow it to heal right?
[lsn21d2] (score 21, diepte 6) It makes it impossible, until you can't walk anymore..what then?

Suffering from something similar btw - walked 10k steps in bad shoes for 2 years to compensate for lack of exercise, now one of my feet hurts when walking. But according to the docs, it's not Plantar fasciitis.
[lsmeh28] (score 20, diepte 4) I bright it up because of your reluctance to reduce your foot activity.
[lsnvt0d] (score 17, diepte 4) Your attitude stinks frankly, there's no miracle cure or medicine. You need it to heal by resting, if you don't rest, it doesn't heal. Simple as. Cop on
[lsma5qv] (score 13, diepte 0) Maybe redirect your exercise to something not foot-based? Or see what your doctor advises if you’re game to get medical advice. I know walking is fantastic exercise, but there’s other options if you’re in pain from doing walking/running specifically, like swimming (if you have pool access).
[lsougsk] (score 11, diepte 2) Unfortunately it’s just not a “play through it” injury. It WILL. NOT. HEAL. If you just keep walking on it. When mine acts up I start biking more for exercise than walking.
[lsmoil8] (score 11, diepte 1) This is really good advice. While I was mending my knees and losing weight I suffered through tendonitus. For me it was the only avenue because I HAD to lose this weight. But someone in a not so state of emergancy, rest and PT is really a better path, and some sort of diet strategy like OMAD or whatever to get you through. I didn't have a medical emergancy btw, just I was in and I knew I had to finish or I probably never would. I managed to suffer through and the tendonitus did heal, but with zero help from me in the middle of it unfortunately.:)
[lsnvibr] (score 8, diepte 6) So what’s the plan if it completely goes and you can’t work or walk the dogs at all?
[lsnynp5] (score 8, diepte 3) Wearing a brace and stretching for months made mine go away
[lsmrtwl] (score 5, diepte 0) I’ve had this off and on my whole life. Best thing for it was getting a good quality physical therapist. Which was hard to find. 

Stretching is really important, as well as massage of the arch. You can get a night splint and try it, or just pull your toes back using a blanket or towel. Inserts and basic exercise is not enough. You need exercise specially for this involving strengthening the feet all the way up to the legs
[lsmabin] (score 4, diepte 0) Do you wear a stability boot to bed? That's the only thing that finally got rid of mine when I had it. It still took months for the pain to subside, but I've been back 100% now.
[lsobup6] (score 4, diepte 2) Yep, definitely this. I was always barefoot for many, many years. My podiatrist told me to stop it. I wear Oofos, and now that it's getting colder I got some slippers from Orthofeet. I also have one of those funky stretcher boots and it helped a lot when things were much worse.
[lsmedth] (score 4, diepte 3 OP) Thank you!
[lsoqz57] (score 4, diepte 2) One of the things that helped me the most was stretching a couple of times a day.   Stand on a stair and lower your heels and stretch those feet.
[lsol6vw] (score 4, diepte 1) Agree. I had it pretty bad with regular moderate exercise every day. Then I got lazy for 2 weeks, then got sick and mostly bed-ridden for a week and it was gone. Jogged a half-marathon on the next day, felt awful for 2 days,  but no plantar fasciatis still. So yes, rest was the answer for me.
[lsmffpn] (score 4, diepte 1 OP) Yeah i know, and I can take that. 

Thank you for all those ideas, I will try them all!
[lsmhyo6] (score 4, diepte 0) Stretching daily basically an achilles/calf stretch), custom orthotics from the podiatrist are better than over the counter, stop going barefoot - wear at least slides at all times, cut out running and high impact until it heals up. There’s also a boot you can use at night to keep it in the right position that helps. Walking reasonable distances wasn’t an issue for me.
[lsmk2om] (score 4, diepte 0) One foot, eh?

Do you have back, hip, or knee pain? PF can be a symptom of a problem elsewhere.

My pf was caused by arthritis in my left hip. I needed 5 weeks of consistent hip, core, and glue exercises before my foot started feeling better.

It’s important to keep in mind that most of us walk on flat, hart, and straight surfaces. This can allow for muscle imbalance where your thigh muscles are tight and over trained and your hips, glutes, and core are under trained. Aside from adding exercises, do add walking sideways, backwards, on soft uneven forest trails, or sandy areas to rebalance, if you are not doing so already.

A massage gun can help too for any calf or hip tightness or if you feel a bump on the bottom of your foot.
[lsmknss] (score 4, diepte 0) I've aggravated mine recently and except for this week when I can't avoid walking, I've just switched to my bike.  It's not possible for everyone or for every circumstance but I find that if you can't rest then the best thing is to switch to activity that doesn't make the problem worse.
[lsmiwr1] (score 3, diepte 6) Definitely pricey but so well worth it. After about a year and a half of pain, I’m pain free now.
[lsmbobw] (score 3, diepte 2) I got mine on Amazon.  It basically keeps your foot at a 90 degree angle when you sleep.  I don't remember the exact science behind it but I think my pain was caused when the tendons at the bottom of my foot would retract. The boot helps keep them stretched supposedly helps fix the pain.
[lsml6gb] (score 3, diepte 0) I'm kind of surprised so few folks just said "see a PT/doctor" but I would start by seeing a PT/doctor. ideally a PT that works with people who train - I had a guy who worked specifically with powerlifters/bodybuilders, and working with somebody who can speak the language is really helpful.

there are a lot of possible causes, could be downstream of some kind of tightness/issue other than your feet that your feet are compensating for. but having somebody take a look and determine what is causing it is really important, otherwise you're just going to keep reinjuring it over and over.

i don't think you'll need to compromise lifting/walking but things like spartan races/other hard peak-performance events are probably a bad idea. depends on what irritates it, when I had mine it was just high-impact stuff.
[lsn1dea] (score 3, diepte 0) I had it for a long time and was in constant pain.  Finally found a good PT, and actually did all the exercises. Every day. 

I also switched to barefoot minimalist shoes (zero drop, wide toe box, thin sole) and I will never go back to regular shoes again. I thought the PT would object but funny enough, nearly everyone working at the PT office I went to were also wearing them and were really supportive.  When I’ve tried to wear my old shoes my foot will start to hurt, so they’ve all gone in the trash. They’ve also helped my balance.  I used to have times when I’d roll my ankle or fall for no good reason, and with the thin soles I can feel the ground and haven’t had any issues in the over a year I’ve been wearing these shoes.  It’s opposite what you normally are told but I’d highly recommend giving them a try. I like the Vivo Barefeet or Xero Shoes.
[lsnrl7l] (score 3, diepte 0) PF is usually from tense calves. Try stretching your calves and massaging them from back of the knee to the ankle using lotion. A smooth stick to massage would be of great help. maybe put your feet in warm water in addition.
[lsm9tf9] (score 2, diepte 2) Yes. Life changing.
[lsmahrs] (score 2, diepte 4) They take a few days to break in and then ahhhhhhhhhh. Good luck to you!!
[lsmfqz7] (score 2, diepte 4) Not to sound like an ad, but just want to give a shoutout to oofos too. Switched to wearing oofos slides whenever home. This helped me more than stretching or using a night splint. I also put orthotic support into all my shoes and I think that helped as well, but I credit oofos helping the most.
[lsobxw6] (score 2, diepte 6) Hooray! I'm excited for you. I will say, I size down as I think they run big! Everyone's foot is different though :) I've never worn the sneakers.
[lspdjen] (score 2, diepte 6) I'm dealing with capsulitis in one of my feet right now. The only thing that helps is resting the foot completely. I've been in a walking boot for almost a month and have had to forgo a lot of activity, but I've gotten a lot better. You're going to have to make some sacrifices if you want to heal. There's no magic fix.
[lsmclbk] (score 2, diepte 1) This is the way make sure you get one that goes up your leg to the calf. It's annoying but mine helped within like a week.
[lsopszq] (score 2, diepte 1) This was the only thing that worked for me. 

It was explained to me this way about how your foot heals at night… If your foot is in the normal, relaxed position the tendons heal but the tears are short. When you get out of bed on the morning, they stretch out and tear apart again. If you sleep with your foot contracted in the boot, the tears are longer when they heal. 

It worked but it was miserable trying to fall asleep the first few nights.
[lsmcq8j] (score 2, diepte 1 OP) Guilty, I will stop doing that. Thanks
[lsnveo6] (score 2, diepte 3) Do you have a link to something like the one you used? I bought one recently on Amazon and it was absolutely useless, I had total movement, was more like a sock
[lso9jto] (score 2, diepte 4) I just went on Amazon to see, and I didn’t see the one I have.  That said, if you look up “plantar fasciitis night splint”, you will see a lot of good options.  The purpose of the splint is to prevent you from flexing your toes downward, which is what causes the problem.
[lsmeq2s] (score 2, diepte 4) Any time! And good luck! Google “rathleff protocol Reddit” for a really good foot strengthening regimen.
[lsptxbm] (score 2, diepte 3) Doing a tennis ball roll a few times a day and wearing a boot at night to keep tension in my foot with my toes pointed up. I've trained my feet now to keep my toes pointed up under the blankets vice down which I feel has kept mine at bay.
[lsrafxm] (score 2, diepte 1) Yea, I had plantar fasciitis and after trying everything for over a year, it healed on its own when I broke my fibula and couldn't walk for 3 months.
[lsmeyoy] (score 2, diepte 1 OP) Ha! I need to try that. They are so ugly, but I can't work past that if they are comfy lmao. Thank you!
[lsmf886] (score 2, diepte 1 OP) Just ordered one from Amazon per another users recommendation, I'm excited to try it!
[lsmfc4x] (score 2, diepte 2) Great. Good luck dude!
[lsmkure] (score 2, diepte 1 OP) You might be right, knees are bad and already had surgery. I know i probably tore something but let it heal and it works decent now. But I might have been overcompensating without thinking about it. I will definitely add more mobility and be more conscious about that. I'll buy a massage gun. Definitely have tight legs.
[lsmqg16] (score 2, diepte 0) Have you been to a podiatrist / chiropodist? My plantar fasciitis was very stubborn but responded to electroshock treatment. More conservatively, a podiatrist can also custom make orthotics for your actual feet - the over the counter ones really don't do much.
[lsnf4gp] (score 2, diepte 0) Physical therapy. ASAP. 

I had terrible PF. They did this really intense massage, which really helped, and also diagnosed an issue with hip weakness that exacerbated the PF issue! Doing the hip exercises, the massage, plus religiously wearing supportive shoes (in the house too), cleared it up b
[lsosd90] (score 2, diepte 0) Change your shoes,
[lspwtpc] (score 2, diepte 0) I dealt with this, and it was frustrating because long walks were my primary exercise and mood regulator. Unfortunately the only way I was able to heal is to stop putting prolonged weight on it for about 2 months. I did this by exclusively wearing Oofos and by getting a gym membership so I could use the stationary bike. The pain went away after 2-3 months, but there’s always a chance of recurrence so I’m careful about wearing good shoes.
[lspxtwj] (score 2, diepte 0) You don't say that you're stretching. Look up stretches for plantar fascia and Achilles tendon. Freeze a bottle of water and use it to roll under your feet to stretch and relieve the pain. Stretch stretch stretch.
[lspy32i] (score 2, diepte 0) You should see a podiatrist and get custom insoles.
[lsql5vr] (score 2, diepte 0) I had plantar fasciitis for around a year and a half and nothing seemed to work. I eventually fixed it by going to a physio for dry needling in my calf at first and then a few sessions with a RAPID neurofascial reset massage therapist (after that maintained the massage on my own). Pain is completely gone and I'm back up to 10k steps a day.
[lsqzvcl] (score 2, diepte 0) It's only going to get better with rest and time for healing. You're actvely making it worse by continuing to walk on it. I had a really bad case for like a year that only got better when I started doing PT exercises and resting and soaking my foot in warm water baths. Losing weight has helped, but rest and self care were the main things.
[lsm9myl] (score 1, diepte 1 OP) Nope, I'll look into it. Did it work for you?
[lsmgdqn] (score 1, diepte 5 OP) Yeah I just ordered the slides,  I sized one up because the reviews said they might run small. I'm stoked about trying them! Looks like you're walking on a cloud. 

I'll wait for the next paycheck for the sneakers,  they were a little pricier haha.
[lsmau56] (score 1, diepte 1 OP) Nope haven't tried that, where did you find it?
[lsmbxz3] (score 1, diepte 3) Doesn't look like the one I bought is listed anymore but here's something similar. 

https://a.co/d/8JMfnEn
[lsmc04q] (score 1, diepte 3 OP) Ok cool, I found it, looks weird but I'll definitely try it!
[lsmeoiz] (score 1, diepte 0) I had it in just one foot also for well over a year. So freaking painful!! I started stretching exercises several times a day and instead of wearing slippers or flip flops around the house I started wearing crocs. The crocs were really the game changer for me. Funny because I used to make fun of people who wore them but within a month it had gone away. My sister who also had it ended up having to get shots in the bottom of her foot but I got her wearing crocs around the house too. 😂 Just never walk around barefoot and if your everyday shoes don’t have a lot of support get some inserts or better shoes.
[lsmg38j] (score 1, diepte 2) They most definitely are but they have a type called literide and that’s what I started out wearing. Smaller holes and not as ugly. Very comfy!!!
[lsmeowx] (score 1, diepte 0) man, that really sucks. plantar fasciitis can be such a pain, especially when you’re super active. it might be worth seeing a doc or a physical therapist to get a fresh take on it. maybe doing some low-impact workouts could help you keep moving without making it worse? sounds like you’re super dedicated, but sometimes it’s okay to ease up a bit to let your body heal. you got this, just don’t push it too hard before the race
[lsml2oi] (score 1, diepte 3 OP) Haha! Dang! Yeah you're right. I'm pretty good at looking past pain, to a fault probably. This is just obnoxious.
(59 reacties met lagere score weggelaten)

=== THREAD zr5zko ===
SUBREDDIT: r/weddingplanning
DATUM: 2022-12-21  SCORE: 0  REACTIES: 119
TITEL: A cold feet thread. Curious if it's something of a red flag, or just normal.
POST (source_id=post):
[deleted]

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[j11tthg] (score 202, diepte 0) As someone who does not want kids, there is no compromise on this one. And kids deserve to be brought into a home where both parents actively want them. The rest of the stuff I can't speak on but the kids thing is 100% either yes or no and both parties NEED to agree before marriage. If she definitely wants them and you don't (which is fine and a good thing to know about yourself) then don't marry her. It won't end well. I'm sorry 😔
[j122dxb] (score 98, diepte 0) Honestly? I’m not hearing a lot of love coming through. It sounds more like you’re in a comfortable relationship and you’re just taking the next logistical step you think you should take. Not that you’re madly in love and can’t wait to build a lift together. And if this is how you feel now, imagine how you’ll feel 5 years from now, 10, 20….usually the wedding is the happiest you’ll be, in a way…

The kids thing is definitely something that needs to be discussed. Having kids and resenting them/her or not having kids and her resenting you aren’t great paths. I never wanted kids and my fiancé can’t have kids, so together it’s perfect, in a way. No resentment. No what ifs. 

While you sound a little shallow about her body. I’ll give you the benefit of the doubt. My fiancé was a SEAL so fitness is obviously important to him. I’m not the thinnest girl, but I love to go for hikes, swims, kayaking, etc with him. It’s a big part of our lifestyle compatibility. 

These sound a little more than just the basic cold feet/wedding jitters and more like you really don’t want to get married to her. You should definitely talk with her.
[j12mh3x] (score 82, diepte 0) I know there are a whole slew of issues here but I’m just stuck on the fact that OP is bashing her for being 135lbs at 5’ 4’”. A completely normal and healthy BMI. Yikes. Like sorry she’s not a rail thin model and that’s a reason you’re hesitating to marry her. I’m really really hoping that the only reason you’re mentioning that is because you’re projecting from the other incompatibilities you mentioned that are very reasonable. You can’t compromise on kids. 

Your comments imply that you love her because of what she does for you and not who she is. 

Please leave her she can do better.
[j121hsz] (score 80, diepte 0) It sounds like if your fiancé is willing,  you should postpone the wedding and go through premarital counseling (and probably individual for yourself as well). I wouldn’t throw away 5 years because of something you’re not completely 100% sure of, but you need a professional—not redditor opinions—to help you and your partner have these difficult conversations, see if that process restores intimacy, and come to a conclusion about how to move forward.
[j126e17] (score 69, diepte 1) It's absolutely insane to marry someone who wants kids when you don't. Have you talked about it? Is the plan to just have them anyways??
[j1208z7] (score 69, diepte 0) Call off your marriage plans.  The kid issue is a deal breaker.  Then, you both deserve to be with people that you find physically attracted to and want to have a close, physical relationship with.
[j11vben] (score 68, diepte 0) This doesn’t seem like a relationship that is going result in a happy marriage. What’s really scary about it is that it seems like it’s completely stagnant, and there’s a possibility that you’ll be in a loveless, sexless marriage because for years because it’s convenient and there’s been no “real reason” to split up. I can see you both dumping years of your lives down the drain in this marriage before realizing that you could’ve been much happier with other people. Your two main concerns are big red flags. The kid situation is very serious, and one of you will end up unhappy either way. Your second reason, to be frank, seems very disrespectful towards her and I wonder how much you actually care about her if you’re considering calling off a marriage because her (completely normal) body isn’t good enough for you. I hope you make whatever choice is best for you.
[j1229xy] (score 67, diepte 1) Agreed with all of this. I’m also frankly confused by a 5’4 person at 135 pounds being suggested as too big/not putting any effort into taking care of herself. Like sorry, it isn’t a health concern to be at a normal middle of the road BMI for your height. 

Obviously every body is different, but I am 5’5 and 135 pounds and my doctor says I’m at an ideal weight. I wear a size 2-4 and have a 25 inch waist. I would have some major issues if my partner suggested I should be smaller.

Love should not be conditional on having a perfect body. You can definitely have legitimate health concerns if your partner is not at a healthy weight / has health issues, but I am really skeptical you’d have legitimate health concerns at that BMI... (Not that BMI is a perfect indicator). You can also of course have different interests and want to share a specific interest in fitness or whatever activity with your partner, but it doesn’t sound as if that’s really what OP is saying by focusing on her height and weight rather than any past activities they previously enjoyed together.
[j11uz86] (score 54, diepte 0) Having kids vs not having kids is a huuuuuge challenge you both will face. I personally watched a marriage crumble because the wife had no interest in having children but the husband wanted them. The husband just thought she’d eventually change her mind. Everything else on your list is not something I’ve really dealt with but the amount of times I’ve heard “you guys need to discuss children before getting engaged” before my fiancé & I got engaged was unreal. It’s a huge deal.
[j12sfb1] (score 53, diepte 4) *if men just went to therapy they wouldn't feel the need to lead us on for half a decade*
[j12eh70] (score 42, diepte 2) Oh well. They can still travel and have a vacation if they’re traveling. No need to get married because it’s more convenient for the guests lol
[j12qrc6] (score 38, diepte 1) Yup, and equating thinness to "health" is a load of issue he's pushing onto a future daughter he doesn't even want.
[j123mx3] (score 36, diepte 0) Don’t do it! You don’t seem excited to get married to this person and it shouldn’t be something you feel “meh” about. She deserves someone who is THRILLED to marry her, and so do you! Your gut is telling you that you don’t want kids and that you aren’t that attracted to your partner…listen to your gut before you end up in a life that you don’t want. I’ve been in a relationship with some similarities to yours and I am so glad I ended it and waited for my husband.
[j11wn2y] (score 32, diepte 0) How old are you and how long have you been together?    

All I can say is that a disconnect on kids is a lot more than cold feet.  This is the one issue that is fully black and white with no room for seeking common ground.

The other thing that is more than cold feet is the intimacy issues.  20 years down the road, fine.  But a couple about to marry?

Tbh, this isn't promising.  At the end, you're basically asking if it's possible for you to change who you are and what you want.  Again, this just isn't how someone about to be  married should be talking.  

I don't know.  If you have a close friend who knows both of you, maybe talk it out and get their take.
[j12m9of] (score 32, diepte 2) I want to point out that 135lbs at 5’4” is a healthy BMI.  While on the high end of healthy, it is healthy and not overweight, and there are plenty of active and healthy people at that height and weight.  Now overall compatibility based on lifestyle choices relating to diet, exercise, & fitness might be something you decide is a deal breaker.  But as others pointed out, the real red flag is the kids thing, knowing your finance wants kids.  Women can't keep putting off having kids, we literally have a biological clock.  It would be cruel to marry a woman in her 30s who's made it clear she wants to have kids, only to refuse once married, or lead her on into thinking you'll want to have kids "someday."  Someday will either never come or it may be too late to have kids because her fertility has declined too much.  You will literally be wasting her fertility if you marry this woman knowing that you aren't committed to having kids.  I'm 35 and just got married this summer, and we've been trying to conceive now for a few months and it's HARD.  Tracking ovulation & timing sex isn't easy, and for fertile couples, there's really only a 20%-30% of conceiving any given cycle with perfectly timed sex.  So you may think you've got plenty of time to figure out if you want to have kids, but there may not be for her.
[j12bv8r] (score 30, diepte 2) Differing opinions on whether or not to have kids is a major relationship dealbreaker. And being in your 30s, this is bound to come up REALLY fast.  I’d be very surprised if your partner isn’t pushing to try for kids shortly after your wedding day.
[j12lq58] (score 30, diepte 4) It doesn’t matter if he’s looking for an excuse or not. If he’s this unsure and there are these many issues, calling it off or postponing is the right thing to do
[j11u36u] (score 29, diepte 0) Lol I’m 5’3” and 151 lbs  lol and I’m not muscular but certainly not fat, you got me wondering what your idea of fit is?
[j12rz9r] (score 26, diepte 3) It's sad that because he can't communicate clearly/make up his mind she's wasted so much of her fertility window with him.
[j12r7py] (score 26, diepte 4) So you only want her around to have a person around and not because you want her specifically around? That’s a bad thing. I’ve been with my SO for ten years. And if he left I would miss HIM not just having someone around. Even when we go a few days with barely seeing each other or not spending time together I miss getting to hangout with him. Because I love and care about him specifically not just having someone around. And yeah even after a decade I wouldn’t ever call is stagnate. Comfortable? Yes. But I still miss him when he’s not around and we still have fun together and have a very different relationship than I do say our current roomate.
[j12ccvr] (score 25, diepte 0) If I married someone and found out later that they were feeling these things or saw the things that you said written in your post and comments…I would be livid. If you don’t tell her, you are being extremely disrespectful and dishonest and she would be making a supposedly lifelong commitment under false pretenses.
[j121ysd] (score 24, diepte 2) I think it’s all the things you said, when you imagine your life with a child, how does that feel? You won’t have freedom anymore, and children are expensive. If you want a different life than that, that’s 100% valid. I guess there’s a chance you might not know for 100% certainty but is that something you want to gamble on when it seems like you’re leaning towards no?
[j129muz] (score 24, diepte 1) I like this the most, they’re not ready to be married at this stage. The wedding just lit some fire under him that it’s time to figure this stuff out once and for all.
[j125iw8] (score 23, diepte 2 OP) Seems as though he should have figured this out prior to getting engaged. He’s getting married in a week and is just now considering these things?
[j133ddb] (score 23, diepte 4) Thanks ❤️ not the most civil but I'm happy  to encompass that exasperated feeling every women feels when she's had her time wasted
[j12rubq] (score 22, diepte 5) If it's not an enthusiastic yes then it's a no. Every kid deserves good parents but not every parent deserves their kids.
[j129kw6] (score 22, diepte 0) If you truly love her please don’t marry her. She deserves better. What is going to happen if she gets breast cancer next year and loses both breasts. That 5’4” 135” is going to seem like Miss America. Not to mention is a healthy BMI. 

She deserves someone who desires her and loves her.
[j11zhm7] (score 21, diepte 2) Try not to think of stagnate in the long term. Long term relationships don’t necessarily need to be roller coasters of achievements and grand gestures and exciting events. Think of stagnation on a day to day. Do you or your partner ever surprise each other? Do something nice for one another without expecting anything in return? Have an actual interesting or novel conversation? Do you laugh with each other daily? Do you anticipate each others needs? If not, I’d consider that stagnation. More of the same old every single day. I can’t imagine living like that.
[j12ns1k] (score 21, diepte 2) It's a bit ironic that you're so into fitness as a hobby and then you say 

>I just don't have interest in getting sweaty or sticky and needing to shower.

Maybe it would be helpful to keep that feeling in mind when considering how your partner isn't interested in going to the gym like you.
[j13xz16] (score 20, diepte 1) This threw me for a loop so much! I’m 5’4” and usually between 130-135lbs and I have never considered myself remotely large for my height. I’m no model but I feel like I present as slim & trim with an athletic figure. Yeah most people (myself included) could stand to work out more but OP seems to have some damaging expectations here.
[j122vzl] (score 19, diepte 0) >Kids: She wants them, I don't. I think they're annoying, hold you back, take up your free time, and cost a lot.

🚩🚩🚩

Does your fiancée know that you don't want children? When one partner wants and the other doesn't, that's nearly always a relationship dealbreaker, sooner or later. And it's worse when the woman wants children and the man doesn't. Her fertile window has an expiry date. Now in her 30s, if you're not going to be the man she can have kids with, then she should be free to find a partner who is on the same page as she is about kids, so she can have her best chance at getting pregnant before it's too late.

>Beyond that I find myself wondering if things would be better with someone else. I find myself always gravitating in my head toward someone slimmer, or more athletic, or someone who is anti kids themselves. I wonder if it's just because then I don't have to challenge myself as much or move out of my comfort zone by imagining being with such a partner already.

More red flags. These would be some good things for you to explore in therapy. It sounds like you feel you are "settling" in this relationship, but you question yourself because you know, or at least suspect, that you're not being fair to your partner here and maybe you're asking for more than what you've currently got to offer. 

But, the solution is not to go into a marriage feeling like your needs and your relationship goals are not being met. For example, while I don't think it's right or fair of you to be critical of your partner's weight (which is totally within the normal range for her height), or her eating and workout habits, if that's how you feel it's important that you've recognized it. But you are doing her no favors marrying her when this is your attitude, and ultimately this is a red herring covering up much more fundamental relationship problems. 

Talk to your partner (but, not about her weight and her body, please!). Let her know that although you care about her deeply, you're having serious doubts if marriage is the right step. The divide over children and the lack of intimacy between you are very significant issues. 

Look into getting individual therapy for yourself, and possibly couples therapy. She too might benefit from individual therapy, but you're the person looking for advice here. You need to work on yourself, while she figures out what she needs for herself.

Please, don't get married in a week when you're feeling this way. Cancel the wedding until the two of you get things sorted out. Maybe you separate or maybe you don't, but you owe it to both of you not to marry her when you have so many doubts.
[j125m3f] (score 19, diepte 2) Ok maybe thrilled is a bit of an exaggeration. I get that things are less exciting when you are in a long relationship. But I still felt excited about the thought of our wedding and being married and our future together. And I wasn’t second guessing whether I should do it. Being secure in your relationship is good, but indifference isn’t. Here’s a question- how would you feel if she broke up with you tomorrow?
[j12725g] (score 18, diepte 0) You don’t sound passionate or excited to be with your fiancée, and don’t sound in love with her. This all sounds so flat, aside from some panic about the kids or no kids aspect. It makes me feel sorta sad for her, honestly. 

FWIW, my fiancé and I are I both in our late 30’s, been together 9 years, and have both decided throughout the course of our relationship to remain kid free, for about a million reasons. 

I’m excited to marry my fiancé next year to solidify our partnership in this thing called life. Together we make the hard times easier to deal with and the mundane days have bright spots. We’re each others biggest supporters for life goals, work goals, health goals, etc. 

Are you passionate about other things in life? Anything that would get you worked up and excited to talk about if you were asked a question about just the right subject?

A therapist could help you work through a lot of this.
[j130ls2] (score 17, diepte 3) Dead. This comment is everything 😂
[j13rqj9] (score 17, diepte 1) Op says he's concerned about her sugar intake, but if a 5'4" woman in her 30s is 135lbs, she's eating reasonable amounts of sugar
[j11tiex] (score 16, diepte 0 OP) I’m not even sure where to start. Did you not think about the kids thing prior to this? You’re getting married in a week and you’re just now thinking that differing opinions on kids might be a big deal?! That’s typically something big you discuss before even getting engaged. 

Her weight and height are proportionate. It sounds rather shallow for you to say she could eat healthier. 

The wedding is planned and a week away and you’re saying you think she may be better with someone else and you might be holding her back? Wow. This sounds like an excuse to back out. 

Some cold feet may be normal but you’re listing off a slew of things and quite honestly are sounding a little selfish and like you really don’t even want to go through with this imo. There’s nothing wrong with not wanting kids, but you probably should have thought about this before proposing and certainly more than a week away from committing to this woman for life. 

Please for her sake, figure this out.
[j138okp] (score 16, diepte 2) Unsolicited opinion coming in here:

IMO you have a bunch of (childhood) trauma that you’ve coped with through emotional numbness - what some would call severe avoidant attachment style. People like that have a hard time liking (the thought of having) kids cause they did not have a great childhood themselves and thus cannot empathize with children. They cannot love normally and the thought of someone depending on them (like kids do) scares the heck out of them.  In my opinion those people should not have kids until they work on this in therapy because if they do, the kid is gonna suffer from having an emotionally unavailable parent. 

This all sounds kinda harsh but I’ve seen too many folks like that to not comment on this.
(81 reacties met lagere score weggelaten)

=== THREAD 5pvgn6 ===
SUBREDDIT: r/Fitness
DATUM: 2017-01-24  SCORE: 41  REACTIES: 116
TITEL: Squat shoes - WOW
POST (source_id=post):
Hi everyone.

Just thought I'd share my experience with my first time using squat shoes.  I have an osteochondral lesion of the talus on my right foot which left me with little/no dorsiflexion.  I'd been getting by with very wide stand and too much movement at the hip (ended up with some hip pain that I'm still working through at the moment). 

I used them for the first time today and WOW.  Have never felt more comfortable squatting.  My usual 5 rep set weight became my 10 rep set weight just with a change of footwear.

Has anyone had such good results?  I'm currently looking into a few other things such as a weight belt - anyone have any success stories with the use of those?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[dcu7vrx] (score 61, diepte 1) 90% of the people in your gym probably don't even know what weightlifting shoes are, and the rest probably don't care.

If you want some then get some. I wish I got mine earlier, made my squat feel amazing and I was able to squat properly while I worked on the underlying issues that made me not able to hit depth without shoes.

Now I can squat either way but I still prefer the shoes.
[dcu4w10] (score 40, diepte 0) Been really debating squat shoes. I have my birthday coming up and I wanted to get some but I'm worried that I'll look like a guy with 'all the gear and no idea'. I only joined the gym in late november and my squat is only 175lbs so I keep thinking I'll look like I'm a bit overkill.
[dcubv55] (score 29, diepte 2) > Its another form of assistance that can be used as a crutch to hide weakness in flexibility, so i would use it sparingly if you do buy some. 

I couldn't disagree with this more.  The heel height in the powerlifts is the same or less than your average running/crosstrainer that 90% of the people in the gym are squatting in.  

The shoes are simply purpose built and more stable.  

I have no issues with mobility in any squat position, and still use my shoes if I'm not squatting low bar.  Why wouldn't I?
[dcugd7c] (score 28, diepte 1) Get the shoes!  People don't run in dress shoes until they're crushing 5ks, they buy running shoes right at the start.

It's a big difference and it helps you get stronger, faster and more safely.  Buy the shoes as soon as you can.
[dcufwbt] (score 21, diepte 1) Blows my mind that people really think they are important enough to think people give a shit about them. You are nothing to most people. End of story.
[dcur64x] (score 21, diepte 1) I judged some guy for having nice shoes and a mediocre squat, but that was only to compensate for my own crippling insecurity.
[dcuahwm] (score 21, diepte 0) I just wear my old vans and they seem fine.
[dcuxbig] (score 15, diepte 2) :(
[dcuk0sn] (score 11, diepte 1) converse low tops
[dcugu6k] (score 10, diepte 2) No guts required, just wear them.  You don't have to hold yourself to some ridiculous standard.  The shoes help from the beginning regardless of how much your squatting.  Just do mobility work in addition.
[dcuenvr] (score 9, diepte 1) So what? Shoes are training tools, nothing wrong with having big box of tools. No piece of training gear - minus barbells and dumbbells - come with 'one needs to hoist XY lbs to use those' clause. Just get 'em and use 'em.
[dcuapfd] (score 9, diepte 1) +1 for vans. That's all I lift in.
[dcuylt6] (score 8, diepte 2) > People don't run in dress shoes  
  
This is now my excuse why I'm bad at running.
[dcuuick] (score 8, diepte 0) Is it ok to squat barefoot?
[dcuxvpa] (score 6, diepte 3 OP) That was really useful. Thanks.
[dcuhsr2] (score 6, diepte 1) I was the same, can hit depth no problem with flat soles then my SO got me a pair of Romaelos for Christmas. Best thing I have for the gym. You feel solid when you are lifting, no squish and you are much more stable than with a pair of chucks.
[dcubrh9] (score 6, diepte 0) I happened to have a high intensity/low volume day when I tried my powerlifts the first time.  

My 1RM went for 3 that day.  The stability improvement was unreal. 

> I'm currently looking into a few other things such as a weight belt - anyone have any success stories with the use of those?

A belt is not like a pair of shoes.  Using the correct pair of shoes will add stability without any change on your part.  Using a belt is something that should be practiced a bit. 

Regardless of that, speaking generally, using a belt can add some weight to your lifts because you can brace harder. 

As for recommendations.  4" wide 10mm thick single prong.  Inzer Forever or similar.  No Velcro, no "weightlifting" belts that are tapered.
[dcv4rn3] (score 5, diepte 4) Tons of lifters from the amateur level to some of the best squatters in the world think they're worth it. They feel great to a lot of people and if you have the money I don't see any issue with it.
[dcugov7] (score 5, diepte 2) Weightlifting shoes should be a supplement to good mobility rather than a replacement.  However, there is still benefit to using the shoes from the beginning.
[dcuo4wh] (score 4, diepte 1) Get them, wear them, squat your ass off. Chances are you'll spend 100+ bucks on a good pair of gym shoes anyways. Might as well be weightlifting shoes if that's what you're doing right?
[dcumifv] (score 4, diepte 1) Not recommended. It increases the range of motion slightly and there's no advantage with respect to the angle of your ankles as with a squat. It will make your deadlift harder and possibly less safe. Deadlift should be done with a completely flat, hard sole, or no shoes at all.
[dcuoga6] (score 4, diepte 0) Bar none squat shoes are the best fitness related purchase I've ever made.
[dcu6cv1] (score 3, diepte 6) Also hip flexor and ankle (or did you mean that with calves?) stretches. But it really depends what is tight for him.
[dcus3ty] (score 3, diepte 5) Personally, wearing squat shoes makes me feel much more stable than my chucks under any weight. I dunno if it's purely psychological, but I lifted for a period without the squat shoes, and returning to using them makes lifting the weight feel so much better.
[dcusi20] (score 3, diepte 2) I honestly would be interested to see how well you squat in gym shoes. Unless you are squatting in some sort of flat shoe like Chuck Taylors?  A crutch? No. Weight lifting shoes serve the same purpose as running shoes. They make squatting feel more natural. You can even use a pair of Chuck Taylors and they would be better. Its not like the shoes fixes your mobility issues either. That comes from practice and muscle isolation strengthening. The shoes merely give you a way to squat more effectively which also helps with your mobility. Not seeing any downside of them or how they are a crutch.
[dcuwwim] (score 3, diepte 3) I squat fine in anything heres a picture of me dicking around in beat up sperrys.


http://imgur.com/a/hpttM


I prefer flat soled shoes. Chuck taylors are not "weightlifting shoes". Im sure the OP meant adipowers/romaleos/etc. Correct, the shoes dont fix your mobility, never did i state that. The heel lift increases ankle mobility and helps one stay more upright (in a more narrow squat stance typically), which can "mask" the imbalances of the lower body musculature. It can serve a purpose in teaching someone how to stay upright but at the end of the day it isnt "needed" and should be considered a tool.
[dcumkdg] (score 3, diepte 1) After several years out of the gym (and out of shape), I recently started over from basically zero.  I've been squatting 115lbs in squat shoes I still have from 5 years ago and bringing fractional plates into the lifting area with me to progress my overhead press.  Nobody's even looked at me curiously.  Get the shoes, nobody cares.
[dcv84c3] (score 3, diepte 1) The Adidas Powerlift look like any other pair of trainers that people wear to the gym so make great stealthish squat shoes. Squat shoes aren't a crutch they are a tool, If you have inflexible ankles then you should work on improving that but not wearing squat shoes (Or a shoe with a heel) isn't going to make them more flexible if anything the load on them is just going to tighten them up and reverse a lot of the work you're doing.
[dcud3pf] (score 3, diepte 0) I switched from Chucks to [squat shoes](https://www.amazon.com/adidas-Performance-Powerlift-3-Cross-Trainer-Metallic/dp/B019EM5JUA/ref=sr_1_1?ie=UTF8&qid=1485270817&sr=8-1&keywords=adidas+powerlift+3) and felt way more stable. It helped get rid of my knee pain as well. I also found that [knee sleeves](https://www.amazon.com/Rehband-7mm-Knee-Sleeve-Original/dp/B0088KPT50/ref=sr_1_2?ie=UTF8&qid=1485270851&sr=8-2&keywords=rehband+knee+sleeves) help reduce or avoid knee pain.
[dcv2ztq] (score 3, diepte 1) Squatting in running shoes is the equivalent of running in lifting shoes. You definitely should not be lifting in boosts.
[dcuw1yl] (score 3, diepte 1) Yes.
[dcv9bl7] (score 3, diepte 1) With socks of course - don't go barefoot in the gym lol
[dcuimmm] (score 2, diepte 2) You don't exist in the minds of 99.999% of people on the planet. Nobody cares what shoes you wear, because nobody cares about -- or even notices -- you, outside of your immediate family/social circle.
[dcu5pki] (score 2, diepte 4) I normally just do warm up sets with no weight and then the bar with no weight. Is there any quick stretches you'd recommend specifically for this?
[dcu6hv4] (score 2, diepte 7) Ankle/Calves yh pretty much the muscles in that area.

hmm I'm not sure about the hip flexors though, there was one time where I had extremely tight hip flexors from daily kicking practices, but it didn't cause me any issues from squatting ATG.
[dcu6m55] (score 2, diepte 8) They do cause me problems if I don't stretch them. I'd definitely recommend doing them for someone that just started out. At least to try if that helps.
[dcukxl7] (score 2, diepte 6) Yeah, I go up gradually to working weight.
[dcvmeno] (score 2, diepte 1) Get them. The heel elevation is going to help you the most early on when your ankle dorsiflexion is poor and squatting any weight in a solid-soled shoe is 10000x better than squatting in soft-soled shoes.
[dcvef9r] (score 2, diepte 1) Converse hi tops
[dcuhzqh] (score 2, diepte 1) I agree 100% with the knee sleeves. I was skeptical at first but since I've started using them I've had zero knee pain.

Still lifting in chucks though.
[dcudgbj] (score 2, diepte 0) A bit off topic but along the same lines.  This morning I decided to take off my kicks when I squatted, I usually wear Adidas Ultra Boosts because I run right before getting into weights to get my HR up. This was a game changer and I'll likely continue taking them off.
[dcvq3rn] (score 2, diepte 4) > Did you miss the no shoes part?

I did, my bad. But a lot of gyms don't allow that.
[dcv5a1m] (score 2, diepte 2) Yup, I got mine for under $70 on amazon. I love them and have had them for about 6 months and still look new.
[dcv5p0x] (score 2, diepte 1) I squat buck naked.
[dcv80vo] (score 2, diepte 1) Nice thing about weightlifting shoes is that they have a raised heel so that you don't need as much ankle mobility if it's an issue for you
[dcu4ylz] (score 1, diepte 1 OP) I worried about that too - I have a squat rack in my garage but I don't think I've got the guts to wear them to the gym just yet
[dcv7839] (score 1, diepte 3) Sad realization, but absolutely true.
[dcutom3] (score 1, diepte 2) Be less weak-minded
[dcv0dz9] (score 1, diepte 4) Haha, I mean it was just a more direct way of saying what others already had. Stop caring what other people think of you. You're actively not using something you have admitted has made lifting better/more enjoyable because you are worried what strangers who have no effect on your life might think. Take a step back and think about that
[dcu55ig] (score 1, diepte 2) Yeah I'll hold off for a couple of months. Right now though I find it incredibly hard to squat unless I raise my heels with plates. Even squatting with no weight.
[dcu5o4y] (score 1, diepte 3) Do you do stretches before and after the workouts? That helps a ton.
[dcu68wx] (score 1, diepte 5) calf, hamstring and glute stretches (Look them up on Google), they are quite basic but they should help a tonne for someone who lacks flexibility.
[dcu6z7a] (score 1, diepte 9) might be because I'm already flexible then :(
[dcugqph] (score 1, diepte 6) The calf, hams, and glutes don't really stretch all the much compared the the ankles.  This tends to be most people's problem in the squat.
[dcuh59y] (score 1, diepte 7) Yes so take the time to stretch it everyone can improve greatly
[dcuc27p] (score 1, diepte 5) You also do the bar with weight before jumping straight to your max right?
[dcugfob] (score 1, diepte 5) Do the squat stretch.  You can find pictures on Google.  Also be warmed up in general (say 5 minutes of easy rowing).
[dcvjukd] (score 1, diepte 3) Try a wider stance. Elevated heels definitely helps your back angle but something they don't tell you is it increases the knee moment arm which in turn increases the stress on your knee.
[dcut8oe] (score 1, diepte 7) Compared to wearing sneakers or flat shoes. I can't imagine barefoot would be much better.
[dcv7yk6] (score 1, diepte 7) Barefoot squats are great. Best option.
[dcve9k1] (score 1, diepte 8) I did barefoot for months. I started lifting in flat bottom shoes and they give the traction to keep my feet in one place and pointed in the same direction throughout the entire lift. I like it.
[dcvhl3q] (score 1, diepte 7) People who aren't oly lifters can still benefit from weightlifting shoes.  Try doing an olympic squat without them.  High bar, atg, as upright as possible.  Maybe you can, but for some that position is anatomically impossible to get into without them.  Even if they can get into it, the shoes make it more comfortable/doable.  You experiences aren't universal.
[dcuvz96] (score 1, diepte 5) because the guy on youtube said it will get them a 4 plate squat
[dcv57uz] (score 1, diepte 5) It just feels better for some people to squat in the shoes I guess. I don't really see a problem with it, it's just personal preference.

They're popular for powerlifters from the amateur level to some of the best squatters in the world. Regardless of if it's an internet lifting trend right now people like them for a reason.
[dcux9k4] (score 1, diepte 3) I completely agree. In my original post i said it is another form of assistance that can be used as a crutch. I didnt call it a flat out crutch. How many beginners are actually going to work on mobility if they can just throw some shoes on and get to work ?
[dcv923g] (score 1, diepte 4) Damn that is intense. Especially with some Sperrys. I know my issues when squatting were eased a bit when I switched to the Nanos but I still had to train alot to get my issues with my hip flexibility better. Now I can go ATG and my feet are not past shoulder with apart. My feet do turn outward a bit still but my knees still never go past my toes. Im pumped to  Squat tomorrow now!
[dcva6k5] (score 1, diepte 5) Yeah back when i was younger in my starting strength days (biggest mistake of my lifting career) i was overly obsessed with atg squatting and had zero knowledge on mobility. So of course my 16 year old dumb ass self starts squatting as deep as possible with no regards to lower back safety. I did injure myself and then learned that i had to train myseld to even squat that deep. Now im lazy though so i jist past parallel slightly lol
[dcveog4] (score 1, diepte 6) Lol nothing wrong with parallel. I would say 90% of the guys I see trying to load two plates or more at the gym cant even hit parallel let alone ATG. Squats have honestly come really far for me and was having some issues with my IT Band being sore because of my form and how I was not going to parallel. I basically restarted my form from 135 and worked back up the correct way. Heavy weights mean nothing when you cant do it correctly.  When I front squat I can get really deep into it. Actually deeper than when I back squat. Which I learned the hard way is extremely exhausting on the quads. Though when the weight hits around 75-80% I throw on my Lever Belt. It still engages the core and keeps my back safe.
[dcuqgpl] (score 1, diepte 2) Well, I currently stand on plates to raise my heels because I can't hit depth. Even squatting without weight I can only get so low unless my heels are raised slightly.
[dcuqn5g] (score 1, diepte 3) If you've already worked on increasing your mobility and flexibility but still need to squat with your heels raised then get them, definitely. Some people just need them to hit depth.
[dcv2j2z] (score 1, diepte 3) I'd rather see a beginner wearing lifting shoes, than balancing on plates.

A lifting shoe is more than a raised heel. It's a hard tight shoe, that stabilizes your entire foot and it's a solid sole. When you're squatting you really shouldn't be introducing anything under you feet, you can slip, trip or slide on, especially when you're balancing heavy weights on your back. 

I'd rather see a beginner wearing proper shoes, that hurt themselves.
[dcu5xbf] (score 1, diepte 0) I can already ATG front and back squat in flat shoes, but I still want a pair for some reason.  The only benefit I see myself getting form them is that my torso would be more upright in the back squat.  I guess I'll just have to try them to find out.
[dcv2ixz] (score 1, diepte 1) Will never be as good as actual weightlifting shoes
[dcwbsj7] (score 1, diepte 3) Have you ever lifted consistently in lifting shoes? I can do a full squat barefoot. I am more stable, upright, and comfortable in lifting shoes.
[dcwm91e] (score 1, diepte 5) Okay? So you would intentionally limit yourself? That doesn't make sense.
[dcx8al8] (score 1, diepte 7) If you're squatting less then yes, you will limit your growth.

Higher squat numbers=more growth
[dcuesc5] (score 1, diepte 1) > Using the correct pair of shoes will add stability without any change on your part. 

On contrary, I needed few weeks to learn to squat in those. Although from perspective of time I should probably blame pancake squats I was performing more than shoes.
[dcuw9h4] (score 1, diepte 1) They did the opposite for me, started to throw me forward :( but damn I miss the stability
[dcvmht3] (score 1, diepte 1) 100% agreed with knee sleeves. I've got genetic knee issues and have had knee surgery and the sleeves are crazy helpful at improving knee mobility and reducing pain.
[dcuekwa] (score 1, diepte 0) Shoes and a belt should be considered standard equipment for squatting heavy.
(36 reacties met lagere score weggelaten)

