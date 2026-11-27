# Label-batch batch_0163

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
Schrijf het resultaat naar `batch_0163.labels.json` in dezelfde map, als JSON-lijst:
`[{"post_id": "...", "label": {...ThreadLabel...}}, ...]`, één item per thread
(2 threads: 2rinwa, yfkf2d).
Importeer daarna met: `python -m vocscraper import-labels`

=== THREAD 2rinwa ===
SUBREDDIT: r/Fitness
DATUM: 2015-01-06  SCORE: 53  REACTIES: 59
TITEL: 6'3" 210lbs wanting to be able to dunk off of two feet
POST (source_id=post):
For the last couple years I've had just enough of a vertical that I can weakly dunk jumping off of one foot. My New Year's resolution is to be able to do it off of two, something I've never done before. I've been doing at least 2 legs days a week, with copious amounts of squatting and lunging, but I'm not quite getting the results I would like. 

To give you an idea of where I'm at strength wise, I did a 3x8 at 225/245/275 for squat without too much concern that I wouldn't get it.

Do I need to start doing higher weight lower reps maybe? I also think that getting a little leaner physique might help me some too, so I'll take advice in that respect as well. Thanks guys!

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[cnge0ni] (score 34, diepte 2) Are you white?
[cng6yoz] (score 26, diepte 0) Google vertical jump bible (latest version is 2)
[cngmjz8] (score 26, diepte 3) Obviously all black people read the vertical jump bible as a part of their cultural upbringing, so my bet is yes, he is white.
[cng802k] (score 10, diepte 1) [Link for free version](http://msuathletics.ru/books/bible/vert_jump_bible.pdf)
[cng7ukf] (score 7, diepte 0) Look into jumpsoles. It was a huge goal of mine, when I was young, to dunk. I am also pretty short. Long story short, I trained with them every day doing fairly easy exercises. They really, really, really DO work. You can even just wear them around the house and passively train. I was grabbing rim with two hands in tenth grade at about 5'5"...and I'm asian; this was jumping off of two feet, but I am inclined to jump off two feet. My calves were HUGE! Jumping off of two feet is a lot about the technique too, like the form of a volleyball spike to create inertia. You might just want to practice that too. If you think about Lebron or whoever going up for an olley-oop you can see the resemblance of the volleyball spike. All-in-all, jumpsoles were like a wonder drug to me; the gains were so quick and noticeable.

Honestly, I was thinking about doing a blog or youtube vid series or something to see if I could maybe regain my hops at my current age, lol. Maybe I will make it my NY resolution.

Good luck and don't forget to post a vid when you hit your goal!!!
[cng79i9] (score 6, diepte 1) Do this ^ and don't listen to anybody else.

Work on getting your squat:bw ratio to at least 1.5 while practicing your jumps. 2.0 would be ideal for most.
[cngrrte] (score 5, diepte 3) I dont think it means that as in "do you really believe that crap" more of a "if you realllly believe in yourself and think its going to happen that quickly"
[cng9b79] (score 5, diepte 1) Wow - it was only a couple of pages in that I realized I knew nothing about jumping.
[cngi08x] (score 5, diepte 3) What kind of training? Is there a routine outlined in the book? Because I don't feel like reading 140+ pages to find a routine 
EDIT: I forgot how to finish
[cng6pcx] (score 4, diepte 0) Have you looked into plyometrics? Google increasing your vertical jump and you'll find a lot of literature.

Getting stronger is a huge help. But, IMO, the best way to get better at jumping is jumping. There's lots of routines out there.
[cngas2s] (score 4, diepte 1) I'm 5'6" an used jumpsoles too when I was young. I was able to touch the very bottom of the rim where the net hangs. This was with very low weights. They really work. 
Do you think it's possible to dunk at 5'6" if you work hard enough? I know spud webb wasn't way taller but he was a freak.
[cngdzz0] (score 4, diepte 3) I feel like verticals are very easy to underestimate. We see one guy jump out of the building and think that's easily a 40+ inch vert; when measured, that person might "only" have a 30" vert which is still pretty damn incredible. I remember when a picture of Andrew Wiggins' workout started to circulate around the internet. People were speculating that it was easily a 45" vert but it turned out to be 39 point something, [pic](http://static6.businessinsider.com/image/53752cafecad043a12dc9061-1200-1206/andrew-wiggins-vertical-leap-photo.jpg). Same for Gerald Green who supposedly has a 39" vert as well, dude nearly decapitates himself on every dunk, these stories make it hard to believe that people like MJ had 46" verts. 

Volleyball explains a lot tho, the sport produces nasty dunkers and mean shot blockers, it is honestly one of the most underrated sports when it comes to physicality and athleticism. 

I should really look into these jumpsoles, I've got 4 inches on you when it comes to height but I can barely touch the rim.
[cngbgm3] (score 3, diepte 1) [You mean these right](http://cdn.gunaxin.com/wp-content/uploads/2011/07/seinfeld-shoes.jpg)
[cngaorw] (score 3, diepte 0) I've learned that the vertical jump is a highly scientific movement based on a ton of variables. Take the following observations with a grain of salt since I have no formal credentials (but i did start dunking at 18yr 5'10):


* I believe hip mobility/hip flexors play a bigger role many think. During baseball season on tall metal cleats I'd get really sore in my hip flexors but I'd end up with a MUCH higher vert than I did during basketball seasons


* Weight training(Squats,DL,Lunges,RDL) helped but I always noticed I had to 'retrain' myself to jump again after a weight training cycle. Maybe this was the 'functional muscle' process maybe not.


* Max effort jumps helped me the most. I had an adjustable bball hoop that I would than allowed me to gradually work myself up to dunking on 10ft. Find a height thats barely within your range and get 15-20 dunks a few times a week.

* As I've gotten older I can lift way more yet I've lost my ability to dunk. Power to weight ratio is very important when flying.


If I had to give a personal estimate of importance with 0% scientific backing I'd breakdown vert as so:

15% Flexibility

25% Strength Training - squats,dl,lunge, etc

15% power/weight ratio

45% 'functional strength' - jumps, sprints, plyos


The tricky part is balancing these attributes. For example heavy weight training can decrease flexibility and make you weigh more, but is also essential in building up your max power output.
[cngciw9] (score 3, diepte 0) Power cleans if you aren't doing them already
[cngedqq] (score 3, diepte 0) The best videos on increasing vertical online:

https://www.youtube.com/watch?v=FzyaOut_QxA

https://www.youtube.com/watch?v=2SLg0HQr4FM

https://www.youtube.com/watch?v=DD08MginLXU

you're welcome
[cngaytr] (score 2, diepte 2) <3
[cngag5j] (score 2, diepte 1) Can someone give me a tl:dr of this?
[cngci37] (score 2, diepte 2) Dude claims to have trained his way to a 40 inch svj, people believe him
[cngk02v] (score 2, diepte 4) Jumping and shit, I can't summarize it
[cngwp7e] (score 2, diepte 4) There are a few to choose from.  The list of routines begins on page 76.  They are simple and.  The routines are clearly formatted and brief.  Not a lot of reading required, don't worry about it.
[cnglzgr] (score 2, diepte 2) Be able to squat 1.5x bodyweight before following program
[cngomww] (score 2, diepte 3) I can do that
[cngayvz] (score 2, diepte 1) Damn 5'5 and grabbing the rim is impressive as fuck, have you ever had your vertical measured?
[cnh39df] (score 2, diepte 2) http://www.jumpusa.com/mm5/merchant.mvc?Screen=PROD&Store_Code=J&Product_Code=1001B&Attributes=Yes&Quantity=1&Affiliate=google&gclid=CMHMg_KzgcMCFYVafgodvoYAVg

I had these. I think they look a lot cooler, and they attach to your personal shoe. These are the "official" jumpsoles.

(Sorry, I dont know how to hyperlink; new to alien blue.)
[cngprdr] (score 2, diepte 1) This is a good answer, let me add a few ideas from the perspective of being a personal trainer and my personal vertical jump training:

- Hip flexors are exactly that, they 'flex' or close the gap of your hip (this is hard to explain via text, google it if you're unclear) therefor you would want to stretch your hip flexors so they're not tight, as a jumping motion would involve rapid lengthening of your hip flexors, and any tightness could reduce your momentum, and apply more resistance the jumping movement

- Become clear about the differences between training styles, i.e. 'strength training' and 'power training'. It's clear once you understand these terms, which style of training is useful for what. That said, strength = how much force can you generate. Power = how much force can you generate and how fast can you do it. These are some pretty overlooked albeit very important distinctions to make in jump training

- Functional strength is a pretty loose term, because functional can be applied so differently to different people. Functional strength for a NFL player is going to be completely different for functional strength for a 75 year old lady with arthritis.
[cnglf3r] (score 1, diepte 1) Yeah when i weighed 155 and squatted about 310 at 5'8 i could hold rim on a basketball net due to the plyometrics my track and field coach had be doing as a long jumper. It added atleast 4 inches to my vertical in 3 months and I didn't even take it seriously at all. It kind of just happened.
[cnghabt] (score 1, diepte 2) Is there a link to version 2? Or is it still pretty much the same?
[cngaaw2] (score 1, diepte 1) yes!!
[cngonfi] (score 1, diepte 5) Haha I thought it might be something like this. I'll just have to suck it up someday and read it
[cngym5y] (score 1, diepte 3) quote from the doc

"it is **not necessary** to squat 1.5 x your bodyweight to partake in light to moderate plyometric drills. These include just about all kinds of jumps, hops and bounds. In fact, pretty much everything except for high depth jumps and shock jumps. "

I didn't read it all, so you still may be right ..?
[cngb7u5] (score 1, diepte 2) Like I said, I was only 5'5" and 15/16 years old when I could grab rim two hands and hang on it. It is most definitely possible!!! The only reason I couldn't dunk consistently is because my hands were too small at the time to grib the ball, and I didn't quite jump high enough to slam with two hands of course or jump high enough to do a Vince Carter type throw the ball in. Please note though, I was obsessed with hops at the time and trained a lot. Jumpsoles though, crazy awesome tool.
[cngbf6s] (score 1, diepte 2) Surprisingly, it wasn't that impressive. It was like in the high 20's. There is a lot of confusion about how to measure a vertical though or a lot of embellishing also. Sometimes I couldn't believe when college scouting reports would claim a player had 46" vertical or something. Sometimes they allow one step or a small step. I measured with no step at all of course. I kind of attribute being able to jump off of two feet well because I did play volleyball also. I think I just had good technique with running and jumping off two feet or something alike. Jumpsoles though! Going to look in the shoe cabinets for them in a minute to see if I still have them after a decade or more.
[cnh3g3t] (score 1, diepte 4) I ran a 4.6 also at 15 because of the quick twitch muscle training the jumpsoles provide. This was just the gym teacher with a stopwatch though; maybe it was a little slower or faster in reality.

You can really feel the burn with the jumpsoles though, and they are really fun to workout with. You can just go shootaround with them on or basically do anything where you're just running around. Do layups and slap backboard, and you can easily tell and feel you're getting a good workout. 

I am sure people are curious about safety and spraining your ankle. I felt really safe in them. The velcro is really strong, and I fastened them really tight. You should naturally not do any movements that might be unsafe. Because the surface area of the platform that touches the ground is so flat and wide, your ankle is not really put into crazy angles.
[cnh5iid] (score 1, diepte 5) They seem amazing, I had never heard of them before. I'd look into a pair for sure if there was actually a place here for me to use them.
[cnh866z] (score 1, diepte 6) You can train with them anywhere man! You basically need like 5 x 5 feet of space. The exercices are basically jumping up and down, jumping and turning 180 degrees, and jumping onto a platform.
[cngli4v] (score 1, diepte 3) Out of curiosity since i have no idea how to do this correctly If I can hold rim (hang from it) at 5'8 what would my vertical theoretically be? I was able to do that at the end of track and field season. I also had one of the highest standing broad jumps on the team, i think the 4th farthest.
[cnh0q4m] (score 1, diepte 4) Depends on how long your arms are. You can measure your vert by measuring the highest point you can touch while standing flat footed, then the highest point you can touch by jumping. The difference is your vertical leap.
[cnh3ama] (score 1, diepte 4) To measure vertical, you stand next to a wall and raise your arm straight up and mark the wall with chalk or something. Without taking any steps, you jump as high as you can and mark the wall. Measure the distance between the two marks... and voila.
[cngw71k] (score 1, diepte 2) Was the sprinting in high metal spikes during baseball season making my hip flexors stronger, more flexible or a combination of both.  I remember getting crazy DOMS in my hips for the first week of adjusting to the spikes.  I've read that hip flexors in a sense restrict the vertical jump pattern so wouldn't stronger hip flexors = smaller vert.
[cnh7470] (score 1, diepte 3) I can't answer your first question because I've never worn or read anything about spikes. I could postulate that because there would have been less 'give' when you strike your foot when sprinting in spikes, there for your muscles need to absorb more shock/force.

Your last point is pretty much correct. I say pretty much for the following reasons:

- your 'hip flexors' are a group of muscles including iliacus, psoas, sartorius, and the rectus femoris.

- your illiopsoas muscles, if contracted or tight, will restrict the extension of your hip joint (think of this as the 'rapidly straightening-out part' of jumping)

- your rec fem and sartorius are both involved extending the knee AND extending the hip joint, so it's arguable that they could play a role increasing your vertical leap by extension of the knee joint, but at the same time it's important that they are able to immediately relax after beginning the jump pattern as to not hinder the following extension of the hip. (Sorry if this is confusing)
[cnhes2i] (score 1, diepte 1) uhhhhhh you are VASTLY underestimating the power/weight ratio. thats the most important one there.
[cngbgaj] (score 1, diepte 0) Traditional leg workouts don't really help you with dunking.  The muscles for dunking are quick-twitch muscle - stuff there for explosive movements.  Doing stuff on a speed ladder, jump boxes, foot speed exercises, weight vest/shoe jumps, or just repetition with max height jumps will increase your ability to explode to the rim.  Flexibility helps, too.  My father has a whole work out for it, something similar to the Jump Bible, that both me and my younger brother tried out.  I did it for a couple weeks and at 25yo was able to dunk off two feet at 6'1, 200lb.  My brother is 6'3 and 175lb, he does the workouts semi frequently still, and can put down 360's off two feet and all sorts of stuff.

TL;DR: Work your quick-twitch explosive muscles in ways other than traditional weight training.
[cngclrj] (score 1, diepte 0) If you're wanting to strictly stay in the weight room, one of the exercises you'll want to learn and perform that will help with your vert is the clean and jerk.  You'll need to find a gym with bumper plates, otherwise you can totally wreck your shoulders (learned from experience on this one).
[cngigl0] (score 1, diepte 0) You'll get better at jumping by jumping.
[cngm0m6] (score 1, diepte 0) Check out Vertical Jump Bible. Basically its getting your squat up to at least 1.5x bodyweight, and then you can incorporate the plyo routines in with your lifting. Its totally worth the read.
[cngmeub] (score 1, diepte 0) I was gonna come here to say squat, squat, squat, but apparently you know already!

How old are you?

I ask because I'm 6'6" and really wasn't able to dunk well until I was 19. Just had to wait for the coordination to catch up to my growth. Could be the same for you!
[cngslh2] (score 1, diepte 0) Work your abs. There like a spring in the center of your body.  Also its more about explosiveness i.e speed then power.
[cngsyyr] (score 1, diepte 0) incorporate power cleans in with leg days
[cnguux6] (score 1, diepte 0) look up dunking videos, there are good ones on youtube. I guarantee your form is off in some way i know mine was, you can gain 3-7 maybe more inches on your dunking vertical just by using proper form i.e. approach planting your feet without stopping momentum.

source: 6'4" used to not be able to dunk well a few years ago, watched videos can 360 dunk now.
[cngv81i] (score 1, diepte 0) I have an easier time dunking off of 2 than off of one. I think you probably have a technique problem instead of an ability problem.
[cnh8bzo] (score 1, diepte 1) Idk how much you play basketball but most people who play can jump higher with a running start off of one foot. But I have a friend who can only dunk off of 2 feet.
[cnh9rgo] (score 1, diepte 2) The forward momentum of a running start doesn't help as much as the upward momentum of starting low on two feet. I don't play a lot of basketball though.
[cnh27vy] (score 1, diepte 0) As somebody who can dunk like you want to, at the same height and with a slightly weaker squat than you, there are a few things I'd recommend.  Vertical jump bible is great, I'd design workouts with a lot of influence from that resource.  I think squats are less helpful for some people than deadlifts or hang cleans.  I especially like deadlifts with the hex bar.  I think you're absolutely correct about a leaner physique helping.  I don't know what your body composition is like but if you have body fat to lose, losing it will help a ton.  You'll probably lose some weight just as a side effect of working on explosiveness.  The last thing that I'd like to add is that in the middle of jump training programs it can feel like you're getting bogged down, but before you worry that you aren't getting results, finish the program and take a week of rest.  Sometimes it takes a minute for your legs to catch up to the work you've put in.
[cngjueu] (score 0, diepte 0) This should give you all the answers you need:

http://vimeo.com/7212184

Helped me dunk at 13 years old.

TL;DR: http://youtu.be/Uwbqr2UjeSg
[cngfiai] (score -1, diepte 1) This.
[cngbjd9] (score -1, diepte 0) Calf work. Do calfs everyday.
[cngbpnz] (score -1, diepte 0) guy comes here asking how to dunk, can already dunk.  fml
[cngnwdr] (score -12, diepte 2) >While flying in a plane is nice and all, it’s a bit expensive and way too temporary.
Sprouting feathers and wings ain’t gonna happen! So, unless you’ve got money to burn or
you really believe in evolution, you’re stuck with improving your vertical jump.

I know it's a joke, but the fact that they're saying believing in evolution involves believing I might sprout wings physically pains me.

=== THREAD yfkf2d ===
SUBREDDIT: r/Frugal
DATUM: 2022-10-28  SCORE: 2  REACTIES: 58
TITEL: Frugal solutions for cold feet?
POST (source_id=post):
I have Hashimotos (medicated) and, as a result, my hands and feet often get painfully cold when the temperatures drop even slightly. I'm especially bothered by the cold feet so I'm wondering if there are any frugal solutions, but ones that would allow me to still move around (as opposed to, say, an electric foot warmer). I'm afraid layering socks doesn't work as I'm currently wearing a pair of normal cotton socks, a pair of fuzzy socks over them, and thick soled slippers but my feet are still cold.

I've heard wool retains heat very well but I don't want to buy new wools socks because animal exploitation and all that. But I have some yarn at home that contains 20 % wool that I accidentally bought once. I could crochet myself a pair of socks out of that. Would 20 % be enough to make a significant difference in the warmth of the socks as opposed to cotton and synthetic materials?

REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):
[iu4de54] (score 18, diepte 3) The sheep get shaved to harvest the wool. Then they grow more. They don’t kill the sheep to get it. Wool is a renewable resource and is the way to go! Alpaca socks are my favorite! Same process as the sheep. They shave them and they grow more.
[iu3xi50] (score 14, diepte 0) I have Reynauds, so I feel your pain!  I got a small space heater on Amazon for about $20 a couple of years ago.  On cold mornings I crank it up and aim it right at my feet and it does the trick.

My other solution is to date someone who is very warm and use them as a foot warmer
[iu4nqqf] (score 10, diepte 5) Usually sheep that are grown for wool are not grown for meat. It sounds counterintuitive, but chickens are the same way. By the time an egg layer stops laying eggs, they are so old that the meat is tough, and not profitable. Any animal raised for meat is going to be slaughtered shortly after achieving the required age and weight.

If you're still concerned, look for a local farm, or a less local farm that you can research, who has ethical practices you're comfortable with to obtain your wool yarn from.
[iu3xdwa] (score 7, diepte 0) Hot water bottle works well when you’re at home.
[iu3vy96] (score 6, diepte 0) Wool socks! I’m from California and moved to Colorado a little over 10 years ago. I’m not gonna lie I had never even heard of wool socks. Like yeah wool exists, but socks? My wife is from Chicago and she bought me my first pair. I haven’t worn socks that weren’t wool since. They’re definitely a little more expensive. I think I bought my last two pairs for the same price as a 12 pack of tubes. But they definitely last longer! I wear thermals through the summer here lol. If you wanna stay warm, stay away from cotton. It gets wet, stays wet and you get cold. Hope that helps ya!
[iu41buy] (score 6, diepte 1) Wool is the answer. SOOOOOOOOOOOOO much warmer than cotton. I have wool socks, wool long underwear, wool scarf, wool slipper socks, wool slippers, wool gloves to go under my wool mittens, wool insoles to put in my shoes, a water resistant winter coat with wool in the insulation, multiple thicknesses of wool sweaters, and a wool duvet. I use a heating pad on my feet in bed and it is fantastic for warming me up so I can fall asleep quickly.  
You can get mulesing-free wool products, or buy used for some things.
[iu4qizr] (score 6, diepte 7) Sheep don't really stop growing wool though, so for your current issue that's not really a concern. They would be killed once they were already old and sick, at which point its probably a mercy. Again though, you can look for ethically raised sheep. Many shepherds care quite deeply about their flock in many parts of the world.

Also, at the age a chicken stops laying eggs they are actually really quite old. Even if they are killed because they're no longer profitable, they have lived a very long life.
[iu3wjm0] (score 6, diepte 0) My one set of hand knit animal fiber winter accessories is the warmest thing I own. It's a bit big on me and not as cushy as a store bought hat and cowl set but if it's even a few degrees above freezing I'm sweating within minutes.

If it helps, I purchased the yarn from a second hand craft supply shop - it's the only way I can afford natural fibers and I'm trying to avoid acrylic yarn now. Of course you have to weigh your own moral priorities, but I wanted to present you with that option. I've heard of people even buying old wool sweaters from a thrift shop and unraveling them to make new projects.
[iu3zbnh] (score 5, diepte 0) I bought electric socks. Ororo brand. $80ish. But I view frugality as not buying to excess, not always simply the cheapest option. They're lovely on snowy walks. 

On a smaller budget, I also have used those reusable instant heat gel pads (the kind with the clicker inside) or hot hands pads. Tuck them in between your sock layers. And additionally, make sure your socks aren't too tight layered up, they can compress and restrict blood flow, making the problem worse.

I also just have multiple heated throw blankets around the house, in the places I tend to sit.
[iu40fv8] (score 5, diepte 0) Not a suggestion for a new pair of socks, but rather a comment on layering: make sure your sock layers aren't too snug, as a lot of the time cold feet can be the result of poor circulation! Several tight layers of socks can actually be counterproductive in warming up cold feet since they can restrict blood flow. Try if layering larger and looser socks help or even including knee socks since they can help with lower leg circulation as well. 

(Also if you're going to crochet that pair, maybe make it extra big to be a loose top layer!)
[iu3smrg] (score 4, diepte 0) There is a warming lotion you can get called Akileine Cold Feet Cream. Not sure what your budget is but it is about $20 a tube.
[iu5b8mr] (score 4, diepte 0) Alpaca fur socks from a local alpaca farm if you're really opposed to wool. The majority of wool and milk sheep farms are very ethical though, so I would consider supporting them.
[iu4bkmt] (score 3, diepte 1 OP) Haha, I do but when he's not at home, my feet suffer.
[iu5bwgx] (score 2, diepte 1 OP) I have no problem with buying an occasional secondhand wool product. I'll try finding a sweater and unraveling it for yarn.

Also, how I wish we had a secondhand craft supply store where I'm from!
[iu42rmh] (score 2, diepte 1) and stays warm all night under the blankets!
[iu4c6if] (score 2, diepte 1 OP) As I said in the original post, I need something to warm my feet while I'm walking around the apartment.
[iu4hahl] (score 2, diepte 2) Check out heated rechargeable socks on Amazon. Pricey but might finally keep your feet warm.
[iu4cbof] (score 2, diepte 1 OP) Oooooo electric socks sound like the stuff of dreams!
[iu4chg3] (score 2, diepte 1 OP) Thanks for the tip! I'm a girl with bigger ankles/calves and so it's hard to find socks that don't squeeze the life out of my ankles.
[iu47qp7] (score 2, diepte 0) I have reusable handwarmers. They are little plastic squares filled with gel and a metal disk and when you bend the disk it creates a chemical reaction and the warmer stays warm for a few hours. So when I'm really cold at work or home I'll just activate one or two. And since they are reusable it's really nice and I basically just carry some around with me all the time.
[iu4bdra] (score 2, diepte 0) Boil 2 eggs for your lunch right before you leave the house and put them in your coat pockets as hand warmers.
[iub2dtq] (score 1, diepte 9) We will all die eventually whether we wanted to or not, whether it’s our natural time or not. It’s the laws of nature and the same thing happens with animals (well, humans are animals too, but you know what I mean).
[iu6dlt2] (score 1, diepte 4) Another option might be musk ox wool, aka qiviut, but it's not cheap because there are only a handful of producers in Canada and Alaska, mostly either non-profits or small native owned cooperatives.

Since they're synchronous shedders there's no shearing involved, their coat comes off naturally each year. And unlike sheep their quality of wool doesn't really deteriorate with age so they are rarely slaughtered for meat, if they are it's usually for subsistence purposes and not commercial sale.

And it's great wool, very warm...but it's hard to call it frugal.
[iu4drt4] (score 1, diepte 2) Lol, I do feel I am living my best life in them. :)

There are battery operated heated booties/slippers out there, too, since you mentioned in another comment you find a lot of socks snug. Just no personal experience with any of the brands.
[iu5kuds] (score 1, diepte 2) i have a pair (not that brand). they work ok. the charge doesn't last that long. my insulated socks are much better.
[iu8096v] (score 1, diepte 2) I hear you! See if bigger and taller socks help. And I think a giant layering pair with 20% wool would help too :)
[iu41wtf] (score 1, diepte 0) Socks
[iu43940] (score 1, diepte 0) Reynauds here too, and swear by my handknit socks (wool) with a slipper. Natural fibres are best for heat feedback, plastic and cotton just aren’t as good. The key is to put them on when your feet are warm, not once they get cold!
[iu448xf] (score 1, diepte 0) Have Reynaulds. Can try different blends of synthetics socks for campers/hunters to avoid wool (I got a knockoff version and it works great).

 When my cat doesn't use her on demand heating pad its my feet's turn, it was around 20.
[iu458t6] (score 1, diepte 0) Socks and slippers
[iu5ajc3] (score 1, diepte 1) This is a great idea. You can tuck them into your socks
[iu4gies] (score 1, diepte 0) \>> I'm afraid layering socks doesn't work as I'm currently wearing a pair of normal cotton socks, a pair of fuzzy socks over them, and thick soled slippers but my feet are still cold.

Wool is very good but with all these layers and still cold, I doubt wool will fix it! 20% wool is going to be basically just a sock like any other. So IMHO no, that's definitely not going to make much of a difference.

I would consider whether your layers are too tight perhaps? One aspect of layers is trapped air. The air in the layers next to your skin becomes warm and the layers holds that warmth near you. If your layers are too tight they won't retain as much air, and so not as much warmth. So perhaps slightly larger socks are in order?

I would also suggest a pair of thin liner socks. Search for "polypropylene liner socks". I find using these as the first layer can add a lot of warmth. They are thin so they won't really increase the tightness of the outer layers.
[iu4iui0] (score 1, diepte 0) How about down booties / slippers?

https://rab.equipment/us/down-hut-slipper

https://featheredfriends.com/products/feathered-friends-down-booties
[iu4jd12] (score 1, diepte 0) I have slippers that keep my feet toasty warm (Bob’s by Sketchers).  They are sold in wide widths, too.  They have real shoe soles and are thick and lined with fuzzy fake fur, too.  In the winter I use these with my thickest socks and my feet stay toasty. If my legs are getting cold when just sitting, I put a blanket over my legs and feet (with slippers still on).  Making sure my feet go directly from warm bed to slippers and stay in something warm at all times helps.  It takes much longer to warm up, so not letting them cool off is essential to consistent comfort.
[iu4ojpv] (score 1, diepte 0) You can buy second hand wool sweaters and unravel them for wool. There are many online tutorials on how to do that. If you can find alpaca that’s even better (easier to unravel and warmer than wool) Keep in mind that the vast majority of breeds kept for wool aren’t good meat producers. You could also try to find someone local that has their animals as pets.
[iu4shti] (score 1, diepte 1 OP) I'd be more comfortable buying secondhand wool. I will probably do that. :)
[iu4vumb] (score 1, diepte 2) Look for tutorials before going to the store so you pick the right sweater construction and type of wool. Some are a nightmare to unravel. If the piece is dusty wash it before you unravel (learn from my mistakes)
[iu4wdrn] (score 1, diepte 3 OP) Thanks, will do.
[iu52w5g] (score 1, diepte 0) Silk socks also retain heat well if, like me, you are allergic to wool.
[iu5av0p] (score 1, diepte 0) You might want to skip the cotton socks and just do the fuzzy socks. Cotton can be cold and clammy. 

Also, I find if I drink hot tea my feet get warmer. Might be worth a try.
[iu5bmmw] (score 1, diepte 1 OP) I'll give both a go, thanks.
[iu5d7ug] (score 1, diepte 0) I also have Hashimoto’s and when I get cold, it goes bone deep. I can only warm up through a hot bath or using an electric blanket or my heavy minky blanket my mom made me. Usually once I get the rest of my body heated up, some of the really fuzzy socks work well for me.

If you’re still getting this cold, you should get your levels checked again. If your doctor isn’t running free T4 and T3 with your TSH, demand it. TSH is not a thyroid hormone but a pituitary one. It doesn’t show the whole picture. You can have a normal TSH and a low T4 which would make you symptomatic. T4 is best at the top of the range while T3 is best mid range. I feel best when my TSH is a 1-2. Remember, the lab’s normal is not always considered optimal and every person is different and reacts differently to meds. So go by your labs yes, but also go by how you feel.
[iu5fnhv] (score 1, diepte 1 OP) Thanks. I'm due for a check up soon, I'll definitely mention the cold feet&hands.
[iu6pzof] (score 1, diepte 2) This is me. The cold goes bone deep. Second hot baths. I’ve even used the blow dryer while the tub fills. My Family Dollar has cabin sox for $3 right now. If feet are really cold, I layer the cheap cabin sox over my wool ones.
[iu5xwl9] (score 1, diepte 0) Do you have high blood pressure? If not, you could try to add some rosemary oil to a cheap foot cream. 
Pure essential oil not scent oil but please don't waste money on overpriced and MLM brands. 
Rosemary oil is not safe for people with high blood pressure.
[iu6hxep] (score 1, diepte 0) All the sock tips - right size, right material, etc - are good, but I also have medical problems that led to cold feet and sometimes that's just not enough. The best tip I've found is a case of toe warmers when they're on sale/I have a coupon. Then I layer them sock, warmer, sock. All day warmth. Just make sure to use toe warmers - walking on them results in a lot or pressure/contact and less air to disperse the hear - using hand warmers instead can cause burns because they get hotter.
[iu6n0zu] (score 1, diepte 0) Try compression socks, it’ll improve blood flow to those areas. Another tip is you can make a foot soak in some warm water and some soap or Epsom salts. Though that is more of a temporary fix
[iu7zirz] (score 1, diepte 0) Just a thought warmer pants to help keep the blood warm well it heads to your feet.
[iu828wi] (score 1, diepte 1 OP) Way ahead of you :) Been layering pants for two weeks now and loving it!
[iu813ni] (score 1, diepte 0) Maybe reusable massage heat packs could work? I’ve had a set for a long time and they still work like new. You pop the little disk thing in the middle and it makes it get warm. When it goes cold you boil it and it goes back to gel ready to pop again. You could put them in your slippers! 

Even cheaper, you can sew a small cotton fabric pouch to fit in each slipper. Fill them with dry uncooked rice and sew them up. You can microwave these pouches for a 1-2 minutes and they stay warm for a long time. I have a large one I made that I use like a heating pad. 

Wishing you warm feet!
[iu82dlh] (score 1, diepte 1 OP) Thanks! I've seen those little heat packs but surprisingly don't own any, which is weird because I'm one cold creature. Maybe it's time to change that!

Can't do microwaveable heat packs though... No microwave. Although I am making some for others for Christmas.
[iu4q8bn] (score -1, diepte 6 OP) >By the time an egg layer stops laying eggs, they are so old that the meat is tough, and not profitable.

Yes, but what do you think happens to them when they stop laying eggs? Maybe not for meat, but they still get killed. Same with sheep, when they are no longer profitable for the farmer, bye bye. No one who raises animals for profit is going to keep them around once they stop being useful.
[iu4ruep] (score -4, diepte 8 OP) Yes, but the quality of the wool eventually decreases, and that happens way before the sheep are "old and sick". Sheep live up to 14 years, whereas their wool is too low quality to be sold at 5 or 6. And after that, the sheep gets slaughtered. Whether for meat or not, that is beside the point.

"Many shepherds care quite deeply about their flock" - I know a guy who raises cows. He genuinely thinks he loves them, he kisses them, gives them names, takes good care of them, calls them "my loves" and such, and when the time comes to slit their throat he probably tells himself that his cows were loved and taken care of, but that doesn't change the fact that a being dies that did not want to die.
[iu4c3on] (score -6, diepte 2 OP) So, as I mentioned in the post, I have yarn with 20 % wool. Would that be enough to keep me warm or would I need a higher wool content?

I'm not comfortable buying any new wool products (the yarn was bought on accident and I'd already opened it before I noticed) because, well, even if I'm not directly paying for the death of the animal, I'd still be giving my money for the sheep to eventually be killed.
[iu4irt6] (score -6, diepte 4 OP) I know, but eventually they get killed for meat.

