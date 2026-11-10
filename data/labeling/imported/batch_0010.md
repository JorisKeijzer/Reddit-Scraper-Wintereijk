# Label-batch batch_0010

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
Schrijf het resultaat naar `batch_0010.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(5 threads: xxbmfa, 16gu1tq, wpv4kz, 1u6k83q, lhgflf).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD xxbmfa ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-10-06  SCORE: 0  REACTIES: 37
TITEL: How to run faster in barefoot shoes?
POST (source_id=post):
So first i have to give some background.

2 years ago when i was 12 my feet started to hurt when i was , the forefoot specifically, the doctors thought that this was many different things, but ended on the diagnosis after 1 year that it was some sort of athritis in the feet. This kinda sucked cause i always loved running around in the school and in the breaks, and this put a stop to this. Now my feet are getting much better and after only being able to go for short walks for 2 years or less, i can finally do stuff with my feet. The 1000 pills i have taken must have helped i guess. Well now i read the book born by run, and i got motivated to start running. So i started going for short runs, 1km, 2 km and then 4,5km. These are the runs i have done and it is over the past 2 weeks. As you know if you have read the book, it talked a lot about running barefoot, or minimalist shoes. So i wanted to try this, so the other day i got a pair of Vivobarefoot primus 3 lite trail shoes. So today i went for a run, 5km. This was in these barefoot shoes and not my regular running shoes (that i despise) or my barefoot. Ofc i felt pain in the feet cause im not used to barefoot running, but what left me annoyed is that i am slow as heck, i ran 5 km in a little under 40 minutes. Truly a turtle. So this is my problem, im very slow and would like to get faster, problem is the 2 years of inactivity has lead to me not spriting for 2 years, and therefor i havent used a lot of running muscles, and when i try to run fast i just feel pain many different places in the body, so i have to run slow, but then i dont get faster. Im just curious how to fix this, and how to run forefootstrike and not heelstrike.

Disclaimer i know a lot of you might say i started to quickly instantly going for a 5km run in barefoot shoes, and i guess thats true but my gym friend advised me to push myself very hard. 

So yea i just want to get some tips, also im 14 if that matters.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[irbvk7b] (score 7, diepte 0) Your gym friend is an idiot. To run faster in any shoes you need to increase distance over time.  Then introduce speed work,  fartlek,, hills, etc.  Too much too soon...especially if you have some kind of juvenile arthritis... will get you injured. Not just your feet but your Achilles, your hips, shins, etc. 

If you want to do minimalist running, that's fine,  but I would work up to it. Use less cushioned shoes and zero drop shoes (altra) to get you used to it.  Vivo are incredibly thin and not for everyone right off the bat.  You could even try Merrell. Born to Run is a great book, and very interesting,  but not gospel. Spend more time learning about running mechanics and training techniques right now before you get yourself hurt.
[irepo0p] (score 4, diepte 2) Basically,  you don't.  You work with what you have,  making sure to take your training slow enough to not get injured.  Run slow, run on soft(er) surfaces (i.e. grass,  track surfaces) if possible.  Work on building intrinsic foot muscles, and introduce dynamic stretching and bodyweight exercises for running-- there are plenty of videos online.

I'm not sure why your more cushioned running shoes hurt you... might be too narrow,  might be the wrong height,  might just be a shoe you don't like.  When you get the chance and the funds try on a bunch of different shoes before you commit -- if they're available in your area. This subreddit is difficult because everyone seems to post who has narrow to normal neutral shoes. Not everyone can  wear the same brands as everyone else. I need stability shoes and I can't wear some shoes because they aren't wide enough.  So their recommendations on types of shoes are helpful but you'll need to understand your foot needs before you can really figure out what will work best
[irba37w] (score 3, diepte 0) >	but my gym friend advised me to push myself very hard.

Your gym friend was wrong. Pushing fast when starting out in normal circumstances is not advised. Add that you’re trying to do this barefoot/minimalist only adds to the potential for injury. Don’t listen to your friend. Go slow and steady right now. Don’t push too far, and don’t push too fast
[irbfpjt] (score 3, diepte 2) It was a fad when that book came out ten years ago and turns out it wrecked a lot of people’s feet/legs. Based on your post it’s clearly not working for you either. If you go to your local running store or watch a marathon, do you see barefoot shoes? Nope. Sounds like you are new to distance running in general, I suggest you either go to a running store and get fitted for the right shoes for you (the staff there will get you set up) or start with a daily trainer from the shoe wiki at the top of this page. Start slowly and you will develop speed.  Good luck!
[ircmsq0] (score 3, diepte 0) Alright, a bit to unpack here.

\--You have to take into consideration your situation/condition. You want to do mobility, and strengthening exercises whether you choose barefoot or not. This will help more muscles be involved in your running, lightening the load on the ones getting most of the stress. It's some kind of rehab we might say

\--You have to take into consideration your fitness level. While a shoe can affect your pace, cadence, form, there's also your own running style that you have to "start from". Do you have a fast cadence, a slow cadence, a long stride, do you keep a steady pace, do you surge a lot, are you out of breathe a lot, do you have pain while running or when you stop running... 

\--You have to take into consideration the barefoot shoes themselves. They require you to have a more efficient strike, meaning you can't be stomping like you're dumbo on the ground, light-touch and quick is the name of the game with minimal/barefoot shoes. So maybe the vivos are too much too soon! You could start with shoes that have zero drop (height of sole at heel vs height of sole at toes) like Altras. Or another shoe brand i just heard about today called Topo Athletic that have some zero drop shoes with little stack (the over height of the foam/sole) 

I love my barefoot shoes and they have a place in my rotation (walking, easy runs, etc) as they help me run with a more efficient form, but i also have my zero drop shoes with stack for my faster and longer runs.  Some people just can't do it... if your foot is used to 8mm drop and more you're going to run into some issues and possibly injuries if you don't listen to your body or take it slow.

Start small and build on it. Your gains are not going anywhere, but it's better to get to said gains injury free if possible.
[irb9uts] (score 2, diepte 0) How fast are you running without barefoot shoes? It might not be the shoes at all, but the fact that you’re coming back from a very long injury.

Barefoot shoes can work for some people, by allowing the body to do what it’s supposed to do naturally. If you’re injured, then your body is already doing something else and barefoot shoes won’t change that. They also won’t provide the protection and support your feet need to continue healing.

There was a huge barefoot running craze around 2009 when the book was published, but you’ll notice that very few people are still doing it today. This suggests that it’s not the fix-all cure that the book suggested it was, or it would still be a lot more common. It can work for some people, but it sounds like it might not be the best for your current situation.
[ircst0a] (score 2, diepte 4) Have you? It sounds like you only started running 2 weeks ago
[irg4u33] (score 2, diepte 8) You should just go to a sports therapist or something, it’s not normal to not be able to run in regular running shoes for anyone. Your foot muscles/tendons/ligaments or something about your legs is probably off.
[irbecir] (score 2, diepte 0) “How to run faster in barefoot shoes?” Answer: Don’t.
[irerqlo] (score 2, diepte 4) A track will usually be softer than city sidewalk/concrete. 

The shoes hurting your calves... it may not be the shoes. You might have tight calves or you might be increasing your running load too quickly.  You can do calf exercises and stretches to work it out.  Your calves and your feet are pretty closely tied together in the muscle chain so it would make sense that a problem with one would create a problem with the other. 

https://youtu.be/AwxCKGkpKQw
[irema11] (score 2, diepte 1 OP) I have pain when running not out of breath tho, what exercises should i do?

I have middle/heel strike want to get a for foot strike but dont know how to. What would starting small be?
[ireujb8] (score 2, diepte 2) "You need to learn to walk before you can run" type of deallol. 

Walk a lot in barefoot around the house, then do some barefoot walking outdoors when/where you can. Do that for a few weeks

Then add in slow jogs here or there (maybe 1k once or twice a week) in your primus, you can do more running in more conventional running shoes too on top of that

Increase the distance slowly over months. Listen to your body. If there's pain, let your feet and legs rest... do some nice hot foot baths. Etc
[irg5n19] (score 2, diepte 4) It's like the concept of training for a certain distance race. If I'm training for a marathon, during the months of training, I'm pretty much never gonna run the full race distance to train for it.

It avoids putting too much load on the body which could take longer to recover. But you will get adaptations to will enable you to eventually run that full distance by doing several smaller workouts. You might be running longer than the marathon distance in the week spread out through different workouts, but you're not running the full distance until race day.

Similar concept for switching to barefoot. Just because you "can" doesn't mean your body is ready for it or won't suffer from it 😁
[irbf4z6] (score 1, diepte 1 OP) I have no idea how long im running without barefoot shoes, as said i just started running, and when using running shoes it hurts so i dont use those.  I bought a pair of barefoot shoes cause when i ran in running shoes and i went barefoot the other day on my 1km run a week ago, i didnt feel any pain in my calves like i do with running shoes. Why would it not be good for me?
[irbf7f1] (score 1, diepte 1 OP) But if i dont push far will i get anything from it\`?
[irbhr3i] (score 1, diepte 2) By going slow and steady. Progressive improvement. If you push to hard too quickly then you’re going to get injured
[irbl0x2] (score 1, diepte 3 OP) Its just i have been trying to go slow the past few months and seen no improvement
[irejnt7] (score 1, diepte 5 OP) yea actually running before, its just been like walking a bit and then running like 100 metres
[irbkkkn] (score 1, diepte 2) You need to build a cardio base first. There's no speed in a couch to 5k plan.
[irbl3sy] (score 1, diepte 3 OP) How do i build cardio when running fast hurts and thawts how i get my breath up?
[irbm0wt] (score 1, diepte 4) Run slow.
[irboe1p] (score 1, diepte 4) You can also build cardio with other activities such as biking, swimming, elliptical, etc that don’t put as much impact on your legs.
[irely8k] (score 1, diepte 5 OP) Yea but my problem is my leg muscles hurt cause i havent used them in a long time cause the injury, i bike daily and my cardio isnt that bad
[irfgh7c] (score 1, diepte 6) You need to start more conservatively. If you have trouble even running for like 20 minutes consecutively you probably lack aerobic health and just leg muscle development. Start slow and just try to run slowly for as long as you can without stopping
[irg4ghr] (score 1, diepte 7 OP) I dont have trouble running for like 20 min, i have trouble running 2 min in my running shoes tho, hate those
[irg5wpd] (score 1, diepte 9 OP) Nah its just the shoes i hope, it doesnt hearty teh calves when baerrfoot
[irbf8k7] (score 1, diepte 1 OP) why not
[irbkrsi] (score 1, diepte 3 OP) Wdym its not workiung for me? When i first ran barefoot i felt no pain and here it ewas just normal foot pain from getting used to them, compared to the pain i feel in running shoes its much better. Besdies its not like i can get my money bak isnt it? And where can i get a trainer?
[irbluw0] (score 1, diepte 4) Sorry for the confusion - a daily trainer is a shoe not a personal trainer. If you are set on using barefoot shoes, go for it. However, you surely shouldn’t be doing all of your runs in them that’s an absolute recipe for disaster.
[irekt5y] (score 1, diepte 5 OP) What should i do then? Going in my normal running shoe hurts
[irem103] (score 1, diepte 1 OP) How do i buy all these shoes i really cant afford it, especially when i just bouhgt new shoe
[ireqatq] (score 1, diepte 3 OP) Is a running track soft? The cusioned shoes heart my calves
[ires6c0] (score 1, diepte 5 OP) "it may not be the shoes." When i take the shoes off it doesnt hurt
[irg3hgm] (score 1, diepte 3 OP) I always go barefoot in the house, if socks count, i just dont have that much time sadly, besides it just feels silly to do that little when i can do more easely
[irg52oo] (score 1, diepte 4) Just go to a doctor. It seems like you have some sort of condition/special case that we won’t be able to solve here.
[irg6hut] (score 1, diepte 5 OP) Ohh i guess thats true, i just dont have other shoes than the barefoot shoes :=) so idk what to do about that
[irekubb] (score 0, diepte 5 OP) That doesnt get my breath up

=== THREAD 16gu1tq ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2023-09-12  SCORE: 3  REACTIES: 37
TITEL: do i HAVE to wear support/stability shoes if i have flat feet (low arch) and overpronate? i have achilles/ankle/knee niggles that dont seem to ever get better
POST (source_id=post):
so im a noobie trying to get more into the running world. ive dealt with achilles/ankle/knee aches and pains/niggles for a really long time. started running in 2020 using my nike free 2017. only couple weeks ago got a saucony kinvara 13 and 2 days ago the new balance 880v13. when i went to the retail store they got me to walk on the machine to see my foot shape/gait etc. they said i had low arches and overpronate so i should look for stability shoes. i tried on hoka gaviota and asics gel kayano and i didnt like em. then i tried on the 880v13 and it felt good to walk in them so i bought them

the thing is i just found out theres a 860v13 stability version so im thinking maybe i should try swap them even tho it feels good to walk/jog in the 880v13. its just these niggles that seem to never go away, im thinking maybe i really do need a stability shoe for my overpronation? i got customized orthotics back in like 2018/2019 and i put those into my nike free's but after awhile i started hating them coz how rigid they felt and i think gave me knee pain when i walking in them

do u guys think the overpronation is the reasoning for all my consistent aches and pains? if i want to experiment with more fun bouncy shoes like the endorphin speed 3 will i have to get customized orthotics again to stop my overpronating? for reference my jogs are mainly 2k ish 'easy runs'  at  7:30/10:00min/km depending how niggly im feeling but mainly around 8:00min/km ish and when my niggles are feeling better i can go 6:00min/km ish for 5k ish. but a big bulk of my jogs are at the easy/recovery runs just coz of my niggles. and also most of these jogs are at the park on grass, but i started trying to jog on pavement more since kinvara/NB since the cushion is better than my beat up nike free's lol 

im thinking of going back and trying on saucony tempus as they sound like they could b very benefical to me

and for reference i would say its my achilles that niggles the worst, then knee and ankles is the least 

cheers for any help :DD

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[k09pylb] (score 3, diepte 0) I think you’re overthinking it, as a newer runner the most common cause of pain is going to be overtraining, not footwear choice.  Not to say you don’t need stability shoes, or that stability shoes aren’t helpful, but their effect on your injury rate is peanuts compared to doing too much too soon.  

You have to wear whatever shoes cause you to not experience pain, and it’s hard to tell without trying a shoe whether or not it’ll work for you.
[k0arsh8] (score 3, diepte 0) Bro the police are on to you!
[k09wy0l] (score 2, diepte 2) You self described as a “noobie” and gave no real metrics, not entirely sure what you expected in terms of discussion. 

Running conditioning is not based on time dabbling in the activity, it is based on time spent doing progressive training.  If you’re not following any sort of plan and just sort of running a random distance at a random pace on random days, it’s easy to fall victim to an overtraining injury.

In terms of overtraining, total mileage is less important than % increase in mileage.  If one were to run for 2 miles two times per week, and then the following week decided to run 2 miles 4 times a week, that’s 100% increase in effort/mileage than what that persons body is used to, which can lead to injury.  Time and intensity matter

Shoes are much less important than gradually increasing intensity in physical activity of all kinds.  Not going to weigh in on whether stability shoes are necessary for anyone, as the science isn’t really there in either direction.  If a stability shoe works for you, great, otherwise it won’t magically solve problems with form/conditioning.
[k09sero] (score 2, diepte 1 OP) which stability shoes did u run in? wen u say u do better in neutral what do u mean by that? u can run longer and faster ? what about aches and pains? did u have any when running in stability or now they ur running in neutral? 

u think its unnecessary then and i cant put the blame of aches on my overpronation or if my shoe is neutral or not?
[k0an57n] (score 2, diepte 3 OP) is standing and off the ledge both important? or u could just choose 1 and dismiss the other? and when u say bent knee is that just the soleus machine? 

lol yea u rite!
[k0bnctz] (score 2, diepte 2) Running on anything uneven will work ur ankles muscles and tendons more.
[k0b72ep] (score 2, diepte 0) If your Achilles' tendon is the primary source of discomfort, you might try shoes with rockers in them. My understanding is that rockered shoes offload the work of running from the Achilles, ankle, and calf and onto the knee and hip. Most (all?) Hokas have a rocker, and many companies have added rockered shoes into their lineups in recent years, e.g., Saucony's Endorphin series and Brooks's new Ghost Max. 

You mention the Endorphin Speed 3 — that does have a rocker (Saucony refers to it as "Speedroll Technology"), but of the Endorphin lineup I think I would recommend the Shift 2 first, because a) you can get a pair for pretty cheap and b) it's not nearly as aggressive a ride as the Speed series. Of course, going back to your running store and asking specifically to try out rockered shoes doesn't require any money and gives you a few options to compare.

As for orthotics, I don't think it's the case that you need get them in order to run in neutral shoes, and I certainly don't think it's the case that you must get custom ones specifically. Runners' biomechanics change over time, and thus so do the shoes that work for them. I also have flat feet and overpronate, and I've had success in everything from the max-support Asics Kayano to the more "stable neutral" Endorphin Shift 2. I also have the Tempus and have been really enjoying it without any real stability issues.
[k09rybz] (score 1, diepte 1 OP) ive been running for 3 years lol and how much i can run in so tiny compared to other runners. its only this year where i tried to get more serious and run almost daily 

i dont think im doing too much too soon at all, if u read how much km's i run its pretty miniscule 

really only peanuts? i thought it was kind of a big deal
[k09zmwd] (score 1, diepte 3 OP) well like i feel like a noob when i compare myself to other runners running 50km's a week lol. but maybe more intermediate would b more accurate. 

im very noob in running knowledge tho, just the last couple weeks i been reading all about the latest shoes/shoe technology and learning all the different types of things that changes a shoe like neutral/stability. 

thats interesting that the science isnt actually their
[k09rng1] (score 1, diepte 0) I have extremely flat feet and some over pronation. I used to run only in stability shoes as that is what my running store recommended; but have found I do better in neutral shoes
[k09t0dw] (score 1, diepte 2) Brooks Adrenaline - my tendinitis got better once switching to neutral shoes but I think that also has to do with working on strengthening my ankles. I just prefer the feel now of a neutral shoe once I tried it compared to the stability shoe. I was worried that switching would cause me some aches and pains but it has not
[k09v2c3] (score 1, diepte 3 OP) thats very interesting that it got better! what kind of ankle strengthen exercises ? 

can u tell me how long wer u running in stability shoes and how long has it been since transitioning to neutral shoes? what exactly do u like about neutral  over stability?  is it the rigidness of stability shoes that is a turn off? 

thats great that it worked out for u, but im wondering how u said u have extreme flat feet but only some overpronation. they didnt tell me how severe the overpronation was for me but my flat feet is only low arch in severity so it sounds like u mite have it worse then me

just wondering what neutral shoes u run in now?
[k0ad6pc] (score 1, diepte 0) you need PT and strength training! Shoes are less likely to be causing you problems than weak muscles. Also running on pavement might actually be better for you. Running on grass will require more stabilisation from your ankles etc. so they’re working harder.
[k0afoip] (score 1, diepte 1 OP) i do see a physio regurarly! i do strength train. what specific exercises and how frequently do u think i need to do? i probably do single legged calve raise both off the floor and off a ledge like 1-2 times a week

oh u think so? the grass is pretty flat tho and it feels nicer running on grass in my free runs/NB but it feels better on pavement for kinvara. i guess it depends on the shoe
[k0aibxc] (score 1, diepte 2) To get rid of an achilles issue, you need to be doing those at least 3 times a week, and progressing them - adding reps or adding weight, adding bent knee calf raises, adding ankle stabilisation exercises in other planes
[k0at1k7] (score 1, diepte 4) Hahah yes the soleus machine. Feel the burn.   
I think the ledge version just gives a wider range of motion compared to the flat version, I think it’s more advanced. But some achilles injuries get worse with this kind of stretching so it depends how your body responds to it :) Google “insertional vs mid portion Achilles tendinitis“
[k0e7lc1] (score 1, diepte 1 OP) i dont think i like rockers if it feels too forced, if its more subtle i think ill like em but  yea we shall see

is there much dif between shift 2 and 3? also it has the same foam as my kinvara 13 rite with pwrun? so its quite firm? im interested in the tempus  or triumph coz of the pwrun+ 

what does 'stable neutral' mean?  but yeah i think the tempus sounds like it will be best suited to me. since u have flat feet too do u ever use orthotics or insoles?  so u never use pure neutral shoes?  did u ever experience niggles before u ran in stability shoes?
[k0ei894] (score 1, diepte 2) I think the big thing between the Shift 2 and 3 is a fairly significant weight reduction. I know the Shift 2 is pretty firm, and I have no reason to think the Shift 3 isn't. 

"Stable neutral" refers to shoes that are technically neutral but that have some stability elements. The Shift, for example, is a neutral shoe but has a pretty prominent heel counter that can help cut down on excessive foot movement. Doctors of Running has a pretty good writeup on stability running shoes that tackles some of this: [https://www.doctorsofrunning.com/p/guide-to-stability-running-shoes-2021.html](https://www.doctorsofrunning.com/p/guide-to-stability-running-shoes-2021.html)

I have occasionally used insoles with mild success but I find that the added weight is really noticeable. I also had a period (based on some bad running store advice) where I ran in pure neutral shoes but ended up having some calf issues and later a knee problem. A lot of this stuff boils down to personal biomechanics and I don't think you can necessarily extrapolate too much from one person's experience to another; I will say though to your "niggles" question that when I run enough in a shoe that isn't a traditional stability trainer I can experience some discomfort on the inside of my right ankle that typically goes away when I get back into something like an Asics Kayano or Mizuno Wave Inspire.
[k0eogs9] (score 1, diepte 3 OP) what was the bad advice the running store gave ? lol

thanks for article will sus it out!

i will try on a tempus and hope it feels good to me. u can use those as daily trainers rite ? for recovery runs / long easy  runs? what else would they b good forr?
[k0bn4k5] (score 1, diepte 0) Very flat feet here.  I wear neutral shoes with support insoles.  Superfeet, power step are good off the shelf.  I also have custom ones that are more supportive.
Size up appropriately for a thicker insole
[k0dj3xp] (score 1, diepte 1 OP) would u say its been very helpful for u ? did u hav niggles before  u did that?
[k0ecmqw] (score 1, diepte 2) Yes insoles helped a ton along with everything else I've done.  But I wear insoles a lot in daily walking and running tho not 100% of the time.  When not in shoes, I wear Birkenstocks in the house.
[k0elxlw] (score 1, diepte 3 OP) r the custom ones better than the superfeet?
[k0enwhl] (score 1, diepte 4) They are stiffer/provide more arch support than my power steps.
And they should last longer too according to podiatrist.

They're expensive, but my insurance covered them.
[k0eqvp1] (score 1, diepte 5 OP) do u use the custom more ? which do u enjoy using more between em?
[k0ey334] (score 1, diepte 6) Been using off the shelf for about a year and only got custom ones maybe 3 months ago.  I use both for daily commute and running.  No huge preference for either.  Custom ones are stiffer and more supportive is all
[k0eyjp6] (score 1, diepte 7 OP) may i ask why u dont buy traditional stability shoes and opt for neutral shoes with ur insoles?
[k0f01a0] (score 1, diepte 8) Totally, option of shoes is huge! How many neutral shoes are there vs stability.  I'm not locked into only the stability model from brands.

I get to try whichever shoe I like and the super deals I find them at and not worry as much about they will feel with my flat feet.

Super shoes are almost never stability shoes.
[k0cat64] (score 1, diepte 0) Fellow flat footer with very wide and flat arches. I had almost the exact progression of shoes except older generations and had a Hoka Rincon in between my Kinvaras and NB 880. Never did well in more traditional stability models because the arch support chunk always caused pressure/pain. I had custom orthotics but they did the same thing. 

I thinks light rocker works well for me and I ended up doing really well with the Mach 4&5 and Tempus. The Mach to me felt like a more springy Kinvara, but the downside is the midsole feels kinda dead after about 350km. The Tempus has a denser regular EVA support frame that gives more support near the arch but it felt a lot less obtrusive than other stability shoes. And after about 50km, the frame moulded to my foot shape and helped reduce medial collapse from my foot without pressure hurting my feet. 

From the sound of it, you’re already taking it lightly and seeing a PT, so you maybe you are someone who does better with stability features.
[k0dkkf5] (score 1, diepte 1 OP) haha wait so uve ran in free runs/kinvara/880's in that same succession  ? thats kinda funny, maybe id like the hoka rincon if u liked these shoes

when u say light rocker, does that mean the rocker is only subtle and not so forceful like some other shoes like hoka gaviota? coz i didnt like that sensation but it its subtle i could probably work with it

i actually tried on the mach 5 but didnt like em coz they felt clunky to me. uve only ran 50km in tempus so i assume u got them not that long ago but seem to be working well for u. our story sounds quite similiar, in how traditional stability and orthotics feel too obtrusive for our feet. is the tempus's arch support more subtle?  so u never use any arch supported insole or orthotics anymore? 

when u say flat feet, is it like pure flat feet with literally 0 arch? or is it low arches like me? 

do u still run in the other shoes mentioned or is the tempus ur main daily now? did u have any aches and pains running in the previous shoes ? has the tempus been a game changer for u ?
[k0eglye] (score 1, diepte 2) None of these shoes are in rotation anymore. I was talking about years ago (Free Run 3, Kinvara 8, Rincon 1, 880v10). The Rincon’s ride was nice but I have super flat arches, like zero arch. I always found the medial part of the Rincon (and Clifton) dug into my arch and caused blistering. I tolerated the Rincon until my arch forced the medial section of the foam to compress but couldn’t get myself to relive that a second time after the first pair died.

The Tempus was my main daily for last year and part of this year. It took about 50km to form to my feet but I’ve taken them to 980km now. They held up well but have lost all bounce at this point. Current dailies are the Superblast but I get a bit of heel slip unless I really crank down the laces, even with a runners knot. Plus it forces my toes too close together for some reason and causes blisters. Spent too much not to run them into the ground but after the foam dies, I think I’m going back to the another pair of Tempus.
[k0etu4a] (score 1, diepte 3 OP) are tempus great for every type of run? like recovery, long easy runs/tempo, speedwork and u can even use them for marathons? 

r u a 1 shoe only guy and run them into the ground? like u dont have anything else in rotation with the superblast?  are superblasts a neutral or stability shoe? 

what made u decide to go with the superblast when u already knew the tempus were great for u?
[k0f6v1n] (score 1, diepte 4) I tend to rotate 2-3 shoes at a time. Endorphin Speed 2 for speed work and either the Mach 5 or Superblast (then Tempus) for everything else. I liked having 2 options for dailies just to give myself some variety and to stretch out the lifespan of both.

The Tempus for me excelled at pretty much everything except speed work. A super stable ride with a tiny bit of bounce. Doesn’t excel at racing, but for my first marathon, I didn’t need a racer, I needed something trustworthy. Even then, it didn’t do a bad job with speed work. Many people use it as a tempo shoe. I just have a better option in the Speed 2 but it’s too unstable for me beyond a half marathon. 

I switched to the Superblast as my new daily because I’m always open to new models and wanted something more fun. And the FF Turbo is more fun and bouncy than the Powerrun PB in the Tempus but the upper fit is causing me too many other issues, especially for its expensive price point. The Superblast is stable for a neutral shoe but doesn’t have actual stability elements like the Tempus. It’s stable in the same way as the Mach 5 in that it has a wide base to land on.
[k0fesqi] (score 1, diepte 5 OP) do u ever experience any niggles  with all the neutral shoes u wear? or do u think im overstating how important a neutral or stability shoe is for aches and pains and the other factors are more important like how conditioned u r and training smartly/using good form and not doing too much too soon etc?

 r superblasts good for recovery/easy runs ?
[k0i76ob] (score 1, diepte 6) Superblasts excel at long runs and tempo efforts but they’re fine for easy paces too. I’ve had more niggles in the Superblasts than in either the Mach 5 or Tempus but I’ve also increased my running volume these past few months and slacked off from lower leg strength/balance exercises so hard to say what has the bigger impact. But overall

Some people will be adamant that you need stability shoes and some will be adamant that you don’t and just need to strengthen your lower legs. Either are probably an oversimplification. I agree with people who say you need to build your mileage slowly to reduce the risk of injury. But whether you need stability shoes is honestly up to you. If you enjoy running and the Tempus helps you do more of what you enjoy, then it’s a valuable tool. If you can afford more than one pair and are concerned about over-relying on stability features, consider getting a stability shoe and a neutral and rotate between the two.
[k0ii5re] (score 1, diepte 7 OP) where bouts the niggles from superblasts? wats the best lower leg strength exercise for achilles? just basic calf raises? 

i will forsure try the tempus and hope i can just kind of rotate between that and neutral shoes. also really wnna get into trail running but that feels like a whole other can of worms and potential headache x)
(1 reacties met lagere score weggelaten)

=== THREAD wpv4kz ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2022-08-16  SCORE: 82  REACTIES: 36
TITEL: First time running in the Speed 2s. Wide feet fam - they felt great! 6 miles and I was cruisin’. Normally a size 11 but went with the 11.5 based on other reviews and I couldn’t agree anymore. Perfect fit.
POST (source_id=post):
(geen tekst)

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ikjains] (score 6, diepte 1) Nylon plate. I can comfortably do everything in the Speed 2. Easy days, tempo, threshold, intervals. Yeah, no recovery but who does recovery runs?
[ikirm6l] (score 5, diepte 0) I got the same ones and they are awesome! #widefeetfam
[ikitw1m] (score 4, diepte 1 OP) Best part is that I got them for $80 with a discount code 😎
[ikj5wxg] (score 4, diepte 0) I don't really have wide feet, but my speed 2s definitely give me blister issues i haven't had before. On the outsides of the balls of my feet. Ah well. Fingers crossed the speed 3s treat me better whenever I get around to replacing.
[ikj9tjd] (score 4, diepte 1) Not for me, best fit ever. Did i mention i love this shoe? LOL
[iklnbk2] (score 3, diepte 3) Try the rebel 2s. The stack height is lower and they feel just as cushioned in my opinion.
[ikjb12v] (score 3, diepte 1) the speed 2s have a nylon (plastic) plate. If youre looking for a carbon plate those will be the endorphin pro’s
[ikkf93f] (score 3, diepte 0) I had to exchange my size 11 for a 11.5 and they are perfect. I too broke them in with a nice 6 mile run on Sunday.
[ikjhke1] (score 2, diepte 2) Great price. My local running shop was clearing these real cheap and i had to convince myself 2 more pairs was enough!
[ikjhmwm] (score 2, diepte 2) Don't consider them half off... Consider them BOGO instead!
[ikiyij7] (score 2, diepte 0) I have the same colour in the Pro 2. I have the multicolour in Speed 2
[ikj4tpm] (score 2, diepte 2) [I feel you.](https://www.reddit.com/r/RunningShoeGeeks/comments/wdqu33/my_rotation_august_2022_description_in_comments/)
[ikj94r2] (score 2, diepte 1 OP) Only did 6 miles, but no issues nonetheless. Are you a heel striker? I know some people mentioned it’s best for mid/forefeet.
[ikja64k] (score 2, diepte 3 OP) I think it’ll just take some getting used to. It can feel a little wobbly on the heel which is probably what’s causing those ankle issues. 

Totally agree. I’ll be picking up another pair if I can snag that 50% discount again.
[ikj8a8e] (score 2, diepte 0) How do these feel in the toe box? I've enjoyed a couple Sauconys but unfortunately felt they pinched on the pinky toe side too much even sizing up. Thanks!
[ikjjo04] (score 2, diepte 2) These do feel a bit like magic...And cheating. 


The shoes are rockets but my legs don't notice. Super comfy and hella fun zoomin around
[ikj9w7o] (score 2, diepte 1 OP) Interesting. I found the 11.5 was the perfect size for me. Had I gotten the 11 it would definitely be too tight in the toe box area.

For reference, I have the Saucony Ride 15 in a size 11 and if I went 11.5 it would definitely be too roomy. Guess I just got lucky to get the sizing down with them having such wide feet!
[ikiz43p] (score 1, diepte 1) Same here, Pro 2 in Vizi Gold.   
The Speed 2 are my current Nirvana shoe. You have no idea how much i love them. Surely, if i could only get 1 pair of shoes for running ever i'd have no doubts which one it would be.
[ikj9on5] (score 1, diepte 3) Duuuude!  
I got 3 of them too.
[ikjewfw] (score 1, diepte 3) Legend
[ikjhmgu] (score 1, diepte 2) Can you tell the Pro’s are clearly the faster shoe???? Mine are about to arrive
[iklyn93] (score 1, diepte 3) Mildly, for me they are snugger and barely lighter. Not a huge difference, but you can tell when going at your above threshold pace. Worth it? Not sure. If you have "chunky" feet your laces might look like they are about to explode. When i put the Pro2 on my feet the first time i was expecting the same fit but the upper is definitely "less". Heel counter is just apparent. But again, no issues and fantastic shoes as well.
[ikj62p8] (score 1, diepte 0) How’d your ankles feel OP? I had a bit of an issue after 8 miles last week.
[ikj9m3v] (score 1, diepte 2) 100% heel striker. I love these shoes so much so I got a second pair (sale ofc) for when it’s time to change out. Time to look up ankle exercises!
[ikjribk] (score 1, diepte 4) BGR50 still gets you 50% off!
[iklrj5d] (score 1, diepte 4) Thanks!
[iklz6jc] (score 1, diepte 3) They do want you to go fast!
[ikja9bs] (score 1, diepte 2) That's helpful thanks! Would like to give these a go if I find a good price.
[ikj8fcv] (score 1, diepte 0) The Speed 2 have a carbon plate right? I see quite a lot of people seeming to use them for daily training - is there something different about these compared to other carbon plate shoes like the Vaporflys?
[ikjbcey] (score 1, diepte 2) I see. Thanks for clarifying!
[ikjbnsp] (score 1, diepte 2) I see. Thanks for clarifying!
[ikjhxvd] (score 1, diepte 0) Love these shoes. To me they feel much smoother and more comfortable than the pros
[ikjszm8] (score 1, diepte 0) Depends on how wide ur feet are.  
I couldnt fit my duck feet in them, and they are not "that" wide....
[ikjuy8x] (score 1, diepte 1 OP) Mine are pretty wide. Was very surprised they fit honestly
[ikkff1i] (score 1, diepte 0) speak for yourself. I found these too narrow 🤷🏼‍♂️
[ikl4ecb] (score 1, diepte 0) Have wide feet but stick to my standard size 12 in these, i just don't lace em tight and use a runners knot.

=== THREAD 1u6k83q ===
SUBREDDIT: r/Shoes
DATUM: 2026-06-15  SCORE: 6  REACTIES: 35
TITEL: Are ON shoes worth the price?
POST (source_id=post):
I have a job for which i have to walk quite a lot. I have been wearing FILA sneakers and its not even been a year and they're already tearing from the sides. I have seen people wear ON alot but because they are expensive i wanted to know for sure they are worth it. Can they be machine washed or it will ruin the shoes if put in the machine? How long does a pair last? And also does the cushioning help with pain in the sole of the foot? 

&#x200B;

&#x200B;

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[ort5j3u] (score 7, diepte 0) I highly suggest going to your local running store if you have one. On shoes are definitely worth the price but so is every other running shoe and each one has different features. I prefer a wide toe box and a rigid soul, so I LOVE brooks running shoes for all the walking I do. If you go to a running store they can help you pick out a shoe that has all the features you like for your feet and let you test them out (they usually have treadmills in the store). Running shoes are absolutely worth it, but if you get the wrong pair, it will be a waste of money.
[ortk7k8] (score 6, diepte 0) FYI, walking shoes only last about 3-6 months (approx 300 - 500 miles).  I walk 4 miles everyday on a treadmill and have to replace my shoes by 4 months.  And they look nearly pristine on the outside, but I can tell they're wearing out inside.
[ort9r3i] (score 4, diepte 0) I have back and hip problems and ON are the most comfortable shoes I've ever worn.
[ortxh71] (score 3, diepte 0) Go to a running store that’s not brand specific and have your gait assessed. 

You might want On. You might be better off with Brooks or Hoka. 

Find what’s best for you and get some advice. 

They’re all expensive so worth doing the research and getting the assessment
[ortcj2z] (score 2, diepte 1 OP) Okayy, I'll look for a store. Thankyou
[ort73zv] (score 2, diepte 0) I own and operate a retail shoe store.

Truthfully, the On Cloud stuff is so cheaply made and over priced. They sell a lot due to massive marketing campaigns, that’s it. Short life span, cushion last about a minute, and they are not that good looking.

If you want a really great fitting and comfortable shoe, look into Topo Athletic. So many styles that fit differently, with an anatomical foot shape that is wonderful. Very long lasting.

I recommend purchasing in store rather than online ordering, because they have so many different fits.
[ortcuq5] (score 2, diepte 1 OP) Oh!! 
Thankyou I'll look into your suggestion ☺️
[ortd53y] (score 2, diepte 1) Odd - I wore my On Clouds every day for a year and then bought another pair b/c they were the only shoes that allowed me to walk (lots of different issues - back, hip, foot.) I'm not going to say they're good looking but I think that's subjective.
[ortsgus] (score 2, diepte 2) Cloud 6.  I don't recall the first style I had, but it was also great.  I recently tried the CloudSurfer Max and hated it, so I went back to the 6.
[orvvqwz] (score 2, diepte 2) Crocs are what work best for me with my plantar fasciitis. I was a reluctant convert, but I can't argue with the results.
[orupcl3] (score 2, diepte 1 OP) Makes sense thankyou
[orvuhz6] (score 2, diepte 0) I will be a customer for life, personally. They’re one of my favorite running shoe brands
[os86xd2] (score 2, diepte 0) Personally, ON Clouds were terrible shoes for me and created a stress injury in my right foot that then led to a bone spur. They were definitely the right size, they just really didn't work for me and I regret switching from Nike and New Balance. 

Try them on in person and a bunch of other shoes, too. They have excellent marketing behind them which is why you see them everywhere.
[ov3a8gc] (score 2, diepte 0) just so you know, in case you are still looking to buy them, some of the ON soles, due to their format, give me motion sickness when i walk
[ov7ydlc] (score 2, diepte 2) Guess it's because of the format plus it's softness
[ortv9nm] (score 1, diepte 2 OP) Hey, which ones do you have?
[ortcxyl] (score 1, diepte 1 OP) Okay!! Which one do you have if i may ask
[ortdpg1] (score 1, diepte 1) same. Bar none. I will say that I wanted to buy a new pair and one of the styles (just one) wasn't comfortable when I put them on so I think it's important to try on in person.
[orubuq1] (score 1, diepte 1) I had hip surgery and my Ons were such stable shoes. They really help my rehab.
[os46gy0] (score 1, diepte 2) I broke my ankle a couple years ago and was non weight bearing in that leg for 6 weeks, and then limited for 2 more weeks, while I was healing. My onclouds were my favorites once I was cleared to start walking again. 

I had original onclouds, and then I think 5s.
[ortd2t0] (score 1, diepte 1 OP) Oh yeah skechers can be good too!
[ortfbu0] (score 1, diepte 0) Bought my first pair pre-covid shut down and absolutely loved them. Every pair I have purchased since is a big disappointment. I have moved on to another brand
[ortu5zy] (score 1, diepte 1 OP) What brand do you wear now and are they comfortable on the sole?
[orun1ex] (score 1, diepte 2) I switched to New Balance. I definitely loved my first On Clouds, never found another pair that fit that well again
[ortu1ar] (score 1, diepte 1 OP) Ohno so walking is expensive too now 🫠😂
[oruf1mz] (score 1, diepte 2) Lol - YES!!!!
[p2cnlth] (score 1, diepte 1) True… started walking 1 mile everyday and I can see the damage!
[ortk8vp] (score 1, diepte 0) I get really bad shin splints and walk to work I upgraded to the ON shoes begrudgingly and they’re now my favorite pair of shoes to wear and my shin splints are basically gone unless I over do it on hills.
[ortutc4] (score 1, diepte 1 OP) Oh i have the same, thats why wanted new shoes, which ones of ON do you have? And how long after do you have to buy new ones?
[ortz52z] (score 1, diepte 2) I have the cloud runner 3s I got them two months ago and I wear them every day and do about 3-6 miles a day walking and they still feel as good as new.
[oruphbr] (score 1, diepte 3 OP) Ohkayyy thankyou
[ortqxk0] (score 1, diepte 0) They're the only shoes that don't make my joints hurt after walking around. They are cushioned but still have support and don't feel mushy. But I do find them too wide, and I don't have narrow feet.
[ortv54r] (score 1, diepte 1 OP) Okayy
Thankyou!!
[ortx7w6] (score 1, diepte 0) I feel like On and Hoka and Brooks are all equal in quality, but what works for some feet doesn't work for others.  My husband has plantars fascitis, and he's tried them all, but only Hokas work for him.  The toe box is too wide and square for me though.  My foot is very narrow, with a longer second toe, and On fit my feet better.
[orupxcl] (score 1, diepte 1 OP) Hmmm makes sense thankyou
[orugde3] (score 1, diepte 0) No
[orujptr] (score 1, diepte 0) No. I bought 2 and I hate both. 

I will stand with UA.
[oshkwdh] (score 1, diepte 0) Nike Vomero 18 are great. Plus version is a little better if they’re on sale.
[ov7ubjs] (score 1, diepte 1 OP) Really?? How does that happen? I'm very curious now 🤔
[ovblbmh] (score 1, diepte 3 OP) Oh wow which one did you get?
[ovc3d44] (score 1, diepte 4) I didn't, I tried it on and felt sick right away, needed up getting their boots that had a flatter sole
[ow7axxq] (score 1, diepte 0) No, they squeak and you’ll sound like an idiot and they don’t care to offer a solution. You’ll get passed of from one AI agent to the next. 

Since I paid cash I had no options lol.. I’m really regretting the purchase but lesson learned.
[ortc9et] (score 0, diepte 0) My friends from abroad love Skechers. They keep telling me that they are great for walking.
[ortkdyz] (score 0, diepte 0) I think Brooks are more comfortable than On.

=== THREAD lhgflf ===
SUBREDDIT: r/RunningShoeGeeks
DATUM: 2021-02-11  SCORE: 14  REACTIES: 35
TITEL: Nike Invincible Run has been released!
POST (source_id=post):
Finally! 

Well they’ve been released in the UK anyway, not sure about other regions. They’re on the UK Nike website, £159.95, one colour as per the previous photos. 

Looking forward to some easy miles! Just doing the usual prayer that they don’t hurt my feet as I’ve always found with Nike shoes that they’re either brilliant or utterly awful.

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[gmxaxt9] (score 17, diepte 1 OP) You do need more.
[gmxb1i7] (score 16, diepte 3 OP) This is the way.
[gmx4fpc] (score 9, diepte 3 OP) That’s the gamble these days with shoes. 

Zoom Fly 2 were brilliant for me, Zoom Fly 3 just so much pain. 

Vaporfly Next% are brilliant, Tempo Next% may as well go in the bin. 

The shoe buying lottery.
[gmxj2x1] (score 8, diepte 3 OP) I've got Endorphin Speeds as well, I'm buying the Invincibles for a different usage that I don't want to use the Speeds for.

The premium cushioned/plush shoe of any brand has always commanded top prices, it's just how it is. Some could argue the stripped down light racers shouldn't be so expensive for what you get.
[gmxazgu] (score 8, diepte 2) You' re right of course.
[gmx9mrs] (score 6, diepte 1 OP) In general or for this particular shoe? If you mean shoes in general these days then I guess you're right, but in the current market this is their premium cushioned shoe with full ZoomX and flyknit and it's the same price point as Adidas Ultraboost which maybe would be the equivalent shoe from Adidas.

I expected this to be about £20 to £30 more expensive than the Reacts and I'm pleased it was only £20. I was worried they'd put it in at something like £189.
[gmxavmp] (score 6, diepte 0) In Germany as well. It' s so tempting but I really don' t need any more daily trainers right now, so guess I' ll wait for more interesting colorways.
[gmxjkmy] (score 6, diepte 0) If anyone has a birthday 25% off code, it works on this shoe. Just placed my order for a Size 10 at £119!
[gmxfjjf] (score 5, diepte 2) For this particular shoe. For 160 quid you can get the endorphin speed which is more versatile. Or for only 10 more you get the premium adidas racer in adios pro. I dunno but Imo training shoes should be under 120. I guess I am just broke. :(
[gmx4318] (score 3, diepte 0) Do you have wide feet? I had issue with the arch being too narrow and causing numbness.
[gn3ec80] (score 3, diepte 5 OP) Yeah it’s so personal. Loads of people love them, I find them noisy, clunky clown boots.
[gn4sx1d] (score 3, diepte 0) Ordered mine last night here in Oz. Big fan of ZoomX and definitely enjoyed the Infinity and they look like a combo. Bad experience with Milers though which share elements with the Invincible too. They'll replace my 2nd pair of Novablasts which were great. Lots of non-technical dirt around here and feel like the outsole will work a treat. Local parkrun is dirt too which I sometimes run as a tempo to bookend against a long run on Sunday... might be a great all-rounder for both days... we shall see. 

Good luck with yours!
[gmx46vc] (score 2, diepte 1 OP) Hopefully that’ll work out well for me then. I’ve found that wide shoes that let my feet spread out cause me loads of pain on the outside of my foot, but narrow shoes that hold me in seem to stop that. I don’t have narrow feet either, maybe it’s a weird quirk of my feet.
[gn10fod] (score 2, diepte 4) If the Vaporfly Next% are wide enough for you, guaranteed you won't have problems with the Invincible. It's much wider, and one of the widest Nikes made in a very long time. Last one that was even close would be the Vomero 9 or 10? It's been a while, but I don't remember that shoe being narrow like so many Nikes have been in the last few years.
[gmzi8g6] (score 2, diepte 3) I watched a video on YouTube of a seasoned runner who ran in 3 different pairs of VaporFly NEXT% - one was new, one had 100 or so miles and another 250+ miles and he said there was very little difference between them. 

Assuming the ZoomX is the same in the Invincible, it should be fine for longevity

https://youtu.be/Qn4tLhFthFE
[gmykjh8] (score 2, diepte 0) Doesn't seem to be dropping in the US today :(
[gmzhuoz] (score 2, diepte 1) One of the YouTubers I follow who reviews shows mentioned that the US release has been delayed :(
[gmyv7fy] (score 2, diepte 0) Yup, seeing them on Canadian site too for nike members. $235 CDN plus tax is steep though.
[gmzk0c1] (score 2, diepte 0) Waiting for some more exciting colours
[gmzwl4s] (score 2, diepte 0) How long does it usually take for new colorways to come out? I'm not in love with this one but really want to try this shoe.
[gn0esrw] (score 2, diepte 0) Ouch, $235 in Canada :/
[gn3ds3e] (score 1, diepte 4) love the Tempo Next%! every shoe can't please everyone...
[gn1dhvt] (score 1, diepte 3 OP) If you really like ZoomX then this is your obvious choice though. Which shoes do you think are better? And is this based on you actually trying these?
[gmyw1yw] (score 1, diepte 1) Still upset JackRabbit didn’t honor us buying the  reduced price white pair. Then they release it couple days later for full price lol
[gmxe4vn] (score 1, diepte 0) I really want them but my rotation doesn't need another shoe :(
[gmzpap3] (score 1, diepte 1) This! Been waiting excitedly for these and opened the email before getting out of bed this morning, clicked through and it's just the one, pretty plain black. I really like the idea of these but after anticipating this release I faltered and didn't add them to the cart. Why do Nike seem to be so reserved at the moment in comparison to brands like Adidas with the Adios. I think I'm now just gonna save the pennies til the Rebel 2 is available
[gnb0dki] (score 1, diepte 1) Usually they start appearing a few weeks to a month or so after initial release, at least going by what I saw with other shoe releases
[gnavypf] (score 1, diepte 0) still no confirmation when this drops in the US?
[gnk5dzh] (score 1, diepte 0 OP) Well these are a strange shoe!

First of all, they are massive! Like huge to hold and just the widest things I’ve ever had on my feet. I feel like I could put both feet into one shoe. 

The ankle collar is quite high. When I first put them on they felt like they were rubbing round my ankle bone so I was a bit worried they’d rub but when I ran in them I couldn’t feel anything so no issue. 

The cushioning is out of this world. ZoomX really is great. So much more than any other shoe I’ve been in, feels like double ultra boost. 

A weird thing though is that I feel like I over pronate in them. I’m a neutral runner normally but I feel like I’m rolling into my big toe more than normal in these. It could just be weak glutes making my knees collapse in a touch but it was a strange feeling I got that I was very aware of the pressure on my big toe on toe off. 

Had high hopes for these but sadly they’re probably going to be far too wide for me. My feet ached so much after my run, could hardly walk.
[gnk9u0o] (score 1, diepte 1) Interesting! I would post this in a new post so it gets more visibility, would be helpful for people to know!
[gmx4a5p] (score 0, diepte 2) Sorry I meant in general with Nike. I have heard these are wider but I don’t want throw £160 on shoes that will never fit!
[gmx8ry2] (score 0, diepte 0) Way too expensive.
[gmxds2w] (score 0, diepte 2) I can bet that zoomx will flatten way faster than boost. UB is overpriced as hell.
[gn05em5] (score 0, diepte 3) Not just overpriced but weight like brick. How can someone even call it a running shoes with 12-13 oz.?
[gn0570o] (score 0, diepte 2) I just think there are better cushion shoes out there with cheaper price.

The premium thing is just a bullshit PR stuff.

